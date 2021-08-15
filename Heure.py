import time
import pygame as pg
from math import cos,sin,tau
from colorsys import hsv_to_rgb
hsv=hsv_to_rgb
print()

pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()
larg=250
haut=250
q=1
h,m,s=0,0,0
s=time.localtime().tm_sec
font=pg.font.SysFont('Consolas',25)
zoom=100

sem=['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
mois='Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre'.split(' ')

while q:
	fps.tick(60)
	pg.display.flip()
	f.fill(0)
	now=time.localtime()
	s+=abs(now.tm_sec-s)/zoom
	s=s%60
	m=now.tm_min+s/60
	h=now.tm_hour+m/60
	alpha=tau
	if now.tm_hour>12:
		pam=12
	else:
		pam=0
	for i in range(pam,pam+12):
		alpha-=tau/12
		suf=font.render(str(i),True,hsv(i/12,1,255))
		sufrect=suf.get_rect()
		f.blit(suf,(larg+cos(i/12*tau-tau/4)*zoom-sufrect.width/2,haut+sin(i/12*tau-tau/4)*zoom-sufrect.height/2))
	alpha=tau
	div=12
	for i in range(div):
		alpha-=tau/div
		suf=font.render(format(i*60/div,'.0f'),True,hsv(i/div,1,255))
		sufrect=suf.get_rect()
		f.blit(suf,(larg+cos(i/div*tau-tau/4)*2*zoom-sufrect.width/2,haut+sin(i/div*tau-tau/4)*2*zoom-sufrect.height/2))
	pg.draw.line(f,hsv(h/12,1,255),(larg,haut),(larg+cos(h/12*tau-tau/4)*zoom,haut+sin(h/12*tau-tau/4)*zoom),int(zoom/100*5))
	pg.draw.line(f,hsv(m/60,1,255),(larg,haut),(larg+cos(m/60*tau-tau/4)*2*zoom,haut+sin(m/60*tau-tau/4)*2*zoom),int(zoom/100*5))
	pg.draw.line(f,hsv(s/60,1,255),(larg,haut),(larg+cos(s/60*tau-tau/4)*2*zoom,haut+sin(s/60*tau-tau/4)*2*zoom),int(zoom/100*2.5))
	suf=font.render(f'{sem[now.tm_wday]} {now.tm_mday} {mois[now.tm_mon-1]}',True,(255,255,255))
	sufrect=suf.get_rect()
	f.blit(suf,(larg+2*zoom+25,haut-sufrect.height/2))
	for event in pg.event.get():
		if event.type==pg.QUIT:
			pg.quit()
			q=0
			print(h,m)
		if event.type==pg.KEYUP:
			if event.key==pg.K_F11:
				pg.display.quit()
				f=pg.display.set_mode((0,0),pg.FULLSCREEN)

				pg.display.init()
				re=pg.display.get_surface().get_rect()
				larg=re.width/2
				haut=re.height/2
			else:
				pg.display.quit()
				f=pg.display.set_mode((500,500),pg.RESIZABLE)
				pg.display.init()
				haut,larg=250,250
				zoom=100
		elif event.type==pg.MOUSEBUTTONDOWN:
			if event.button==4:
				zoom+=10
			elif event.button==5:
				zoom-=10
		elif event.type==pg.VIDEORESIZE:
			haut=event.h/2
			larg=event.w/2

"""		
		%Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        tm_year, tm_mon, tm_mday, tm_hour, tm_min,
        tm_sec, tm_wday, tm_yday, tm_isdst
"""
