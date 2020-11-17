from math import gcd

first_up, first_down = map(int, input().split())
second_up, second_down = map(int, input().split())

first_up *= second_down
second_up *= first_down

sum_up = first_up + second_up
sum_down = first_down * second_down

max_common = gcd(sum_up, sum_down)
print(sum_up//max_common, sum_down//max_common)

