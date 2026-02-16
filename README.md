# Atelier — Programmation augmentée

Ce dépôt est un **mini-projet pédagogique** prêt à être ouvert dans **GitHub Codespaces**.
Il contient 4 petites activités pour découvrir la programmation assistée par IA (Copilot / ChatGPT / etc.)
tout en apprenant les bons réflexes : **tests**, **lecture critique**, **vérification**, **sécurité**.

## Démarrage rapide (Codespaces)

1. Ouvrez le dépôt dans GitHub → **Code** → **Create codespace on main**
2. À l’ouverture, le conteneur installe automatiquement les dépendances.
3. Lancez les tests :

```bash
pytest -q
```

## Démarrage rapide (local)

Pré-requis : Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
pytest -q
```

## Activités

### Activité 1 — “Démo live” (enseignant)
Dossier : `activities/1_demo_live/`

Un script très simple (conversion Celsius/Fahrenheit + tests).
But : montrer la boucle *demande → suggestion IA → exécution → vérification*.

### Activité 2 — Bug + tests (binômes)
Dossier : `activities/2_bug_and_tests/`

La fonction `is_prime` contient volontairement un bug.
Objectif : faire passer les tests (et expliquer la correction).

### Activité 3 — Esprit critique : hallucination d’API
Dossier : `activities/3_api_hallucination/`

L’IA propose un paramètre qui n’existe pas (`descending=True`).
Objectif : exécuter, comprendre l’erreur, corriger (`reverse=True`).

### Activité 4 — Prototype créatif (mini-projet)
Dossier : `activities/4_creative_prototype/`

Un mini jeu “Devine le nombre” à compléter + idées d’améliorations.

## Bonnes pratiques (à rappeler aux élèves)

- Ne collez **jamais** de secrets (mots de passe, clés API, tokens).
- Une sortie d’IA = **proposition**, pas une preuve.
- **Toujours** exécuter / tester / relire.
- Vérifier l’existence des APIs et des dépendances (doc officielle).
- Préférer des exercices publics / données fictives pendant l’atelier.

## Licence
MIT (voir `LICENSE`).
