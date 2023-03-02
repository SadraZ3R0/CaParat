from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["wget", "requests"]

setup(
    name="CaParat",
    version="0.0.1",
    author="SadraZ3R0",
    author_email="m.sadra.gorji@gmail.com",
    description="a simple client for Aparat\nBy Z3R0 - Sadra\nZ3R0 discord > https://discord.gg/animeh",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/SadraZ3R0/CaParat/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)