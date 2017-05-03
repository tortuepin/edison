from setuptools import setup

setup(
    name="edison",
    version='1,0',
    install_requires=[
        'Click',
        'toml',
        ],
    entry_points='''
        [console_scripts]
        edison=interface:cli
        ''',
        )

