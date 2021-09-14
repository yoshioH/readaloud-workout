# coding: utf-8
import random
from chunks import Chunk
from chunks import ChunkType
from chunks import ChunkResource

class RandomArithmeticResource(ChunkResource):
    def __init__(self) -> None:
        super().__init__()
        self.__current_count = 0
        self.__current_expression = ''

    @classmethod
    def __multiply(cls):
        left   = str(random.randint(1, 9))
        right  = str(random.randint(1, 9))
        return f'{left} * {right}'

    @classmethod
    def __divide(cls):
        left   = str(random.randint(1, 9))
        right  = str(random.randint(1, 9))
        answer = eval(f'{left} * {right}')
        return f'{answer} / {left}'

    @classmethod
    def __num(cls):
        return str(random.randint(1, 99))

    @classmethod
    def __monomial(cls):
        monomial_type = random.choice([0, 1, 2])
        if monomial_type == 0:
            return cls.__multiply()
        elif monomial_type == 1:
            return cls.__divide()
        return cls.__num()

    @classmethod
    def __expression(cls):
        return cls.__monomial() + ' ' + random.choice(['+', '-']) + ' ' + cls.__monomial()

    def generate(self) -> Chunk:
        chunk = None
        if self.__current_count % 2 == 0:
            self.__current_expression = RandomArithmeticResource.__expression()
            chunk = Chunk(ChunkType.QUESTION, self.__current_expression + ' = ?')
        else:
            chunk = Chunk(ChunkType.ANSWER, str(int(eval(self.__current_expression))))
        self.__current_count+=1
        return chunk
