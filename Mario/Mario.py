from argparse import Action
from turtle import width
import pygame
import pgzero
import pgzrun #thư viện pygamezer
from random import randint  #de chon 1 so nguyen ngau nhien trong 1 day so


WIDTH = 564    #chieu dai va rong của backgroud
HEIGHT = 564
score =0   #so diem
game_over =False
mario = Actor('mario')
mario.pos=100,200 #vi tri cua mario
coin=Actor("coin")
coin.pos=300,300   #vi tri cua coin

def place_coin():  #ham dieu khien vi tri cua coin
    coin.x=randint(20,(WIDTH-20))  #width -20 de coin luon o trong background, ko bi chay ra ngoai
    coin.y=randint(20,(HEIGHT-20))

def update(): #ham giup mario di chuyen
    global score   #de dung bien score ngoai ham update
   
    if keyboard.left:
        if mario.x>0:
            mario.x = mario.x-4  #di chuyen mario sang ben trai truc ox
    elif  keyboard.right:
        if mario.x<WIDTH:
            mario.x = mario.x +4
    elif  keyboard.up:
        if mario.y>0:
            mario.y=mario.y -4   #muon di chuyen len tren thi -4 do truc 0y huong xuong
    elif  keyboard.down:
        if mario.y<(HEIGHT):
            mario.y=mario.y +4
    
    coin_collected = mario.colliderect(coin) #ham colliderect xet mario cham vao coin ; tra ve TRUE
    if coin_collected:
        score+=10        #khi mario cham vao coin thi cong 10 diem
        place_coin()     #bien coin ngau nhien o vi tri khac

def time_up():   #ham đặt thời gian ket thuc game
    global game_over  #goi bien game_over ngoai ham timup() vao
    game_over =True   #luc dau gam gia tri game_over=False

clock.schedule(time_up,20.0) #thoi gian choi 10s

def draw():
    screen.blit("background",(0,0))
    mario.draw()
    coin.draw()  
    screen.draw.text("score " + str(score),color="black",topleft=(10,10))  #bien doi bien score thanh dang string de in len man hinh 

    if game_over : #khi het game muon hien ra ket qua final score
        screen.blit("background",(0,0))
        screen.draw.text("Final Score " + str(score),color="black",topleft=(10,10))
 
place_coin()  #goi ham place_coin ra

pgzrun.go()