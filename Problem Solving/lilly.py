# input: [1, 2, 5, 6, 8, 1, 5, 1]
# output: [3, 10]

# input: [2, 4, 2, 3, 4, 4]
# output: [4, 12]

# def count(input_arr):
#     count_dict = {}

#     for i in input_arr:
#         if i in count_dict.keys():
#             count_dict[i] += 1
#         else:
#             count_dict[i] = 1

#     output_arr = []
#     for k,v in count_dict.items():
#         if v > 1:
#             element = k * v
#             output_arr.append(element)

#     return output_arr

# count()


# Employees
# Last 3 records



first_name = ["Ramesh", "Suresh","Dinesh","Jignesh"]
last_name = ["Ramanathan", "Narayana","Sharma","Patel"]
# Output = [Ramesh Ramanathan, Suresh Narayana, Dinesh Sharma, Jignesh Patel]
# print(zip(first_name,last_name))

select emp.first_name from Employee emp 
where joining_date like "%2015"

select sum(emp.salary), emp.department from Employee emp group by emp.department































