# Dictionary :
Languages = {1:"Python", 2:"C", 3:"C++", 4:"Java"}
# Adding an element
Languages[5]="Javascript"
print(Languages)
# Updating an element 
Languages[3]="HTML"
print(Languages)
# Deleting an element
del Languages[4]
print(Languages)
# 4. Deleting an element from it's index
Languages.pop(2)
print(Languages)

# Tuple :

Courses = ("Law","CSE","Design","Mechanical")

# Tuples are immutable

# Lists :

my_list = ["Sanyat","Satyam","Sangakara","Dhoni"]
print(my_list)
# Adding element
my_list.append("Virat")
print(my_list)

# Adding multiple elements 
my_list.extend(["Varun","Dhawan"])
print(my_list)

# Updating an element 
my_list[2]= "Jadeja" 
print(my_list)

# Deleting an element 
my_list.remove("Dhoni")
print(my_list)

# Deleting a specific element
my_list.pop(0)      
print(my_list)

# 6. Reversing a list
my_list.reverse()
print(my_list)
