from tkinter import*
tk=Tk()

x=0
y=0
canvas=Canvas(tk,width=450,height=300)
canvas.pack()
campo=PhotoImage(file='Campo.gif')
my_image=PhotoImage(file='balon1.png')
gol=PhotoImage(file='gol.png')

canvas.create_image(0,0,anchor=NW, image=campo)
canvas.create_image(210,153,anchor=NW, image=my_image)


def moverbalon(event):
    global y,x
    if event.keysym=='Up':
        
        canvas.move(2,0,-6)
        y=y-6
    elif event.keysym=='Down':
        
        
        canvas.move(2,0,6)
        y=y+6
    elif event.keysym=='Left':
        
        canvas.move(2,-6,0)
        x=x-6
    else:        
        canvas.move(2,6,0)

        x=x+6
    if x == 222 or x== -222:
        print('GO00000000l!!!!')
    
canvas.bind_all('<KeyPress-Up>',moverbalon)
canvas.bind_all('<KeyPress-Down>',moverbalon)
canvas.bind_all('<KeyPress-Left>',moverbalon)
canvas.bind_all('<KeyPress-Right>',moverbalon)



tk.mainloop()

