Title: HBS-Research
Date: 2015-11-15
Category: Expérience
Lang: fr
sortorder: 05
status: hidden

**Rôle :** géomaticien développeur, administration système et base de données. 

*En poste de septembre 2006 à novembre 2009*.

Le développement de l'application a été réalisé au sein d'un framework PHP 
appelé Symfony. La pile cartographique est constituée de PostgreSQL/PostGIS, 
MapServer, TileCache et OpenLayers. Chacune de ces applications a été optimisée 
pour obtenir une application rapide et efficace.

Logo d'OpenLayers L'interface graphique, côté client, a été développée sous 
OpenLayers puis enrichie petit à petit en fonction des nouveautés proposées par 
les différentes versions publiées : cluster, optimisation, WMC, pop-up, barre 
d'échelle, etc.

Le serveur cartographique est constitué de postGIS pour le stockage des données 
(en partie) et de MapServer pour le rendu de carte. Le serveur de base de 
données a fait l'objet d'une optimisation spécifique pour cette application par
mes soins afin d'utiliser au mieux la mémoire disponible sur le serveur.

La partie serveur cartographique proprement dite a fait l'objet d'une conception 
en amont afin de structurer et optimiser les fichiers de configuration (mapfile). 
L'optimisation a portée également sur l'utilisation d'un système de cache écrit 
en python et configuré en mod d'Apache, TileCache, accélérant ainsi fortement 
la diffusion des tuiles vers le client.

Linux La compilation, l'installation et la création de paquet permet de mettre 
à jour le serveur avec les dernières versions des logiciels, évitant ainsi les 
failles de sécurité et la possibilité de suivre au plus près les développements
des projets des applications cartographiques (optimisation des performances, 
nouvelles fonctionnalités, amélioration de la qualité du rendu, etc.)

Compétences :

* OpenLayers ;
* TileCache ;
* MapServer (installation, configuration, gestion) ;
* PostGIS (installation, configuration, gestion) ;
* PostgreSQL (installation, configuration, gestion, optimisation)
* Script Bash, Python ;
* Installation et configuration (Debian et dérivé, Mandriva, RedHat et dérivé) ;
* Compilation et création de paquet.

Liens :

* La place de l'immobilier pro
* OpenLayers
* MapServer
* PostGIS
* TileCache
* Symfony

