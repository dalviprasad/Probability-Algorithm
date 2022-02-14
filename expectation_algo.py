# Code for 1st Person
# Sample Space of rolling a dice
cut1 = [1,2,3,4,5,6]
# cut when the dice rolls a even number
x1 = [0,1,0,1,0,1]
# Probability of success
px1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
# Area of Square = square of side
# Expectation of X ie E(X) = x*P(x)*(side**2)
area1 = 0
for i in range(len(x1)):
    area1 = area1 + (x1[i]*px1[i]*(cut1[i]**2))
print("1st Person will cut on an average - {}".format(area1))


# Code for 2nd Person
# Sample Space of rolling a dice
cut2 = [1,2,3,4,5,6]
# cut when the dice rolls a any number
x2 = [1,1,1,1,1,1]
# Probability of success
px2 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
# Area of Rectangle = lenght * breadth
# Expectation of X ie E(X) = x*P(x)*(lenght*breadth)
area2 = 0
for i in range(len(x2)):
    for j in range(len(x2)):
        area2 = area2 + x2[i]*px2[i]*cut2[i]*cut2[j]
print("2nd Person will cut on an average - {}".format(area2))
# They are not equal
# 2nd person cuts the larger area as the 2nd person cuts the area everytime he rolls a dice.
