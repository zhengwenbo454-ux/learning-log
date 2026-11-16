def calculate(a, /, b, *args,op="+", precision):
    total = a + b
    for num in args:
        total += num
    result = round(total, precision)
    return result
 
 
if __name__ == "__main__":

    result = calculate(1,2,3,4, precision = 2)
    print(result)