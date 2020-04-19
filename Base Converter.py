import math
num = input("What number would you like to convert bases with?")
oldbase = int(input("What base is that number in?"))
newbase = int(input("What base would you like to turn it into?"))
numbers = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbersdict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}
actualnum = 0
finalnum = ""
for i in range(len(num)):
    actualnum+=numbersdict[num[i]]*(oldbase**(len(num)-i-1))
for i in range(int(math.log(actualnum,newbase))+1):
    finalnum+=numbers[int((actualnum%(newbase**int(math.log(actualnum,newbase)-i+1)))/(newbase**int(math.log(actualnum,newbase)-i)))]
print(finalnum)
