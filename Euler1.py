"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""
import time
print("Using brute force")
start_time = time.time()
total = sum([i for i in range(0,1000) if(i%3 == 0 or i%5==0)])
time_taken = time.time() - start_time
print('Total=', total, ' in ', time_taken, ' seconds')

print("Using only multiples of 3 and 5")
start_time = time.time()
total = 0
total += sum([i for i in range(0,1000, 3)])

total += sum([i for i in range(5, 1000, 15)])
total += sum([i for i in range(10, 1000, 15)])
time_taken = time.time() - start_time
print('Total=', total, ' in ', time_taken, ' seconds')