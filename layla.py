with open("students.txt", "w") as file: 
file.write("Layla\nAlessandro\nMarlee\nTao\nJoseph\nRafael\nMaisie\nOliver\nSelma\nBram\nBayne\nLetlotlo\nLida\nOliver\nAmelia\nBen\nTara\nLeila\nSofia\nHarry\nJolie\nKen\nAxel\n") 
 
with open("students.txt", "r") as file: 
for line in file: 
print(line.strip()) 
 
with open("students.txt", "r") as file: 
for line in file: 
print(line[1]) 
with open("students.txt", "r") as file: 
for line in file: 
if (len(line)>6): 
print(line) 
input =  
with open("students.txt", "a") as file: 
file.write("input") 
 
 
