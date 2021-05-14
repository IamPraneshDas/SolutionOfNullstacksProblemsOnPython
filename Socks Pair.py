# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:43:59 2021
@author: Saikat Datta
"""

def find_pairs(arr,v):
    unique=[]
    for each in arr:                #also can be done using set() function to get unique elements
        if(each not in unique):
            unique.append(each)
    
    count_pair=[]
    
    for each in unique:             #finding number of occurances in the list
        count_pair.append(arr.count(each)) 
    print(count_pair) 
    
    final_count=0
    
    for each in count_pair:         #finding number of pairs
        final_count+=each//2
    return final_count        
            
    """for each in unique:               Alternative method
        pair_count+=arr.count(each)//2
      print(pair_count) 
      """

n=10
sock_list=[10,20,20,10,10,30,50,10,20,20]       
print(find_pairs(sock_list, n)) 