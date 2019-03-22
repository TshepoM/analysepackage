from setuptools import setup, find_packages

setup(
    name='analysepackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA TSHEPO MOLOPE analyse hackathon submission',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/TshepoM/analysepackage',
    author='TSHEPO MOLOPE',
    author_email='tfmolope@gmail.com'
)
