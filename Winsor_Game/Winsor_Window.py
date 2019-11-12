from PIL import Image
import pyglet
import os
from pyglet import image
from pyglet import text
from pyglet.window import key
import random
import csv
import string
# from pprint import pprint
# pprint(globals())
# pprint(locals())

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
        self.subgroups = {'bg_0' : pyglet.graphics.OrderedGroup(0), 'bg_1' : pyglet.graphics.OrderedGroup(1), 'walls' : pyglet.graphics.OrderedGroup(2), 'chars' : pyglet.graphics.OrderedGroup(3)}
        # Batch tells graphics what is going on
        
        
        # SPITES FOR CHARACTERS
        # self.sprites['dave'] = CustomSprite('images/dave_the_devil.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['lil_win'] = CustomSprite('images/winsor_0.png', batch=self.batch['game'], group=self.subgroups['chars'])
        
        # SPRITES FOR OBSTICALS
        self.sprites['wall1'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step1'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step2'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step3'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        self.sprites['step4'] = CustomSprite('images/wall.png', batch=self.batch['game'], group=self.subgroups['bg_1'])
        
        #STEPS/WALLS Co - Ords
        self.sprites['lil_win'].x = 250
        self.sprites['lil_win'].y = 350
        
        self.sprites['wall1'].x = 200
        self.sprites['wall1'].y = 0
        self.wall_1 = (self.sprites['wall1'].x, self.sprites['wall1'].y)
        
        self.sprites['step1'].x = 250
        self.sprites['step1'].y = 0
        self.step_1 = (self.sprites['step1'].x, self.sprites['step1'].y)
        
        self.sprites['step2'].x = 300
        self.sprites['step2'].y = 0
        
        self.sprites['step3'].x = 350
        self.sprites['step3'].y = 0
        
        self.sprites['step4'].x = 250
        self.sprites['step4'].y = 50
        # self.sprites['rock'].x = 200
        # self.sprites['rock'].y = 50
        # self.rock = (self.sprites['rock'].x, self.sprites['rock'].y)
        
        
        self.b_alive = 1000 # bobby is alive
        health = str(self.b_alive)
        self.d_alive = 1 # dave is alive
        
        #sprites for labels
        self.sprites[self.b_alive] = pyglet.text.Label("HEALTH: " + health, batch=self.batch['game'], group=self.subgroups['bg_1'], x=100, y=400)
        # self.sprites[self.player] = pyglet.text.Label("PLAYER: " + name, batch=self.batch['game'], group=self.subgroups['bg_1'], x=100, y=380)

    # def read_data(self):
    #     with open("character_data.csv", 'r') as csv_db:
    #         reader = csv.reader(csv_db)
    #         line = 0
    #         for row in reader:
    #             if line == 0:
    #                 row1 = (row[0])
    #                 print(row1)
    #                 line += 1
    #             if line == 1:
    #                 row2 = (row[0])
    #                 print(row2)
    #             return(row1)
        
    # def write_data(self, name, health):
    #     health_stat = int(health)
            
    #     with open ('player_data.csv', 'w') as csv_file:
    #         csv_writer = csv.writer(csv_file, delimiter=';')
    #         row = {}
    #         line_count = 0
    #         for i in range(len(row)):
    #             if line_count == 0:
    #                 csv_writer.writerow([self.sprites[self.name]])
    #                 line_count += 1
    #                 csv_writer.writerow(health_stat)
    #                 csv_file.close()
    #                 print(health_stat)
    #                 print(self.sprites[self.name])
    #             elif health == 0:
    #                     print(f'{name}, HAS DIED')
    #                     line_count += 1
    #                     csv_file.close()

    def collision(self):
        # collision X and Y seperate
        #USE GRID_SET to set object_collision
        self.set_x = Main.grid_set_x(self)
        self.set_y = Main.grid_set_y(self)
        #add border then grvity//
        
        if self.set_x == 'd' and self.set_y == '1':
            return True
        if self.sprites[self.name].x == 250 and self.self.sprite[self.name] == 50:
            return False
        
        
    
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
        
    def grid_set_y(self):
        #check Y Co_Ords
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

 
    def run(self, name): # Run render while bobby is alive
        self.name = name
        self.sprites[self.name] = CustomSprite('images/winsor_1.png', batch=self.batch['game'], group=self.subgroups['chars'])
        self.sprites[self.name].x = 10
        self.sprites[self.name].y = 10
        
        self.set_y = Main.collision(self)
        while self.b_alive >= 1:
            self.sprites[self.name].y -= 1
            if self.sprites[self.name].y == 0 or self.set_y == False:
                self.sprites[self.name].y += 2
        
            self.render()
            event = self.dispatch_events()

    def on_draw(self):
        self.render()
        self.labelset.draw()
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
            if symbol == key.SPACE:
                self.sprites[self.name].y += 50
        except:
            pass
        try:
            if self.block != True and symbol == key.RIGHT:
                self.sprites[self.name].x += 10 #UPDATES BATCH DATA -> For Graphics 
                print("RIGHT ->")
            elif self.block == True:
                self.sprites[self.name].x -= 2
        except:
            pass
        try:
            if self.block != True and symbol == key.UP:
                self.sprites[self.name].y += 10
                print("UP ^")
            elif self.rock == True:
                self.sprites[self.name].y -= 2
        except:
            pass
        try:
            if self.block != True and symbol == key.DOWN:
                self.sprites[self.name].y -= 10
                print("DOWN v")
            elif self.rock == True:
                self.sprites[self.name].y += 2
        except:
            pass
        try:
            if self.block != True and symbol == key.LEFT:
                self.sprites[self.name].x -= 10
                print("LEFT <-")
            elif self.block == True:
                self.sprites[self.name].x += 2
        except:
            pass
        try:
            if symbol == key.A:
                print('HEALTH:')
        except KeyError as e:
            print(e)
                # FIX KEY_ERROR HANDLING //
                
    def on_key_release(self, symbol, modifiers): #takes key stroke as ARGUMENTS
        
        self.block = Main.collision(self)
        if self.block == True:
            print("Rock...")
            
        if symbol == key.ESCAPE:
            print('EXITED GAME')
            self.b_alive = 0
        try:
            if self.block != True and symbol == key.RIGHT:
                self.sprites[self.name].x += 10 #UPDATES BATCH DATA -> For Graphics 
                print("RIGHT ->")
            elif self.block == True:
                self.sprites[self.name].x -= 5
        except:
            pass
                
        try:
            if self.rock != True and symbol == key.UP:
                self.sprites[self.name].y += 10
                print("UP ^")
            elif self.rock == True:
                self.sprites.y -= 5
        except:
            pass
                
        try:
            if self.rock != True and symbol == key.DOWN:
                self.sprites[self.name].y -= 10
                print("DOWN v")
            elif self.rock == True:
                self.sprites[self.name].y += 5
        except:
            pass
        try:
            if self.rock != True and symbol == key.LEFT:
                self.sprites[self.name].x -= 10
                print("LEFT <-")
            elif self.rock == True:
                self.sprites[self.name].x += 5
        except:
            pass
            
name = input("Player Name: ")
x = Main()
# x.write_data(name, 1000)
x.run(name)