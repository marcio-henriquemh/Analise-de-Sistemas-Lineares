# Funções Matemáticas em Python: Degrau e Seno

Este projeto tem como objetivo estudar e visualizar **funções matemáticas** utilizadas em **Sinais e Sistemas**, como a **função degrau unitário** e **funções senoidais**.  
O código é implementado em **Python** de forma didática e utiliza a biblioteca `matplotlib` para plotagem dos gráficos.

---

## 📘 Conceitos

### 🪜 Função Degrau Unitário

A função degrau unitário, ou função de Heaviside, é definida como:

\[
u(t) =
\begin{cases}
0, & t < 0 \\
1, & t \ge 0
\end{cases}
\]

Ela representa sinais que **iniciam em um determinado instante**.

---

### 🔁 Função Senoidal

A função seno é definida como:

\[
y(t) = A \cdot \sin(2\pi f t + \phi)
\]

- \(A\) → Amplitude (máximo e mínimo da função)  
- \(f\) → Frequência (quantos ciclos ocorrem por unidade de tempo)  
- \(\phi\) → Fase (deslocamento horizontal do gráfico)  

Exemplo: `y(t) = sin(x)`, `y(t) = 0.5·sin(2x - π)`.

---

### 🧩 Funções Compostas do Projeto

1. **y(t) = u(t) + 1/2 · sen(2x - π)**  
   Combina a função degrau com uma senoide, representando um sinal que **liga em t = 0** e depois é modulado por uma onda senoidal.

2. **y(t) = (sen(x))² · u(x - 1)**  
   Combina o **seno ao quadrado** com um degrau deslocado, fazendo com que o sinal só apareça a partir de `x = 1`.

---

