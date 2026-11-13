# TP DataOps 1

**TP CI/CD – GitHub Actions pour Airflow**

Anthony Blondel - Master Data Engineering & AI

## Mise en place

- cloner le dépôt GitHub
- créer un environnement virtuel Python
- activer l'environnement virtuel
- installer les dépendances avec `pip install -e ".[dev]"`

##  Génération du `requirements-dev.txt`

```bash
pip-compile --config pyproject.toml --extra dev -o requirements-dev.txt
```
