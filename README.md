# Fisher Information

Discrete amplitude method with disjoint bins:
* discrete_amp_nrw.py -> bins are determined based on entire time series, used within each window
* discrete_amp_rw.py -> bins are determined based on sliding window

Discrete amplitude method with overlapping bins:
* discrete_amp_overlap.py

Kernel method:
* kernel_functions_hinwindows.py -> bandwidth determined within the rolling window
* kernel_functions_hnotinwindows.py -> bandwidth determined for entire time series, used within each window
