from setuptools import setup, find_packages

classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]


setup(
    name="lois",
    version="0.0.7",
    description="the fastest and easy way to get insight of your dataset",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/charleslf2/lois.git",
    project_urls={
        "Bug Tracker":"https://github.com/charleslf2/lois/issues"
    },
    author="Charles TCHANAKE",
    author_email="datadevfernolf@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["EDA", "Data analysis", "Charles TCHANAKE", "Automation"],
    packages=find_packages(),
    install_requires=['pandas', "matplotlib", "seaborn", "rich"]
)