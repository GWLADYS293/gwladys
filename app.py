from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>App Docker - Gwladys</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 60px 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
            max-width: 600px;
            width: 90%;
        }
        .logo { font-size: 70px; margin-bottom: 20px; }
        h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle { color: rgba(255,255,255,0.7); margin: 10px 0 25px; }
        .badge {
            display: inline-block;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7);
            padding: 8px 20px;
            border-radius: 50px;
            font-weight: 600;
            margin: 5px;
        }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px; }
        .card {
            background: rgba(255,255,255,0.07);
            border-radius: 12px;
            padding: 15px;
        }
        .label { font-size: 0.75rem; color: rgba(255,255,255,0.5); text-transform: uppercase; }
        .value { color: #00d2ff; font-weight: 600; margin-top: 4px; }
        footer { margin-top: 30px; font-size: 0.85rem; color: rgba(255,255,255,0.4); }
        footer strong { color: #00d2ff; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🐳</div>
        <h1>Application Conteneurisée</h1>
        <p class="subtitle">Déployée avec Docker & Flask • KEYCE Informatique</p>
        <div>
            <span class="badge">🚀 Flask</span>
            <span class="badge">🐳 Docker</span>
            <span class="badge">🐍 Python 3.9</span>
        </div>
        <div class="grid">
            <div class="card"><div class="label">Statut</div><div class="value">✅ En ligne</div></div>
            <div class="card"><div class="label">Port</div><div class="value">5000</div></div>
            <div class="card"><div class="label">Technologie</div><div class="value">Flask + Docker</div></div>
            <div class="card"><div class="label">Méthode</div><div class="value">DevOps / Agile</div></div>
        </div>
        <footer>
            Bonjour à tous — Application conteneurisée avec Docker par <strong>Gwladys</strong><br>
            KEYCE — CC1 Conduite de Projet 2026
        </footer>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
