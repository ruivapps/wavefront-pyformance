# coding: utf-8

"""
    Wavefront Pyformance Library

    <p>The Wavefront Pyformance library provides Wavefront reporters (via proxy and direct ingestion) and a simple abstraction for tagging at the host level. It also includes support for Wavefront delta counters.</p>  # noqa: E501

"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wavefront_pyformance"
VERSION = "0.9.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pyformance >= 0.4", "wavefront_sdk"]

setup(
    name=NAME,
    version=VERSION,
    description="Wavefront Pyformance Library",
    author_email="",
    url="https://github.com/wavefrontHQ/wavefront-pyformance",
    keywords=["Wavefront Pyformance", "Wavefront"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Wavefront Pyformance library provides Wavefront reporters (via proxy and direct ingestion) and a simple abstraction for tagging at the host level. It also includes support for Wavefront delta counters.
    """
)
