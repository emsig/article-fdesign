from numpy import savetxt, loadtxt
from empymod.filters import DigitalFilter
from empyscripts.fdesign import load_filter, save_filter


def shelved2ascii(name):
    """Store filter and inversion output in plain ASCII files.

    Geophysics doesn't permit binary files to be distributed. So we load
    the information stored with `empyscripts.fdesign.save_filter` and store
    it in plain ASCII files.

    """
    # Base-name for files
    base = './filters/'+name

    # Get the filter
    filt, out = load_filter(name, True)

    # Store arrays
    savetxt(base+'-filt-base.txt', filt.base)
    savetxt(base+'-filt-j0.txt', filt.j0)
    savetxt(base+'-filt-j1.txt', filt.j1)
    savetxt(base+'-out-2a.txt', out[2][0])
    savetxt(base+'-out-2b.txt', out[2][1])
    savetxt(base+'-out-3.txt', out[3])

    # Store scalars in one file
    savetxt(base+'-scalars.txt',
            [filt.factor, out[0][0], out[0][1], out[1]],
            header=filt.name + '; filt.factor; out[0][1]; out[0][1]; out[1]')


def ascii2shelved(name):
    """Convert ASCII-files to empyscripts.fdesign.save_filter-object.

    Geophysics doesn't permit binary files to be distributed. So we load
    the information stored in plain ASCII files, and create the required
    binaries with `empyscripts.fdesign.save_filter`.

    """
    # Base-name of files
    base = './filters/'+name

    # Get scalars
    numbers = loadtxt(base+'-scalars.txt')

    # Collect inversion-result tuple
    out = ([numbers[1], numbers[2]],
           numbers[3],
           [loadtxt(base+'-out-2a.txt'), loadtxt(base+'-out-2b.txt')],
           loadtxt(base+'-out-3.txt'))

    # Collect digital filter
    dlf = DigitalFilter(name)
    dlf.base = loadtxt(base+'-filt-base.txt')
    dlf.factor = numbers[0]
    dlf.j0 = loadtxt(base+'-filt-j0.txt')
    dlf.j1 = loadtxt(base+'-filt-j1.txt')

    # Save the filter and the inversion result
    save_filter(name, dlf, out)


if __name__ == "__main__":
    ascii2shelved('wer201')
    ascii2shelved('wer2001')
