from setuptools import setup, find_packages
VERSION = '0.0.2'
DESCRIPTION = 'A package to drive the linguistic turn of accounting'
LONG_DESCRIPTION = 'We are the Intelligent Accounting Research Team of Beijing Foreign Studies University'

# Setting up
setup(
    name="cpanlp",
    version=VERSION,
    author="Draco Deng",
    author_email="dracodeng6@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://cpanlp.com"
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'accounting', 'cpa', 'intelligent accounting', 'linguistic turn', 'linguistic'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
