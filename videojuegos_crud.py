import mysql.connector
from mysql.connector import Error

# Configuración de la conexión a la base de datos
def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='videogames_db',
            user='root',  
            password='password'  
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print("Error al conectar a MySQL", e)
        return None

# Función para agregar un nuevo juego
def create_game(connection):
    cursor = connection.cursor()
    name = input("Nombre del juego: ")
    release_date = input("Fecha de lanzamiento (YYYY-MM-DD): ")
    genre = input("Género: ")
    query = "INSERT INTO games (name, release_date, genre) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, release_date, genre))
    connection.commit()
    print("Juego agregado exitosamente")

# Función para mostrar todos los juegos
def read_games(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    for game in games:
        print(f"ID: {game[0]}, Nombre: {game[1]}, Fecha de lanzamiento: {game[2]}, Género: {game[3]}")

# Función para actualizar
def update_game(connection):
    cursor = connection.cursor()
    game_id = input("ID del juego a actualizar: ")
    new_name = input("Nuevo nombre del juego: ")
    new_release_date = input("Nueva fecha de lanzamiento (YYYY-MM-DD): ")
    new_genre = input("Nuevo género: ")
    query = "UPDATE games SET name = %s, release_date = %s, genre = %s WHERE id = %s"
    cursor.execute(query, (new_name, new_release_date, new_genre, game_id))
    connection.commit()
    print("Juego actualizado exitosamente")

# Función para eliminar un juego
def delete_game(connection):
    cursor = connection.cursor()
    game_id = input("ID del juego a eliminar: ")
    query = "DELETE FROM games WHERE id = %s"
    cursor.execute(query, (game_id,))
    connection.commit()
    print("Juego eliminado exitosamente")

# Función principal que ejecuta las operaciones CRUD
def main():
    connection = connect()
    if connection is None:
        return
    while True:
        print("\n--- CRUD Videojuegos ---")
        print("1. Crear juego")
        print("2. Ver juegos")
        print("3. Actualizar juego")
        print("4. Eliminar juego")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_game(connection)
        elif choice == '2':
            read_games(connection)
        elif choice == '3':
            update_game(connection)
        elif choice == '4':
            delete_game(connection)
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
