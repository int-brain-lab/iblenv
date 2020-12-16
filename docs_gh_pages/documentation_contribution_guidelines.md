# Overview of documentation

The documentation is built locally and hosted on a github-pages website at this address:
https://int-brain-lab.github.io/iblenv/

The website is generated using
 1. The markdown files in the `./docs-gh-pages` folder
 2. The python or ipython notebooks in the `./docs-gh-pages/notebooks`
 3. The python or ipython notebooks in the ibllib repo  `./examples` and `./brainbox/examples` folders
 4. The docstrings in the source code of the `./ibllib`, `./alf`, `./one` and `./brainbox` folders


# Contributing to documentation

### Adding examples or tutorials to the documentation
Examples or tutorials should be placed in the folders (can be in sub-folders within these folders)
`ibllib-repo/examples`
or
`ibllib-repo/brainbox/examples`

They can be either `.py` or `.ipynb` form but must have a prefix of `docs` to be included in the documentation, 
e.g `docs_coronal_slice.py` or `docs_get_LFP_data.ipynb`. Each example/ tutorial must start with a title and a brief 
description of the content. Please refer to the templates in the [templates folder](./templates) for examples of 
how to layout the title and description in order for it to be correctly rendered and displayed on the website. 

Once you have created the example/ tutorial you should link to the file in either `05_tutorials.rst` or `06_examples.rst`.
The link should be made by adding in the following line `notebooks_external\name_of_example_without_extension`, e.g
`notebooks_external\docs_coronal_slice`

`notebooks_external\docs_get_LFP_data`

An example implementation can be seen in the `06_examples.rst` file

## Making documentation
### Install dependencies to build the website locally
```shell
pip install -r ./docs_gh_pages/requirements-docs.txt
```

### Option 1: Only building changes to documentation
If you have only made changes to the documentation (any of the files with `.md` or `.rst` extenstion), you can build the
documentation without running the examples. The examples previously updated on the website will remain. To only
build the documentation, the following command can be used

```python
cd ./docs_gh_pages
python make_script.py -d
```

### Option 2: Building changes to documentation and specific examples
If you want to add a new example or change a few of the existing examples, it is possible to the build the documentation
while only executing a few specified examples. The documentation can be built using the following commnand and providing
the path to your .ipynb or .py example scripts. 

```python
cd ./docs_gh_pages
python make_script.py -e -s <path to example to execute>
```

An example would be
```
python make_script.py -e -s C:\Users\Mayo\iblenv\ibllib-repo\brainbox\examples\docs_get_training_status.py C:\Users\Mayo\iblenv\iblenv\docs_gh_pages\notebooks\one_basics\one_basics.ipynb
```

### Option 3: Building changes to documentation and all examples
If you want to rebuild the documentation and all examples you can use the following code

```python
cd ./docs_gh_pages
python make_script.py -e
```

### Previewing the built documentation
Once the `make_script.py` has completed a preview of the documentation can be viewed by opening 
`./docs-gh-pages/_build/html/index.html` in a web browser.

Check that all notebooks have run without errors and that your changes have been implemented correctly! (N.B if you have
run the `make_script.py` using option 1 or 2, some or all of the examples will not have executed, this is expected)


## Pushing changes to gh-pages
Once you are happy with the built documentation, the changes can be deployed to the website by running the following
command

```python
python make_script.py -gh -m "your commit message"
```

## Cleaning up your build
Once your changes have been pushed to github, run the following command to clean up your ibllib and iblenv 
directories and unexecute example notebooks
```python
python make_script.py -c
```


