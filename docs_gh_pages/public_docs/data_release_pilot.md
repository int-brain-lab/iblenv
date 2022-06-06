# Data Release - Pilot Dataset

The IBL has released a handful of pilot datasets that are available for download through ONE.

## How to browse the datasets
If you first want to quickly view and browse what datasets are in a recording session, you can easily do so in a web browser via this [Flatiron web page](https://ibl.flatironinstitute.org/public/).

Generally speaking, a single recording session fits into a folder, which name is characterised by:
it's lab name / a folder Subjects / the name of the subject (i.e. the mouse nickname) / the date / the session number.

For example: `mainenlab/Subjects/ZM_2240/2020-01-21/001`

Notes:
- A lab can host multiple subjects, e.g. the
[Churchland lab](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects) hosts `CSHL047` and `CSHL049`.
- There can be multiple sessions done in one day per subject, in such case the number of session `001` would increase
to `002`, `003` etc.
- Sometimes, the valuable data is found only in a later session in the day (in the case of a restart for example),
so it is not uncommon to see sessions for which only the `003` folder is saved for example.

## Neuropixels pilot datasets
Specifically, the Neuropixels pilot datasets are in the folders:

- [churchlandlab/Subjects/CSHL047/2020-01-20/001](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects/CSHL047/2020-01-20/001/)
- [churchlandlab/Subjects/CSHL049/2020-01-08/001](https://ibl.flatironinstitute.org/public/churchlandlab/Subjects/CSHL049/2020-01-08/001/)
- [cortexlab/Subjects/KS023/2019-12-10/001](https://ibl.flatironinstitute.org/public/cortexlab/Subjects/KS023/2019-12-10/001/)
- [hoferlab/Subjects/SWC_043/2020-09-21/001](https://ibl.flatironinstitute.org/public/hoferlab/Subjects/SWC_043/2020-09-21/001/)
- [zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001](https://ibl.flatironinstitute.org/public/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/)
- [mainenlab/Subjects/ZM_2240/2020-01-21/001/](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/)

Taking the session from [mainenlab/Subjects/ZM_2240/2020-01-21/001/](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/)
 as example, the following subfolders will contain:
- `alf/` : The extracted data, to be used in analysis.
- `logs/` : logged information
- `raw_behavior_data/` : The raw behavior data (events that occur during a trials)
- `raw_ephys_data/` : The raw ephys data (in this case, Neuropixels data)
- `raw_passive_data/`: The raw passive data (events that occur during the replay of task stimuli)
- `raw_video_data/`: The raw video data
- `spike_sorters/` : The raw processing output data for each spike sorter used

The `alf/` folder notably contains:
- the probe folder (`probe00/` or `probe01/`), in which are the extracted output of the spike sorting to be used for analysis
- the extracted behavior trials data
- the extracted DLC data (for each camera used, here `body`, `left` and `right`)
- the extracted wheel data
- the extracted passive protocol data

One probe folder, e.g. [`probe00/`](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/alf/probe00/)
can contain the output of multiple spike sorters. In this case, it contains a first spike sorter output directly into the
folder itself (see e.g. the `cluster` datasets), and a secondary version under a subfolder
(here the subfolder named `pykilosort`).

The size of each dataset can be easily viewed under the `Size` column in the web browser. For example,
the [raw vide data](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/raw_video_data/)
is particularly heavy (several GB). In this specific case, you can view the raw video data in the browser by clicking on it,
e.g. [_iblrig_leftCamera.raw](https://ibl.flatironinstitute.org/public/mainenlab/Subjects/ZM_2240/2020-01-21/001/raw_video_data/_iblrig_leftCamera.raw.edcfa043-6314-4f80-ba6f-bf6d08922eda.mp4).

A detailed explanation of datasets definition and format are described
in this [sheet](https://docs.google.com/spreadsheets/u/1/d/1ieLXRPLLSgUKcLvFkrqizfZl5HjdfE6bQ2KLBCRmjQo/edit?usp=drive_web&ouid=107692576857324699678)
and [document](https://docs.google.com/document/d/1OqIqqakPakHXRAwceYLwFY9gOrm8_P62XIfCTnHwstg/edit#).

## Download the public datasets

To start downloading and performing analysis on the datasets, please follow the link below.

1)  [Accessing public data with ONE](https://int-brain-lab.github.io/ONE/notebooks/one_quickstart.html)