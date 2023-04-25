from setuptools import setup

setup(
    name="housing-prediction",
    version="0.0.1",
    author="Arya Dixit",
    description="mmy ml pipline",
    packages=["housing"],
    install_requires=["Flask","pandas" ,"numpy","unicorn","sklearn"]
)