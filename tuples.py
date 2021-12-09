first_tuple = (1,2,"Hello",100,[101,105])
#first_tuple[1] = 3 #error, not allowed
new_tuple = first_tuple[1],97,first_tuple[4]
print(new_tuple) #(2, 97, [101, 105])
second_tuple = (first_tuple[1],97,first_tuple[4])
print(second_tuple) #(2, 97, [101, 105])
print(first_tuple[4][0]) #101
print(len(first_tuple)) #5
print(first_tuple.count(100)) #1
print(100 in first_tuple)  #True
print(105 in first_tuple)  #False
print(first_tuple.index(2)) #1
print(first_tuple * 5) #repeats the tuple