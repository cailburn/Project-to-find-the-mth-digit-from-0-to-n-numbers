n = int(input("Input the value of n: "))
l = int(input("Enter the digit index to find (1-based): "))

digits = []
sr = []  # parallel list: sources[i] is the number that produced digits[i]

for num in range(1, n + 1):
    for ch in str(num):        # convert each number to its digits without using .join
        digits.append(int(ch))
        sr.append(num)

if l < 1 or l > len(digits):
    print(f"Index out of range. There are only {len(digits)} digits from 1 to {n}.")

print(digits)
print(digits[l - 1])
print("The", l, "th digit is from the number", sr[l - 1])
