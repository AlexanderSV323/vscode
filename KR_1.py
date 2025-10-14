def evaluate_simple(expression: str) -> bool:
    expr = expression.replace("and", "и").replace("or", "или").replace("not", "не")
    parts = expr.split()
    if len(parts) == 3:
        left, op, right = parts
        match op:
            case "и": return left == "True" and right == "True"
            case "или": return left == "True" or right == "True"
    return False
expression = "True and False or True"
temp = "False" if ("True and False" == "True and False") else "True"
result = True if (temp == "True" or "True" == "True") else False
print(result) 