'''
animals=['man','pig','bird','cat']
transport=['car','plane','bus']
last_two=animals[-2:-1]
print(last_two)
bird_index=animals.index('bird')
print(bird_index)
try:
    dog_index=animals.index('dog')
    print(dog_index)
except:
    dog_index='No dog found'
print(dog_index)

index=0
while index<len(animals):
    print(animals[index])
    index=index+1

sorted_animals=sorted(animals)
print('Animals after sorted: {}'.format(sorted_animals))

all_group=animals+transport
print(all_group)
'''
animals=['man','pig','bird','cat']
animals.extend(['fly'])
print(animals)

for animals in animals:
    print(animals)
for number in range(3):
    print(number)

for number in range(1,10,3):
    print(number)

