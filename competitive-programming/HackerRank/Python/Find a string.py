def count_substring(string, sub_string):
    count=0
    i=string.find(sub_string)
    while(i != -1):
        count+=1
        i=string.find(sub_string,i+1)
    return count
