import os
import importlib.util
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def scan_directory(folder_path):
    if sys.argv:
        scan_directory = sys.argv[1] if len(sys.argv) > 1 else None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if root.split(os.path.sep)[-1] == scan_directory if scan_directory else True and file.endswith("_model.py"):
                module_name = os.path.splitext(file)[0]
                module_path = os.path.join(root, file)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if hasattr(attribute, "__tablename__"):
                        attribute.metadata.create_all(engine)

current_dir = os.path.dirname(os.path.abspath(__file__))

# as_std_folder = os.path.join(os.path.dirname(current_dir), "as_std_номенклатура")
as_std_folder = os.path.abspath(os.path.join(current_dir, ".."))

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

scan_directory(as_std_folder)

session.close()

