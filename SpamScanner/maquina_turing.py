"""
SpamScanner 2.0 — Etapa 1: Normalización Selectiva (Máquina de Turing)

Definición formal:
  M = (Q, Σ, Γ, δ, q₀, B, F)

Q = {q₀, qf}
Σ = {caracteres imprimibles ASCII presentes en mensajes SMS}
Γ = Σ ∪ {B}
q₀ = q₀
B  = \0 (null / fin de cinta)
F  = {qf}

δ: Q × Γ → Q × Γ × {L, R}
  δ(q₀, s) = (q₀, s,  R)  si s ∈ {A-Z, a-z, 0-9, espacio, $, ., :, /}
  δ(q₀, s) = (q₀, ' ', R)  si s ∉ conjunto de conservación y s ≠ B
  δ(q₀, B) = (qf, B,  R)  fin de la entrada
"""

KEEP = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 $.:/")


class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.head = 0
        self.state = "q0"
        self.blank = "\0"
        self.trace = []

    def step(self):
        if self.head < len(self.tape):
            symbol = self.tape[self.head]
        else:
            symbol = self.blank

        if self.state == "q0":
            if symbol == self.blank:
                self.state = "qf"
                self.trace.append(
                    f"delta(q0, {symbol}) = (qf, {symbol}, R) -> fin de cinta"
                )
                return True

            if symbol in KEEP:
                write = symbol
                self.trace.append(
                    f"delta(q0, {symbol}) = (q0, {symbol}, R) -> conserva"
                )
            else:
                write = " "
                self.trace.append(
                    f"delta(q0, {symbol}) = (q0, {write}, R) -> reemplaza por espacio"
                )

            self.tape[self.head] = write
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank)
            return True

        return False

    def run(self):
        while self.state != "qf":
            if not self.step():
                break
        result = "".join(self.tape)
        if self.blank in result:
            result = result[: result.index(self.blank)]
        return result


def normalizar(texto):
    """Aplica la MT de normalización sobre un texto."""
    mt = TuringMachine(texto)
    resultado = mt.run()
    return resultado, mt.trace
