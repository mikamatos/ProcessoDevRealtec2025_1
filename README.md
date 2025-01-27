# Simulação de Controle de Temperatura
Este projeto é uma simulação de controle de temperatura utilizando Python, com a biblioteca Pygame para a interface gráfica e Matplotlib para a visualização dos dados gerados. A simulação demonstra um sistema de controle de temperatura que alterna entre aquecimento e resfriamento de acordo com limites definidos.

# Funcionalidades

Simulação do Sistema de Controle de Temperatura:
- Um motor que aquece ou resfria o sistema com base em limites predefinidos.
- Representação visual da temperatura atual e estado do motor (ligado/desligado).

Interface Gráfica (Pygame):
- Barra de temperatura dinâmica.
- Exibição dos limites de temperatura para ligar/desligar o motor.
- Indicador do estado do motor e da temperatura atual.

Visualização de Dados (Matplotlib):
- Gráfico da variação da temperatura ao longo do tempo.
- Linhas indicativas para os limites de ligar e desligar o motor.

# Requisitos
- Python 3.8+
  
Bibliotecas necessárias:
- pygame
- matplotlib

Instale as bibliotecas necessárias com o comando:
```
pip install pygame matplotlib
```

# Como Executar
Salve o código em um arquivo, por exemplo, controle_temperatura.py.
Execute o script:
```
python controle_temperatura.py
```

# Componentes Principais
Simulação (simular_temperatura):
- Realiza a simulação do sistema, alternando entre aquecimento e resfriamento.
- Atualiza a interface gráfica em tempo real com o estado do motor e a temperatura.
  
Gráfico (exibir_grafico):
- Gera um gráfico mostrando a variação da temperatura durante a simulação.
- Inclui linhas de referência para os limites de ligar/desligar o motor.
  
# Controles
- Fechar a janela do Pygame: Encerra a simulação e exibe o gráfico
