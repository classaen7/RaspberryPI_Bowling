#main Class

from Pin import Pin
from Zzangu import Zzangu
from Ball import Ball
from Joystick import Joystick
from ScoreDisplay import ScoreDisplay


import time
import random
from colorsys import hsv_to_rgb
import board
import numpy as np
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789

    
pin7 = Pin(97,91)
pin8 = Pin(113,91)
pin9 = Pin(127,91)
pin10 = Pin(143,91)

pin4 = Pin(105,93,pin7,pin8)
pin5 = Pin(120,93,pin8,pin9)
pin6 = Pin(135,93,pin9,pin10)

pin2 = Pin(112,95,pin4,pin5,pin8)
pin3 = Pin(128,95,pin5,pin6,pin9)

pin1 = Pin(120,97,pin2,pin3,pin5)
    
pin_list = [
    pin10,
    pin9,
    pin8,
    pin7,
    pin6,
    pin5,
    pin4,
    pin3,
    pin2,
    pin1
]

pin_dict = {
    pin1 : (213,27,221,35),
    
    pin2 : (208,19,216,27),
    pin3 : (218,19,226,27),
    
    pin4 : (204,11,212,19),
    pin5 : (213,11,221,19),
    pin6 : (222,11,230,19),
    
    pin7 : (200,3,208,11),
    pin8 : (209,3,217,11),
    pin9 : (218,3,226,11),
    pin10 : (226,3,234,11)
    
}

score_dict = {
    "1_1": ["False",(12,15)],
    "1_2": ["False",(37,15)],
    
    "2_1": ["False",(62,15)],
    "2_2": ["False",(87,15)],
    
    "3_1": ["False",(112,15)],
    "3_2": ["False",(137,15)],
    
    "4_1": ["False",(12,15)],
    "4_2": ["False",(37,15)],
    
    "5_1": ["False",(62,15)],
    "5_2": ["False",(87,15)],
    
    "6_1": ["False",(112,15)],
    "6_2": ["False",(137,15)],
}

def total_score(score_dict):
    score = 0
    for i in range(1,7):
        for j in range(1,3):
            if score_dict[str(i)+"_"+str(j)][0] != 'False':
                score += score_dict[str(i)+"_"+str(j)][0]
            else:
                break
    return score

stage_score = {
            "1": (27,32),
            "2": (73,32),
            "3": (121,32)   
        }


point = 0

