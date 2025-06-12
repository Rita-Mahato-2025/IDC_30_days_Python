import time
from functools import wraps

# Decorator definition
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

# Function to test
@log_execution_time
def wait_two_seconds():
    time.sleep(2)
    print("Finished waiting")

# Main block to run the code
if __name__ == "__main__":
    wait_two_seconds()