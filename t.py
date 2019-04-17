class boxes:
	def __init__(self,color,start_x,start_y,width,height):
		self.color = color
		self.start_y = start_y
		self.start_x = start_x
		self.width = width
		self.height = height
	def draw_box(self):
		pygame.draw.rect(gameDisplay,self.color,pygame.Rect(self.start_x,self.start_y,self.height,self.width))

def mark_the_box(self):
	print("dfs")
	if(self[0] < org_x_start or self[0] > org_x_start + 3*width):
		print("Wrong Move")
		return 
	if(self[1] < org_y_start or self[1] > org_y_start + 3*height):
		print("Wrong Move")
		return 
	global turn_count
	turn_count = turn_count + 1
	print(turn_count)
	if(turn_count % 2 == 1):
		color_1 = (255,0,0)
	else:
		color_1 = (0,255,0)

	x_cor = self[0] - org_x_start
	y_cor = self[1]	- org_y_start
	temp_x = x_cor // width
	var_x = org_x_start + temp_x * width
	temp_y = y_cor // height
	var_y = org_y_start + temp_y * height
	print(temp_y,temp_x)
	obj = boxes(color_1,var_x,var_y,height,width)
	obj.draw_box();

import pygame
import sys
pygame.init()
quit = True
turn_count = 0
color_0=(0,128,255)
org_x_start = 230
org_y_start = 80
height=140
width=140
x_start = org_x_start - width
y_start = org_y_start - height
gameDisplay = pygame.display.set_mode((900,600))
pygame.display.set_caption('TIC TAC TOE')

for i in range(3):
	y_start = y_start + height
	x_start = org_x_start - width
	for j in range(3):
		x_start = x_start + width
		obj = boxes(color_0,x_start,y_start,height,width);
		print(type(obj))
		obj.draw_box()

#pygame.draw.circle(gameDisplay,color_1,(org_x_start + width,org_y_start + height),20,4)

while quit:
	#pygame.display.set_caption('TIC TAC TOE')   #########this cause infinte loop (hangs comp)
	for event in pygame.event.get():
		#print(event.type)
		if event.type == pygame.QUIT:
			quit = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			print(type(pos))
			mark_the_box(pos);
			print(pos)
	#pygame.draw.rect(gameDisplay,(0,128,255),pygame.Rect(30,30,60,60))
	# pygame.draw.line(gameDisplay,color,(100,120),(300,120),2)
	# pygame.draw.line(gameDisplay,color,(100,200),(300,200),2)
	# pygame.draw.line(gameDisplay,color,(150,60),(150,270),2)
	# pygame.draw.line(gameDisplay,color,(250,60),(250,270),2)
	pygame.display.flip()