def main():
    joystick = Joystick()
    score_disp = ScoreDisplay()
    my_image = Image.new("RGB", (240, 45))
    my_draw = ImageDraw.Draw(my_image)
   
    #게임 상태를 나타내는 코드 -> 상태에 따라 입력, 화면 출력, 상태 변환등 서로 다른 일을 수행함
    on_game = 0
    game_state = 0  
    
    game_stage =1 # 1~5
    game_turn = 1 # 1 or 2
    
    hit_position = "False"
    
    skill_chance = 1
    
    strike_flag = 0
    spare_flag = 0
    sleep_flag = 0
    
   # 잔상이 남지 않는 코드
    zzangu = Zzangu(120)
    
    ball = Ball(zzangu.xpos)
    
    #시작화면
    while True:
        if on_game == 0:
            fnt = ImageFont.truetype("/home/kau-esw/balling-game/font/RixInooAriDuri Regular.ttf", 27)
            temp_img = Image.new("RGB",(240,240),"#3cd275")
            draw = ImageDraw.Draw(temp_img)
            draw.text((13,25),"Zzangu's",font=fnt,fill="red")
            draw.text((23,55),"Balling Game",font=fnt,fill="yellow")
            fnt = ImageFont.truetype("/home/kau-esw/balling-game/font/RixInooAriDuri Regular.ttf", 17)
            draw.ellipse((110,130,133,151),outline="white")
            draw.text((50,130),"Press  A  Button",font=fnt)
            draw.text((80,160),"To Start",font=fnt)
            back = Image.open('/home/kau-esw/balling-game/esw_pic/normback.png')
            back.paste(temp_img, (0, 0))
            joystick.disp.image(back)
                
            if not joystick.button_A.value:
                on_game += 1
            
        elif on_game == 1:    
            #game_state == 0 는 짱구에 대한 커맨드를 받는 상태 -> 공을 어떻게, 어디로, 어디서 던질지에 대한 커맨드를 받음
            if game_state == 0:
                command = None
                # 위 커맨드 = 짱구를 움직일 수 있게 해줌 (default는 짱구가 움직일 수 있음)
                if not joystick.button_U.value:  # up pressed
                    zzangu.move_state ="ON"

                # 아래 커맨드 = 짱구를 고정시켜 공을 던질 수 있게 해줌 (고정을 시켜 화면에 ON에 점등이 되는걸 확인 할 수 있음)
                elif not joystick.button_D.value:  # down pressed
                    zzangu.move_state ="OFF"

                # 좌, 우 커맨드 = 짱구가 움직일 수 있는 상태 일 때 짱구를 좌우로 움직일 수 있게 함
                elif not joystick.button_L.value:  # left pressed
                    command = 'left_pressed'

                elif not joystick.button_R.value:  # right pressed
                    command = 'right_pressed'
                    
                #짱구가 고정이 되어 공을 던질 수 있게 되면..
                if zzangu.move_state=="OFF":
                    
                    # 여러 커맨드를 통해 어떻게 공을 던질지를 커맨드를 통해 선택함
                    """
                    커맨드 설명 - 던지는 방법
                    1. A : straight shoot
                    2. <- + A : left spin shoot
                    3. -> + A : right spin shoot
                    4. B : Skill shoot
                    """
                    if not joystick.button_A.value:
                        if not joystick.button_L.value:
                            # <- + A : left spin shoot
                            ball.spin="LEFT"
                        
                        elif not joystick.button_R.value:
                            # -> + A : left spin shoot
                            ball.spin="RIGHT"
                        
                        game_state += 1
                        zzangu.state='ON'
                        point = 0
                        ball.state = "ON"
                        
                        
                    # 스킬 슛에 대한 조건문
                    elif not joystick.button_B.value and skill_chance > 0:
                        ball.state = "SKILL"
                        game_state += 1
                        zzangu.state='ON'
                        point = 0
                        skill_chance -= 1
                        
                    else:
                        command = None
            
            
            #game_state == 1 는 공을 던지는 순간에 대한 설정들 -> 공이 어디로 굴러가야 하는지, 그리기에 대한 설정 등..
            elif game_state == 1:
                ball.xpos = zzangu.xpos
                ball.set_roll()
                zzangu.state='AFT'
                game_state +=1


            #game_state == 2는 공이 굴러가는 상태 -> 공이 굴러가면서 해야할 처리들을 담당함
            elif game_state == 2:
                if ball.ypos <= 91:
                    hit_position = ball.xpos
                
                # 공이 다 굴러 갔을 때에 대한 처리
                if ball.ypos <= 85:
                    
                    #턴 종료시 점수 합산
                    for pin in pin_list:
                        if pin.state == "OFF":
                            point+=1
                    
                    # 점수를 받는 딕셔너리에 점수 저장
                    if str(game_stage)+"_"+str(game_turn) in score_dict and score_dict[str(game_stage)+"_"+str(game_turn)][0] == 'False':
                        score_dict[str(game_stage)+"_"+str(game_turn)][0] = point
                    
                    #Strike or Spare일 시 flag를 통해 전달
                    if point == 10:
                        if game_turn == 1:
                            strike_flag += 1
                                
                            for pin in pin_list:
                                pin.state = "ON"
                                pin.is_hit_back='False'
                        
                        elif game_turn == 2:
                            spare_flag +=1
                    
                    
                    #다음 단계로 이동
                    if game_turn == 1:
                        game_turn = 2
                    elif game_turn == 2:
                        game_turn = 1
                        game_stage += 1
                        
                        #1turn일 시 핀 다시 세우기
                                    
                        for pin in pin_list:
                            pin.state = "ON"
                            pin.is_hit_back='False'
                            
                    #모든 스테이지가 종료 되면 
                    if game_stage == 7:
                        on_game += 1
                    
                    if game_stage==4 and game_turn==1:
                        sleep_flag = 1
                    if game_stage==7 and game_turn==1:
                        sleep_flag = 1
                    
                    game_state = 0
                    ball.state="OFF"
                    ball.ypos = 210
                    ball.spin ="OFF"
                    
                    zzangu.state="BEF"
                    zzangu.move_state="ON"
                    
                    #핀이 넘어졌는지 확인 -> 넘어진 핀에 대하여 아예 사라지게 끔
                    for pin in pin_list:
                        pin.is_fall()
                
                # 공이 굴러가는 동안에 대한 처리
                ball.roll()
                
                #공이 굴러가면서 핀에 부딪히거나 핀 끼리 부딪혀 넘어지는 경우 확인
                for pin in pin_list:
                    pin.collide_ball(ball)
                    pin.hit_back()
                    
                
                
                    
                
                
            
            #짱구의 좌우 이동 (고정된 상태가 아닐때)
            if zzangu.move_state == "ON":
                zzangu.move(command)
            
            #짱구, 볼링공, 핀, 배경에 대한 그리기
            #배경
            back = Image.open('/home/kau-esw/balling-game/esw_pic/backgroundbef.png')
            #핀 - 핀의 상태에 따른 그림
            for pin in pin_list:
                pin.darw_pin(back)
            
            #공 - game_state가 2일때, 즉 공이 굴러갈때만 공을 그림
            if game_state == 2:
                ball.draw_ball(back)  
            
            #짱구 - skill을 사용하는게 아니라면 짱구를 그림 ( 스킬을 사용한다면 짱구가 직접 굴러가기 때문에 그리지 않음 )
            if ball.state != "SKILL":
                zzangu.draw_zz(back)

            
            
            # 점수판에 대한 이미지 처리
            score_img = Image.new('RGBA', (240,46), "#7fae68")
            draw = ImageDraw.Draw(score_img)
            
            
            
            if sleep_flag == 1:
                score_disp.bg(draw,game_stage-1<=3)
                score_disp.score(score_dict,stage_score,draw,game_stage-1<=3)    
            else:
                score_disp.bg(draw,game_stage<=3)
                score_disp.score(score_dict,stage_score,draw,game_stage<=3)
            
            score_disp.state(zzangu.move_state,skill_chance,draw)
            score_disp.pin(pin_list,pin_dict,draw)
            
            if hit_position != "False":
                score_disp.point(hit_position,draw)
                
            # 스트라이크 or 스페어에 따른 점수판에 문자 출력 1
            if strike_flag == 1:
                score_disp.strike_1(draw)
                
            elif spare_flag == 1:
                score_disp.spare_1(draw)
                
            back.paste(score_img, (0, 0))
            joystick.disp.image(back)
            
            
            # 스트라이크 or 스페어에 따른 점수판에 문자 출력 2
            if strike_flag == 1:
                score_disp.strike_2(draw,back,joystick,score_img)
                strike_flag = 0
                
            elif spare_flag == 1:
                score_disp.spare_2(draw,back,joystick,score_img)
                spare_flag = 0
            
            if sleep_flag == 1:
                time.sleep(1)
                sleep_flag -= 1
            

                
        #최종 점수표
        elif on_game==2:
            fnt = ImageFont.truetype("/home/kau-esw/balling-game/font/RixInooAriDuri Regular.ttf", 27)
            temp_img = Image.new("RGB",(240,240),"#3cd275")
            draw = ImageDraw.Draw(temp_img)
            draw.text((13,40),"Total Score is",font=fnt,fill="white")
            fnt = ImageFont.truetype("/home/kau-esw/balling-game/font/RixInooAriDuri Regular.ttf", 40)
            draw.text((95,120),str(total_score(score_dict)),font=fnt,fill="yellow")
            back = Image.open('/home/kau-esw/balling-game/esw_pic/normback.png')
            back.paste(temp_img, (0, 0))
            joystick.disp.image(back)
                
            if not joystick.button_A.value:
                #점수 등 여러 값들에 대한 초기화
                for i in range(1,7):
                    for j in range(1,3):
                        score_dict[str(i)+"_"+str(j)][0] = 'False'
                on_game = 0
                game_stage = 1
                game_turn = 1
                skill_chance = 1
    
    

if __name__ == '__main__':
    main()