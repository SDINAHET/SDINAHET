from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

# 1. Config Jinja : les templates sont dans le dossier "templates"
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"])
)

# 2. Simuler Flask's url_for pour les fichiers statiques
def url_for(endpoint, **values):
    """
    Remplace url_for('static', filename='...') par 'static/...'
    Les fichiers statiques doivent être dans docs/static/
    """
    if endpoint == "static":
        filename = values.get("filename", "")
        return f"static/{filename}"
    # Si jamais autre chose est appelée
    return "#"

# On injecte url_for dans l'environnement Jinja
env.globals["url_for"] = url_for

# 3. Pages à générer : (template source, nom du fichier de sortie, contexte)
pages = [
    ("index.html", "index.html", {"title": "HBnB - Home"}),
    ("login.html", "login.html", {"title": "Login - HBnB"}),
    ("place.html", "place.html", {"title": "Place details - HBnB"}),
]

# 4. Dossier de sortie : "docs" (utilisé par GitHub Pages)
output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

for template_name, output_name, context in pages:
    template = env.get_template(template_name)
    rendered_html = template.render(**context)

    output_path = os.path.join(output_dir, output_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"Généré : {output_path}")

print("Terminé !")
