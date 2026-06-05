nums = [1,2,3,4,5,7,8,9,10]

n =10

expected_sums = n * (n+1)//2
actual_sums = sum(nums)

missing = expected_sums-actual_sums

print("Missing number",missing)