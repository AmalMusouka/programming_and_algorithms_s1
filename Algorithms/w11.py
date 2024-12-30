from collections import deque


# knight on a chessboard

dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (1, -2),]

# Given a state, return a list of its neighbours
def next(state):
    x, y = state
    return [(x + dx, y + dy) for dx, dy in dirs if 0 <= x < 8 and 0 <= y < 8]

# return a path from start to goal
def search(start, goal):
    # visited set
    prev = {start: None}

    q = deque()
    q.append(start)

    while len(q) > 0:
        state = q.popleft()
        if state == goal:
            path = []
            while state != None:
                path.append(state)
                state = prev[state]
            return path[::-1]
        for n in next(state):
            if n not in prev:
                prev[n] = state
                q.append(n)
    assert False, 'no path found'



class Expr:
    pass

class OpExpr(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self):
        l = self.left.eval()
        r = self.right.eval()
        match self.op:
            case '+': return l + r
            case '-': return l - r
            case '*': return l * r
            case '/': return l // r
            case _ : assert False, 'unknown op'

    def to_infix(self):
        return f'{self.left.to_infix()} {self.op} {self.right.to_infix()}'

    def to_prefix(self):
        return f'{self.op} {self.left.to_prefix()} {self.right.to_prefix()}'


class IntExpr(Expr):
    def __init__(self, n):
        self.n = n

    def eval(self):
        return self.n

    def to_infix(self):
        return str(self.n)

    def to_prefix(self):
        return str(self.n)


class Lexer:
    def __init__(self, s):
        self.s = s
        self.i = 0 # current position in the string

    # return next token
    def next(self):
        # Move past whitespace
        while self.i < len(self.s) and self.s[self.i].isspace():
            self.i += 1

        if self.i >= len(self.s):
            return None # there are no more tokens

        c = self.s[self.i]
        if c.isdigit(): # we have a number
            n = c
            self.i += 1
            while self.i < len(self.s) and self.s[self.i].isdigit():
                n += self.s[self.i]
                self.i += 1
            return int(n)

        assert c in '+-*/()'
        self.i += 1
        return c # this is a symbol

def parse_prefix(s): # Parse an expression in prefix notation
    l = Lexer(s)

    def parse():
        t = l.next()
        if isinstance(t, int):
            return IntExpr(t)

        left = parse()
        right = parse()
        return OpExpr(t, left, right)

    return parse()

# Parse a fully parenthesized infix expression.
def parse_infix(s):
    l = Lexer(s)

    def parse():
        t = l.next()
        if isinstance(t, int):
            return IntExpr(t)

        assert t == '('
        left = parse()
        op = l.next()
        assert op in '+-*/'
        right = parse()
        assert l.next() == ')'
        return OpExpr(op, left, right)

my_expr = OpExpr('+', IntExpr(2), IntExpr(3))