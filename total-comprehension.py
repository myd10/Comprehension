# total-comprehension.py
#list exercise before finising groceries-exercise

#start
my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

#using mapping capabilities to multiply each number by 100

mapped_list = [n *100 for n in my_numbers]

print("----------")
print("Mapped List: ", mapped_list )

# Use filtering capabilities to return only the numbers greater than three

def greater_than_three(n):
    return n >3

filtered_list = list(filter(greater_than_three, my_numbers))

print("----------")
print("Filtered list: ", filtered_list)

#Use filtered capabilites to return only the numbers greater than eight

def greater_than_eight(n):
    return n >8

morethan_eight = list(filter(greater_than_eight, my_numbers))

print("-----------")
print("Filtered List take two: ", morethan_eight)

#use mapping and filtering cpabilites to return only the numbers greater than 3, each multipled by 100

#def greater_than_three(n):
  #  return n >3

final_list = list(filter(greater_than_three, my_numbers))

mapped_list_two = [n*100 for n in final_list]

print("-----------")
print("Mapped and Filtered: ", mapped_list_two)


print("-----------")
print("YAY! Good job, Michael")