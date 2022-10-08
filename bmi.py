weight = int(input());
height = float(input());
x = weight/float(height*height);
if x < 18.5:
    print('Underweight')
else if x>=18.5 and x<25:
    print("Normal")
else if x >= 25 and x < 30:
   print('Overweight')
else x >= 30:
   print('Obesity')
#use of if-else ladder
#reducing execution time
