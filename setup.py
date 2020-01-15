import ast
import codecs
import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Extra commands for documentation management
cmdclass = {}
command_options = {}

# Build Sphinx documentation (html)
# python setup.py build_sphinx
# generates files into build/sphinx/html
try:
    from sphinx.setup_command import BuildDoc

    cmdclass["build_sphinx"] = BuildDoc
except ImportError:
    pass


# Upload Sphinx documentation to PyPI (using Sphinx-PyPI-upload)
# python setup.py build_sphinx
# updates documentation at http://packages.python.org/affo-email-service/
try:
    from sphinx_pypi_upload import UploadDoc

    cmdclass["upload_sphinx"] = UploadDoc
except ImportError:
    pass


# Get the long description
with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


# Get version
_version_re = re.compile(r"VERSION\s+=\s+(.*)")

with open("affo_email_service/__init__.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1)))


# Get requirements
def get_requirements(env=None):
    requirements_filename = "requirements.txt"

    if env:
        requirements_filename = f"requirements-{env}.txt"

    with open(requirements_filename) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requirements = get_requirements()
test_requirements = get_requirements("test")

setup(
    name="affo-email-service",
    version=version,
    description="",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/affoio/affo-email-service",
    author="Aleksey Dalekin",
    author_email="ald@affo.io",
    license="BSD",
    platforms=["any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Distributed Computing",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
    ],
    keywords="email service",
    packages=find_packages(exclude=["test*"]),
    cmdclass=cmdclass,
    command_options=command_options,
    setup_requires=["pytest-runner"],
    install_requires=install_requirements,
    tests_require=test_requirements,
    include_package_data=True,
    entry_points={"console_scripts": ["affo-email-service = affo_email_service.cli:manager.run"]},
)
