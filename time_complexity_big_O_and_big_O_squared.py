import time
import matplotlib.pyplot as plt

def convert_to_dict_method1(string):
    string = list(string)
    new_dict = {}
    for key in string:
        new_dict[key] = string.count(key)
    return new_dict

def convert_to_dict_method2(string):
    string = list(string)
    new_dict = {}
    for key in string:
        new_dict[key] = new_dict.get(key, 0) + 1
    return new_dict

input_sizes = range(1, 1001)
method1_times = []
method2_times = []

for size in input_sizes:
    string = 'a' * size  # Generate a string of length 'size'
    
    # Measure time taken by method 1
    start_time = time.time()
    convert_to_dict_method1(string)
    method1_times.append(time.time() - start_time)
    
    # Measure time taken by method 2
    start_time = time.time()
    convert_to_dict_method2(string)
    method2_times.append(time.time() - start_time)

# Plot the results
plt.plot(input_sizes, method1_times, label='Method 1 (O(n^2)')
plt.plot(input_sizes, method2_times, label='Method 2 (O(n))')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Comparison')
plt.legend()
plt.show()
