from setuptools import setup, find_packages

setup(
    name='ChFTP',
    version='1.0',
    packages=find_packages(),
    extras_require={
        'Colors-CLI': 'termcolor'
    },
    url='https://github.com/Chapna/ChFTP',
    license='GPLv2',
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Simple ‫‪Distributed‬‬ ‫‪File‬‬ ‫‪Sharing‬‬ System'
)
