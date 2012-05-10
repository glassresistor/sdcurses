from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    requirements = file.read()
requirements = requirements.split('\n')

setup(
    name='sdcurses',
    version='0.0.1',
    description="A curses interface for the SmartData Center technology.",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
    ],
    keywords='web,joyent',
    author='Michael T. Clemmons',
    author_email='glassresistor@gmail.com',
    url='https://github.com/glassresistor/sdcurses',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    entry_points={
    'console_scripts': [
        'sdcurses = sdcurses.main:start',
        ],
    },
)
