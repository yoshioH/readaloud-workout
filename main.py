# coding: utf-8
from chunks import generate
from chunks.arithmetic_operations import RandomArithmeticResource

resource = RandomArithmeticResource()
count = 0
for chunk in generate(resource):
    print(f'{chunk.type} : {chunk.text}')
    count+=1
    if count > 3:
        break

print('bye')
