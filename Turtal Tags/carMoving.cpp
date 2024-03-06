#include<graphics.h>

#include<conio.h>

#include<stdio.h>

#include<dos.h>

#include<stdlib.h>



void main()

{

int a , gd=DETECT,gm,d,ii,c=200,s=190,f=210,t,r,v=180,b=210,m,n,speed=8;



int c1=398,f1=408,v1=358,b1=408,s1=388,t1,r1,m1,n1,y=0,i;



char msg[50];



system("cls");



initgraph(&gd,&gm,"");



setbkcolor(BLUE);



settextstyle(TRIPLEX_FONT,HORIZ_DIR,10);

sprintf(msg,"If Kissing U is a Crime  , Then Am Ready To Go to Jail");

setcolor(YELLOW);

outtextxy(100,200,msg);

getch();

cleardevice();

getch();





for(a=1;a<=12;a++)

{

t = s , r = f;

m = s , n = f;

t1 = s1, r1 = f1;

m1 = s1, n1 = f1;

	for(ii=300;ii<=315&&!kbhit();ii++)

	{

	gotoxy(29,2);

	

	printf("Happy Kiss Day By Pankaj Panjwani");

	setcolor(WHITE);

	circle(c1,270,10);

	ellipse(c1-4,269,0,360,2,3);

	putpixel(c1-4,269,15);

	line(c1-6,276,c1-2,276);

	line(c1,280,c1,302);

	

	line(c1,303,c1+13,330);

	line(c1,280,n1-=1,300);

	line(c1,280,m1+=1,300);

	

	line(c1+13,330,c1-13,330);

	line(c1-13,330,c1,303);

	line(c1-1,330,r1-=1,350);

	

	line(c1,330,t1+=1,350);

	/////////////////////////

	setcolor(BROWN);

	line(1,351,630,351);

	////////////////////////////

	setcolor(WHITE);

	circle(c,270,10);

	ellipse(c+5,269,0,360,2,3);

	putpixel(c+5,269,15);

	line(c+3,276,c+8,276);

	line(c,280,c,320);

	line(c+1,280,c+1,320);

	

	line(c+1,280,n-=1,301);

	line(c,280,m+=1,301);

	

	line(c+1,320,r-=1,350);

	line(c,320,t+=1,350);

	delay(100);

	if(a==12)

	goto zx;

	cleardevice();

	}

	c+=speed;

	s+=speed,f+=speed,v+=speed,b+=speed;

	c1-=speed;

	s1-=speed,f1-=speed,v1-=speed,b1-=speed;

}

zx:

{

setcolor(RED);

gotoxy(38,18);printf("%c",3);

settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);

sprintf(msg,"Can i borrow a KISS? I promise I'll give it back");

setcolor(10);

outtextxy(230,200,msg);

}

getch();

closegraph();

} 