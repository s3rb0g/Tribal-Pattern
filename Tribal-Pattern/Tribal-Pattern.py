import turtle
t = turtle.Turtle()
t.speed(0)
t.width(5)

'First layer'
t.penup()
t.goto(-250, 250)
t.pendown()

for tri in range(5):
  t.rt(10)
  for triangle in range(2):
    t.fd(100)
    t.right(160)
  
  t.lt(60)
  t.fd(35)
	
  t.penup()
  t.rt(90)
  t.fd(100)
  t.pendown()

'Second layer'
t.penup()
t.goto(-250, 180)
t.pendown()

for tri2 in range(20):
  if (tri2 == 2) or (tri2 == 5) or (tri2 == 8) or (tri2 == 11) or (tri2 == 14) or (tri2 == 17):
    t.penup()
  
  t.rt(50)
  for tri1 in range(3):
    if tri1 == 2:
      t.penup()
      t.rt(50)
      t.fd(45)
      t.pendown()
    else:
      t.fd(30)
      t.rt(85)    
    
  t.penup()
  t.rt(90)
  t.fd(25)
  t.pendown()

'Third layer'
t.penup()
t.goto(-250, 100)
t.pendown()

for s1 in range(13):
  for s2 in range(2):
    t.fd(20)
    t.rt(90)
    t.fd(30)
    t.rt(90)

  t.penup()
  t.fd(40)
  t.pendown()

'Fourth layer'
t.penup()
t.goto(-250, 30)
t.pendown()

for tri in range(17):
  if (tri == 5) or (tri == 11) or (tri == 17):
    t.penup()
    
  t.rt(10)
  for triangle in range(2):
    t.fd(30)
    t.right(160)
  
  t.lt(60)
  t.fd(10)
	
  t.penup()
  t.rt(90)
  t.fd(30)
  t.pendown()

'Fifth layer'
t.penup()
t.goto(-250, -20)
t.pendown()

for squ in range(15):
  t.color("Black")
  t.begin_fill()
  
  for sque in range(4):    
    t.fd(20)
    t.rt(90)
    
  t.end_fill()
  t.penup()
  t.fd(35)
  t.pendown()

'Sixth layer'
t.penup()
t.goto(-250, -80)
t.pendown()

for w in range(4):
  t.color("Black")
  t.begin_fill()
  
  for q in range(3):
    t.fd(100)
    t.rt(120)
 	
  t.end_fill()
  t.penup()
  t.fd(130)
  t.pendown()

t.penup()
t.goto(-250, -170)
t.fd(64)
t.pendown()

for a in range(4):
  t.color("Black")
  t.begin_fill()
  
  for e in range(3):
    t.fd(100)
    t.lt(120)

  t.end_fill()
  t.penup()
  t.fd(130)
  t.pendown()  

'Seventh layer'
t.penup()
t.goto(-250, -200)
t.pendown()
    
for qt in range(17):
  if (qt == 2) or (qt == 3) or (qt == 4) or (qt == 5) or (qt == 8) or (qt == 9) or (qt == 10) or (qt == 11) or (qt == 14) or (qt == 15) or (qt == 16):
     t.penup()
  
  if (qt == 1) or (qt == 7)or (qt == 13):
    t.color("black" , "white")
    t.begin_fill()
  t.rt(10)
  for l in range(2):
    t.fd(50)
    t.right(160)
  
  t.end_fill()
  t.lt(60)
  t.fd(17.4)
	
  t.penup()
  t.rt(90)
  t.fd(30)
  t.pendown()

t.rt(180)

for qt1 in range(17):
  if (qt1 == 2) or (qt1 == 3) or (qt1 == 4) or (qt1 == 5) or (qt1 == 8) or (qt1 == 9) or (qt1 == 10) or (qt1 == 11) or (qt1 == 14) or (qt1 == 15) or (qt1 == 16):
     t.penup()
  
  if (qt1 == 1) or (qt1 == 7)or (qt1 == 13):
    t.color("black" , "white")
    t.begin_fill()
  t.lt(10)
  for v in range(2):
    t.fd(50)
    t.lt(160)   
	
  t.end_fill()
  t.rt(60)
  t.fd(17.3)

  t.penup()
  t.lt(90)
  t.fd(30)
  t.pendown()

'Eighth layer'
t.penup()
t.goto(-250, -250)
t.rt(180)
t.pendown()    

for v in range(18):
  if (v == 2) or (v == 5) or (v == 8) or (v == 11) or (v == 14) or (v == 17):
    t.penup()
  else:
    t.color("black")
    t.begin_fill()
    
  t.rt(10)
  for l in range(2):
      t.fd(50)
      t.right(160)    

  t.end_fill()
  t.lt(60)
  t.fd(17.3)

  t.penup()
  t.rt(90)
  t.fd(30)
  t.pendown()
  
'Ninth layer'
t.penup()
t.goto(-250, -300)
t.pendown()  
 
for p in range(15):
  t.lt(45)
  for o in range(4):
    t.fd(20)
    t.rt(90)

  t.rt(45)
  t.penup()
  t.fd(35)
  t.pendown()
    
    
    
