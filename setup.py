import setuptools

with open("README.md", "r") as fh:
    long_description = str(fh.read())

setuptools.setup(
    name="pyShodan",
    version="0.2.7",
    author="Shane Scott",
    author_email="sscott@gotham-security.com",
    description="Python library for querying the Shodan API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoVanguard/pyShodan",
    packages=['pyShodan'],
    install_requires=["shodan", "IPy"],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ),
)
