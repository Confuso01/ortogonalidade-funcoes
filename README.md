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

### Por que Seno e Cosseno são Ortogonais?

A ortogonalidade vem das **identidades trigonométricas**:

```
sin(A)sin(B) = ½[cos(A-B) - cos(A+B)]
cos(A)cos(B) = ½[cos(A-B) + cos(A+B)]
sin(A)cos(B) = ½[sin(A+B) + sin(A-B)]
```

Quando integramos sobre um período completo, os termos cosseno e seno se anulam!

### Fórmulas de Euler

```
cos(nω₀t) = (e^(jnω₀t) + e^(-jnω₀t))/2
sin(nω₀t) = (e^(jnω₀t) - e^(-jnω₀t))/(2j)
```

As propriedades de ortogonalidade de seno/cosseno **derivam** da ortogonalidade das exponenciais complexas.

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
