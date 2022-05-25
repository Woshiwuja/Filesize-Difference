#make a pong game with pygame
import pygame
import sys
import random
import time
import os
import math
import numpy as np

from pygame.locals import *
#create the window
pygame.init()  #initialize pygame
screen = pygame.display.set_mode((800,600)) #create the screen
pygame.display.set_caption("Copilot") #set the caption
#set the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#set the font
font = pygame.font.SysFont(None, 25)
#set the clock
clock = pygame.time.Clock()
#set the ball
ball_x = 400
ball_y = 300
ball_x_change = 0
ball_y_change = 0
ball_radius = 10
#set the paddle
paddle_x = 400
paddle_y = 550
paddle_x_change = 0
paddle_width = 100
paddle_height = 10
#set the score
score_value = 0
#set the game loop
game_over = False
#set the game loop
while not game_over:
    if ball_y > paddle_y:
        game_over = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_x_change = -5
            if event.key == pygame.K_RIGHT:
                paddle_x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_x_change = 0
    paddle_x += paddle_x_change
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > 799:
        paddle_x = 799
    #set the ball
    ball_x += ball_x_change
    ball_y += ball_y_change
    if ball_x < 0:
        ball_x = 0
        ball_x_change = -ball_x_change
    if ball_x > 799:
        ball_x = 799
        ball_x_change = -ball_x_change
    if ball_y < 0:
        ball_y = 0
        ball_y_change = -ball_y_change
    if ball_y > 599:
        ball_y = 599
        ball_y_change = -ball_y_change
    #set the score
    score_text = font.render("Score: " + str(score_value), True, WHITE)
    screen.blit(score_text, [10, 10])
    #set the ball
    pygame.draw.circle(screen, WHITE, [int(ball_x), int(ball_y)], ball_radius)
    #set the paddle
    pygame.draw.rect(screen, WHITE, [paddle_x, paddle_y, paddle_width, paddle_height])
    #update the screen
    pygame.display.update()
    #set the clock
    clock.tick(60)
#set the game over text
game_over_text = font.render("Game Over", True, WHITE)
screen.blit(game_over_text, [200, 250])
#update the screen
pygame.display.update()
#set the clock
time.sleep(2)
#set the game loop
game_over = False
#set the score
score_value = 0
#set the ball
ball_x = 400
ball_y = 300
ball_x_change = 0
ball_y_change = 0
ball_radius = 10
#set the paddle
paddle_x = 400
paddle_y = 550
paddle_x_change = 0
paddle_width = 100
paddle_height = 10
