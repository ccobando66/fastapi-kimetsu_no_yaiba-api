from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv
load_dotenv()

conexion = create_engine(f"postgresql://{os.environ.get('USER_NAME')}:{os.environ.get('PASSWD')}@"
                         f"{os.environ.get('HOSTMANE')}:{os.environ.get('PORT')}/{os.environ.get('DB')}")
Seccion = sessionmaker(bind=conexion)
Base = declarative_base()


    
 