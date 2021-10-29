from glob import glob
from os.path import splitext, basename

from setuptools import setup, find_packages

CLASSIFIERS = [
    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: MIT',
    'Operating System :: Unix',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Utilities',
]

setup(
    name='faker_animal',
    version='0.1',
    license='MIT',
    description='Provider for Faker which adds fake animal names.',
    author='Mario Rojas',
    author_email='mrojas.leyva@gmail.com',
    url='https://github.com/mariorojas/faker_animal',
    packages=find_packages('faker_animal'),
    package_dir={'': 'faker_animal'},
    py_modules=[splitext(basename(path))[0] for path in glob('faker_animal/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    project_urls={
        'Issue Tracker': 'https://github.com/mariorojas/faker_animal/issues',
    },
    python_requires='>=3.6',
    install_requires=['Faker>=4.0.3'],
    test_requires=['pytest>=6.2'],
)
