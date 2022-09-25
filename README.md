# Description

Creates the basic repository structure for python projects

# Usage

`main.py [-h] --path PATH --name NAME`


| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path of the directory in which the repository shall be created |
|--name | -n | String | - | Name of the new repository |
| --type | -t | String | - | Creates either a module or a lib | 

# Example

`python main.py -p /path/to/repo/dir -n new-module-repo -t module`

Creates the following result:

```
################################################################################

Repository Setup by 5f0
Creates the basic repository structure for python projects

Current working directory: /path/to/repository-setup

Target directory: /path/to/repo/dir
Name of new repository: new-module-repo

Creation Datetime: 01/01/1970 10:11:12

################################################################################

Repository of type module created successfully under /path/to/repo/dir/new-module-repo

################################################################################
```

With the following folder structure:

```
/path/to/repo/dir/new-module-repo
├─── example
└─── /src
     └─── Controller.py
└─── .gitignore
└─── main.py
└─── LICENSE.md
└─── README.md 
```

The structure for a lib repo looks like:
```
/path/to/repo/dir/new-lib-repo
└─── /src
└─── .gitignore
└─── main.py
└─── LICENSE.md
└─── README.md 
```

# License

MIT