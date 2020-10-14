from typing import Optional

from lpp.ast import Program
from lpp.lexer import Lexer
from lpp.token import (
    Token,
    TokenType,
)


class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer
        self._current_token: Optional[Token] = None
        self._peek_token: Optional[Token] = None

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        assert self._current_token is not None
        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            if statement is not None:
                program.statements.append(statement)

        return program

    def _parse_statement(self) -> Optional[Statment]:
        assert self._current_token is not None
        if self._current_token.token_type == TokenType.LET:
            return self._parse_let_statement()
        else:
            return None

