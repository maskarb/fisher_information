# Fisher Information

Example dataset:
* [cantar2019.csv](cantar2019.csv) -> dataset for Cantareira system in Brazil. Includes monthly precipitation and storage values from Jan-2004 to Apr-2019.

Discrete amplitude method with disjoint bins:
* [discrete_amp_nrw.py](discrete_amp_nrw.py) -> bins are determined based on entire time series, used within each window
* [discrete_amp_rw.py](discrete_amp_rw.py) -> bins are determined based on sliding window

Discrete amplitude method with overlapping bins:
* [discrete_amp_overlap.py](discrete_amp_overlap.py)

Kernel method:
* [kernel_functions_hinwindows.py](kernel_functions_hinwindows.py) -> bandwidth determined within the rolling window
* [kernel_functions_hnotinwindows.py](kernel_functions_hnotinwindows.py) -> bandwidth determined for entire time series, used within each window
