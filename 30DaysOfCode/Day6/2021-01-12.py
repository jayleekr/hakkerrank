# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases=[]
#1
T=int(input())
for _ in range(T):
    input_str=input()
    even_str=""
    odd_str=""
    for i in range(0,len(input_str)):
        if i % 2 == 0:
            even_str = even_str+input_str[i]
        else:
            odd_str = odd_str+input_str[i]
    print(even_str+ " " + odd_str)
    
