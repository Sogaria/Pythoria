def args_test(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
    
args_test(1, 2, 3, 4, 5)