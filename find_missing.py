def find_missing(input):
    max_element,element_sum = find_max_element_sum(input)
    return find_real_sum(max_element) - element_sum

def find_real_sum(max_element):
    return ((1 + max_element)/2) * max_element

def find_max_element_sum(input):
    element_sum = 0
    max_element = 0
    for i in range(len(input)):
        element_sum = element_sum + input[i]
        if(input[i] > max_element):
            max_element = input[i]
    return max_element,element_sum    

print(find_missing([3,7,1,2,8,4,5]))