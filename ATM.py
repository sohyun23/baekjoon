n = int(input())
peoples = list(map(int, input().split()))
p = [3, 1, 4, 3, 2]
sorted_p = sorted(p)
# print(sorted_p)
count = list(reversed([i+1 for i in range(len(p))]))
# print(count)

dict_sort = dict(zip(count,sorted_p))
# print(dict_sort)

sum_minimize=sum([key*val for key, val in dict_sort.items()])

print(sum_minimize)
