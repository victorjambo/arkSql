from setuptools import setup, find_packages

setup(
    name="arksql",
    packages=find_packages(),
    version="0.0.1",
    description="light weight orm",
    author="Victor Mutai",
    author_email="victor.mutai@andela.com",
    url="https://github.com/victorjambo",
    download_url="https://github.com/victorjambo",
    keywords=["victorjambo", "orm", "ark", "arksql"],  # arbitrary keywords
    install_requires=[
        "pytest==2.9.2",
        "psycopg2==2.7.6"
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Database :: Front-Ends"
    ],
    entry_points={
        "console_scripts": [
            "ark = arksql:print_hello_world"
        ]},
)