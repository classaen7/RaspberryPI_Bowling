
from PIL import ImageFont
import time

class ScoreDisplay:
    def bg(self,draw,stage):
        draw.rectangle((3,3,153,43),outline="#FFFFFF",fill="#61904a")
        
        draw.polygon([ (3,13), (153,13)],outline="#FFFFFF")
        draw.polygon([ (53,3), (53,42)],outline="#FFFFFF")
        draw.polygon([ (103,3), (103,42)],outline="#FFFFFF")
        draw.polygon([ (3,33), (153,33)],outline="#FFFFFF")
        
        draw.polygon([ (28,13), (28,33)],outline="#FFFFFF")
        draw.polygon([ (78,13), (78,33)],outline="#FFFFFF")
        draw.polygon([ (128,13), (128,33)],outline="#FFFFFF")
        
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 9)
        
        if stage == 1:
            a, b, c ="1", "2", "3"
        elif stage == 0:
            a, b, c ="4", "5", "6"
            
        draw.text((25,3),a,font=fnt)
        draw.text((75,3),b,font=fnt)
        draw.text((125,3),c,font=fnt)
        
        
    def score(self,score_dict,stage_score,draw,stage):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 15)
        if stage == 1:
            g = 0
        else:
            g = 3
        for i in range(1,4):
            for j in range(1,3):
                if str(i+g)+"_"+str(j) in score_dict and score_dict[str(i+g)+"_"+str(j)][0] != 'False':
                    score = str(score_dict[str(i+g)+"_"+str(j)][0])
                    if score == "10":
                        score ="-"
                    draw.text(score_dict[str(i+g)+"_"+str(j)][1],score,font=fnt)
        
        
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 10)
        for i in range(1,4):
            if score_dict[str(i+g)+"_"+"1"][0] != 'False' and score_dict[str(i+g)+"_"+"2"][0] != 'False':
                if score_dict[str(i+g)+"_"+"1"][0] == 10:
                    score = score_dict[str(i+g)+"_"+"2"][0] + 10
                    draw.text(stage_score[str(i)], str(score),font=fnt)        
                else:
                    draw.text(stage_score[str(i)], str(score_dict[str(i)+"_"+"2"][0]),font=fnt)
                
                
    def state(self,zz,sk,draw):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 11)
        if zz == "ON":
            move_color = "yellow"
            on_color = "#FFFFFF"
        else:
            move_color = "#FFFFFF"
            on_color = "yellow"
        draw.text((157,3),"MOVE",font=fnt,fill=move_color)
        
        draw.text((157,17),"ON",font=fnt,fill=on_color)
        
        
        
        #score_disp(skill_chance,draw)
        if sk == 1:
            skill_color = "green"
        else:
            skill_color = "#FFFFFF"
            
        draw.text((157,30),"SKILL",font=fnt,fill=skill_color)
        
    
    def pin(self,pin_list,pin_dict,draw):
        draw.polygon([(195,0),(195,45),(196,45),(196,0)],outline="brown",fill="brown")
        for pin in pin_list:
            if pin.state =="ON":
                fillcolor = "#FFFFFF"
            else:
                fillcolor = "green"

            draw.ellipse(pin_dict[pin],fill=fillcolor)
            
            
    def point(self,hit_position,draw):
        #200~234 = 34
        #90~150 = 60
        ratio = 34/60
        poly_xpos = (hit_position-90)*ratio+200
        
        fill_clr = "brown"
        if poly_xpos <= 203:
            poly_xpos = 203
        elif poly_xpos >= 237:
            poly_xpos = 237
        draw.polygon([(poly_xpos-3,45),(poly_xpos+3,45),(poly_xpos+3,40),(poly_xpos+5,40),(poly_xpos,35)
                      ,(poly_xpos-5,40),(poly_xpos-3,40)],outline="#1e5f76",fill="#43abff")
            
            
            
    def spare_1(self,draw):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 35)
        draw.rectangle((0,0,240,43),outline="black",fill="black")
        draw.text((50,0),"SPARE",font=fnt,fill="red")
        
    def spare_2(self,draw,back,joystick,score_img):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 35)
        time.sleep(0.5)
        draw.rectangle((0,0,240,43),outline="black",fill="black")
        draw.text((50,0),"SPARE",font=fnt,fill="yellow")
        back.paste(score_img, (0, 0))
    
        joystick.disp.image(back)
        time.sleep(0.5)
        
            
            
            
    def strike_1(self,draw):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 35)
        draw.rectangle((0,0,240,43),outline="black",fill="black")
        draw.text((50,0),"STRIKE",font=fnt,fill="red")
    
    def strike_2(self,draw,back,joystick,score_img):
        fnt = ImageFont.truetype("./Assets/Default_Font.ttf", 35)
        time.sleep(0.5)
        draw.rectangle((0,0,240,43),outline="black",fill="black")
        draw.text((50,0),"STRIKE",font=fnt,fill="yellow")
        back.paste(score_img, (0, 0))
    
        joystick.disp.image(back)
        time.sleep(0.5)
        