from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="repository_setup",            
    version="2.0.0",
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
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "repository_setup.files": ["__init__.py", "__main__.py", "Args.py", ".gitignore",
                                   "Output.py", "Util.py", "LICENSE.md", "README.md",
                                   "setup.py"]
    },
    install_requires=[
        
    ],
    entry_points={
        "console_scripts": [
            "repository_setup = repository_setup.__main__:main"
        ]
    }
)