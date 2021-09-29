.. one_ibl documentation master file, created by
   sphinx-quickstart on Fri Jul 20 17:20:00 2018.

Welcome to IBL code library documentation!
##########################################

IBL data structure
*************************
.. image:: ./_static/IBL_data.png
   :alt: Alyx data structure

In the IBL, data acquired in laboratories spread across countries needs to be centralized into a
common store, accessible from anywhere in the world, at all times.
This challenge is met by the IBL data architecture, documented briefly below; a thorough description
can be found in our `preprint <https://www.biorxiv.org/content/10.1101/827873v3>`_.

The central store has two components:

* A **Bulk Data Store** that stores **large raw data files** (e.g. raw electrophysiology and video data) as well as **pre-processed data** (e.g. results of spike sorting or video segmentation). This database is accessible through HTTP, FTP and Globus. This is known informally as the "Flatiron server" as our original data server was generously hosted by the `Flatiron Institute <https://www.simonsfoundation.org/flatiron/>`_.
* A **Relational Database** that stores **metadata** (e.g. information on each experiment and experimental subject) in a structured manner, together with links to the bulk data files. This database is known as `Alyx <https://github.com/cortex-lab/alyx>`_, for reasons no-one can remember.

Tools to access the data
*************************
There are two main ways to access the data:

* `ONE <https://int-brain-lab.github.io/ONE/>`_: an API that connects to the central store, allowing users to search and load data of interest from specific experiments.
* `Datajoint <https://datajoint.io>`_: a framework to perform automated pipelined analyses on a subset of lightweight data such as behavioral choices and spike times, that allows rapid integration of data from multiple experiments and users.

The full IBL data will be publically released when we have completed collection, preprocessing, curation, and quality control. In the meantime, a subset of curated data are publically available.

.. attention::
   Internal users should install the `Unified Environment <./02_installation.html>`_.

.. toctree::
   :hidden:
   :caption: The Open Neurophysiology Environment
   :maxdepth: 1

   notebooks_external/one_quickstart
   Full documentation Website for ONE <https://int-brain-lab.github.io/ONE/>

.. toctree::
   :hidden:
   :caption: DataJoint
   :maxdepth: 1

   dj_docs/dj_introduction
   dj_docs/dj_credentials
   notebooks/dj_intro/dj_intro
   notebooks/dj_basics/dj_basics

.. toctree::
   :hidden:
   :caption: Miscellaneous
   :maxdepth: 1

   02_installation
   011_ibl_viewer
   09_contribution
   genindex

.. toctree::
   :hidden:
   :caption: Examples & Tutorials
   :maxdepth: 1

   06_examples
   notebooks/dj_intro/dj_intro
   notebooks_external/docs_wheel_moves

.. toctree::
   :hidden:
   :caption: API Reference
   :maxdepth: 1

   010_api_reference.rst






