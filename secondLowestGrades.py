
names = []                                          # list for names
grades = []                                         # list for grades                    
rec = []                                            # list for joining names and grades
res = []                                            # list for storing filtered names 

size = int (input ("Size = "))
for i in range (size):
    name = input ("name :")
    names.append (name)
    
    grade = float (input ("grade = "))
    grades.append (grade)

rec = names + grades

newGrades  = grades.copy ()                         # grade are copied to a new list
    
newGrades.sort ()                                   # sort copied grades

count = 1
for i in range (1, size):
   if newGrades [0] == newGrades [i]:
        count+=1                                    # get  the index of the second lowest grade
        
#newGrades.pop (0)

#print (newGrades [count])

for i in range (4, len (rec)):
    if rec [i] == newGrades [count]:                # find for other second lowest values
        res.append (rec [i-size])                   # names of the second lowest grades are stored

res.sort ()                                         # Sort the filtered names

for i in res:
    print (i)                                       # print line by line