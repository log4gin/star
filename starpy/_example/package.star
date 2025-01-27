package_name := load('_example/type.star')

print(' i am load package ' ,package_name)

result := eval(' a := 22 , b := 33, (a + b) ')

print(result)
