#Zzangu class

from PIL import Image
   
class Zzangu:
    def __init__(self, pos):
        self.xpos = pos
        self.state = 'BEF'
        self.move_state = "ON"
        
        
    def move(self, command = None):
        if self.move_state == "ON":
            if command == 'left_pressed':
                if self.xpos >= 45:
                    self.xpos -= 3
                

            elif command == 'right_pressed':
                if self.xpos <= 192:
                    self.xpos += 3
            

            
        
    def draw_zz(self,bg):
        if self.state == 'BEF':
            x = self.xpos-25
            y=175
            
            img = Image.open('/home/kau-esw/balling-game/Assets/zzangu1step.png').convert('RGBA')
            bg.paste(img,(x,y),img)
            
        elif self.state =='ON':
            x = self.xpos-30
            y=190
            
            img = Image.open('/home/kau-esw/balling-game/Assets/zzangu2step.png').convert('RGBA')
            bg.paste(img,(x,y),img)
            
        elif self.state =='AFT':
            x = self.xpos-30
            y= 185
            
            img = Image.open('/home/kau-esw/balling-game/Assets/zzangu3step.png').convert('RGBA')
            bg.paste(img,(x,y),img)
            
            

        