from PIL import Image
import pyglet
import os
from pyglet import image
from pyglet import graphics
from pyglet import text
from pyglet.window import key
import random
import csv
import string

class CustomSprite(pyglet.sprite.Sprite):
    def __init__(self, texture_file, x=100, y=100, batch=None, group=None):
        # Must load texture beforeinit class:sprite

        self.texture = pyglet.image.load(texture_file)
        # self.label = pyglet.text.Label('This is BOBBY THE PIRATE: KILL DAVE', font_name='Times New Roman', font_size=36, x=window.W / 2, y=window.H / 2, anchor_x='center', anchor_y='center')
        super(CustomSprite, self).__init__(self.texture, batch=batch, group=group)
        self.x = x
        self.y = y

class Main(pyglet.window.Window):

    def __init__(self):
        super(Main, self).__init__(400, 450, fullscreen = False)# set screen size
        self.x = 0
        self.y = 0

        self.sprites = {} # declare use of batch 'sprites'
        self.batch = {'game' : pyglet.graphics.Batch()} #Init batch 
        self.subgroups = {'bg_0' : pyglet.graphics.OrderedGroup(0), 'bg_1' : pyglet.graphics.OrderedGroup(1), 'bg_2' : pyglet.graphics.OrderedGroup(2), 'walls' : pyglet.graphics.OrderedGroup(3), 'chars' : pyglet.graphics.OrderedGroup(4)}
        # Batch tells graphics what is going on
        
        
        # SPITES FOR CHARACTERS
        self.sprites['dave'] = CustomSprite('images/dave_the_devil.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['lil_win'] = CustomSprite('images/winsor_0.png', batch=self.batch['game'], group=self.subgroups['chars'])
        
        avo = pyglet.image.load_animation('images/image.gif')
        self.sprites['avo'] = pyglet.sprite.Sprite(avo, batch=self.batch['game'], group=self.subgroups['bg_0'])
        
        # SPRITES FOR OBSTICALS
        self.sprites['wall1'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step1'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step2'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step3'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step4'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step5'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step6'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step7'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step8'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step9'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step10'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step11'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step12'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step13'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        
        
        #STEPS/WALLS Co - Ords
        self.sprites['avo'].x = 0
        self.sprites['avo'].y = 0
        self.sprites['lil_win'].x = 250
        self.sprites['lil_win'].y = 350
        self.sprites['dave'].x = 150
        self.sprites['dave'].y = 350
        
        self.sprites['wall1'].x = 200
        self.sprites['wall1'].y = 0
        self.sprites['step1'].x = 250
        self.sprites['step1'].y = 0
        self.sprites['step2'].x = 300
        self.sprites['step2'].y = 0
        self.sprites['step3'].x = 350
        self.sprites['step3'].y = 0
        self.sprites['step4'].x = 250
        self.sprites['step4'].y = 50
        self.sprites['step5'].x = 0
        self.sprites['step5'].y = 100
        self.sprites['step6'].x = 50
        self.sprites['step6'].y = 100
        self.sprites['step7'].x = 100
        self.sprites['step7'].y = 100
        self.sprites['step8'].x = 300
        self.sprites['step8'].y = 150
        self.sprites['step9'].x = 350
        self.sprites['step9'].y = 150
        self.sprites['step10'].x = 250
        self.sprites['step10'].y = 300
        self.sprites['step11'].x = 150
        self.sprites['step11'].y = 200
        self.sprites['step12'].x = 100
        self.sprites['step12'].y = 200
        self.sprites['step13'].x = 300
        self.sprites['step13'].y = 300


    def collision(self):
        #USE GRID_SET to set object_collision
        self.set_x = Main.grid_set_x(self)
        self.set_y = Main.grid_set_y(self)
        # state = 1
        
        # y = (((state & 1) * 1) + ((state & 2) * -1)) * 0.1 * 50
        
        if self.set_y == '0':
            return 0
        
        if self.set_x == 'd' and self.set_y == '1':
            return 1
        if self.set_x == 'e' and self.set_y == '2':
            return 2
        if self.set_x == 'f' and self.set_y == '2':
            return 3
        if self.set_x == 'g' and self.set_y == '1':
            return 4
        if self.set_x == 'a' and self.set_y == '3':
            return 5
        if self.set_x == 'b' and self.set_y == '3':
            return 6
        if self.set_x == 'c' and self.set_y == '3':
            return 7
        if self.set_x == 'f' and self.set_y == '4':
            return 8
        if self.set_x == 'f' and self.set_y == '7':
            return 9
        if self.set_x == 'g' and self.set_y == '4':
            return 10
        if self.set_x == 'e' and self.set_y == '7':
            return 11
        if self.set_x == 'c' and self.set_y == '5':
            return 12
        if self.set_x == 'b' and self.set_y == '5':
            return 10

    def grid_set_x(self):
        #make "BLOCKS"
        #checks X Co_Ords
        if self.sprites[self.name].x in range(0, 50):
            return 'a'
        if self.sprites[self.name].x in range(50, 100):
            return 'b'
        if self.sprites[self.name].x in range(100, 150):
            return 'c'
        if self.sprites[self.name].x in range(150, 200):
            return 'd'
        if self.sprites[self.name].x in range(200, 250):
            return 'e'
        if self.sprites[self.name].x in range(250, 300):
            return 'f'
        if self.sprites[self.name].x in range(300, 350):
            return 'g'
        if self.sprites[self.name].x in range(350, 400):
            return 'h'
        if self.sprites[self.name].x in range(400, 450):
            return 'i'
        
    def grid_set_y(self):
        #check Y Co_Ords
        if self.sprites[self.name].y == 0:
            return '0'
        if self.sprites[self.name].y in range(0, 50):
            return '1'
        if self.sprites[self.name].y in range(50, 100):
            return '2'
        if self.sprites[self.name].y in range(50, 150):
            return '3'
        if self.sprites[self.name].y in range(150, 200):
            return '4'
        if self.sprites[self.name].y in range(200, 250):
            return '5'
        if self.sprites[self.name].y in range(250, 300):
            return '6'
        if self.sprites[self.name].y in range(300, 350):
            return '7'
        if self.sprites[self.name].y in range(350, 400):
            return '8'

 
    def run(self, name): # Run render while bobby is alive
        self.name = name
        self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'])
        self.sprites[self.name].x = 10
        self.sprites[self.name].y = 10
        dude = str(self.name)
        self.sprites['name'] = pyglet.text.Label("PLAYER: " + dude, batch=self.batch['game'], group=self.subgroups['bg_1'], color=(2, 2, 2, 255) ,x=0, y=380)

        self.b_alive = 1000
        self.sprites[self.b_alive] = pyglet.text.Label("HEALTH: ",batch=self.batch['game'], group=self.subgroups['chars'], color=(2, 2, 2, 255), x=0, y=400)

# import time
        # clk = time.clock()
        # interval = clk.real
        while self.b_alive >= 1:
            Main.dave(self, self.b_alive)

            if self.sprites[self.name].x in range(self.sprites['lil_win'].x, self.sprites['lil_win'].x + 50) and self.sprites[self.name].y in range(self.sprites['lil_win'].y, self.sprites['lil_win'].y + 50):
                self.sprites['WINNER'] = pyglet.text.Label("YOU SAVED CHOW_BOT: LEVEL ONE CLEARED", batch=self.batch['game'], group=self.subgroups['walls'], color=(2, 2, 2, 255), x=0, y=250)
                self.sprites['lil_win'].x = self.sprites[self.name].x + 20
                self.sprites['lil_win'].y = self.sprites[self.name].y

            self.grav = Main.collision(self)
            if self.sprites[self.name].y in range(-50, 2):
                self.sprites[self.name].y += 1
            if self.grav in range(0, 19):
                self.sprites[self.name].y += 1
            else:
                self.sprites[self.name].y -= 2
            # if clk.real - interval > 1000/30:
                # interval = clk.real
                # pass # do update
            self.render()
            event = self.dispatch_events()
        

    def on_draw(self):
        self.sprites[self.b_alive].draw()
        self.render()
        self.label.draw()

    def on_close(self):
        self.b_alive = 0

    def render(self):
        self.clear() # keep screen from duplicating on movement
        for batch_name, batch_object in self.batch.items():
            batch_object.draw() # Draw the batch files on screen
        self.flip() #UPDATES THE SCREEN -FlipIt-
        
    def on_key_press(self, symbol, modifiers): #takes key stroke as ARGUMENTS

        self.block = Main.collision(self)
        if symbol == key.ESCAPE:
            print('EXITED GAME')
            self.b_alive = 0
           
        try:
            if symbol == key.R:
                print("TRYING_R")
                self.sprites[self.name] = CustomSprite('images/winsor_jump.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y) 
            else:
                self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
        except:
            pass
        try:
            if self.block in range(0, 19) and symbol == key.SPACE:
                print("POWER JUMP")
                self.sprites[self.name].y += 50
                self.sprites[self.name].y += 50
                self.sprites[self.name] = CustomSprite('images/winsor_jump.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
            else:
                self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
                
        except:
            pass
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].x -= 1
            elif self.block != True and symbol == key.RIGHT:
                self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
                self.sprites[self.name].x += 10 #UPDATES BATCH DATA -> For Graphics 
                self.sprites[sel.f.name].y += 1
                print("RIGHT ->")
        except:
            pass
        try:
            if self.block != True and symbol == key.UP:
                self.sprites[self.name].y += 5
                print("UP ^")
            # elif self.block in range(0, 19):
                # self.sprites[self.name].y -= 1
        except:
            pass
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].y += 1
            elif self.block != True and symbol == key.DOWN:
                self.sprites[self.name].y -= 5
                print("DOWN v")
        except:
            pass
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].x += 1
            elif self.block != True and symbol == key.LEFT:
                self.sprites[self.name] = CustomSprite('images/winsor_1L.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
                self.sprites[self.name].x -= 10
                self.sprites[self.name].y += 2
                print("LEFT <-")
        except:
            pass
                # FIX KEY_ERROR HANDLING //
                
    def on_key_release(self, symbol, modifiers): #takes key stroke as ARGUMENTS
        
        self.block = Main.collision(self)
        if self.block == True:
            print("Rock...")
          
        try:
            if self.block in range(0, 19) and symbol == key.SPACE:
                print("POWER JUMP")
                self.sprites[self.name].y += 50
                # self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'])
        except:
            pass
        if symbol == key.ESCAPE:
            print('EXITED GAME')
            self.b_alive = 0
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].x -= 1
            if self.block != True and symbol == key.RIGHT:
                self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
                self.sprites[self.name].x += 10 #UPDATES BATCH DATA -> For Graphics 
                print("RIGHT ->")
        except:
            pass
        try:
            if self.block in range(0, 19):
                self.sprites.y -= 1
            elif self.block != True and symbol == key.UP:
                self.sprites[self.name].y += 5
                print("UP ^")
        except:
            pass
                
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].y += 1
            elif self.block != True and symbol == key.DOWN:
                self.sprites[self.name].y -= 5
                print("DOWN v")
        except:
            pass
        try:
            if self.block in range(0, 19):
                self.sprites[self.name].y -= 1
            elif self.block != True and symbol == key.LEFT:
                self.sprites[self.name] = CustomSprite('images/winsor_1L.png', batch=self.batch['game'], group=self.subgroups['chars'], x=self.sprites[self.name].x, y=self.sprites[self.name].y)
                self.sprites[self.name].y += 10
                print("LEFT <-")
        except:
            pass
        
            
    def dave(self, health):
        self.move = Main.collision(self)
        self.b_alive = health
        if self.sprites['dave'].y in range(200, 400):
            self.sprites['dave'].y -= 1
        
        if self.sprites['dave'].y in range(0, 200):
            self.sprites['dave'].x += 1
            if self.sprites['dave'].x in range(350, 400):
                self.sprites['dave'].y += 1
                self.sprites['dave'].x -= 100

        if self.sprites[self.name].x in range(self.sprites['dave'].x, self.sprites['dave'].x + 10) and self.sprites[self.name].y in range(self.sprites['dave'].y, self.sprites['dave'].y + 10):
            self.b_alive -= 42
            print("HIT BY DAVE", self.b_alive)
        if self.b_alive >= 1:
            self.sprites['green'] = CustomSprite('images/grenn_bar.png', batch=self.batch['game'], group=self.subgroups['bg_1'], x=0, y=400)
            
        if self.b_alive in range(900, 999):
            self.sprites['red1'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=0, y=400)
        if self.b_alive in range(800, 899):
            self.sprites['red2'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x= 50, y=400)
        if self.b_alive in range(700, 799):
            self.sprites['red3'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=100, y=400)
        if self.b_alive in range(600, 699):
            self.sprites['red4'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=150, y=400)
        if self.b_alive in range(500, 599):
            self.sprites['red5'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=200, y=400)
        if self.b_alive in range(400, 499):
            self.sprites['red6'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=250, y=400)
        if self.b_alive in range(300, 399):
            self.sprites['red7'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=300, y=400)
        if self.b_alive in range(200, 299):
            self.sprites['red8'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=350, y=400)
        if self.b_alive in range(100, 199):
            self.sprites['red9'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=400, y=400)
        if self.b_alive in range(1, 99):
            self.sprites['red10'] = CustomSprite('images/red_box.png', batch=self.batch['game'], group=self.subgroups['bg_2'], x=450, y=400)
                
            return self.b_alive




name = input("Player Name: ")
x = Main()
x.run(name)