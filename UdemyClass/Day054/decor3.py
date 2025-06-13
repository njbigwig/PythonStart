import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper_function():
      start_time = time.time()
      function()
      end_time = time.time()
      print(end_time-start_time)
  return wrapper_function
      
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
fast_function()        

@speed_calc_decorator
def slow_function():
  for i in range(100000000):
    i * i
slow_function()