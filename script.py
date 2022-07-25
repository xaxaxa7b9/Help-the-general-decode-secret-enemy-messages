import string


def encode(s):
  charList=[]
  encrypted = []

  
  charList.append("æ") #just blank place for index 0
  for x, y in zip(range(1, 64), string.ascii_letters+string.digits):
      charList.append(y)
      
 
    
  charList.append('æ') #dk
  charList.append(',')
  charList.append('.')
  charList.append(' ')
  charList.append('æ') #dk
  
  exceptions = ['!','@','#','$','%','^','&','*','(',')','_','+','-','~']

  #encoding
  
  for j in range(1,len(s)+1):
    if exceptions.count(s[j-1]) > 0:
        encrypted.append(s[j-1])
    for el in charList:
      if el == s[j-1]:
        encrypted.append((charList.index(el)*(2**j)) % 67)
        
  
  for i in encrypted:
    if(type(i) == str):
      print(i, end="")
    else:
      print(charList[i], end="")


toEncode = "Hello World!"

encode(toEncode)






#(i+(2^j-1)*i)%67
#i*2^j

#where i = character index
#      j = letter position ("abc" a=1,b=2,c=3 position)



#a=1
#b=2
#c=3
#d=4
#e=5
#f=6
#g=7
#h=8
#i=9
#j=10
#k=11
#l=12
#m=13
#n=14
#o=15
#p=16
#q=17
#r=18
#s=19
#t=20
#u=21
#v=22
#w=23
#x=24
#y=25
#z=26
#A=27
#B=28
#C=29
#D=30
#E=31
#F=32
#G=33
#H=34
#I=35
#J=36
#K=37
#L=38
#M=39
#N=40
#O=41
#P=42
#Q=43
#R=44
#S=45
#T=46
#U=47
#V=48
#W=49
#X=50
#Y=51
#Z=52
#0=53
#1=54
#2=55
#3=56
#4=57
#5=58
#6=59
#7=60
#8=61
#9=62
#no idea = 63
#,=64
#.(?)=65
#space=66
#no idea = 67

