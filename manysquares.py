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
    # #52c4e9 lighter blue
    # #1a60a4 dark blue
    

def main():
	turtle.tracer(0,0)
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	count = 0
	for x in range (-400,451,25):
		for y in range (-400,401,25):
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
								
			t.color(thecolor)
			square(t,20)
			count = count + 1
			print(x,y,count,thecolor)

	turtle.update()
	twin.exitonclick()

if __name__=="__main__":
	main()

