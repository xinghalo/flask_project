from setuptools import setup, find_packages

setup(
    name='test',
    version='1.0',
    long_description='hello world by xingoo',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'argparse'
    ],
    test_suite='tests',
    tests_require=['unittest2']
)