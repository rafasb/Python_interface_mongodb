#Clase para la gestión de colecciones

from pymongo.database import Collection
from database import MyDataBase, ConnectionError, ElementNotEspcifiedError

class InsertionError(Exception):
  def __init__(self, message="Error al insertar el documento."):
    self.message = message
    super().__init__(self.message)

class MyCollection(MyDataBase):
  # Atributos
  __collection: Collection
  __collection_name: str
  
  @property
  def collection_name(self):
    return self.__collection_name
  
  # Constructor
  def __init__(self, collection_name:str, db_name:str = MyDataBase.db_name):
    if not collection_name:
      raise ElementNotEspcifiedError("No se ha especificado la colección.")
    
    self.__collection = None
    self.__collection_name = collection_name
    
    try:
      super().__init__(db_name)
      self.__collection = self.db[collection_name]
    except Exception as e:
      raise ConnectionError(f"Error al conectar a la colección: {e}")
    
  # Metodos
  def insert(self, document:dict):
    '''
    Función para insertar uno o varios documentos en la colección.
    - document: dict, Documento o documentos a insertar.
    '''
    if document in [None, {}]:
      raise ElementNotEspcifiedError("No se ha especificado el documento.")
    
    try:
      if isinstance(document, dict):
        self.__collection.insert_one(document)
      elif isinstance(document, list):
        self.__collection.insert_many(document)
    except Exception as e:
      raise InsertionError(f"Error al insertar el documento: {e}")
    
  def find_one(self, query:dict, clean_id:bool = True):
    '''
    Función para buscar documentos en la colección.
    - query: dict, Consulta a realizar.
    Retorna el documento.
    '''
    if query in [None, {}]:
      raise ElementNotEspcifiedError("No se ha especificado la consulta.")
    
    try:
      doc = self.__collection.find_one(query)
      if clean_id:
        doc.pop("_id", None)
      return doc
    except Exception as e:
      raise ConnectionError(f"Error al buscar el documento de la colección {self.__collection_name}: {e}") 
  
  def find_all(self, query:dict, clean_id:bool = True):
    '''
    Función para buscar todos los documentos que cumplan con la consulta en la colección.
    - query: dict, Consulta a realizar.
    Retorna un array con los documentos.
    '''
    
    documents = []
    
    if query in [None, {}]:
      raise ElementNotEspcifiedError("No se ha especificado la consulta.")
    
    try:
      for doc in self.__collection.find(query):
        if clean_id:
          doc.pop("_id", None)
        documents.append(doc)
      return documents
    except Exception as e:
      raise ConnectionError(f"Error al buscar los documentos de la colección {self.__collection_name}: {e}")
    
  def update(self, query:dict, new_values:dict):
    '''
    Función para actualizar o añade un documento de la colección.
    - query: dict, Consulta para buscar el documento a actualizar.
    - new_values: dict, Nuevos valores del documento.
    Retorna el número de documentos actualizados.
    '''
    if query in [None, {}] or new_values in [None, {}]:
      raise ElementNotEspcifiedError("No se han especificado la consulta o los nuevos valores.")
    
    try:
      result = self.__collection.update_one(query, {"$set": new_values}, upsert=True).matched_count
      return result
    except Exception as e:
      raise ConnectionError(f"Error al actualizar el documento de la colección {self.__collection_name}: {e}")
    
  def delete(self, query:dict):
    '''
    Función para eliminar un documento de la colección.
    - query: dict, Consulta para buscar el documento a eliminar.
    Retorna el número de documentos eliminados.
    '''
    if query in [None, {}]:
      raise ElementNotEspcifiedError("No se ha especificado la consulta.")
    
    try:
      result = self.__collection.delete_one(query).deleted_count
      return result
    except Exception as e:
      raise ConnectionError(f"Error al eliminar el documento de la colección {self.__collection_name}: {e}")
    
  def drop(self):
    '''
    Función para eliminar la colección.
    '''
    
    try:
      self.db.drop_collection(self.__collection_name)
      self.__collection = None
      self.__collection_name = None
      self.close()
      return True
    except Exception as e:
      raise ConnectionError(f"Error al eliminar la colección {self.__collection_name}: {e}")