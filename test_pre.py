""" 
    Write a program to solve the initial value problem (IVP)
    y' = (x^2).(1 + y^2)
    y(1) = 1

    (1) Adam's Bash fourth order pc method
    (2) Milne's fourth order pc method

    perform 5 iterations of corrector take h = 0.01 and calculate the value at [1.4, 1.6]

    use (1) Euler's Method (2) Euler's Modified Method (3) RK 4th order Method
    
"""

# Inputs

h = 0.01           # Step size
dec_factor = 2

target = 1.4       # Target value of x
corr_steps = 5     # Number of Corrections in each Iteration

# Selecting Multi-Step Method

print("1. Adam's Bash Method")
print("2. Milne's Method")

multi_method_list = ['Adam\'s Bash Method', 'Milne\'s Method']
multi_step_method = int(input("\nEnter (1 / 2) for selecting Multi Step Method: "))

print("\n1. Euler's Method")
print("2. Modified Euler's Method")
print("3. RK 4th Order Method")

single_method_list = ['Euler\'s Method', 'Modified Euler\'s Method', 'RK 4th Order Method']
single_step_method = int(input("\nEnter (1 / 2 / 3) for selecting Single Step Method: "))

print("\nMulti-Step Method - {}".format(multi_method_list[multi_step_method - 1]))
print("Single-Step Method - {}\n".format(single_method_list[single_step_method - 1]))

if (multi_step_method == 1):
    if (single_step_method == 1):
        output = open('Adam_Euler.txt', 'w')
        output.write("Multi-Step Method - Adam's Bash Method\n")
        output.write("Single-Step Method - Euler's Method\n")
    elif (single_step_method == 2):
        output = open('Adam_Modified_Euler.txt', 'w')
        output.write("Multi-Step Method - Adam's Bash Method\n")
        output.write("Single-Step Method - Modified Euler's Method\n")
    elif (single_step_method == 3):
        output = open('Adam_RK.txt', 'w')
        output.write("Multi-Step Method - Adam's Bash Method\n")
        output.write("Single-Step Method - RK 4th Order Method\n")

elif (multi_step_method == 2):
    if (single_step_method == 1):
        output = open('Milne_Euler.txt', 'w')
        output.write("Multi-Step Method - Milnes's Method\n")
        output.write("Single-Step Method - Euler's Method\n")
    elif (single_step_method == 2):
        output = open('Milne_Modified_Euler.txt', 'w')
        output.write("Multi-Step Method - Milne's Method\n")
        output.write("Single-Step Method - Modified Euler's Method\n")
    elif (single_step_method == 3):
        output = open('Milne_RK.txt', 'w')
        output.write("Multi-Step Method - Milne's Method\n")
        output.write("Single-Step Methos - RK 4th Order Method\n")

# Functions

# dy / dx  = f(x, y) function given in the question
def f(x, y):
    return round(((x ** 2) * (1 + (y ** 2))), 8)

# Euler's method
def euler(y, f, h):
    return round((y + (h * f)), 8)

# Euler's Modified Method
def euler_mod(y, x, h):
    k1 = f(x, y)
    k2 = f(x + h, (y + (h * k1)))

    return round((y + ((0.5 * h) * (k1 + k2))), 8)

# RK Method
def rk(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + (0.5 * h), y + (k1 * 0.5))
    k3 = h * f(x + (h * 0.5), y + (k2 * 0.5))
    k4 = h * f(x + h, y + k3)
    k = (k1 + (2 * (k2 + k3)) + k4) / 6

    return round((y + k), 8)

# Adam Bash Fourth Order PC
# Predictor Function
def adam_pred(y, fn, fn_1, fn_2, fn_3, h):
    return round((y + ((h / 24) * ((55 * fn) - (59 * fn_1) + (37 * fn_2) - (9 * fn_3)))), 8)

# Corrector Function
def adam_corr(y, fn_2, fn_1, fn, f, h):
    return round((y + ((h / 24) * (fn_2 - (5 * fn_1) + (19 * fn) + (9 * f)))), 8)

# Milne's Fourth Order PC
# Predictor Function
def milne_pred(y, h, fn_3, fn_2, fn_1):
    return round((y + (((4 * h) / 3) * ((2 * fn_3) - fn_2 + (2 * fn_1)))), 8)

# Corrector Function
def milne_corr(y, h, fn_2, fn_3, f):
    return round((y + ((h / 3) * (fn_2 + (4 * fn_3) + f))), 8)

# Display Function for debugging code
def stat():
    print(temp_x)
    print(temp_y)
    print(temp_f)

# Single Step Method

index = 0
x = 1
temp_x = [x]             # temp_x[0] = x0
temp_y = [1, 0, 0, 0]    # temp_y[0] = y(x0) = y0
temp_f = [2, 0, 0, 0]    # temp_f[0] = f(x0, y0)

print('---- Single Step Method ----')
output.write("\n---- Single Step Method ----\n")

