import useful
# from useful import is_odd

for num in range(1, 25):
    # if is_odd(num):
    if useful.is_odd(num):
        print "%s is odd" % num
    else:
        print "%s is even" % num
