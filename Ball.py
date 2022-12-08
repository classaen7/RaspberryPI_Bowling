#Ball Class

from PIL import Image, ImageDraw, ImageFont

class Ball:
    def __init__(self,zz_xpos):
        self.xpos = zz_xpos
        self.ypos = 210
        
        self.grad = abs(self.xpos - 120)
        self.spin = "OFF"
        self.state = "OFF"  # OFF / ON / SPIN / SKILL
        self.grad=0
        self.xplus = 0
        self.yplus = 0
        self.radius = 7
        
        
    def draw_ball(self,bg):
        if self.state == "ON" or self.state=="FALL":
            if self.ypos > 180:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/front_ball.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-12,int(self.ypos)-12),ball_img)
            elif self.ypos > 150:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/mid_ball.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-11,int(self.ypos)-11),ball_img)
            elif self.ypos > 110:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/mid_ball2.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-11,int(self.ypos)-11),ball_img)
            else:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/back_ball.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-10,int(self.ypos)-10),ball_img)
            #ypos에 따라 공의 크기 바꾸기 
            
            
        elif self.state == "SKILL":
            if self.ypos > 180:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/zzzanguskill1.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-50,int(self.ypos)-26),ball_img)
                
            elif self.ypos >150:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/zzzanguskill2.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-50,int(self.ypos)-26),ball_img)
            elif self.ypos >110:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/zzzanguskill1.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-50,int(self.ypos)-26),ball_img)
            else:
                ball_img = Image.open('/home/kau-esw/balling-game/esw_pic/zzzanguskill2.png').convert('RGBA')
                bg.paste(ball_img,(int(self.xpos)-50,int(self.ypos)-26),ball_img)
                self.radius = 6
                
                
            
            
            
    def roll(self):
        
        
        #핀과 근접할 시 좀더 세부적으로 좌표 관리 for 충돌하는지 확인
        if self.ypos <= 101:
            if self.spin == "RIGHT":
                self.xpos -= 3
            elif self.spin == "LEFT":
                self.xpos += 3

            self.ypos -= 3

        
        #볼링공이 빠져나가는 것에 대한 조건문 -> 빠져나가면 핀을 넘어뜨릴 수 없음
        if self.state != "FALL" and self.ypos <= (-3)*self.xpos+ 360:
            self.state="FALL"
            self.xpos -= 7
            
        elif self.state != "FALL" and self.ypos <= 3*self.xpos - 360:
            self.state="FALL"
            self.xpos += 7


                
        if self.state == "FALL":
            if self.xpos < 120:
                self.xpos += 3
                self.ypos -= 9
            else:
                self.xpos -= 3
                self.ypos -= 9
        
        #빠지지 않을 시에 굴러가게 함
        else:   #제대로 굴러가는 경우
            if self.xpos < 120 :
                # 커브를 줄 시 기존의 이동 보다 더 각을 크게 이동
                self.xpos += self.xplus

            else:
                self.xpos -= self.xplus    
            self.ypos -= self.yplus
            
            if self.spin == "RIGHT":
                    if self.ypos > 150:
                        self.xpos += 2
                    else:
                        self.xpos -=3
                
            elif self.spin == "LEFT":
                if self.ypos > 150:
                    self.xpos -= 2
                else:
                    self.xpos += 3
    
    
    def set_roll(self):
        if self.state == "SKILL":
            self.radius = 30
            self.xpos = 120
            self.xplus = 0
            self.yplus = 5
            
            
        else:    
            height = 120
            target = abs(self.xpos-120) * (80/170)
            width = abs(self.xpos-120)-target
            
            if width == 0:
                width = 1
            self.grad = height/width
            self.xplus = width/20
            self.yplus = self.xplus * self.grad
        
        
    