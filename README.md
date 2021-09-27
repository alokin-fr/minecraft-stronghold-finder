# minecraft-stronghold-finder

This algorithm allows Minecraft players to determine the X and Z coordinates of a stronghold using only 2 eyes of Ender. Once launched, an eye of Ender moves a few blocks in the direction of the nearest stronghold. By using 2 Ender eyes and mathematically extending their respective trajectories, we can then determine their intersection, which corresponds to the location of the stronghold.

The lateral angles and coordinates can be read on the left side of the **debug screen**, by pressing **F3**. The coordinates, which can be rounded to the nearest whole number, are displayed on the `XYZ` line. The lateral angle, which can be rounded to one decimal place, is the first number in brackets on the `Facing` line.

How to proceed?
1. Choose a 1st position and take its coordinates `X1` and `Z1`. Without moving, throw a 1st eye of Ender and aim it at its center with the central cursor, then take the lateral angle `a1`.
2. Move a few hundred blocks, if possible perpendicularly to the trajectory of the previously thrown eye of Ender.
3. Choose a 2nd position and take its coordinates `X2` and `Z2`. Without moving, throw a 2nd eye of Ender and aim it at its center with the central cursor, then note the lateral angle `a2`.
4. Enter the 6 values `X1`, `Z1`, `a1`, `X2`, `Z2` and `a2` in the algorithm.
5. Go to and dig at the `X` and `Z` coordinates specified by the algorithm.

⚠️Depending on the accuracy of the measurements, it is possible that the stronghold is actually a few blocks away from the indicated position. In addition, the algorithm will return an error if the trajectories of the 2 eyes of Ender do not intersect, or if the intersection is not in a stronghold generation zone. In this case, repeat the procedure, making sure to determine the values accurately. Take into account that it is indeed possible that the two eyes of Ender each show a different stronghold.
