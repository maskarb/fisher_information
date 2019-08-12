# Fisher Information

Example dataset:
* [cantar2019.csv](cantar2019.csv) -> dataset for Cantareira system in Brazil. Includes monthly precipitation and storage values from Jan-2004 to Apr-2019.

Discrete amplitude method with disjoint bins:
* [discrete_amp_disjoint.py](discrete_amp_disjoint.py) -> bins are determined based on entire time series, used within each window

Discrete amplitude method with overlapping bins:
* [discrete_amp_overlap.py](discrete_amp_overlap.py)

Kernel method:
* [kernel_functions.py](kernel_functions.py) -> bandwidth determined for entire time series, used within each window
