# Overview of documentation

The documentation is built locally and hosted on a github-pages website at this address:
https://int-brain-lab.github.io/iblenv/

The website is generated using
 1. The markdown files in the `./docs-gh-pages` folder
 2. The python or ipython notebooks in the `./docs-gh-pages/notebooks`
 3. The python or ipython notebooks in the  `./examples` and `./brainbox/examples` folders
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
Once you have made your changes to the documentation, the documentation can be built using the following command. This
executes all .ipynb and .py notebooks included in the documentation and uses nb-sphinx and sphinx to then generate the 
built html version of the files. 

```python
cd ./docs_gh_pages
python make_script.py -e -d -c
```
- `-e` executes all the notebooks and python scripts specified in the build path
- `-d` builds the documentation using sphinx
- `-c` unexecutes all notebooks and removes any unwanted files

Once this script has completed a preview of the documentation can be viewed by opening 
`./docs-gh-pages/_build/html/index.html` in a web browser.

Check that all notebooks have run without errors and that your changes have been implemented correctly!

## Pushing changes to gh-pages
Once you are happy with the built documentation, the changes can be deployed to the website by running the following
command

```python
python make_script.py -gh -m "your commit message"
```

## Flake8nb
Linting checks can be applied to ipynb. notebooks using flake8_nb, an example implementation is
```python
flake8_nb .\notebooks\one_intro\one_intro.ipynb
```

