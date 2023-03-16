from setuptools import setup

setup(
    name="ioka-test",
    version="0.0.1",
    description="Ioka payment system package",
    url="http://github.com/amiradin/ioka-test",
    author="Zhaks",
    license="MIT",
    packages=["ioka-test"],
    install_requires=[
        "requests",
    ],
    zip_safe=False,
)
