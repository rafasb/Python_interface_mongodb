from database import MyDataBase
from collection import MyCollection
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Test database.py")
  parser.add_argument("--interactive", action="store_true", help="Run tests interactively")
  args = parser.parse_args()
  interactive = args.interactive
  
  db = MyDataBase()
  print(f"Nombre de la base de datos creada: {db.db_name}")
  
  # TEST: Crear colección, insertar documento y eliminar colección
  collection_name = "test_collection"
  collection = MyCollection(collection_name, db.db_name)
  print(f"Colección {collection.collection_name} creada correctamente")
  if interactive:
    input("Presione Enter para continuar...")
  collection.insert({"name": "test"})
  print("Documento insertado correctamente")
  if interactive:
    input("Presione Enter para continuar...")
  collection.drop()
  print("Colección eliminada correctamente")
  db.close()
  
  # TEST: Crear colección con documentos 
  collection_name = "test_collection"
  collection = MyCollection(collection_name, db.db_name)
  print(f"Colección {collection.collection_name} creada correctamente")
  collection.insert([{"name": "test1"}, {"name": "test2"}])
  if interactive:
    input("Presione Enter para continuar...")
  collection.drop()
  print("Colección eliminada correctamente")
  db.close()
  
  # TEST: Crear colección con documentos y buscar documentos
  collection_name = "test_collection"
  collection = MyCollection(collection_name, db.db_name)
  print(f"Colección {collection.collection_name} creada correctamente")
  collection.insert([{"name": "test1"}, {"name": "test2"}])
  doc = collection.find_one({"name": "test1"})
  print(f"Documento encontrado: {doc}")
  if interactive:
    input("Presione Enter para continuar...")
  doc = collection.find_all({"name": "test1"})
  print(f"Documentos encontrados: {doc}")
  if interactive:
    input("Presione Enter para continuar...")
  collection.drop()
  print("Colección eliminada correctamente")
  db.close()
  
  # TEST: Actualizar documento
  collection_name = "test_collection"
  collection = MyCollection(collection_name, db.db_name)
  print(f"Colección {collection.collection_name} creada correctamente")
  collection.insert([{"name": "test1", "year":"1973"}, {"name": "test2"}])
  if interactive:
    input("Presione Enter para continuar...")
  collection.update({"name": "test1"}, {"name": "test2"})
  print("Documento actualizado correctamente")  
  if interactive:
    input("Presione Enter para continuar...")
  doc = collection.find_all({"name": "test2"})
  print(f"Documentos encontrados: {doc}")
  if interactive:
    input("Presione Enter para continuar...")
  collection.drop()
  print("Colección eliminada correctamente")
  db.close()
  
  # TEST: borrar un documento
  collection_name = "test_collection"
  collection = MyCollection(collection_name, db.db_name)
  print(f"Colección {collection.collection_name} creada correctamente")
  collection.insert([{"name": "test2", "year":"1973"}, {"name": "test2"}])
  if interactive:
    input("Presione Enter para continuar...")
  collection.delete({"name": "test2"})
  print("Documento eliminado correctamente")  
  if interactive:
    input("Presione Enter para continuar...")
  doc = collection.find_all({"name": "test2"})
  print(f"Documentos encontrados: {doc}")
  if interactive:
    input("Presione Enter para continuar...")
  collection.drop()
  print("Colección eliminada correctamente")
  db.close()