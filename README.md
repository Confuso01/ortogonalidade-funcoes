#  Ortogonalidade e Não-Ortogonalidade de Funções

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-green.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Visualizador Interativo de Ortogonalidade de Funções Trigonométricas**  
> Projeto educacional para demonstrar conceitos de ortogonalidade através de cálculos detalhados e visualizações gráficas interativas.

---

##  Sobre o Projeto

Este projeto combina **teoria matemática rigorosa** com **visualizações interativas** para explorar o conceito fundamental de ortogonalidade de funções, especialmente aplicado a:

- Séries de Fourier
- Análise de Sinais
- Processamento de Sinais Digitais
- Engenharia Elétrica e de Telecomunicações

###  Autor
**Moisés Diego Cipriano dos Santos**  
Data: 11/09/2025

---
 ##
 Para visualizar o documento sobre ortogonalidade, [baixe o PDF](Ortogonalidade.pdf)
 ##
##  Características Principais

###  Documentação Teórica
-  Demonstrações matemáticas completas
-  Cálculos passo a passo detalhados
-  Exemplos ortogonais e não-ortogonais
-  Propriedades de exponenciais complexas
-  Relação com Séries de Fourier

###  Visualizador Interativo
-  **8 Exemplos Interativos** com navegação por botões
-  **Visualizações em tempo real** de funções trigonométricas
-  **Análise de produtos** e integrais
-  **Cancelamento de áreas** (positiva/negativa)
-  **Interface moderna** com Matplotlib widgets
-  **Exemplos de não-ortogonalidade** explicados visualmente

---

##  Começando

### Pré-requisitos

```bash
Python 3.7 ou superior
NumPy
Matplotlib
```

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/ortogonalidade-funcoes.git
cd ortogonalidade-funcoes
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute o visualizador:**
```bash
python ortogonalidade.py
```

---

##  Exemplos Interativos

O visualizador inclui 8 exemplos diferentes:

### 1️ **Exemplo Principal**
- **Funções:** `cos(4πt) × sin(2πt)`
- **Resultado:** Ortogonais em [0,1], mas não em [0,0.5]
- **Conceito:** Importância do intervalo de integração

### 2️ **Senos Ortogonais**
- **Funções:** `sin(2πt) × sin(4πt)`
- **Resultado:** ∫ ≈ 0
- **Conceito:** Cancelamento perfeito de áreas

### 3️ **Cossenos Ortogonais**
- **Funções:** `cos(2πt) × cos(6πt)`
- **Resultado:** ∫ ≈ 0
- **Conceito:** Oscilações rápidas e cancelamento

### 4️ **Seno × Cosseno**
- **Funções:** `sin(2πt) × cos(4πt)`
- **Resultado:** **SEMPRE ortogonais**
- **Conceito:** Propriedade fundamental

### 5️ **Não-Ortogonal: sin²(2πt)**
- **Funções:** Função consigo mesma
- **Resultado:** ∫ = 0.5 ≠ 0
- **Conceito:** Frequências iguais → não-ortogonalidade

### 6️ **Intervalo Inadequado**
- **Análise detalhada** de como o intervalo afeta a ortogonalidade
- **Comparação** [0,1] vs [0,0.5]

### 7️ **Frequências Próximas**
- **Efeito de batimento** (beat frequency)
- **Envelope de amplitude**

### 8️ **Decomposição Trigonométrica**
- **Série de Fourier** aproximando onda quadrada
- **Componentes individuais**

---

##  Conceitos Matemáticos

### Definição de Ortogonalidade

Duas funções f(t) e g(t) são **ortogonais** em [a,b] se:

```
∫ₐᵇ f(t)g(t) dt = 0
```

### Propriedades Fundamentais

Para `T₀ = 2π/ω₀` (período fundamental):

