
from lpp.ast import Program
from lpp.lexer import Lexer


class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        return program
