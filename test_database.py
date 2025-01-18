from database import MyDataBase
import argparse


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Test database.py")
  parser.add_argument("--interactive", action="store_true", help="Run tests interactively")
  args = parser.parse_args()
  interactive = args.interactive
  
  db = MyDataBase()
  print(f"Nombre de la base de datos creada: {db.db_name}")
  print(f"Propiedades de la base de datos: {db.db}")
  db.close()
  print("Conexión cerrada correctamente")
  
  db = MyDataBase()
  collection_name = "test_collection"
  db.db.create_collection(collection_name)
  print(f"Colección {collection_name} creada correctamente")
  if interactive:
    input("Presione Enter para continuar...")
  db.dropDatabase()
  print("Base de datos eliminada correctamente")
  db.close()
  
  db = MyDataBase()
  collection_name = "test_collection"
  db.db.create_collection(collection_name)
  print(f"Colección {collection_name} creada correctamente")
  if interactive:
    input("Presione Enter para continuar...")
  db.dropCollection(collection_name)
  print("Base de datos eliminada correctamente")
  db.close()
  
  
  
    
  
  