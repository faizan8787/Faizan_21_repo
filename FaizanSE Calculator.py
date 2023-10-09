def calculator(x, y, sign):
    if sign == '+':
        return x + y
    elif sign == '-':
        return x - y
    elif sign == '*':
        return x * y
    elif sign == '/':
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operator"

# Example usage:
x=int(input('Enter a Number'))
y=int(input('Enter second Number'))
sign=input('Enter Sign')
result = calculator(x, y, sign)
print(f"{x} {sign} {y} = {result}")
