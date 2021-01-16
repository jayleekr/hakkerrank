# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {_key:_value for _key,_value in name_numbers}

for _ in range(n):
    _name = input()
    if _name in phone_book:
        print("%s=%s" % (_name, phone_book[_name]))
    else:
        print("Not found")