from setuptools import find_packages, setup

setup(
    name='bonsai_web_api',
    version='0.1dev',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ],
)