in_ = input("Enter Rows (odd number) and Columns (Rows *3)>> ")
in_ = list(map(int, in_.split()))
n = in_[0]
m = in_[1]

for i in range(1,n,2):
    print("-"*((m-(i*3))//2), end="")
    print(".|."*(i), end="")
    print("-"*((m-(i*3))//2))
print("-"*((m-7)//2),end="")
print("WELCOME", end="")
print("-"*((m-7)//2))
for i in range(n-2,0,-2):
    print("-"*((m-(i*3))//2), end="")
    print(".|."*(i), end="")
    print("-"*((m-(i*3))//2))
