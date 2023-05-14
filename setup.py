from setuptools import setup, find_packages

setup(
    name='cgso',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cgso = replace_names.cli:cli',
        ],
    },
    install_requires=[
        'Click>=8.0.0',
    ],
)
