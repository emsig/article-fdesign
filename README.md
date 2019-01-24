# A tool for designing digital filters for the Hankel and Fourier transforms in potential, diffusive, and wavefield modeling

> Werthmüller, D., K. Key, and E. Slob, 2019, A tool for designing digital
> filters for the Hankel and Fourier transforms in potential, diffusive, and
> wavefield modeling: Geophysics, 84(2), ??-??; DOI:
> [10.1190/geo2018-0069.1](http://doi.org/10.1190/geo2018-0069.1).

## Manuscript for Geophysics paper

Directory contains the LaTeX source of the manuscript as well as the notebooks
to reproduce all the figures.


## History

1. First submitted 22/01/2018 to Geophysics for the Software & Algorithms
   Section. The stable release at the time of submission of `empymod` was
   [Version 1.5.0](https://github.com/empymod/empymod/releases/tag/v1.5.0)
   and of `empyscripts` was
   [Version 0.2.0](https://github.com/empymod/empyscripts/releases/tag/v0.2.0).

    * Re-submitted 22/02/2018. The stable release at the time of submission of
      `empymod` was
      [Version 1.5.0](https://github.com/empymod/empymod/releases/tag/v1.5.0)
      and of `empyscripts` was
      [Version  0.3.0](https://github.com/empymod/empyscripts/releases/tag/v0.3.0).
      There is no difference in the article between the first and the second
      submission. In the first submission only the file `fdesign.py` was
      submitted as source code to Geophysics. The second submission contains a
      zip-file with the current version of `empymod` and `empyscripts` as well
      as all the notebooks to reproduce the figures.

    * Re-submitted 12/03/2018. The only difference is that all binary files
      were replaced by plain ASCII files, due to restrictions by the SEG, and a
      routine to convert the ASCII files into the binary format was added.

2. Re-submitted 19/06/2018. The stable release at the time of submission of
   `empymod` was
   [Version 1.7.1](https://github.com/empymod/empymod/releases/tag/v1.7.1).

3. Final manuscript submitted 21/11/2018. The stable release at the time of
   submission of `empymod` was
   [Version 1.8.1](https://github.com/empymod/empymod/releases/tag/v1.8.1).


## Instructions to reproduce the figures with the zip-file provided by the SEG

The piece of code related to the publication is `fdesign.py`, located in the
folder `notebooks/empymod/scripts` in the zip-file or in the folder
`empymod/scripts` on <https://github.com/empymod/empymod>.

- The zip-file provided by the SEG contains all files required to reproduce the
  figures of the article.
- Have a look at <https://empymod.github.io> for the latest version of
  `empymod`, further instructions, the manual, and many more examples and
  information.
- For a maintained version of the figures in the article see
  <https://github.com/empymod/article-fdesign>.


## Requirements

Required are Python version 3.5 or higher and the modules `NumPy` and `SciPy`
to use `fdesign`. To reproduce the figures with the provided notebooks the
modules `IPython`, `Jupyter`, and `matplotlib` are required additionally.

If you are new to Python I recommend using a Python distribution, which will
ensure that all dependencies are met, specifically properly compiled versions
of `NumPy` and `SciPy`; I recommend using Anaconda, <https://www.anaconda.com>.

The required module `empymod` is included in the provided source code (folder
in which this README resides). Have a look at <https://empymod.github.io> if
you want to install the latest version of them.


## Reproducing

Start `Jupyter` and navigate to the notebooks-folder. The notebooks to
reproduce the figures in the article are:

1. **01-Figure_InversionCriterium.ipynb**: Figure 1.
2. **02-03-04-Figure_ExampleDesign.ipynb**: Figures 2, 3, and 4.
3. **05-06-Figure_KongKey.ipynb**: Figures 5 and 6.
4. **07-08-Figure_Errors.ipynb**: Figures 7 and 8.
5. **09-Figure_GPR.ipynb**: Figure 9.
6. **10-11_Figure_GPR-f-t.ipynb**: Figures 10 and 11.
7. **A-GPR-create-data.ipynb**: Creation of data for Figures 9-11 (see
   comments below).

Some comments regarding `A-GPR-create-data.ipynb`:
- If you want to reproduce the data for `EMmod` too, you will have to install
  `EMmod` as well (see <http://software.seg.org/2015/0001>).
- If you want to run the whole file, including the cell for `EMmod`, the whole
  script will take likely a day to run.
- The required data-zips are provided in the `notebooks/data`-directory on
  <https://github.com/empymod/article-fdesign>, so you can get them there
  instead of running `A-GPR-create-data.ipynb` in order to run
  `09-Figure_GPR.ipynb` and `10-11-Figure_GPR-f-t.ipynb`.

Other notebooks in the notebooks-folder:

8. **AnalyticalTransformPairs.ipynb**: Visual check of all theoretical
   transform pairs included in ``fdesign``.
9. **Errors-AllFilters.ipynb**: Check the errors as in Figure 7 but for all
   filters included in `empymod`.
10. **Example-using-empymod.ipynb**: Create a filter using `empymod` or your own
    theoretical transform pairs.
11. **Filter-wer2001.ipynb**: Creation of the 2001 pt filter.
12. **Filter-wer201-SineCosine.ipynb**: Creation of a 201 pt Fourier filter.
13. **Filter-wer201.ipynb**: Creation of the 201 pt filter.
14. **GPR-RPD.ipynb**: Another error plot for the GPR result.


Maintained versions of the notebooks can be found on
<https://github.com/empymod/article-fdesign>.


## Note

The final edited version is &copy; Society of Exploration Geophysicists SEG.
