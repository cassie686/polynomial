class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

class Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        # Ensure proper parenthetical structure
        left_repr = f"({repr(self.left)})" if isinstance(self.left, Add) else repr(self.left)
        right_repr = f"({repr(self.right)})" if isinstance(self.right, Add) else repr(self.right)
        return f"{left_repr} - {right_repr}"

class Div:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        # Ensure proper parenthetical structure and handle division by zero
        num_repr = f"({repr(self.numerator)})" if isinstance(self.numerator, (Add, Sub)) else repr(self.numerator)
        den_repr = f"({repr(self.denominator)})" if isinstance(self.denominator, (Add, Sub, Mul)) else repr(self.denominator)
        if isinstance(self.denominator, Int) and self.denominator.i == 0:
            return "Undefined"  # or "DivisionByZero"
        return f"{num_repr} / {den_repr}"

class Mul:
    # ... (existing __init__ method)

    def __repr__(self):
        # Modified __repr__ method with proper parenthetical structure
        left_repr = f"({repr(self.p1)})" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        right_repr = f"({repr(self.p2)})" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{left_repr} * {right_repr}"

# Test cases
x = X()
expr1 = Add(Mul(Int(2), x), Int(3))  # Represents 2*X + 3
expr2 = Sub(expr1, x)                # Represents (2*X + 3) - X
expr3 = Div(expr1, expr2)            # Represents (2*X + 3) / ((2*X + 3) - X)
expr4 = Div(expr1, Int(0))           # Represents (2*X + 3) / 0, should handle division by zero

print(expr1)  # Should output: (2 * X) + 3
print(expr2)  # Should output: ((2 * X) + 3) - X
print(expr3)  # Should output: ((2 * X) + 3) / (((2 * X) + 3) - X)
print(expr4)  # Should output: Undefined or DivisionByZero

class X:
    # ... (existing methods)

    def evaluate(self, value):
        return value

class Int:
    # ... (existing methods)

    def evaluate(self, value):
        return self.i

class Add:
    # ... (existing methods)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Sub:
    # ... (existing methods)

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    # ... (existing methods)

    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    # ... (existing methods)

    def evaluate(self, value):
        numerator = self.numerator.evaluate(value)
        denominator = self.denominator.evaluate(value)
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return numerator / denominator
    
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))  # Replace -1 with any value you want to evaluate the polynomial at



