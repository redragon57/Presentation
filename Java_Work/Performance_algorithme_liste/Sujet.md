# P4a

## Présentation du sujet

Ce module vous demandera d'étudier des problèmes de performances des opérations élémentaires sur des structures de données dont les éléments sont des entiers.

### Première étape : interface `IntegerContainer`

Il faudra créer une interface comportant les méthodes suivantes :
- `Integer minimum()` : renvoie le plus petit entier de la structure
- `void add(Integer x)` : ajoute l'élément `x` à la structure
- `void remove(Integer x)` : supprime un élément

### Deuxième étape : classes enveloppantes

Créer des classes enveloppantes (wrapper) implémentant l'interface `IntegerContainer` pour les classes suivantes, en implémentant soi-même les méthodes manquantes si nécessaire :

- `LinkedList<Integer>` (on appellera la classe enveloppante `ICLinkedList`)
- `ArrayDeque<Integer>` (on appellera la classe enveloppante `ICArrayDeque`)
- `Stack<Integer>`  (on appellera la classe enveloppante `ICStack`)

### Troisième étape : implémentations personnelles

Implémenter soi-même, en partant d'un tableau, une structure de type suivant :
- Arbre Binaire de Recherche (qu'on appellera `ICBinaryTreeSearch`)
- Liste Chaînée (qu'on appellera `ICOwnLinkedList`)
implémentant l'interface `IntegerContainer`.


### Quatrième étape : mesures et créations de fichiers de données pour

Faire des mesures de temps d'exécution d'opérations élémentaires (on pourra utiliser `System.currentTimeMillis()` par exemple ou d'autres méthodes qui vous semblent appropriées).

Produire des fichiers csv de vos mesures.

On commencera par un cas particulier (par exemple `n` ajouts d'entiers dans une liste chaînée).


### Cinquième étape : représentation des données

Représenter graphiquement vos données à l'aide de R.


### Sixième étape : automatisation des processus

Vous avez tout pour automatiser le processus avec un script et tester un maximum de cas de figures.

Argumentez sur la complexité algorithmique que vous observez.

### Septième étape : argumentation

Vous êtes engagé par une communauté religieuse attendant le retour du Grand Lapin Primordial sur Terre. Les membres traquent les signes de ce retour à travers les émissions de rayons-fanes cosmiques (cherchez pas, c'est technique).

Des appareils de mesures (assez chers, il faut le reconnaître) ont été spécialement développés dans ce but et beaucoup de membres de cette communauté (3 millions au doigt mouillé), ont acquis un de ces appareils pour effectuer les mesures depuis chez eux. À intervalle régulier, toutes les mesures sont envoyées à un serveur central (sur une architecture de processeurs en trits du Frintel 2000, pour les connaisseurs).

Avec ces données reçues à intervalle régulier, réalisez les methodes suivantes :
- `void purify()` : vous devez garder les 100 000 mesures les plus hautes de la série précédente (ça sent la fraude scientifique mais vous êtes bien payé);
- `void eat(int x)` : agréger les données reçues les nouvelles données reçues;
- `void carrot()` : vous devez supprimer les 100 000 mesures les plus faibles (je vous rappelle que vous êtes toujours bien payé).

Trouvez la structure de données qui vous semble la plus judicieuse pour effectuer ces opérations et argumentez à l'aide d'un rapport illustré. Dans le doute (on ne sait jamais ce qui se passe dans la tête d'une personne habillée de pied en cap d'un pyjama-lapin), vous prenez la chose au sérieux pour ne pas décevoir le Héraut Cuniculaire (qui a beaucoup d'argent surtout mais je crois que je l'ai déjà dit), vous mettez tout en oeuvre de ce que vous avez appris en P4a pour faire valider votre choix.



## Critères d'évaluation

Le projet sera évalué via le dépôt auquel il faut nous donner accès.

Il sera évalué sur les critères suivants :

- Qualité du code
- Processus de production des mesures
- Rédaction et analyse
- Qualité des représentations graphiques
- **Argumentation du choix de votre structure**
