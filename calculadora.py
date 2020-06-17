prefijo = "*+472"
postfijo = "472*+"
infijo = "4+(7*2)"






def postFijoAInfijo(cadena):
    stack = []
    for carac in cadena:
        #print carac
        if carac == "+" or carac == "*":
            a = stack.pop()
            print (a)
            b = stack.pop()
            print (b)
            stack.append("(" + b + carac + a + ")")
        else:
            stack.append(carac)
    return stack.pop()

print (postFijoAInfijo(postfijo))


def r