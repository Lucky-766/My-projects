def test_range(n):
    if n in range(1,100):
        print(n,"is in the range")
    else:
        print(n,"is out of range")
min_value=int(input())
max_value=int(input())
n=int(input("Enter the number you want to check:"))
test_range(n)
