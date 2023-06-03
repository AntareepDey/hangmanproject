import random
from tkinter import *
from tkinter import messagebox                      # for all other info
from tkinter import simpledialog                    #takes input

score = 0
run = True

# main loop
while run:
    #making the main game window parameters
    root = Tk()
    root.geometry('1060x720')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing word
    file = open('words.txt','r')
    l = file.readlines()
    for i in range(0,len(l)):
        l[i] = l[i].strip('\n')
    selected_word =random.choice(l)
    print(selected_word)
        
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #letters icon
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    button = [['b1','a',10,540],['b2','b',90,540],['b3','c',170,540],['b4','d',250,540],['b5','e',330,540],['b6','f',410,540],['b7','g',490,540],['b8','h',570,540],['b9','i',650,540],['b10','j',730,540],['b11','k',810,540],['b12','l',890,540],['b13','m',970,540],['b14','n',10,590],['b15','o',90,590],['b16','p',170,590],['b17','q',250,590],['b18','r',330,590],['b19','s',410,590],['b20','t',490,590],['b21','u',570,590],['b22','v',650,590],['b23','w',730,590],['b24','x',810,590],['b25','y',890,590],['b26','z',970,590]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))
    # placement of first hangman image
    c1.place(x = 300,y =- 50)
    
    # exit buton
    def close():
        global run         
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
    # input name
    na=simpledialog.askstring("name","What is your name:",parent=root)
    na2 = 'Hello '+str(na)
    na1 = Label(root,text = na2,bg = "#E7FFFF",font = ("arial",20))
    na1.place(x = 10,y = 10)
    #exit button        
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=930,y=10)
    #score
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",20))
    s1.place(x = 10,y = 40)
    
    

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    score += 10                     
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
                s2 = 'SCORE:'+str(score)
                s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",20))
                s1.place(x = 10,y = 40)
                                
            if win_count == len(selected_word):
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,300,-50))
            if count == 6:
                ow='The original word was:'+' '+selected_word.upper()
                i=messagebox.showinfo("info",ow)
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()

    

