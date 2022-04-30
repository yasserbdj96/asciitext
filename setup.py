#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com


#START{
from setuptools import setup,find_packages
setup(
    name="asciitext",
    version="0.0.4",
    author="YasserBDJ96",
    author_email="yasser.bdj96@gmail.com",
    description='''Text to ASCII Art Generator.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    project_urls={
        'Source Code': "https://github.com/yasserbdj96/asciitext",
        'Author WebSite': "https://yasserbdj96.github.io/",
        'Instagram': "https://www.instagram.com/yasserbdj96/",
    },
    install_requires=["hexor","requests"],
    keywords=['yasserbdj96', 'python', 'ascii', 'texts', 'colors.', 'hex','background', 'rgb'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Communications :: Email'
    ],
    python_requires=">=3.x.x"
)
#}END.
