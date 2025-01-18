from pymongo import MongoClient
from pymongo.database import Database, Collection
import os

USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "supersecret")
HOST = os.getenv("MONGO_HOST", "localhost")
PORT = os.getenv("MONGO_PORT", "27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "test")

class DataAlreadyExistsError(Exception):
    def __init__(self, message="El dato ya existe."):
        self.message = message
        super().__init__(self.message)

class ConnectionError(Exception):
    def __init__(self, message="Error al conectar a la base de datos."):
        self.message = message
        super().__init__(self.message)

class ClientCreationError(Exception):
    def __init__(self, message="Error al crear el cliente de la base de datos."):
        self.message = message
        super().__init__(self.message)

class ConnectionCloseError(Exception):
    def __init__(self, message="Error al cerrar el cliente de la base de datos."):
        self.message = message
        super().__init__(self.message)

class ElementNotEspcifiedError(Exception):
    def __init__(self, message="No se ha especificado el elemento."):
        self.message = message
        super().__init__(self.message)

class MyDataBase():
    '''
    Clase para manejar la conexión a la base de datos.
    Metodos:
    - dropCollection: Elimina una colección.
    - dropDatabase: Elimina la base de datos.
    - close: Cierra la conexión a la base de datos.
    '''
    
    # Atributos
    __client: MongoClient
    __db: Database
    __db_name: str
    
    @property
    def db_name(self):
        return self.__db_name
    
    @property
    def db(self):
        return self.__db
    
    # Constructor
    def __init__(self, db_name:str = DB_NAME):
        self.__client = None
        self.__db = None
        self.__db_name = db_name
        try:
            self.__client = MongoClient(f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}")
            self.__db = self.__client[db_name]
        except Exception as e:
            raise ConnectionError(f"Error al conectar a la base de datos: {e}")
        
    # Metodos
    # Cerrar la conexión a la base de datos
    def close(self):
        try:
            self.__client.close()
        except Exception as e:
            raise ConnectionCloseError(f"Error al cerrar el cliente de la base de datos: {e}")
        
    # Eliminar una colección
    def dropCollection(self, collection_name:str):
        if not collection_name:
            raise ElementNotEspcifiedError("No se ha especificado la colección.")
        try:
            self.__db.drop_collection(collection_name)
        except Exception as e:
            raise ConnectionError(f"Error al eliminar la colección: {e}")
        
    # Eliminar la base de datos
    def dropDatabase(self):
        try:
            self.__client.drop_database(self.__db_name)
        except Exception as e:
            raise ConnectionError(f"Error al eliminar la base de datos: {e}")

