#Pin Class

import math
from PIL import Image, ImageDraw, ImageFont
import random

class Pin:
    def __init__(self,xpos,ypos,lb=None,rb=None,mb=None):
        self.xpos = xpos
        self.ypos = ypos
        self.state = "ON" # ON / OFF / Left_fall / Right_fall / Mid_fall / ball_hit / pin_hit
        self.radius = 3.5
        
        self.left_back = lb
        self.right_back = rb
        self.mid_back = mb
        
        self.is_hit_back= "False"
        
    
    def darw_pin(self,bg):
        
        if self.state == "ON":
            a = self.xpos - 5
            b = self.ypos - 16    
            img = Image.open('/home/kau-esw/balling-game/esw_pic/pin1.png').convert('RGBA')
            bg.paste(img,(a,b),img)
        
        elif self.state =="Left_fall":
            a = self.xpos - 10
            b = self.ypos - 11
            img = Image.open('/home/kau-esw/balling-game/esw_pic/pin2.png').convert('RGBA')
            bg.paste(img,(a,b),img)
            self.state="OFF"
            
            
        elif self.state == "Right_fall" or self.state == "Mid_fall":
            a = self.xpos - 5
            b = self.ypos - 11
            img = Image.open('/home/kau-esw/balling-game/esw_pic/pin3.png').convert('RGBA')
            bg.paste(img,(a,b),img)
            self.state="OFF"
    
        
    
    def collide_ball(self,ball):
        if ball.state != "OFF" and self.state=="ON":
            x = self.xpos - ball.xpos
            y = self.ypos - ball.ypos
            
            dist = math.sqrt((x * x) + (y * y))
            
            if dist < ball.radius + self.radius and self.state=="ON":
                xdiff = abs(x)
                std_dist = self.radius+ball.radius
                #볼링공이 볼링핀이 끝부분을 살짝 치는 경우 -> 뒤에 핀을 넘어 뜨리지 않음
                
                if std_dist-2 <= xdiff <= std_dist:
                    if self.xpos < ball.xpos:
                        self.state = "Left_fall"
                    else:
                        self.state = "Right_fall"
                #볼링공이 볼링핀을 넘어 트리는데 그 핀이 뒤에 핀을 넘어뜨릴수 있는 경우
                elif 3 <= xdiff < std_dist-2:
                    self.is_hit_back = "ball_hit"
                    if self.xpos > ball.xpos:
                        self.state = "Left_fall"
                    else:
                        self.state = "Right_fall"
                elif 1 < xdiff < 3:
                    if self.xpos < ball.xpos:
                        self.state = "Left_fall"
                    else:
                        self.state = "Right_fall"
                #볼링공이 볼링핀을 정확히 가운데서 치는 경우
                else:
                    self.is_hit_back = "ball_hit"
                    self.state = "Mid_fall"
                   
    
                    
    
    #볼링공이 다 지나간 뒤에 볼링핀들이 넘어져있는지 확인하는 코드
    def is_fall(self):
        if self.state=="Left_fall" or self.state=="Right_fall" or self.state=="Mide_fall":
            self.state = "OFF"


    def hit_back(self):
        if self.is_hit_back == "True":
            if self.state == "Left_fall" and self.left_back != None:
                self.left_back.state = "Left_fall"
                self.left_back.is_hit_back = "True"
            elif self.state == "Right_fall" and self.right_back != None:
                self.right_back.state = "Right_fall"
                self.right_back.is_hit_back = "True"
            elif self.state == "Mid_fall" and self.mid_back != None:
                self.mid_back.state = "Mid_fall"
                self.mid_back.is_hit_back = "True"
    
    
        
            
        
        
            
        
            


    

       