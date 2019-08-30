from setuptools import setup, find_packages


setup(
    name='Video Tools',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "colorama",
    ],
    entry_points='''
        [console_scripts]
        video_tools=video_tools.__main__:cli
    ''',
)
