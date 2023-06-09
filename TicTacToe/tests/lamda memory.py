def create_lambda_functions():
    lambdas = []
    for i in range(3):
        # Creating a lambda function that captures the value of `i` for each iteration
        lambdas.append(lambda x=i: x)
    return lambdas


functions = create_lambda_functions()

# Check memory locations of the lambda functions
for func in functions:
    print(hex(id(func)))
