grades=['A','B','A','C','F','F']
#filter to hide gred F

#using function
def remove_fails(grade):
    return grade!='F'
    
print(list(filter(remove_fails,grades)))
#filter(testing_function,grades)


#using for loop
filtered_grades=[]
for grade in grades:
    if grade!='F':
        filtered_grades.append(grade)
print(filtered_grades)

#using comprehension
print([grade for grade in grades if grade!='F'])