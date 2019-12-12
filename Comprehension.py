#List Comprehension
input_list = [1,0,2,3]
output_list = [i for i in input_list if i%2 == 0]
print("Outpu list using list comprehension is: ",output_list)


#Set Comprehension
set_com = [var for var in input_list if var%2 != 0]
print("output set using set comprehension : ",set_com)


# Dictionary Using forloop
state = ['gujarat','rajsthan']
capital = ['ghandhinagar','jaipur']
output_dic = {}
for(key,value) in zip(state,capital):
    output_dic[key]=value
print("ans:",output_dic)


#using dict comprehension
output_dic = {key:value for(key,value) in zip(state,capital) }
print("ans:",output_dic)

