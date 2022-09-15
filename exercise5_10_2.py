numimax = 0
numimin = 0
nums = []

while True:
    num = input("please enter a number:")
    if num == 'done':
        break;
    else:
        try:
            num = float(num)
            nums.append(num)
        except:
            print("Invalid input!")

for i in nums:
    numimax = int(max(nums))
    numimin = int(min(nums))

print(numimax)
print(numimin)