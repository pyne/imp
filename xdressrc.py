sourcedir = "../moab/itaps/imesh"
package = "imp"

includes = ["/home/scopatz/.local/include", "/home/scopatz/moab/src"]

undefines = ["__cplusplus"]

functions = [
    ('iMesh_dtor', 'iMesh_MOAB', 'iMesh'),
    ('iMesh_getRootSet', 'iMesh_MOAB', 'iMesh'),
    ]

classes = [
    ('iMesh_Instance', 'iMesh', 'iMesh'),
    ('iMesh_Instance_Private', 'iMesh', 'iMesh'),
    ('iMeshArrayManager', 'iMesh_MOAB', 'iMesh'),
    ]
