# xmlrpc-c Builds

Ce dépôt contient des scripts pour compiler automatiquement la bibliothèque xmlrpc-c et créer des packages Debian (.deb).

## Particularités

- Les packages créés installent xmlrpc-c dans `/usr/local/`
- Ces packages sont destinés à être utilisés sur des systèmes Ubuntu/Debian
- Les builds sont automatisés via GitHub Actions

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
