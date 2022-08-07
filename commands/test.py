def calculator(a, b, operation):
    if a == '' or b == '':
        return 'FUCK YOU!'
    else:
         a = float(a)
         b = float(b)
    match operation:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case default:
            return 'FUCK YOU!'