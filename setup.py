from setuptools import setup, find_packages

VERSION = '2.0.0'
DESCRIPTION = 'Acceleration methods to real series'

# Setting up
setup(
    name="extrapolation",
    version=VERSION,
    author="Wellington Silva",
    author_email="<wellington.71319@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages(),
    keywords=['python', 'extrapolation', 'numerical-analysis']
)
