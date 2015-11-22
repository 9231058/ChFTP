from setuptools import setup

setup(
    name='ChFTP',
    version='1.5',
    packages=['ftp', 'presence'],
    package_dir={'ftp': 'src/ftp', 'presence': 'src/presence'},
    scripts=['src/scripts/ChFTP_cli.py'],
    url='https://github.com/Chapna/ChFTP',
    license='GPLv2',
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Simple ‫‪Distributed‬‬ ‫‪File‬‬ ‫‪Sharing‬‬ System',
    requires=['termcolor']
)
