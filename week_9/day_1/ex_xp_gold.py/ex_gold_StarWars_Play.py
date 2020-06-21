exec(open(r"ex_gold_StarWars.py").read())


Jedi1=Jedi("Jane")
Jedi2=Jedi("John")
Jedi3=Jedi("Julie")

jedi_list=[]
jedi_list.append(Jedi("Jane"))
jedi_list.append(Jedi("John"))
jedi_list.append(Jedi("Julie"))
print("The Jedis are:",jedi_list[0].name+",",jedi_list[1].name+",",jedi_list[2].name)

sith_list=[]
sith_list.append(Sith("Same"))
sith_list.append(Sith("Seth"))
sith_list.append(Sith("Simone"))
print("The Siths are:",sith_list[0].name+",",sith_list[1].name+",",sith_list[2].name+"\n")

num_fights=0
while True:
    import random
    randomJ=random.randint(0,len(jedi_list)-1)
    randomS=random.randint(0,len(sith_list)-1)
    random_attack=random.randint(0,1)
    print("\n\nJedi/Sith Fight About to Start!!!")
    if random_attack==0:
        winner=sith_list[randomS].fight_method(jedi_list[randomJ])
    if random_attack==1:
        winner=jedi_list[randomJ].fight_method(sith_list[randomS])
    if "Darth" in winner.name:
        print("Sith {} won!!!".format(sith_list[randomS].name))
        sith_list[randomS].train()
        jedi_list[randomJ].train()
    else:
        print("Jedi {} won!!!".format(jedi_list[randomJ].name))
        print("Sorry Sith {}. You died.".format(sith_list[randomS].name))
        jedi_list[randomJ].train()
        sith_list.pop(randomS)
   
    if num_fights>100 and len(sith_list)>0:
        print("Destroy all Siths before they take over the Galaxy!!!")
    elif len(sith_list)==0:
        print("Jedis won! The Siths are dead!")
        break
    if num_fights>1000:
        print("Oh, no! The Siths have won!")
        break
    num_fights+=1
    
