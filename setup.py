from setuptools import find_packages, setup
from pathlib import Path

__version__ = "0.1.0"

install_requires = (
    "Django==3.1.6",
    "djangorestframework==3.12.2",
    "djangogrpcframework==0.2",
    "django-manifest-loader==1.0.0",
    "grpcio-tools==1.35.0",
    "channels==3.0.3",
    "channels-redis==3.2.0",
    "beatserver==0.0.7",
)

development_requires = ["black"]

description = Path(__file__).with_name("README.md").open().read()

setup(
    description=description,
    install_requires=install_requires,
    extras_require={"development": development_requires},
    name="tunneltech",
    packages=find_packages(),
    python_requires="~=3.8",
    version=__version__,
)
