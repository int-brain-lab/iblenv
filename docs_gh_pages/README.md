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

Once you have created the example/ tutorial you should link to the file in the appropriate `.rst` file: `index.rst`, `06_examples.rst`
, `atlas_examples.rst` etc...
The link should be made by adding in the following line `notebooks_external\name_of_example_without_extension`, e.g
`notebooks_external\docs_coronal_slice`

`notebooks_external\docs_get_LFP_data`

An example implementation can be seen in the `06_examples.rst` file

### Tips to create and edit example notebooks

#### Hide a cell in the documentation
In the cell metadata, add the key `nbsphinx` with the value `hidden` to hide the cell in the documentation.

```json
{
    "nbsphinx": "hidden",
    "trusted": false
}
```

#### Prevent execution of a cell in the build documentation
Let's say an example is using too large of a dataset. One cell can be disabled by adding the following key to the to cell metadata.

```json
{
    "ibl_execute": false
}
```

#### Prevent execution of the whole notebook in the build documentation
If the full notebook is to be skipped, you can also set the `ibl_execute` flag to `false` in the notebook metadata.

#### Disable logging and tqdm output:
To have a clean output in the documentation, it is recommended to disable the logging and tqdm output in the example by adding a hidden cell at the top of the notebook.
(make sure the cell metadata contains the key `nbsphinx` with the value `hidden` as specified above)

```python
# Turn off logging and disable tqdm this is a hidden cell on docs page
import logging
import os

logger = logging.getLogger('ibllib')
logger.setLevel(logging.CRITICAL)

os.environ["TQDM_DISABLE"] = "1"
```

## Making documentation using github actions
Two github actions workflows have been made available to automate the building and the deployment of the docs. These are located in the int-brain-lab/iblenv repository and can be accessed under the actions tab

### Developing docs

Steps:
- create documentation branches called `docs` on the `ibllib` and `iblenv` repositories. The workflow will only run if the branch exists in both repos  (TODO if it doesn't exist make github action fallback to master)
- add your changes to the documentation
- run the [Build docs workflow](https://github.com/int-brain-lab/iblenv/actions/workflows/build_docs.yml).  To run the workflow click on the `run_workflow` button in the top left corner and choose the branch you want to launch it from (this should normally be docs).

After the docs build has completed succesfully your documentation will appear at this site http://testdocs.internationalbrainlab.org.s3-website-us-east-1.amazonaws.com
 

### Deploying docs
**WARNING: Do not run this workflow unless you have run the build docs workflow above and checked that the documentation is correct**

Steps:
-   merge the `docs` branch into `master` on the `iblenv` repository
-   merge the `docs` branch into `develop` on the `ibllib` repository
-   run the [Deploy docs workflow](https://github.com/int-brain-lab/iblenv/actions/workflows/deploy_docs.yml).  To run the workflow click on the `run_workflow` button in the top left corner and choose the branch you want to launch it from (this should be master).
 
The new docs will then be deployed to the main documnetation website https://int-brain-lab.github.io/iblenv/


## Making documentation locally
### Install dependencies to build the website locally
Activate your iblenv environment first and install the dependencies on top using pip
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



