from setuptools import setup

setup(
    name="Grank",
    version="0.0.4",
    py_modules=['grank'],
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
    """
)