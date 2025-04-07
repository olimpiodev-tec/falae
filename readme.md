# ✨ Falaê

## 1. 🛠 Descrição
O projeto consiste em converter texto para áudio permitindo uma pré visualização do resultado diretamente na página.

## 2. 💻 Tecnologias Utilizadas
A implementação do projeto será feito utilizando as seguintes tecnologias:
- **📝 Linguagem**: Python
- **🛠 Framework**: Flask

## 3. 📚 Bibliotecas do projeto
O projeto faz uso de ambiente virtual **python** com as bibliotecas abaixo instaladas:
- 🛠 [Flask](https://flask.palletsprojects.com/en/stable/)
- 🛠 [gTTS](https://gtts.readthedocs.io/en/latest/)
- 🛠 [gunicorn](https://gunicorn.org/)

O **gunicorn** é usado para realizar a publicação na plataforma [Render](https://render.com/)

Para instalar as bibliotecas <ins>crie e ative o ambiente virtual python</ins> no sistema operacional que você estiver usando, então execute os comandos abaixo:
```
pip install Flask
pip install gunicorn
pip install gTTS
```

## 4. 🛠 Estrutura do Projeto
A organização do projeto seguirá a estrutura abaixo:
```
📁 falae/
├── 📁 static/
│   │   ├── 📁 audio
│   │   ├── 📁 css
│   │       ├── 📄 styles.css
│   │   ├── 📁 img
│   │        ├── 📄 favicon.png
│   │   ├── 📁 js
│   │        ├── 📄 index.js
│   📁 templates/
│   │   ├── 📄 index.html
├── 📄 main.py
├── 📄 req.txt
```