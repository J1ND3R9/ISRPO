def func(path):
   file = open(path)
   for line in file:
     if 'error' in line.lower():
       yield line
        
def write(lines):
   file = open(r"Quest 12\logs_error.txt", "w")
   for i in lines:
    file.write(i)
    
lines = func(r"D:\ПБ-42к\py\py\Quest 12\log.txt")
write(lines)
print("Готово!")