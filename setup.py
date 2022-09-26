from setuptools import setup

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="repository_setup",            
    version="1.0.0",
    author="5f0",
    url="https://github.com/5f0ne/repository-setup",
    description="Creates the basic repository structure for python projects",    
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=["repository_setup"],
    install_requires=[
        
    ],
    entry_points={
        "console_scripts": [
            "repository_setup = repository_setup.__main__:main"
        ]
    },
    data_files=[("files", ["files/__init__.py", "files/__main__.py", "files/.gitignore", 
                           "files/Controller.py", "files/LICENSE.md", "README.md",
                           "setup.py"])]
)