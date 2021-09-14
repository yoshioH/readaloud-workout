# coding: utf-8
from enum import Enum
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

class ChunkType(Enum):
    READ_ALOUD  = 0
    QUESTION    = 1
    ANSWER      = 2

@dataclass(frozen=True)
class Chunk:
    type: ChunkType
    text: str

class ChunkResource(ABC):
    @abstractmethod
    def generate(self) -> Chunk:
        return Chunk(ChunkType.READ_ALOUD, 'Yaruki Max Orix!!')

def generate(chunk_generator:ChunkResource):
    while True:
        chunk = chunk_generator.generate()
        if chunk is None:
            break
        yield chunk
