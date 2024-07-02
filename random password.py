def sumofd(a):
    sum = 0
    while (a != 0): 
        sum = int(sum + (a % 10))
        a = int(a/10)
       
    return sum
def random_password(data,len1,opt):
    for i in opt:
        i=int(i)
        x=int((len1/len(opt)))+(len1%len(opt))
        #print(x)
        for j in range(1,x):
            lower=((len1*len(data[i-1])*11)+(i*j+1))%len(data[i-1])
            res=data[i-1][lower]
            print(data[i-1][lower],end="")  
    return res        
data=[["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["1","2","3","4","5","6","7","8","9","0"],["!","@","#","$","%","^","&","*","(",")","-","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","_","`","~"]] 
len1=int(input("enter the password length you want :"))
print("enter the specification you want for password \n 1.uppercase \n 2.lowercase \n 3.numbers \n 4.special characters \n enter the option numbers seperated by spaces :")
opt=list(input())
for i in opt:
    if i==" ":
        opt.remove(" ")   
random_password(data,len1,opt)

    