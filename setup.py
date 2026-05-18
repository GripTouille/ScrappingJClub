from setuptools import setup, find_packages

setup(
    name="scrappingjclub",
    version="1.0.0",
    author="GripTouille",
    description="Un outil de synchronisation pour Cahier de Prépa",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GripTouille/ScrappingJClub",  # Optionnel
    packages=find_packages(),
    py_modules=["scrapp", "fonctions"],
    install_requires=[
        "selenium==4.44.0",
        "webdriver-manager==4.0.2",
        "requests==2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "scrapp-jclub=scrapp:main",  # Permettra de lancer le script avec une seule commande
        ],
    },
    python_requires=">=3.6",
)