#Pin Class
import math
from PIL import Image

class Pin:
    def __init__(self,xpos,ypos,lb=None,rb=None,mb=None):
        self.xpos = xpos
        self.ypos = ypos
        self.state = "ON" # ON / OFF / Left_fall / Right_fall / Mid_fall / ball_hit / pin_hit
        self.radius = 3.5
        
        self.left_back = lb
        self.right_back = rb
        self.mid_back = mb
        
        self.is_hit_by_pin= "False" #앞의 핀에게 맞았는지 확인하는 변수
        
    
    def darw_pin(self,bg):
        
        if self.state == "ON":
            a = self.xpos - 5
            b = self.ypos - 16    
            img = Image.open('/home/kau-esw/balling-game/Assets/pin1.png').convert('RGBA')
            bg.paste(img,(a,b),img)
        
        elif self.state =="Left_fall":
            a = self.xpos - 10
            b = self.ypos - 11
            img = Image.open('/home/kau-esw/balling-game/Assets/pin2.png').convert('RGBA')
            bg.paste(img,(a,b),img)
            self.state="OFF"
            
            
        elif self.state == "Right_fall" or self.state == "Mid_fall":
            a = self.xpos - 5
            b = self.ypos - 11
            img = Image.open('/home/kau-esw/balling-game/Assets/pin3.png').convert('RGBA')
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
                
                if std_dist-1 <= xdiff <= std_dist:
                    if self.xpos < ball.xpos:
                        self.state = "Left_fall"
                    else:
                        self.state = "Right_fall"
                #볼링공이 볼링핀을 넘어 트리는데 그 핀이 뒤에 핀을 넘어뜨릴수 있는 경우
                elif 2.5 <= xdiff < std_dist-1:
                    if self.xpos > ball.xpos:
                        self.state = "Left_fall"
                        if self.left_back != None:
                            self.left_back.is_hit_by_pin = self.state
                    else:
                        self.state = "Right_fall"
                        if self.right_back != None:
                            self.right_back.is_hit_by_pin = self.state
                elif 1 < xdiff < 2.5:
                    if self.xpos < ball.xpos:
                        self.state = "Left_fall"
                    else:
                        self.state = "Right_fall"
                #볼링공이 볼링핀을 정확히 가운데서 치는 경우
                else:
                    self.state = "Mid_fall"
                    if self.mid_back != None:
                        self.mid_back.is_hit_by_pin = self.state
                   
    
                    
    
    #볼링공이 다 지나간 뒤에 볼링핀들이 넘어져있는지 확인하는 코드
    def is_fall(self):
        if self.state=="Left_fall" or self.state=="Right_fall" or self.state=="Mide_fall":
            self.state = "OFF"


    def hit_by_pin(self):
        if self.is_hit_by_pin != "False":
            if self.state == "ON":
                if self.is_hit_by_pin == "Left_fall":
                    self.state = "Left_fall"
                    if self.left_back!=None:
                        self.left_back.is_hit_by_pin = self.state
                    
                elif self.is_hit_by_pin == "Right_fall":
                    self.state = "Right_fall"
                    if self.right_back!=None:
                        self.right_back.is_hit_by_pin = self.state
                    
                elif self.is_hit_by_pin == "Mid_fall":
                    self.state = "Mid_fall"
                    if self.mid_back!=None:
                        self.mid_back.is_hit_by_pin = self.state
                    
                
    
    
        
            
        
        
            
        
            


    

       