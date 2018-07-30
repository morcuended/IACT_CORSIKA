import matplotlib.pyplot as plt
from argparse import ArgumentParser
import numpy as np
from eventio import IACTFile

parser = ArgumentParser()
parser.add_argument('-i', '--inputfile', dest='inputfile')
parser.add_argument('-e', '--event', dest='event', type=int, default=0)


class Hist1D(object):

    def __init__(self, nbins, xlow, xhigh):
        self.nbins = nbins
        self.xlow = xlow
        self.xhigh = xhigh
        self.hist, edges = np.histogram([], bins=nbins, range=(xlow, xhigh))
        self.bins = (edges[:-1] + edges[1:]) / 2.

    def fill(self, arr):
        hist, edges = np.histogram(arr, bins=self.nbins, range=(self.xlow,
                                                                self.xhigh))
        self.hist += hist

    @property
    def data(self):
        return self.bins, self.hist


def main():
    args = parser.parse_args()

    wlen_min = 200
    wlen_max = 700
    bins = 10 * (wlen_max - wlen_min)
    h = Hist1D(bins, wlen_min, wlen_max)

    fig, ax = plt.subplots()
    ax.set_xlabel("wavelength [nm]")

    with IACTFile(args.inputfile) as f:
        print(f)
        for n in range(len(f)):
            event = f[n]
            bunches = event.photon_bunches[0]
            f_bunches = bunches[bunches['lambda'] > 0]

            h.fill(f_bunches['lambda'])

        ax.step(*h.data, color='red', label='Fluorescence')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
