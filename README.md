# Fisher Information

This program utilizes Python3.8 and was developed on Ubuntu in Windows Subsystem for Linux.

See [Fisher Information Methods for Detecting Shifting Regimes in Water Supply Systems](https://repository.lib.ncsu.edu/handle/1840.20/36907) for more information.

## Dependencies

Boost.python 1.67

    sudo apt install libboost-python1.67-dev

To compile the `fast_deriv.cpp`, do the following:

    g++ -I /usr/include/python3.8 -fpic -c -o fast_deriv.o fast_deriv.cpp

    g++ -o fast_deriv.so -shared fast_deriv.o -lboost_python38 -lpython3.8

Any errors are up to the user to troubleshoot.

## Usage

Example dataset:
* [cantar2019.csv](cantar2019.csv) -> dataset for Cantareira system in Brazil. Includes monthly precipitation and storage values from Jan-2004 to Apr-2019.

Discrete amplitude method with disjoint bins:
* [discrete_amp_disjoint.py](discrete_amp_disjoint.py) -> bins are determined based on entire time series, used within each window

        python discrete_amp_disjoint.py

Discrete amplitude method with overlapping bins:
* [discrete_amp_overlap.py](discrete_amp_overlap.py)

        python discrete_amp_overlap.py

Kernel method:
* [kernel_functions.py](kernel_functions.py) -> bandwidth determined for entire time series, used within each window

        python kernel_functions.py
