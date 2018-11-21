# Notebooks to reproduce results shown in paper.

1. **01-Figure_InversionCriterium.ipynb**: Figure 1.
2. **02-03-04-Figure_ExampleDesign.ipynb**: Figures 2, 3, and 4.
3. **05-06-Figure_KongKey.ipynb**: Figures 5 and 6.
4. **07-08-Figure_Errors.ipynb**: Figures 7 and 8.
5. **09-Figure_GPR.ipynb**: Figure 9.
6. **10-11_Figure_GPR-f-t.ipynb**: Figures 10 and 11.
7. **A-GPR-create-data.ipynb**: Creation of data for Figures 9-11 (see
   comments below).
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


Some comments regarding `A-GPR-create-data.ipynb`:
- If you want to reproduce the data for `EMmod` too, you will have to install
  `EMmod` as well (see <http://software.seg.org/2015/0001>).
- If you want to run the whole file, including the cell for `EMmod`, the whole
  script will take likely a day to run.
- The required data-zips are provided in the `notebooks/data`-directory on
  <https://github.com/empymod/article-fdesign>, so you can get them there
  instead of running `A-GPR-create-data.ipynb` in order to run
  `09-Figure_GPR.ipynb` and `10-11-Figure_GPR-f-t.ipynb`.
