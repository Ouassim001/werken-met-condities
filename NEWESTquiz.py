import datetime
import time
x = datetime.datetime.now()
print("hallo vandaag is het  " + (x.strftime("%x")))

time.sleep(3)
print("mijn naam is anthony")
time.sleep(2)
print("en vandaag doen we een leuke quiz die ik zelf heb gebouwd samen met oussaime ")
time.sleep(2)
My_list =('ja','jazeker','jawel')
klaar = input("ben je er klaar voor? ").lower()
score = 0

if klaar =="ja":
    print("a bill gates")
    time.sleep(1)
    print("b elon musk")
    time.sleep(1)
    print("c jeff bezos")
    time.sleep(1)
    while True:
        vraag1 = input("wie is de rijkste man ter wereld? ").lower()
    
        if vraag1 =="a":
            print("fout")
            break
        if vraag1 =="b":
            print("correct")
            score = score + 1
            break
            
        if vraag1 =="c":
            print("antwoord fout")
            break
        else:
            print("antwoord of fout getypt of niet correct")
else:
    print("einde")
    
print("a albert einstein")
time.sleep(1)
print("b dirk van de broek")
time.sleep(1)
print("c William sinis")
time.sleep(1)
while True:
    vraag2 =input("wie is de slimste man ter wereld? ").lower()
    if vraag2 =="a":
        print("fout")
        break
    if vraag2 =="c":
        print("correct")
        score = score + 1
        break       
    print(score)
    if vraag2 =="b":
        print("fout")
        break
    else:
        print("je hebt het verkeerd getypt")


print("a je kan  zwemmen zonder je armen")
print("b je kan kinderen krijgen als man")
print('c minecraft bestaat al meer dan 18 jaar')
while True: 
    vraag3 = input("welke van de 3 is waar? ").lower()
    if vraag3 == "a":
        print("correct")
        score = score +1
        vraag19 = input("is de aarde rond")
        if vraag19 == "ja":
            print("correct")
            score = score +1
        else:
            print("fout")
        break
      
    if vraag3 =="b":
        print("fout")
        break
    if vraag3 =="c":
        print("fout")
    
    else:
        print("verkeerd getypt")
print("de langste man van de wereld is")
print("a chinees")
print("b een aziat")
print("c een turk")
while True:
    Vraag4 = input("welke soort persoon is het langs?" ).lower()
    if Vraag4 =="c":
        print("correct")
        score = score + 1
        print('a zwart')
        print('b blauw')
        print("c geel")
        jan = input("welke kleur gebruikt nike")
        if jan =="ja":
            print("correct")
            score = score +1
        else:
            print("fout")
        break
    if Vraag4 =="b":
        print("fout")
        break
    if Vraag4 =="c":
        print("fout")     
        break
    else:
            print("verkeerd getypt")
            
print("a is groen en wit")
print("b is geel en blauw")
print("c is blauw en blauw")
print("d is zwart en geel")
while True:
    vraag6= input("welke kleuren zitten in de python logo? ").lower()
    if vraag6 =="b":
        print("correct")
        score = score +1
        break
    if vraag6 =="c":
        print("fout")
    if vraag6 =="a":
        print("fout")
        break
    if vraag6 =="d":
        print("fout")
        vraag20 = input("hoeveel strepen heeft het adidas logo? ")
        if vraag20 =="3":
            print("correct")
        else:
            print("fout")
            
        break
    else:
        print("verkeerd getypt")
        

print("a is niet gelijk aan")
print("b is kleiner dan")
print("c is gelijk aan")
print("d is groter dan")
while True:
    vraag8 = input("wat betekent ==? ").lower()
    if vraag8 =="c":
        print("correct")
        score = score +1
        break
    if vraag8 =="a":
        print("fout")
        break
    if vraag8 =="d":
        print("fout")
        break
    if vraag8 =="b":
        print("fout")
        break


    else:
        ("verkeerd getypt")

        

print("a is kleiner")
print("b is groter dan")
print("c is evengroot")
print("d is groter")
while True:
    vraag7 = input("wat betekent <? ").lower()
    if  vraag7 =="a":
        print("correct") 
        score = score +1 
        break
    if vraag7 =="c":
        print("fout")
        break
    if vraag7 =="d":
        print("fout")
        break
        
    if vraag7 =="b":
        print("fout")
        break
    else:
        print("verkeerd getypt")
        

print("a is groter")
print("b is kleiner")
print("c is evengroot")
print("d is zwart")

while True:
    vraag9= input("wat betekent >? ").lower()
    if vraag9 =="a":
        print("correct")
        score = score+1
        break
    if vraag9 =="c":
        print("fout")
        break
        
    if vraag9 =="d":
        print("fout")
        break
        
    if vraag9 =="b":
        print("fout")
        break
        

    else:
        print("verkeerd getyped")


print("je hebt" + score, "punten")
if score == 8:
    print("wil je een geheim weten? ")
    time.sleep(2)
    print("de wereld is rond ")
