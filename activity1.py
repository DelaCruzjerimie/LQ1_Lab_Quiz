# Team Name
teamName = "svelt"

# Groupmate Names
memberName1 = "Jerimie Dela Cruz"
memberName2 = "Princess Mikylla Daquing"
memberName3 = "Vinico Sumbad"

# Groupmate Ages
memberAge1 = 22
memberAge2 = 20
memberAge3 = 20

# Groupmate Weekly Allowances
memberAllowance1 = 500
memberAllowance2 = 1000
memberAllowance3 = 1000

print(f"Team Name: {teamName}")

print(f"{memberName1}, his age is {memberAge1}, allowance per week is {memberAllowance1}")
print(f"{memberName2}, her age is {memberAge2}, allowance per week is {memberAllowance2}")
print(f"{memberName3}, his age is {memberAge3}, allowance per week is {memberAllowance3}")

# Calculate Name Lengths
memberName1_length = len(memberName1)
memberName2_length = len(memberName2)
memberName3_length = len(memberName3)

# Print Name Lengths
print(f"MEMBER 1 consists of {memberName1_length} characters")
print(f"MEMBER 2 consists of {memberName2_length} characters")
print(f"MEMBER 3 consists of {memberName3_length} characters")

# Age Operations
print("\nAge Operations:")
print(f"Sum of Ages (Member 1, 2, 3): {memberAge1 + memberAge2 + memberAge3}")
print(f"Difference of Ages (Member 1 - Member 2): {memberAge1 - memberAge2}")
print(f"Difference of Ages (Member 2 - Member 3): {memberAge2 - memberAge3}")
print(f"Product of Ages (Member 1 * Member 2 * Member 3): {memberAge1 * memberAge2 * memberAge3}")

# Allowance Operations
print("\nAllowance Operations:")
print(f"Sum of Allowances (Member 1, 2, 3): {memberAllowance1 + memberAllowance2 + memberAllowance3}")
print(f"Difference of Allowances (Member 1 - Member 2): {memberAllowance1 - memberAllowance2}")
print(f"Difference of Allowances (Member 2 - Member 3): {memberAllowance2 - memberAllowance3}")
print(f"Product of Allowances (Member 1 * Member 2 * Member 3): {memberAllowance1 * memberAllowance2 * memberAllowance3}")

# Comparisons
print("\nComparisons:")
print(f"Age Comparison (Member 1 - Member 2): {memberAge1 - memberAge2}")
print(f"Age Comparison (Member 2 - Member 3): {memberAge2 - memberAge3}")
print(f"Name Length Comparison (Member 1 - Member 2): {memberName1_length - memberName2_length}")
print(f"Name Length Comparison (Member 2 - Member 3): {memberName2_length - memberName3_length}")