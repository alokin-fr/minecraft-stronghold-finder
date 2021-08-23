# minecraft-stronghold-finder

Cet algorthme permet aux joueurs de Minecraft de déterminer les coordonnées X et Z d'un fort en utilisant uniquement 2 yeux de l'Ender. Une fois lancé, un oeil de l'Ender se déplace de quelques blocs dans la direction du fort le plus proche. En utilisant 2 yeux de l'Ender et en prolongeant mathématiquement leurs trajectoires respectives, on peut alors déterminer leur intersection correspondant à la position du fort.

Les angles latéraux et coordonnées peuvent être lus sur la gauche de l'**écran de débogage**, en appuyant sur **F3**. Les coordonnées, que l'on pourra arrondir à l'unité, s'affichent sur la ligne `XYZ`, tandis que l'angle latéral que l'on écrira avec une décimale après la virgule, est le 1er nombre entre parenthèses sur la ligne `Facing`.

Comment procéder ?
1. Choisir une 1ère position et en noter les coordonnées `X1` et `Z1`. Sans bouger, lancer un 1er oeil de l'Ender et le viser en son centre avec le curseur central, puis noter l'angle latéral `a1`.
2. Se déplacer de quelques centaines de blocs, si possible perpendiculairement à la trajectoire de l'oeil de l'Ender précédemment lancé.
3. Choisir une 2nde position et en noter les coordonnées `X2` et `Z2`. Sans bouger, lancer un 2nd oeil de l'Ender et le viser en son centre avec le curseur central, puis noter l'angle latéral `a2`.
4. Entrer les 6 valeurs `X1`, `Z1`, `a1`, `X2`, `Z2` et `a2` dans l'algorithme.
5. Se rendre et creuser aux coordonnées `X` et `Z` indiquées par l'algorithme.

⚠️En fonction de la précision des mesures, il est possible que le fort soit en réalité à quelques blocs de la position indiquée. D'autre part, l'algorithme retournera une erreur si les trajectoires des 2 yeux de l'Ender ne s'intersectent pas, ou bien si l'intersection ne se situe pas dans une zone de génération de forts. Dans ce cas de figure, recommencer la procédure en veillant à déterminer les valeurs avec précision. Prendre en compte qu'il est effectivement possible que les deux yeux de l'Ender montrent chacun un fort différent.
