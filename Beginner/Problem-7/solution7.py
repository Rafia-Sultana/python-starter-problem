def fizz_buzz(number):
    if number%3 == 0 and number%5 == 0:
        return "FizzBuzz"
    elif number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

print(fizz_buzz(15))
print(fizz_buzz(9))