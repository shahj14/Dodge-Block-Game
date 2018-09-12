import pygame
import time
import random

pygame.init()

disp_width = 750
disp_height = 750

person_width = 200
person_height = 200

personImg = pygame.image.load('person.png')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Dodge Block')
clock = pygame.time.Clock()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()

def scorer(count):
	font = pygame.font.SysFont(None,45)
	text = font.render("Score: "+str(count),True,white)
	gameDisplay.blit(text,(0,0))

def highscorer(count):
	font = pygame.font.SysFont(None,45)
	text = font.render("Highscore: "+str(count),True,white)
	gameDisplay.blit(text,(200,0))

def objects(objectx,objecty,objectw,objecth,color):
	pygame.draw.rect(gameDisplay,color,[objectx,objecty,objectw,objecth])


def person(x,y):
	gameDisplay.blit(personImg,(x,y))

def text_objects(text,font,color):
	textSf = font.render(text,True, color)
	return textSf, textSf.get_rect()

def message_display(text):
	TitleText = pygame.font.Font('freesansbold.ttf',60)
	TextSurf, TextRect = text_objects(text,TitleText,red)
	TextRect.center = disp_width/2, disp_height/2
	gameDisplay.blit(TextSurf,TextRect)

	pygame.display.update()

	time.sleep(2)
	gameLoop()

def collide():
	message_display('Better Luck Next Time')


def read():
	file_handle = open('scores.txt','r')
	num = file_handle.readlines()
	final = int(num[0])
	file_handle.close()
	return final

def compare(count):
	if count > read():
		text_file = open('scores.txt','w')
		text_file.write(str(count))
		text_file.close()

def gameLoop():
	score = 0
	high = read()
	x = (disp_width * .45)
	y = (disp_height * .75)

	x_move = 0
	y_move = 0

	object_startx = random.randrange(0,disp_width);
	object_starty = random.randrange(0,disp_height/2);
	object_speed = 20
	object_width = 100
	object_height = 100

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move = -8
				elif event.key == pygame.K_RIGHT:
					x_move = 8
				elif event.key == pygame.K_UP:
					y_move = -8
				elif event.key == pygame.K_DOWN:
					y_move = 8

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					x_move = 0
					y_move = 0

		x = x + x_move
		y = y + y_move

		
		
		gameDisplay.fill(white)
		gameDisplay.blit(pygame.image.load('background.png'),(0,0))
		scorer(score)
		highscorer(high)


		objects(object_startx,object_starty,object_width,object_height,red)
		object_starty += object_speed
		person(x,y)


		if x > disp_width - 150 or x < -50:
			gameExit = True
			compare(score)
			collide()
			

		if y < -30 or y > disp_height - 150:
			gameExit = True
			compare(score)
			collide()

		if object_starty >= disp_height - object_height:
			object_starty = random.randrange(0,disp_height/2);
			object_startx = random.randrange(0,disp_width);
			score = score +1

		if y < object_starty + 50:
			if x < object_startx and x > object_startx - object_width:# or x+person_width>object_startx and x + person_width < object_startx + object_width:
				gameExit = True
				compare(score)
				collide()
	


		pygame.display.update()
		clock.tick(60)
gameLoop()
pygame.quit()
quit()