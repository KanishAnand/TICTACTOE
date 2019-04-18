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
	#print("dfs")
	if(self[0] < org_x_start or self[0] > org_x_start + 3*width):
		print("Wrong Move")
		return 0
	if(self[1] < org_y_start or self[1] > org_y_start + 3*height):
		print("Wrong Move")
		return 0

	x_cor = self[0] - org_x_start
	y_cor = self[1]	- org_y_start
	temp_x = x_cor // width
	var_x = org_x_start + temp_x * width
	temp_y = y_cor // height
	var_y = org_y_start + temp_y * height
	val = temp_x + temp_y*3

	if(arr[val] != 0):
		print("Wrong Move")
		return 0

	global turn_count
	turn_count = turn_count + 1
	
	if(turn_count % 2 == 1):
		text = font.render("TURN_1",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start+ width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)

		text = font.render("TURN_0",True,(0,255,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start + 2*width + width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)
	else:
		text = font.render("TURN_0",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start + 2*width + width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)

		text = font.render("TURN_1",True,(255,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start+ width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)
	#print(turn_count)
	if(turn_count % 2 == 1):
		color_1 = (255,0,0)
	else:
		color_1 = (0,255,0)

	if(turn_count % 2 == 1):
		arr[val] = 1
	else:
		arr[val] = 2

	#print(temp_y,temp_x)
	obj = boxes(color_1,var_x,var_y,height,width)
	obj.draw_box();
	result=check(val)
	if(result == 0):
		text = font.render("TURN_1",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start+ width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)

		text = font.render("TURN_0",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start + 2*width + width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)

		text = font.render(str(turn_count%2) + " WON",True,(24,78,208),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start + width + width//2,org_y_start + 4*height)
		gameDisplay.blit(text,textRect)
		#print(str(turn_count%2) + "  WON")
		return 1

	elif turn_count == 9:
		text = font.render("TURN_1",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start+ width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)

		text = font.render("TURN_0",True,(0,0,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start + 2*width + width//2,org_y_start+4*height)
		gameDisplay.blit(text,textRect)
		text = font.render("DRAW",True,(24,78,208),(0,0,0))
		textRect = text.get_rect()
		textRect.center= (org_x_start+width + width//2,org_y_start + 4*height)
		gameDisplay.blit(text,textRect)
		#print("DRAW")
		return 1
	return 0

def check(val):
	temp = val // 3
	beg = temp*3
	flag = 0
	for i in range(3):
		if(arr[beg + i] != arr[val]):
			flag = 1
			break
	if flag == 1:
		flag = 0
		temp_col = val % 3
		beg = temp_col
		j = 0
		for i in range(3):
			if(arr[beg+j] != arr[val]):
				flag = 1
				break
			j += 3

	if flag == 1:
		flag = 0
		temp = val % 4
		if(val == 4):
			j=0
			for i in range(3):
				if(arr[j] != arr[val]):
					flag = 1
					break
				j += 4
			if flag == 1:
				flag = 0
				j=2
				for i in range(3):
					if(arr[j] != arr[val]):
						flag = 1
						break
					j += 2

		elif(temp  == 0):
			j=0
			for i in range(3):
				if(arr[j] != arr[val]):
					flag = 1
					break
				j += 4

		else:
			#print("D")
			j=2
			for i in range(3):
				if(arr[j] != arr[val]):
					flag = 1
					break
				j += 2

	return flag

import pygame
import sys
import os
import array 
arr = array.array('i',[0])
for i in range(10):
	arr.append(0)
# for i in range(10):
# 	print(arr[i])
# for i in range(3):
# 	print(arr[i])
pygame.init()
marked=[]
quit = True
turn_count = 0
color_0=(0,128,255)
org_x_start = 230
org_y_start = 80
height=140
width=140
x_start = org_x_start - width
y_start = org_y_start - height
os.environ['SDL_VIDEO_WINDOW_POS'] 	= "%d,%d" %(600,250)
gameDisplay = pygame.display.set_mode((900,700))
pygame.display.set_caption('TIC TAC TOE')
font = pygame.font.Font('freesansbold.ttf',32)

for i in range(3):
	y_start = y_start + height
	x_start = org_x_start - width
	for j in range(3):
		x_start = x_start + width
		obj = boxes(color_0,x_start,y_start,height,width);
		#print(type(obj))
		obj.draw_box()

color_line = (0,0,0)
#pygame.draw.circle(gameDisplay,color_1,(org_x_start + width,org_y_start + height),20,4)
pygame.draw.line(gameDisplay,color_line,(org_x_start,org_y_start+height),(org_x_start+width*3,org_y_start+height),4)
pygame.draw.line(gameDisplay,color_line,(org_x_start,org_y_start+2*height),(org_x_start+width*3,org_y_start+2*height),4)
pygame.draw.line(gameDisplay,color_line,(org_x_start+width,org_y_start),(org_x_start+width,org_y_start+3*height),4)
pygame.draw.line(gameDisplay,color_line,(org_x_start+width*2,org_y_start),(org_x_start+width*2,org_y_start+3*height),4)

text = font.render("TURN_1",True,(255,0,0),(0,0,0))
textRect = text.get_rect()
textRect.center= (org_x_start+ width//2,org_y_start+4*height)
gameDisplay.blit(text,textRect)

while quit:
	#pygame.display.set_caption('TIC TAC TOE')   #########this cause infinte loop (hangs comp)
	for event in pygame.event.get():
		#print(event.type)
		if event.type == pygame.QUIT:
			quit = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			#print(pos)
			result = mark_the_box(pos);
			pygame.draw.line(gameDisplay,color_line,(org_x_start,org_y_start+height),(org_x_start+width*3,org_y_start+height),4)
			pygame.draw.line(gameDisplay,color_line,(org_x_start,org_y_start+2*height),(org_x_start+width*3,org_y_start+2*height),4)
			pygame.draw.line(gameDisplay,color_line,(org_x_start+width,org_y_start),(org_x_start+width,org_y_start+3*height),4)
			pygame.draw.line(gameDisplay,color_line,(org_x_start+width*2,org_y_start),(org_x_start+width*2,org_y_start+3*height),4)
			if result == 1:
				#pygame.time.wait(500)
				quit = False
			# for i in range(10):
			# 	print(arr[i])
			# print(pos)
	#pygame.draw.rect(gameDisplay,(0,128,255),pygame.Rect(30,30,60,60))
	# pygame.draw.line(gameDisplay,color,(100,120),(300,120),2)
	# pygame.draw.line(gameDisplay,color,(100,200),(300,200),2)
	# pygame.draw.line(gameDisplay,color,(150,60),(150,270),2)
	# pygame.draw.line(gameDisplay,color,(250,60),(250,270),2)
	pygame.display.flip()
	if(quit == False):
		pygame.time.wait(1000)
