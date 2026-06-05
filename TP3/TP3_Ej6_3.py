class ParserDescendente:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # Obtiene el token actual
    def token_actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    # Consume un token esperado
    def consumir(self, esperado):
        actual = self.token_actual()

        if actual == esperado:
            print("Consumido:", actual)
            self.pos += 1
        else:
            raise SyntaxError(
                "Error sintáctico: se esperaba '%s', se encontró '%s'"
                % (esperado, actual)
            )

    # Punto de entrada
    def parsear(self):
        print("Aplicando E → T E'")
        self.E()

        # Verifica que no queden tokens sin consumir
        if self.pos != len(self.tokens):
            raise SyntaxError(
                "Error sintáctico: token inesperado '%s'"
                % self.token_actual()
            )

        print("Resultado: ACEPTADO")
        return True

    # E → T E'
    def E(self):
        print("Aplicando E → T E'")
        self.T()
        self.Ep()

    # E' → + T E' | ε
    def Ep(self):
        actual = self.token_actual()

        if actual == '+':
            print("Aplicando E' → + T E'")
            self.consumir('+')
            self.T()
            self.Ep()
        else:
            print("Aplicando E' → ε")

    # T → F T'
    def T(self):
        print("Aplicando T → F T'")
        self.F()
        self.Tp()

    # T' → * F T' | ε
    def Tp(self):
        actual = self.token_actual()

        if actual == '*':
            print("Aplicando T' → * F T'")
            self.consumir('*')
            self.F()
            self.Tp()
        else:
            print("Aplicando T' → ε")

    # F → ( E ) | num
    def F(self):
        actual = self.token_actual()

        if actual == 'num':
            print("Aplicando F → num")
            self.consumir('num')

        elif actual == '(':
            print("Aplicando F → ( E )")
            self.consumir('(')
            self.E()
            self.consumir(')')

        else:
            raise SyntaxError(
                "Error sintáctico: se esperaba 'num' o '(', se encontró '%s'"
                % actual
            )


# -------------------------------
# EJEMPLO VÁLIDO
# -------------------------------

tokens = ['num', '+', 'num', '*', 'num']

parser = ParserDescendente(tokens)

try:
    resultado = parser.parsear()
except SyntaxError as error:
    print(error)


# -------------------------------
# EJEMPLO INVÁLIDO
# -------------------------------

tokens_invalidos = ['num', '+', '+', 'num']

parser2 = ParserDescendente(tokens_invalidos)

try:
    parser2.parsear()
except SyntaxError as error:
    print(error)