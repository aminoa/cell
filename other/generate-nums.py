import random

# List of available numbers
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

# Initialize the result list with 0s
result_list = [0] * 5004

# Generate 5004 bytes in groups of 12
for i in range(0, len(result_list), 12):
    random_number = random.choice(number_list)
    random_index = random.randint(0, 11)
    result_list[i + random_index] = random_number

# Print the result list (first 60 bytes as an example)
print(result_list[:60])

# write this list to a file called "numbers.txt" in a list format
with open("numbers.txt", "w") as f:
    f.write(str(result_list))
    