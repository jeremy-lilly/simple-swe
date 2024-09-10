# Tensor train SWE gravity wave solver
Author: Jeremy Lilly
___


## Description

Our goal is to solve the linearized SWE gravity wave subsystem,
\begin{align*}
\partial_t u &= -c\ \partial_x h \\
\partial_t v &= -c\ \partial_y h \\
\partial_t h &= -c\ \left( \partial_x u + \partial_y v \right) \,,
\end{align*}
using tensor train (TT) representations of both variable data and RHS operators.

This repo contains three notebooks:
1) `wave_loops.ipynb` implements a simple, loop based approach to calculating tendencies,
2) `wave_matmul.ipynb` implements RHS calculations via matrix-vector multiply,
3) `wave_qtt.ipynb` uses quantized tensor train (QTT) representations of data and operators.


## Installing and running

Best practice is to create a new python environment then install the required packages via `pip` (or `conda`). Using `pip`:
1) Create a new virtual environment and activate,
    ```bash
    python -m venv /path/to/new/env
    source /path/to/new/env/bin/activate
    ```
2) Install needed packages using the provided `requirements.txt`. Note that this assumes you are using the CPU version of PyTorch as the backend for `torchTT`, if you want a version with GPU capability, remove the `torch` line from `requirements.txt` and install manually. 
    ```bash
    pip install -r requirements.txt
    ```
   - This will probably fail as pip tries to install `torchTT` from PyPI. If it does, remove the offending line from `requirements.txt` and rerun the above. Then, install `torchTT` manually from GitHub,
        ```bash
        git clone https://github.com/ion-g-ion/torchTT
        cd torchTT
        python setup.py install
        ```
3) Start the Jupyter notebook,
    ```bash
    jupyter-notebook
    ```
4) When done, close the notebook server with `ctrl-c`, then leave the virtual environment,
    ```bash
    deactivate
    ```
