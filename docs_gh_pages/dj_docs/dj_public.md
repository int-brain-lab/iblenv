# Publicly available IBL data

## Pilot electrophysiology data release

The IBL has released four pilot datasets that are available through both ONE and Datajoint. To start exploring the datasets with ONE please follow the link below.

[**Accessing public data with ONE**](https://int-brain-lab.github.io/ONE/notebooks/one_quickstart.html)

The IBL has also released all of the behavior sessions associated with the publication, [International Brain Laboratory et al., 2021](https://elifesciences.org/articles/63711). To access these data using DataJoint, follow the steps below.

## Accessing public IBL data with DataJoint

### Accessing the public database through JupyterHub

You can use an online python environment to interact with the data using the following link:

**Jupyter Notebooks website <https://jupyterhub.internationalbrainlab.org/>**

```{important}
To be able to log in to JupyterHub, you will need a [GitHub](https://github.com/) account to authorize login sessions.
```

The site hosts several python notebooks that will allow you to interact with the database directly online using DataJoint. You won't need to download or install anything locally. 


1. Log in with your GitHub account.
   - If logging in for the first time, you may need to click the "Start My Server" button.
   - After logging in, you should see `private_notebooks`, `public_notebooks`, and `README.md`.
2. Read over the file `README.md`
3. Click on `public_notebooks/Explore IBL pipeline` to see several `.ipynb` files. These notebooks will guide you through the process of replicating the figures from the behavior paper.
   - To replicate all the figures from the behavior paper, visit this GitHub Repository: <https://github.com/int-brain-lab/paper-behavior>
4. Use the `private_notebooks` folder to write your own personal scripts and notebooks only available to you.

### Accessing the public database on your local machine

```{important}
To be able to access the data from your local machine, you will need to have a working python environment with all of the required dependencies installed. For more information, see <https://github.com/int-brain-lab/iblenv>.
```

Before you can start using DataJoint with IBL data on your local machine, you will need to set your DataJoint credentials. You must specify a database connection to tell DataJoint where to look for IBL data, as well as grant access to these data by providing a username and password. 

Start by opening a new python script or terminal, then import DataJoint and set a few configuration options. [With your IBL environment activated](../02_installation.md), run:

```python
import datajoint as dj
```

The database's hostname, username, and password are saved in the global variable `dj.config`. See it's contents by running the following line:

```python
dj.config
```

By default, it should look something like this:

```
{   'connection.charset': '',
    'connection.init_function': None,
    'database.host': 'localhost',
    'database.password': None,
    'database.port': 3306,
    'database.reconnect': True,
    'database.use_tls': None,
    'database.user': None,
    'display.limit': 12,
    'display.show_tuple_count': True,
    'display.width': 14,
    'enable_python_native_blobs': True,
    'fetch_format': 'array',
    'loglevel': 'INFO',
    'safemode': True}
```

You need to replace a few entries with the following values used for the public data: 

```{important}
Public IBL Credentials:

  hostname: datajoint-public.internationalbrainlab.org
  username: ibl-public
  password: ibl-public
```

The database connection is specified by the key `database.host`. Change the config using the values above for the fields `database.host`, `database.user` and `database.password`:

```python
dj.config["database.host"] = "datajoint-public.internationalbrainlab.org"
dj.config["database.user"] = "ibl-public"
dj.config["database.password"] = "ibl-public"
```

Then save the changes to a local JSON configuration file (`dj_local_conf.json`) by running:

```python
dj.config.save_local()
```

After the above step, every time you start your python kernel from a directory that contains this file, DataJoint will look for this file and load the config without having to set credentials again. If you want to set your credentials globally without having to be in the directory containing the file `dj_local_config.json`, you can do so by running the following:

```python
dj.config.save_global()
```

To test whether your credentials work, try connecting to the database by running:

```python
dj.conn()
```

You should find that DataJoint automatically connects to the database! To see which schemas you have access to, run:

```python
dj.list_schemas()
```

You should have access to the following _public_ schemas:

```python
[
    "ibl_acquisition",
    "ibl_action",
    "ibl_analyses_behavior",
    "ibl_behavior",
    "ibl_data",
    "ibl_ephys",
    "ibl_histology",
    "ibl_reference",
    "ibl_storage",
    "ibl_subject",
]
```

Use the DataJoint class `VirtualModule` to connect the database schemas to python and be able to use DataJoint syntax to access and query data from the above tables. 

```python
reference = dj.VirtualModule("reference", "ibl_reference")
subject = dj.VirtualModule("subject", "ibl_subject")
action = dj.VirtualModule("action", "ibl_action")
acquisition = dj.VirtualModule("acquisition", "ibl_acquisition")
data = dj.VirtualModule("data", "ibl_data")
behavior = dj.VirtualModule("behavior", "ibl_behavior")
ephys = dj.VirtualModule("ephys", "ibl_ephys")
histology = dj.VirtualModule("histology", "ibl_histology")
behavior_analyses = dj.VirtualModule("analysis.behavior", "ibl_analyses_behavior")
```

Use `VirtualModule()` so you don't have to obtain the [IBL-pipeline](https://github.com/int-brain-lab/IBL-pipeline) source code and import these modules directly from the `ibl_pipeline` package. The `VirtualModule` method is equivalent (in terms of public data read access privileges) to doing the following if you have access to the source code:

```python
from ibl_pipeline import reference, subject, action, acquisition, data, behavior, ephys, histology
from ibl_pipeline.analyses import behavior as behavior_analyses
```

You can view the `public_notebooks` as described in the JupyterHub section above for more details on queries and usage of the public tables using DataJoint for python, as well as the [IBL DataJoint behavior plot example notebook](../notebooks/dj_intro/dj_intro.ipynb) 

### Accessing public data through direct download

You may also directly download the data through your web browser without running any code. Simply load an internet browser and use the provided link below.

Behavior paper data URL: <http://ibl.flatironinstitute.org/public/behavior_paper_data.zip>

### Accessing data via IBL Navigator

**IBL Navigator website [https://data.internationalbrainlab.org/](https://data.internationalbrainlab.org/)**

DataJoint also provides a website that displays plots generated from public data managed by the [IBL-pipeline](https://github.com/int-brain-lab/IBL-pipeline). 

### DataJoint reference material

For general documentation on DataJoint, please see the following links:

- [DataJoint Python Documentation](https://docs.datajoint.org/python/)
- [Explore DataJoint interactively](https://tutorials.datajoint.io/)
- [IBL DataJoint Basics](https://int-brain-lab.github.io/iblenv/notebooks/dj_basics/dj_basics.html)
