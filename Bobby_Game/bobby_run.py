import pyglet
import os
from pyglet.window import key
import random

class CustomSprite(pyglet.sprite.Sprite):
    def __init__(self, texture_file, x=100, y=100, batch=None, group=None):
        # Must load texture beforeinit class:sprite
        # ADD BATCH FOR BACKGROUND GRID, THEN PUT GUNS IN FOREGROUND //
        # Then make guns shoot dave ;) //

        self.texture = pyglet.image.load(texture_file)
        # label = pyglet.text.Label('This is BOBBY THE PIRATE: KILL DAVE', font_name='Times New Roman', font_size=36, x=window.W / 2, y=window.H / 2, anchor_x='center', anchor_y='center')
        super(CustomSprite, self).__init__(self.texture, batch=batch, group=group)
        self.x = x
        self.y = y


class Main(pyglet.window.Window):

    def __init__(self):
        super(Main, self).__init__(800, 600, fullscreen = False)# set screen size
        self.x = 0
        self.y = 0

        W = 800
        H = 600

        self.sprites = {} # declare use of batch 'sprites'
        self.batch = {'main' : pyglet.graphics.Batch()} #Init batch 
        self.subgroups = {'background' : pyglet.graphics.OrderedGroup(0), 'foreground' : pyglet.graphics.OrderedGroup(1)}
        # Batch tells graphics what is going on
        self.sprites['guns'] = CustomSprite('guns.jpg', batch=self.batch['main'], group=self.subgroups['background'])#
        self.sprites['bobby'] = CustomSprite('bobby_the_pirate.png', batch=self.batch['main'], group=self.subgroups['foreground'])
        self.sprites['dave'] = CustomSprite('dave_the_devil.png', batch=self.batch['main'], group=self.subgroups['foreground'])
        # ADD SPRITES FOR OBSTICALS
        self.b_alive = 1 # bobby is alive
        self.d_alive = 1 # dave is alive

        d_x = random.randint(100, 500)
        d_y = random.randint(100, 500)
        self.sprites['guns'].x = 20
        self.sprites['guns'].y = 20
        self.sprites['dave'].x = d_x # set dave the devil location
        self.sprites['dave'].y = d_y
        # Implement random location setting for dave//


    def run(self): # Run render while bobby is alive
        while self.health > 0:
            self.render()
            event = self.dispatch_events()

    def on_draw(self):
        self.render()
        label.draw()

    def on_close(self):
        self.b_alive = 0

    def render(self):
        self.clear() # keep screen from duplicating on movement

        for batch_name, batch_object in self.batch.items():
            batch_object.draw() # Draw the batch files on screen
            
        self.flip() #UPDATES THE SCREEN -FlipIt-

    def dave(self):
        # aim dave to bobby //
        # make dave move on his own //
        self.sprites['dave'].x = random.randint(100, 500)
        self.sprites['dave'].y = random.randint(100, 500)
        if self.sprites['dave'].x == self.sprites['bobby'].x and self.sprites['dave'].y == self.sprites['bobby'].y:
            print("YOU DIED")
            Main.on_close(self)

        
    def on_key_press(self, symbol, modifiers): #takes key stroke as ARGUMENTS
        bobby_position_x = 0
        bobby_position_y = 0
        try:
            if symbol == key.SPACE:
                print("DAVE IS COMING")
                Main.dave(self) # Moves dave closer
            if symbol == key.ESCAPE:
                self.b_alive = 0
            elif symbol == key.RIGHT:
                bobby_position_x += 1 #does nothing for now
                self.sprites['bobby'].x += 10 #UPDATES BATCH DATA -> For Graphics 
                print("RIGHT ->")
            elif symbol == key.UP:
                bobby_position_y += 1
                self.sprites['bobby'].y += 10
                print("UP ^")
            elif symbol == key.DOWN:
                bobby_position_y -= 1
                self.sprites['bobby'].y -= 10
                print("DOWN v")
            elif symbol == key.LEFT:
                bobby_position_x -= 1
                self.sprites['bobby'].x -= 10
                print("LEFT <-")
        except KeyError:
            print("That Button Has No Power Here")        
                # FIX KEY_ERROR HANDLING
x = Main()
x.run()

# Make Character is born function 
# Allocate image.png for each new character