from distutils.core import setup

setup(
    name='django-ssha512-hasher',
    version='1.0',
    packages=['ssha512',],
    license='MIT',
    install_requires=['django==1.7.5'],
    long_description=open('README.md').read(),
)

