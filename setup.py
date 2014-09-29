from setuptools import setup

setup(
    name='pastio',
    version='0.0.1',
    description='Copy-Paste buffer across a cloud',
    url='',
    packages=['pastio'],
    entry_points={'console_scripts': ['pastio = pastio.cli:cli',
                                      'pastin = pastio.cli:copy',
                                      'pastout = pastio.cli:paste']},
    install_requires=['click', 'parse_rest'],
    maintainer='Alexander Kushnarev',
    maintainer_email='avkushnarev@gmail.com',
)