| Produto | Condição | Resultado |
|---------|----------|-----------|
| `sin(nω₀t) × sin(mω₀t)` | n ≠ m | 0 |
| `sin(nω₀t) × sin(mω₀t)` | n = m | T₀/2 |
| `cos(nω₀t) × cos(mω₀t)` | n ≠ m | 0 |
| `cos(nω₀t) × cos(mω₀t)` | n = m | T₀/2 |
| `sin(nω₀t) × cos(mω₀t)` | ∀n,m | 0 |

### Exponenciais Complexas

```
∫₀^T₀ e^(jnω₀t) · e^(-jmω₀t) dt = { T₀,  se n = m
                                    { 0,   se n ≠ m
```

---

##  Aplicações

Este conceito é fundamental em:

-  **Processamento de Sinais**
-  **Telecomunicações**
-  **Análise de Circuitos Elétricos**
-  **Áudio Digital e Compressão**
---



##  Como Usar o Visualizador

### Interface do Programa

1. **Botões Laterais:** Clique para alternar entre exemplos
2. **Gráfico Superior:** Funções originais
3. **Gráfico Central:** Produto das funções
4. **Gráfico Inferior:** Análise detalhada

### Navegação

```python
# O programa abre automaticamente
python ortogonalidade.py

# Use os botões na lateral direita para navegar
# Cada botão está colorido para facilitar identificação
```

### Interpretação dos Resultados

-  **Verde:** Funções ortogonais (∫ ≈ 0)
-  **Vermelho:** Funções não-ortogonais (∫ ≠ 0)
-  **Azul:** Áreas positivas
-  **Vermelho:** Áreas negativas

---

## Exemplos de Código

### Exemplo 1: Verificar Ortogonalidade

```python
import numpy as np

def verificar_ortogonalidade(f1, f2, a=0, b=1, n_points=1000):
    """
    Verifica se duas funções são ortogonais em [a,b]
    """
    t = np.linspace(a, b, n_points)
    produto = f1(t) * f2(t)
    integral = np.trapz(produto, t)
    
    if abs(integral) < 1e-6:
        print(f"✅ Ortogonais: ∫ = {integral:.8f}")
    else:
        print(f"❌ Não-ortogonais: ∫ = {integral:.8f}")
    
    return integral

# Teste
f1 = lambda t: np.sin(2*np.pi*t)
f2 = lambda t: np.sin(4*np.pi*t)

verificar_ortogonalidade(f1, f2)
```

### Exemplo 2: Criar Visualização Personalizada

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)
f1 = np.cos(4*np.pi*t)
f2 = np.sin(2*np.pi*t)
produto = f1 * f2

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, f1, label='cos(4πt)')
plt.plot(t, f2, label='sin(2πt)')
plt.legend()
plt.title('Funções Originais')

plt.subplot(3, 1, 2)
plt.plot(t, produto)
plt.fill_between(t, produto, 0, alpha=0.5)
plt.title('Produto')

plt.subplot(3, 1, 3)
integral = np.trapz(produto, t)
plt.text(0.5, 0.5, f'∫ = {integral:.8f}', 
         ha='center', va='center', fontsize=20)
plt.axis('off')

