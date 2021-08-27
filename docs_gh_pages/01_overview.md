# IBL data architecture
[Alyx data structure](./_static/IBL_data.png)

In the IBL, data is acquired in various laboratories spread across countries, and needs to be centralized into a common database accessible to all from anywhere in the world, at all times.
This challenge is met by the IBL data architecture, described briefly below; a thorough description can be found on [**Biorxiv**](https://www.biorxiv.org/content/10.1101/827873v3).

Once acquired on a Rig, the data is first registered by the local server associated to that Rig onto two databases:
- [**Alyx**](https://github.com/cortex-lab/alyx), that stores **meta-data** (e.g. information on the mouse) in a relational manner
- [**Flatiron**](https://www.simonsfoundation.org/flatiron/), that stores **bulky raw data** (e.g. raw electrophysiology and video data) as well as processed data (e.g. output of spike sorting, output of video segmentation). This database is accessible through HTTP, FTP and Globus.

The Alyx database points to the files on the Flatiron server.

A specific set of lightweight, processed data (e.g. events on trials, spike times), **not raw data**, are then transferred onto a third database that enables further scientific analysis:
- [Datajoint](https://datajoint.io), that stores specific *processed, lightweight data* commonly used in analysis

An example of such analysis is to compute a subject's behavioral performance on a given day.

## How to access the data
-   **ONE**: set of normalized functions to access the IBL data. It queries the Alyx database and downloads data files from the FlatIron.
-   **Datajoint**: used for further processing the IBL neuroscience data.
