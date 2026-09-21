# Basic Programming & Precision Arithmetic 

# 1.
#from math import *
#a,b = int(input()), int(input())
#c = sqrt(a**2 + b**2)
#angle1 = degrees(atan(b/a))
#angle2 = degrees(atan(a/b))
#print(f'Hypotenuse = {c:.1f}, Angle1 = {angle1:.2f} deg, Angle2 = {angle2:.2f} deg')

# 2. A = P * (1 + R/100*n)**(n*t)
#p, r, t, n = int(input('P: ')), int(input('R: ')), int(input('t: ')), int(input('n: '))
#a = p * (1 + r/(100*n))**(n*t) - p
#print(f'Compound Interest = {a:.2f}')

# 3.
#x1,y1,x2,y2=int(input()), int(input()), int(input()), int(input())
#print(f'Distance = {(((x2-x1)**2 + (y2-y1)**2)**(1/2)):.1f}')

# 4.
#n=int(input())
#print(f'100$: {n//100}, 50$: {(n-(n//100)*100)//50}, 20$: {(n-((n//100)*100+((n-(n//100)*100)//50)*50))//20}, 10$: {(n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20))//10}, 5$: {(n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20 + ((n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20))//10)*10))//5}, 1$: {(n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20 + ((n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20))//10)*10 + ((n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20 + ((n-((n//100)*100 + ((n-(n//100)*100)//50)*50 + ((n-((n//100)*100+((n-(n//100)*100)//50)*50))//20)*20))//10)*10))//5)*5))//1}')

# 5.
#n=input()
#print(f'Tens = {n[-2]}, Hundreds = {n[-3]}')

# 6. Surface Area (Total): A = 2(pi)rh + 2(pi)r**2 ; Volume: V = (pi)(r**2)h
#from math import *
#r,h=int(input()), int(input())
#print(f'Surface Area = {(2*pi*r*h + 2*pi*(r**2)):.2f}, Volume = {(pi*(r**2)*h):.2f}')

# 7.
#n=list(map(int,input().split()))
#if n[0]+n[1]>n[2] and n[1]+n[2]>n[0] and n[2]+n[0]>n[1]:
#    print('Valid Triangle')
#else:
#    print('Invalid Triangle')

# 8.
#n=int(input())
#print(f'{n//1440} day(s), {(n%1440)//60} hour(s), {n%30} minute(s)')

# 9.
#a,b=int(input()),int(input())
#print(f'AND = {a & b}, OR = {a | b}, XOR = {a ^ b}, Shift = {a << b}')

# 10.
#a,b,c=int(input()),int(input()),int(input())
#print(f'Root 1 = {((-b+(b**2-4*a*c)**(1/2))/2*a):.1f}, Root 2 = {((-b-(b**2-4*a*c)**(1/2))/2*a):.1f}')

# 11.
#print(int(input())//10*10+10)


# Conditions

# 12.
#n=[int(i) for i in input().split()]
#if n.count(n[0]) == 3:
#    print('Equilateral')
#elif n.count(n[0]) == 2 or n.count(n[1]) == 2:
#    print('Isosceles')
#else:
#    print('Scalene')

# 13.
#n=int(input())
#tax=0.0
#if n > 30000:
#    tax+=(n-30000)*0.2
#    n=30000
#if n > 10000:
#    tax+=(n-10000)*0.1
#print(f'Total Tax = {tax:.1f}')

# 14.
#n1,n2=int(input('Hours = ')),int(input('Minutes = '))
#if n1<=24 and n2<=60:
#    print('Valid Time')
#else:
#    print('Invalid Time')

# 15.
# def find_quadrant(x, y):
#    if x > 0 and y > 0:
#        return "Quadrant 1"
#    elif x < 0 and y > 0:
#        return "Quadrant 2"
#    elif x < 0 and y < 0:
#        return "Quadrant 3"
#    elif x > 0 and y < 0:
#        return "Quadrant 4"
#    elif x == 0 and y != 0:
#        return "Y-axis"
#    elif y == 0 and x != 0:
#        return "X-axis"
#    else:
#        return "Origin"
# print(find_quadrant(int(input()), int(input())))

# 16.
# n=float(input())
# s=n
# c=0
# if s>100:
#     c+=100*0.5
#     s-=100
# if s>100:
#     c+=100*0.75
#     s-=100
# if n>200:
#     c+=s*1.2
# print(f'Total Cost = {c:.1f}')