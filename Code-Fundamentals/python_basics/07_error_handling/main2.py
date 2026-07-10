import time

try:
    raise ValueError('bad input', 42)
except ValueError as e:
    print('str(e):', str(e))
    print('e.args:', e.args)
    print('type name:', type(e).__name__)

def call_with_retry(func, max_attempts=5):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except ConnectionError as e:
            wait = 2 ** attempt   # exponential backoff: 2, 4, 8, 16...
            print(f'attempt {attempt} failed: {e} -> retrying in {wait}s')
            if attempt == max_attempts:
                print('max attempts reached, giving up')
                raise
            time.sleep(wait)

call_count = 0

def flaky_api_call():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f'server unreachable (call {call_count})')
    return 'success!'

result = call_with_retry(flaky_api_call)
print('result:', result)