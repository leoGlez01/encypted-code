from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="encryptedcode",
    version="1.1.5",
    python_requires=">=3.6",
    description="This library can be used to encrypt and decrypt passwords using the new L0123 algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Leandro Gonzalez Espinosa",
    author_email="lworkgonzalez01@gmail.com",
    url="https://github.com/leoGlez01/encrypted-code.git",
    packages=find_packages(),
    install_requires=[
        "cryptography>=3.4.7"
    ],
    keywords=["encryption", "encrypted", "encode", "decode", "algorithm", "Leandro Gonzalez Espinosa", "Leandro Gonzalez", "Glez Dev"],
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)