# xmlrpc-c Builds

Ce dépôt contient des scripts pour compiler automatiquement la bibliothèque xmlrpc-c et créer des packages Debian (.deb).

## Particularités

- Les packages créés installent xmlrpc-c dans `/usr/local/`
- Ces packages sont destinés à être utilisés sur des systèmes Ubuntu/Debian
- Les builds passent par GitHub Actions, déclenchés **uniquement** en **`workflow_dispatch`** (onglet **Actions** ; aucun run au **push**)
- Les sources sont récupérées par **`svn export`** sur le dépôt SourceForge : sous-arbre  
  [`release_number/<version>`](https://svn.code.sf.net/p/xmlrpc-c/code/release_number/)  
  (révisions SVN optionnellement épinglées dans `matrix.py`, ex. [r3332 pour 1.66.01](https://sourceforge.net/p/xmlrpc-c/code/3332/tree/release_number/)).

## GitHub Actions

Le fichier `.github/workflows/build.yaml` ne définit que **`workflow_dispatch`** : lancer le build depuis **Actions** en choisissant **`all`** ou une version listée.

## Utilisation locale

Pour construire manuellement un package xmlrpc-c :

```bash
./build.sh <VERSION>
```

Exemple :
```bash
./build.sh 1.54.06
```

## Packages disponibles

Les packages sont disponibles dans les GitHub Releases de ce dépôt. Chaque release comprend :
- Un fichier `.deb` qui peut être installé avec `dpkg -i`
- Un fichier `.json` contenant les métadonnées du package

## Structure du package

Une fois installé, le package placera :
- Les fichiers d'en-tête (headers) dans `/usr/local/include`
- Les bibliothèques dans `/usr/local/lib`
- Les binaires dans `/usr/local/bin`

## Dépendances

Pour compiler xmlrpc-c, vous aurez besoin de :
- build-essential
- autoconf
- automake
- libtool
- libcurl4-openssl-dev
- libssl-dev
- pkg-config

## Licence

Ce dépôt est sous licence selon les termes de la licence présente dans le fichier LICENSE.

xmlrpc-c est distribué sous les termes de la [BSD License](https://github.com/mirror/xmlrpc-c/blob/master/doc/COPYING). 
