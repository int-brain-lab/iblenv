# DataJoint credentials for internal IBL users

Before you can start using DataJoint with the IBL data online or on your local machine, you will need to retrieve and set your DataJoint credentials. You must specify a database connection to tell DataJoint where to look for IBL data, as well as grant access to these data by providing a username and password.

```{important}
To set up credentials for accessing internal IBL data (not the external/public-facing data), you will need access to your DataJoint username and password. You may use the same GitHub account to access the internal IBL DataJoint database from jupyter, but must first be added as an authorized user by an IBL admin. If you do not have access to any of these, please get in contact with a member of the IBL software team.
```

The _internal_ data configuration process is similar to the process outlined for public access. This process is described in the section, [**Accessing public IBL data with DataJoint**](dj_public).

The notable differences for external/public access are the following:

## Internal Jupyter link

The internal jupyter link is located at the:

**Internal Jupyter Notebooks website [https://jupyter.internationalbrainlab.org/](https://jupyter.internationalbrainlab.org/)**

## Internal database credentials

Whereas the public data uses the same credentials for all users, you will need your own credentials to access the internal IBL data. Also note the different database hostname.

```{important}
Internal IBL Credentials:

hostname: datajoint.internationalbrainlab.org
username: <your datajoint database username>
password: <your datajoint database password>
```

## Internal IBL Navigator access

The internal navigator link is located at the:

**Internal IBL Navigator website [https://djcompute.internationalbrainlab.org/](https://djcompute.internationalbrainlab.org/)**

You will need your DataJoint credentials from above to access the contents of this page.
