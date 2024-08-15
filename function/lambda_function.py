# ---
def lambda_handler(event, context):
    out = ""
    if not 'body' in event or event['body'] is None:
        out = "Post body required (must be an integer)"
    else:
        try:
            fib = int(event['body'])
            out = fibonacci(fib)
        except ValueError:
            out = "Post body must be an integer"
    return {"statusCode": 200, "body": f"{out}"}

def fibonacci(n):
    """Iterative Fibonacci algorithm"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    previous = 0
    last = 1
    for i in range(2, n + 1):
        acc = last + previous
        previous = last
        last = acc
    return acc

for i in range(0, 10):
    print(f"{i}: " + lambda_handler({'body': None}, {} )["body"])
