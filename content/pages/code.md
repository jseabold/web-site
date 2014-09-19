Title: Projects

My public projects and those to which I contribute can be found on my [github page](https://www.github.com/jseabold).

- {% code_project http://statsmodels.sf.net, statsmodels, https://www.github.com/statsmodels/statsmodels/, Statsmodels is the main project that I work on. It provides the ability to do statistical modeling in Python. We've been working on it since 2009 and are always looking for good contributions. %}
- {% code_project https://www.github.com/jseabold/wbquery, wbquery, https://www.github.com/jseabold/wbquery/, Wbquery is a Python project for querying the World Bank data API. Data are returned as either pandas Series or DataFrames. There is probably some bit rot in this project. Get in touch with me, if you're interested in pushing this forward. %}
- {% code_project https://www.github.com/jseabold/python-iso3166, python-iso3166, https://www.github.com/jseabold/python-iso3166, This is an implementation of the iso3166 standard for country names. It provides a convenient way to look up a country's name as well as their numeric, alpha-2, and alpha-3 codes. I make some but not much effort to keep this up to date. %}
- {% code_project https://jseabold.github.com/, This Site, https://www.github.com/jseabold/jseabold.github.com, This site was created using [Pelican](http://docs.getpelican.com/en/3.2/). You can browse and fork the source on github. %}


Scripts
=======

My public scripts can all be found on my [gist page](https://gist.github.com/jseabold).

Python
------

- {% code_snippet 1473363, translate.py, Get translations using the Google Translate API. %}
- {% code_snippet 1399100, webuse.py, An implementation of Stata's webuse in Python. This is now included in statsmodels %}
- {% code_snippet 1291003, send_text.py, A context manager that will text you when it is done running some code. %}
- {% code_snippet 5859121, orth_poly.py, A translation of Stata's orthpoly.ado in Python. %}
- {% code_snippet 4669598, spirals.py, Draw spirals in matplotlib. %}
- {% code_snippet 4158367, ungoogle.py, Un-google-ify URLs from Google search. useful for getting the download URL for a pdf, for example. %}

R
--

- {% code_snippet 1160958, R2array.R, Convert R matrices and vectors to numpy arrays. %}

Stata
-----

- {% code_snippet 1160969, mat2nparray.ado, Make a list of Stata matrices importable as Python objects. %}
- {% code_snippet 1602938, bigmat.ado, Put a variable or variable list into a matrix even if it's bigger than matsize. %}
- {% code_snippet 4488712, cls.ado, Clear the screen in the Stata GUI. %}

Bash
----

- {% code_snippet 2989276, rmpy.sh, Shell script to delete Python package from dist-packages. %}
- {% code_snippet 5911795, pushdp.sh, Change to a directory in which a Python package is installed. %}
- {% code_snippet 5911810, prompt.sh, A prompt that includes the GitHub branch that you are on. %}
- {% code_snippet 5911875, alias.sh, Some helpful .bashrc aliases. %}