plt.tight_layout()
plt.show()
```

---

##  Fundamentos Teóricos

## Ortogonalidade de Seno e Cosseno

Para $T_0 = \frac{2\pi}{\omega_0}$ (período fundamental), vamos demonstrar as propriedades de ortogonalidade, assumindo que $n$ e $m$ são **inteiros** ($n,m \in \mathbb{Z}$).

> **Observação:** Se $n=0$ ou $m=0$, então:
> 
> $$\sin(0\cdot\omega_0 t) \equiv 0 \quad\text{ e }\quad \cos(0\cdot\omega_0 t) \equiv 1$$
> 
> portanto, os produtos envolvendo $\sin(0\cdot\omega_0 t)$ serão sempre nulos, e os produtos envolvendo $\cos(0\cdot\omega_0 t)$ devem ser tratados separadamente.

---

### Produto de Senos com Frequências Diferentes

**Para $n \neq m$:**

$$\int_0^{T_0} \sin(n\omega_0 t)\sin(m\omega_0 t)\,dt$$

Usando a identidade trigonométrica: $\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$

$$= \int_0^{T_0} \frac{1}{2}[\cos((n-m)\omega_0 t) - \cos((n+m)\omega_0 t)]\,dt$$

$$= \frac{1}{2}\left[\frac{\sin((n-m)\omega_0 t)}{(n-m)\omega_0} - \frac{\sin((n+m)\omega_0 t)}{(n+m)\omega_0}\right]_0^{T_0}$$

Como $T_0 = \frac{2\pi}{\omega_0}$, temos:
- $(n-m)\omega_0 T_0 = (n-m) \cdot 2\pi$ (múltiplo inteiro de $2\pi$)
- $(n+m)\omega_0 T_0 = (n+m) \cdot 2\pi$ (múltiplo inteiro de $2\pi$)

Portanto: $\sin((n-m) \cdot 2\pi) = \sin((n+m) \cdot 2\pi) = 0$

> **Resultado:** $= 0$ quando $n \neq m$

**Para $n = m$:**

$$\int_0^{T_0} \sin^2(n\omega_0 t)\,dt$$

Usando a identidade: $\sin^2(x) = \frac{1-\cos(2x)}{2}$

$$= \int_0^{T_0} \frac{1-\cos(2n\omega_0 t)}{2}\,dt$$

$$= \frac{1}{2}\left[t - \frac{\sin(2n\omega_0 t)}{2n\omega_0}\right]_0^{T_0}$$

$$= \frac{1}{2}\left[T_0 - \frac{\sin(2n\omega_0 T_0)}{2n\omega_0} + 0\right]$$

Como $2n\omega_0 T_0 = 4n\pi$, temos $\sin(4n\pi) = 0$

> **Resultado:** $= \frac{T_0}{2}$ quando $n = m$

---

### Produto de Cossenos

**Para $n \neq m$:**

$$\int_{0}^{T_0}\cos(n\omega_0 t)\cos(m\omega_0 t)\,dt$$

Usando a identidade trigonométrica:
$$\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$$

$$= \int_{0}^{T_0} \frac{1}{2}[\cos((n-m)\omega_0 t) + \cos((n+m)\omega_0 t)]\,dt$$

$$= \frac{1}{2} \int_{0}^{T_0} \cos((n-m)\omega_0 t)\,dt + \frac{1}{2} \int_{0}^{T_0} \cos((n+m)\omega_0 t)\,dt$$

$$= \frac{1}{2}\left[\frac{\sin((n-m)\omega_0 t)}{(n-m)\omega_0}\right]_{0}^{T_0} + \frac{1}{2}\left[\frac{\sin((n+m)\omega_0 t)}{(n+m)\omega_0}\right]_{0}^{T_0}$$

Como $T_0 = \frac{2\pi}{\omega_0}$, temos:

$$(n - m)\omega_0 T_0 = (n - m)\,2\pi \quad \text{(múltiplo inteiro de } 2\pi \text{)}$$

$$(n + m)\omega_0 T_0 = (n + m)\,2\pi \quad \text{(múltiplo inteiro de } 2\pi \text{)}$$

Portanto:

$$\sin((n - m)\omega_0 T_0) = \sin((n + m)\omega_0 T_0) = 0$$

e os termos se anulam.

$$\Rightarrow \int_{0}^{T_0}\cos(n\omega_0 t)\cos(m\omega_0 t)\,dt = 0 \quad \text{quando } n \neq m$$

> **Resultado:** $= 0$ quando $n \neq m$

**Para $n = m$:**

$$\int_{0}^{T_0}\cos^2(n\omega_0 t)\,dt$$

Usando a identidade: $\cos^2 A = \frac{1}{2}[1 + \cos(2A)]$

$$= \frac{1}{2}\int_{0}^{T_0} [1 + \cos(2n\omega_0 t)]\,dt$$

$$= \frac{1}{2}\left[\int_{0}^{T_0}1\,dt + \int_{0}^{T_0}\cos(2n\omega_0 t)\,dt\right]$$

$$= \frac{1}{2}\left[T_0 + \frac{\sin(2n\omega_0 T_0)}{2n\omega_0}\right]$$

Como $2n\omega_0 T_0 = 4n\pi$, e $\sin(4n\pi) = 0$:

$$\Rightarrow \int_{0}^{T_0}\cos^2(n\omega_0 t)\,dt = \frac{T_0}{2}$$

> **Resultado:** $= \frac{T_0}{2}$ quando $n = m$

---

### Produto de Seno e Cosseno

$$\int_0^{T_0} \sin(n\omega_0 t)\cos(m\omega_0 t)\,dt$$

Usando: $\sin A \cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$

$$= \frac{1}{2}\int_0^{T_0} [\sin((n+m)\omega_0 t) + \sin((n-m)\omega_0 t)]\,dt$$

$$= \frac{1}{2}\left[-\frac{\cos((n+m)\omega_0 t)}{(n+m)\omega_0} - \frac{\cos((n-m)\omega_0 t)}{(n-m)\omega_0}\right]_0^{T_0}$$

Avaliando nos limites e usando que $(n \pm m)\omega_0 T_0$ são múltiplos de $2\pi$:

> **Resultado:** $= 0$ para todos os valores de $n$ e $m$

---

## Exemplos Ortogonais

### Exemplo 1: Produto de Cossenos

Considere: $x(t) = \cos(2\pi t)\cos(6\pi t)$

**Cálculo no intervalo $[0,1]$:**

O cálculo é análogo ao dos senos. Consideremos o produto de dois cossenos com frequências diferentes:

$$\int_0^1 \cos(2\pi t) \cdot \cos(6\pi t) \, dt$$

Utilizando a identidade trigonométrica para produto de cossenos:

$$\cos A \cdot \cos B = \frac{1}{2}[\cos(A + B) + \cos(A - B)]$$

Aplicando esta identidade com $A = 2\pi t$ e $B = 6\pi t$:

$$\cos(2\pi t) \cdot \cos(6\pi t) = \frac{1}{2}[\cos(2\pi t + 6\pi t) + \cos(2\pi t - 6\pi t)]$$

$$= \frac{1}{2}[\cos(8\pi t) + \cos(-4\pi t)]$$

$$= \frac{1}{2}[\cos(8\pi t) + \cos(4\pi t)]$$

Onde utilizamos a propriedade $\cos(-x) = \cos(x)$.

Substituindo na integral:

$$\int_0^1 \cos(2\pi t) \cdot \cos(6\pi t) \, dt = \int_0^1 \frac{1}{2}[\cos(8\pi t) + \cos(4\pi t)] \, dt$$

$$= \frac{1}{2} \int_0^1 \cos(8\pi t) \, dt + \frac{1}{2} \int_0^1 \cos(4\pi t) \, dt$$

Calculando cada integral separadamente:

$$\int_0^1 \cos(8\pi t) \, dt = \left[ \frac{\sin(8\pi t)}{8\pi} \right]_0^1$$

$$= \frac{\sin(8\pi) - \sin(0)}{8\pi}$$

$$= \frac{0 - 0}{8\pi} = 0$$

$$\int_0^1 \cos(4\pi t) \, dt = \left[ \frac{\sin(4\pi t)}{4\pi} \right]_0^1$$

$$= \frac{\sin(4\pi) - \sin(0)}{4\pi}$$

$$= \frac{0 - 0}{4\pi} = 0$$

Portanto:

$$\int_0^1 \cos(2\pi t) \cdot \cos(6\pi t) \, dt = \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 0 = 0$$

> **Resultado:** $= 0$

**Conclusão:** As funções $\cos(2\pi t)$ e $\cos(6\pi t)$ são ortogonais no intervalo $[0,1]$, uma vez que sua integral é zero.

<img width="1361" height="837" alt="Figura4" src="https://github.com/user-attachments/assets/29165366-5fcb-4335-811b-b64037060608" />

**Generalização:** Para quaisquer inteiros $n \neq m$:
$$\int_0^1 \cos(n\pi t) \cdot \cos(m\pi t) \, dt = 0$$

---

### Exemplo 2: Produto de Senos

Considere: $x(t) = \sin(2\pi t)\sin(4\pi t)$

**Cálculo no intervalo $[0,1]$:**

Consideremos o produto de dois senos com frequências diferentes:

$$\int_0^1 \sin(2\pi t) \cdot \sin(4\pi t) \, dt$$

Utilizando a identidade trigonométrica para produto de senos:

$$\sin A \cdot \sin B = \frac{1}{2}[\cos(A - B) - \cos(A + B)]$$

Aplicando esta identidade com $A = 2\pi t$ e $B = 4\pi t$:

$$\sin(2\pi t) \cdot \sin(4\pi t) = \frac{1}{2}[\cos(2\pi t - 4\pi t) - \cos(2\pi t + 4\pi t)]$$

$$= \frac{1}{2}[\cos(-2\pi t) - \cos(6\pi t)]$$

$$= \frac{1}{2}[\cos(2\pi t) - \cos(6\pi t)]$$

Onde utilizamos a propriedade $\cos(-x) = \cos(x)$.

Substituindo na integral:

$$\int_0^1 \sin(2\pi t) \cdot \sin(4\pi t) \, dt = \int_0^1 \frac{1}{2}[\cos(2\pi t) - \cos(6\pi t)] \, dt$$

$$= \frac{1}{2} \int_0^1 \cos(2\pi t) \, dt - \frac{1}{2} \int_0^1 \cos(6\pi t) \, dt$$

Calculando cada integral separadamente:

$$\int_0^1 \cos(2\pi t) \, dt = \left[ \frac{\sin(2\pi t)}{2\pi} \right]_0^1$$

$$= \frac{\sin(2\pi) - \sin(0)}{2\pi}$$

$$= \frac{0 - 0}{2\pi} = 0$$

$$\int_0^1 \cos(6\pi t) \, dt = \left[ \frac{\sin(6\pi t)}{6\pi} \right]_0^1$$

$$= \frac{\sin(6\pi) - \sin(0)}{6\pi}$$

$$= \frac{0 - 0}{6\pi} = 0$$

Portanto:

$$\int_0^1 \sin(2\pi t) \cdot \sin(4\pi t) \, dt = \frac{1}{2} \cdot 0 - \frac{1}{2} \cdot 0 = 0$$

**Conclusão:** As funções $\sin(2\pi t)$ e $\sin(4\pi t)$ são ortogonais no intervalo $[0,1]$, uma vez que sua integral é zero.

> **Resultado:** $= 0$

<img width="1356" height="822" alt="Figura5" src="https://github.com/user-attachments/assets/51b08fe9-409c-4dd2-9ac9-241dcc30c05a" />

**Generalização:** Para quaisquer inteiros $n \neq m$:
$$\int_0^1 \sin(n\pi t) \cdot \sin(m\pi t) \, dt = 0$$

---

### Exemplo 3: Produto de Cosseno e Seno

Considere: $x(t) = \cos(4\pi t)\sin(2\pi t)$

**Cálculo no intervalo $[0,1]$:**

Usando: $\cos A \sin B = \frac{1}{2}[\sin(A+B) - \sin(A-B)]$

$$x(t) = \cos(4\pi t)\sin(2\pi t) = \frac{1}{2}[\sin(6\pi t) - \sin(2\pi t)]$$

$$\int_0^1 x(t)\,dt = \int_0^1 \frac{1}{2}[\sin(6\pi t) - \sin(2\pi t)]\,dt$$

$$= \frac{1}{2}\left[-\frac{\cos(6\pi t)}{6\pi} + \frac{\cos(2\pi t)}{2\pi}\right]_0^1$$

$$= \frac{1}{2}\left[\left(-\frac{\cos(6\pi)}{6\pi} + \frac{\cos(2\pi)}{2\pi}\right) - \left(-\frac{\cos(0)}{6\pi} + \frac{\cos(0)}{2\pi}\right)\right]$$

$$= \frac{1}{2}\left[\left(-\frac{1}{6\pi} + \frac{1}{2\pi}\right) - \left(-\frac{1}{6\pi} + \frac{1}{2\pi}\right)\right]$$

> **Resultado:** $= 0$

<img width="1087" height="554" alt="Figura11" src="https://github.com/user-attachments/assets/29643b3a-ce91-4b1c-8855-68116d62c35d" />

Isso confirma que $\cos(4\pi t)$ e $\sin(2\pi t)$ são ortogonais no intervalo $[0,1]$.

---

## Exemplos Não Ortogonais

### Caso 1: Frequências Iguais (Função consigo mesma)

$$\int_0^1 \sin^2(2\pi t)\,dt$$

Usando $\sin^2(x) = \frac{1-\cos(2x)}{2}$:

$$= \int_0^1 \frac{1-\cos(4\pi t)}{2}\,dt$$

$$= \frac{1}{2}\left[t - \frac{\sin(4\pi t)}{4\pi}\right]_0^1$$

$$= \frac{1}{2}\left[\left(1 - \frac{\sin(4\pi)}{4\pi}\right) - \left(0 - \frac{\sin(0)}{4\pi}\right)\right]$$

$$= \frac{1}{2}[1 - 0 - 0 + 0] = \frac{1}{2}$$

> **Resultado:** $\neq 0$, portanto não são ortogonais.

<img width="1058" height="828" alt="Figura2" src="https://github.com/user-attachments/assets/0305cb9f-18c3-40e0-9915-4ec88376773d" />

---

### Caso 2: Intervalo Inadequado

Para $x(t) = \cos(4\pi t)\sin(2\pi t)$ no intervalo $[0, 0.5]$:

$$\int_0^{0.5} \cos(4\pi t)\sin(2\pi t)\,dt = \frac{1}{2}\int_0^{0.5} [\sin(6\pi t) - \sin(2\pi t)]\,dt$$

$$= \frac{1}{2}\left[-\frac{\cos(6\pi t)}{6\pi} + \frac{\cos(2\pi t)}{2\pi}\right]_0^{0.5}$$

$$= \frac{1}{2}\left[\left(-\frac{\cos(3\pi)}{6\pi} + \frac{\cos(\pi)}{2\pi}\right) - \left(-\frac{1}{6\pi} + \frac{1}{2\pi}\right)\right]$$

$$= \frac{1}{2}\left[\left(-\frac{(-1)}{6\pi} + \frac{(-1)}{2\pi}\right) - \left(-\frac{1}{6\pi} + \frac{1}{2\pi}\right)\right]$$

$$= \frac{1}{2}\left[\frac{1}{6\pi} - \frac{1}{2\pi} + \frac{1}{6\pi} - \frac{1}{2\pi}\right]$$

$$= \frac{1}{2} \cdot \frac{2}{6\pi} - \frac{1}{2} \cdot \frac{2}{2\pi} = \frac{1}{6\pi} - \frac{1}{2\pi}$$

$$= \frac{1-3}{6\pi} = -\frac{2}{6\pi} = -\frac{1}{3\pi}$$

> **Resultado:** $\neq 0$, confirmando que no intervalo inadequado a ortogonalidade não se mantém.

<img width="1067" height="545" alt="Figura33" src="https://github.com/user-attachments/assets/4f9347bd-c9c9-4986-91ab-a0d870ab1392" />

---

## Ortogonalidade das Exponenciais Complexas

Para exponenciais complexas $e^{jn\omega_0 t}$ e $e^{jm\omega_0 t}$:

$$\int_0^{T_0} e^{jn\omega_0 t} \overline{e^{jm\omega_0 t}}\,dt = \int_0^{T_0} e^{jn\omega_0 t} e^{-jm\omega_0 t}\,dt$$

$$= \int_0^{T_0} e^{j(n-m)\omega_0 t}\,dt$$

**Para $n \neq m$:**

$$= \frac{e^{j(n-m)\omega_0 t}}{j(n-m)\omega_0}\Big|_0^{T_0} = \frac{e^{j(n-m)\omega_0 T_0} - 1}{j(n-m)\omega_0}$$

Como $(n-m)\omega_0 T_0 = (n-m) \cdot 2\pi$, temos $e^{j(n-m) \cdot 2\pi} = 1$

> **Resultado:** $= 0$ quando $n \neq m$

**Para $n = m$:**

$$\int_0^{T_0} e^0\,dt = \int_0^{T_0} 1\,dt = T_0$$

> **Resultado:** $= T_0$ quando $n = m$

---

## Relação entre Exponenciais e Funções Trigonométricas

As fórmulas de Euler:

$$\cos(n\omega_0 t) = \frac{e^{jn\omega_0 t} + e^{-jn\omega_0 t}}{2}$$

$$\sin(n\omega_0 t) = \frac{e^{jn\omega_0 t} - e^{-jn\omega_0 t}}{2j}$$

Mostram que as propriedades de ortogonalidade dos senos e cossenos derivam diretamente da ortogonalidade das exponenciais complexas, uma vez que qualquer combinação linear de funções ortogonais mantém as propriedades de ortogonalidade quando apropriadamente normalizada.

---

## Resumo das Propriedades de Ortogonalidade

$$\int_0^{T_0} \sin(n\omega_0 t)\sin(m\omega_0 t)\,dt = \begin{cases} 0, & n\neq m\\ T_0/2, & n=m \end{cases}$$

$$\int_0^{T_0} \cos(n\omega_0 t)\cos(m\omega_0 t)\,dt = \begin{cases} 0, & n\neq m\\ T_0/2, & n=m \end{cases}$$

$$\int_0^{T_0} \sin(n\omega_0 t)\cos(m\omega_0 t)\,dt = 0$$

$$\int_0^{T_0} e^{j n \omega_0 t} e^{-j m \omega_0 t}\,dt = \begin{cases} T_0, & n=m\\ 0, & n\neq m \end{cases}$$

---

##  Referências
1. **Oppenheim, A. V., & Willsky, A. S.** - *Signals and Systems*
---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas!

1. Faça um **Fork** do projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/NovaVisualizacao`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova visualização'`)
4. **Push** para a branch (`git push origin feature/NovaVisualizacao`)
5. Abra um **Pull Request**

### Ideias de Contribuições

-  Novos exemplos interativos
-  Interface web com Plotly/Dash
-  Tradução para outros idiomas
-  Mais documentação e tutoriais

---

##  Problemas Conhecidos

- Em telas pequenas, os botões podem sobrepor
- Alguns exemplos requerem mais de 1GB de RAM
- A renderização pode ser lenta em computadores antigos

**Soluções:**
```python
# Reduzir número de pontos para melhor performance
t = np.linspace(0, 1, 500)  # ao invés de 1000
```

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
MIT License - Você pode usar, modificar e distribuir livremente!
```

---

## 📧 Contato

**Moisés Diego Cipriano dos Santos**

- 📧 Email: [moises.diego@estudante.ufcg.edu.br]

---



<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**🐛 Encontrou um bug? [Abra uma issue](https://github.com/seu-usuario/ortogonalidade-funcoes/issues)**

**💡 Tem uma sugestão? [Contribua com o projeto!](#-como-contribuir)**

---

*Desenvolvido com ❤️ para facilitar o aprendizado de Sinais e Sistemas*

</div>