print()
output.write("\n")

print("y{3} = y({0}) = {1}, f({0}, {1}) = {2}".format(temp_x[0], temp_y[0], temp_f[0], index))
output.write("y{3} = y({0}) = {1}, f({0}, {1}) = {2}\n".format(temp_x[0], temp_y[0], temp_f[0], index))

for i in range(1, 4):
    x += h
    index += 1
    temp_x.append(round(x, dec_factor))

    if (single_step_method == 1):
        temp_y[i] = euler(temp_y[i - 1], temp_f[i - 1], h)  # y1 = y0 + h * f(x0, y0)
        temp_f[i] = f(temp_x[i], temp_y[i])
    elif (single_step_method == 2):
        temp_y[i] = euler_mod(temp_y[i - 1], temp_x[i - 1], h)
        temp_f[i] = f(temp_x[i], temp_y[i])
    elif (single_step_method == 3):
        temp_y[i] = rk(temp_x[i - 1], temp_y[i - 1], h)
        temp_f[i] = f(temp_x[i], temp_y[i])

    print("y{3} = y({0}) = {1}, f({0}, {1}) = {2}".format(temp_x[i], temp_y[i], temp_f[i], index))
    output.write("y{3} = y({0}) = {1}, f({0}, {1}) = {2}\n".format(temp_x[i], temp_y[i], temp_f[i], index))

print()
output.write("\n")

# Multi Step Method

output.write("---- Multi-Step Method ----\n\n")
print("---- Multi-Step Method ----")

steps = int(target * (10 ** dec_factor)) - int(temp_x[3] * (10 ** dec_factor))

for i in range(4, (4 + steps)):
    index += 1
    x += h
    temp_x.append(round(x, dec_factor))

    # temp_f = [fn_3, fn_2, fn_1, fn_0] = [f_0, f_1, f_2, f_3] = [0, 1, 2, 3]

    if (multi_step_method == 1):
        temp_y.append(adam_pred(temp_y[3], temp_f[3], temp_f[2], temp_f[1], temp_f[0], h))
        del temp_y[0]
        del temp_x[0]

        print("y(p){2} = y({0}) = {1}, f({0}, {1}) = {3}".format(temp_x[3], temp_y[3], index, f(temp_x[3], temp_y[3])))
        output.write("y(p){2} = y({0}) = {1}, f({0}, {1}) = {3}\n".format(temp_x[3], temp_y[3], index, f(temp_x[3], temp_y[3])))

        index_j = 0

        for j in range(corr_steps):
            index_j += 1
            temp_y[3] = adam_corr(temp_y[2], temp_f[1], temp_f[2], temp_f[3], f(temp_x[3], temp_y[3]), h)
            print("y(c{3}){2} = y({0}) = {1}, f({0}, {1}) = {4}".format(temp_x[3], temp_y[3], index, index_j, f(temp_x[3], temp_y[3])))
            output.write("y(c{3}){2} = y({0}) = {1}, f({0}, {1}) = {4}\n".format(temp_x[3], temp_y[3], index, index_j, f(temp_x[3], temp_y[3])))

        temp_f.append(f(temp_x[3], temp_y[3]))

        del temp_f[0]
        # del temp_x[0]
    elif (multi_step_method == 2):
        temp_y.append(milne_pred(temp_y[0], h, temp_f[3], temp_f[2], temp_f[1]))
        del temp_y[0]
        del temp_x[0]

        print("y(p){2} = y({0}) = {1}, f({0}, {1}) = {3}".format(temp_x[3], temp_y[3], index, f(temp_x[3], temp_y[3])))
        output.write("y(p){2} = y({0}) = {1}, f({0}, {1}) = {3}\n".format(temp_x[3], temp_y[3], index, f(temp_x[3], temp_y[3])))
        
        index_j = 0

        for j in range(corr_steps):
            index_j += 1
            temp_y[3] = milne_corr(temp_y[1], h, temp_f[2], temp_f[3], f(temp_x[3], temp_y[3]))
            print("y(c{3}){2} = y({0}) = {1}, f({0}, {1}) = {4}".format(temp_x[3], temp_y[3], index, index_j, f(temp_x[3], temp_y[3])))
            output.write("y(c{3}){2} = y({0}) = {1}, f({0}, {1}) = {4}\n".format(temp_x[3], temp_y[3], index, index_j, f(temp_x[3], temp_y[3])))

        temp_f.append(f(temp_x[3], temp_y[3]))

        del temp_f[0]

    print()
    output.write("\n")

    print("y{3} = y({0}) = {1}, f({0}, {1}) = {2}\n".format(temp_x[-1], temp_y[-1], temp_f[-1], index))
    output.write("y{3} = y({0}) = {1}, f({0}, {1}) = {2}\n\n".format(temp_x[-1], temp_y[-1], temp_f[-1], index))

output.close()

quit = input("Press any Key to Quit")
