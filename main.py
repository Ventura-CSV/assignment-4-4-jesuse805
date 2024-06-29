def main():

    numbers = []

    for i in range(5):
        while True:
            try:
                num = float(input(f'Enter number {i+1}'))
                numbers.append(num)
                break
            except ValueError:
                print('Invalid Input, Try Again')
        
    if numbers:
        minval = numbers[]
        maxval = numbers[]
        
                
                









    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
