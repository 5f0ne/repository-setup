# Description

Creates the basic repository structure for python projects

# Usage

`main.py [-h] --path PATH --name NAME`


| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path of the directory in which the repository shall be created |
|--name | -n | String | - | Name of the new repository |

# Example

Creates the following result:

```
################################################################################

Repository Setup by 5f0
Creates the basic repository structure for python projects

Current working directory: /path/to/repository-setup

Target directory: /path/to/repo/dir
Name of new repository: new-repo

Creation Datetime: 01/01/1970 10:11:12

################################################################################

Repository under /path/to/repo/dir/new-repo created successfully!

################################################################################
```

With the following folder structure:

```
/path/to/repo/dir/new-repo
├─── example
└─── src
     └─── Controller.py
└─── .gitignore
└─── main.py
└─── LICENSE.md
└─── README.md 
```

# License

MIT