"""
Utility to print date, time, and version information.

Adjusted from https://github.com/empymod/example-notebooks, which in turn was
heavily inspired by:

    - ipynbtools.py from qutip https://github.com/qutip
    - watermark.py from https://github.com/rasbt/watermark

"""

import sys
import time
import platform
import multiprocessing
import numpy
import scipy
import IPython
import empyscripts
import empymod
import matplotlib
from IPython.display import HTML


def info():
    """Print date and version information as a html-table."""

    # Define styles
    style1 = " style='border: 2px solid #fff; text-align: left;'"
    style2 = " style='background-color: #ccc;"
    style2 += "width: 10%; border: 2px solid #fff;'"

    # Print date and time info as title
    html = "<h3>%s</h3>" % time.strftime('%a %b %d %H:%M:%S %Y %Z')

    # Start table
    html += '<table>'

    # empymod, OS, threads, IPython
    html += "<tr" + style1 + ">"
    html += "<td" + style2 + ">%s</td>" % empymod.__version__
    html += "<td" + style1 + ">empymod</td>"
    html += "<td" + style2 + ">%s</td>" % numpy.__version__
    html += "<td" + style1 + ">numpy</td>"
    html += "<td" + style2 + ">%s</td>" % platform.system()
    html += "<td" + style1 + ">OS</td>"
    html += "<td" + style2 + ">%s</td>" % IPython.__version__
    html += "<td" + style1 + ">IPython</td>"
    html += "</tr>"

    # numpy, scipy, matplotlib
    html += "<tr" + style1 + ">"
    html += "<td" + style2 + ">%s</td>" % empyscripts.__version__
    html += "<td" + style1 + ">empyscripts</td>"
    html += "<td" + style2 + ">%s</td>" % scipy.__version__
    html += "<td" + style1 + ">scipy</td>"
    html += "<td" + style2 + ">%s</td>" % multiprocessing.cpu_count()
    html += "<td" + style1 + ">CPU(s)</td>"
    html += "<td" + style2 + ">%s</td>" % matplotlib.__version__
    html += "<td" + style1 + ">matplotlib</td>"
    html += "</tr>"

    # sys.version
    html += "<tr" + style1 + ">"
    html += "<td" + style1 + " colspan='8'>%s</td>" % sys.version
    html += "</tr>"

    # Finish table
    html += "</table>"

    return HTML(html)
