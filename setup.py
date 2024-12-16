from setuptools import setup, find_packages

setup(
    name="star4py",
    version="1.7.0",
    description="自己的编程语言，再小也可以发光",
    author="Gin",
    author_email="log4gin@gmail.com",
    url="https://github.com/tomygin/star",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "star= starpy.star:main",
        ],
    },
    python_requires=">=3.10",
)
