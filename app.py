"""
NetOps Pro — Plateforme IT complète
====================================
Application web Flask couvrant :
  - Cybersécurité (IDS, détection de menaces)
  - Dashboard temps réel
  - Automatisation IT (utilisateurs, rapports)
  - Monitoring réseau

Auteur : DOGLO Koami Justin
GitHub : https://github.com/justindoglo
"""

from flask import Flask, render_template, jsonify, request
from modules.network.monitor   import NetworkMonitor
from modules.security.ids      import ThreatDetector
from modules.automation.engine import AutomationEngine
from modules.dashboard.metrics import MetricsCollector
import threading, json, os

app = Flask(__name__)

# ── Instances globales ──────────────────────────────────────────
monitor    = NetworkMonitor()
ids        = ThreatDetector()
automation = AutomationEngine()
metrics    = MetricsCollector()

# ── Démarrage des threads de surveillance ───────────────────────
def start_background():
    t1 = threading.Thread(target=monitor.start_monitoring,  daemon=True)
    t2 = threading.Thread(target=ids.start_detection,       daemon=True)
    t1.start(); t2.start()

# ══════════════════════════════════════════════════════
#  ROUTES — PAGES
# ══════════════════════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/security")
def security():
    return render_template("security.html")

@app.route("/network")
def network():
    return render_template("network.html")

@app.route("/automation")
def automation_page():
    return render_template("automation.html")

# ══════════════════════════════════════════════════════
#  API — DASHBOARD
# ══════════════════════════════════════════════════════

@app.route("/api/metrics")
def api_metrics():
    return jsonify(metrics.collect())

@app.route("/api/metrics/history")
def api_metrics_history():
    return jsonify(metrics.get_history())

# ══════════════════════════════════════════════════════
#  API — RÉSEAU
# ══════════════════════════════════════════════════════

@app.route("/api/network/scan", methods=["POST"])
def api_scan():
    data   = request.get_json()
    target = data.get("target", "127.0.0.1")
    result = monitor.scan(target)
    return jsonify(result)

@app.route("/api/network/hosts")
def api_hosts():
    return jsonify(monitor.get_known_hosts())

@app.route("/api/network/status")
def api_network_status():
    return jsonify(monitor.get_status())

# ══════════════════════════════════════════════════════
#  API — SÉCURITÉ
# ══════════════════════════════════════════════════════

@app.route("/api/security/alerts")
def api_alerts():
    return jsonify(ids.get_alerts())

@app.route("/api/security/stats")
def api_security_stats():
    return jsonify(ids.get_stats())

@app.route("/api/security/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()
    result = ids.analyze_input(data)
    return jsonify(result)

@app.route("/api/security/alerts/<alert_id>/resolve", methods=["POST"])
def api_resolve_alert(alert_id):
    result = ids.resolve_alert(alert_id)
    return jsonify(result)

# ══════════════════════════════════════════════════════
#  API — AUTOMATISATION
# ══════════════════════════════════════════════════════

@app.route("/api/automation/users")
def api_users():
    return jsonify(automation.get_users())

@app.route("/api/automation/users", methods=["POST"])
def api_create_user():
    data   = request.get_json()
    result = automation.create_user(data)
    return jsonify(result)

@app.route("/api/automation/users/<username>/reset", methods=["POST"])
def api_reset_password(username):
    result = automation.reset_password(username)
    return jsonify(result)

@app.route("/api/automation/users/<username>/disable", methods=["POST"])
def api_disable_user(username):
    result = automation.disable_user(username)
    return jsonify(result)

@app.route("/api/automation/tasks")
def api_tasks():
    return jsonify(automation.get_tasks())

@app.route("/api/automation/tasks", methods=["POST"])
def api_run_task():
    data   = request.get_json()
    result = automation.run_task(data.get("task_id"), data.get("params", {}))
    return jsonify(result)

@app.route("/api/automation/report", methods=["POST"])
def api_generate_report():
    result = automation.generate_report()
    return jsonify(result)

# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    start_background()
    print("\n  🚀 NetOps Pro démarré sur http://127.0.0.1:5000\n")
    app.run(debug=False, host="0.0.0.0", port=5000)
