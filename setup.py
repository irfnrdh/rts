from setuptools import setup, find_packages

setup(
    name="RTS",
    version="0.1.0",
    py_modules=["rts"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
             'rts=rts.cli:main',
        ],
    },
)