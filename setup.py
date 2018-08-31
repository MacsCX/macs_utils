from distutils.core import setup

setup(
    name="MacsUtils",
    author="MacsCX",
    author_email="maciek-cx@protonmail.com",
    version="0.1dev",
    packages=["macs_utils"],
    license="beerware",
    long_description=open("README.txt").read(),

    package_data={"": ["mock_data/*", "mock_data/long_strings/*"]}
)
