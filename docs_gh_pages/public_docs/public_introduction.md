# Publically available IBL data

## 2021: Pilot electrophysiology data release

The IBL has released four pilot datasets, that include both compressed raw ephys data and preprocessed data, as well as behaviour
and video data.  A full list of dataset types and their details can be found 
[here](https://docs.google.com/document/d/1OqIqqakPakHXRAwceYLwFY9gOrm8_P62XIfCTnHwstg/edit).

These datasets are available through ONE and Datajoint. 
To start exploring these datasets please follow the links below.

1) **[Accessing public data with ONE](public_one)** 
- Files are stored on Flatiron, following the ALF convention, and can be downloaded via ONE.
- If you want to access raw data (e.g. `raw_ephys_data`) please use this method, as the raw, bulky data is not stored on the Datajoint database.
- The full architecture of the folders and list of the files stored on Flatiron can be found below.

2)  **[Accessing public data with Datajoint](public_datajoint)** 
- Files are stored on the Datajoint database, following Datajoint nomenclatures with tables and schemas.
- Reminder: Only a subset of lightweight, commonly used datasets are stored on this database.
<!-- - TODO: List of datasets available -->

### ALF files on Flatiron
All of the following files can be dowloaded via ONE from Flatiron :
91 directories, 411 files
```
.
├─ behavior_paper_data.zip
├─ churchlandlab
|    ├─  Subjects
|        ├─ CSHL047
|        |    ├─  2020-01-20
|        |        ├─  001 -> /mnt/ibl/churchlandlab/Subjects/CSHL047/2020-01-20/001
|        ├─  CSHL049
|            ├─  2020-01-08
|                ├─  001
|                    ├─ alf
|                    |    ├─ _ibl_bodyCamera.dlc.92ff6d68-a6bc-4f6e-82fa-2c5bf577483a.pqt -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_bodyCamera.dlc.92ff6d68-a6bc-4f6e-82fa-2c5bf577483a.pqt
|                    |    ├─ _ibl_bodyCamera.times.0d42d971-c4f3-4cf4-971f-f380d226113b.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_bodyCamera.times.0d42d971-c4f3-4cf4-971f-f380d226113b.npy
|                    |    ├─ _ibl_leftCamera.dlc.c7b78fa3-4d65-4c5b-8520-7d67530c6aa7.pqt -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_leftCamera.dlc.c7b78fa3-4d65-4c5b-8520-7d67530c6aa7.pqt
|                    |    ├─ _ibl_leftCamera.times.4e0178c9-b4fd-49db-8c2e-42225b9edf9f.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_leftCamera.times.4e0178c9-b4fd-49db-8c2e-42225b9edf9f.npy
|                    |    ├─ _ibl_rightCamera.dlc.560f095a-2e15-4c42-a98f-ce16d64ac4d2.pqt -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_rightCamera.dlc.560f095a-2e15-4c42-a98f-ce16d64ac4d2.pqt
|                    |    ├─ _ibl_rightCamera.times.ba47762c-4ab1-404b-9e42-23a5e239cad9.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_rightCamera.times.ba47762c-4ab1-404b-9e42-23a5e239cad9.npy
|                    |    ├─ _ibl_trials.choice.54507795-e83a-4acf-934e-475bdc26f482.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.choice.54507795-e83a-4acf-934e-475bdc26f482.npy
|                    |    ├─ _ibl_trials.contrastLeft.eda2790e-3fdd-4621-a451-2896b24ae78a.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.contrastLeft.eda2790e-3fdd-4621-a451-2896b24ae78a.npy
|                    |    ├─ _ibl_trials.contrastRight.93c43e40-55bc-4c13-8eef-fc961ee7d360.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.contrastRight.93c43e40-55bc-4c13-8eef-fc961ee7d360.npy
|                    |    ├─ _ibl_trials.feedbackType.0c21e24e-e53b-4976-97bf-4c340ab9eaa7.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.feedbackType.0c21e24e-e53b-4976-97bf-4c340ab9eaa7.npy
|                    |    ├─ _ibl_trials.feedback_times.0a0b51ea-2fc5-472b-8161-4a179598f0a0.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.feedback_times.0a0b51ea-2fc5-472b-8161-4a179598f0a0.npy
|                    |    ├─ _ibl_trials.firstMovement_times.cd1c2cf9-b85b-4cf8-b936-97a3197fcdd1.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.firstMovement_times.cd1c2cf9-b85b-4cf8-b936-97a3197fcdd1.npy
|                    |    ├─ _ibl_trials.goCueTrigger_times.b85ad188-d4a2-439b-badb-a8b467e762ad.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.goCueTrigger_times.b85ad188-d4a2-439b-badb-a8b467e762ad.npy
|                    |    ├─ _ibl_trials.goCue_times.aa6c1a7d-88f7-4719-af37-9cc254b4918c.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.goCue_times.aa6c1a7d-88f7-4719-af37-9cc254b4918c.npy
|                    |    ├─ _ibl_trials.intervals.0992fbf5-097e-4e11-b77d-7b67aded890e.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.intervals.0992fbf5-097e-4e11-b77d-7b67aded890e.npy
|                    |    ├─ _ibl_trials.intervals_bpod.0fa9d4e9-5019-4014-839e-dd013228cf93.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.intervals_bpod.0fa9d4e9-5019-4014-839e-dd013228cf93.npy
|                    |    ├─ _ibl_trials.itiDuration.d50bdf3a-3e65-4003-b0c3-a9a832f92c34.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.itiDuration.d50bdf3a-3e65-4003-b0c3-a9a832f92c34.npy
|                    |    ├─ _ibl_trials.probabilityLeft.57bb5aab-5f5f-4a1c-be08-2a650c224853.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.probabilityLeft.57bb5aab-5f5f-4a1c-be08-2a650c224853.npy
|                    |    ├─ _ibl_trials.response_times.e3b133e5-65f9-47f7-be15-637ee5f334ec.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.response_times.e3b133e5-65f9-47f7-be15-637ee5f334ec.npy
|                    |    ├─ _ibl_trials.rewardVolume.0b8b202d-2bbc-4d95-93f1-3bcdde74de3f.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.rewardVolume.0b8b202d-2bbc-4d95-93f1-3bcdde74de3f.npy
|                    |    ├─ _ibl_trials.stimOff_times.1d3026b2-74c2-4df4-9149-4b912252b434.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.stimOff_times.1d3026b2-74c2-4df4-9149-4b912252b434.npy
|                    |    ├─ _ibl_trials.stimOn_times.37d9cdf2-e316-416d-b65d-34bd17c02fb7.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_trials.stimOn_times.37d9cdf2-e316-416d-b65d-34bd17c02fb7.npy
|                    |    ├─ _ibl_wheel.position.afde4e35-848c-4eb2-a8c1-d7b011fb4ffb.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_wheel.position.afde4e35-848c-4eb2-a8c1-d7b011fb4ffb.npy
|                    |    ├─ _ibl_wheel.timestamps.4cf15398-9653-4238-b240-ca11adaeaf33.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_wheel.timestamps.4cf15398-9653-4238-b240-ca11adaeaf33.npy
|                    |    ├─ _ibl_wheelMoves.intervals.08150b8d-a6ab-4466-a7b2-c1087e713c51.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_wheelMoves.intervals.08150b8d-a6ab-4466-a7b2-c1087e713c51.npy
|                    |    ├─ _ibl_wheelMoves.peakAmplitude.8662d859-adc1-44dd-8120-d5a2ced585df.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/_ibl_wheelMoves.peakAmplitude.8662d859-adc1-44dd-8120-d5a2ced585df.npy
|                    |    ├─ probe00
|                    |    |    ├─ _kilosort_whitening.matrix.f229df73-2b61-497c-bc6d-185e7f2d1515.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/_kilosort_whitening.matrix.f229df73-2b61-497c-bc6d-185e7f2d1515.npy
|                    |    |    ├─ _phy_spikes_subset.channels.955fb963-0525-4ae3-8177-62eb7e2af276.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/_phy_spikes_subset.channels.955fb963-0525-4ae3-8177-62eb7e2af276.npy
|                    |    |    ├─ _phy_spikes_subset.spikes.ab25435e-3839-4d87-aae5-6a1676ef3f28.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/_phy_spikes_subset.spikes.ab25435e-3839-4d87-aae5-6a1676ef3f28.npy
|                    |    |    ├─ _phy_spikes_subset.waveforms.768421cf-aba2-4f7a-96bc-f26cba4badbf.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/_phy_spikes_subset.waveforms.768421cf-aba2-4f7a-96bc-f26cba4badbf.npy
|                    |    |    ├─ channels.brainLocationIds_ccf_2017.474bc31b-4752-494d-b2c8-d23f08d86f6e.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/channels.brainLocationIds_ccf_2017.474bc31b-4752-494d-b2c8-d23f08d86f6e.npy
|                    |    |    ├─ channels.localCoordinates.526e6c4b-5b00-43b1-aa48-1f1028bc41ad.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/channels.localCoordinates.526e6c4b-5b00-43b1-aa48-1f1028bc41ad.npy
|                    |    |    ├─ channels.mlapdv.b3a4651a-e3b0-4e1a-8853-67de8e3e19b1.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/channels.mlapdv.b3a4651a-e3b0-4e1a-8853-67de8e3e19b1.npy
|                    |    |    ├─ channels.rawInd.167e2841-8e3c-4cf0-92af-b46c3b540ff4.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/channels.rawInd.167e2841-8e3c-4cf0-92af-b46c3b540ff4.npy
|                    |    |    ├─ clusters.amps.b07e52eb-ac25-4131-84ab-bf2f58735b62.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.amps.b07e52eb-ac25-4131-84ab-bf2f58735b62.npy
|                    |    |    ├─ clusters.brainLocationAcronyms_ccf_2017.6a8a7567-7d3c-4303-87e7-0247fd718d23.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.brainLocationAcronyms_ccf_2017.6a8a7567-7d3c-4303-87e7-0247fd718d23.npy
|                    |    |    ├─ clusters.brainLocationIds_ccf_2017.105ffedc-d9a6-4ee0-941b-e4c895f9c042.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.brainLocationIds_ccf_2017.105ffedc-d9a6-4ee0-941b-e4c895f9c042.npy
|                    |    |    ├─ clusters.channels.efde1a72-ed6e-47f2-92ed-9e405fb183f7.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.channels.efde1a72-ed6e-47f2-92ed-9e405fb183f7.npy
|                    |    |    ├─ clusters.depths.3908c52b-b108-48f1-b98f-1ec7b6735342.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.depths.3908c52b-b108-48f1-b98f-1ec7b6735342.npy
|                    |    |    ├─ clusters.metrics.b1c8554f-97a8-4ab6-91be-2280ac2cdbe3.pqt -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.metrics.b1c8554f-97a8-4ab6-91be-2280ac2cdbe3.pqt
|                    |    |    ├─ clusters.mlapdv.9c74d851-b704-4673-8954-2b4dc85082f7.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.mlapdv.9c74d851-b704-4673-8954-2b4dc85082f7.npy
|                    |    |    ├─ clusters.peakToTrough.06b68df1-5b00-481f-9d2d-3e976f46c3d5.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.peakToTrough.06b68df1-5b00-481f-9d2d-3e976f46c3d5.npy
|                    |    |    ├─ clusters.uuids.6a94e649-d55f-41b0-a7b9-b0bdc9872a67.csv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.uuids.6a94e649-d55f-41b0-a7b9-b0bdc9872a67.csv
|                    |    |    ├─ clusters.waveforms.b201ffc2-c2ee-464e-8cea-0ced9a3d894e.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.waveforms.b201ffc2-c2ee-464e-8cea-0ced9a3d894e.npy
|                    |    |    ├─ clusters.waveformsChannels.6746c3de-efb4-44a5-86e8-367637ce9225.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/clusters.waveformsChannels.6746c3de-efb4-44a5-86e8-367637ce9225.npy
|                    |    |    ├─ spikes.amps.eb7b95aa-ef46-49e7-b45e-bd491e5d460f.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.amps.eb7b95aa-ef46-49e7-b45e-bd491e5d460f.npy
|                    |    |    ├─ spikes.clusters.c4d3e959-b163-424f-8f45-ba2234f9acf1.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.clusters.c4d3e959-b163-424f-8f45-ba2234f9acf1.npy
|                    |    |    ├─ spikes.depths.d4e7ca4f-4cd9-4749-bab2-c4aca66c9bd3.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.depths.d4e7ca4f-4cd9-4749-bab2-c4aca66c9bd3.npy
|                    |    |    ├─ spikes.samples.ad534eec-abad-4bb1-b0b5-c0648bfc0a97.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.samples.ad534eec-abad-4bb1-b0b5-c0648bfc0a97.npy
|                    |    |    ├─ spikes.templates.81f0b888-ed61-4529-b940-fb9db5da0415.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.templates.81f0b888-ed61-4529-b940-fb9db5da0415.npy
|                    |    |    ├─ spikes.times.ba2c983c-2ae6-4a35-afe5-e17fb4ac94bb.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/spikes.times.ba2c983c-2ae6-4a35-afe5-e17fb4ac94bb.npy
|                    |    |    ├─ templates.amps.ce123733-e6f1-4e67-96bb-7aff770a88dc.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/templates.amps.ce123733-e6f1-4e67-96bb-7aff770a88dc.npy
|                    |    |    ├─ templates.waveforms.1d30cbec-a6bd-4244-998c-3da2fb93d106.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/templates.waveforms.1d30cbec-a6bd-4244-998c-3da2fb93d106.npy
|                    |    |    ├─  templates.waveformsChannels.0716caf7-5cd9-4ca9-8726-d53a017e03a1.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probe00/templates.waveformsChannels.0716caf7-5cd9-4ca9-8726-d53a017e03a1.npy
|                    |    ├─ probes.description.82237144-41bb-4e7f-9ef4-cabda4381d9f.json -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probes.description.82237144-41bb-4e7f-9ef4-cabda4381d9f.json
|                    |    ├─  probes.trajectory.a439c2bc-dc54-456e-9918-c24579ec8664.json -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/alf/probes.trajectory.a439c2bc-dc54-456e-9918-c24579ec8664.json
|                    ├─ raw_behavior_data
|                    |    ├─ _iblrig_ambientSensorData.raw.9568e7ba-78fb-4077-8732-3e7357bf79c1.jsonable -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_ambientSensorData.raw.9568e7ba-78fb-4077-8732-3e7357bf79c1.jsonable
|                    |    ├─ _iblrig_codeFiles.raw.e177d8c3-ae90-4e9a-b2ce-ccbf11e3ae4a.zip -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_codeFiles.raw.e177d8c3-ae90-4e9a-b2ce-ccbf11e3ae4a.zip
|                    |    ├─ _iblrig_encoderEvents.raw.4c4c9533-35e9-4981-b99d-405f51f30b60.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_encoderEvents.raw.4c4c9533-35e9-4981-b99d-405f51f30b60.ssv
|                    |    ├─ _iblrig_encoderPositions.raw.38a57dcb-353b-4b5b-ae48-17873a02f2a3.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_encoderPositions.raw.38a57dcb-353b-4b5b-ae48-17873a02f2a3.ssv
|                    |    ├─ _iblrig_encoderTrialInfo.raw.5311e0b6-bc6f-4124-847f-38e6b1d99f65.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_encoderTrialInfo.raw.5311e0b6-bc6f-4124-847f-38e6b1d99f65.ssv
|                    |    ├─ _iblrig_stimPositionScreen.raw.eda81210-00b6-4464-9727-7b442ff6e310.csv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_stimPositionScreen.raw.eda81210-00b6-4464-9727-7b442ff6e310.csv
|                    |    ├─ _iblrig_taskData.raw.50f9242c-52a3-44b5-800a-c495879251fa.jsonable -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_taskData.raw.50f9242c-52a3-44b5-800a-c495879251fa.jsonable
|                    |    ├─  _iblrig_taskSettings.raw.a558cebc-4737-4c93-bd9d-5f2f45b3aae1.json -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_behavior_data/_iblrig_taskSettings.raw.a558cebc-4737-4c93-bd9d-5f2f45b3aae1.json
|                    ├─ raw_ephys_data
|                    |    ├─ probe00
|                    |    |    ├─ _iblqc_ephysSpectralDensityAP.freqs.6ee05e99-5e18-4ae8-a6ad-2b51dce5ac9c.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityAP.freqs.6ee05e99-5e18-4ae8-a6ad-2b51dce5ac9c.npy
|                    |    |    ├─ _iblqc_ephysSpectralDensityAP.power.3142b721-8f85-41f6-ba87-3cfbeec5043e.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityAP.power.3142b721-8f85-41f6-ba87-3cfbeec5043e.npy
|                    |    |    ├─ _iblqc_ephysSpectralDensityLF.freqs.a41ced3a-405b-4a42-b319-811a1bf296f4.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityLF.freqs.a41ced3a-405b-4a42-b319-811a1bf296f4.npy
|                    |    |    ├─ _iblqc_ephysSpectralDensityLF.power.316f1aed-b85d-40de-8883-d0c351cc7453.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityLF.power.316f1aed-b85d-40de-8883-d0c351cc7453.npy
|                    |    |    ├─ _iblqc_ephysTimeRmsAP.rms.e433534f-d5a2-4ca0-aa33-e1ef18091122.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsAP.rms.e433534f-d5a2-4ca0-aa33-e1ef18091122.npy
|                    |    |    ├─ _iblqc_ephysTimeRmsAP.timestamps.0cdf2c43-9bcd-4cdc-9145-497d9fb83696.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsAP.timestamps.0cdf2c43-9bcd-4cdc-9145-497d9fb83696.npy
|                    |    |    ├─ _iblqc_ephysTimeRmsLF.rms.30c65edd-24dd-404d-89cf-654015856587.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsLF.rms.30c65edd-24dd-404d-89cf-654015856587.npy
|                    |    |    ├─ _iblqc_ephysTimeRmsLF.timestamps.614d9333-ff4c-4c97-b26e-66f81d2263ff.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsLF.timestamps.614d9333-ff4c-4c97-b26e-66f81d2263ff.npy
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.ap.0e7b6472-f264-4eca-8adf-6c7b84f69436.cbin -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.ap.0e7b6472-f264-4eca-8adf-6c7b84f69436.cbin
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.ap.1b57ddc4-9edd-49ab-9965-389ec8974e23.meta -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.ap.1b57ddc4-9edd-49ab-9965-389ec8974e23.meta
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.ap.363863a0-436a-47a0-9411-34a711e3a5ee.ch -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.ap.363863a0-436a-47a0-9411-34a711e3a5ee.ch
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.lf.31f683ce-76fe-45c8-a362-4330efe7f2f2.ch -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.lf.31f683ce-76fe-45c8-a362-4330efe7f2f2.ch
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.lf.e10cb66a-e2e4-438b-acc1-55e732f5d89e.cbin -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.lf.e10cb66a-e2e4-438b-acc1-55e732f5d89e.cbin
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.lf.e9da6334-29b6-468e-9315-84a140965452.meta -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.lf.e9da6334-29b6-468e-9315-84a140965452.meta
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.sync.33cd051a-32af-43c4-b789-6b73fbecaa56.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.sync.33cd051a-32af-43c4-b789-6b73fbecaa56.npy
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.timestamps.f97491b5-736d-415d-b009-1bdcfb7db669.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.timestamps.f97491b5-736d-415d-b009-1bdcfb7db669.npy
|                    |    |    ├─ _spikeglx_ephysData_g0_t0.imec.wiring.51c89626-e1d7-4847-b8c4-b630c23cdea1.json -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec.wiring.51c89626-e1d7-4847-b8c4-b630c23cdea1.json
|                    |    |    ├─ _spikeglx_ephysData_probe00_g0
|                    |    |    |    ├─ _spikeglx_sync.channels._spikeglx_ephysData_probe00_g0.1ee0bfb9-7e48-4922-9704-01019c0e0341.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_probe00_g0/_spikeglx_sync.channels._spikeglx_ephysData_probe00_g0.1ee0bfb9-7e48-4922-9704-01019c0e0341.npy
|                    |    |    |    ├─ _spikeglx_sync.polarities._spikeglx_ephysData_probe00_g0.e9a3e63b-85eb-4545-a102-103969d56ddb.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_probe00_g0/_spikeglx_sync.polarities._spikeglx_ephysData_probe00_g0.e9a3e63b-85eb-4545-a102-103969d56ddb.npy
|                    |    |    |    ├─  _spikeglx_sync.times._spikeglx_ephysData_probe00_g0.76910106-84c3-44b0-8409-2f82dbcd9fb5.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_ephysData_probe00_g0/_spikeglx_sync.times._spikeglx_ephysData_probe00_g0.76910106-84c3-44b0-8409-2f82dbcd9fb5.npy
|                    |    |    ├─ _spikeglx_sync.channels.probe00.68e99a68-1aee-4a81-b37c-c4917b6be8cd.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_sync.channels.probe00.68e99a68-1aee-4a81-b37c-c4917b6be8cd.npy
|                    |    |    ├─ _spikeglx_sync.polarities.probe00.97f18dae-c701-4996-b49f-b3abdcb394d1.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_sync.polarities.probe00.97f18dae-c701-4996-b49f-b3abdcb394d1.npy
|                    |    |    ├─  _spikeglx_sync.times.probe00.1143267d-c812-4939-8ba4-dde7c7584668.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe00/_spikeglx_sync.times.probe00.1143267d-c812-4939-8ba4-dde7c7584668.npy
|                    |    ├─  probe01
|                    |        ├─  _spikeglx_ephysData_probe01_g0
|                    |            ├─ _spikeglx_sync.channels._spikeglx_ephysData_probe01_g0.b4f84257-c14d-49bf-be6e-610d2b1c4fdd.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe01/_spikeglx_ephysData_probe01_g0/_spikeglx_sync.channels._spikeglx_ephysData_probe01_g0.b4f84257-c14d-49bf-be6e-610d2b1c4fdd.npy
|                    |            ├─ _spikeglx_sync.polarities._spikeglx_ephysData_probe01_g0.9cc27278-e924-4076-a400-004f140e18d0.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe01/_spikeglx_ephysData_probe01_g0/_spikeglx_sync.polarities._spikeglx_ephysData_probe01_g0.9cc27278-e924-4076-a400-004f140e18d0.npy
|                    |            ├─  _spikeglx_sync.times._spikeglx_ephysData_probe01_g0.c4526930-17e3-4f62-9bcd-f3619ddd793c.npy -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_ephys_data/probe01/_spikeglx_ephysData_probe01_g0/_spikeglx_sync.times._spikeglx_ephysData_probe01_g0.c4526930-17e3-4f62-9bcd-f3619ddd793c.npy
|                    ├─ raw_video_data
|                    |    ├─ _iblrig_bodyCamera.raw.f1b7f563-6569-4b36-9a60-57fedc4b4a2a.mp4 -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_bodyCamera.raw.f1b7f563-6569-4b36-9a60-57fedc4b4a2a.mp4
|                    |    ├─ _iblrig_bodyCamera.timestamps.b56af44c-3992-4a5a-a271-87e9c5a94cce.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_bodyCamera.timestamps.b56af44c-3992-4a5a-a271-87e9c5a94cce.ssv
|                    |    ├─ _iblrig_leftCamera.raw.e30d84a2-1445-419d-ba5b-00ef72613156.mp4 -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_leftCamera.raw.e30d84a2-1445-419d-ba5b-00ef72613156.mp4
|                    |    ├─ _iblrig_leftCamera.timestamps.d6c1d390-675b-4391-bbb5-88bf050690bf.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_leftCamera.timestamps.d6c1d390-675b-4391-bbb5-88bf050690bf.ssv
|                    |    ├─ _iblrig_rightCamera.raw.110f45f8-7854-4747-ac75-63c0f1a6d324.mp4 -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_rightCamera.raw.110f45f8-7854-4747-ac75-63c0f1a6d324.mp4
|                    |    ├─  _iblrig_rightCamera.timestamps.a2b89de4-04da-40bc-98de-5fce554c6fa0.ssv -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/raw_video_data/_iblrig_rightCamera.timestamps.a2b89de4-04da-40bc-98de-5fce554c6fa0.ssv
|                    ├─  spike_sorters
|                        ├─  ks2_matlab
|                            ├─  probe00
|                                ├─  _kilosort_raw.output.433df34b-bfa5-4a82-986b-d8a96752e101.tar -> /mnt/ibl/churchlandlab/Subjects/CSHL049/2020-01-08/001/spike_sorters/ks2_matlab/probe00/_kilosort_raw.output.433df34b-bfa5-4a82-986b-d8a96752e101.tar
├─ cortexlab
|    ├─  Subjects
|        ├─  KS023
|            ├─  2019-12-10
|                ├─  001
|                    ├─ alf
|                    |    ├─ _ibl_bodyCamera.dlc.bb5795d7-be89-4f57-9e58-034d43610c47.pqt -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_bodyCamera.dlc.bb5795d7-be89-4f57-9e58-034d43610c47.pqt
|                    |    ├─ _ibl_bodyCamera.times.5b807b18-202c-4fa8-89a2-b92dd707b5cf.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_bodyCamera.times.5b807b18-202c-4fa8-89a2-b92dd707b5cf.npy
|                    |    ├─ _ibl_leftCamera.dlc.d79a914f-0613-4ac3-82fe-1f8d66aa4633.pqt -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_leftCamera.dlc.d79a914f-0613-4ac3-82fe-1f8d66aa4633.pqt
|                    |    ├─ _ibl_leftCamera.times.a6007758-ef26-4cf0-9246-c3a7de1ecac9.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_leftCamera.times.a6007758-ef26-4cf0-9246-c3a7de1ecac9.npy
|                    |    ├─ _ibl_rightCamera.dlc.868a3954-7847-4fcb-84e9-8479da319c39.pqt -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_rightCamera.dlc.868a3954-7847-4fcb-84e9-8479da319c39.pqt
|                    |    ├─ _ibl_rightCamera.times.9c31bb81-58be-47ef-8654-312798b2de1b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_rightCamera.times.9c31bb81-58be-47ef-8654-312798b2de1b.npy
|                    |    ├─ _ibl_trials.choice.d73f567a-5799-4051-9bc8-6f0fd6bb478b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.choice.d73f567a-5799-4051-9bc8-6f0fd6bb478b.npy
|                    |    ├─ _ibl_trials.contrastLeft.d078bfc8-214d-4682-8621-390ad74dd6d5.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.contrastLeft.d078bfc8-214d-4682-8621-390ad74dd6d5.npy
|                    |    ├─ _ibl_trials.contrastRight.63aa7dea-1ee2-4a0c-88bc-00b5cba6b8b0.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.contrastRight.63aa7dea-1ee2-4a0c-88bc-00b5cba6b8b0.npy
|                    |    ├─ _ibl_trials.feedbackType.c8cd43a7-b443-4342-8c37-aa93a2067447.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.feedbackType.c8cd43a7-b443-4342-8c37-aa93a2067447.npy
|                    |    ├─ _ibl_trials.feedback_times.6b94f568-9bb6-417c-9423-a84559f403d5.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.feedback_times.6b94f568-9bb6-417c-9423-a84559f403d5.npy
|                    |    ├─ _ibl_trials.firstMovement_times.0bc9607d-0a72-4c5c-8b9d-e239a575ff67.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.firstMovement_times.0bc9607d-0a72-4c5c-8b9d-e239a575ff67.npy
|                    |    ├─ _ibl_trials.goCueTrigger_times.16c81eaf-a032-49cd-9823-09c0c7350fd2.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.goCueTrigger_times.16c81eaf-a032-49cd-9823-09c0c7350fd2.npy
|                    |    ├─ _ibl_trials.goCue_times.69236a5d-1e4a-4bea-85e9-704492756848.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.goCue_times.69236a5d-1e4a-4bea-85e9-704492756848.npy
|                    |    ├─ _ibl_trials.intervals.d11d7b33-3a96-4ea6-849f-5448a97d3fc1.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.intervals.d11d7b33-3a96-4ea6-849f-5448a97d3fc1.npy
|                    |    ├─ _ibl_trials.intervals_bpod.4ee1110f-3ff3-4e26-87b0-41b687f75ce3.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.intervals_bpod.4ee1110f-3ff3-4e26-87b0-41b687f75ce3.npy
|                    |    ├─ _ibl_trials.itiDuration.b77d2665-876e-41e7-ac57-aa2854c5d5cd.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.itiDuration.b77d2665-876e-41e7-ac57-aa2854c5d5cd.npy
|                    |    ├─ _ibl_trials.probabilityLeft.91f08c6d-7ee0-487e-adf5-9c751769af06.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.probabilityLeft.91f08c6d-7ee0-487e-adf5-9c751769af06.npy
|                    |    ├─ _ibl_trials.response_times.2f4cc220-55b9-4fb3-9692-9aaa5362288f.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.response_times.2f4cc220-55b9-4fb3-9692-9aaa5362288f.npy
|                    |    ├─ _ibl_trials.rewardVolume.fceb8cfe-77b4-4177-a6af-44fbf51b33d0.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.rewardVolume.fceb8cfe-77b4-4177-a6af-44fbf51b33d0.npy
|                    |    ├─ _ibl_trials.stimOff_times.e1793e9d-cd96-4cb6-9fd7-a6b662c41971.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.stimOff_times.e1793e9d-cd96-4cb6-9fd7-a6b662c41971.npy
|                    |    ├─ _ibl_trials.stimOn_times.c14d8683-3706-4e44-a8d2-cd0e2bfd4579.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_trials.stimOn_times.c14d8683-3706-4e44-a8d2-cd0e2bfd4579.npy
|                    |    ├─ _ibl_wheel.position.c027a616-e68d-491b-bfa6-ed334e5a24d4.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_wheel.position.c027a616-e68d-491b-bfa6-ed334e5a24d4.npy
|                    |    ├─ _ibl_wheel.times.801c9ecd-a9a6-40a3-b64b-7fa189a8b5a3.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_wheel.times.801c9ecd-a9a6-40a3-b64b-7fa189a8b5a3.npy
|                    |    ├─ _ibl_wheel.timestamps.3a8cd82f-d5ad-4ac9-b735-a124059c9f52.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_wheel.timestamps.3a8cd82f-d5ad-4ac9-b735-a124059c9f52.npy
|                    |    ├─ _ibl_wheelMoves.intervals.24620dbe-dc33-4b1d-b5fb-6fd387874994.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_wheelMoves.intervals.24620dbe-dc33-4b1d-b5fb-6fd387874994.npy
|                    |    ├─ _ibl_wheelMoves.peakAmplitude.dfa5d232-b6cc-426b-b282-d71af133a58c.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/_ibl_wheelMoves.peakAmplitude.dfa5d232-b6cc-426b-b282-d71af133a58c.npy
|                    |    ├─ probe01
|                    |    |    ├─ _kilosort_whitening.matrix.7e2b87e2-fc7a-4566-b5eb-2a0b9395c5fb.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/_kilosort_whitening.matrix.7e2b87e2-fc7a-4566-b5eb-2a0b9395c5fb.npy
|                    |    |    ├─ _phy_spikes_subset.channels.8431a704-bddb-46c1-beed-6c2a24dc7eac.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/_phy_spikes_subset.channels.8431a704-bddb-46c1-beed-6c2a24dc7eac.npy
|                    |    |    ├─ _phy_spikes_subset.spikes.ea83bcd5-3b2e-4b71-8afe-200c787aedcb.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/_phy_spikes_subset.spikes.ea83bcd5-3b2e-4b71-8afe-200c787aedcb.npy
|                    |    |    ├─ _phy_spikes_subset.waveforms.ee21069a-45ef-4719-8e1e-2da14febb847.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/_phy_spikes_subset.waveforms.ee21069a-45ef-4719-8e1e-2da14febb847.npy
|                    |    |    ├─ channels.brainLocationIds_ccf_2017.4a1500c2-60f3-418f-afa2-c752bb1890f0.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/channels.brainLocationIds_ccf_2017.4a1500c2-60f3-418f-afa2-c752bb1890f0.npy
|                    |    |    ├─ channels.localCoordinates.c4f4dcd2-c304-4028-846c-a900b7836097.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/channels.localCoordinates.c4f4dcd2-c304-4028-846c-a900b7836097.npy
|                    |    |    ├─ channels.mlapdv.681e9b3c-125f-4154-b1e1-ef276535652b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/channels.mlapdv.681e9b3c-125f-4154-b1e1-ef276535652b.npy
|                    |    |    ├─ channels.rawInd.b60c6fb3-4e63-4266-b67c-40ca4ed372a8.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/channels.rawInd.b60c6fb3-4e63-4266-b67c-40ca4ed372a8.npy
|                    |    |    ├─ clusters.amps.1c8b1144-dc2a-49bb-9593-c9d07c959353.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.amps.1c8b1144-dc2a-49bb-9593-c9d07c959353.npy
|                    |    |    ├─ clusters.brainLocationAcronyms_ccf_2017.3a74efb6-11ec-473d-8669-4528c078cc8b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.brainLocationAcronyms_ccf_2017.3a74efb6-11ec-473d-8669-4528c078cc8b.npy
|                    |    |    ├─ clusters.brainLocationIds_ccf_2017.4e8a7ed9-cea6-46e7-9dbe-05e92e2dd47c.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.brainLocationIds_ccf_2017.4e8a7ed9-cea6-46e7-9dbe-05e92e2dd47c.npy
|                    |    |    ├─ clusters.channels.43ec27b3-3d32-4aef-9947-852fab986033.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.channels.43ec27b3-3d32-4aef-9947-852fab986033.npy
|                    |    |    ├─ clusters.depths.287b97f9-da17-4660-9858-e637f32eed06.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.depths.287b97f9-da17-4660-9858-e637f32eed06.npy
|                    |    |    ├─ clusters.metrics.f61d4de7-8b48-4d65-b030-e539979a0980.pqt -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.metrics.f61d4de7-8b48-4d65-b030-e539979a0980.pqt
|                    |    |    ├─ clusters.mlapdv.905dcfe6-5edb-48f7-b9b0-c6cd0fa4cca9.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.mlapdv.905dcfe6-5edb-48f7-b9b0-c6cd0fa4cca9.npy
|                    |    |    ├─ clusters.peakToTrough.45dd0bbc-72c3-46c8-a64f-7b3027630b39.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.peakToTrough.45dd0bbc-72c3-46c8-a64f-7b3027630b39.npy
|                    |    |    ├─ clusters.uuids.a4d697b5-0517-44b1-9e8f-2bdda98a6959.csv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.uuids.a4d697b5-0517-44b1-9e8f-2bdda98a6959.csv
|                    |    |    ├─ clusters.waveforms.5e24f2a8-285a-49a6-9c8f-dbd5fa8f90d4.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.waveforms.5e24f2a8-285a-49a6-9c8f-dbd5fa8f90d4.npy
|                    |    |    ├─ clusters.waveformsChannels.e23da06b-650d-4fb3-b82a-c007d6f89e0d.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/clusters.waveformsChannels.e23da06b-650d-4fb3-b82a-c007d6f89e0d.npy
|                    |    |    ├─ spikes.amps.17a7a1bb-00dd-4331-a6da-a5241bb91c63.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.amps.17a7a1bb-00dd-4331-a6da-a5241bb91c63.npy
|                    |    |    ├─ spikes.clusters.2e3a207d-6b7a-41b3-80b9-d759a6557b55.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.clusters.2e3a207d-6b7a-41b3-80b9-d759a6557b55.npy
|                    |    |    ├─ spikes.depths.9cbed712-3d4e-44d4-8ec8-f915a884e667.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.depths.9cbed712-3d4e-44d4-8ec8-f915a884e667.npy
|                    |    |    ├─ spikes.samples.7b7969a6-23ae-43c0-bb71-d4b3a7be489e.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.samples.7b7969a6-23ae-43c0-bb71-d4b3a7be489e.npy
|                    |    |    ├─ spikes.templates.8cea5059-d98f-42fe-8a83-69be9b005e4d.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.templates.8cea5059-d98f-42fe-8a83-69be9b005e4d.npy
|                    |    |    ├─ spikes.times.99ed1a2d-bb18-4f86-92f3-23a15b7d9972.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/spikes.times.99ed1a2d-bb18-4f86-92f3-23a15b7d9972.npy
|                    |    |    ├─ templates.amps.9029d522-cf24-4253-a26b-1f5d8001107b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/templates.amps.9029d522-cf24-4253-a26b-1f5d8001107b.npy
|                    |    |    ├─ templates.waveforms.96fbf47d-576a-4996-ae55-c6cae63a0a81.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/templates.waveforms.96fbf47d-576a-4996-ae55-c6cae63a0a81.npy
|                    |    |    ├─  templates.waveformsChannels.cbe58889-6625-4902-80e8-94df30b94824.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probe01/templates.waveformsChannels.cbe58889-6625-4902-80e8-94df30b94824.npy
|                    |    ├─ probes.description.066fb5b0-1f51-4e22-a398-b768dfdd0971.json -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probes.description.066fb5b0-1f51-4e22-a398-b768dfdd0971.json
|                    |    ├─  probes.trajectory.cc05625d-c1f5-4b68-9a89-f1e8c8c3927e.json -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/alf/probes.trajectory.cc05625d-c1f5-4b68-9a89-f1e8c8c3927e.json
|                    ├─ raw_behavior_data
|                    |    ├─ _iblrig_ambientSensorData.raw.fe3e4584-d1ae-4f11-9bed-ecca6903411e.jsonable -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_ambientSensorData.raw.fe3e4584-d1ae-4f11-9bed-ecca6903411e.jsonable
|                    |    ├─ _iblrig_codeFiles.raw.9e5175cb-3f7b-4f7b-85d4-87bf8983dde0.zip -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_codeFiles.raw.9e5175cb-3f7b-4f7b-85d4-87bf8983dde0.zip
|                    |    ├─ _iblrig_encoderEvents.raw.b420905d-b421-456a-8ef1-122f0b622975.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_encoderEvents.raw.b420905d-b421-456a-8ef1-122f0b622975.ssv
|                    |    ├─ _iblrig_encoderPositions.raw.1e3da02b-1745-4e4e-93b5-acd8648836e2.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_encoderPositions.raw.1e3da02b-1745-4e4e-93b5-acd8648836e2.ssv
|                    |    ├─ _iblrig_encoderTrialInfo.raw.7d36b813-0dd0-44df-a9cc-8e445132beb1.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_encoderTrialInfo.raw.7d36b813-0dd0-44df-a9cc-8e445132beb1.ssv
|                    |    ├─ _iblrig_taskData.raw.de1e163d-edf5-4955-9a47-a13d9a9b9219.jsonable -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_taskData.raw.de1e163d-edf5-4955-9a47-a13d9a9b9219.jsonable
|                    |    ├─  _iblrig_taskSettings.raw.282dde2a-fd92-4b5a-8d2d-98dd6dfabed5.json -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_behavior_data/_iblrig_taskSettings.raw.282dde2a-fd92-4b5a-8d2d-98dd6dfabed5.json
|                    ├─ raw_ephys_data
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.424e4909-a9ab-4b29-a55f-a47bb564442d.meta -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.424e4909-a9ab-4b29-a55f-a47bb564442d.meta
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.eb36952d-5f90-4751-bfaf-5ec60fe2a750.cbin -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.eb36952d-5f90-4751-bfaf-5ec60fe2a750.cbin
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.ed4b62a1-8705-4b67-837d-b72ab39f0625.ch -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.ed4b62a1-8705-4b67-837d-b72ab39f0625.ch
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.wiring.1360f768-077c-4b21-8143-3b5a0f67f0f3.json -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.wiring.1360f768-077c-4b21-8143-3b5a0f67f0f3.json
|                    |    ├─ _spikeglx_sync.channels.a5d7dc10-e437-47ec-97d8-1030dc35b5bb.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_sync.channels.a5d7dc10-e437-47ec-97d8-1030dc35b5bb.npy
|                    |    ├─ _spikeglx_sync.polarities.f99b6d20-c403-4c41-b00e-4f10a3a2201c.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_sync.polarities.f99b6d20-c403-4c41-b00e-4f10a3a2201c.npy
|                    |    ├─ _spikeglx_sync.times.3efa4da0-9206-4617-b311-93457f16e69d.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/_spikeglx_sync.times.3efa4da0-9206-4617-b311-93457f16e69d.npy
|                    |    ├─  probe01
|                    |        ├─ _iblqc_ephysSpectralDensityAP.freqs.0ebde5c8-a615-4bbe-a838-6b75d881b025.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityAP.freqs.0ebde5c8-a615-4bbe-a838-6b75d881b025.npy
|                    |        ├─ _iblqc_ephysSpectralDensityAP.power.f665f47f-07fe-4cad-9c5d-842a3d205e99.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityAP.power.f665f47f-07fe-4cad-9c5d-842a3d205e99.npy
|                    |        ├─ _iblqc_ephysSpectralDensityLF.freqs.2f721b84-6fa1-463b-9d61-f3c8024b3fb4.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityLF.freqs.2f721b84-6fa1-463b-9d61-f3c8024b3fb4.npy
|                    |        ├─ _iblqc_ephysSpectralDensityLF.power.8643216d-448d-4335-86cf-03bc9fa7bd84.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityLF.power.8643216d-448d-4335-86cf-03bc9fa7bd84.npy
|                    |        ├─ _iblqc_ephysTimeRmsAP.rms.c3d24b08-d6aa-41cf-a6c1-cc81cc63258a.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsAP.rms.c3d24b08-d6aa-41cf-a6c1-cc81cc63258a.npy
|                    |        ├─ _iblqc_ephysTimeRmsAP.timestamps.4cb77450-2746-48c2-8ef4-cb7c3d4b8193.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsAP.timestamps.4cb77450-2746-48c2-8ef4-cb7c3d4b8193.npy
|                    |        ├─ _iblqc_ephysTimeRmsLF.rms.945f72c2-a12a-45f6-9bc4-f6202c53553e.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsLF.rms.945f72c2-a12a-45f6-9bc4-f6202c53553e.npy
|                    |        ├─ _iblqc_ephysTimeRmsLF.timestamps.d828d3d0-152c-46e3-9a17-d2108ab6fb0b.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsLF.timestamps.d828d3d0-152c-46e3-9a17-d2108ab6fb0b.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.44f643a9-2268-44cc-abe4-7f0c18f66ef8.cbin -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.44f643a9-2268-44cc-abe4-7f0c18f66ef8.cbin
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.9c4e4632-c0c6-498b-8cb9-6ecb1f606653.ch -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.9c4e4632-c0c6-498b-8cb9-6ecb1f606653.ch
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.bd522d3b-e190-45bb-9c39-e22ac00f3d8f.meta -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.bd522d3b-e190-45bb-9c39-e22ac00f3d8f.meta
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.02607687-d634-4e8e-9491-e1efafa4d1db.meta -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.02607687-d634-4e8e-9491-e1efafa4d1db.meta
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.b393396f-4e25-43fa-a8e6-9369c2e650fb.ch -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.b393396f-4e25-43fa-a8e6-9369c2e650fb.ch
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.d035699e-a090-4172-a4e1-ad747ca9f7ee.cbin -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.d035699e-a090-4172-a4e1-ad747ca9f7ee.cbin
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.sync.9e198738-1544-482b-a3f0-e0912bd08f40.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.sync.9e198738-1544-482b-a3f0-e0912bd08f40.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.timestamps.b134482b-569b-4f9d-b953-565f9ed1f472.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.timestamps.b134482b-569b-4f9d-b953-565f9ed1f472.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.wiring.d9b874b3-eb5e-47e8-ac3b-4dec01c8ea28.json -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.wiring.d9b874b3-eb5e-47e8-ac3b-4dec01c8ea28.json
|                    |        ├─ _spikeglx_sync.channels.probe01.bb5c370c-547b-439a-a0e5-2d4558013dca.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_sync.channels.probe01.bb5c370c-547b-439a-a0e5-2d4558013dca.npy
|                    |        ├─ _spikeglx_sync.polarities.probe01.5b30d3d8-2e2b-429b-85bc-13e7b54b36ba.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_sync.polarities.probe01.5b30d3d8-2e2b-429b-85bc-13e7b54b36ba.npy
|                    |        ├─  _spikeglx_sync.times.probe01.7bca9fb7-81eb-4c80-bab4-f6461413d012.npy -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_ephys_data/probe01/_spikeglx_sync.times.probe01.7bca9fb7-81eb-4c80-bab4-f6461413d012.npy
|                    ├─ raw_video_data
|                    |    ├─ _iblrig_bodyCamera.raw.cd133c97-2780-458e-ad87-b99322619209.mp4 -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_bodyCamera.raw.cd133c97-2780-458e-ad87-b99322619209.mp4
|                    |    ├─ _iblrig_bodyCamera.timestamps.6166b1ba-17a0-45df-8d90-27ba6b3de35d.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_bodyCamera.timestamps.6166b1ba-17a0-45df-8d90-27ba6b3de35d.ssv
|                    |    ├─ _iblrig_leftCamera.raw.a0050b1d-2f18-48ed-9355-33319eaf559b.mp4 -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_leftCamera.raw.a0050b1d-2f18-48ed-9355-33319eaf559b.mp4
|                    |    ├─ _iblrig_leftCamera.timestamps.1d0ebf96-3ee1-4a41-adf9-18f486cd881c.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_leftCamera.timestamps.1d0ebf96-3ee1-4a41-adf9-18f486cd881c.ssv
|                    |    ├─ _iblrig_rightCamera.raw.b6ba1396-698c-40e9-969e-8e9804e84c6c.mp4 -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_rightCamera.raw.b6ba1396-698c-40e9-969e-8e9804e84c6c.mp4
|                    |    ├─  _iblrig_rightCamera.timestamps.a248c2f1-b3c5-4a9f-9f01-c168e82b978c.ssv -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/raw_video_data/_iblrig_rightCamera.timestamps.a248c2f1-b3c5-4a9f-9f01-c168e82b978c.ssv
|                    ├─  spike_sorters
|                        ├─  ks2_matlab
|                            ├─  probe01
|                                ├─  _kilosort_raw.output.f7ea52c8-3cbe-4c4f-9532-466f1991e50f.tar -> /mnt/ibl/cortexlab/Subjects/KS023/2019-12-10/001/spike_sorters/ks2_matlab/probe01/_kilosort_raw.output.f7ea52c8-3cbe-4c4f-9532-466f1991e50f.tar
├─ hoferlab
|    ├─  Subjects
|        ├─  SWC_043
|            ├─  2020-09-21
|                ├─  001
|                    ├─ alf
|                    |    ├─ _ibl_bodyCamera.dlc.21870f45-8954-4bdf-b4e3-12608b6fa570.pqt -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_bodyCamera.dlc.21870f45-8954-4bdf-b4e3-12608b6fa570.pqt
|                    |    ├─ _ibl_bodyCamera.times.e2723912-e6fd-45b7-b203-d2a18c46071a.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_bodyCamera.times.e2723912-e6fd-45b7-b203-d2a18c46071a.npy
|                    |    ├─ _ibl_leftCamera.dlc.dbb79c10-4832-4036-bf1a-93846515aa6f.pqt -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_leftCamera.dlc.dbb79c10-4832-4036-bf1a-93846515aa6f.pqt
|                    |    ├─ _ibl_leftCamera.times.08217c66-2f83-4747-ae17-04ea0f789aca.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_leftCamera.times.08217c66-2f83-4747-ae17-04ea0f789aca.npy
|                    |    ├─ _ibl_passiveGabor.table.aeb4c865-3f0c-49d2-aae3-f018eb9dace4.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_passiveGabor.table.aeb4c865-3f0c-49d2-aae3-f018eb9dace4.csv
|                    |    ├─ _ibl_passivePeriods.intervalsTable.66d5ede4-c4c5-44b1-a665-820ad0f0b7c8.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_passivePeriods.intervalsTable.66d5ede4-c4c5-44b1-a665-820ad0f0b7c8.csv
|                    |    ├─ _ibl_passiveRFM.times.9242bd1f-e1cd-4f78-87fd-47da609a50c3.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_passiveRFM.times.9242bd1f-e1cd-4f78-87fd-47da609a50c3.npy
|                    |    ├─ _ibl_passiveStims.table.992b9dc5-82cb-4b06-976d-fd489a1d4eb4.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_passiveStims.table.992b9dc5-82cb-4b06-976d-fd489a1d4eb4.csv
|                    |    ├─ _ibl_rightCamera.dlc.b15b3375-69c1-4963-aba8-fbd68832cdc3.pqt -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_rightCamera.dlc.b15b3375-69c1-4963-aba8-fbd68832cdc3.pqt
|                    |    ├─ _ibl_rightCamera.times.94a47981-0f30-4920-b83f-594b1d6f2e2b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_rightCamera.times.94a47981-0f30-4920-b83f-594b1d6f2e2b.npy
|                    |    ├─ _ibl_trials.choice.68fd21d9-18b8-4e6c-87f2-910b2047179b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.choice.68fd21d9-18b8-4e6c-87f2-910b2047179b.npy
|                    |    ├─ _ibl_trials.contrastLeft.2b8f3ebd-277c-4a61-83a1-c38fee79acd1.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.contrastLeft.2b8f3ebd-277c-4a61-83a1-c38fee79acd1.npy
|                    |    ├─ _ibl_trials.contrastRight.344cad48-f043-4f36-af10-cd706beb9d34.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.contrastRight.344cad48-f043-4f36-af10-cd706beb9d34.npy
|                    |    ├─ _ibl_trials.feedbackType.3029884a-7205-4f44-8491-eae7ae694170.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.feedbackType.3029884a-7205-4f44-8491-eae7ae694170.npy
|                    |    ├─ _ibl_trials.feedback_times.3ecaf927-1cfc-4c33-b0d8-0fa7a883e316.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.feedback_times.3ecaf927-1cfc-4c33-b0d8-0fa7a883e316.npy
|                    |    ├─ _ibl_trials.firstMovement_times.7735d675-8988-4d71-9647-df3b7acd694b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.firstMovement_times.7735d675-8988-4d71-9647-df3b7acd694b.npy
|                    |    ├─ _ibl_trials.goCueTrigger_times.850ed0ac-ead2-45aa-b437-dc110f84cd89.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.goCueTrigger_times.850ed0ac-ead2-45aa-b437-dc110f84cd89.npy
|                    |    ├─ _ibl_trials.goCue_times.de97c402-4f93-44da-93b6-5ba9eb20ba50.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.goCue_times.de97c402-4f93-44da-93b6-5ba9eb20ba50.npy
|                    |    ├─ _ibl_trials.intervals.bce466b6-0013-4da9-a1e5-abaa02b18705.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.intervals.bce466b6-0013-4da9-a1e5-abaa02b18705.npy
|                    |    ├─ _ibl_trials.intervals_bpod.6060983b-6231-4ae6-830d-971c68af29eb.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.intervals_bpod.6060983b-6231-4ae6-830d-971c68af29eb.npy
|                    |    ├─ _ibl_trials.probabilityLeft.64e043a9-d31e-4453-8d45-3a8ddb328078.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.probabilityLeft.64e043a9-d31e-4453-8d45-3a8ddb328078.npy
|                    |    ├─ _ibl_trials.response_times.a03853e8-6383-4ec7-926a-75e878b052db.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.response_times.a03853e8-6383-4ec7-926a-75e878b052db.npy
|                    |    ├─ _ibl_trials.rewardVolume.e8b14bca-bb27-4567-a63e-66e8d348c8f8.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.rewardVolume.e8b14bca-bb27-4567-a63e-66e8d348c8f8.npy
|                    |    ├─ _ibl_trials.stimOff_times.e06e6716-59cc-40cc-a6f7-e15eec1cadd5.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.stimOff_times.e06e6716-59cc-40cc-a6f7-e15eec1cadd5.npy
|                    |    ├─ _ibl_trials.stimOn_times.1807acee-005f-413f-b435-7cb4d3232bda.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_trials.stimOn_times.1807acee-005f-413f-b435-7cb4d3232bda.npy
|                    |    ├─ _ibl_wheel.position.67b3a4fb-29fc-40d2-a4fd-477689ba0aa2.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_wheel.position.67b3a4fb-29fc-40d2-a4fd-477689ba0aa2.npy
|                    |    ├─ _ibl_wheel.timestamps.53090473-9474-4a23-8cea-c5e062c6120e.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_wheel.timestamps.53090473-9474-4a23-8cea-c5e062c6120e.npy
|                    |    ├─ _ibl_wheelMoves.intervals.ab951a5f-662f-4ddd-a08b-669bd8c52af6.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_wheelMoves.intervals.ab951a5f-662f-4ddd-a08b-669bd8c52af6.npy
|                    |    ├─ _ibl_wheelMoves.peakAmplitude.36a7e6f6-fe06-449e-b66e-8abb159cb72a.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/_ibl_wheelMoves.peakAmplitude.36a7e6f6-fe06-449e-b66e-8abb159cb72a.npy
|                    |    ├─ probe00
|                    |    |    ├─ _kilosort_whitening.matrix.af8dd0e9-2057-4d2c-b47f-2598153f187d.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/_kilosort_whitening.matrix.af8dd0e9-2057-4d2c-b47f-2598153f187d.npy
|                    |    |    ├─ _phy_spikes_subset.channels.00c234a3-a4ff-4f97-a522-939d15528a45.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/_phy_spikes_subset.channels.00c234a3-a4ff-4f97-a522-939d15528a45.npy
|                    |    |    ├─ _phy_spikes_subset.spikes.582cd4c3-02b8-4121-84ba-f4611aa4dcfe.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/_phy_spikes_subset.spikes.582cd4c3-02b8-4121-84ba-f4611aa4dcfe.npy
|                    |    |    ├─ _phy_spikes_subset.waveforms.322e85c0-b5d8-4013-9db0-5f523a2a489c.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/_phy_spikes_subset.waveforms.322e85c0-b5d8-4013-9db0-5f523a2a489c.npy
|                    |    |    ├─ channels.localCoordinates.53ab50fe-b57d-4013-909f-05219e77b053.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/channels.localCoordinates.53ab50fe-b57d-4013-909f-05219e77b053.npy
|                    |    |    ├─ channels.rawInd.5327c66d-dab0-41b3-b180-3aa7d47d5303.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/channels.rawInd.5327c66d-dab0-41b3-b180-3aa7d47d5303.npy
|                    |    |    ├─ clusters.amps.cc9bf356-9ec2-4100-8256-4a0363d2085a.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.amps.cc9bf356-9ec2-4100-8256-4a0363d2085a.npy
|                    |    |    ├─ clusters.channels.0d0bad29-7f05-4825-8cf9-50d9b7dc83c3.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.channels.0d0bad29-7f05-4825-8cf9-50d9b7dc83c3.npy
|                    |    |    ├─ clusters.depths.cf745deb-4a45-418f-9871-6a51a6ec712d.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.depths.cf745deb-4a45-418f-9871-6a51a6ec712d.npy
|                    |    |    ├─ clusters.metrics.8091108f-a0d2-44e0-bf01-5c0a93de7844.pqt -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.metrics.8091108f-a0d2-44e0-bf01-5c0a93de7844.pqt
|                    |    |    ├─ clusters.peakToTrough.9314c967-4b92-421a-8956-3daaf5be1da7.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.peakToTrough.9314c967-4b92-421a-8956-3daaf5be1da7.npy
|                    |    |    ├─ clusters.uuids.3d9cbd53-fe3f-41ca-ae37-71936f5ca68f.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.uuids.3d9cbd53-fe3f-41ca-ae37-71936f5ca68f.csv
|                    |    |    ├─ clusters.waveforms.7fbebff5-8f6a-4b4b-aeba-c5a9118343db.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.waveforms.7fbebff5-8f6a-4b4b-aeba-c5a9118343db.npy
|                    |    |    ├─ clusters.waveformsChannels.6cd3b0c3-8d83-4367-b554-f90f8d505c0e.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/clusters.waveformsChannels.6cd3b0c3-8d83-4367-b554-f90f8d505c0e.npy
|                    |    |    ├─ spikes.amps.a51473f0-4139-4d01-9264-bea36db1789a.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.amps.a51473f0-4139-4d01-9264-bea36db1789a.npy
|                    |    |    ├─ spikes.clusters.854e2ec7-c974-4dcc-8dea-b0a6063febdf.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.clusters.854e2ec7-c974-4dcc-8dea-b0a6063febdf.npy
|                    |    |    ├─ spikes.depths.545f7a74-9a47-438b-8367-d715d70a3710.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.depths.545f7a74-9a47-438b-8367-d715d70a3710.npy
|                    |    |    ├─ spikes.samples.249fd743-3207-478f-923a-45749d92d87b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.samples.249fd743-3207-478f-923a-45749d92d87b.npy
|                    |    |    ├─ spikes.templates.25c2b0f4-6201-407d-8cf6-f892370a5a44.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.templates.25c2b0f4-6201-407d-8cf6-f892370a5a44.npy
|                    |    |    ├─ spikes.times.dd78976c-fc95-4221-83db-a034652b8867.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/spikes.times.dd78976c-fc95-4221-83db-a034652b8867.npy
|                    |    |    ├─ templates.amps.600b333b-030b-482f-a02f-0a8b90e73eab.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/templates.amps.600b333b-030b-482f-a02f-0a8b90e73eab.npy
|                    |    |    ├─ templates.waveforms.ffea1a62-dc7e-4d01-8f86-03801a88615f.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/templates.waveforms.ffea1a62-dc7e-4d01-8f86-03801a88615f.npy
|                    |    |    ├─  templates.waveformsChannels.3d1fc6f0-48bc-493e-834d-d1cf6a496255.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probe00/templates.waveformsChannels.3d1fc6f0-48bc-493e-834d-d1cf6a496255.npy
|                    |    ├─ probes.description.c4df1eea-c92c-479f-a907-41fa6e770094.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probes.description.c4df1eea-c92c-479f-a907-41fa6e770094.json
|                    |    ├─  probes.trajectory.84116a5c-131e-40a2-92d4-62c4aaae5c52.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/alf/probes.trajectory.84116a5c-131e-40a2-92d4-62c4aaae5c52.json
|                    ├─ raw_behavior_data
|                    |    ├─ _iblrig_ambientSensorData.raw.8164342b-3289-4d70-bb85-b205b4ffbcfd.jsonable -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_ambientSensorData.raw.8164342b-3289-4d70-bb85-b205b4ffbcfd.jsonable
|                    |    ├─ _iblrig_encoderEvents.raw.ca99fbcf-0d9c-45ac-9e40-913c7871fb6d.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_encoderEvents.raw.ca99fbcf-0d9c-45ac-9e40-913c7871fb6d.ssv
|                    |    ├─ _iblrig_encoderPositions.raw.10a1244b-b527-4e39-ad6b-e1f64a4c3902.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_encoderPositions.raw.10a1244b-b527-4e39-ad6b-e1f64a4c3902.ssv
|                    |    ├─ _iblrig_encoderTrialInfo.raw.40ef7f67-7d1b-4a4a-8729-b04284d9bb6f.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_encoderTrialInfo.raw.40ef7f67-7d1b-4a4a-8729-b04284d9bb6f.ssv
|                    |    ├─ _iblrig_micData.raw.fedbe9a1-0ed7-4c0b-b226-e0ef247b86f4.flac -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_micData.raw.fedbe9a1-0ed7-4c0b-b226-e0ef247b86f4.flac
|                    |    ├─ _iblrig_stimPositionScreen.raw.bb6bb56d-887c-4dc4-9a32-c13b4c92256e.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_stimPositionScreen.raw.bb6bb56d-887c-4dc4-9a32-c13b4c92256e.csv
|                    |    ├─ _iblrig_syncSquareUpdate.raw.f8b90888-b6cf-4462-beac-a467520e961a.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_syncSquareUpdate.raw.f8b90888-b6cf-4462-beac-a467520e961a.csv
|                    |    ├─ _iblrig_taskData.raw.7bcaf2fc-6cb0-45a4-9708-193904026721.jsonable -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_taskData.raw.7bcaf2fc-6cb0-45a4-9708-193904026721.jsonable
|                    |    ├─  _iblrig_taskSettings.raw.5c426c45-3e1f-4f90-b3f7-bca76c6e0725.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_behavior_data/_iblrig_taskSettings.raw.5c426c45-3e1f-4f90-b3f7-bca76c6e0725.json
|                    ├─ raw_ephys_data
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.55da0b2e-69d8-40d9-961a-d812b38876ba.cbin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.55da0b2e-69d8-40d9-961a-d812b38876ba.cbin
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.64924ee8-395e-41f8-ac07-c74f853a8671.meta -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.64924ee8-395e-41f8-ac07-c74f853a8671.meta
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.ae1ab148-520f-4003-91d0-2ff05480b191.ch -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.ae1ab148-520f-4003-91d0-2ff05480b191.ch
|                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.wiring.11914a2c-bf83-47b1-ab8a-b743663ac3c5.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.wiring.11914a2c-bf83-47b1-ab8a-b743663ac3c5.json
|                    |    ├─ _spikeglx_sync.channels.495dfc0f-3450-4f75-8629-055e16e053a3.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_sync.channels.495dfc0f-3450-4f75-8629-055e16e053a3.npy
|                    |    ├─ _spikeglx_sync.polarities.2e0f57b0-8fc9-4d08-b16d-6b9e4009deb5.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_sync.polarities.2e0f57b0-8fc9-4d08-b16d-6b9e4009deb5.npy
|                    |    ├─ _spikeglx_sync.times.eb04d3e9-5e67-4833-8321-fbccb3e9699b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/_spikeglx_sync.times.eb04d3e9-5e67-4833-8321-fbccb3e9699b.npy
|                    |    ├─  probe00
|                    |        ├─ _iblqc_ephysSpectralDensityAP.freqs.138676a2-d310-49b4-865e-0e14f8b13182.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityAP.freqs.138676a2-d310-49b4-865e-0e14f8b13182.npy
|                    |        ├─ _iblqc_ephysSpectralDensityAP.power.e9d8ddb5-ddaf-48b7-8a78-49d909c80ef1.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityAP.power.e9d8ddb5-ddaf-48b7-8a78-49d909c80ef1.npy
|                    |        ├─ _iblqc_ephysSpectralDensityLF.freqs.b31f4721-0163-4aec-a92e-7353764ce355.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityLF.freqs.b31f4721-0163-4aec-a92e-7353764ce355.npy
|                    |        ├─ _iblqc_ephysSpectralDensityLF.power.45854a1c-c309-4bb0-806e-a4f9f1617472.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysSpectralDensityLF.power.45854a1c-c309-4bb0-806e-a4f9f1617472.npy
|                    |        ├─ _iblqc_ephysTimeRmsAP.rms.bce68e1c-1d72-4bf9-b77f-0c9e3b1c5c12.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsAP.rms.bce68e1c-1d72-4bf9-b77f-0c9e3b1c5c12.npy
|                    |        ├─ _iblqc_ephysTimeRmsAP.timestamps.c0c3c1a7-ee4d-4117-8a6f-93d9d43c52ee.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsAP.timestamps.c0c3c1a7-ee4d-4117-8a6f-93d9d43c52ee.npy
|                    |        ├─ _iblqc_ephysTimeRmsLF.rms.837af07a-26aa-4264-97d6-fa55d2382f77.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsLF.rms.837af07a-26aa-4264-97d6-fa55d2382f77.npy
|                    |        ├─ _iblqc_ephysTimeRmsLF.timestamps.4f397701-da2e-460b-9937-a6a53ff23959.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_iblqc_ephysTimeRmsLF.timestamps.4f397701-da2e-460b-9937-a6a53ff23959.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.ap.54e5d55d-e19d-452d-beed-ff49a5b3b38b.ch -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.54e5d55d-e19d-452d-beed-ff49a5b3b38b.ch
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.ap.94285bfd-7500-4583-83b1-906c420cc667.cbin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.94285bfd-7500-4583-83b1-906c420cc667.cbin
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.ap.ea257f30-8a0f-4cde-83d2-aa4d2ce4bd23.meta -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.ea257f30-8a0f-4cde-83d2-aa4d2ce4bd23.meta
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.lf.5c814a9b-be69-4513-8282-a8fd3d562521.meta -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.lf.5c814a9b-be69-4513-8282-a8fd3d562521.meta
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.lf.99c957a8-f664-463b-afae-a1ba570a85b2.cbin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.lf.99c957a8-f664-463b-afae-a1ba570a85b2.cbin
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.lf.eaed8cf5-0bb9-4eaf-8d8e-3471e39d63fa.ch -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.lf.eaed8cf5-0bb9-4eaf-8d8e-3471e39d63fa.ch
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.sync.236a116c-8a18-4dd0-a2b5-169b28ef7fd4.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.sync.236a116c-8a18-4dd0-a2b5-169b28ef7fd4.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.timestamps.a3bf84f1-3ee2-4f3c-a36a-4b4959a513ba.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.timestamps.a3bf84f1-3ee2-4f3c-a36a-4b4959a513ba.npy
|                    |        ├─ _spikeglx_ephysData_g0_t0.imec0.wiring.40af4a49-1b9d-45ec-b443-a151c010ea3c.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.wiring.40af4a49-1b9d-45ec-b443-a151c010ea3c.json
|                    |        ├─ _spikeglx_sync.channels.probe00.4420d325-141b-4d30-8b92-0f8f545274d3.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_sync.channels.probe00.4420d325-141b-4d30-8b92-0f8f545274d3.npy
|                    |        ├─ _spikeglx_sync.polarities.probe00.6a0c68d2-2728-4d3d-8422-2228fe52226b.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_sync.polarities.probe00.6a0c68d2-2728-4d3d-8422-2228fe52226b.npy
|                    |        ├─  _spikeglx_sync.times.probe00.eaa07c05-df66-42ce-ae59-326b6ac9e8f0.npy -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_ephys_data/probe00/_spikeglx_sync.times.probe00.eaa07c05-df66-42ce-ae59-326b6ac9e8f0.npy
|                    ├─ raw_passive_data
|                    |    ├─ _iblrig_RFMapStim.raw.35976552-2c0f-4104-a79f-b40fe9efd747.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_RFMapStim.raw.35976552-2c0f-4104-a79f-b40fe9efd747.bin
|                    |    ├─ _iblrig_encoderEvents.raw.2b479438-2e0f-47ed-96cc-14ea415739d9.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_encoderEvents.raw.2b479438-2e0f-47ed-96cc-14ea415739d9.ssv
|                    |    ├─ _iblrig_encoderPositions.raw.c7d84d1f-7f60-417b-974a-0bb59fb88f33.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_encoderPositions.raw.c7d84d1f-7f60-417b-974a-0bb59fb88f33.ssv
|                    |    ├─ _iblrig_encoderTrialInfo.raw.f6011d97-2d08-4e97-ac72-1851fd2ff73e.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_encoderTrialInfo.raw.f6011d97-2d08-4e97-ac72-1851fd2ff73e.ssv
|                    |    ├─ _iblrig_stimPositionScreen.raw.97a83209-7b62-48da-805a-6fddd342f244.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_stimPositionScreen.raw.97a83209-7b62-48da-805a-6fddd342f244.csv
|                    |    ├─ _iblrig_syncSquareUpdate.raw.53182d6d-61b9-4d99-8e1c-1d6245ee923a.csv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_syncSquareUpdate.raw.53182d6d-61b9-4d99-8e1c-1d6245ee923a.csv
|                    |    ├─  _iblrig_taskSettings.raw.6391acef-5176-4fa4-9452-d6f6d4951e2f.json -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_passive_data/_iblrig_taskSettings.raw.6391acef-5176-4fa4-9452-d6f6d4951e2f.json
|                    ├─ raw_video_data
|                    |    ├─ _iblrig_bodyCamera.GPIO.64507d74-1af4-41e1-b785-680d801e325a.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_bodyCamera.GPIO.64507d74-1af4-41e1-b785-680d801e325a.bin
|                    |    ├─ _iblrig_bodyCamera.frame_counter.56cd0ba8-d1c0-4936-9a22-58721dfdef25.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_bodyCamera.frame_counter.56cd0ba8-d1c0-4936-9a22-58721dfdef25.bin
|                    |    ├─ _iblrig_bodyCamera.raw.face92e8-c8e9-4d10-8a89-525acc3381e2.mp4 -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_bodyCamera.raw.face92e8-c8e9-4d10-8a89-525acc3381e2.mp4
|                    |    ├─ _iblrig_bodyCamera.timestamps.cb336885-2bba-43d0-9e25-e6ed316ab22d.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_bodyCamera.timestamps.cb336885-2bba-43d0-9e25-e6ed316ab22d.ssv
|                    |    ├─ _iblrig_leftCamera.GPIO.d3c7d6d8-22a9-4d19-a15b-c9ad8c7cde0f.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_leftCamera.GPIO.d3c7d6d8-22a9-4d19-a15b-c9ad8c7cde0f.bin
|                    |    ├─ _iblrig_leftCamera.frame_counter.bb6b22ea-d744-4050-a632-bfa5a5c02cca.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_leftCamera.frame_counter.bb6b22ea-d744-4050-a632-bfa5a5c02cca.bin
|                    |    ├─ _iblrig_leftCamera.raw.3afad240-b6cd-45ee-b471-aa4265c23ce6.mp4 -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_leftCamera.raw.3afad240-b6cd-45ee-b471-aa4265c23ce6.mp4
|                    |    ├─ _iblrig_leftCamera.timestamps.3081bd45-6e10-4342-b09f-24f97ff4beee.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_leftCamera.timestamps.3081bd45-6e10-4342-b09f-24f97ff4beee.ssv
|                    |    ├─ _iblrig_rightCamera.GPIO.2b820d68-e1f6-4713-993c-dcc844128a75.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_rightCamera.GPIO.2b820d68-e1f6-4713-993c-dcc844128a75.bin
|                    |    ├─ _iblrig_rightCamera.frame_counter.dfed8727-da6b-41f8-87c0-1648097aec99.bin -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_rightCamera.frame_counter.dfed8727-da6b-41f8-87c0-1648097aec99.bin
|                    |    ├─ _iblrig_rightCamera.raw.b9d9825e-c47f-4a21-a7f2-9847038e3c14.mp4 -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_rightCamera.raw.b9d9825e-c47f-4a21-a7f2-9847038e3c14.mp4
|                    |    ├─  _iblrig_rightCamera.timestamps.c1f5e7c1-26e3-43eb-aabb-f411551649d2.ssv -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/raw_video_data/_iblrig_rightCamera.timestamps.c1f5e7c1-26e3-43eb-aabb-f411551649d2.ssv
|                    ├─  spike_sorters
|                        ├─  ks2_matlab
|                            ├─  probe00
|                                ├─  _kilosort_raw.output.10ee20c5-71dc-4e6d-9c52-45c78d9ac57b.tar -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-21/001/spike_sorters/ks2_matlab/probe00/_kilosort_raw.output.10ee20c5-71dc-4e6d-9c52-45c78d9ac57b.tar
├─ mainenlab
|    ├─  Subjects
|        ├─  ZM_2240
|            ├─  2020-01-21
|                ├─  001 -> /mnt/ibl/mainenlab/Subjects/ZM_2240/2020-01-21/001
├─ ps-vae_demo_head-fixed.zip
├─ public_tree.txt
├─ registration
|    ├─ churchlandlab
|    |    ├─  Subjects
|    |        ├─  CSHL045
|    |            ├─  2020-02-25
|    |                ├─  002
|    |                    ├─  raw_ephys_data
|    |                        ├─  probe00
|    |                            ├─  probe00 -> /mnt/ibl/churchlandlab/Subjects/CSHL045/2020-02-25/002/raw_ephys_data/probe00
|    ├─  hoferlab
|        ├─  Subjects
|            ├─ SWC_042
|            |    ├─  2020-07-15
|            |        ├─  001
|            |            ├─  raw_ephys_data
|            |                ├─  probe01
|            |                    ├─  probe01 -> /mnt/ibl/hoferlab/Subjects/SWC_042/2020-07-15/001/raw_ephys_data/probe01
|            ├─  SWC_043
|                ├─  2020-09-16
|                    ├─  002
|                        ├─  raw_ephys_data
|                            ├─  probe01
|                                ├─  probe01 -> /mnt/ibl/hoferlab/Subjects/SWC_043/2020-09-16/002/raw_ephys_data/probe01
├─  zadorlab
    ├─  Subjects
        ├─  CSH_ZAD_029
            ├─  2020-09-19
                ├─  001
                    ├─ alf
                    |    ├─ _ibl_bodyCamera.dlc.38ec5e8f-fc0c-479d-8cf6-1eb981bd206f.pqt -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_bodyCamera.dlc.38ec5e8f-fc0c-479d-8cf6-1eb981bd206f.pqt
                    |    ├─ _ibl_bodyCamera.times.bd941eb1-d512-4f65-9ab8-d6021fe4d877.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_bodyCamera.times.bd941eb1-d512-4f65-9ab8-d6021fe4d877.npy
                    |    ├─ _ibl_leftCamera.dlc.461179ee-d800-4e9e-88d7-f521eec12162.pqt -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_leftCamera.dlc.461179ee-d800-4e9e-88d7-f521eec12162.pqt
                    |    ├─ _ibl_leftCamera.times.7fe90b96-ba20-4173-9ede-befcf8a5bce8.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_leftCamera.times.7fe90b96-ba20-4173-9ede-befcf8a5bce8.npy
                    |    ├─ _ibl_rightCamera.dlc.7961de5d-39b9-4919-9c7e-1280bdfba06a.pqt -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_rightCamera.dlc.7961de5d-39b9-4919-9c7e-1280bdfba06a.pqt
                    |    ├─ _ibl_rightCamera.times.4987b769-7726-4136-9fa8-87de39b21c0f.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_rightCamera.times.4987b769-7726-4136-9fa8-87de39b21c0f.npy
                    |    ├─ _ibl_trials.choice.7167f119-5f21-47e6-bb7f-e79b08065c45.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.choice.7167f119-5f21-47e6-bb7f-e79b08065c45.npy
                    |    ├─ _ibl_trials.contrastLeft.a9fcb585-b842-4b69-97f5-28e372440eb8.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.contrastLeft.a9fcb585-b842-4b69-97f5-28e372440eb8.npy
                    |    ├─ _ibl_trials.contrastRight.5bc75b41-beb2-42b6-8969-13e0be154f72.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.contrastRight.5bc75b41-beb2-42b6-8969-13e0be154f72.npy
                    |    ├─ _ibl_trials.feedbackType.64948037-74de-416a-87e7-dedac77cadf5.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.feedbackType.64948037-74de-416a-87e7-dedac77cadf5.npy
                    |    ├─ _ibl_trials.feedback_times.6c1d8f6f-dc54-4572-91e0-554e93480bd7.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.feedback_times.6c1d8f6f-dc54-4572-91e0-554e93480bd7.npy
                    |    ├─ _ibl_trials.firstMovement_times.44809de9-d186-4e56-8fb3-63fa54c79080.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.firstMovement_times.44809de9-d186-4e56-8fb3-63fa54c79080.npy
                    |    ├─ _ibl_trials.goCueTrigger_times.e18b1aad-b331-4e46-bef0-9083d63300e8.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.goCueTrigger_times.e18b1aad-b331-4e46-bef0-9083d63300e8.npy
                    |    ├─ _ibl_trials.goCue_times.f939691c-86b6-4350-aeb3-ef9441d730a4.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.goCue_times.f939691c-86b6-4350-aeb3-ef9441d730a4.npy
                    |    ├─ _ibl_trials.intervals.ebbcb591-3b59-4694-a8b4-a01fcda2c538.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.intervals.ebbcb591-3b59-4694-a8b4-a01fcda2c538.npy
                    |    ├─ _ibl_trials.intervals_bpod.f4f4d5e6-2bc2-4148-9874-32c31d16197a.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.intervals_bpod.f4f4d5e6-2bc2-4148-9874-32c31d16197a.npy
                    |    ├─ _ibl_trials.probabilityLeft.72c7a12f-34b0-4aff-91fd-e1251137ed14.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.probabilityLeft.72c7a12f-34b0-4aff-91fd-e1251137ed14.npy
                    |    ├─ _ibl_trials.response_times.f477091c-33c3-4db9-ba14-a9f5e6ad7b58.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.response_times.f477091c-33c3-4db9-ba14-a9f5e6ad7b58.npy
                    |    ├─ _ibl_trials.rewardVolume.515bc3ed-3f15-4b9b-93c8-a66ca21d275f.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.rewardVolume.515bc3ed-3f15-4b9b-93c8-a66ca21d275f.npy
                    |    ├─ _ibl_trials.stimOff_times.beab3d32-9af6-4a66-9a76-a28d2d4792cc.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.stimOff_times.beab3d32-9af6-4a66-9a76-a28d2d4792cc.npy
                    |    ├─ _ibl_trials.stimOn_times.7fdfb88c-c0c2-40fe-a5d4-e6b9df64f5d1.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_trials.stimOn_times.7fdfb88c-c0c2-40fe-a5d4-e6b9df64f5d1.npy
                    |    ├─ _ibl_wheel.position.97f3e770-1cae-4441-962a-a6dce1057f5d.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_wheel.position.97f3e770-1cae-4441-962a-a6dce1057f5d.npy
                    |    ├─ _ibl_wheel.timestamps.070b7410-d053-42e7-8b3a-3e336ae66567.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_wheel.timestamps.070b7410-d053-42e7-8b3a-3e336ae66567.npy
                    |    ├─ _ibl_wheelMoves.intervals.8c168f34-5c2b-4cad-9473-b329596ad8ae.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_wheelMoves.intervals.8c168f34-5c2b-4cad-9473-b329596ad8ae.npy
                    |    ├─ _ibl_wheelMoves.peakAmplitude.5b60fe9c-d343-4449-8d0d-38abec11c99f.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/_ibl_wheelMoves.peakAmplitude.5b60fe9c-d343-4449-8d0d-38abec11c99f.npy
                    |    ├─ probe01
                    |    |    ├─ _kilosort_whitening.matrix.a61aae08-5042-4664-a834-50ff19dbc489.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/_kilosort_whitening.matrix.a61aae08-5042-4664-a834-50ff19dbc489.npy
                    |    |    ├─ _phy_spikes_subset.channels.dfbe5988-aff7-4ac1-a0a3-06cc2329af69.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/_phy_spikes_subset.channels.dfbe5988-aff7-4ac1-a0a3-06cc2329af69.npy
                    |    |    ├─ _phy_spikes_subset.spikes.863c7a10-3621-4d8b-883d-6992f4c61ba6.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/_phy_spikes_subset.spikes.863c7a10-3621-4d8b-883d-6992f4c61ba6.npy
                    |    |    ├─ _phy_spikes_subset.waveforms.26c5c31f-f3f2-4777-8ed7-bbe45a522636.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/_phy_spikes_subset.waveforms.26c5c31f-f3f2-4777-8ed7-bbe45a522636.npy
                    |    |    ├─ channels.brainLocationIds_ccf_2017.430ca150-6d52-449d-830e-5339acba3cfe.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/channels.brainLocationIds_ccf_2017.430ca150-6d52-449d-830e-5339acba3cfe.npy
                    |    |    ├─ channels.localCoordinates.2d5dc314-38fd-41d4-b6bb-ba6d232aba9a.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/channels.localCoordinates.2d5dc314-38fd-41d4-b6bb-ba6d232aba9a.npy
                    |    |    ├─ channels.mlapdv.1bd1b382-1096-4e71-aa35-8459cb4ffacc.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/channels.mlapdv.1bd1b382-1096-4e71-aa35-8459cb4ffacc.npy
                    |    |    ├─ channels.rawInd.c2036b4e-4148-46ee-87fa-7abff36a269f.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/channels.rawInd.c2036b4e-4148-46ee-87fa-7abff36a269f.npy
                    |    |    ├─ clusters.amps.3322d09a-4e81-450d-9bfe-af5abd568083.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.amps.3322d09a-4e81-450d-9bfe-af5abd568083.npy
                    |    |    ├─ clusters.brainLocationAcronyms_ccf_2017.4dd88c23-fd55-4ff8-9d24-3dab07d07068.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.brainLocationAcronyms_ccf_2017.4dd88c23-fd55-4ff8-9d24-3dab07d07068.npy
                    |    |    ├─ clusters.brainLocationIds_ccf_2017.300c8851-bdf3-474e-b1c1-bdca78a498b2.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.brainLocationIds_ccf_2017.300c8851-bdf3-474e-b1c1-bdca78a498b2.npy
                    |    |    ├─ clusters.channels.676b2abe-5c09-4bab-8ec6-715ee6636319.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.channels.676b2abe-5c09-4bab-8ec6-715ee6636319.npy
                    |    |    ├─ clusters.depths.e9569239-74c1-4176-9d20-46a273dccd43.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.depths.e9569239-74c1-4176-9d20-46a273dccd43.npy
                    |    |    ├─ clusters.metrics.c16e07c8-49aa-4bb2-ae0f-890389ac5b88.pqt -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.metrics.c16e07c8-49aa-4bb2-ae0f-890389ac5b88.pqt
                    |    |    ├─ clusters.mlapdv.76601f6b-0650-492a-90a0-fd777b4fa75d.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.mlapdv.76601f6b-0650-492a-90a0-fd777b4fa75d.npy
                    |    |    ├─ clusters.peakToTrough.3ae3e228-c11f-45e0-9de0-f03ff09cb83a.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.peakToTrough.3ae3e228-c11f-45e0-9de0-f03ff09cb83a.npy
                    |    |    ├─ clusters.uuids.4a9275f2-861c-418e-aa64-49f4aa4e044b.csv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.uuids.4a9275f2-861c-418e-aa64-49f4aa4e044b.csv
                    |    |    ├─ clusters.waveforms.6eaa4de8-02de-4306-826e-1bdb62c4dd65.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.waveforms.6eaa4de8-02de-4306-826e-1bdb62c4dd65.npy
                    |    |    ├─ clusters.waveformsChannels.f9f9150d-2447-4790-a005-0ae864dc36f5.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/clusters.waveformsChannels.f9f9150d-2447-4790-a005-0ae864dc36f5.npy
                    |    |    ├─ spikes.amps.3de1a824-44cc-42ab-b427-c1bd7e19244a.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.amps.3de1a824-44cc-42ab-b427-c1bd7e19244a.npy
                    |    |    ├─ spikes.clusters.6242cbe7-6633-4b32-a69f-52656995a644.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.clusters.6242cbe7-6633-4b32-a69f-52656995a644.npy
                    |    |    ├─ spikes.depths.6bebe065-eba6-4f18-9ef5-adb784e56205.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.depths.6bebe065-eba6-4f18-9ef5-adb784e56205.npy
                    |    |    ├─ spikes.samples.b4232e3d-858f-454a-a532-ae7c403da605.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.samples.b4232e3d-858f-454a-a532-ae7c403da605.npy
                    |    |    ├─ spikes.templates.e0a29dfc-d6e9-4a88-8f0a-1a924c707cb9.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.templates.e0a29dfc-d6e9-4a88-8f0a-1a924c707cb9.npy
                    |    |    ├─ spikes.times.7be77e6a-58f8-4b9b-b4ea-121108ddd8e1.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/spikes.times.7be77e6a-58f8-4b9b-b4ea-121108ddd8e1.npy
                    |    |    ├─ templates.amps.16397e55-cdf3-463a-ac55-90b83c2e35b5.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/templates.amps.16397e55-cdf3-463a-ac55-90b83c2e35b5.npy
                    |    |    ├─ templates.waveforms.f49dda8e-5a95-45d7-bccd-3b76b84f93a4.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/templates.waveforms.f49dda8e-5a95-45d7-bccd-3b76b84f93a4.npy
                    |    |    ├─  templates.waveformsChannels.0f712c61-05b2-4161-8749-84ad72a9fcfb.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probe01/templates.waveformsChannels.0f712c61-05b2-4161-8749-84ad72a9fcfb.npy
                    |    ├─ probes.description.ddfd81bd-69d5-4a56-8250-d6aeb921b29c.json -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probes.description.ddfd81bd-69d5-4a56-8250-d6aeb921b29c.json
                    |    ├─  probes.trajectory.920ca2fa-1605-42a1-a57e-534780af0f9d.json -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/alf/probes.trajectory.920ca2fa-1605-42a1-a57e-534780af0f9d.json
                    ├─ raw_behavior_data
                    |    ├─ _iblrig_ambientSensorData.raw.2a36cce8-f789-470d-b461-30b1ea070751.jsonable -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_ambientSensorData.raw.2a36cce8-f789-470d-b461-30b1ea070751.jsonable
                    |    ├─ _iblrig_encoderEvents.raw.f97b8409-adfa-4ff4-b0fd-c6f36a699d80.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_encoderEvents.raw.f97b8409-adfa-4ff4-b0fd-c6f36a699d80.ssv
                    |    ├─ _iblrig_encoderPositions.raw.1bb91eb9-9aee-4650-926b-6afd63892e76.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_encoderPositions.raw.1bb91eb9-9aee-4650-926b-6afd63892e76.ssv
                    |    ├─ _iblrig_encoderTrialInfo.raw.cad93260-0c21-4cf7-ac63-f9af968bfbb2.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_encoderTrialInfo.raw.cad93260-0c21-4cf7-ac63-f9af968bfbb2.ssv
                    |    ├─ _iblrig_stimPositionScreen.raw.9542b195-394f-4ad7-8277-82ca71be55b4.csv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_stimPositionScreen.raw.9542b195-394f-4ad7-8277-82ca71be55b4.csv
                    |    ├─ _iblrig_syncSquareUpdate.raw.db1fa5d5-7fc7-4bfa-95da-3185f53e6ea7.csv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_syncSquareUpdate.raw.db1fa5d5-7fc7-4bfa-95da-3185f53e6ea7.csv
                    |    ├─ _iblrig_taskData.raw.98406b22-9919-4035-9295-2eb523d40eb5.jsonable -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_taskData.raw.98406b22-9919-4035-9295-2eb523d40eb5.jsonable
                    |    ├─  _iblrig_taskSettings.raw.6b5dbd12-6dac-4479-a4e4-f93942577928.json -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_behavior_data/_iblrig_taskSettings.raw.6b5dbd12-6dac-4479-a4e4-f93942577928.json
                    ├─ raw_ephys_data
                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.2da9b2ec-0a4d-481e-a93a-e17b493e9751.ch -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.2da9b2ec-0a4d-481e-a93a-e17b493e9751.ch
                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.d4b309d6-80ba-4aa2-9087-cfd9c3f73152.meta -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.d4b309d6-80ba-4aa2-9087-cfd9c3f73152.meta
                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.e55ca015-a12d-4a8e-a4db-864877ec6440.cbin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.e55ca015-a12d-4a8e-a4db-864877ec6440.cbin
                    |    ├─ _spikeglx_ephysData_g0_t0.nidq.wiring.a96a1c65-9bd5-4e5a-8b88-fe3b1e3b5636.json -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.wiring.a96a1c65-9bd5-4e5a-8b88-fe3b1e3b5636.json
                    |    ├─ _spikeglx_sync.channels.3b51a7bf-8cef-4df0-8e29-2869a61e843d.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_sync.channels.3b51a7bf-8cef-4df0-8e29-2869a61e843d.npy
                    |    ├─ _spikeglx_sync.polarities.37c397d0-c06a-43fa-b950-a2c9e15962d6.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_sync.polarities.37c397d0-c06a-43fa-b950-a2c9e15962d6.npy
                    |    ├─ _spikeglx_sync.times.6d2aa754-aa5f-4291-8e06-43dc356d46ab.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/_spikeglx_sync.times.6d2aa754-aa5f-4291-8e06-43dc356d46ab.npy
                    |    ├─  probe01
                    |        ├─ _iblqc_ephysSpectralDensityAP.freqs.92597c6d-40fa-431e-94bf-5b930aa4797e.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityAP.freqs.92597c6d-40fa-431e-94bf-5b930aa4797e.npy
                    |        ├─ _iblqc_ephysSpectralDensityAP.power.066e7069-dc8a-43cc-a831-53f4713b1130.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityAP.power.066e7069-dc8a-43cc-a831-53f4713b1130.npy
                    |        ├─ _iblqc_ephysSpectralDensityLF.freqs.73d5a610-d926-497c-a4da-6b31bb5754da.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityLF.freqs.73d5a610-d926-497c-a4da-6b31bb5754da.npy
                    |        ├─ _iblqc_ephysSpectralDensityLF.power.95fda7e6-554f-4406-8537-6d60996c7b14.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysSpectralDensityLF.power.95fda7e6-554f-4406-8537-6d60996c7b14.npy
                    |        ├─ _iblqc_ephysTimeRmsAP.rms.cb01d433-c7ca-4253-8fa6-dfb23dfdc0f3.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsAP.rms.cb01d433-c7ca-4253-8fa6-dfb23dfdc0f3.npy
                    |        ├─ _iblqc_ephysTimeRmsAP.timestamps.0ae13c77-59a5-45c3-86ef-ac5b911382ee.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsAP.timestamps.0ae13c77-59a5-45c3-86ef-ac5b911382ee.npy
                    |        ├─ _iblqc_ephysTimeRmsLF.rms.49892eaf-fdea-4ad7-af63-290076904e1c.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsLF.rms.49892eaf-fdea-4ad7-af63-290076904e1c.npy
                    |        ├─ _iblqc_ephysTimeRmsLF.timestamps.a197e81e-7614-48db-a389-c94a323fc744.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_iblqc_ephysTimeRmsLF.timestamps.a197e81e-7614-48db-a389-c94a323fc744.npy
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.0444c530-f280-4450-b1cb-baad8c046ca1.meta -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.0444c530-f280-4450-b1cb-baad8c046ca1.meta
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.0a554854-aa80-4fae-8e59-c08bb5f6f8d4.ch -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.0a554854-aa80-4fae-8e59-c08bb5f6f8d4.ch
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.ap.7035d424-3dba-4c3f-989e-2d3097c8dfd2.cbin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.7035d424-3dba-4c3f-989e-2d3097c8dfd2.cbin
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.93aa6670-8560-42bd-b0ee-910c6ed1843f.meta -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.93aa6670-8560-42bd-b0ee-910c6ed1843f.meta
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.c91d6d49-5eb5-4491-ade4-445dae61ccf0.ch -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.c91d6d49-5eb5-4491-ade4-445dae61ccf0.ch
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.lf.fafa6d01-17b0-4026-bfc7-cf2581f0cfa9.cbin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.lf.fafa6d01-17b0-4026-bfc7-cf2581f0cfa9.cbin
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.sync.5e843c08-e29c-4296-be4d-bd59a7c46d7e.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.sync.5e843c08-e29c-4296-be4d-bd59a7c46d7e.npy
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.timestamps.a837aa50-87e8-4413-8736-d13fdb7590fd.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.timestamps.a837aa50-87e8-4413-8736-d13fdb7590fd.npy
                    |        ├─ _spikeglx_ephysData_g0_t0.imec1.wiring.abbb8463-43b5-4888-8524-e8200e15ef79.json -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.wiring.abbb8463-43b5-4888-8524-e8200e15ef79.json
                    |        ├─ _spikeglx_sync.channels.probe01.910a4d9c-0e60-45a8-b1f6-606eadd11020.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_sync.channels.probe01.910a4d9c-0e60-45a8-b1f6-606eadd11020.npy
                    |        ├─ _spikeglx_sync.polarities.probe01.af1e1a20-c6a9-49bd-bcf6-982abb2661ab.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_sync.polarities.probe01.af1e1a20-c6a9-49bd-bcf6-982abb2661ab.npy
                    |        ├─  _spikeglx_sync.times.probe01.6b46ee81-4007-4b9f-a097-9c4bdcecc8c9.npy -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_ephys_data/probe01/_spikeglx_sync.times.probe01.6b46ee81-4007-4b9f-a097-9c4bdcecc8c9.npy
                    ├─ raw_video_data
                    |    ├─ _iblrig_bodyCamera.GPIO.56a7cb63-b408-4d9a-a24f-8326c33a1e00.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_bodyCamera.GPIO.56a7cb63-b408-4d9a-a24f-8326c33a1e00.bin
                    |    ├─ _iblrig_bodyCamera.frame_counter.a61fc64b-ed95-4543-8ece-3119fb529be1.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_bodyCamera.frame_counter.a61fc64b-ed95-4543-8ece-3119fb529be1.bin
                    |    ├─ _iblrig_bodyCamera.raw.ad16cc47-43c0-4a00-b572-25a5e144910d.mp4 -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_bodyCamera.raw.ad16cc47-43c0-4a00-b572-25a5e144910d.mp4
                    |    ├─ _iblrig_bodyCamera.timestamps.da3b54b6-48d4-43c5-8b31-28271d7941af.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_bodyCamera.timestamps.da3b54b6-48d4-43c5-8b31-28271d7941af.ssv
                    |    ├─ _iblrig_leftCamera.GPIO.1efd6fbb-bb19-4346-b9b6-8c541f21baf9.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_leftCamera.GPIO.1efd6fbb-bb19-4346-b9b6-8c541f21baf9.bin
                    |    ├─ _iblrig_leftCamera.frame_counter.3c9938bd-0bbe-4075-befb-dcb95be1aef5.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_leftCamera.frame_counter.3c9938bd-0bbe-4075-befb-dcb95be1aef5.bin
                    |    ├─ _iblrig_leftCamera.raw.6ef2a0e0-1b0e-45cd-aba5-80ad3e400ad9.mp4 -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_leftCamera.raw.6ef2a0e0-1b0e-45cd-aba5-80ad3e400ad9.mp4
                    |    ├─ _iblrig_leftCamera.timestamps.9ccf901f-faa5-476e-aa1e-84925f5adec9.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_leftCamera.timestamps.9ccf901f-faa5-476e-aa1e-84925f5adec9.ssv
                    |    ├─ _iblrig_rightCamera.GPIO.d1506242-263d-4c18-a513-f17dc8dd8e57.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_rightCamera.GPIO.d1506242-263d-4c18-a513-f17dc8dd8e57.bin
                    |    ├─ _iblrig_rightCamera.frame_counter.dc5cb4f9-7f0b-46c4-b91a-7e8c75c8f8aa.bin -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_rightCamera.frame_counter.dc5cb4f9-7f0b-46c4-b91a-7e8c75c8f8aa.bin
                    |    ├─ _iblrig_rightCamera.raw.9c160ed6-cdf2-4d59-a5f3-a06526df5f9a.mp4 -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_rightCamera.raw.9c160ed6-cdf2-4d59-a5f3-a06526df5f9a.mp4
                    |    ├─  _iblrig_rightCamera.timestamps.c5c5e27b-985f-4aee-921f-94a0698a0522.ssv -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/raw_video_data/_iblrig_rightCamera.timestamps.c5c5e27b-985f-4aee-921f-94a0698a0522.ssv
                    ├─  spike_sorters
                        ├─  ks2_matlab
                            ├─  probe01
                                ├─  _kilosort_raw.output.204a5a51-c1ca-4cfc-9142-5570c4f96a7b.tar -> /mnt/ibl/zadorlab/Subjects/CSH_ZAD_029/2020-09-19/001/spike_sorters/ks2_matlab/probe01/_kilosort_raw.output.204a5a51-c1ca-4cfc-9142-5570c4f96a7b.tar
```

## 2020: Behavior data release associated with a publication
The IBL has released all of the behavior sessions associated with the publication 
[International Brain Laboratory et al., 2021](https://elifesciences.org/articles/63711)
via [Datajoint](public_datajoint). 