f=open("1.txt","w")
f.write("张晨波\n")
f.close()


f1=open("1.txt","a")
f1.write("世界你好\n")
f1.close()


f2=open("1.txt","r")
f3=f2.read()
f2.close()

f4=open("1.cp.txt","w")
f4.write(f3)
f4.close()

