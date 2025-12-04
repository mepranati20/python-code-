# Given two lists of numbers called secret and key, use the following steps to decode the message.

# Get the absolute value of each number in secret
# For each index add the number in key to the result of step 1
# Reverse the order of the numbers in the result of step 2
# Use integer division to divide each number in the result of step 3 by 5
# Add the index of each number in step 4 to its value
# Convert each value to a character
# use ''.join(list) to convert a list of characters to a string
secret = [-12, 7, -25, 30, -3] 
key = [3, -2, 10, 4, 1]        
step1 = [abs(n) for n in secret]
step2 = [step1[i] + key[i] for i in range(len(secret))]
step3 = step2[::-1]
step4 = [n // 5 for n in step3]
step5 = [step4[i] + i for i in range(len(step4))]
chars = [chr(n) for n in step5]
message = ''.join(chars)
print(message)