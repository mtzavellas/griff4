from setuptools import setup, find_packages
setup(
    name="griff4",
    version="0.1",
    packages=find_packages('src'),
)

install_requires=[
   'numpy',
   'pandas'
]
