# Basic Programming & Precision Arithmetic 

# 1.
# from math import *
# a,b = int(input()), int(input())
# c = sqrt(a**2 + b**2)
# angle1 = degrees(atan(b/a))
# angle2 = degrees(atan(a/b))

# angle1 = (b/a) * 180 / pi
# angle2 = (a/b) * 180 / pi

# print(f'Hypotenuse = {c:.1f}, Angle1 = {angle1:.2f} deg, Angle2 = {angle2:.2f} deg')

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

# 9. I need help
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

# 13. I need help
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
# print(f'Total Bill = ${c:.1f}')

# 17.
# n=input()
# sum=0
# for i in n:
#     sum+=int(i)**4

# if sum==int(n):
#     print('Armstrong Number')
# else:
#     print('Not an Armstrong Number')

# 18.
# n1,n2=[int(input()),int(input())],[int(input()),int(input())]
# s1,s2=[i for i in range(n1[0],n1[1]+1)],[i for i in range(n2[0],n2[1]+1)]
# c=0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1[i]==s2[j]:
#             c+=1
# print('Overlapping' if c>0 else 'Non-Overlapping')

# 19. I need help
# from datetime import datetime
# year, month, day = int(input()), int(input()), int(input())
# if datetime(year, month, day):
#     print("Valid Date")
# else:
#     print("Invalid Date")

# 20.
# p1,p2=int(input()),int(input())
# if (p1>p2 and p1!=0 and p2!=0) or (p1>p2 and p1==1 and p2==0) or (p1==0 and p2==2):
#     print('Player 1 Wins')
# elif (p2>p1 and p1!=0 and p2!=0) or (p2>p1 and p1==0 and p2==1) or (p1==2 and p2==0):
#     print('Player 2 Wins')
# else:
#     print('No Winner')

# 21. I used the gemini to solve this problem, but I will provide a solution here as well.

# n = input().split()
# nums = [float(n[i]) for i in range(0, len(n), 2)]
# ops = n[1::2]
# i = 0
# while i < len(ops):
#     if ops[i] in ('*', '/'):
#         if ops[i] == '*':
#             nums[i] = nums[i] * nums[i + 1]
#         else:
#             nums[i] = nums[i] / nums[i + 1]
#         del nums[i + 1]
#         del ops[i]
#     else:
#         i += 1
# res = nums[0]
# for i in range(len(ops)):
#     if ops[i] == '+':
#         res += nums[i + 1]
#     elif ops[i] == '-':
#         res -= nums[i + 1]
# print(f"Result = {int(res) if res.is_integer() else res}")


# For Loop

# 22.
# print(*[i for i in range(1, int(input()) + 1) if i % 3 == 0 and i % 5 == 0])

# 23.
# c=1
# for i in range(1, int(input()) + 1):
#     c*=i
# print(c)

# import math
# print(math.factorial(int(input( ))))

# 24.
# for i in range(1, int(input()) + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# 25.
# s=[]
# for i in range(1, int(input()) + 1):
#     s.append(i**2)
# print(f'Sum = {sum(s)}({"+".join([str(i) for i in s])})')

# 26. I need help
# n=int(input())
# c=0
# l=0
# for i in range(n):
#     c+=1
#     print(i+l, end=' ')
#     l=i
#     if c==len([i for i in range(1, n + 1)]):
#         break
# figonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# print(*figonacci[:n])

# 27.
# print(int(input())**int(input()))

# 28.
# n=int(input())
# print(*[f'{i}x1={i*1} {i}x2={i*2} {i}x3={i*3} {i}x4={i*4} {i}x5={i*5} {i}x6={i*6} {i}x7={i*7} {i}x8={i*8} {i}x9={i*9} {i}x10={i*10}' for i in range(1, n + 1)], sep='\n')

# 29.
# n=int(input())
# c=0
# l=[]
# for i in range(1, n + 1):
#     for j in range(1, i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         l.append(i)
#     c=0
# print(f'Prime Count = {len(l)} ({", ".join([str(i) for i in l])})')

# 30.
# for i in range(int(input()), 0, -1):
#     print((i*2-1)*'*')

# 31.
# c=0
# for i in range(1, int(input()) + 1):
#     c+=1/i
# print(f'Sum = {c:.4f}')


# While Loop

# 32.
# print(len(input()))

# 33.
# print(sum([int(i) for i in input()]))

# 34
# n=[int(i) for i in input()]
# n.sort(reverse=True)
# print(*n)

