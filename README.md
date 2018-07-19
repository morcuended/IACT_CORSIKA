# Inspection of IACT output for air fluorescence photon bunches simulated with CORSIKA

  - [IACT/ATMO package](https://www.mpi-hd.mpg.de/hfm/~bernlohr/iact-atmo/) version 1.50 by Konrad Bernlöhr.

An example of photon bunches distribution (red for fluorescence and blue for Cherenov) at
observation level. IACT option of CORSIKA has been used to store them.

![](images/iact3d.png)

## Requirements and installation
In order to run the notebook with the examples, you will need to have the following packages
installed:
  - matplotlib
  - numpy
  - **eventio**: [pyeventio](https://github.com/fact-project/pyeventio)(install it
    with `pip install eventio`)

### Example (see jupyter notebook)

![](images/vertical.png "Top view")

### Content:
  - *data*: output data from several test runs
  - *IACT_output_inspection.ipynb* jupyter notebook with some examples.
