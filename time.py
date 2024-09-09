import time

l = [1, 2, 3]
start_time = time.time()
l.append(4)
end_time = time.time()
# Calculate the time taken
exe_time = end_time - start_time
print(f"Time taken for append operation: {exe_time} ")
l+=[4]
end_time = time.time()
exe_time = end_time - start_time
print(f"Time taken for  operation: {exe_time} ")
l=l+[4]
end_time = time.time()
exe_time = end_time - start_time
print(f"Time taken for operation: {exe_time} ")

