import pymysql.connections

#seteo variables principales de la conexion

def conectar_db():
    conexion = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        port = 3306,
        database = 'cac_personas'
    )
    return conexion

def nuevos_registros(nombre,edad):
    conexion = conectar_db()
    try:
        cursor = conexion.cursor()
        sql = f"INSERT INTO personas (nombre,edad) VALUES ('{nombre}',{edad})"
        cursor.execute(sql) # Ejecuta la consulta.
        conexion.commit() # Guarda los cambos en la db
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print(f"Error al intentar guardar el registro, error desconocido {type(e)}")        
    finally:
        conexion.close()


def borrar_registros(id):
    conexion = conectar_db()    
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas     
        sql = f"DELETE FROM personas WHERE id={id}"
        cursor.execute(sql) # Ejecuta la consulta.
        conexion.commit() # Guarda los cambos en la db
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print(f"Error al intentar guardar el registro, error desconocido {type(e)}")        
    finally:
        conexion.close()


def actualizar_registros(id,nombre,nuevo_nombre):
    conexion = conectar_db()    
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas     
        sql = f"UPDATE personas SET nombre='{nuevo_nombre}' where id='{id}' and nombre='{nombre}' "
        cursor.execute(sql) # Ejecuta la consulta.
        conexion.commit() # Guarda los cambos en la db
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print(f"Error al intentar guardar el registro, error desconocido {type(e)}")        
    finally:
        conexion.close()

def leer_registros():
    conexion = conectar_db()
    try:
        cursor = conexion.cursor() # cursor para ejecutar las consultas     
        sql = f"SELECT * FROM personas "
        cursor.execute(sql) # Ejecuta la consulta.
        listado_personas = cursor.fetchall() #Metodo de cursor que me trae todo.
        return listado_personas
    except ConnectionError:
        print("Error de conexion")
    except Exception as e:
        print(f"Error al intentar guardar el registro, error desconocido {type(e)}")        
    finally:
        conexion.close()    


#### PROGRAMA PRINCIPAL


#nuevos_registros("Alemitosis",27)
# borrar_registros(3)
# actualizar_registros(5,"Ale","Jorgito")

personas = leer_registros()
for persona in personas:
    print(persona)