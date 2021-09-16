number_of_shoes=int(input())
shoes_sizes=list(map(int, input().split()))
number_of_customers=int(input())
s=0
for i in range(number_of_customers):
    shoes_size, price = map(int, input().split())
    if(shoes_size in shoes_sizes):
        shoes_sizes.remove(shoes_size)
        s=s+price
print(s)
