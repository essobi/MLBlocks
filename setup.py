#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
    'keras>=2.1.3',
    'numpy>=1.14.0',
    'opencv-python>=3.4.0.12',
    'scikit-image>=0.13.1',
    'featuretools==0.1.17'
]

tests_require = [
    'mock>=2.0.0',
    'pytest>=3.4.2',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Pipelines and primitives for machine learning and data science.",
    extras_require={
        'test': tests_require
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='machine learning classification',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='mlblocks',
    packages=find_packages(include=['mlblocks', 'mlblocks.*']),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/HDI-Project/MLBlocks',
    version='0.1.4-dev',
    zip_safe=False,
)
