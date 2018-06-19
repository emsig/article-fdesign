# Notebooks to reproduce results shown in paper.

1. **Figure-InversionCriterium.ipynb**: Figure 1.
2. **Figure-ExampleDesign.ipynb**: Figures 2, 3, and 4.
3. **Figure-KongKey.ipynb**: Figures 5 and 6.
4. **Figure-Errors.ipynb**: Figures 7 and 8.
5. **GPR-create-data.ipynb**: Creation of data for Figures 9-11 (see comments
   below).
6. **GPR-Figure.ipynb**: Figure 9.
7. **GPR-f-t.ipynb**: Figures 10 and 11.
8. **AnalyticalTransformPairs.ipynb**: Visual check of all theoretical
   transform pairs included in ``fdesign``.
9. **Example-using-empymod.ipynb**: Create a filter using `empymod` or your own
   theoretical transform pairs.
10. **Figure-Errors-AllFilters.ipynb**: Check the errors as in Figure 7 but for
    all filters included in `empymod`.
11. **Filter-wer2001.ipynb**: Creation of the 2001 pt filter.
12. **Filter-wer201.ipynb**: Creation of the 201 pt filter.
13. **Filter-wer201-SineCosine.ipynb**: Creation of a 201 pt Fourier filter.
14. **GPR-Figure-RPD.ipynb**: Another error plot for the GPR result.

Some comments regarding `GPR-create-data.ipynb`:
- If you want to reproduce the data for `EMmod` too, you will have to install
  `EMmod` as well (see <http://software.seg.org/2015/0001>).
- If you want to run the whole file, including the cell for `EMmod`, the whole
  script will take likely a day to run.
- The required data-zips are provided in the `notebooks/data`-directory on
  <https://github.com/empymod/article-fdesign>, so you can get them there
  instead of running `GPR-create-data.ipynb` in order to run `GPR-Figure.ipynb`
  and `GPR-f-t.ipynb`.
