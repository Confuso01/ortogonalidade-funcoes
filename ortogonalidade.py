import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.gridspec as gridspec

class OrtogonalityVisualizer:
    def __init__(self):
        self.t = np.linspace(0, 1, 1000)
        self.current_example = 0
        self.setup_figure()
        self.examples = [
            self.exemplo_ortogonal_principal,
            self.exemplo_senos_ortogonais,
            self.exemplo_cossenos_ortogonais,
            self.exemplo_seno_cosseno,
            self.exemplo_nao_ortogonal_mesmo,
            self.exemplo_nao_ortogonal_intervalo,
            self.exemplo_freq_proximas,
            self.exemplo_decomposicao
        ]
        self.titles = [
            "Exemplo Principal: cos(4πt) × sin(2πt)",
            "Senos Ortogonais: sin(2πt) × sin(4πt)", 
            "Cossenos Ortogonais: cos(2πt) × cos(6πt)",
            "Seno × Cosseno: sin(2πt) × cos(4πt)",
            "Não-Ortogonal: sin²(2πt)",
            "Intervalo Inadequado: Análise Detalhada",
            "Frequências Próximas: Efeito de Batimento",
            "Decomposição Trigonométrica"
        ]
        self.show_example()

    def setup_figure(self):
        plt.style.use("seaborn-v0_8-whitegrid")
        self.fig = plt.figure(figsize=(18, 11))
        
        # Layout melhorado com GridSpec
        gs = gridspec.GridSpec(3, 4, figure=self.fig, 
                              width_ratios=[3, 3, 3, 1], 
                              height_ratios=[1, 1, 1],
                              hspace=0.3, wspace=0.3)
        
        # Áreas principais para gráficos
        self.ax1 = self.fig.add_subplot(gs[0, :3])
        self.ax2 = self.fig.add_subplot(gs[1, :3])
        self.ax3 = self.fig.add_subplot(gs[2, :3])
        
        # Área para botões (coluna da direita)
        button_area = self.fig.add_subplot(gs[:, 3])
        button_area.axis("off")
        
        # Criar botões verticais mais organizados
        self.buttons = []
        button_info = [
            ("Exemplo Principal", "lightblue"),
            ("Senos Ortogonais", "lightgreen"),
            ("Cossenos Ortogonais", "lightcoral"),
            ("Seno × Cosseno", "lightyellow"),
            ("sin² (Não-Ortog.)", "lightpink"),
            ("Intervalo Inade.", "lightgray"),
            ("Freq. Próximas", "lavender"),
            ("Decomposição", "lightcyan")
        ]
        
        for i, (name, color) in enumerate(button_info):
            # Posicionamento vertical dos botões
            # Ajustado: x de 0.78 para 0.80, largura de 0.18 para 0.15, altura de 0.08 para 0.06
            # Espaçamento vertical (i*0.1 para i*0.08) também foi ajustado.
            ax_button = plt.axes([0.80, 0.85 - i*0.08, 0.15, 0.06])
            button = Button(ax_button, name, color=color, hovercolor="white")
            button.label.set_fontsize(9) # Reduzido para caber melhor
            button.label.set_weight("bold")
            button.on_clicked(lambda event, idx=i: self.change_example(idx))
            self.buttons.append(button)

    def change_example(self, example_idx):
        self.current_example = example_idx
        self.show_example()
        
        # Destacar botão ativo
        for i, button in enumerate(self.buttons):
            if i == example_idx:
                button.color = "gold"
                button.hovercolor = "orange"
            else:
                # Restaurar cores originais - CORES COMPACTAS
                colors = ["lightblue", "lightgreen", "lightcoral", "lightyellow", 
                         "lightpink", "lightgray", "lavender", "lightcyan"]
                button.color = colors[i]
                button.hovercolor = "white"

    def show_example(self):
        # Limpar gráficos
        for ax in [self.ax1, self.ax2, self.ax3]:
            ax.clear()
            ax.grid(True, alpha=0.3)
        
        # Mostrar exemplo atual
        self.examples[self.current_example]()
        
        # Título principal mais visível
        self.fig.suptitle(f"{self.titles[self.current_example]}", 
                         fontsize=18, fontweight="bold", y=0.95)
        plt.draw()

    def exemplo_ortogonal_principal(self):
        f1 = np.cos(4*np.pi*self.t)
        f2 = np.sin(2*np.pi*self.t)
        produto = f1 * f2
        
        I1 = np.trapz(produto, self.t)
        mask = self.t <= 0.5
        I2 = np.trapz(produto[mask], self.t[mask])
        
        # Funções originais
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="cos(4πt)", alpha=0.8)
        self.ax1.plot(self.t, f2, "red", linewidth=3, label="sin(2πt)", alpha=0.8)
        self.ax1.set_title("Funções Originais", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        # Produto em [0,1] - ORTOGONAL
        self.ax2.plot(self.t, produto, "green", linewidth=3)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        pos_mask = produto >= 0
        self.ax2.fill_between(self.t, produto, 0, where=pos_mask, 
                             color="dodgerblue", alpha=0.6, label="Área Positiva")
        self.ax2.fill_between(self.t, produto, 0, where=~pos_mask, 
                             color="crimson", alpha=0.6, label="Área Negativa")
        self.ax2.set_title(f"Produto em [0,1]: ∫ = {I1:.8f} ≈ 0 ✓ ORTOGONAIS", 
                          fontsize=14, fontweight="bold", color="green")
        self.ax2.set_ylabel("cos(4πt) × sin(2πt)", fontsize=12)
        self.ax2.legend(fontsize=12)
        
        # Produto em [0,0.5] - NÃO ORTOGONAL
        self.ax3.plot(self.t[mask], produto[mask], "darkorange", linewidth=4)
        self.ax3.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax3.fill_between(self.t[mask], produto[mask], 0, alpha=0.6, color="orange")
        self.ax3.set_title(f"Produto em [0,0.5]: ∫ = {I2:.6f} ≠ 0 ✗ NÃO-ORTOGONAIS", 
                          fontsize=14, fontweight="bold", color="red")
        self.ax3.set_ylabel("cos(4πt) × sin(2πt)", fontsize=12)
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.set_xlim(0, 0.5)

    def exemplo_senos_ortogonais(self):
        f1 = np.sin(2*np.pi*self.t)
        f2 = np.sin(4*np.pi*self.t)
        produto = f1 * f2
        integral = np.trapz(produto, self.t)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="sin(2πt) - freq = 1 Hz")
        self.ax1.plot(self.t, f2, "red", linewidth=3, label="sin(4πt) - freq = 2 Hz")
        self.ax1.set_title("Senos com Frequências Diferentes (n ≠ m)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, produto, "purple", linewidth=3)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax2.fill_between(self.t, produto, 0, alpha=0.5, color="purple")
        self.ax2.set_title(f"sin(2πt) × sin(4πt): ∫ = {integral:.8f} ≈ 0 ✓", 
                          fontsize=14, fontweight="bold", color="green")
        self.ax2.set_ylabel("Produto", fontsize=12)
        
        # Análise detalhada do cancelamento
        pos_mask = produto >= 0
        area_pos = np.trapz(produto[pos_mask], self.t[pos_mask])
        area_neg = np.trapz(produto[~pos_mask], self.t[~pos_mask])
        
        self.ax3.fill_between(self.t, produto, 0, where=pos_mask, 
                             color="blue", alpha=0.7, label=f"Área + = {area_pos:.4f}")
        self.ax3.fill_between(self.t, produto, 0, where=~pos_mask, 
                             color="red", alpha=0.7, label=f"Área - = {area_neg:.4f}")
        self.ax3.axhline(0, color="black", linestyle="--", linewidth=2)
        self.ax3.set_title("Cancelamento Perfeito: Área+ + Área- ≈ 0", 
                          fontsize=14, fontweight="bold")
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.set_ylabel("Produto", fontsize=12)
        self.ax3.legend(fontsize=12)

    def exemplo_cossenos_ortogonais(self):
        f1 = np.cos(2*np.pi*self.t)
        f2 = np.cos(6*np.pi*self.t)
        produto = f1 * f2
        integral = np.trapz(produto, self.t)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="cos(2πt) - freq = 1 Hz")
        self.ax1.plot(self.t, f2, "red", linewidth=3, label="cos(6πt) - freq = 3 Hz")
        self.ax1.set_title("Cossenos com Frequências Diferentes (n ≠ m)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, produto, "green", linewidth=3)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax2.fill_between(self.t, produto, 0, alpha=0.5, color="green")
        self.ax2.set_title(f"cos(2πt) × cos(6πt): ∫ = {integral:.8f} ≈ 0 ✓", 
                          fontsize=14, fontweight="bold", color="green")
        self.ax2.set_ylabel("Produto", fontsize=12)
        
        # Mostrar oscilações rápidas
        self.ax3.plot(self.t, produto, "green", linewidth=2, alpha=0.8)
        self.ax3.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        
        # Destacar regiões de cancelamento
        for i in range(0, len(self.t), 100):
            if i + 100 < len(self.t):
                section = slice(i, i + 100)
                color = "lightblue" if i % 200 == 0 else "lightcoral"
                self.ax3.fill_between(self.t[section], produto[section], 0, 
                                     alpha=0.4, color=color)
        
        self.ax3.set_title("Oscilações Rápidas: Cancelamento por Seções", 
                          fontsize=14, fontweight="bold")
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.set_ylabel("Produto", fontsize=12)

    def exemplo_seno_cosseno(self):
        f1 = np.sin(2*np.pi*self.t)
        f2 = np.cos(4*np.pi*self.t)
        produto = f1 * f2
        integral = np.trapz(produto, self.t)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="sin(2πt)")
        self.ax1.plot(self.t, f2, "red", linewidth=3, label="cos(4πt)")
        self.ax1.set_title("Seno × Cosseno (SEMPRE Ortogonais)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, produto, "brown", linewidth=3)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax2.fill_between(self.t, produto, 0, alpha=0.5, color="brown")
        self.ax2.set_title(f"sin(2πt) × cos(4πt): ∫ = {integral:.8f} ≈ 0 ✓", 
                          fontsize=14, fontweight="bold", color="green")
        self.ax2.set_ylabel("Produto", fontsize=12)
        
        # Texto explicativo sobre a propriedade
        self.ax3.text(0.5, 0.7, "📋 PROPRIEDADE FUNDAMENTAL:", 
                     ha="center", va="center", fontsize=16, fontweight="bold",
                     bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        
        self.ax3.text(0.5, 0.45, "∫ sin(n·ω₀·t) × cos(m·ω₀·t) dt = 0", 
                     ha="center", va="center", fontsize=18, fontweight="bold",
                     bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.9))
        
        self.ax3.text(0.5, 0.2, "para QUALQUER valor de n e m\n(frequências diferentes ou iguais)", 
                     ha="center", va="center", fontsize=14,
                     bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.8))
        
        self.ax3.set_xlim(0, 1)
        self.ax3.set_ylim(0, 1)
        self.ax3.axis("off")

    def exemplo_nao_ortogonal_mesmo(self):
        f1 = np.sin(2*np.pi*self.t)
        f_squared = f1**2
        integral = np.trapz(f_squared, self.t)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="sin(2πt)")
        self.ax1.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.5)
        self.ax1.set_title("Função Original: sin(2πt)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, f_squared, "red", linewidth=4)
        self.ax2.fill_between(self.t, f_squared, 0, alpha=0.6, color="red")
        self.ax2.axhline(0.5, color="green", linestyle="--", linewidth=2, alpha=0.7, label="Valor Médio = 0.5")
        self.ax2.set_title(f"sin²(2πt): ∫ = {integral:.4f} ≠ 0 ✗ NÃO-ORTOGONAL", 
                          fontsize=14, fontweight="bold", color="red")
        self.ax2.set_ylabel("sin²(2πt)", fontsize=12)
        self.ax2.legend(fontsize=12)
        
        # Decomposição de sin^2(x) = 0.5 - 0.5cos(2x)
        self.ax3.plot(self.t, 0.5 - 0.5 * np.cos(4*np.pi*self.t), "purple", linewidth=3, label="0.5 - 0.5cos(4πt)")
        self.ax3.axhline(0.5, color="green", linestyle="--", linewidth=2, alpha=0.7, label="Componente DC (0.5)")
        self.ax3.set_title("Decomposição: sin²(x) = 0.5 - 0.5cos(2x)", 
                          fontsize=14, fontweight="bold")
        self.ax3.set_ylabel("Amplitude", fontsize=12)
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.legend(fontsize=12)
        self.ax3.set_ylim(-0.2, 1.2)

    def exemplo_nao_ortogonal_intervalo(self):
        f1 = np.cos(2*np.pi*self.t)
        f2 = np.sin(2*np.pi*self.t)
        produto = f1 * f2
        
        # Intervalo de integração de 0 a 0.5
        mask_intervalo = self.t <= 0.5
        t_intervalo = self.t[mask_intervalo]
        produto_intervalo = produto[mask_intervalo]
        integral_intervalo = np.trapz(produto_intervalo, t_intervalo)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=3, label="cos(2πt)")
        self.ax1.plot(self.t, f2, "red", linewidth=3, label="sin(2πt)")
        self.ax1.set_title("Funções Ortogonais (mas intervalo importa!)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, produto, "purple", linewidth=3)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax2.fill_between(self.t, produto, 0, alpha=0.5, color="purple")
        self.ax2.set_title(f"Produto cos(2πt) × sin(2πt): ∫[0,1] = {np.trapz(produto, self.t):.8f} ≈ 0", 
                          fontsize=14, fontweight="bold", color="green")
        self.ax2.set_ylabel("Produto", fontsize=12)
        
        self.ax3.plot(t_intervalo, produto_intervalo, "darkorange", linewidth=4)
        self.ax3.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax3.fill_between(t_intervalo, produto_intervalo, 0, alpha=0.6, color="orange")
        self.ax3.set_title(f"∫[0,0.5] = {integral_intervalo:.6f} ≠ 0 ✗ Intervalo Inadequado", 
                          fontsize=14, fontweight="bold", color="red")
        self.ax3.set_ylabel("Produto", fontsize=12)
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.set_xlim(0, 0.5)

    def exemplo_freq_proximas(self):
        f1 = np.sin(2*np.pi*self.t * 10) # Frequência 10 Hz
        f2 = np.sin(2*np.pi*self.t * 10.5) # Frequência 10.5 Hz
        produto = f1 * f2
        integral = np.trapz(produto, self.t)
        
        self.ax1.plot(self.t, f1, "blue", linewidth=2, label="sin(20πt)")
        self.ax1.plot(self.t, f2, "red", linewidth=2, label="sin(21πt)")
        self.ax1.set_title("Frequências Próximas: Efeito de Batimento", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.ax2.plot(self.t, produto, "green", linewidth=2)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=2, alpha=0.7)
        self.ax2.fill_between(self.t, produto, 0, alpha=0.5, color="green")
        self.ax2.set_title(f"Produto: ∫ = {integral:.4f} (quase zero, mas não ideal)", 
                          fontsize=14, fontweight="bold", color="darkorange")
        self.ax2.set_ylabel("Produto", fontsize=12)
        
        # Envelope do batimento
        envelope = np.cos(2*np.pi*self.t * 0.25) # Frequência de batimento (10.5-10)/2 = 0.25
        self.ax3.plot(self.t, produto, "gray", alpha=0.6, label="Produto")
        self.ax3.plot(self.t, envelope, "--", color="blue", label="Envelope Superior")
        self.ax3.plot(self.t, -envelope, "--", color="blue", label="Envelope Inferior")
        self.ax3.set_title("Batimento: Envelope de Amplitude", fontsize=14, fontweight="bold")
        self.ax3.set_ylabel("Amplitude", fontsize=12)
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.legend(fontsize=12)
        self.ax3.set_ylim(-1.2, 1.2)

    def exemplo_decomposicao(self):
        # Exemplo de uma função arbitrária e sua decomposição em série de Fourier
        # Para simplificar, vamos usar uma onda quadrada aproximada
        t_decomp = np.linspace(0, 1, 1000, endpoint=False)
        onda_quadrada = np.zeros_like(t_decomp)
        onda_quadrada[t_decomp < 0.5] = 1
        onda_quadrada[t_decomp >= 0.5] = -1
        
        # Aproximação com poucos termos da série de Fourier
        aprox_fourier = np.zeros_like(t_decomp)
        for n in range(1, 10, 2): # Apenas termos ímpares
            aprox_fourier += (4/np.pi) * (1/n) * np.sin(n * 2 * np.pi * t_decomp)
            
        self.ax1.plot(t_decomp, onda_quadrada, "blue", linewidth=3, label="Onda Quadrada")
        self.ax1.set_title("Função Original (Onda Quadrada)", fontsize=14, fontweight="bold")
        self.ax1.set_ylabel("Amplitude", fontsize=12)
        self.ax1.legend(fontsize=12)
        self.ax1.set_ylim(-1.5, 1.5)
        
        self.ax2.plot(t_decomp, aprox_fourier, "red", linewidth=3, label="Aproximação Fourier (9 termos)")
        self.ax2.set_title("Aproximação por Série de Fourier", fontsize=14, fontweight="bold")
        self.ax2.set_ylabel("Amplitude", fontsize=12)
        self.ax2.legend(fontsize=12)
        self.ax2.set_ylim(-1.5, 1.5)
        
        # Mostrar a contribuição de um termo individual
        termo_individual = (4/np.pi) * np.sin(1 * 2 * np.pi * t_decomp) # Primeiro termo
        self.ax3.plot(t_decomp, termo_individual, "green", linewidth=3, label="Primeiro Termo (n=1)")
        self.ax3.set_title("Componente Individual da Série de Fourier", fontsize=14, fontweight="bold")
        self.ax3.set_ylabel("Amplitude", fontsize=12)
        self.ax3.set_xlabel("Tempo (t)", fontsize=12)
        self.ax3.legend(fontsize=12)
        self.ax3.set_ylim(-1.5, 1.5)


if __name__ == "__main__":
    visualizer = OrtogonalityVisualizer()
    plt.show()


