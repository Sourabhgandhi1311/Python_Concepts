# [djaslkdjalskdsldjvads21873298743qaddjals]
# 1. Count each element
# 2. Print the count in descending

inp_str = "djaslkdjalskdsldjvads21873298743qaddjals"
count_dict = {}
for i in inp_str:
    if i in count_dict.keys():
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)
def samp(item):
    return item[1]
# print(sorted(count_dict.items(), key = lambda item: item[1], reverse=True))
for k,v in sorted(count_dict.items(), key = samp, reverse=True):
    print(k,v)