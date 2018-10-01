import setuptools


setuptools.setup(
    name="Grank",
    version="0.0.7",
    py_modules=['grank'],
    packages=setuptools.find_packages(),
    install_requires= [
        'click',
        'requests',
        'pandas',
        'numpy',
        'matplotlib'
    ],
    entry_points="""
        [console_scripts]
        grank=grank.core:main
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)