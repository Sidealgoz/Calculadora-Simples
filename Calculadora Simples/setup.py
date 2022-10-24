from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Calculadora Simples",
    version="0.0.1",
    author="Rodrigo Macario",
    author_email="rodrigo.macario@gmail.com",
    description="Aprendendo Python implementation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sidealgoz/simple-package-template"
    packages=find_packages(),
    install_requires=import operators,
    python_requires='>=3.8',
)
