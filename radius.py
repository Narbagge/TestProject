import libs.radius as radius

print('Input X coordinate!')
x = float(input())
print('Input Y coordinate!')
y = float(input())

print('Radius Squared: ', radius.radius_squared(x, y))
print('Radius: ', radius.radius_squared(x, y) ** 0.5)

input()