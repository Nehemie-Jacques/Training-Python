#!/bin/bash

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔧 Création de l’environnement virtuel avec Python 3.13...${NC}"

# Vérifie que Python 3.13 est disponible
if ! command -v python3.13 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python 3.13 n'est pas installé ou n'est pas dans le PATH.${NC}"
    exit 1
fi

# Crée le venv
python3.13 -m venv .venv

# Active le venv
source .venv/bin/activate

echo -e "${GREEN}✅ Environnement virtuel activé : $(which python)${NC}"

# Si requirements.txt existe, on installe les paquets
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}📦 Installation des dépendances depuis requirements.txt...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo -e "${YELLOW}ℹ️  Aucun fichier requirements.txt trouvé. Rien à installer.${NC}"
fi

echo -e "${GREEN}🚀 Prêt à coder dans l’environnement virtuel !${NC}"
echo -e "${YELLOW}ℹ️ Pour l’activer à nouveau plus tard : source .venv/bin/activate${NC}"
