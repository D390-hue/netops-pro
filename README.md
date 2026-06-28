# 🖥️ NetOps Pro — Plateforme IT complète

> Application web Python/Flask de monitoring, sécurité, automatisation et surveillance réseau — conçue pour les environnements Helpdesk et Admin IT.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🎯 Vue d'ensemble

**NetOps Pro** est une plateforme IT web unifiée qui regroupe 4 modules essentiels :

| Module | Description |
|--------|-------------|
| 📊 **Dashboard temps réel** | CPU, RAM, disques, réseau — métriques live avec graphiques |
| 🌐 **Monitoring réseau** | Scanner de ports, suivi des hôtes, analyse des risques |
| 🔴 **Sécurité / IDS** | Détection d'intrusion, alertes de sécurité, simulateur d'événements |
| ⚙️ **Automatisation IT** | Gestion utilisateurs AD, reset MDP, tâches planifiées, rapports |

---

## 📸 Interface

```
┌─────────────────────────────────────────────────────┐
│ NetOpsPro  📊 Dashboard  🌐 Réseau  🔴 Sécurité  ⚙️  │
├──────────┬──────────────────────────────────────────┤
│          │  CPU: 34%  RAM: 6.2Go  Réseau: 124KB/s  │
│ Justin   │  ──────────────────────────────────────  │
│  Doglo   │  [Graphique CPU 60s] [Graphique RAM 60s] │
│  Admin   │  ──────────────────────────────────────  │
│          │  Disques   Processus   Interfaces réseau │
└──────────┴──────────────────────────────────────────┘
```

---

## 🚀 Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/justindoglo/netops-pro.git
cd netops-pro

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python app.py
```

Ouvrez votre navigateur sur **http://127.0.0.1:5000**

---

## 📁 Structure du projet

```
netops-pro/
│
├── app.py                        # Application Flask principale
├── requirements.txt
├── README.md
│
├── modules/
│   ├── dashboard/
│   │   └── metrics.py            # Collecte métriques système (psutil)
│   ├── network/
│   │   └── monitor.py            # Scanner réseau, monitoring hôtes
│   ├── security/
│   │   └── ids.py                # Détection d'intrusion, gestion alertes
│   └── automation/
│       └── engine.py             # Gestion utilisateurs AD, tâches
│
├── templates/
│   ├── index.html                # Dashboard
│   ├── network.html              # Page réseau
│   ├── security.html             # Page sécurité
│   └── automation.html           # Page automatisation
│
├── static/
│   ├── css/main.css              # Design système
│   └── js/
│       ├── dashboard.js          # Graphiques temps réel
│       ├── network.js            # Scanner réseau
│       ├── security.js           # Alertes IDS
│       └── automation.js        # Gestion utilisateurs
│
└── data/
    ├── logs/                     # Hôtes et utilisateurs (JSON)
    ├── alerts/                   # Alertes de sécurité (JSON)
    └── reports/                  # Rapports générés
```

---

## 🔧 Fonctionnalités détaillées

### 📊 Dashboard
- Métriques CPU, RAM, réseau actualisées toutes les 3 secondes
- Graphiques historique 60 secondes (Chart.js)
- Top 5 processus par consommation CPU
- Vue de toutes les interfaces réseau

### 🌐 Réseau
- Scanner ping sweep sur plage CIDR complète
- Scan multi-threadé de 18 ports courants (SSH, RDP, LDAP, SMB…)
- Évaluation automatique du risque (LOW / MEDIUM / HIGH)
- Historique des hôtes connus avec suivi de disponibilité

### 🔴 Sécurité / IDS
- Règles de détection : scan de ports, bruteforce SSH/RDP, ports suspects
- Simulateur d'événements réseau pour tester les règles
- Gestion des alertes : ouverture → résolution
- Statistiques par sévérité (CRITICAL / HIGH / MEDIUM / LOW)

### ⚙️ Automatisation IT
- Gestion des comptes utilisateurs (simulation Active Directory)
- Création de comptes avec génération de mot de passe sécurisé
- Réinitialisation de mots de passe
- Désactivation de comptes (déprovisioning M365)
- 8 tâches IT automatisées (audit, backup, nettoyage, synchronisation AD…)
- Génération de rapports JSON

---

## 🛠️ Technologies

| Couche | Technologie |
|--------|-------------|
| Backend | Python 3.8+, Flask 3 |
| Métriques | psutil |
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Graphiques | Chart.js 4 |
| Stockage | JSON (sans base de données) |
| Réseau | socket, subprocess, concurrent.futures |

---

## 🔐 Sécurité

> Ce projet est conçu à des fins éducatives et de démonstration. Le module réseau effectue des pings et scans TCP — à utiliser uniquement sur des réseaux dont vous avez l'autorisation.

---

## 👤 Auteur

**DOGLO Koami Justin**  
Technicien Support IT — Helpdesk N1/N2/N3  
📍 Meknès, Maroc  
📧 doglojustin5@gmail.com  
🔗 [linkedin.com/in/justindoglo](https://linkedin.com/in/justindoglo)  
🌐 [justindoglo.github.io](https://justindoglo.github.io)

---

## 📄 Licence

MIT License — libre d'utilisation et de modification.
