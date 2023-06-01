string_1 = "Hello World!"

print("For Loop")
for iter_var in string_1:
    print("The character reached during the traversal is: ", iter_var)
    
    
# nest For loops
list_1 = [1, 2, 3]

list_2 = ['Apple', 'Orange', 'Guava']

print("Nested For Loop")
for iter_var1 in list_1:
    print(iter_var1)
    
    for iter_var2 in list_2:
        print(iter_var2)
        
        
print("Using Break statement in a For loop")
list_3 = ['Apple', 'Orange', 'Mango', 'Guava', 'Banana']

print(list_3)

for iter_var1 in list_3:
    if ( iter_var1 == 'Guava'):
        break
    else:
        print(iter_var1)
    