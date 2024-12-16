order := load('stdlib/order.star')

max := order.max // 我是中文

print(max(table(1,2,3,4)))



arr := table(23,3424,123,43454,2233,4455,6677,9911)
choose := order.choose

ordered_arr := choose(arr)

copy_arr := copy(arr)

print('ptr of arr',ptr(arr),arr)

print('ptr of ordered arr',ptr(ordered_arr),ordered_arr)

print('ptr of copy arr',ptr(copy_arr),copy_arr)
