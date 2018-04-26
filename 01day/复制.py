#1.txt
file_name=input("请输入文件名要带后缀名")
old_name=open(file_name,"r")
content =old_file.read()

new_file=open(file_name+"复制","w")
new_file.write(content)


old_file.colse()
new_file.colse()
