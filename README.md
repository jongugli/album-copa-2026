# Álbum Virtual — Figurinhas Copa do Mundo 2026 🌍

Controle simples e rápido para saber quais figurinhas você tem, quais faltam e quais estão repetidas para trocar.

---

## Como usar

Cada figurinha tem 3 estados — **clique para alternar:**

| Estado | Cor | Significado |
|---|---|---|
| ⬜ Cinza | Não tenho | Ainda precisa dessa |
| ✅ Verde | Tenho | Já colei no álbum |
| 🔄 Laranja | Repetida | Tenho duplicata, boa para troca |

**Botões no topo:**
- **📋 Faltam** — mostra a lista completa com os números que faltam
- **🔄 Repetidas** — mostra os números que você tem a mais para trocar
- **🗑 Zerar** — apaga tudo e começa do zero (pede confirmação)

---

## Rodar localmente

```bash
# 1. Entre na pasta
cd 08-figurinhas-copa-2026

# 2. Crie um ambiente virtual e instale
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt

# 3. Rode o servidor
python app.py

# 4. Abra no navegador
# http://localhost:5000
```

O progresso fica salvo no arquivo `album.db` (SQLite) na mesma pasta.

---

## Deploy gratuito no Render.com

O Render tem um plano gratuito para aplicações web. O disco persistente custa US$ 0.25/GB/mês (menos de R$ 1,50/mês), mas o plano gratuito já inclui 1GB de storage temporário.

### Passo a passo

**1. Suba o código no GitHub**
```bash
git init
git add .
git commit -m "Album Copa 2026"
git remote add origin https://github.com/SEU_USUARIO/album-copa-2026.git
git push -u origin main
```

**2. Crie conta no Render**
- Acesse [render.com](https://render.com)
- Crie conta gratuita (pode usar o GitHub)

**3. Novo Web Service**
- Clique em **New → Web Service**
- Conecte seu repositório GitHub
- Configure:
  - **Name:** album-copa-2026
  - **Runtime:** Python
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
- Clique em **Create Web Service**

**4. Aguarde o deploy (~2 minutos)**
- Render vai exibir a URL pública: `https://album-copa-2026.onrender.com`

**Nota sobre persistência no plano gratuito:**
O plano free do Render pode reiniciar o serviço após inatividade, o que pode apagar o `album.db`. Para persistência garantida, adicione um **Disk** no painel do serviço (US$ 0.25/GB/mês ≈ R$ 1,50/mês).

### Alternativa ainda mais barata: Railway

```bash
# Com Railway CLI
npm install -g @railway/cli
railway login
railway init
railway up
```

Railway tem US$ 5 de crédito gratuito por mês — suficiente para este projeto.

---

## Estrutura do projeto

```
08-figurinhas-copa-2026/
├── app.py              # Servidor Flask (rotas e banco de dados)
├── stickers_data.py    # Todos os números e nomes das figurinhas
├── templates/
│   └── index.html      # Interface completa (HTML + CSS + JS)
├── requirements.txt    # Flask + Gunicorn
├── render.yaml         # Configuração de deploy automático
└── README.md
```

---

## Álbum: 680 figurinhas

| Seção | Qtd |
|---|---|
| Abertura | 30 |
| Sedes (EUA, Canadá, México) | 56 |
| Brasil, Argentina, França, Inglaterra, Espanha, Portugal | 90 |
| Alemanha, Holanda, Bélgica, Itália, Croácia, Suíça | 90 |
| Dinamarca, Sérvia, Polônia, Turquia, Escócia, Suécia | 90 |
| Uruguai, Colômbia, Equador, Paraguai | 60 |
| Marrocos, Nigéria, Senegal, Egito, Camarões, Costa do Marfim, Gana, Tunísia | 120 |
| Japão, Coreia do Sul, Austrália, Irã, Arábia Saudita | 75 |
| Jamaica, Costa Rica, Nova Zelândia | 45 |
| Especiais ⭐ | 24 |

> **Nota:** Os números exatos serão confirmados quando a Panini lançar o álbum oficial. Para atualizar, edite o arquivo `stickers_data.py`.

---

## Como atualizar os números quando o álbum sair

```python
# stickers_data.py

# Altere o range das figurinhas de cada seção:
{
    "id": "brasil",
    "label": "Brasil",
    "emoji": "🇧🇷",
    "stickers": make_stickers(87, 101, [
        "Brasão Brasil",
        "Vinicius Jr.",
        # ... nomes reais do álbum
    ]),
}
```
