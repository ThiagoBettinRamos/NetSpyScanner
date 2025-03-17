# 📡 NetSpyScanner - Scanner de Rede Inteligente

![GitHub repo size](https://img.shields.io/github/repo-size/ThiagoBettinRamos/NetSpyScanner?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/ThiagoBettinRamos/NetSpyScanner?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/ThiagoBettinRamos/NetSpyScanner?style=for-the-badge)

**NetSpyScanner** é uma ferramenta avançada para **análise e monitoramento de redes locais**, permitindo identificar dispositivos conectados, serviços ativos e portas abertas. Ideal para profissionais de cibersegurança, administradores de rede e entusiastas da área.

---

## 🚀 Funcionalidades
✅ Escaneia dispositivos conectados na rede  
✅ Identifica endereços IP e MAC  
✅ Descobre portas abertas e serviços ativos  
✅ Permite salvar logs da análise  
✅ Interface CLI intuitiva e fácil de usar  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Scapy** (para análise de pacotes)
- **Socket** (para conexões de rede)
- **Argparse** (para argumentos na CLI)
- **Rich** (para saída colorida no terminal)

---

## 📥 Instalação e Uso

### 1️⃣ Clonar o repositório
```sh
git clone https://github.com/ThiagoBettinRamos/NetSpyScanner.git
cd NetSpyScanner
```

### 2️⃣ Criar ambiente virtual (opcional)
```sh
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Executar o scanner
```sh
python netspy.py --target 192.168.1.1/24
```
> 🔹 **Observação:** É necessário rodar como **administrador/root** para obter informações completas.

---

## 🎯 Exemplos de Uso

🔍 **Escanear rede local**
```sh
python netspy.py --target 192.168.1.1/24
```

🔍 **Verificar portas abertas de um IP**
```sh
python netspy.py --target 192.168.1.10 --scan-ports
```

🔍 **Salvar o resultado em um arquivo**
```sh
python netspy.py --target 192.168.1.1/24 --output results.txt
```

---

## ⚡ Melhorias Futuras
🔹 Criar interface gráfica (GUI)  
🔹 Suporte a IPv6  
🔹 Integração com base de dados para identificação de fabricantes  

---

## 🏆 Contribuindo
Sinta-se à vontade para contribuir! Para isso:
1. Faça um **fork** do projeto
2. Crie uma **branch** (`git checkout -b feature-nova-funcionalidade`)
3. Faça suas **modificações** e **commits**
4. Envie um **pull request**

---

## 🛡️ Aviso Legal
Este projeto é destinado a **fins educacionais** e testes em **redes autorizadas**. O uso indevido pode violar leis de privacidade e segurança.

---

## 👨‍💻 Autor
Feito com ❤️ por **Thiago Bettin Ramos**  
🔗 [GitHub](https://github.com/ThiagoBettinRamos) | [LinkedIn](https://www.linkedin.com/in/thiago-bettin-ramos-91b878238/)

