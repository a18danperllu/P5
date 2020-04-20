# #
# MySQL 8 Shell
# #
# Este ejemplo muestra un script X DevAPI simple para trabajar con datos relacionales
# #
desde  mysqlsh  import  mysqlx  # necesario en caso de que ejecute el código fuera del shell
Sentencia # SQL CREATE TABLE
CREATE_TBL  =  "" "
CREAR TABLA `supermercat`.`caixer` (
  `ID_CAIXER 'INT no nulo auto_increment,
  `DNI_CLIENT` VARCHAR (9) NOT NULL,
  `NOM_CAIXER` VARCHAR (15) DEFAULT NULL,
  `COGNOM_CAIXER` VARCHAR (15) NO NULL DEFAULT CURRENT_TIMESTAMP EN ACTUALIZAR CURRENT_TIMESTAMP,
  `NUM_TELF` INT DEFAULT NULL,
  CLAVE PRIMARIA `ID_CAIXER` (` id`)
) MOTOR = InnoDB CARACTER POR DEFECTO = latin1
"" "
# lista de columnas, estructura de datos del usuario
COLUMNS  = [ 'Id_Caixer' , 'DNI_Client' , 'Nom_Caixer' , 'Cognom_Caixer' , 'Num_Telef' ]
user_info  = {
  'host' : 'localhost' ,
  'puerto' : 33060 ,
  'user' : 'root' ,
  'contraseña' : 'root' ,
}
print ( "Listado 4-6 Ejemplo: demostración de Python X DevAPI con datos relacionales" )
# Obtener una sesión (conexión)
my_session  =  mysqlx . get_session ( información_usuario )
# Esquema de caída preventiva
my_session . drop_schema ( 'supermercat' )
# Crear la base de datos (esquema)
my_db  =  my_session . create_schema ( 'supermercat' )
# Ejecute la instrucción SQL para crear la tabla
sql_res  =  my_session . sql ( CREATE_TBL ). ejecutar ()
# Obtener el objeto de la tabla
my_tbl  =  my_db . get_table ( 'caixer' )
# Insertar algunas filas (datos)
my_tbl . insertar ( COLUMNAS ). valores ( 123 , '12366677Z' , 'Roser' , 'Avellan' , 934524565 ). ejecutar ()
my_tbl . insertar ( COLUMNAS ). valores ( 124 , '14366677W' , 'Fran' , 'Catala' , 932457825 ). ejecutar ()
my_tbl . insertar ( COLUMNAS ). valores ( 125 , '11363547X' , 'Pau' , 'Barber' , 938742595 ). ejecutar ()
my_tbl . insertar ( COLUMNAS ). valores ( 126 , '12366677E' , 'Lluc' , 'Avellan' , 932541525 ). ejecutar ()
# Ejecute una selección simple (SELECCIONAR ∗ DESDE)
print ( " \ n Mostrando resultados después de insertar todas las filas" )
my_res  =  my_tbl . seleccione ( COLUMNAS ). ejecutar ()
# Mostrar los resultados. Demuestra cómo trabajar con resultados.
# Imprima los nombres de columna seguidos de las filas
COLUMN_NAMES  =  my_res . get_column_names ()
column_count  =  my_res . get_column_count ()
para  i  en  rango ( 0 , column_count ):
    si  yo  <  column_count  -  1 :
        imprima  "{0}," . formato ( column_names [ i ]),
    más :
        imprime  "{0}" . formato ( column_names [ i ]),
impresión
para  fila  en  my_res . fetch_all ():
    para  i  en  rango ( 0 , column_count ):
        si  yo  <  column_count  -  1 :
            imprima  "{0}," . formato ( fila [ i ]),
        más :
            imprime  "{0}" . formato ( fila [ i ]),
    impresión
# Actualizar una fila
my_tbl . actualización (). conjunto ( 'NUM_TELF' , 935876433 ). donde ( 'ID_CAIXER LIKE 124' ). ejecutar ()
print ( " \ n Mostrando resultados después de actualizar la fila con ID_CAIXER LIKE 124." )
# Ejecute una selección simple (SELECCIONAR ∗ DESDE)
my_res  =  my_tbl . seleccione ( COLUMNAS ). ejecutar ()
# Mostrar los resultados
para  fila  en  my_res . fetch_all ():
     fila de impresión
# Eliminar algunas filas
my_tbl . eliminar (). donde ( 'NUM_TELF> 30' ). ejecutar ()
# Ejecute una selección simple (SELECCIONAR ∗ DESDE)
print ( " \ n Mostrando resultados después de eliminar filas con NUM_TELF> 30." )
my_res  =  my_tbl . seleccione ( COLUMNAS ). ejecutar ()
# Mostrar los resultados
para  fila  en  my_res . fetch_all ():
     fila de impresión
# Eliminar la base de datos (esquema)
my_session . drop_schema ( 'supermercat' )
