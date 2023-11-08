inp=int(input("Enter the number of split words"))
list_new=[]
for k in range(inp):
    x=input("Enter the input")
    list_new.append(x)
#list_new = ['ABCD', 'SNU_', 'U_CH', 'CHEN', 'ENNA', 'NAI.', 'CDEF']
def rec_ai():
    
    for i in range(len(list_new)):
        for j in range(len(list_new)):
            if i != j and list_new[i][-2:] == list_new[j][:2]:
                list_new[i] = list_new[i] + list_new[j][2:]
                list_new.pop(j)
                #rec_ai()
                return 
rec_ai()
print(list_new)
