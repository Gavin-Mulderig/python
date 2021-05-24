# recursion
import turtle

def square(t,d):
	t.pendown()
	t.begin_fill()
	for i in  range (0,4):
		t.fd(d)
		t.rt(90)
	t.end_fill()
	t.penup()
    

def main():
	turtle.tracer(0,0)
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	count = 0
	for x in range (-400,451,25):
		for y in range (-375,426,25):
			t.penup()
			t.goto(x,y)
			thecolor = "#000000"
			if (count > 1 and count < 33):
				thecolor = "#ffffff"
			if (count == 34):
				thecolor = "#1a60a4"
			if (count > 35 and count < 66):
				thecolor = "#ffffff"
			if (count == 67):
				thecolor = "#1a60a4"	
			if (count > 68 and count < 99):
				thecolor = "#ffffff"
			if (count > 99 and count < 102):
				thecolor = "#1a60a4"	
			if (count > 102 and count < 111):
				thecolor = "#ffffff"
			if (count > 113 and count < 132):
				thecolor = "#ffffff"
			if (count > 132 and count < 135):
				thecolor = "#1a60a4"	
			if (count > 135 and count < 143):
				thecolor = "#ffffff"
			if (count > 143 and count < 147):
				thecolor = "#1a60a4"
			if (count > 147 and count < 165):
				thecolor = "#ffffff"
			if (count > 165 and count < 169):
				thecolor = "#1a60a4"			
			if (count > 169 and count < 175):
				thecolor = "#ffffff"
			if (count > 175 and count < 179):
				thecolor = "#1a60a4"
			if (count > 178 and count < 181):
				thecolor = "#52c4e9"		
			if (count > 181 and count < 198):
				thecolor = "#ffffff"
			if (count > 198 and count < 203):
				thecolor = "#1a60a4"		
			if (count > 203 and count < 207):
				thecolor = "#ffffff"	
			if (count > 207 and count < 212):
				thecolor = "#1a60a4"
			if (count > 211 and count < 214):
				thecolor = "#52c4e9"	
			if (count > 214 and count < 231):
				thecolor = "#ffffff"
			if (count > 231 and count < 235): 
				thecolor = "#1a60a4"
			if (count > 234 and count < 237):
				thecolor = "#52c4e9"
			if (count == 238):
				thecolor = "#ffffff"
			if (count > 239 and count < 242):
				thecolor = "#1a60a4"
			if (count > 243 and count < 248):
				thecolor = "#52c4e9"	
			if (count > 248 and count < 264):
				thecolor = "#ffffff"		
			if (count > 265 and count < 267):
				thecolor = "#1a60a4" 
			if (count > 266 and count < 271):
				thecolor = "#52c4e9"
			if (count > 272 and count < 277):
				thecolor = "#1a60a4"
			if (count > 277 and count < 281):
				thecolor = "#52c4e9"
			if (count > 281 and count < 299):
				thecolor = "#ffffff"	
			if (count > 299 and count < 303):
				thecolor = "#52c4e9"
			if (count > 302 and count < 306):
				thecolor = "#1a60a4"	
			if (count > 306 and count < 309):
				thecolor = "#1a60a4"
			if (count > 309 and count < 313):
				thecolor = "#52c4e9"	
			if (count > 315 and count < 333):
				thecolor = "#ffffff"
			if (count > 333 and count < 335):
				thecolor = "#52c4e9"
			if (count > 334 and count < 339):
				thecolor = "#1a60a4"
			if (count == 339):
				thecolor = "#52c4e9"
			if (count > 341 and count < 344):
				thecolor = "#52c4e9"	
			if (count > 345 and count < 349):
				thecolor = "#52c4e9"
			if (count > 350 and count < 367):
				thecolor = "#ffffff"
			if (count > 367 and count < 371):
				thecolor = "#1a60a4"
			if (count > 370 and count < 376):
				thecolor = "#52c4e9"
			if (count > 376 and count < 384):
				thecolor = "#1a60a4"
			if (count > 384 and count < 396):
				thecolor = "#ffffff"
			if (count > 397 and count < 400):
				thecolor = "#ffffff"	
			if (count > 400 and count < 404):	
				thecolor = "#1a60a4"
			if (count > 403 and count < 408):
				thecolor = "#52c4e9"	
			if (count > 408 and count < 410):
				thecolor = "#1a60a4"
			if (count > 409 and count < 413):
				thecolor = "#ffe9a8"	
			if (count > 412 and count < 418):
				thecolor = "#1a60a4"	
			if (count > 418 and count < 429):
				thecolor = "#ffffff"		
			if (count == 430):
				thecolor = "#1a60a4"
			if (count == 433):
				thecolor = "#52c4e9"
			if (count > 433 and count < 437):
				thecolor = "#1a60a4"	
			if (count > 436 and count < 440):
				thecolor = "#52c4e9"
			if (count > 440 and count < 444):
				thecolor = "#ffe9a8"	
			if (count > 443 and count < 446): 
				thecolor = "#efefef"
			if (count == 446):
				thecolor = "#ffe9a8"
			if (count > 446 and count < 451):
				thecolor = "#1a60a4"
			if (count > 451 and count < 462):
				thecolor = "#ffffff"	
			if (count > 462 and count < 466):
				thecolor = "#1a60a4"
			if (count > 465 and count < 468):
				thecolor = "#52c4e9"
			if (count > 467 and count < 470):
				thecolor = "#1a60a4"
			if (count > 469 and count < 473):
				thecolor = "#52c4e9"
			if (count == 474):
				thecolor = "#ffe9a8"
			if (count > 475 and count < 480):
				thecolor = "#efefef"
			if (count > 479 and count < 484):
				thecolor = "#1a60a4"
			if (count > 485 and count < 495):
				thecolor = "#ffffff"											
			if (count > 495 and count < 499):
				thecolor ="#1a60a4"
			if (count > 498 and count < 502):
				thecolor = "#52c4e9"	
			if (count == 502):
				thecolor = "#1a60a4"
			if (count > 502 and count < 506):
				thecolor = "#52c4e9"
			if (count == 507):
				thecolor = "#ffe9a8"				
			if (count == 509):
				thecolor = "#efefef"				
			if (count == 512):
				thecolor = "#efefef"	
			if (count > 512	and count < 516):
				thecolor = "#1a60a4"				
			if (count == 517):
				thecolor = "#52c4e9"				
			if (count > 518 and count < 528):
				thecolor = "#ffffff"	
			if (count > 528 and count < 533):
				thecolor = "#1a60a4"
			if (count == 533):
				thecolor = "#53c4e9"
			if (count > 536 and count < 539):
				thecolor = "#53c4e9"
			if (count == 540):
				thecolor = "#ffe9a8"
			if (count == 542):
				thecolor = "#efefef"				
			if (count == 545):
				thecolor = "#efefef"
			if (count == 546):
				thecolor = "#1a60a4"
			if (count > 548 and count < 551):
				thecolor = "#53c4e9"	
			if (count > 551 and count < 561):
				thecolor = "#ffffff"		
			if (count == 562):
				thecolor = "#1a60a4"	
			if (count > 563 and count < 566):
				thecolor = "#1a60a4"
			if (count > 566 and count < 570):
				thecolor = "#ffffff"		
			if (count == 571):
				thecolor = "#53c4e9"
			if (count == 573):
				thecolor = "#ffe9a8"
			if (count > 574 and count < 578):
				thecolor = "#ffe9a8"
			if (count == 578):
				thecolor = "#1a60a4"
			if (count == 580):
				thecolor = "#53c4e9"
			if (count == 582): 
				thecolor = "#53c4e9"	
			if (count > 583 and count < 594):
				thecolor = "#ffffff"	
			if (count == 595):
				thecolor = "#1a60a4"	
			if (count > 598 and count < 604):
				thecolor = "#ffffff"
			if (count == 605):
				thecolor = "#53c4e9"
			if (count == 607):
				thecolor = "#ffe9a8"
			if (count == 608):
				thecolor = "#efefef"
			if (count == 611):
				thecolor = "#1a60a4"
			if (count == 613):
				thecolor = "#53c4e9"
			if (count > 615 and count < 627):
				thecolor = "#ffffff"		
			if (count == 628):
				thecolor = "#1a60a4"	
			if (count > 629 and count < 637):
				thecolor = "#ffffff"	
			if (count > 637 and count < 640):
				thecolor = "#53c4e9"
			if (count == 641):
				thecolor = "#ffe9a8"
			if (count > 641 and count < 645):
				thecolor = "#efefef"
			if (count > 644 and count < 647):
				thecolor = "#1a60a4"
			if (count > 647 and count < 660):
				thecolor = "#ffffff"	
			if (count > 661 and count < 670):
				thecolor = "#ffffff"			
			if (count > 670 and count < 673):
				thecolor = "#53c4e9"
			if (count > 680 and count < 703):
				thecolor = "#ffffff"	
			if (count > 703 and count < 707):
				thecolor = "#53c4e9"
			if (count > 707 and count < 737):
				thecolor = "#ffffff"		
			if (count > 740 and count < 769):
				thecolor = "#ffffff"	
			if (count > 769 and count < 774):
				thecolor = "#1a60a4"	
			if (count > 774 and count < 802):
				thecolor = "#ffffff"
			if (count > 802 and count < 805):
				thecolor = "#1a60a4"
			if (count == 805):
				thecolor = "#53c4e9"
			if (count == 806):
				thecolor = "#1a60a4"	
			if (count > 807 and count < 835):
				thecolor = "#ffffff"	
			if (count > 835 and count < 838):	
				thecolor = "#1a60a4"
			if (count == 838):		
				thecolor = "#53c4e9"
			if (count == 839):
				thecolor = "#1a60a4"
			if (count > 840 and count < 868):
				thecolor = "#ffffff"					
			if (count == 870):
				thecolor = "#1a60a4"
			if (count == 871):
				thecolor = "#53c4e9"
			if (count == 872):
				thecolor = "#1a60a4"
			if (count > 873 and count < 902):
				thecolor = "#ffffff"				
			if (count > 905 and count < 935):
				thecolor = "#ffffff"
			if (count == 936):
				thecolor = "#1a60a4"
			if (count == 937):
				thecolor = "#53c4e9"
			if (count > 938 and count < 969):
				thecolor = "#ffffff" 	
			if (count > 970):
				thecolor ="#ffffff"
							
	
				# tan = #ffe9a8
				# dark blue = #1a60a4
				# light blue = #53c4e9
																							
			t.color(thecolor)
			square(t,20)
			count = count + 1
			print(x,y,count,thecolor)

	turtle.update()
	twin.exitonclick()

if __name__=="__main__":
	main()

