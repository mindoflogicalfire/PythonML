import turtle as t
t.speed('fastest')
t.color('red')
t.showturtle()
t.pensize(3)
for i in range(10):
	for j in range (i,10):
		for k in range (10):
			t.forward (100);t.right(36);t.forward(-50)
		t.right(-36);t.penup();t.forward(50);t.pendown()
	t.right(36)
t.exitonclick()