def remo(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        main_list.pop(index)
    return main_list
main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]
result = remo(main_list, indexes_list)
print(result)



def remove_one_element(list, index):
    if 0 <= index < len(list):  
        list.pop(index) 
        print(list)  
    else:
        print("kaikai kaiakaia ")
kaikaci = [1, 2, 3, 4, 5]
remove_one_element(kaikaci, 2)  


