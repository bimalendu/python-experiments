num_list = [1,2,3,"4",None,[6,58,19]]
num_list.append(100)
print(num_list)  #[1,2,3,”4”,None,[6,58,19],100]
print(len(num_list)) #7
print(num_list.pop()) #100
print(num_list.count(3)) #1
print(num_list.index(3)) #2
num_list.remove(1) 
print(num_list)#[2,3,”4”,None,[6,58,19]]
print(2 in num_list) #True
print(19 in num_list) #False
num_list.extend([5,9,8,0]) #[2,3,”4”,None,[6,58,19],5,9,8,0]
print(num_list + [7,22,0]) #[2,3,”4”,None,[6,58,19],5,9,8,0,7,22,0]
print(num_list) #[2,3,”4”,None,[6,58,19],5,9,8,0]