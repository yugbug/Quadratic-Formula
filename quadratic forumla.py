a = input("what will the value for a be?")
b = input("what will the value for b be?")
c = input("what will the value for c be?")

dis_crim = int(b) ** 2 - 4 * int(a) * int(c)
print("The discriminant is " + str(dis_crim))

if dis_crim < 0:
    print("There aren't any real world solutions to the function.")
    exit(0)

the_top_of_function_positive = int(dis_crim) ** 0.5 + int(b) * -1

bottom = 2 * int(a)

top = the_top_of_function_positive
bot = bottom

pos_root = top / bot

if dis_crim != 0:
    print("One root of the function is " + str(pos_root))
else:
    print("The only root of the function is " + str(pos_root))

negative_discrim = (int(dis_crim) ** 0.5) * -1

the_top_of_function_negative = negative_discrim + (int(b) * -1)

toptwo = the_top_of_function_negative
neg_root = toptwo / bot



if pos_root != neg_root:
    print("The other root is " + str(neg_root))

