# discordBots

## Petit bot discord qui joue à de petits jeu ##
- Devine un nombre
- Pierre - Feuille - Ciseaux (TODO)

## Install ##

- executer le script INSTALL
> sh INSTALL.txt
- ou bien les commandes ci-dessous (les lignes sans #)
> \# télécharge le code  
> git clone https://github.com/7clem/discordBots.git  
\# entre dans le dossier          
> cd discordBots  
> \# crée un environnement virtuel    
> python -m venv .env      
> \# active l'environnement  
> source .env/bin/activate      
>\# installe tous les paquets requis.  
> python3 -m pip install -U -r requirements.txt  

## Executer ##
- créer un compte discord
- Créer une application (https://discord.com/developers/applications)
- créer un bot
- obtenir le token du bot et placer la valeur dans
un fichier texte nommé discordBotToken.txt
- executer le bot :
  >python3 devine.py discordBotToken.txt
- inviter le bot dans un salon textuel Discord
