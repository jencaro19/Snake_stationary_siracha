from setuptools import setup
import os

def open_file(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name="spicy_snake",            # name of your package
   version="0.0.1",
   description="a terminal based snake game",
   long_description=open_file("README.md"),  # only if you have a README.md
   author="Jenny Carolina Franco Valiente",
   author_email="jencaro19@hotmail.com",
   packages=["spicy_snake"],      # same as name the folder where the game is inside not the main folder name
   url="https://github.com/jencaro19/Snake_stationary_siracha",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.8",
   ]
)