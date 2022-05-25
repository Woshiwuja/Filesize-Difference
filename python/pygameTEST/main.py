# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    HEIGHT = 720
    WIDTH = 1280 
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("minimal program")
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
    #variables
    vec = pygame.math.Vector2

    ACC = 0.5
    FRIC = -0.1
    FPS = 60
    FramePerSec = pygame.time.Clock()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
