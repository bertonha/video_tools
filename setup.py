from setuptools import setup

setup(
    name='Video Compressor',
    version='0.1',
    py_modules=['video_compress'],
    install_requires=[
        "Click",
        "pathlib",
    ],
    entry_points='''
        [console_scripts]
        video_compress=video_compress:cli
    ''',
)
