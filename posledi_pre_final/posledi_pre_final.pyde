pravo = 0
vniz = 0
def setup():
    background(90,109,160)
    size(800,600)
    
def draw():
    global pravo
    global vniz
    background(90,109,160)
    textSize(25)
    text("proide labirint", 300, 550);
    fill(180,249,255)
    ellipse(pravo,vniz,20,20)
    if keyPressed ==True:
        if key == "d":
            pravo = pravo + 1
                
    
        if key == 's':
            vniz = vniz + 1
            
        if key == "a":
            pravo = pravo - 1
            

            
        if key == "w":
            vniz = vniz - 1
            
    strokeWeight(5)
    point(280,520)
    point(280,600)
    line(280,520,280,600)
    
    point(480,520)
    point(480,600)
    line(480,520,480,600)
    line(280,520,480,520)
    
    point(30,0)
    point(30,60)
    line(30,0,30,60)
    point(65,60)
    line(30,60,65,60)
    point(65,23)
    line(65,60,65,23)
    point(100,23)
    line(65,23,100,23)
    point(125,23)
    line(100,23,125,23)
    point(125,60)
    line(125,23,125,60)
    point(100,60)
    line(125,60,100,60)
    point(100,110)
    line(100,60,100,110)

    
    
    point(170,110)
    line(100,110,170,110)
    point(170,25)
    line(170,110,170,25)
    point(230,25)
    line(170,25,230,25)
    point(290,25)
    
    
    line(230,25,290,25)
    point(290,55)
    line(290,25,290,55)
    point(255,55)
    line(290,55,255,55)
    point(255,90)
    line(255,55,255,90)
    point(230,90)
    line(255,90,230,90)
    point(230,55)
    line(230,90,230,55)
    point(203,55)
    line(230,55,203,55)
    point(203,109)
    line(203,55,203,109)
    point(289,109)
    line(203,109,289,109)
    point(289,143)
    line(289,143,228,143)
    
    print(mouseX,mouseY)
    
    point(0,95)
    point(66,95)
    line(0,95,66,95)
    point(66,143)
    line(66,95,66,143)
    point(98,143)
    line(66,143,98,143)
    point(98,209)
    line(98,143,98,209)
    point(98,235)
    line(98,209,98,235)
    point(228,235)
    line(98,235,228,235)
    point(228,205)
    line(228,235,228,205)
    point(165,205)
    line(228,205,165,205)
    point(165,170)
    line(165,205,165,170)
    
    textSize(25)
    text("Patch pre final", 300, 580);
    point(228,170)
    line(165,170,228,170)
    point(133,170)
    point(133,205)
    line(133,170,133,205)
    point(133,143)
    line(133,205,133,143)
    point(228,143)
    line(133,143,228,143)
    point(228,143)
    point(228,170)
    line(228,143,228,170)
    point(289,275)
    line(289,143,289,275)
    point(327,275)
    line(289,275,327,275)
    point(364,275)
    point(419,275)
    line(364,275,419,275)
    point(419,250) 
    line(419,275,419,250)
    point(458,250)
    line(419,250,458,250)
    point(458,304)
    line(458,250,458,304)
    point(419,220)
    point(490,304)
    line(458,304,490,304)
    point(490,278)
    line(490,304,490,278)
    point(515,278)
    line(490,278,515,278)
    point(515,220)
    line(515,278,515,220)
    line(515,220,419,220)
    point(419,190)
    line(419,220,419,190)
    point(489,190)
    line(419,190,489,190)
    point(489,110)
    line(489,190,489,109)
    line(489,110,288,109)
    point(450,110)
    point(450,155)
    line(450,110,450,155)
    point(419,155)
    line(450,155,419,155)
    point(387,155)
    
    
    point(387,143)
    line(387,155,387,143)
    point(326,143)
    line(387,143,326,143)
    point(326,240)
    line(326,143,326,240)
    point(387,240)
    line(326,240,387,240)
    line(387,240,387,143)
    point(327,275)
    point(327,319)
    line(327,275,327,319)
    point(265,319)
    line(327,319,265,319)
    point(364,275)
    
    
    point(364,319)
    line(364,275,364,319)
    point(364,350)
    line(364,319,364,350)
    point(265,350)
    line(364,350,265,350)
    point(265,277)
    line(264,319,265,277)
    point(118,277)
    line(265,277,118,277)
    
    point(118,311)
    
    
    point(118,365)
    line(118,311,118,365) 
    
    
    point(118,398)
    
    
    point(118,432)
    line(118,398,118,432)
    point(159,432)
    line(118,432,159,432)
    point(159,483)
    line(159,432,159,483)
    point(222,483)
    line(159,483,222,483)
    point(222,454)
    line(222,483,222,454)
    point(187,454)
    line(222,454,187,454)
    point(187,432)
    
    
    line(187,454,187,432)
    point(265,432)
    line(187,432,265,432)
    point(265,384)
    line(265,432,265,384)
    point(414,384)
    line(265,384,414,384)
    point(414,439)
    line(414,384,414,439)
    point(331,439)
    line(414,439,331,439)
    
    point(118,277)
    point(58,277)
    line(118,277,58,277)
    point(58,398)
    line(58,277,58,398)
    point(118,398)
    line(58,398,118,398)
    point(92,365)
    line(118,365,92,365)
    point(92,311)
    line(92,365,92,311)
    line(92,311,118,311)
