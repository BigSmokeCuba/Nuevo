from os import getenv


# DATOS DEL MOODLE

USERID = getenv('USERID')

if USERID is None:

    raise Exception("Por favor configura la ID del Moodle") 

