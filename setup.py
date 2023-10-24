from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="emeson_borges",
    author_email="borges2016.leh@gmail.com",
    description="Biblioteca para processamento de Imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emeson-Borges"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)