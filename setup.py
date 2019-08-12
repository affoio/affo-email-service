import ast
import codecs
import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Get version
_version_re = re.compile(r'VERSION\s+=\s+(.*)')

with open('affo_email_service/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


# Get requirements
def get_requirements(env=None):
    requirements_filename = 'requirements.txt'

    if env:
        requirements_filename = f'requirements-{env}.txt'

    with open(requirements_filename) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


install_requirements = get_requirements()
tests_requirements = get_requirements('test')

setup(
    name='affo-email-service',
    version=version,
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/affoio/affo-email-service',
    author='Aleksey Dalekin',
    author_email='ald@affo.io',
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Distributed Computing',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent'
    ],
    keywords='email service',
    packages=find_packages(exclude=['test*']),
    setup_requires=['pytest-runner'],
    install_requires=install_requirements,
    tests_require=tests_requirements
)
