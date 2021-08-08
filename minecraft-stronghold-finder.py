from math import sin,cos

#Throw your 1st Ender Eye from a 1st location.
x1=int(input("X coordinate of the 1st location (integer):"))
z1=int(input("Z coordinate of the 1st location (integer):"))
a1=float(input("Lateral angle displayed by pointing the 1st Ender Eye (1 decimal digit):"))

#Walk a few hundred blocks perpendicular to the Ender Eye direction, then throw your 2nd Ender Eye from a 2nd location.
x2=int(input("X coordinate of the 2nd location (integer):"))
z2=int(input("Z coordinate of the 2nd location (integer):"))
a2=float(input("Lateral angle displayed by pointing the 2nd Ender Eye (1 decimal digit):"))

a1=3.141592653589793*(0.5+a1/180)   #Convert angles so that they suit the cartesian system (from deg to rad).
a2=3.141592653589793*(0.5+a2/180)

def compute():
    try:
        x=(cos(a2)*(cos(a1)*z1-sin(a1)*x1)-cos(a1)*(cos(a2)*z2-sin(a2)*x2))/sin(a2-a1)  #X coordinate of the stronghold (theorical).
        z=(sin(a2)*(sin(a1)*x1-cos(a1)*z1)-sin(a1)*(sin(a2)*x2-cos(a2)*z2))/sin(a1-a2)  #Z coordinate of the stronghold (theorical).
    except ZeroDivisionError:
        return print("ERROR: The two angles are equal.")    #Check if the angles are different.

    sol=[x,z]
    coor=[x1,z1,x2,z2]
    trig=[cos(a1),sin(a1),cos(a2),sin(a2)]
    for i in range(4):  #Check if the 2 rays representing each of the directions of the Ender Eyes intersect.
        k=i%2
        if trig[i]>=0:
            if sol[k]<=coor[i]:
                return print("ERROR: The trajectories of the Ender Eyes do not converge. Either the Ender Eyes indicate the location of two different strongholds, or the input values are incorrect.")
        else:
            if sol[k]>coor[i]:
                return print("ERROR: The trajectories of the Ender Eyes do not converge. Either the Ender Eyes indicate the location of two different strongholds, or the input values are incorrect.")

    inf=[1408,4480,7552,10624,13696,16768,19840,22912]  #Check if the theorical stronghold is located in a stronghold generation area.
    sup=[2688,5760,8832,11904,14976,18048,21120,24192]
    dist=(x**2+z**2)**0.5
    for i in range(8):
        if dist>=inf[i] and dist<=sup[i]:
            break
        elif i==7:
            return print("ERROR: Computed coordinates do not represent a location in a stronghold generation area. The input values are either incorrect or inaccurate.")

    return print(f"STRONGHOLD LOCATION: (can be inacurate by a few blocks)\nX={round(x)}\nZ={round(z)}")

compute()
