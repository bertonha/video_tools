from setuptools import setup

setup(
    name='Video Compressor',
    version='0.1',
    py_modules=['compress_dir'],
    install_requires=[
        "Click",
        "pathlib",
    ],
    entry_points='''
        [console_scripts]
        compress_dir=compress_dir:cli
    ''',
)
