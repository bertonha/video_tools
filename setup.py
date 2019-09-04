from setuptools import setup, find_packages


setup(
    name="Video Tools",
    version="0.1",
    packages=find_packages(),
    install_requires=["Click>=7.0.0", 'colorama;sys_platform=="win32"'],
    classifiers=["Programming Language :: Python :: 3"],
    license="MIT",
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["video_tools=video_tools.__main__:cli"]},
)
