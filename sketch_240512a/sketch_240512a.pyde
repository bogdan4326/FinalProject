img=0
mode=12
col1 = color(139,71,28)
col2 = color(139,71,28)

def setup():
    global img
    size(1000,600)
    img=loadImage("focsi.jpeg")

def draw():
    global  col1, col2
    
    fill(col1)
    rect(150,50,320,500)
    ellipse(220, 290, 60, 60)
    
    fill(col2)
    rect(500,50,320,500)
    ellipse(580, 290, 60, 60)
    
    
    
   
    if mode ==1:
        
        image(img, 0, 0, 1000, 600)
        fill(255)
        textSize(20)
        text(u"проиграл", 300,300)  
        noLoop()
        
    if mode ==2:
        fill(255)
        textSize(20)
        text(u"Ты выграл", 700,300)
        noLoop()
        
def mouseClicked(): 
    global col1, col2,mode
    
    if mouseX > 150 and mouseX < 470 and mouseY > 50 and mouseY < 550:
        mode=1
        col1 = color(0,0,0)
    
    if mouseX > 500 and mouseX < 820 and mouseY > 50 and mouseY < 550:
        mode=2
        col2 = color(0,0,0)
        
        
    fill(255)
    textSize(20)
    text(u"Ты выграл", 700,300)
