from setuptools import setup, find_packages

setup(
    name="wifite_h4x0r",
    version="1.0.0",
    description="Custom launcher for Wifite2 on Kali Linux",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Abdo / Kojak291",
    url="https://github.com/Kojak291/Abdo/wifite-h4x0r",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": ["wifite-h4x0r = wifite_h4x0r.cli:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)
