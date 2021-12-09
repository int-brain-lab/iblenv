# How to contribute

## Code
### Linting
We use `flake8` python module to enforce a consistent style in the CI.

### Testing
Unit testing.  For Python we use the `pytest` module and alternate between `unittest` and `pytest` syntax. 
For `Matlab` we use the embedded test framework.

### Continuous Integration
For production repositories such as ibllib and alyx, continuous integration is set on Travis to install the application and run the tests on pull request.


## Contributions and releases
### Contributions and code review
The branches `develop` and `master` are protected.

Contributions are developed either:
-   on a separate branch
-   on a separate fork of the repository

and then merged in `develop` through a pull request.


#### Practical tips:
-   to avoid merge conflicts merge `develop` into your branch (or rebase your branch) before submitting the PR !
-   make sure your branch passes tests:
    -   before pushing by running unit tests and flake8 locally 
    -   after pushing looking at continuous integration results on Github 
-   go through the review process with maintainers on the pull request interface on GitHub. Remind them if not done in a timely manner. Github sends them a bazillion emails daily.


### Branching model: gitflow
Branching model as close as possible to gitflow, i.e. one master branch with every commit tagged with a version number: one develop branch to integrate the different volatile feature branches.
**Both develop and master should pass CI tests**

### Releasing scheme: semantic versioning
If any releasing scheme (such as ibllib), we use semantic versioning using the major.minor.micro or major.minor.patch model. patch/micro for bugfixes; minor for augmented functionality; major for retrocompatibility breaks.
Version 0.*.* are developing versions w/ no guarantee of retrocompatibility.

It is a good practice to document the changes in a `RELEASE_NOTES.md` document at the root of the repository.  
NB: those notes should be geared towards users not other fellow contributors.
