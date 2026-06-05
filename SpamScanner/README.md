# SpamScanner 2.0

Trabajo Práctico Integrador de **Autómatas y Gramáticas**.

## Integrantes

* Franco Verdini
* Jerónimo Soto
* Agustín Valdebenito

---

## Descripción

SpamScanner 2.0 es un sistema de análisis y clasificación de mensajes SMS basado en modelos formales de la Jerarquía de Chomsky.

El sistema procesa mensajes provenientes del SMS Spam Collection Dataset y los clasifica como:

* HAM
* SPAM
* SPAM ATÍPICO

El procesamiento se realiza mediante un pipeline compuesto por cuatro etapas.

---

## Pipeline del Sistema

```text
SMS Original
      ↓
Máquina de Turing
      ↓
Texto Normalizado
      ↓
Expresiones Regulares
      ↓
Tokenización
      ↓
Clasificación Heurística
      ↓
Validación con GLC
      ↓
HAM / SPAM / SPAM ATÍPICO
```

---

## Estructura del Proyecto

```text
SpamScanner/
│
├── main.py
├── maquina_turing.py
├── tokenizador.py
├── clasificador.py
├── gramatica.py
│
├── dataset/
│   └── SpamCollectionSpanish.csv
│
├── docs/
│   └── Trabajo_Final_Integrador.pdf
│
└── README.md
```

---

## Etapa 1 - Máquina de Turing

Implementación de una Máquina de Turing utilizada para la normalización selectiva del texto.

Funciones principales:

* Conserva letras y números.
* Conserva espacios.
* Conserva símbolos relevantes:

  * $
  * .
  * :
  * /
* Reemplaza caracteres irrelevantes por espacios.

Salida:

```text
WIN $1000 now!
```

↓

```text
WIN $1000 now
```

---

## Etapa 2 - Tokenización con Expresiones Regulares

Identificación de patrones mediante expresiones regulares.

Tokens reconocidos:

| Token | Descripción            |
| ----- | ---------------------- |
| MONEY | Valores monetarios     |
| URL   | Direcciones web        |
| PHONE | Números telefónicos    |
| CAPS  | Palabras en mayúsculas |
| WORD  | Resto de las palabras  |

Ejemplo:

```text
WIN $1000 NOW www.premio.com
```

↓

```text
CAPS MONEY CAPS URL
```

---

## Etapa 3 - Clasificación Heurística

Clasificación basada en pesos asociados a cada token.

| Token | Peso |
| ----- | ---- |
| MONEY | 3    |
| PHONE | 3    |
| URL   | 2    |
| CAPS  | 1    |
| WORD  | 0    |

Si la suma de pesos supera un umbral U:

```text
SPAM
```

En caso contrario:

```text
HAM
```

---

## Etapa 4 - Gramática Libre de Contexto

Validación estructural de mensajes clasificados previamente como SPAM.

Alfabeto terminal:

```text
caps
money
contact
text
```

donde:

* contact = PHONE o URL
* text = uno o más WORD

La estructura válida debe contener:

```text
GANCHO → caps
CONTENIDO → money | text
CIERRE → contact
```

Mensajes que no cumplen la estructura son clasificados como:

```text
SPAM ATÍPICO
```

---

## Dataset

Se utiliza el SMS Spam Collection Dataset.

Para las métricas del trabajo se procesan al menos:

* 50 mensajes HAM
* 50 mensajes SPAM

---

## Ejecución

Ejecutar el pipeline completo:

```bash
python main.py
```

---

## Tecnologías Utilizadas

* Python 3
* Expresiones Regulares (`re`)
* Implementación de Máquina de Turing
* Gramáticas Libres de Contexto

---

## Materia

Autómatas y Gramáticas

Ingeniería en Informática
