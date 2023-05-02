[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Tournois-echecs : OC - Project 4
---
### Pré-requis
Avoir un OS **Linux** avec **Python 3.11** installé  
<br/>

### Installation
Executer ces commandes dans un terminal **bash**
pour installer installer le projet
```bash
git clone git@github.com:Jeremie-Silva/tournois-echecs.git
cd tournois-echecs
```
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
export PYTHONPATH=$PWD
pip install -r requirements.txt
```  
<br/>

### Codingstyle
Executer ces commandes dans un terminal **bash**
pour générer un nouveau rapport de codingstyle avec **Flake8**
```bash
flake8 --format=html --htmldir=flake8_report app
google-chrome flake8_report/players.html
```
Remplacer `google-chrome` par le nom de votre navigateur  
<br/>

### Tests
Executer ces commandes dans un terminal **bash**
pour générer un nouveau rapport de couverture avec **pytest**
```bash
pytest --cov=app & coverage html
google-chrome htmlcov/players.html
```
Remplacer `google-chrome` par le nom de votre navigateur  
<br/>

### Lancer l'application
```bash
python3 app/main.py
```
Quitter l'environnement virtuel :
```bash
deactivate
```  
<br/>