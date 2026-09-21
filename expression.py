from stack_array import ArrayStack

# Written for you. Higher number binds tighter.
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

# Written for you. 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2)
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression):
    """Written for you. Splits on whitespace."""
    return expression.split()


def infix_to_postfix(expression):
    """Step 1. Convert infix to postfix."""
    tokens = tokenize(expression)
    output = []
    operators = ArrayStack()

    for token in tokens:
        if token in PRECEDENCE:
            while (
                not operators.is_empty()
                and operators.peek() != "("
                and (
                    PRECEDENCE[operators.peek()] > PRECEDENCE[token]
                    or (
                        PRECEDENCE[operators.peek()] == PRECEDENCE[token]
                        and token not in RIGHT_ASSOCIATIVE
                    )
                )
            ):
                output.append(operators.pop())

            operators.push(token)

        elif token == "(":
            operators.push(token)

        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())

            if operators.is_empty():
                raise ValueError("unbalanced parentheses")

            operators.pop()

        else:
            output.append(token)

    while not operators.is_empty():
        if operators.peek() == "(":
            raise ValueError("unbalanced parentheses")

        output.append(operators.pop())

    return " ".join(output)


def evaluate_postfix(expression):
    """Step 2. Evaluate a postfix expression."""
    tokens = tokenize(expression)
    values = ArrayStack()

    for token in tokens:
        if token in PRECEDENCE:
            if values.size() < 2:
                raise ValueError("not enough operands")

            right = values.pop()
            left = values.pop()

            result = apply_operator(token, left, right)
            values.push(result)

        else:
            try:
                values.push(float(token))
            except ValueError:
                raise ValueError("invalid operand")

    if values.size() != 1:
        raise ValueError("invalid postfix expression")

    return values.pop()


def apply_operator(operator, left, right):
    """Step 3. Apply an operator."""
    if operator == "+":
        return left + right

    elif operator == "-":
        return left - right

    elif operator == "*":
        return left * right

    elif operator == "/":
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return left / right

    elif operator == "%":
        if right == 0:
            raise ZeroDivisionError("modulo by zero")
        return left % right

    elif operator == "^":
        return left ** right

    else:
        raise ValueError("unknown operator")


def convert_and_evaluate(expression):
    """Written for you."""
    postfix = infix_to_postfix(expression)
    return postfix, evaluate_postfix(postfix)


if __name__ == "__main__":
    try:
        postfix, value = convert_and_evaluate("3 + 4 * 2")

        print("infix   : 3 + 4 * 2")
        print("postfix :", postfix)
        print("value   :", value)

    except NotImplementedError as unfinished:
        print("Not written yet ->", unfinished)