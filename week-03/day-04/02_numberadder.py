# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def recursive(n):
    if n == 1:
        return 1
    return n + recursive(n - 1)

print(recursive(10))
