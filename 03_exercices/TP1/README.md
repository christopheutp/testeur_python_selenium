## Organisation des pages

Dans ce TP1, les différentes pages ont été regroupées dans le dossier `pages`.

Cette organisation correspond à une correction de la structure initiale, dans laquelle les fichiers avaient été placés à la racine du projet afin d’éviter des problèmes d’import.

Les imports internes utilisent désormais des chemins relatifs, avec l’ajout d’un point devant le module concerné, ce qui permet d’assurer le bon fonctionnement des imports entre classes d’un même dossier.

Exemple :

```python
from .base_page import BasePage
````

