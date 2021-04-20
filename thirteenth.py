# The for loop

primes = [2, 3, 5, 7, 11]
for prime in primes:
    print(f'{prime} is  a prime number.')



for i in range(20):
    print(i)

print(range(10))

# Iteration of dictionaries


my_friends = {
    'Tushar': 6,
    'Sunny': 12,
    'Sameer': 6
}

for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago.')


"""
Notice what .items() gives us:
"""

print(my_friends.items())

friend_info = [('Tushar', 6), ('Sunny', 12), ('Sameer', 6)]
for name, days in friend_info:
    print(f'{name}, {days}')

