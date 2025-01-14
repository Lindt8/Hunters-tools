'''

This Python module contains a collection of my functions which I often utilize in
other scripts and/or are just generally useful and could possibly be useful in the future.

The functions contained in this module and brief descriptions of their functions are included below.

### General Purpose Functions

- `find`                            : return index of the first instance of a value in a list
- `scan_folder_for_file`            : determine if a file is present a folder or any of its subfolders
- `slugify`                         : converts a string to a characterset usable in filenames
- `hex_to_rgb`                      : converts a hexidecimal color string to a RGB tuple
- `rgb_to_hex`                      : converts a RGB tuple to a hexidecimal color string
- `round_up_to_next_multiple`       : rounds a number up to its next multiple of some value
- `round_down_to_next_multiple`     : rounds a number down to its next multiple of some value
- `humansize`                       : converts a number in bytes to a more readable unit (kB, MB, GB, etc.)
- `table_array_generator`           : generates an array of table values and headers
- `Excel_table_generator`           : generates an Excel-formatted (tab-delimited) table string
- `Latex_table_generator`           : generates a LaTeX-formatted table string
- `make_pickle`                     : saves an object to a pickle file
- `read_pickle`                     : retrieves an object from a pickle file

### Science/Engineering Functions

- `time_str_to_sec_multiplier`      : determine multiplier to convert a time unit to seconds
- `seconds_to_dhms`                 : convert a time in seconds to a string of human-relatable time units
- `seconds_to_ydhms`                : convert a time in seconds to a string of human-relatable time units (also with years)
- `seconds_to_human_time`           : convert a time in seconds to the shortest string of human-relatable time units
- `time_units_converter`            : convert a decimal time in one unit to a decimal time in different units
- `SI_prefix_converter`             : returns a multiplier to convert from one SI prefix to another
- `Element_Z_to_Sym`                : returns elemental symbol provided the atomic number Z
- `Element_Sym_to_Z`                : returns an atomic number Z provided the elemental symbol
- `Element_ZorSym_to_name`          : returns a string of the name of an element provided its atomic number Z or symbol
- `Element_ZorSym_to_mass`          : returns the average atomic mass of an element provided its atomic number Z or symbol
- `nuclide_to_Latex_form`           : form a LaTeX-formatted string of a nuclide provided its information
- `nuclide_plain_str_to_latex_str`  : convert a plaintext string for a nuclide to a LaTeX formatted raw string
- `nuclide_plain_str_to_ZZZAAAM`    : convert a plaintext string for a nuclide to an integer ZZZAAAM value
- `ZZZAAAM_to_nuclide_plain_str`    : convert an integer ZZZAAAM value for a nuclide to a plaintext string
- `relative_error_to_N`             : convert a relative uncertainty to an "N" value (analogous to number of counts)
- `N_to_relative_error`             : convert an "N" value (analogous to number of counts) to a relative uncertainty
- `fractional_error`                : calculate the fractional error of a test value relative to a reference value
- `fractional_difference`           : calculate the fractional difference between two values (of equal merit)
- `absolute_difference`             : calculate the difference between a reference and test value
- `quotient`                        : safely divide two values, returning 0 if either the numerator or denominator are 0
- `Lorentz_gamma`                   : determine the Lorentz variable gamma from a velocity in cm/ns
- `Lorentz_B2_from_Tn`              : determine the Lorentz variable beta^2 from a neutron kinetic energy in MeV
- `dist`                            : Cartesian distance between two N-dimensional points
- `curvature`                       : find the curvature (N-2 values) of N 2D Cartesian points
- `circumradius`                    : find the circumradius of 3 2D Cartesian points
- `circumcenter`                    : find the circumcenter of 3 2D Cartesian points
- `circ_solid_angle`                : calculate solid angle of a source as seen by a detector, provided coordinates for all
- `energy_resolution_of_peak`       : calculate energy resolution (& related values) from a spectrum and range of channels
- `eval_distribution`               : evaluate y values of named distribution with provided x and fit parameters
- `fit_distribution`                : determine best fit parameters for a distribution based on initial guesses
- `r_squared`                       : calculate R-squared value between two arrays of y values, experimental and fitted
- `chi_squared`                     : calculate chi-squared value between two arrays of y values, experimental and fitted
- `tally`                           : tally/histogram values (and their indices) falling within a desired binning structure
- `rebinner`                        : rebin a set of y-data to a new x-binning structure (edges not necessarily preserved)
- `calc_GCR_intensity`              : calculate GCR intensity for a provided solar modulation, ion, and energy
- `assemble_GCR_flux`               : assemble GCR spectra for desired elements/ions
- `ICRP116_effective_dose_coeff`    : returns effective dose of a mono-energetic particle of some species and some geometry

### Monte Carlo transport code Functions (PHITS/MCNP)

- `fetch_MC_material`               : returns a string of a formatted material for MCNP or PHITS
- `parse_tally_dump_file`           : parser for dump files from "dump" flag in PHITS [T-Cross], [T-Time], and [T-Track] tallies
- `parse_ttrack_file`               : parser for the [T-Track] output file from PHITS
- `parse_tdeposit_file`             : parser for the [T-Deposit] output file from PHITS
- `parse_dyld_files`                : parser for the *.dyld files from PHITS meant for DCHAIN

### Plotting-related Functions

- `generate_line_bar_coordinates`   : convert a set of bin-wise data to line coordinates to plot normally looking like bars
- `colors_list_6`                   : return 1 of 6 color values from ColorBrewer
- `colors_list_12`                  : return 1 of 12 color values from ColorBrewer
- `colors_list_10`                  : return 1 of 10 color values from the new matplotlib default from v3 1 1
- `colors_list_20`                  : return 1 of 20 color values from a blog post by Sasha Trubetskoy
- `colors_list_64`                  : return 1 of 64 color values from a StackOverflow comment by user Tatarize
- `get_colormap`                    : retrieve a matplotlib colormap using just its string name
- `truncate_colormap`               : truncate a colormap to new upper/lower bounds to a subset of the original colormap
- `add_colorbar_onto_plot`          : overlay a colorbar onto an existing figure with user-specified bounds and values
- `makeErrorBoxes`                  : draw uncertainties as a box surrounding a point (can be used with/instead of crosshair-style error bars)
- `fancy_plot`                      : very comprehensive plotter for 2D datasets, an accumulation of all of my past plotting commands/settings
- `fancy_3D_plot`                   : very comprehensive plotter for 3D datasets on 3D axes, an accumulation of all of my past plotting commands/settings
- `fancy_save_plot`                 : save images of figures in various file formats at once

'''
'''
Each function beings with a comment block containing the following sections:

    Description:
        
    
    Dependencies:
        
    
    Inputs:
        
    
    Outputs:
     
("Dependencies:" is omitted when there are none.)        
'''

import unicodedata as ud
import re
import os
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mticker
from matplotlib import cm
from scipy.interpolate import CubicSpline, lagrange, interp1d
from lmfit.models import GaussianModel

from mpl_toolkits.mplot3d.axis3d import Axis
import matplotlib.projections as proj
from matplotlib.colors import colorConverter, LinearSegmentedColormap
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable

from munch import *
from scipy.optimize import curve_fit
from scipy import stats
from scipy.stats import chisquare
from scipy.io import FortranFile


'''
**************************************************************************************************
----------------------------------- GENERAL PURPOSE FUNCTIONS ------------------------------------
**************************************************************************************************
'''

def find(target, myList):
    '''
    Description:
        Search for and return the index of the first occurance of a value in a list.

    Inputs:
        - `target` = value to be searched for
        - `myList` = list of values

    Output:
        - index of first instance of `target` in `myList`
    '''
    for i in range(len(myList)):
        if myList[i] == target:
            return i

def scan_folder_for_file(path,filename):
    '''
    Description:
        Provided a path to a folder and a filename, determine if the file is present in the folder or any of its subfolders

    Dependencies:
        `import os`

    Inputs:
        - `path` = string, path to folder (containing files, folders, and/or nested subfolders)
        - `filename` = string, filename to search for in folders

    Outputs:
        - logical variable `True` or `False` stating whether the filename exists anywhere in the specified path and it's subdirectories
    '''
    file_found = False
    #for entry in os.scandir(final_exp_folder_path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == filename:
                file_found = True
                return file_found
    return file_found

def slugify(value):
    '''
    Description:
        Normalizes string, converts to lowercase, removes non-alpha characters,and converts spaces to hyphens.
        This is useful for quickly converting TeX strings, plot titles, etc. into legal filenames.

    Dependencies:
        - `import unicodedata as ud`
        - `import re`

    Input:
        - `value` = string to be "slugified"

    Output:
        - `value` converted to a string only consisting of characters legal in filenames
    '''
    old_value = value
    value = str(ud.normalize('NFKD', value).encode('ascii', 'ignore'))
    value = str(re.sub('[^\w\s-]', '', value).strip().lower())
    value = str(re.sub('[-\s]+', '-', value))
    if value[0]=='b' and old_value[0]!='b': value = value[1:] # TeX strings sometimes case resulting string to being with 'b'
    return value

def hex_to_rgb(hexcol,opacity=1.0,out_of_one=False):
    '''
    Description:
        Return (red, green, blue, opacity) for the color given as `#rrggbb` and optional opacity

    Inputs:
        - `hexcol` = string of hexidecimal color formatted as `#rrggbb`
        - `opacity` = float between 0 and 1 specifying color opacity (D=1.0)
        - `out_of_one` = bool which toggles whether output will be out of 255 (default, =`False`) or 1 (=`True`)
                     useful if you'd rather have white be (255,255,255) (default) or (1,1,1)

    Outputs:
        - tuple containing RGB values and opacity,  (red, green, blue, opacity)
    '''
    divisor = 1
    if out_of_one: divisor = 255
    value = hexcol.lstrip('#')
    lv = len(value)
    rgb = (int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    rgb = tuple(rgb)
    rgbo = [rgb[0]/divisor,rgb[1]/divisor,rgb[2]/divisor,opacity]
    return tuple(rgbo)

def rgb_to_hex(rgb):
    '''
    Description:
        Return hexidecimal color string `#rrggbb` for the color given as a tuple (red, green, blue, opacity)

    Inputs:
        - `rgb` = tuple containing RGB values and (optionally) opacity,  (red, green, blue, opacity); note that
                  the opacity value is not preserved when converted to hex

    Outputs:
        - string of hexidecimal color formatted as `#rrggbb`

    Notes:
      Each RGB tuple value needs to be either between 0 and 1 or between 0 and 255.  If no values greater
      than 1 are provided in the rgb tuple, they will be automatically renormalized to 255.
      Additionally, any values outside of the bounds will be reassigned to the nearest bound value.
    '''
    if any(rgb[i]>255 or rgb[i]<0 for i in range(3)):
        print('Warning: Check that rgb values of color tuple are within bounds [0,255].')
    if any(rgb[i]>1 for i in range(3)):
        nrm_fac = 1
    else:
        nrm_fac = 255
    hex_col_str = '#%02x%02x%02x' % (max(0, min(int(nrm_fac*rgb[0]), 255)),max(0, min(int(nrm_fac*rgb[1]), 255)),max(0, min(int(nrm_fac*rgb[2]), 255)))
    return hex_col_str

def round_up_to_next_multiple(value,mult=1):
    '''
    Description:
        Round a number up to its nearest multiple of some value

    Dependencies:
        `import numpy as np`

    Input:
        - `value` = number to be rounded
        - `mult` = multiple to be rounded to (D=1, next higher integer)

    Output:
        - `value` rounded up to its nearest multiple of `mult`
    '''
    round_val = np.ceil(value/mult)*mult
    if isinstance(mult,int) or (abs(round_val)%1<0.01): round_val = int(round_val)
    return round_val

def round_down_to_next_multiple(value,mult=1):
    '''
    Description:
        Round a number down to its nearest multiple of some value

    Dependencies:
        `import numpy as np`

    Input:
        - `value` = number to be rounded
        - `mult` = multiple to be rounded to (D=1, next lower integer)

    Output:
        - `value` rounded down to its nearest multiple of `mult`
    '''
    round_val = np.floor(value/mult)*mult
    if isinstance(mult,int) or (abs(round_val)%1<0.01): round_val = int(round_val)
    return round_val


def humansize(nbytes):
    '''
    Description:
        Provided an integer describing a number of bytes, return a string in more human-readable units

    Dependencies:
        `import numpy as np`

    Input:
        - `nbytes` = integer number of bytes (B)

    Output:
        - string containing the number converted to a human-readable number in *B
    '''
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def table_array_generator(core_table,row_headers=None,row_header_spans=None,column_headers=None,column_header_spans=None,float_formatting='{:g}'):
    '''
    Description:
        Generates a properly populated array which can be easily converted to a table.

    Dependencies:
        `import numpy as np`

    Notes:

       At its core, a table at minimum consists of an array of 1x1 cells.  In addition, it may be padded to
       its left and top with row and column headers, respectively, which may span multiple rows/columns.
       The number of row-header columns or column-header rows can be arbitrary.

    Inputs:
       (required)

       - `core_table` = an RxC array (number of rows x number of columns) or equivalent list of table values constituting
                      the core portion of the table composed of 1x1 cell elements

    Inputs:
       (optional)

       - `row_headers` = A list (or list of lists) of row headers; it must be accompanied by the below variable:
       - `row_header_spans` = A list (or list of lists) of the number of rows each row header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `column_headers` = A list (or list of lists) of column headers; it must be accompanied by the below variable:
       - `column_header_spans` = A list (or list of lists) of the number of column each column header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `float_formatting` = default formatting string for floating point numbers passed to this function (D=`'{:g}'`)

    Outputs:
       - `table_array` = an (R+num_col_heads)x(C+num_row_heads) array of strings forming the table
    '''

    core_num_rows, core_num_cols = np.shape(core_table)
    core_table = np.array(core_table)

    # identify structure of row and column headers, if included
    num_row_header_columns = 0
    if row_headers:
        if not isinstance(row_headers,list):
            print('row_headers is not a list (or list of lists), quitting...')
            return None
        if not row_header_spans:
            print('row_header_spans must also be provided, quitting...')
            return None
        if isinstance(row_headers[0],list):
            num_row_header_columns = len(row_headers)
        else:
            num_row_header_columns = 1

    num_column_header_rows = 0
    if column_headers:
        if not isinstance(column_headers,list):
            print('column_headers is not a list (or list of lists), quitting...')
            return None
        if not column_header_spans:
            print('column_header_spans must also be provided, quitting...')
            return None
        if isinstance(column_headers[0],list):
            num_column_header_rows = len(column_headers)
        else:
            num_column_header_rows = 1

    nrows = core_num_rows + num_column_header_rows
    ncols = core_num_cols + num_row_header_columns

    # initialize table array
    table_array = np.empty((nrows,ncols),dtype=object)
    for ri in range(nrows):
        for ci in range(ncols):
            table_array[ri,ci] = ' '


    # Now populate its values
    # first, put core table into the bottom right of table
    table_array[-core_num_rows:,-core_num_cols:] = core_table

    # then row headers...
    if row_headers:
        for rhi in range(num_row_header_columns-1,-1,-1):
            ci = rhi
            if num_row_header_columns==1:
                this_header_set = row_headers
                this_header_spans = row_header_spans
            else:
                this_header_set = row_headers[rhi]
                this_header_spans = row_header_spans[rhi]

            if not isinstance(this_header_spans,list):
                tmp = this_header_spans
                this_header_spans = [tmp for i in this_header_set]

            if np.sum(this_header_spans) > nrows:
                print('Total span of row headers ({}) exceeds total number of rows calculated ({}); please reassess index {} of row headers lists'.format(str(int(np.sum(this_header_spans))),str(nrows),str(rhi)))
                return None

            ri = nrows
            for hei in range(len(this_header_set)-1,-1,-1):
                ri = ri - this_header_spans[hei]
                if isinstance(this_header_set[hei],str):
                    val = this_header_set[hei]
                elif isinstance(this_header_set[hei],float):
                    val=float_formatting.format(this_header_set[hei])
                else:
                    val = str(this_header_set[hei])
                table_array[ri,ci] = val

    # then column headers...
    if column_headers:
        for chi in range(num_column_header_rows-1,-1,-1):
            ri = chi
            if num_column_header_rows==1:
                this_header_set = column_headers
                this_header_spans = column_header_spans
            else:
                this_header_set = column_headers[chi]
                this_header_spans = column_header_spans[chi]

            if not isinstance(this_header_spans,list):
                tmp = this_header_spans
                this_header_spans = [tmp for i in this_header_set]

            if np.sum(this_header_spans) > ncols:
                print('Total span of column headers ({}) exceeds total number of columns calculated ({}); please reassess index {} of column headers lists'.format(str(int(np.sum(this_header_spans))),str(ncols),str(chi)))
                return None

            ci = ncols
            for hei in range(len(this_header_set)-1,-1,-1):
                ci = ci - this_header_spans[hei]
                if isinstance(this_header_set[hei],str):
                    val = this_header_set[hei]
                elif isinstance(this_header_set[hei],float):
                    val=float_formatting.format(this_header_set[hei])
                else:
                    val = str(this_header_set[hei])
                table_array[ri,ci] = val


    return table_array


def Excel_table_generator(core_table,title=None,row_headers=None,row_header_spans=None,column_headers=None,column_header_spans=None,float_formatting='{:g}'):
    '''
    Description:
        This function generates a string containing a Excel-formatted (tab delimited) table from an input array supplemented with
        other formatting and header information.

    Dependencies:
        - `import numpy as np`

    Notes:
        At its core, a table at minimum consists of an array of 1x1 cells.  In addition, it may be padded to
        its left and top with row and column headers, respectively, which may span multiple rows/columns.
        The number of row-header columns or column-header rows can be arbitrary.

    Inputs:
       (required)

       - `core_table` = an RxC array (number of rows x number of columns) or equivalent list of table values
                      constituting the core portion of the table composed of 1x1 cell elements

    Inputs:
        (optional)

       - `title` = (optional) string to be placed above the table (D=`None`)
       - `row_headers` = A list (or list of lists) of row headers; it must be accompanied by the below variable:
       - `row_header_spans` = A list (or list of lists) of the number of rows each row header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `column_headers` = A list (or list of lists) of column headers; it must be accompanied by the below variable:
       - `column_header_spans` = A list (or list of lists) of the number of column each column header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `float_formatting` = default formatting string for floating point numbers passed to this function (D=`'{:g}'`)

    Outputs:
       - `tab_str` = text string containing the formatted table
    '''

    core_table = np.array(core_table)
    if row_headers or column_headers: # need to generate comprehensive table array using headers and provided core array
        table_array = table_array_generator(core_table,row_headers=row_headers,row_header_spans=row_header_spans,column_headers=column_headers,column_header_spans=column_header_spans,float_formatting=float_formatting)
    else:
        table_array = core_table

    num_rows, num_cols = np.shape(table_array)

    tab_str = ''
    for ri in range(num_rows):
        for ci in range(num_cols):
            if isinstance(table_array[ri,ci],str):
                val = table_array[ri,ci]
            elif isinstance(table_array[ri,ci],float):
                val=float_formatting.format(table_array[ri,ci])
            else:
                val = str(table_array[ri,ci])
            tab_str += val + '\t'
        tab_str = tab_str[:-1] +  '\n'
    if title:
        tab_str = title + '\n' + tab_str
    return tab_str


def Latex_table_generator(core_table,title=None,row_headers=None,row_header_spans=None,column_headers=None,column_header_spans=None,
                          float_formatting='{:g}',table_positioning='[h]',label=None,use_table_ruling=True,coulmn_formatting=None,
                          hline_row_indices=None,cline_row_cstart_cend_indices_triplets = None,return_only_core_tabular_environment=False,
                          nest_in_ruledtabular=False,colormap=None,color_transform_fcn=None,color_scale='linear',color_min_val=None,color_max_val=None):
    '''
    Description:
        This function generates a string containing a LaTeX-formatted table from an input array supplemented with
        other formatting and header information.

    Dependencies:
        `import numpy as np`

    Notes:
        At its core, a table at minimum consists of an array of 1x1 cells.  In addition, it may be padded to
        its left and top with row and column headers, respectively, which may span multiple rows/columns.
        The number of row-header columns or column-header rows can be arbitrary.

    Inputs:
       (required)

       - `core_table` = an RxC array (number of rows x number of columns) or equivalent list of table values
                      constituting the core portion of the table composed of 1x1 cell elements

    Inputs:
       (optional)

       - `title` = (optional) string to be placed above the table (D=`None`)
       - `row_headers` = A list (or list of lists) of row headers; it must be accompanied by the below variable:
       - `row_header_spans` = A list (or list of lists) of the number of rows each row header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `column_headers` = A list (or list of lists) of column headers; it must be accompanied by the below variable:
       - `column_header_spans` = A list (or list of lists) of the number of column each column header spans.  If these are to
                      be uniform for all entries, a single value (or list of single values) may be provided instead.
       - `float_formatting` = default formatting string for floating point numbers passed to this function (D=`'{:g}'`)
       - `table_positioning` = string of table positioning argument for LaTeX (D=`'[h]'`)
       - `label` = string of table label (D = `slugify(title)`)
       - `use_table_ruling` = boolean controlling automatic use of toprule, midrule, and bottomrule (D=`True`)
       - `coulmn_formatting` = string controlling column borders and justification (D=`'{ccc...ccc}'` (all columns centered))
       - `hline_row_indices` = list (or single) of integer row indices beneath which a hline, spanning all columns,
                      should be drawn (D=`None`) (-1 places line above very first row)
       - `cline_row_cstart_cend_indices_triplets` = list of length-3 lists (or an individual length-3 list) composed of
                      [row index, column start, column end] for the \cline{start-stop} command
       - `return_only_core_tabular_environment` = boolean specifying whether the whole table (`False`) or just the inner
                      tabular environment (`True`) will be returned (D=`False`)
       - `nest_in_ruledtabular` = boolean specifying if the tabular environment will (`True`) or will not (`False`) be
                      nested inside of the ruledtabular environment used by REVTeX (D=`False`)
       - `colormap` = callable colormap object or string of matplotlib colormap name to be used in setting the background
                      color of each cell in the table.  By default, `colormap = None` and the table is produced normally.
                      Otherwise, the specified colormap will be used to color the background of each cell based on its value.
                      For the colors used, the values of `core_table` are rescaled from `[min(core_table),max(core_table)]`
                      to `[0,1]` and then used to sample the provided colormap.  As a special case, if `colormap='default'`
                      then `colormap=truncate_colormap('bwr',0.35,0.65)` is used; ref:`truncate_colormap`
                      Note that in the LaTeX document `\\usepackage[table]{xcolor}` must be included in the preamble for table colors to function.
       - `color_transform_fcn` = user-supplied function called to alter each value of `core_table` used for color assignment, prior to
                      rescaling/normalization.  This only affects color assignment, not the actual value printed to the final table. (D=`None`)
       - `color_scale` = string specifying whether the mapping of colors to the table values should use `'linear'` (default) or `'log'` scaling
       - `color_min_val` = float/int specifying new lower bound of `core_table` to be used in colormap normalization; all values
                      less than or equal to `col_min_val` will be set to 0 in the array used to sample the colormap.
       - `color_max_val` = float/int specifying new upper bound of `core_table` to be used in colormap normalization; all values
                      greater than or equal to `col_max_val` will be set to 1 in the array used to sample the colormap.

    Outputs:
       - `tab_str` = text string containing the formatted table
    '''

    core_table = np.array(core_table)
    core_nrows, core_ncols = np.shape(core_table)
    # ensure everything is sorted nicely into the table array
    table_array = table_array_generator(core_table,row_headers=row_headers,row_header_spans=row_header_spans,column_headers=column_headers,column_header_spans=column_header_spans,float_formatting=float_formatting)
    num_rows, num_cols = np.shape(table_array)
    num_column_header_rows, num_row_header_columns = num_rows-core_nrows, num_cols-core_ncols

    if colormap:
        if isinstance(colormap,str):
            if colormap=='default' or colormap=='Default' or colormap=='DEFAULT':
                cmap = truncate_colormap('bwr', 0.35, 0.65)
            else:
                cmap = get_colormap(cmap)
        else:
            cmap = colormap

        color_val_table = np.copy(core_table)

        if color_transform_fcn!=None: # user supplied function to transform values
            for ri in range(core_nrows):
                for ci in range(core_ncols):
                    color_val_table[ri,ci] = color_transform_fcn(color_val_table[ri,ci])

        if color_min_val==None:
            col_min_val = np.min(color_val_table)
        else:
            col_min_val = color_min_val
        if color_max_val==None:
            col_max_val = np.max(color_val_table)
        else:
            col_max_val = color_max_val

        color_val_table[color_val_table<col_min_val] = col_min_val
        color_val_table[color_val_table>col_max_val] = col_max_val

        if color_scale=='log':
            if np.any(color_val_table<0):
                print('Warning: col_min_val<0 & core_table contains negative values and thus cannot be color scaled logarithmically; reverting to linear color scale.')
            else:
                if np.any(color_val_table==0):
                    print('Warning: core_table contains zero values; they will be ignored while assigning colors.')
                color_val_table[color_val_table==0] = np.nan # set to NaN and use this as a flag to ignore later
                color_val_table = np.log(color_val_table)
                col_min_val = np.log(col_min_val)
                col_max_val = np.log(col_max_val)

        color_val_table = (color_val_table - col_min_val)/(col_max_val - col_min_val)


        # double check values are within bounds
        color_val_table[color_val_table<0] = 0
        color_val_table[color_val_table>1] = 1



    if hline_row_indices:
        if not isinstance(hline_row_indices,list): hline_row_indices = [hline_row_indices]

    if cline_row_cstart_cend_indices_triplets:
        if not isinstance(cline_row_cstart_cend_indices_triplets,list):
            print('cline_row_cstart_cend_indices_triplets elements must be length-3 lists of the row index, starting column, and ending column')
            return None
        if not isinstance(cline_row_cstart_cend_indices_triplets[0],list):
            cline_row_cstart_cend_indices_triplets = [cline_row_cstart_cend_indices_triplets]

    tab_str = ''

    if not return_only_core_tabular_environment:
        tab_str += r'\begin{table}' + table_positioning + '\n'
        #tab_str += r'%\vspace*{-0.4cm}' + '\n'
        if title:
            tab_str += '\t' + r'\caption{'+title+'}' + '\n'
        else:
            tab_str += '\t' + r'%\caption{Title}' + '\n'
        if label:
            tab_str += '\t' + r'\label{tab:'+label+'}' + '\n'
        elif title:
            tab_str += '\t' + r'\label{tab:'+slugify(title)+'}' + '\n'
        else:
            tab_str += '\t' + r'%\label{tab:Label}' + '\n'
        tab_str += '\t' + r'\centering' + '\n'

    if nest_in_ruledtabular:
        tab_str += '\t' + r'\begin{ruledtabular}' + '\n'

    if coulmn_formatting:
        tab_str += '\t' + r'\begin{tabular}' + coulmn_formatting + '\n'
    else:
        cstr = 'c'*num_cols
        tab_str += '\t' + r'\begin{tabular}{'+cstr+'}' + '\n'

    if use_table_ruling: tab_str += '\t\t' + r'\toprule' + '\n'

    if hline_row_indices:
        if -1 in hline_row_indices: tab_str += '\t\t' + r'\hline' + '\n'


    chi_list = [0 for i in range(num_row_header_columns)]
    for ri in range(num_rows):
        line = ''

        # handle header row separately
        if ri < num_column_header_rows:
            if num_column_header_rows==1:
                this_header_set = column_headers
                this_header_spans = column_header_spans
            else:
                this_header_set = column_headers[ri]
                this_header_spans = column_header_spans[ri]

            if not isinstance(this_header_spans,list):
                tmp = this_header_spans
                this_header_spans = [tmp for i in this_header_set]

            for hi in range(len(this_header_set)-1,-1,-1):
                if this_header_spans[hi] == 1:
                    line = this_header_set[hi] + ' & ' + line
                else:
                    line = r'\multicolumn{'+'{}'.format(this_header_spans[hi])+'}{c}{' + this_header_set[hi] + '} & ' + line

            if np.sum(this_header_spans) < num_cols:
                for i in range(num_cols-int(np.sum(this_header_spans))):
                    line = ' & ' + line

            tab_str += '\t\t' + line[:-2] + ' \\\\' + '\n'

            if hline_row_indices:
                if ri in hline_row_indices:
                    tab_str += '\t\t' + r'\hline' + '\n'

            if cline_row_cstart_cend_indices_triplets:
                for i in range(len(cline_row_cstart_cend_indices_triplets)):
                    if ri == cline_row_cstart_cend_indices_triplets[i][0]:
                        tab_str += '\t\t' + r'\cline{' + '{}-{}'.format(str(int(cline_row_cstart_cend_indices_triplets[i][1])),str(int(cline_row_cstart_cend_indices_triplets[i][2]))) + '}' + '\n'


            continue

        if use_table_ruling and ri==num_column_header_rows and num_column_header_rows>0:
            tab_str += '\t\t' + r'\midrule' + '\n'


        for ci in range(num_cols):
            val = table_array[ri,ci]
            if not isinstance(val,str): val = float_formatting.format(val)

            # add multicolumns where appropriate
            if ci < num_row_header_columns:
                if num_row_header_columns==1:
                    this_header_set = row_headers
                    this_header_spans = row_header_spans
                else:
                    this_header_set = row_headers[ci]
                    this_header_spans = row_header_spans[ci]

                if not isinstance(this_header_spans,list):
                    tmp = this_header_spans
                    this_header_spans = [tmp for i in this_header_set]

                if val != ' ' and this_header_spans[ci]>1:
                    line += r'\multirow{'+'{}'.format(this_header_spans[chi_list[ci]])+'}{*}{' + this_header_set[chi_list[ci]] + '} & '
                    chi_list[ci] += 1
                else:
                    line += val + ' & '
                continue

            if colormap:
                if not np.isnan(color_val_table[ri-num_column_header_rows,ci-num_row_header_columns]): # skip zero values assigned NaN when log scaled
                    col_rgb = cmap(color_val_table[ri-num_column_header_rows,ci-num_row_header_columns])
                    col_hex = rgb_to_hex(col_rgb)[1:] # remove leading '#' character
                    line += r'\cellcolor[HTML]{'+col_hex+'} '

            line += val + ' & '

        tab_str += '\t\t' + line[:-2] + ' \\\\' + '\n'

        if hline_row_indices:
            if ri in hline_row_indices:
                tab_str += '\t\t' + r'\hline' + '\n'

        if cline_row_cstart_cend_indices_triplets:
            for i in range(len(cline_row_cstart_cend_indices_triplets)):
                if ri == cline_row_cstart_cend_indices_triplets[i][0]:
                    tab_str += '\t\t' + r'\cline{' + '{}-{}'.format(str(int(cline_row_cstart_cend_indices_triplets[i][1])),str(int(cline_row_cstart_cend_indices_triplets[i][2]))) + '}' + '\n'


    if use_table_ruling: tab_str += '\t\t' + r'\bottomrule' + '\n'

    tab_str += '\t' + r'\end{tabular}' + '\n'
    if nest_in_ruledtabular:
        tab_str += '\t' + r'\end{ruledtabular}' + '\n'
    if not return_only_core_tabular_environment:
        tab_str += r'\end{table}' + '\n'
    if return_only_core_tabular_environment:
        tab_str = tab_str[1:].replace('\n\t','\n') # remove extra tab character from start of each line

    return tab_str

def make_pickle(path_to_pickle_file, object_to_be_pickled):
    '''
    Description:
        Save a provided object to a provided filepath as a pickle file.

    Dependencies:
        `import pickle`

    Input:
        - `path_to_pickle_file` = File path to where the pickle file should be saved
        - `object_to_be_pickled` = Object (array, dict, list, etc.) to be pickled.

    Output:
        - (none)
    '''
    with open(path_to_pickle_file, 'wb') as handle:
        pickle.dump(object_to_be_pickled, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print('Pickle file written:', path_to_pickle_file, '\n')
    return

import numpy as np
import os
import sys
import pickle
import time

def read_pickle(path_to_pickle_file):
    '''
    Description:
        Save a provided object to a provided filepath as a pickle file.

    Dependencies:
        `import pickle`

    Input:
        - `path_to_pickle_file` = File path to where the pickle file is saved

    Output:
        - `extracted_data_from_pickle` = Object with contents of the pickle file
    '''
    with open(path_to_pickle_file, 'rb') as handle:
        extracted_data_from_pickle = pickle.load(handle)
    return extracted_data_from_pickle

'''
**************************************************************************************************
-------------------------------- SCIENCE/ENGINEERING FUNCTIONS -----------------------------------
**************************************************************************************************
'''


def time_str_to_sec_multiplier(time_str):
    '''
    Description:
        Provide a time unit and this function provides what those time units need to be multiplied by to obtain seconds.

    Inputs:
        - `time_str` = string containing time units character(s) [s,m,h,d,y,ms,us,ns,ps,fs]

    Outputs:
        - `m` = multiplier to convert a time of the supplied units to seconds

    '''
    try:
        if time_str == 's':
            m = 1
        elif time_str == 'm':
            m = 60
        elif time_str == 'h':
            m = 60*60
        elif time_str == 'd':
            m = 60*60*24
        elif time_str == 'y':
            m = 60*60*24*365.25
        elif time_str == 'ms':
            m = 1e-3
        elif time_str == 'us':
            m = 1e-6
        elif time_str == 'ns':
            m = 1e-9
        elif time_str == 'ps':
            m = 1e-12
        elif time_str == 'fs':
            m = 1e-15
        return m
    except:
        print('"{}" is not a valid time unit; please use one of the following: [s,m,h,d,y,ms,us,ns,ps,fs]'.format(time_str))
        return None

def seconds_to_dhms(t_sec):
    '''
    Description:
        Provide a time in seconds and obtain a string with the time in days, hours, minutes, and seconds

    Inputs:
        - `t_sec` = a time in seconds (float or int)

    Outputs:
        - `time_str` = string containing the time prettily formatted in d/h/m/s format

    '''
    m, s = divmod(t_sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d != 0:
        time_str = "{:0.0f}d {:0.0f}h {:0.0f}m {:0.2f}s".format(d,h,m,s)
    elif h != 0:
        time_str = "{:0.0f}h {:0.0f}m {:0.2f}s".format(h,m,s)
    elif m != 0:
        time_str = "{:0.0f}m {:0.2f}s".format(m,s)
    elif s != 0:
        time_str = "{:0.2f}s".format(s)
    else:
        time_str = ""

    return time_str

def seconds_to_ydhms(t_sec):
    '''
    Description:
        Provide a time in seconds and obtain a string with the time in years, days, hours, minutes, and seconds

    Inputs:
        - `t_sec` = a time in seconds (float or int)

    Outputs:
        - `time_str` = string containing the time prettily formatted in y/d/h/m/s format

    '''
    m, s = divmod(t_sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    if y>=4 : # if leap year occurred
        n_leap_years = int(y/4)
        d = d-n_leap_years

    if y != 0:
        time_str = "{:0.0f}y {:0.0f}d {:0.0f}h {:0.0f}m {:0.2f}s".format(y,d,h,m,s)
    elif d != 0:
        time_str = "{:0.0f}d {:0.0f}h {:0.0f}m {:0.2f}s".format(d,h,m,s)
    elif h != 0:
        time_str = "{:0.0f}h {:0.0f}m {:0.2f}s".format(h,m,s)
    elif m != 0:
        time_str = "{:0.0f}m {:0.2f}s".format(m,s)
    elif s != 0:
        time_str = "{:0.2f}s".format(s)
    else:
        time_str = ""

    return time_str

def seconds_to_human_time(t_sec,time_style='mixed',abbreviation_style='shortest'):
    '''
    Description:
        Provide a time in seconds and obtain a string with the time in years, days, hours, minutes, and seconds,
        presented in the shortest and most human-friendly/readable format

    Inputs:
        (required)

        - `t_sec` = a time in seconds (float or int)

    Inputs:
        (optional)

        - `time_style` = string denoting whether times are split into mixed units (`'mixed'`, default, e.g. `1d 12h`),
                         one value in the largest units (`'single_largest'`, e.g. `1.5d`), or one value in the largest
                         integer units (`'single_integer'`, e.g. `36h`)
        - `abbreviation_style` = string denoting style of abbreviation (D=`'shortest'`); select from: [`'shortest'`,`'normal'`,`'none'`],
                         for example: h/hr(s)/hour(s), m/min/minute(s)

    Outputs:
        - `time_str` = string containing the time prettily formatted in the selected format

    '''

    if abbreviation_style=='shortest':
        tu_strs = ['s','m','h','d','y']
    elif abbreviation_style=='normal':
        tu_strs = [' sec',' min',' hr',' day',' yr']
    elif abbreviation_style=='none':
        tu_strs = [' second',' minute',' hour',' day',' year']
    else:
        print('Check value of "abbreviation_style"; assuming "shortest" was intended.')
        abbreviation_style = 'shortest'
        tu_strs = ['s','m','h','d','y']

    m, s = divmod(t_sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    if y>=4 : # if leap year occurred
        n_leap_years = int(y/4)
        d = d-n_leap_years

    time_str = ''

    if time_style=='single_integer':
        divs = [60,60,24,365.25]
        t = t_sec
        for i in range(len(divs)):
            t_new = t/divs[i]
            if not t_new.is_integer():
                time_str = "{:8.4g}{:}".format(t,tu_strs[i])
                if t>1.0 and ((abbreviation_style=='normal' and i!=0 and i!=1) or abbreviation_style=='none'):
                    time_str += 's'
                break
            else:
                t = t_new

    elif time_style=='single_largest':
        divs = [365.25,24,60,60]
        t_yr = t_sec/(60*60*24*365.25)
        t = t_yr
        for i in range(len(divs)+1):
            if round(t,6)>=1.0:
                time_str = "{:8.4g}{:}".format(t,tu_strs[4-i])
                if t>1.0 and ((abbreviation_style=='normal' and i!=4 and i!=3) or abbreviation_style=='none'):
                    time_str += 's'
                break
            else:
                t = t*divs[i]

    else:
        vals = [y,d,h,m,s]
        for vi in range(len(vals)):
            if vals[vi] != 0:
                if vi==4:
                    time_str += " {:0.2g}{:}".format(vals[vi],tu_strs[4-vi]) # 4 = number of total time units - 1
                else:
                    time_str += " {:0.0g}{:}".format(vals[vi],tu_strs[4-vi]) # 4 = number of total time units - 1
                # make units plural if warranted
                if vals[vi]>1.0 and ((abbreviation_style=='normal' and vi!=4 and vi!=3) or abbreviation_style=='none'):
                    time_str += 's'

    if time_str=='': time_str = '0{:}'.format(tu_strs[0])
    time_str = time_str.strip()

    return time_str

def time_units_converter(t1_val,t1_units='s',t2_units='s'):
    '''
    Description:
        Provide a decimal time, its current units, and the desired units to obtain a new decimal time in the desired units

    Inputs:
        - `t1_val` = a decimal time value (float or int)
        - `t1_units` = (optional) a time units string for the input time value (D=`'s'`); select from: `['s','m','h','d','y','ms','us','ns','ps','fs']` (str)
        - `t2_units` = (optional) a time units string for the output time value (D=`'s'`); select from: `['s','m','h','d','y','ms','us','ns','ps','fs']` (str)

    Outputs:
        - `t2_val` = a decimal time value in the units specified by `t2_units` (float)

    '''
    t1_sec = t1_val*time_str_to_sec_multiplier(t1_units)
    t2_val = t1_sec/time_str_to_sec_multiplier(t2_units)

    return t2_val

def SI_prefix_converter(SI1,SI2=''):
    '''
    Description:
        Provides the multiplication constant needed to convert between SI prefixes

    Dependencies:
        `find` (function within the "Hunter's tools" package)

    Inputs:
        - `SI1` = string of SI prefix of the current value
        - `SI2` = string of the desired SI prefix of the value (D=`''`, no SI prefix)

          These values should be selected from this list:
            `['y', 'z', 'a', 'f', 'p', 'n', 'u', 'm', 'c', 'd', '', 'da', 'h', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']`

    Outputs:
        - `m` = multiplier to convert a value of SI prefix `SI1` to one of SI prefix `SI2`

    '''
    SI_prefixes = ['y','z','a','f','p','n','u','m','c','d','','da','h','k','M','G','T','P','E','Z','Y']
    SI_powers   = [-24,-21,-18,-15,-12, -9, -6, -3, -2, -1, 0,   1,  2,  3,  6,  9, 12, 15, 18, 21, 24]
    if SI1 not in SI_prefixes or SI2 not in SI_prefixes:
        if SI1 not in SI_prefixes and SI2 not in SI_prefixes:
            pstr = 'Both SI1={} and SI2={} are not valid entries.'.format(SI1,SI2)
        elif SI1 not in SI_prefixes:
            pstr = 'SI1={} is not a valid entry.'.format(SI1)
        elif SI1 not in SI_prefixes:
            pstr = 'SI2={} is not a valid entry.'.format(SI2)
        pstr += '\nPlease select from the valid SI prefixes:'
        print(pstr,SI_prefixes)
        return None
    v1=SI_powers(find(SI1))
    v2=SI_powers(find(SI2))
    m = 10**(v2-v1)
    return m

def Element_Z_to_Sym(Z):
    '''
    Description:
        Returns elemental symbol for a provided atomic number Z

    Inputs:
        - `Z` = atomic number

    Outputs:
        - `sym` = string of elemental symbol for element of atomic number Z
    '''
    elms = ["n ",\
            "H ","He","Li","Be","B ","C ","N ","O ","F ","Ne",\
            "Na","Mg","Al","Si","P ","S ","Cl","Ar","K ","Ca",\
            "Sc","Ti","V ","Cr","Mn","Fe","Co","Ni","Cu","Zn",\
            "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y ","Zr",\
            "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",\
            "Sb","Te","I ","Xe","Cs","Ba","La","Ce","Pr","Nd",\
            "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",\
            "Lu","Hf","Ta","W ","Re","Os","Ir","Pt","Au","Hg",\
            "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",\
            "Pa","U ","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",\
            "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",\
            "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
    i = int(Z)
    if i < 0 or i > len(elms):
        print('Z={} is not valid, please select a number from 0 to 118 (inclusive).'.format(str(Z)))
        return None
    return elms[i].strip()

def Element_Sym_to_Z(sym):
    '''
    Description:
        Returns atomic number Z for a provided elemental symbol

    Dependencies:
        `find` (function within the "Hunter's tools" package)

    Inputs:
        - `sym` = string of elemental symbol for element of atomic number Z

    Outputs:
        - `Z` = atomic number
    '''
    elms = ["n ",\
            "H ","He","Li","Be","B ","C ","N ","O ","F ","Ne",\
            "Na","Mg","Al","Si","P ","S ","Cl","Ar","K ","Ca",\
            "Sc","Ti","V ","Cr","Mn","Fe","Co","Ni","Cu","Zn",\
            "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y ","Zr",\
            "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",\
            "Sb","Te","I ","Xe","Cs","Ba","La","Ce","Pr","Nd",\
            "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",\
            "Lu","Hf","Ta","W ","Re","Os","Ir","Pt","Au","Hg",\
            "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",\
            "Pa","U ","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",\
            "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",\
            "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]

    if len(sym.strip())>2:
        print('Please provide a valid elemental symbol (1 or 2 characters), {} is too long'.format(sym))
        return -1

    # handle exception for neutron first
    if sym.strip()=='XX':
        return 0

    # make sure string is formatted to match entries in elms list
    sym2 = sym.strip()
    if len(sym2)==1: sym2 += ' '
    sym2 = sym2[0].upper() + sym2[1].lower()

    Z = find(sym2,elms)

    if Z==None:
        print('Z could not be found for element "{}"; please make sure entry is correct.'.format(sym))
        return -1

    return Z

def Element_ZorSym_to_name(Z):
    '''
    Description:
        Returns an element's name provided its atomic number Z or elemental symbol

    Inputs:
        - `Z` = string of elemental symbol or atomic number Z

    Outputs:
        - `name` = element name
    '''
    element_names = ['neutron','Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Fluorine',
                     'Neon','Sodium','Magnesium','Aluminium','Silicon','Phosphorus','Sulfur','Chlorine','Argon',
                     'Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt',
                     'Nickel','Copper','Zinc','Gallium','Germanium','Arsenic','Selenium','Bromine','Krypton',
                     'Rubidium','Strontium','Yttrium','Zirconium','Niobium','Molybdenum','Technetium','Ruthenium',
                     'Rhodium','Palladium','Silver','Cadmium','Indium','Tin','Antimony','Tellurium','Iodine','Xenon',
                     'Caesium','Barium','Lanthanum','Cerium','Praseodymium','Neodymium','Promethium','Samarium',
                     'Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium',
                     'Lutetium','Hafnium','Tantalum','Tungsten','Rhenium','Osmium','Iridium','Platinum','Gold',
                     'Mercury','Thallium','Lead','Bismuth','Polonium','Astatine','Radon','Francium','Radium',
                     'Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium',
                     'Berkelium','Californium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium',
                     'Rutherfordium','Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadtium',
                     'Roentgenium','Copernicium','Nihonium','Flerovium','Moscovium','Livermorium','Tennessine','Oganesson']

    try:
        zi = int(Z)
    except:
        zi = Element_Sym_to_Z(Z)

    return element_names[zi]

def Element_ZorSym_to_mass(Z):
    '''
    Description:
        Returns an element's average atomic mass provided its atomic number Z or elemental symbol

    Inputs:
        - `Z` = string of elemental symbol or atomic number Z

    Outputs:
        - `A_avg` = average atomic mass
    '''

    average_atomic_masses = [1.008664,1.007,4.002602,6.941,9.012182,10.811,12.0107,14.0067,15.9994,18.9984032,
                             20.1797,22.98976928,24.305,26.9815386,28.0855,30.973762,32.065,35.453,39.948,39.0983,
                             40.078,44.955912,47.867,50.9415,51.9961,54.938045,55.845,58.933195,58.6934,63.546,65.38,
                             69.723,72.63,74.9216,78.96,79.904,83.798,85.4678,87.62,88.90585,91.224,92.90638,95.96,98,
                             101.07,102.9055,106.42,107.8682,112.411,114.818,118.71,121.76,127.6,126.90447,131.293,
                             132.9054519,137.327,138.90547,140.116,140.90765,144.242,145,150.36,151.964,157.25,
                             158.92535,162.5,164.93032,167.259,168.93421,173.054,174.9668,178.49,180.94788,183.84,
                             186.207,190.23,192.217,195.084,196.966569,200.59,204.3833,207.2,208.9804,209,210,222,
                             223,226,227,232.03806,231.03588,238.02891,237,244,243,247,247,251,252,257,258,259,
                             266,267,268,269,270,277,278,281,282,285,286,289,290,293,294,294]

    try:
        zi = int(Z)
    except:
        zi = Element_Sym_to_Z(Z)

    return average_atomic_masses[zi]

def nuclide_to_Latex_form(Z,A,m=''):
    '''
    Description:
        Form a LaTeX-formatted string of a nuclide provided its information

    Dependencies:
        `Element_Z_to_Sym` (function within the "Hunter's tools" package)
        (only required if inputed Z is not already an elemental symbol)

    Inputs:
        - `Z` = atomic number of nuclide (int, float, or string) or elemental symbol (string)
        - `A` = atomic mass of nuclide (int, float, or string) or string to go in place of A (ex. 'nat')
        - `m` = metastable state (D='', ground state); this will be appended to the end of A
              if not a string already, it will be converted into one and appended to 'm' (ex. 1 -> 'm1')

    Outputs:
        - LaTeX-formatted raw string of a nuclide, excellent for plot titles, labels, and auto-generated LaTeX documents
    '''
    if isinstance(A,(int,float)): A = str(int(A))
    if not isinstance(Z,str): symbol = Element_Z_to_Sym(int(Z))
    if isinstance(m,float): m = int(m)
    if isinstance(m,int): m = 'm' + str(m)
    latex_str = r"$^{{{}{}}}$".format(A,m) + "{}".format(symbol)
    return latex_str

def nuclide_plain_str_to_latex_str(nuc_str,include_Z=False):
    '''
    Description:
        Converts a plaintext string of a nuclide to a LaTeX-formatted raw string
        Note: if you already have the Z, A, and isomeric state information determined, the "nuclide_to_Latex_form" function can be used instead

    Dependencies:
        - `Element_Z_to_Sym` (function within the "Hunter's tools" package) (only required if `include_Z = True`)

    Input:
        (required)

       - `nuc_str` = string to be converted; a huge variety of formats are supported, but they all must follow the following rules:
           + Isomeric/metastable state characters must always immediately follow the atomic mass characters.
               Isomeric state labels MUST either:
               - (1) be a single lower-case character OR
               - (2) begin with any non-numeric character and end with a number
           + Atomic mass numbers must be nonnegative integers OR the string `"nat"` (in which case no metastable states can be written)
           + Elemental symbols MUST begin with an upper-case character

    Input:
       (optional)

       - `include_Z` = `True`/`False` determining whether the nuclide's atomic number Z will be printed as a subscript beneath the atomic mass

    Output:
        - LaTeX-formatted raw string of nuclide
    '''
    tex_str = r''

    # remove unwanted characters from provided string
    delete_characters_list = [' ', '-', '_']
    for dc in delete_characters_list:
        nuc_str = nuc_str.replace(dc,'')

    # determine which characters are letters versus numbers
    isalpha_list = []
    isdigit_list = []
    for c in nuc_str:
        isalpha_list.append(c.isalpha())
        isdigit_list.append(c.isdigit())

    symbol = ''
    mass = ''
    isost = ''

    # string MUST begin with either mass number or elemental symbol
    if isdigit_list[0] or nuc_str[0:3]=='nat': # mass first
        mass_first = True
    else:
        mass_first = False

    if mass_first:
        if nuc_str[0:3]=='nat':
            mass = 'nat'
            ci = 3
        else:
            ci = 0
            while isdigit_list[ci]:
                mass += nuc_str[ci]
                ci += 1
            mass = str(int(mass)) # eliminate any extra leading zeros
            # encountered a non-numeric character, end of mass
            # now, determine if metastable state is listed or if element is listed next
            # first, check to see if any other numerals are in string
            lni = 0 # last numeral index
            for i in range(ci,len(nuc_str)):
                if isdigit_list[i]:
                    lni = i
            if lni != 0:
                # grab all characters between ci and last numeral as metastable state
                isost = nuc_str[ci:lni+1]
                ci = lni + 1
            else: # no more numerals in string, now check for single lower-case letter
                if isalpha_list[ci] and nuc_str[ci].islower():
                    isost = nuc_str[ci]
                    ci += 1

            # Now extract elemental symbol
            for i in range(ci,len(nuc_str)):
                if isalpha_list[i]:
                    symbol += nuc_str[i]

    else: # if elemental symbol is listed first
        if 'nat' in nuc_str:
            mass = 'nat'
            nuc_str = nuc_str.replace('nat','')

        ci = 0
        # Extract all characters before first number as the elemental symbol
        while nuc_str[ci].isalpha():
            symbol += nuc_str[ci]
            ci += 1

        # now, extract mass
        if mass != 'nat':
            while nuc_str[ci].isdigit():
                mass += nuc_str[ci]
                ci += 1
                if ci == len(nuc_str):
                    break

            # lastly, extract isomeric state, if present
            if ci != len(nuc_str):
                isost = nuc_str[ci:]

    # treating the cases of lowercase-specified particles (n, d, t, etc.)
    if symbol == '' and isost != '':
        symbol = isost
        isost = ''

    # Now assemble LaTeX string for nuclides
    if include_Z:
        if symbol == 'n':
            Z = 0
        elif symbol == 'p' or symbol == 'd' or symbol == 't':
            Z = 1
        else:
            Z = Element_Sym_to_Z(symbol)
        Z = str(int(Z))
        tex_str = r"$^{{{}{}}}_{{{}}}$".format(mass,isost,Z) + "{}".format(symbol)
    else:
        tex_str = r"$^{{{}{}}}$".format(mass,isost) + "{}".format(symbol)

    return tex_str

def nuclide_plain_str_to_ZZZAAAM(nuc_str):
    '''
    Description:
        Converts a plaintext string of a nuclide to an integer ZZZAAAM = 10000\*Z + 10\*A + M

    Dependencies:
        `Element_Z_to_Sym` (function within the "Hunter's tools" package)

    Input:
       - `nuc_str` = string to be converted; a huge variety of formats are supported, but they all must follow the following rules:
           + Isomeric/metastable state characters must always immediately follow the atomic mass characters.
               Isomeric state labels MUST either:
               - (1) be a single lower-case character OR
               - (2) begin with any non-numeric character and end with a number
           + Atomic mass numbers must be nonnegative integers OR the string "nat" (in which case no metastable states can be written)
           + Elemental symbols MUST begin with an upper-case character


    Output:
        - ZZZAAAM integer
    '''

    # remove unwanted characters from provided string
    delete_characters_list = [' ', '-', '_']
    for dc in delete_characters_list:
        nuc_str = nuc_str.replace(dc,'')

    # determine which characters are letters versus numbers
    isalpha_list = []
    isdigit_list = []
    for c in nuc_str:
        isalpha_list.append(c.isalpha())
        isdigit_list.append(c.isdigit())

    symbol = ''
    mass = ''
    isost = ''

    if 'nat' in nuc_str:
        print('Must specify a specific nuclide, not natural abundances')
        return None

    # string MUST begin with either mass number or elemental symbol
    if isdigit_list[0]: # mass first
        mass_first = True
    else:
        mass_first = False

    if mass_first:
        ci = 0
        while isdigit_list[ci]:
            mass += nuc_str[ci]
            ci += 1
        mass = str(int(mass)) # eliminate any extra leading zeros
        # encountered a non-numeric character, end of mass
        # now, determine if metastable state is listed or if element is listed next
        # first, check to see if any other numerals are in string
        lni = 0 # last numeral index
        for i in range(ci,len(nuc_str)):
            if isdigit_list[i]:
                lni = i
        if lni != 0:
            # grab all characters between ci and last numeral as metastable state
            isost = nuc_str[ci:lni+1]
            ci = lni + 1
        else: # no more numerals in string, now check for single lower-case letter
            if isalpha_list[ci] and nuc_str[ci].islower():
                isost = nuc_str[ci]
                ci += 1

        # Now extract elemental symbol
        for i in range(ci,len(nuc_str)):
            if isalpha_list[i]:
                symbol += nuc_str[i]

    else: # if elemental symbol is listed first
        ci = 0
        # Extract all characters before first number as the elemental symbol
        while nuc_str[ci].isalpha():
            symbol += nuc_str[ci]
            ci += 1

        # now, extract mass
        while nuc_str[ci].isdigit():
            mass += nuc_str[ci]
            ci += 1
            if ci == len(nuc_str):
                break

        # lastly, extract isomeric state, if present
        if ci != len(nuc_str):
            isost = nuc_str[ci:]

    # treating the cases of lowercase-specified particles (n, d, t, etc.)
    if symbol == '' and isost != '':
        symbol = isost
        isost = ''


    if symbol == 'n':
        Z = 0
    elif symbol == 'p' or symbol == 'd' or symbol == 't':
        Z = 1
    else:
        Z = Element_Sym_to_Z(symbol)

    A = int(mass)

    if isost.strip()=='' or isost=='g':
        M = 0
    elif isost=='m' or isost=='m1':
        M = 1
    elif isost=='n' or isost=='m2':
        M = 2
    elif isost=='o' or isost=='m3':
        M = 3
    elif isost=='p' or isost=='m4':
        M = 4
    elif isost=='q' or isost=='m5':
        M = 5
    else:
        print("Unknown isomeric state {}, assumed ground state".format(isost))
        M = 0

    ZZZAAAM = 10000*Z + 10*A + M

    return ZZZAAAM
nuclide_plain_str_ZZZAAAM = nuclide_plain_str_to_ZZZAAAM # backwards compatibility with old version of function name


def ZZZAAAM_to_nuclide_plain_str(ZZZAAAM,include_Z=False,ZZZAAA=False,delimiter='-'):
    '''
    Description:
        Converts a plaintext string of a nuclide to an integer ZZZAAAM = 10000\*Z + 10\*A + M

    Dependencies:
        `Element_Z_to_Sym` (function within the "Hunter's tools" package)

    Input:
       - `ZZZAAAM` = integer equal to 10000*Z + 10*A + M, where M designates the metastable state (0=ground)
       - `include_Z` = Boolean denoting whether the Z number should be included in the output string (D=`False`)
       - `ZZZAAA` = Boolean denoting whether the input should be interpreted as a ZZZAAA value (1000Z+A) instead (D=`False`)
       - `delimiter` = string which will be used to separate elements of the output string (D=`-`)

    Output:
       - `nuc_str` = string describing the input nuclide formatted as [Z]-[Symbol]-[A][m]
    '''
    ZZZAAAM = int(ZZZAAAM)
    if ZZZAAA:
        ZZZAAAM = ZZZAAAM*10
    m = ZZZAAAM % 10
    A = (ZZZAAAM % 10000) // 10
    Z = ZZZAAAM // 10000
    symbol = Element_Z_to_Sym(Z)

    m_str = ''
    if m>0:
        m_str = 'm' + str(m)

    nuc_str = ''
    if include_Z:
        nuc_str += str(Z) + delimiter
    nuc_str += symbol + delimiter + str(A) + m_str

    return nuc_str


def relative_error_to_N(relerr):
    '''
    Description:
        Convert a relative uncertainty to a "N" value
    Inputs:
      - `relerr` = a relative uncertainty
    Outputs:
      - `N` = "number of counts"-like number
    '''
    if relerr == 0:
        N = 0
    else:
        N = (1/(relerr**2))
    return N

def N_to_relative_error(N):
    '''
    Description:
        Convert an "N" value to a relative uncertainty
    Inputs:
      - `N` = "number of counts"-like number
    Outputs:
      - `relerr` = a relative uncertainty
    '''
    if N == 0: # or N < 0:
        relerr = 0
    else:
        relerr = (1/(N**0.5))
    return relerr

def fractional_error(test_val,ref_val):
    '''
    Description:
        Calculate fractional error of an experimental test value relative to a reference value
    Inputs:
      - `test_val` = new/tested/experimental value (`float` ot `int`)
      - `ref_val` = old/established/reference value (`float` ot `int`)
    Outputs:
      - `ferr` = fractional error of the new value from the old one
    '''
    if ref_val != 0:
        ferr = (test_val-ref_val)/ref_val
    elif test_val == 0: # both are zero
        ferr = 0
    else: # only one is zero, 100% error
        ferr = 1
        #ferr = 0 # changed to zero because I'd rather reject points where no comparison can be made
    return ferr

def fractional_difference(v1,v2):
    '''
    Description:
        Calculate fractional difference between two values (neither of more merit than the other)
    Inputs:
      - `v1` = first value (`float` ot `int`)
      - `v2` = second value (`float` ot `int`)
    Outputs:
      - `fdiff` = fractional difference between the two values
    '''
    if v1 != 0 and v2 != 0:
        fdiff = abs(v1-v2)/(0.5*(v1+v2))
    elif (v1+v2) != 0: # only one is nonzero, 100% difference
        fdiff = 1
    else: # both are zero
        fdiff = 0
    return fdiff

def absolute_difference(test_val,ref_val):
    '''
    Description:
        Calculate absolute difference of a reference value and an experimental test value
    Inputs:
      - `test_val` = new/tested/experimental value (`float` ot `int`)
      - `ref_val` = old/established/reference value (`float` ot `int`)
    Outputs:
      - `absdiff` = difference of reference and test values
    '''
    absdiff = ref_val-test_val
    return absdiff

def quotient(n,d):
    '''
    Description:
        Calculate the quotient of two value, returning 0 if either the numerator or demoninator equal zero
    Inputs:
      - `n` = numerator (`float` ot `int`)
      - `d` = denominator (`float` ot `int`)
    Outputs:
      - `q` = quotient of `n` and `d` (`q=n/d`)
    '''
    if n != 0 and d != 0:
        q = n/d
    else:
        q = 0
    return q


def Lorentz_gamma(v):
    '''
    Description:
        Calculate the Lorentz variable gamma provided a velocity in cm/ns
    Inputs:
      - `v` = velocity in cm/ns (`float` ot `int`)
    Outputs:
      - `gamma` = Lorentz variable gamma
    '''
    m_n = 939.5654133 # neutron mass in MeV/c^2
    c_vac = 29979245800 # cm/s
    refractive_index_air = 1.0003
    c = c_vac/refractive_index_air
    c_cm_per_ns = c/(10**9)
    beta = v/c_cm_per_ns
    gamma = np.sqrt(1/(1 - beta**2))
    return gamma

def Lorentz_B2_from_Tn(Tn):
    '''
    Description:
        Calculate the Lorentz variable beta^2 provided a neutron kinetic energy in MeV
    Inputs:
      - `Tn` = neutron kinetic energy in MeV (`float` ot `int`)
    Outputs:
      - `beta_squared` = Lorentz variable beta^2
    '''
    m_n = 939.5654133 # neutron mass in MeV/c^2
    c_vac = 29979245800 # cm/s
    refractive_index_air = 1.0003
    c = c_vac/refractive_index_air
    c_cm_per_ns = c/(10**9)
    gamma = 1 + (Tn/m_n)
    beta_squared = 1 - (1/(gamma**2))
    return beta_squared

def dist(a,b):
    '''
    Description:
        Calculate the distance between two N-dimensional Cartesian points a and b
    Dependencies:
        `import numpy as np`
    Inputs:
      - `a` = length N list containing coordinates of the first point, a  (ex. [ax,ay] or [ax,ay,az])
      - `b` = length N list containing coordinates of the second point, b (same format as a)
    Outputs:
      - `d` = Cartesian distance between points a and b

    '''
    if len(a) != len(b):
        print('a ({}) and b ({}) are not of the same dimension'.format(str(len(a)),str(len(b))))
        return 0
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    d = np.sqrt(d)
    return d

def curvature(x_data,y_data):
    '''
    Description:
        Calculates curvature for all interior points on a curve whose coordinates are provided

    Dependencies:
        `circumradius` (function within the "Hunter's tools" package)

    Inputs:
        - `x_data` = list of N x-coordinates
        - `y_data` = list of N y-coordinates
    Outputs:
        - `curvature` = list of N-2 curvature values
    '''
    curvature = []
    for i in range(1,len(x_data)-1):
        R = circumradius(x_data[i-1:i+2],y_data[i-1:i+2])
        if ( R == 0 ):
            print('Failed: points are either collinear or not distinct')
            return 0
        curvature.append(1/R)
    return curvature

def circumradius(xvals,yvals):
    '''
    Description:
        Calculates circumradius between three 2-dimensional points

    Inputs:
        - `xvals` = list of 3 x-coordinates
        - `yvals` = list of 3 y-coordinates
    Outputs:
        - `R` = circumradius of the three points
    '''
    x1, x2, x3, y1, y2, y3 = xvals[0], xvals[1], xvals[2], yvals[0], yvals[1], yvals[2]
    den = 2*((x2-x1)*(y3-y2)-(y2-y1)*(x3-x2))
    num = ( (((x2-x1)**2) + ((y2-y1)**2)) * (((x3-x2)**2)+((y3-y2)**2)) * (((x1-x3)**2)+((y1-y3)**2)) )**(0.5)
    if ( den == 0 ):
        print('Failed: points are either collinear or not distinct')
        return 0
    R = abs(num/den)
    return R

def circumcenter(xvals,yvals):
    '''
    Description:
        Calculates circumcenter between three 2-dimensional points

    Inputs:
        - `xvals` = list of 3 x-coordinates
        - `yvals` = list of 3 y-coordinates
    Outputs:
        - `x` = x-coordinate of circumcenter
        - `y` = y-coordinate of circumcenter
    '''
    x1, x2, x3, y1, y2, y3 = xvals[0], xvals[1], xvals[2], yvals[0], yvals[1], yvals[2]
    A = 0.5*((x2-x1)*(y3-y2)-(y2-y1)*(x3-x2))
    if ( A == 0 ):
        print('Failed: points are either collinear or not distinct')
        return 0
    xnum = ((y3 - y1)*(y2 - y1)*(y3 - y2)) - ((x2**2 - x1**2)*(y3 - y2)) + ((x3**2 - x2**2)*(y2 - y1))
    x = xnum/(-4*A)
    y =  (-1*(x2 - x1)/(y2 - y1))*(x-0.5*(x1 + x2)) + 0.5*(y1 + y2)
    return x, y

def circ_solid_angle(pp,a,b,r):
    '''
    Description:
        Calculates the solid angle subtended on (circular-faced) detector from point pp [xp,yp] to two points on a detector a [xa, ya] and b [xb, yb]
    Dependencies:
        `import numpy as np`
    Inputs:
      - `pp` = point of emission (radiation source), N-dimensional, list of floats/ints
      - `a` = point on edge of circular detector face, N-dimensional, list of floats/ints
      - `b` = point on edge of circular detector face opposite a, N-dimensional, list of floats/ints
      - `r` = radius of the detector (in the same units as the coordinates)
    Outputs:
      - `omega` = solid angle of source at pp as seen by a detector whose circular face has a diameter with ends at a and b

    '''
    d_pa = dist(pp,a)
    d_pb = dist(pp,b)
    theta = 0.5*np.arccos((d_pa**2 + d_pb**2 - (2*r)**2)/(2*d_pa*d_pb))
    omega = 2*np.pi*(1-np.cos(theta))
    return omega


def energy_resolution_of_peak(y,x,):
    '''
    Description:
        Provided a spectrum of counts (or equivalent) and it's bin centers or edges, and optionally the range of bins to evaluate, determine the
        energy resolution FWHM/H0 (also sigma/H0) of peak with average value H0.

    Inputs:
        - `y` = list/array of y values (length N)
        - `x` = list/array of x bin centers (length N) or bin edges (length N+1) corresponding to y
        - `peak_guess_location` = single value (float/int) denoting an initial guess of the peak's x location
        - `peak_search_range` = length-2 list of x values (not indices) between which the peak will be searched for

    Notes:
        At present, this function is only designed with "bell-shaped" distributions describable with three parameters related to
        amplitude/height, x position/centering, and width.

    Outputs:
        - `y_fit` = list/array of evaluated y values using the optimally found fit parameters
        - `dist_info` = dictionary object containing the distribution `short_name` and `full_name`; optimized fit parameters `a`, `mu`, and `sigma`;
                      calculated `FWHM`, `r2`/`r_squared` R^2, and `chi2`/`chi_squared` values; Python string of the function `fcn_py_str`; and LaTex string of the function `fcn_tex_str`
    '''

    return None


def eval_distribution(x,dist_name='gauss',a=1,mu=0,sigma=0.3,a2=None,mu2=None,sigma2=None):
    '''
    Description:
        Evaluates a provided array of x values (or single value) for a desired distribution provided its defining parameters.

    Dependencies:
        `from munch import *`

    Inputs:
        - `x` = list/array of x values or single x value
        - `dist_name` = string denoting the distribution used (D=`'Gaussian'`), options include:
                       `['gauss','normal','Logistic','sech']`, Read more here on the [Gaussian/normal](https://en.wikipedia.org/wiki/Normal_distribution),
                       [Logistic](https://en.wikipedia.org/wiki/Logistic_distribution), and
                       [Hyperbolic secant](https://en.wikipedia.org/wiki/Hyperbolic_secant_distribution) distributions.
        - `a` = distribution amplitude/height parameter
        - `mu` = distribution mean/center parameter
        - `sigma` = distribution width parameter

    Notes:
        At present, this function is only designed with "bell-shaped" distributions describable with three parameters related to
        amplitude/height, x position/centering, and width.

    Outputs:
        - `y_eval` = list/array of evaluated y values or single y value
        - `dist_info` = dictionary object containing the distribution `short_name` and `full_name`; assigned fit parameters `a`, `mu`, and `sigma`;
                      Python string of the function `fcn_py_str`; and LaTex string of the function `fcn_tex_str`
    '''
    dist_names_list = ['gauss','normal','Logistic','sech','cos','cosine','double-gauss']
    dist_name = dist_name.lower()
    if dist_name not in dist_names_list:
        print('Selected distribution name, ',dist_name,' is not in the list of allowed distribution names: ',dist_names_list,'\n exiting function... Please pick from this list and try again.')
        return None
    if type(x) is list: x = np.array(x)

    if dist_name=='gauss' or dist_name=='normal':
        y_eval = a*np.exp(-(x-mu)**2/(2*sigma**2))
        fcn_py_str = 'f = a*np.exp(-(x-mu)**2/(2*sigma**2))'
        fcn_tex_str = r'f(x) = A$\cdot$exp$(\frac{-(x-\mu)^2}{2\sigma^2})$'
        if dist_name=='gauss':
            dist_full_name = 'Gaussian'
        else:
            dist_full_name = 'Normal'
    elif dist_name=='double-gauss':
        y_eval = a*np.exp(-(x-mu)**2/(2*sigma**2)) + a2*np.exp(-(x-mu2)**2/(2*sigma2**2))
        fcn_py_str = 'f = a_0*np.exp(-(x-mu_0)**2/(2*sigma_0**2)) + a_1*np.exp(-(x-mu_1)**2/(2*sigma_1**2))'
        fcn_tex_str = r'f(x) = $A_0\cdot$exp$(\frac{-(x-\mu_0)^2}{2\sigma_0^2})$' + '\n' + r'$\quad + A_1\cdot$exp$(\frac{-(x-\mu_1)^2}{2\sigma_1^2})$'
        dist_full_name = 'Double Gaussian'
    elif dist_name=='logistic':
        y_eval = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))**2
        fcn_py_str = 'f = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))**2'
        fcn_tex_str = r'f(x) = $\frac{A}{4\sigma}$sech$^2(\frac{x-\mu}{2\sigma})$'
        dist_full_name = 'Logistic'
    elif dist_name=='sech':
        y_eval = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))
        fcn_py_str = 'f = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))'
        fcn_tex_str = r'f(x) = $\frac{A}{4\sigma}$sech$(\frac{x-\mu}{2\sigma})$'
        dist_full_name = 'Hyperbolic secant'
    else:
        y_eval = a*np.cos(sigma*(x-mu))
        fcn_py_str = 'f = a*np.cos(sigma*(x-mu))'
        fcn_tex_str = r'f(x) = $A*\cos(\sigma*(x-\mu))$'
        dist_full_name = 'Cosine'

    dist_info = {'short_name':dist_name,
                 'full_name':dist_full_name,
                 'a':a,
                 'mu':mu,
                 'sigma':sigma,
                 'fcn_py_str':fcn_py_str,
                 'fcn_tex_str':fcn_tex_str}

    if dist_name=='double-gauss':
        dist_info.update({
                 'a2':a2,
                 'mu2':mu2,
                 'sigma2':sigma2,
        })

    try:
        dist_info = Munch(dist_info)
    except:
        print("Munch failed.  Returned object is a conventional dictionary rather than a munch object.")

    return y_eval,  dist_info


def fit_distribution(x,y,dist_name='gauss',a0=None,mu0=None,sigma0=None,custom_fcn=None,a1=None,mu1=None,sigma1=None):
    '''
    Description:
        Determine best fit parameters and quality of fit provided test x and y values, the name of the ditribution to be fit, and initial guesses of its parameters.
        If initial guesses are omitted, they will try to be automatically assessed (your mileage may vary).

    Dependencies:
        `from munch import *`
        `from scipy.optimize import curve_fit`
        `from lmfit.models import GaussianModel`

    Inputs:
        - `x` = list/array of x values to be fit
        - `y` = list/array of y values to be fit
        - `dist_name` = string denoting the distribution used (D=`'Gaussian'`), options include:
                       `['gauss','normal','Logistic','sech']`, Read more here on the [Gaussian/normal](https://en.wikipedia.org/wiki/Normal_distribution),
                       [Logistic](https://en.wikipedia.org/wiki/Logistic_distribution), and
                       [Hyperbolic secant](https://en.wikipedia.org/wiki/Hyperbolic_secant_distribution) distributions.
        - `a0` = initial guess of the distribution amplitude/height parameter
        - `mu0` = initial guess of the distribution mean/center parameter
        - `sigma0` = initial guess of the distribution width parameter
        - `custom_fcn` = user-provided function which accepts arguments and can be called as `custom_fcn(x,a,mu,sigma)`, this will overwrite `dist_name`
                         if set to anything other than its default value D=`None`

    Notes:
        At present, this function is only designed with "bell-shaped" distributions describable with three parameters related to
        amplitude/height, x position/centering, and width.

    Outputs:
        - `y_fit` = list/array of evaluated y values using the optimally found fit parameters
        - `dist_info` = dictionary object containing the distribution `short_name` and `full_name`; optimized fit parameters `a`, `mu`, and `sigma`;
                      calculated `FWHM`, `r2`/`r_squared` R^2, and `chi2`/`chi_squared` values; Python string of the function `fcn_py_str`; and LaTex string of the function `fcn_tex_str`
    '''
    dist_names_list = ['gauss','normal','Logistic','sech','cos','cosine','double-gauss']
    dist_name = dist_name.lower()
    if dist_name not in dist_names_list:
        print('Selected distribution name, ',dist_name,' is not in the list of allowed distribution names: ',dist_names_list,'\n exiting function... Please pick from this list and try again.')
        return None
    if type(x) is list: x = np.array(x)
    if type(y) is list: y = np.array(y)

    use_lmfit_for_gauss = False # True

    def gaus(x,a,mu,sigma):
        f = a*np.exp(-(x-mu)**2/(2*sigma**2))
        return f
    def double_gauss(x,a0,mu0,sigma0,a1,mu1,sigma1):
        f = a0*np.exp(-(x-mu0)**2/(2*sigma0**2)) + a1*np.exp(-(x-mu1)**2/(2*sigma1**2))
        return f
    def logistic_dist(x,a,mu,sigma):
        f = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))**2
        return f
    def hyperbolic_secant_dist(x,a,mu,sigma):
        f = (a/(4*sigma))*(1/np.cosh((x-mu)/(2*sigma)))
        return f
    def cos_dist(x,a,mu,sigma):
        f = a*np.cos(sigma*(x-mu))
        return f

    if custom_fcn!=None:
        fit_fcn = custom_fcn
    else:
        if dist_name=='gauss' or dist_name=='normal':
            fit_fcn = gaus
        elif dist_name=='double-gauss':
            fit_fcn = double_gauss
        elif dist_name=='logistic':
            fit_fcn = logistic_dist
        elif dist_name=='cos' or dist_name=='cosine':
            fit_fcn = cos_dist
        else: #if dist_name=='sech'
            fit_fcn = hyperbolic_secant_dist


    n = len(x)
    ymax = max(y)
    ysum = sum(y)
    mean = sum(x*y/ymax)/(ysum/ymax)#n
    sigma = sum((y/ymax)*(x-mean)**2)/(ysum/ymax) #n

    if a0==None: a0 = ymax
    if mu0==None: mu0 = mean
    if sigma0==None: sigma0 = sigma
    #print('GUESS MEAN, SIGMA:',mu0,sigma0)

    if use_lmfit_for_gauss and (dist_name=='gauss' or dist_name=='normal'):
        model = GaussianModel()
        #params = model.make_params(center=mu0, amplitude=a0, sigma=sigma0)
        params = model.guess(y, x=x)
        result = model.fit(y, params, x=x)
        # see: https://lmfit.github.io/lmfit-py/fitting.html
        a = result.params['amplitude'].value
        mu = result.params['center'].value
        sigma = result.params['sigma'].value
        FWHM_fit = 2*np.sqrt(2*np.log(2))*sigma

        y_fit, dist_info = eval_distribution(x, dist_name=dist_name, a=a, mu=mu, sigma=sigma)
        r2 = r_squared(y,y_fit)

        chi2 = result.chisqr
        redchi2 = result.redchi
        num_fit_params=3
        ndf_chi2 = len(y) - num_fit_params
        p_chi2 = stats.chi2.sf(chi2,ndf_chi2)


    else:
        if dist_name=='double-gauss':
            if a1==None: a1=a0
            if mu1==None: mu1=mu0
            if sigma1==None: sigma1=sigma0
            popt,pcov = curve_fit(fit_fcn,x,y,p0=[a0,mu0,sigma0,a1,mu1,sigma1])
            a, mu, sigma = popt[0], popt[1], abs(popt[2])
            a2, mu2, sigma2 = popt[3], popt[4], abs(popt[5])
            FWHM_fit = 2*np.sqrt(2*np.log(2))*sigma

            y_fit, dist_info = eval_distribution(x, dist_name=dist_name, a=a, mu=mu, sigma=sigma, a2=a2, mu2=mu2, sigma2=sigma2)
            r2 = r_squared(y,y_fit)
        else:
            popt,pcov = curve_fit(fit_fcn,x,y,p0=[a0,mu0,sigma0])
            a, mu, sigma = popt[0], popt[1], abs(popt[2])
            FWHM_fit = 2*np.sqrt(2*np.log(2))*sigma

            y_fit, dist_info = eval_distribution(x, dist_name=dist_name, a=a, mu=mu, sigma=sigma)
            r2 = r_squared(y,y_fit)

        #chi2,red_chi2 = chi_squared(y,y_fit,num_fit_params=3)
        num_fit_params=3
        chi2,p_chi2,ndf_chi2 = chi_squared(y,y_fit,num_fit_params=num_fit_params)

    # How to write chi2 results: https://www.socscistatistics.com/tutorials/chisquare/default.aspx
    if p_chi2<0.001:
        chi_p_str = 'p<0.001'
    else:
        chi_p_str = 'p = {:4g}'
    chi2_tex_str = r'$\chi^2$'+'({:},N={:})={:.3g}, {}'.format(num_fit_params,n,chi2,chi_p_str)

    dist_info.update({
        'FWHM':FWHM_fit,
        'r2':r2,
        'r_squared':r2,
        'chi2':chi2,
        'chi_squared':chi2,
        'p_chi2':p_chi2,
        'ndf_chi2':ndf_chi2,
        'chi2_tex_str':chi2_tex_str
        #'red_chi2':red_chi2,
        #'red_chi_squared':red_chi2,
        })

    return y_fit, dist_info


def r_squared(y,y_fit):
    '''
    Description:
        Calculate R^2 (R-squared) value between two sets of data, an experimental "y" and fitted "y_fit"

    Inputs:
        - `y` = list/array of y values (experimental)
        - `y_fit` = list/array of fitted y values to be compared against y

    Outputs:
        - `r_squared` = calculated R-squared value
    '''
    # Calculate R^2
    # residual sum of squares
    ss_res = np.sum((y-y_fit)**2)
    # total sum of squares
    ss_tot = np.sum((y-np.mean(y))**2)
    # r-squared
    r2 = 1-(ss_res/ss_tot)
    return r2


def chi_squared(y,y_fit,num_fit_params=0):
    '''
    Description:
        Calculate chi^2 (chi-squared) value between two sets of data, an experimental "y" and fitted "y_fit"

    Dependencies:
        `from scipy.stats import chisquare`

    Inputs:
        - `y` = list/array of y values (experimental)
        - `y_fit` = list/array of fitted y values to be compared against y
        - `num_deg_freedom` = number of degrees of freedom (DoF) in fit function (number of optimized parameters) (D=`0`)

    Outputs:
        - `chi_squared` = calculated chi-squared value
        - `reduced_chi_squared` = calculated reduced chi-squared value (chi^2 / DoF)
    '''
    # This normalization shouldn't be necessary, but a past build of scipy broke the chisquare function from working without it
    y_fit = y_fit*sum(y)/sum(y_fit)
    chi2,p = chisquare(y,f_exp=y_fit,ddof=num_fit_params)
    ndf = len(y) - num_fit_params
    # Hand calc
    #O_k = y     # observed, from measurement
    #E_k = y_fit # expected, from some distribution e.g. Gaussian
    #chi2 = np.sum( ((O_k-E_k)**2)/E_k )
    #num_deg_freedom = len(O_k) - num_fit_params
    #red_chi2 = chi2/num_deg_freedom
    return chi2, p, ndf


def tally(data, bin_edges=[], min_bin_left_edge=None, max_bin_right_edge=None, nbins=None, bin_width=None, divide_by_bin_width=False, normalization=None, scaling_factor=1, place_overflow_at_ends=True, return_uncertainties=False, return_event_indices_histogram=False):
    '''
    Description:
        Tally number of incidences of values falling within a desired binning structure

    Inputs:
        - `data` = list of values to be tallied/histogrammed
        - `bin_edges` = list of N+1 bin edge values for a tally of N bins
        - `min_bin_left_edge` = left/minimum edge value of the first bin
        - `max_bin_right_edge` = right/maximum edge value of the last bin
        - `nbins` = number of equally-sized bins to be created from `min_bin_left_edge` to `max_bin_right_edge`
        - `bin_width` = constant width of bins to be created from `min_bin_left_edge` to `max_bin_right_edge`
        - `divide_by_bin_width` = Boolean denoting whether final bin values are divided by their bin widths (D=`False`)
        - `normalization` = determine how the resulting histogram is normalized (D=`None`), options are:
                       `[None, 'unity-sum', 'unity-max-val']`.  If `None`, no additional normalization is done.
                       If `unity-sum`, the data is normalized such that its sum will be 1.  If `unity-max-val`, the
                       data is normalized such that the maximum value is 1.  The operation occurs after any bin
                       width normalization from `divide_by_bin_width` but before any scaling from `scaling_factor`.
        - `scaling_factor` = value which all final bins are multiplied/scaled by (D=`1`)
        - `place_overflow_at_ends` = handling of values outside of binning range (D=`True`); if `True` extreme
                       values are tallied in the first/last bin, if `False` extreme values are discarded
        - `return_uncertainties` = Boolean denoting if should return an extra N-length list whose elements
                       are the statistical uncertainties (square root w/ normalizations) of the tally bins (D=`False`)
        - `return_event_indices_histogram` = Boolean denoting if should return an extra N-length list whose elements
                       are each a list of the event indices corresponding to each bin (D=`False`)

    Notes:
        Regarding the binning structure, this function only needs to be provided `bin_edges` directly (takes priority)
        or the information needed to calculate `bin_edges`, that is: `min_bin_left_edge` and `max_bin_right_edge` and
        either `nbins` or `bin_width`.  (Priority is given to `nbins` if both are provided.)

    Outputs:
        - `tallied_hist` = N-length list of tallied data
        - `bin_edges` = list of N+1 bin edge values for a tally of N bins
        - `tallied_hist_err` = (optional) N-length list of statistical uncertainties of tallied data
        - `tallied_event_indicies` = (optional) N-length list of, for each bin, a list of the event indices populating it
    '''

    normalization_valid_entries = [None, 'unity-sum', 'unity-max-val']
    if normalization not in normalization_valid_entries:
        print("Entered normalization option of ",normalization," is not a valid option; please select from the following: [None, 'unity-sum', 'unity-max-val']".format())

    if len(bin_edges)!=0:
        bin_edges = np.array(bin_edges)
    else:
        if nbins != None:
            bin_edges = np.linspace(min_bin_left_edge,max_bin_right_edge,num=nbins+1)
        else:
            bin_edges = np.arange(min_bin_left_edge,max_bin_right_edge+bin_width,step=bin_width)

    nbins = len(bin_edges) - 1

    if return_event_indices_histogram:
        tallied_event_indicies = []
        tallied_hist = np.zeros(nbins)
        for i in range(nbins):
            tallied_event_indicies.append([])
        # events must be histogrammed manually
        for i, val in enumerate(data):
            if val < bin_edges[0]:
                if place_overflow_at_ends:
                    tallied_hist[0] += 1
                    tallied_event_indicies[0].append(i)
                continue
            if val > bin_edges[-1]:
                if place_overflow_at_ends:
                    tallied_hist[-1] += 1
                    tallied_event_indicies[-1].append(i)
                continue
            for j, be in enumerate(bin_edges):
                if be > val: # found right edge of bin containing val
                    tallied_hist[j-1] += 1
                    tallied_event_indicies[j-1].append(i)
                    break



    else:
        tallied_hist, bins = np.histogram(data,bins=bin_edges)

    if return_uncertainties:
        tallied_hist_err = np.sqrt(tallied_hist)
        if divide_by_bin_width: tallied_hist_err = tallied_hist_err/(bin_edges[1:]-bin_edges[:-1])
        if normalization=='unity-sum': tallied_hist_err = tallied_hist_err/np.sum(tallied_hist)
        if normalization=='unity-max-val': tallied_hist_err = tallied_hist_err/np.max(tallied_hist)
        if scaling_factor != 1: tallied_hist_err = tallied_hist_err*scaling_factor

    if divide_by_bin_width: tallied_hist = tallied_hist/(bin_edges[1:]-bin_edges[:-1])
    if normalization=='unity-sum': tallied_hist = tallied_hist/np.sum(tallied_hist)
    if normalization=='unity-max-val': tallied_hist = tallied_hist/np.max(tallied_hist)
    if scaling_factor != 1: tallied_hist = tallied_hist*scaling_factor

    if return_event_indices_histogram:
        if return_uncertainties:
            return tallied_hist,bin_edges,tallied_hist_err,tallied_event_indicies
        else:
            return tallied_hist,bin_edges,tallied_event_indicies
    else:
        if return_uncertainties:
            return tallied_hist,bin_edges,tallied_hist_err
        else:
            return tallied_hist,bin_edges





def rebinner(output_xbins,input_xbins,input_ybins):
    """
    Description:
        The purpose of this function is to rebin a set of y values corresponding to a set of x bins to a new set of x bins.
        The function seeks to be as generalized as possible, meaning bin sizes do not need to be consistent.

    Dependencies:
        `import numpy as np`

    Inputs:
      - `output_xbins` = output array containing bounds of x bins of length N; first entry is leftmost bin boundary
      - `input_xbins`  = input array containing bounds of x bins of length M; first entry is leftmost bin boundary
      - `input_ybins`  = input array containing y values of length M-1

    Outputs:
      - `output_ybins` = output array containing y values of length N-1
    """

    N = len(output_xbins)
    M = len(input_xbins)
    output_ybins = np.zeros(N-1)

    for i in range(0,N-1):
        # For each output bin
        lxo = output_xbins[i]   # lower x value of output bin
        uxo = output_xbins[i+1] # upper x value of output bin
        dxo = uxo - lxo         # width of current x output bin

        # Scan input x bins to see if any fit in this output bin
        for j in range(0,M-1):
            lxi = input_xbins[j]    # lower x value of input bin
            uxi = input_xbins[j+1]  # upper x value of input bin
            dxi = uxi - lxi         # width of current x input bin

            if uxi<lxo or lxi>uxo:
                # no bins are aligned
                continue
            elif lxi >= lxo and lxi < uxo:
                # start of an input bin occurs in this output bin
                if lxi >= lxo and uxi <= uxo:
                    # input bin completely encompassed by output bin
                    output_ybins[i] = output_ybins[i] + input_ybins[j]
                else:
                    # input bin spans over at least one output bin
                    # count fraction in current output x bin
                    f_in_dxo = (uxo-lxi)/dxi
                    output_ybins[i] = output_ybins[i] + f_in_dxo*input_ybins[j]
            elif lxi < lxo and uxi > uxo:
                # output bin is completely encompassed by input bin
                f_in_dxo = (uxo-lxo)/dxi
                output_ybins[i] = output_ybins[i] + f_in_dxo*input_ybins[j]
            elif lxi < lxo and uxi > lxo and uxi <= uxo:
                # tail of input bin is located in this output bin
                f_in_dxo = (uxi-lxo)/dxi
                output_ybins[i] = output_ybins[i] + f_in_dxo*input_ybins[j]

    return output_ybins


def calc_GCR_intensity(Z,W,E):
    '''
    Description:
        Calculate GCR flux for a given ion at a given energy using the Matthia model
        https://www.sciencedirect.com/science/article/pii/S0273117712005947?via%3Dihub

    Dependencies:
        `import numpy as np`

    Inputs:
       - `Z` = GCR ion Z
       - `W` = solar modulation parameter
       - `E` = GCR ion energy (in MeV/n)

    Outputs:
       - `IOSI` = ion flux in (s\*sr\*cm^2\*MeV/n)^-1
    '''

    if Z<1 or Z>28 or W<0 or W>200:
        return -99
    if E<10:
        return 0

    AI = [1.0 ,4.0,  6.9,  9.0, 10.8, 12.0, 14.0, 16.0, 19.0, 20.2, 23.0, 24.3, 27.0, 28.1, 31.0, 32.1, 35.4, 39.9, 39.1, 40.1, 44.9, 47.9, 50.9, 52.0, 54.9, 55.8, 58.9, 58.7]
    CI = [1.85e4, 3.69e3, 19.5, 17.7, 49.2, 103.0, 36.7, 87.4, 3.19, 16.4, 4.4300, 19.300, 4.17, 13.4, 1.15, 3.060, 1.30, 2.33, 1.87, 2.17, 0.74, 2.63, 1.23, 2.12, 1.14, 9.32, 0.10, 0.48]
    gammaI = [2.74, 2.77, 2.82, 3.05, 2.96, 2.76, 2.89, 2.70, 2.82, 2.76, 2.84, 2.70, 2.77, 2.66, 2.89, 2.71, 3.00, 2.93, 3.05, 2.77, 2.97, 2.99, 2.94, 2.89, 2.74, 2.63, 2.63, 2.63]
    alphaI = [2.85, 3.12, 3.41, 4.30, 3.93, 3.18, 3.77, 3.11, 4.05, 3.11, 3.14, 3.65, 3.46, 3.00, 4.04, 3.30, 4.40, 4.33, 4.49, 2.93, 3.78, 3.79, 3.50, 3.28, 3.29, 3.01, 4.25, 3.52]

    P = [0.02,4.7]

    i = int(Z-1)

    E0S = 938.0 # rest mass in MeV/n
    if Z>1: E0S = 939.0 # rest mass in MeV/n
    E0SS = E0S/1000 # rest mass in GeV/n
    ES = E/1000 # energy in GeV/n
    RigS = (AI[i]/Z*np.sqrt(ES*(ES+2*E0SS))) #rigidity in GV
    betaS2 = (np.sqrt(ES*(ES+2.*E0SS))/(ES+E0SS)) #convert kinetic energy per nucleon to beta=v/c
    R0S = (0.37+0.0003*(W**1.45))
    DELTAI = (P[1]+P[0]*W)
    PHII = CI[i]*(betaS2**alphaI[i])/(RigS**gammaI[i])
    PHII = PHII*((RigS/(RigS+R0S))**DELTAI)
    IOSI = 0.0001*PHII*AI[i]/Z*0.001/betaS2

    return IOSI

def assemble_GCR_flux(W,Z_list,nEbins=1000):
    '''
    Description:
        Composes a NumPy array containing GCR flux from 10 MeV/n to 1 TeV/n for each GCR ion specified

    Dependencies:
       - `import numpy as np`
       - `calc_GCR_intensity` (function within the "Hunter's tools" package)

    Inputs:
       - `W` = solar modulation parameter
       - `Z_list` = list of element atomic numbers to form GCR spectra for
       - `nEbins` = number of evenly-logspaced energy bins (D=1000)

    Outputs:
       - `GCR_flux(len(Z_list),4,nEbins)` = array containing flux values in (s\*sr\*cm^2\*MeV/n)^-1 ; [emin/emid/emax/flux]
    '''
    GCR_flux = np.zeros((len(Z_list),4,nEbins))

    Emin = 10 # MeV
    Emax = 1e6 # MeV

    logEmin = np.log10(Emin)
    logEmax = np.log10(Emax)
    logdE = (logEmax-logEmin)/nEbins
    logE = logEmin

    for k in range(nEbins):
        GCR_flux[:,0,k] = 10**(logE)
        GCR_flux[:,1,k] = 10**(logE+0.5*logdE)
        GCR_flux[:,2,k] = 10**(logE+logdE)
        logE += logdE

    for j in range(len(Z_list)):
        Z = Z_list[j]
        for k in range(nEbins):
            GCR_flux[j,3,k] = calc_GCR_intensity(Z,W,GCR_flux[j,1,k])

    return GCR_flux



def ICRP116_effective_dose_coeff(E=1.0,particle='photon',geometry='AP',interp_scale='log',interp_type='cubic',extrapolation_on=False):
    '''
    Description:
        For a given particle at a given energy in a given geometry, returns its
        effective dose conversion coefficient from ICRP 116

    Dependencies:
        - `import numpy as np`
        - `from scipy.interpolate import CubicSpline, lagrange, interp1d`
        - `find` (function within the "Hunter's tools" package)

    Inputs:
       - `E` = energy of the particle in MeV (D=`1`)
       - `particle` = select particle (D=`'photon'`, options include: `['photon', 'electron', 'positron' ,'neutron' ,'proton', 'negmuon', 'posmuon', 'negpion', 'pospion', 'He3ion']`)
       - `geometry` = geometric arrangement (D=`'AP'`, options include: `['AP', 'PA', 'LLAT', 'RLAT', 'ROT', 'ISO', 'H*(10)']` (`'LLAT'`,`'RLAT'`,`'ROT'` only available for photon, proton, and neutron))
              - Meanings:
               AP, antero-posterior; PA, postero-anterior; LLAT, left lateral; RLAT, right lateral; ROT, rotational; ISO, isotropic.
              - Note: `'H*(10)'` ambient dose equivalent is available for photons only
       - `interp_scale` = interpolation scale (D=`'log'` to interpolate on a log scale, options include: `['log','lin']`, ICRP 74/116 suggest log-log cubic interpolation)
       - `interp_type`  = interpolation method (D=`'cubic'` to interpolate with a cubic spline, options include: `['cubic','linear']`, ICRP 74/116 suggest log-log cubic interpolation)
                                              technically, any options available for scipy.interpolate.interp1d() can be used: `['linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'previous']`
       - `extrapolation_on` = boolean designating whether values outside of the tabulated energies will be extrapolated (D=`False`)

             |                      |                                                                       |
             | -------------------- | --------------------------------------------------------------------- |
             | if False & E < E_min | f(E) = 0                                                              |
             | if False & E > E_max | f(E) = f(E_max)                                                       |
             | if True  & E < E_min | f(E) is linearly interpolated between (0,0) and (E_min,f(E_min))      |
             | if True  & E > E_max | f(E) is extrapolated using the specified interpolation scale and type |
    Outputs:
       - `f` = effective dose conversion coefficient in pSv*cm^2
    '''

    pars_list = ['photon','electron','positron','neutron','proton','negmuon','posmuon','negpion','pospion','He3ion']
    geo_list_all = ['AP','PA','LLAT','RLAT','ROT','ISO','H*(10)']
    geo_list_short = ['AP','PA','ISO']

    if particle not in pars_list or geometry not in geo_list_all:
        pstr = 'Please select a valid particle and geometry.\n'
        pstr += "Particle selected = {}, options include: ['photon','electron','positron','neutron','proton','negmuon','posmuon','negpion','pospion','He3ion']".format(particle)
        pstr += "Geometry selected = {}, options include: ['AP','PA','LLAT','RLAT','ROT','ISO'] ('LLAT','RLAT','ROT' only available for photon, proton, and neutron)"
        print(pstr)
        return None

    if (particle not in ['photon','neutron','proton'] and geometry in ['LLAT','RLAT','ROT']) or (particle!='photon' and geometry=='H*(10)'):
        if (particle!='photon' and geometry=='H*(10)'):
            pstr = "geometry = {} is only available for photons\n".format(geometry)
        else:
            pstr = "geometry = {} is only available for photon, neutron, and proton\n".format(geometry)
            pstr += "For selected particle = {}, please choose geometry from ['AP','PA','ISO']".format(particle)
        print(pstr)
        return None

    E_photon = [0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.511, 0.6, 0.662, 0.8, 1, 1.117, 1.33, 1.5, 2, 3, 4, 5, 6, 6.129, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_photon = [
    [0.0685, 0.156, 0.225, 0.313, 0.351, 0.37, 0.39, 0.413, 0.444, 0.519, 0.748, 1, 1.51, 2, 2.47, 2.52, 2.91, 3.17, 3.73, 4.49, 4.9, 5.59, 6.12, 7.48, 9.75, 11.7, 13.4, 15, 15.1, 17.8, 20.5, 26.1, 30.8, 37.9, 43.1, 47.1, 50.1, 54.5, 57.8, 63.3, 67.3, 72.3, 75.5, 77.5, 78.9, 80.5, 81.7, 83.8, 85.2, 86.9, 88.1, 88.9, 89.5, 90.2, 90.7],
    [0.0184, 0.0155, 0.026, 0.094, 0.161, 0.208, 0.242, 0.271, 0.301, 0.361, 0.541, 0.741, 1.16, 1.57, 1.98, 2.03, 2.38, 2.62, 3.13, 3.83, 4.22, 4.89, 5.39, 6.75, 9.12, 11.2, 13.1, 15, 15.2, 18.6, 22, 30.3, 38.2, 51.4, 62, 70.4, 76.9, 86.6, 93.2, 104, 111, 119, 124, 128, 131, 135, 138, 142, 145, 148, 150, 152, 153, 155, 155],
    [0.0189, 0.0416, 0.0655, 0.11, 0.14, 0.16, 0.177, 0.194, 0.214, 0.259, 0.395, 0.552, 0.888, 1.24, 1.58, 1.62, 1.93, 2.14, 2.59, 3.23, 3.58, 4.2, 4.68, 5.96, 8.21, 10.2, 12, 13.7, 13.9, 17, 20.1, 27.4, 34.4, 47.4, 59.2, 69.5, 78.3, 92.4, 103, 121, 133, 148, 158, 165, 170, 178, 183, 193, 198, 206, 212, 216, 219, 224, 228],
    [0.0182, 0.039, 0.0573, 0.0891, 0.114, 0.133, 0.15, 0.167, 0.185, 0.225, 0.348, 0.492, 0.802, 1.13, 1.45, 1.49, 1.78, 1.98, 2.41, 3.03, 3.37, 3.98, 4.45, 5.7, 7.9, 9.86, 11.7, 13.4, 13.6, 16.6, 19.7, 27.1, 34.4, 48.1, 60.9, 72.2, 82, 97.9, 110, 130, 143, 161, 172, 180, 186, 195, 201, 212, 220, 229, 235, 240, 244, 251, 255],
    [0.0337, 0.0664, 0.0986, 0.158, 0.199, 0.226, 0.248, 0.273, 0.297, 0.355, 0.528, 0.721, 1.12, 1.52, 1.92, 1.96, 2.3, 2.54, 3.04, 3.72, 4.1, 4.75, 5.24, 6.55, 8.84, 10.8, 12.7, 14.4, 14.6, 17.6, 20.6, 27.7, 34.4, 46.1, 56, 64.4, 71.2, 82, 89.7, 102, 111, 121, 128, 133, 136, 142, 145, 152, 156, 161, 165, 168, 170, 172, 175],
    [0.0288, 0.056, 0.0812, 0.127, 0.158, 0.18, 0.199, 0.218, 0.239, 0.287, 0.429, 0.589, 0.932, 1.28, 1.63, 1.67, 1.97, 2.17, 2.62, 3.25, 3.6, 4.2, 4.66, 5.9, 8.08, 10, 11.8, 13.5, 13.7, 16.6, 19.6, 26.8, 33.8, 46.1, 56.9, 66.2, 74.1, 87.2, 97.5, 116, 130, 147, 159, 168, 174, 185, 193, 208, 218, 232, 243, 251, 258, 268, 276],
    [0.061, 0.83, 1.05, 0.81, 0.64, 0.55, 0.51, 0.52, 0.53, 0.61, 0.89, 1.20, 1.80, 2.38, 2.93, 2.99, 3.44, 3.73, 4.38, 5.20, 5.60, 6.32, 6.90, 8.60, 11.10, 13.40, 15.50, 17.60, 17.86, 21.60, 25.60, 8.53, 8.29, 8.23, 8.26, 8.64, 8.71, 8.86, 9.00, 9.60, 10.20, 10.73, 11.27, 11.80, 11.78, 11.74, 11.70, 11.60, 11.50, 12.10, 12.70, 13.30, 13.08, 12.64, 12.20]
    ]

    E_electron = [0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_electron = [
    [0.0269, 0.0404, 0.0539, 0.081, 0.108, 0.135, 0.163, 0.218, 0.275, 0.418, 0.569, 0.889, 1.24, 1.63, 2.05, 4.04, 7.1, 15, 22.4, 36.1, 48.2, 59.3, 70.6, 97.9, 125, 188, 236, 302, 329, 337, 341, 346, 349, 355, 359, 365, 369, 372, 375, 379, 382, 387, 391, 397, 401, 405, 407, 411, 414],
    [0.0268, 0.0402, 0.0535, 0.0801, 0.107, 0.133, 0.16, 0.213, 0.267, 0.399, 0.53, 0.787, 1.04, 1.28, 1.5, 1.68, 1.68, 1.62, 1.62, 1.95, 2.62, 3.63, 5.04, 9.46, 18.3, 53.1, 104, 220, 297, 331, 344, 358, 366, 379, 388, 399, 408, 414, 419, 428, 434, 446, 455, 468, 477, 484, 490, 499, 507],
    [0.0188, 0.0283, 0.0377, 0.0567, 0.0758, 0.0948, 0.114, 0.152, 0.191, 0.291, 0.393, 0.606, 0.832, 1.08, 1.35, 1.97, 2.76, 4.96, 7.24, 11.9, 16.4, 21, 25.5, 35.5, 46.7, 76.9, 106, 164, 212, 249, 275, 309, 331, 363, 383, 410, 430, 445, 457, 478, 495, 525, 549, 583, 608, 628, 646, 675, 699]
    ]

    E_positron = [0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_positron = [
    [3.28, 3.29, 3.3, 3.33, 3.36, 3.39, 3.42, 3.47, 3.53, 3.67, 3.84, 4.16, 4.52, 4.9, 5.36, 7.41, 10.5, 18.3, 25.7, 39.1, 51, 61.7, 72.9, 99, 126, 184, 229, 294, 320, 327, 333, 339, 342, 349, 354, 362, 366, 369, 372, 376, 379, 385, 389, 395, 399, 402, 404, 408, 411],
    [1.62, 1.64, 1.65, 1.68, 1.71, 1.73, 1.76, 1.82, 1.87, 2.01, 2.14, 2.4, 2.65, 2.9, 3.12, 3.32, 3.37, 3.44, 3.59, 4.19, 5.11, 6.31, 8.03, 14, 23.6, 59, 111, 221, 291, 321, 334, 349, 357, 371, 381, 393, 402, 409, 415, 424, 430, 443, 451, 465, 473, 480, 486, 495, 503],
    [1.39, 1.4, 1.41, 1.43, 1.45, 1.47, 1.49, 1.53, 1.57, 1.67, 1.77, 1.98, 2.21, 2.45, 2.72, 3.38, 4.2, 6.42, 8.7, 13.3, 18, 22.4, 26.9, 36.7, 47.6, 75.5, 104, 162, 209, 243, 268, 302, 323, 356, 377, 405, 425, 440, 453, 474, 491, 522, 545, 580, 605, 627, 645, 674, 699]
    ]

    E_neutron = [1.00E-09, 1.00E-08, 2.50E-08, 1.00E-07, 2.00E-07, 5.00E-07, 1.00E-06, 2.00E-06, 5.00E-06, 1.00E-05, 2.00E-05, 5.00E-05, 1.00E-04, 2.00E-04, 5.00E-04, 0.001, 0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 0.9, 1, 1.2, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 30, 50, 75, 100, 130, 150, 180, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 5000, 10000]
    f_neutron = [
    [3.09, 3.55, 4, 5.2, 5.87, 6.59, 7.03, 7.39, 7.71, 7.82, 7.84, 7.82, 7.79, 7.73, 7.54, 7.54, 7.61, 7.97, 9.11, 12.2, 15.7, 23, 30.6, 41.9, 60.6, 78.8, 114, 177, 232, 279, 301, 330, 365, 407, 458, 483, 494, 498, 499, 499, 500, 500, 499, 495, 493, 490, 484, 477, 474, 453, 433, 420, 402, 382, 373, 363, 359, 363, 389, 422, 457, 486, 508, 524, 537, 612, 716, 933],
    [1.85, 2.11, 2.44, 3.25, 3.72, 4.33, 4.73, 5.02, 5.3, 5.44, 5.51, 5.55, 5.57, 5.59, 5.6, 5.6, 5.62, 5.95, 6.81, 8.93, 11.2, 15.7, 20, 25.9, 34.9, 43.1, 58.1, 85.9, 112, 136, 148, 167, 195, 235, 292, 330, 354, 371, 383, 392, 398, 404, 412, 417, 419, 420, 422, 423, 423, 422, 428, 439, 444, 446, 446, 447, 448, 464, 496, 533, 569, 599, 623, 640, 654, 740, 924, 1.17E+03],
    [1.04, 1.15, 1.32, 1.7, 1.94, 2.21, 2.4, 2.52, 2.64, 2.65, 2.68, 2.66, 2.65, 2.66, 2.62, 2.61, 2.6, 2.74, 3.13, 4.21, 5.4, 7.91, 10.5, 14.4, 20.8, 27.2, 39.7, 63.7, 85.5, 105, 115, 130, 150, 179, 221, 249, 269, 284, 295, 303, 310, 316, 325, 333, 336, 338, 343, 347, 348, 360, 380, 399, 409, 416, 420, 425, 427, 441, 472, 510, 547, 579, 603, 621, 635, 730, 963, 1.23E+03],
    [0.893, 0.978, 1.12, 1.42, 1.63, 1.86, 2.02, 2.11, 2.21, 2.24, 2.26, 2.24, 2.23, 2.24, 2.21, 2.21, 2.2, 2.33, 2.67, 3.6, 4.62, 6.78, 8.95, 12.3, 17.9, 23.4, 34.2, 54.4, 72.6, 89.3, 97.4, 110, 128, 153, 192, 220, 240, 255, 267, 276, 284, 290, 301, 310, 313, 317, 323, 328, 330, 345, 370, 392, 404, 413, 418, 425, 429, 451, 483, 523, 563, 597, 620, 638, 651, 747, 979, 1.26E+03],
    [1.7, 2.03, 2.31, 2.98, 3.36, 3.86, 4.17, 4.4, 4.59, 4.68, 4.72, 4.73, 4.72, 4.67, 4.6, 4.58, 4.61, 4.86, 5.57, 7.41, 9.46, 13.7, 18, 24.3, 34.7, 44.7, 63.8, 99.1, 131, 160, 174, 193, 219, 254, 301, 331, 351, 365, 374, 381, 386, 390, 395, 398, 398, 399, 399, 398, 398, 395, 395, 402, 406, 411, 414, 418, 422, 443, 472, 503, 532, 558, 580, 598, 614, 718, 906, 1.14E+03],
    [1.29, 1.56, 1.76, 2.26, 2.54, 2.92, 3.15, 3.32, 3.47, 3.52, 3.54, 3.55, 3.54, 3.52, 3.47, 3.46, 3.48, 3.66, 4.19, 5.61, 7.18, 10.4, 13.7, 18.6, 26.6, 34.4, 49.4, 77.1, 102, 126, 137, 153, 174, 203, 244, 271, 290, 303, 313, 321, 327, 332, 339, 344, 346, 347, 350, 352, 353, 358, 371, 387, 397, 407, 412, 421, 426, 455, 488, 521, 553, 580, 604, 624, 642, 767, 1.01E+03, 1.32E+03]
    ]

    E_proton = [1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_proton = [
    [5.46, 8.2, 10.9, 16.4, 21.9, 27.3, 32.8, 43.7, 54.9, 189, 428, 750, 1.02E+03, 1.18E+03, 1.48E+03, 2.16E+03, 2.51E+03, 2.38E+03, 1.77E+03, 1.38E+03, 1.23E+03, 1.15E+03, 1.16E+03, 1.11E+03, 1.09E+03, 1.15E+03, 1.12E+03, 1.23E+03, 1.27E+03, 1.23E+03, 1.37E+03, 1.45E+03, 1.41E+03],
    [5.47, 8.21, 10.9, 16.4, 21.9, 27.3, 32.8, 43.7, 54.6, 56.1, 43.6, 36.1, 45.5, 71.5, 156, 560, 1.19E+03, 2.82E+03, 1.93E+03, 1.45E+03, 1.30E+03, 1.24E+03, 1.23E+03, 1.23E+03, 1.23E+03, 1.25E+03, 1.28E+03, 1.34E+03, 1.40E+03, 1.45E+03, 1.53E+03, 1.65E+03, 1.74E+03],
    [2.81, 4.21, 5.61, 8.43, 11.2, 14, 16.8, 22.4, 28.1, 50.7, 82.8, 180, 290, 379, 500, 799, 994, 1.64E+03, 2.15E+03, 1.44E+03, 1.27E+03, 1.21E+03, 1.20E+03, 1.19E+03, 1.18E+03, 1.21E+03, 1.25E+03, 1.32E+03, 1.31E+03, 1.39E+03, 1.44E+03, 1.56E+03, 1.63E+03],
    [2.81, 4.2, 5.62, 8.41, 11.2, 14, 16.8, 22.4, 28.1, 48.9, 78.8, 172, 278, 372, 447, 602, 818, 1.46E+03, 2.18E+03, 1.45E+03, 1.28E+03, 1.21E+03, 1.20E+03, 1.20E+03, 1.20E+03, 1.23E+03, 1.25E+03, 1.32E+03, 1.33E+03, 1.41E+03, 1.45E+03, 1.59E+03, 1.67E+03],
    [4.5, 6.75, 8.98, 13.4, 17.8, 22.1, 26.3, 34.5, 50.1, 93.7, 165, 296, 422, 532, 687, 1.09E+03, 1.44E+03, 2.16E+03, 1.96E+03, 1.44E+03, 1.28E+03, 1.22E+03, 1.22E+03, 1.20E+03, 1.19E+03, 1.23E+03, 1.23E+03, 1.30E+03, 1.29E+03, 1.35E+03, 1.41E+03, 1.49E+03, 1.56E+03],
    [3.52, 5.28, 7.02, 10.5, 13.9, 17.3, 20.5, 26.8, 45.8, 80.1, 136, 249, 358, 451, 551, 837, 1.13E+03, 1.79E+03, 1.84E+03, 1.42E+03, 1.25E+03, 1.18E+03, 1.17E+03, 1.17E+03, 1.15E+03, 1.21E+03, 1.22E+03, 1.31E+03, 1.40E+03, 1.43E+03, 1.57E+03, 1.71E+03, 1.78E+03]
    ]

    E_negmuon = [1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_negmuon = [
    [180, 180, 184, 188, 193, 205, 242, 293, 332, 414, 465, 657, 735, 755, 628, 431, 382, 340, 326, 319, 320, 321, 325, 327, 333, 331, 333, 336, 337, 337, 337, 337, 338],
    [75.2, 76.8, 78.3, 81.4, 84.8, 87.7, 86.7, 86.8, 88.6, 100, 122, 251, 457, 703, 775, 485, 402, 345, 329, 321, 321, 324, 326, 332, 337, 338, 341, 344, 345, 346, 346, 347, 347],
    [78.7, 79.5, 80.9, 83.7, 87.1, 91.5, 98.1, 113, 127, 161, 191, 275, 363, 446, 496, 498, 432, 354, 332, 321, 321, 323, 326, 331, 337, 338, 341, 344, 346, 347, 347, 348, 348]
    ]

    E_posmuon = [1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    f_posmuon = [
    [194, 196, 198, 202, 207, 216, 251, 300, 340, 425, 481, 674, 751, 768, 635, 431, 381, 339, 326, 318, 319, 320, 322, 325, 327, 331, 333, 336, 337, 337, 337, 337, 339],
    [82.6, 84.1, 85.7, 88.9, 92.1, 94.3, 92.5, 92.8, 94.8, 108, 133, 265, 473, 721, 787, 483, 399, 345, 328, 320, 321, 323, 325, 330, 333, 339, 341, 344, 345, 346, 346, 347, 347],
    [85.2, 86.2, 87.5, 90.3, 93.6, 97.7, 103, 117, 132, 167, 199, 284, 373, 456, 506, 502, 432, 354, 332, 320, 320, 322, 324, 329, 333, 338, 341, 344, 346, 347, 347, 348, 348]
    ]

    E_negpion = [1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 80000, 100000, 150000, 200000]
    f_negpion = [
    [406, 422, 433, 458, 491, 528, 673, 965, 1.09E+03, 1.25E+03, 1.28E+03, 1.77E+03, 1.92E+03, 1.93E+03, 1.68E+03, 1.14E+03, 995, 927, 902, 848, 844, 869, 901, 947, 977, 1.03E+03, 1.05E+03, 1.03E+03, 1.03E+03, 1.06E+03, 1.09E+03, 1.14E+03, 1.17E+03, 1.21E+03, 1.24E+03, 1.30E+03, 1.35E+03, 1.39E+03, 1.42E+03, 1.48E+03, 1.54E+03, 1.67E+03, 1.78E+03],
    [194, 201, 210, 225, 233, 237, 208, 181, 178, 197, 244, 547, 1.02E+03, 1.70E+03, 1.99E+03, 1.31E+03, 991, 889, 871, 843, 850, 880, 917, 976, 1.02E+03, 1.08E+03, 1.12E+03, 1.11E+03, 1.13E+03, 1.18E+03, 1.22E+03, 1.29E+03, 1.34E+03, 1.41E+03, 1.47E+03, 1.56E+03, 1.63E+03, 1.70E+03, 1.75E+03, 1.86E+03, 1.95E+03, 2.15E+03, 2.33E+03],
    [176, 189, 198, 215, 232, 251, 271, 317, 361, 439, 508, 676, 868, 1.02E+03, 1.15E+03, 1.15E+03, 1.03E+03, 857, 815, 794, 807, 838, 875, 935, 979, 1.05E+03, 1.09E+03, 1.11E+03, 1.15E+03, 1.20E+03, 1.26E+03, 1.36E+03, 1.43E+03, 1.55E+03, 1.64E+03, 1.79E+03, 1.91E+03, 2.02E+03, 2.11E+03, 2.29E+03, 2.46E+03, 2.80E+03, 3.04E+03]
    ]

    E_pospion = [1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 80000, 100000, 150000, 200000]
    f_pospion = [
    [314, 324, 340, 379, 429, 489, 540, 717, 819, 1000, 1.10E+03, 1.52E+03, 1.75E+03, 1.83E+03, 1.66E+03, 1.22E+03, 1.13E+03, 1.22E+03, 1.25E+03, 1.07E+03, 969, 943, 952, 999, 1.04E+03, 1.10E+03, 1.10E+03, 1.06E+03, 1.06E+03, 1.07E+03, 1.10E+03, 1.14E+03, 1.17E+03, 1.22E+03, 1.25E+03, 1.30E+03, 1.34E+03, 1.38E+03, 1.42E+03, 1.48E+03, 1.54E+03, 1.67E+03, 1.78E+03],
    [121, 125, 133, 151, 170, 183, 185, 177, 179, 201, 247, 494, 906, 1.48E+03, 1.82E+03, 1.38E+03, 1.12E+03, 1.15E+03, 1.23E+03, 1.10E+03, 998, 970, 980, 1.04E+03, 1.09E+03, 1.16E+03, 1.19E+03, 1.16E+03, 1.16E+03, 1.20E+03, 1.24E+03, 1.31E+03, 1.35E+03, 1.42E+03, 1.48E+03, 1.57E+03, 1.64E+03, 1.70E+03, 1.75E+03, 1.84E+03, 1.94E+03, 2.14E+03, 2.33E+03],
    [151, 160, 168, 183, 198, 216, 233, 265, 296, 367, 439, 602, 787, 953, 1.09E+03, 1.16E+03, 1.10E+03, 1.05E+03, 1.08E+03, 1.02E+03, 953, 930, 938, 993, 1.05E+03, 1.13E+03, 1.16E+03, 1.16E+03, 1.18E+03, 1.23E+03, 1.28E+03, 1.37E+03, 1.43E+03, 1.55E+03, 1.64E+03, 1.79E+03, 1.90E+03, 2.01E+03, 2.10E+03, 2.27E+03, 2.42E+03, 2.76E+03, 3.07E+03]
    ]

    E_He3ion = [1, 2, 3, 5, 10, 14, 20, 30, 50, 75, 100, 150, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 10000, 20000, 50000, 100000]
    f_He3ion = [
    [219, 438, 656, 1.09E+03, 2.19E+03, 4.61E+03, 1.72E+04, 3.01E+04, 4.75E+04, 8.05E+04, 1.01E+05, 9.25E+04, 6.74E+04, 5.14E+04, 4.27E+04, 4.11E+04, 4.00E+04, 4.02E+04, 4.08E+04, 4.12E+04, 4.56E+04, 5.12E+04, 6.12E+04, 7.14E+04],
    [219, 438, 657, 1.09E+03, 2.19E+03, 2.56E+03, 1.74E+03, 1.44E+03, 2.88E+03, 1.75E+04, 4.84E+04, 1.10E+05, 7.29E+04, 5.33E+04, 4.49E+04, 4.60E+04, 4.47E+04, 4.80E+04, 5.01E+04, 5.17E+04, 6.26E+04, 6.10E+04, 8.14E+04, 1.01E+05],
    [141, 281, 419, 689, 1.82E+03, 2.81E+03, 5.46E+03, 9.86E+03, 1.78E+04, 3.00E+04, 4.55E+04, 6.95E+04, 7.01E+04, 5.25E+04, 4.27E+04, 4.19E+04, 4.09E+04, 4.31E+04, 4.50E+04, 4.76E+04, 5.73E+04, 7.10E+04, 9.67E+04, 1.24E+05]
    ]


    E_all = [E_photon, E_electron, E_positron, E_neutron, E_proton, E_negmuon, E_posmuon, E_negpion, E_pospion, E_He3ion]
    f_all = [f_photon, f_electron, f_positron, f_neutron, f_proton, f_negmuon, f_posmuon, f_negpion, f_pospion, f_He3ion]

    pi = find(particle, pars_list)
    if particle in ['photon','neutron','proton']:
        gi = find(geometry, geo_list_all)
    else:
        gi = find(geometry, geo_list_short)

    E_list = E_all[pi]
    f_list = f_all[pi][gi]

    # Interpolate f given E
    if E in E_list:
        f = f_list[find(E,E_list)]
    else:
        if not extrapolation_on and (E < E_list[0] or E > E_list[-1]):  # E is outside of bounds and extrapolation is off
            if E < E_list[0]:
                f = 0   # assume negligibly low energy particle
            if E > E_list[-1]:
                f = f_list[-1]  # just set equal to max energy particle's coefficient
        else:
            if E < E_list[0]:
                E_list = [0] + E_list
                f_list = [0] + f_list
                interp_scale = 'linear'

            if interp_scale=='log':
                cs = interp1d(np.log10(np.array(E_list)),np.log10(np.array(f_list)), kind=interp_type,fill_value='extrapolate')
                f = 10**cs(np.log10(E))
            else:
                cs = interp1d(np.array(E_list),np.array(f_list), kind=interp_type,fill_value='extrapolate')
                f = cs(E)

            # for sake of sanity, return zero for values quite below minimum coefficients
            if f < 1e-4:
                f = 0.0


        #if interp_type=='cubic':
        #    if interp_scale=='log':
        #        cs = interp1d(np.log10(np.array(E_list)),np.log10(np.array(f_list)), kind='cubic',fill_value='extrapolate')
        #        f = 10**cs(np.log10(E))
        #    else:
        #        cs = interp1d(np.array(E_list),np.array(f_list), kind='cubic',fill_value='extrapolate')
        #        f = cs(E)
        #else:
        #    if interp_scale=='log':
        #        f = 10**np.interp(np.log10(E),np.log10(np.array(E_list)),np.log10(np.array(f_list)))
        #    else:
        #        f = np.interp(E,np.array(E_list),np.array(f_list))

        #if interp_type=='cubic':
        #    if interp_scale=='log':
        #        cs = lagrange(np.log10(np.array(E_list)),np.log10(np.array(f_list)))
        #        f = 10**cs(np.log10(E))
        #    else:
        #        cs = lagrange(np.array(E_list),np.array(f_list))
        #        f = cs(E)
        #if interp_type=='cubic':
        #    if interp_scale=='log':
        #        cs = CubicSpline(np.log10(np.array(E_list)),np.log10(np.array(f_list)))
        #        f = 10**cs(np.log10(E))
        #    else:
        #        cs = CubicSpline(np.array(E_list),np.array(f_list))
        #        f = cs(E)

    return f



'''
**************************************************************************************************
------------------------------- MC-TRANSPORT-CODE-RELATED FUNCTIONS ------------------------------
**************************************************************************************************
'''


def fetch_MC_material(matid=None,matname=None,matsource=None,concentration_type=None,particle=None):
    '''
    Description:
        Returns a materials definition string formatted for use in MCNP or PHITS

    Dependencies:
        - `import os`
        - `import pickle`
        - PYTHONPATH environmental variable must be set and one entry must contain the directory
                which contains the vital "MC_tools/materials/Hunters_MC_materials.pkl" file.

    Inputs:
       (required to enter `matid` OR `matname`, with `matid` taking priority if conflicting)

       - `matid` = ID number in the "Hunters_MC_materials" file
       - `matname` = exact name of material in "Hunters_MC_materials" file
       - `matsource` = exact source of material in "Hunters_MC_materials" file, only used when multiple
                materials have identical names
       - `concentration_type` = selection between `'weight fraction'` (default if no formula) and `'atom fraction'` (default if formula present) to be returned
       - `particle` = selection of whether natural (`'photons'`, default) or isotopic (`'neutrons'`) elements are used
                Note that if "enriched" or "depleted" appears in the material's name, particle=`'neutrons'` is set automatically.

    Outputs:
       - `mat_str` = string containing the material's information, ready to be inserted directly into a MCNP/PHITS input deck
    '''

    if not matid and not matname:
        print('Either "matid" or "matname" MUST be defined')
        return None

    # First, locate and open materials library
    try:
        user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
        lib_file = None
        for i in user_paths:
            if 'personal Python scripts' in i:
                lib_file = i + r"\MC_tools\materials\Hunters_MC_materials"
        if not lib_file:
            print('Could not find "personal Python scripts" folder in PYTHONPATH; this folder contains the vital "MC_tools/materials/Hunters_MC_materials.pkl" file.')
    except KeyError:
        print('The PYTHONPATH environmental variable must be defined and contain the path to the directory holding "MC_tools/materials/Hunters_MC_materials.pkl"')
        return None

    # Load materials library
    def load_obj(name ):
        with open(name + '.pkl', 'rb') as f:
            return pickle.load(f)
    all_mats_list = load_obj(lib_file)

    if matid: # use mat ID number
        mi = int(matid)-1
        matname = all_mats_list[mi]['name']
    else: # use material name and possibly source too
        # determine material
        mi = None
        # first check for exact matches
        matching_mi = []
        for i in range(len(all_mats_list)):
            if all_mats_list[i]['name'].lower()==matname.lower():
                matching_mi.append(i)
        if len(matching_mi)==1:
            mi = matching_mi[0]
        elif len(matching_mi)>1:
            print('Found multiple materials with this identical matname value:')
            for mmi in matching_mi:
                print('\tmatid={}  matname="{}"  source="{}"'.format(str(mmi+1),all_mats_list[mmi]['name'],all_mats_list[mmi]['source']))
                if all_mats_list[mmi]['source'] and all_mats_list[mmi]['source']==matsource:
                    mi = mmi
                    print('\t\t^ matches inputed "matsource" and will be used')
            if mi==None:
                print('Please enter a "matsource" value identical to one of these two (or the matid).')
                return None
        else: # Exact material name not found
            # search for similar entries
            similar_mi = []
            for i in range(len(all_mats_list)):
                if matname.lower() in all_mats_list[i]['name'].lower():
                    similar_mi.append(i)
            if len(similar_mi)==0:
                print('No materials with that exact name or names containing "matname" were found.')
                return None
            elif len(similar_mi)==1:
                mi = similar_mi[0]
                print('Found one similar material (matid={}  matname="{}"  source="{}"); using it.'.format(str(mi+1),all_mats_list[mi]['name'],all_mats_list[mi]['source']))
            else:
                print('Found no material with exact "matname" but {} with similar names:'.format(len(similar_mi)))
                for smi in similar_mi:
                    print('\tmatid={}  matname="{}"  source="{}"'.format(str(smi+1),all_mats_list[smi]['name'],all_mats_list[smi]['source']))
                print('The first of these will be used.  If another material was desired, please enter its "matid" or exact "matname".')
                mi = similar_mi[0]

    # Now that material ID has been found, generate text entry
    mat = all_mats_list[mi]
    banner_width = 60
    cc = '$'  # comment character

    entry_text  = '\n'+cc+'*'*banner_width + '\n'
    entry_text += cc+'  {:<3d} : {} \n'.format(mi+1,mat['name'])
    if mat['source'] and mat['source']!='-':
        entry_text += cc+'  Source = {} \n'.format(mat['source'])
    if mat['formula'] and mat['formula']!='-':
        entry_text += cc+'  Formula = {} \n'.format(mat['formula'])
    if mat['molecular weight'] and mat['molecular weight']!='-':
        entry_text += cc+'  Molecular weight (g/mole) = {} \n'.format(mat['molecular weight'])
    if mat['density'] and mat['density']!='-':
        entry_text += cc+'  Density (g/cm3) = {} \n'.format(mat['density'])
    if mat['total atom density'] and mat['total atom density']!='-':
        if isinstance(mat['total atom density'],str):
            entry_text += cc+'  Total atom density (atoms/b-cm) = {} \n'.format(mat['total atom density'])
        else:
            entry_text += cc+'  Total atom density (atoms/b-cm) = {:<13.4E} \n'.format(mat['total atom density'])

    if concentration_type==None: # user did not select this, determine which is more appropriate automatically
        if mat['formula'] and mat['formula']!='-':
            concentration_type = 'atom fraction'
        else:
            concentration_type = 'weight fraction'

    entry_text += cc+'  Composition by {} \n'.format(concentration_type)

    # Determine if neutron or photon entry will be used
    neutron_keyword_list = ['depleted','enriched',' heu',' leu','uranium','plutonium','uranyl']
    if particle==None: # user did not select this, determine which is more appropriate automatically
        neutron_kw_found_in_name = False
        for nki in neutron_keyword_list:
            if nki in matname.lower():
                neutron_kw_found_in_name = True
        if neutron_kw_found_in_name:
            particle = 'neutrons'
        else:
            particle = 'photons'


    for j in range(len(mat[particle][concentration_type]['ZA'])):

        if isinstance(mat[particle][concentration_type]['value'][j],str):
            entry_format = '{:4}    {:>7}  {:13}   '+cc+'  {}'  + '\n'
        else:
            entry_format = '{:4}    {:>7d}  {:<13.6f}   '+cc+'  {}'  + '\n'

        if j==0:
            mstr = 'M{:<3}'.format(mi+1)
        else:
            mstr = ' '*4

        ZZZAAA = mat[particle][concentration_type]['ZA'][j]
        if ZZZAAA == '-':
            ZZZAAA = mat['photons'][concentration_type]['ZA'][j]

        Z = int(str(ZZZAAA)[:-3])
        A = str(ZZZAAA)[-3:]
        sym = Element_Z_to_Sym(Z)
        if A != '000':
            isotope = sym+'-'+A.lstrip('0')
        else:
            isotope = sym

        entry_text += entry_format.format(mstr,ZZZAAA,mat[particle][concentration_type]['value'][j],isotope)
    entry_text  += cc+'*'*banner_width + '\n'

    return entry_text

def parse_tally_dump_file(path_to_dump_file ,dump_data_number ,dump_data_sequence,return_directional_info=False,
                          use_degrees=False,max_entries_read=None,return_namedtuple_list=True,return_Pandas_dataframe=True):
    '''
    Description:
        Parses the dump file of a [T-Cross], [T-Product], or [T-Time] tally generated by PHITS, in ASCII or binary format.

    Inputs:
        - `path_to_dump_file` = string or Path object denoting the path to the dump tally output file to be parsed
        - `dump_data_number` = integer number of data per row in dump file, binary if >0 and ASCII if <0.
                 This should match the value following `dump=` in the tally creating the dump file.
        - `dump_data_sequence` = string or list of integers with the same number of entries as `dump_data_number`,
                 mapping each column in the dump file to their physical quantities.
                 This should match the line following the `dump=` line in the tally creating the dump file.
                 See PHITS manual section "6.7.22 dump parameter" for further explanations of these values.
        - `return_directional_info` = (optional, D=`False`) Boolean designating whether extra directional information
                 should be calculated and returned; these include: radial distance `r` from the origin in cm,
                 radial distance `rho` from the z-axis in cm,
                 polar angle `theta` between the direction vector and z-axis in radians [0,pi] (or degrees), and
                 azimuthal angle `phi` of the direction vector in radians [-pi,pi] (or degrees).
                 Note: This option requires all position and direction values [x,y,z,u,v,w] to be included in the dump file.
        - `use_degrees` = (optional, D=`False`) Boolean designating whether angles `theta` and `phi` are returned
                 in units of degrees. Default setting is to return angles in radians.
        - `max_entries_read` = (optional, D=`None`) integer number specifying the maximum number of entries/records
                 of the dump file to be read.  By default, all records in the dump file are read.
        - `return_namedtuple_list` = (optional, D=`True`) Boolean designating whether `dump_data_list` is returned.
        - `return_Pandas_dataframe` = (optional, D=`True`) Boolean designating whether `dump_data_frame` is returned.

    Outputs:
        - `dump_data_list` = List of length equal to the number of records contained in the file. Each entry in the list
                 is a namedtuple containing all of the physical information in the dump file for a given particle event,
                 in the same order as specified in `dump_data_sequence` and using the same naming conventions for keys as
                 described in the PHITS manual section "6.7.22 dump parameter". If `return_directional_info = True`,
                 `r`, `rho`, `theta`, and `phi` are appended to the end of this namedtuple, in that order.
        - `dump_data_frame` = A Pandas dataframe created from `dump_data_list` with columns for each physical quantity
                 and rows for each record included in the dump file.
    '''

    if not return_namedtuple_list and not return_Pandas_dataframe:
        print('ERROR: Both "return_namedtuple_list" and "return_Pandas_dataframe" are False. Enable at least one to use this function.')
        sys.exit()

    if isinstance(dump_data_sequence, str):
        dump_data_sequence = dump_data_sequence.split()
        dump_data_sequence = [int(i) for i in dump_data_sequence]
    dump_file_is_binary = True if (dump_data_number > 0) else False  # if not binary, file will be ASCII
    data_values_per_line = abs(dump_data_number)
    if data_values_per_line != len(dump_data_sequence):
        print('ERROR: Number of values in "dump_data_sequence" is not equal to "dump_data_number"')
        sys.exit()

    # Generate NamedTuple for storing record information
    # See PHITS manual section "6.7.22 dump parameter" for descriptions of these values
    dump_quantities = ['kf', 'x', 'y', 'z', 'u', 'v', 'w', 'e', 'wt', 'time', 'c1', 'c2', 'c3', 'sx', 'sy', 'sz',
                       'name', 'nocas', 'nobch', 'no']
    ordered_record_entries_list = [dump_quantities[i - 1] for i in dump_data_sequence]
    rawRecord = namedtuple('rawRecord', ordered_record_entries_list)
    if return_directional_info:
        ordered_record_entries_list += ['r', 'rho', 'theta', 'phi']
        angle_units_mult = 1
        if use_degrees: angle_units_mult = 180 / np.pi
    Record = namedtuple('Record', ordered_record_entries_list)

    records_list = []
    if dump_file_is_binary:
        # Read binary dump file; extract each record (particle)
        file_size_bytes = os.path.getsize(path_to_dump_file)
        record_size_bytes = (data_values_per_line + 1) * 8  # each record has 8 bytes per data value plus an 8-byte record end
        num_records = int(file_size_bytes / record_size_bytes)
        if max_entries_read != None:
            if max_entries_read < num_records:
                num_records = max_entries_read
        # print(num_records)
        current_record_count = 0
        if return_directional_info:
            with FortranFile(path_to_dump_file, 'r') as f:
                while current_record_count < num_records:
                    current_record_count += 1
                    raw_values = f.read_reals(float)
                    rawrecord = rawRecord(*raw_values)
                    # calculate r, rho, theta (w.r.t. z-axis), and phi (w.r.t. x axis)
                    r = np.sqrt(rawrecord.x ** 2 + rawrecord.y ** 2 + rawrecord.z ** 2)
                    rho = np.sqrt(rawrecord.x ** 2 + rawrecord.y ** 2)
                    dir_vector = [rawrecord.u, rawrecord.v, rawrecord.w]
                    theta = np.arccos(np.clip(np.dot(dir_vector, [0, 0, 1]), -1.0, 1.0)) * angle_units_mult
                    phi = np.arctan2(rawrecord.y, rawrecord.x) * angle_units_mult
                    record = Record(*raw_values, r, rho, theta, phi)
                    records_list.append(record)
        else: # just return data in dump file
            with FortranFile(path_to_dump_file, 'r') as f:
                while current_record_count < num_records:
                    current_record_count += 1
                    raw_values = f.read_reals(float)
                    record = Record(*raw_values)
                    records_list.append(record)
    else: # file is ASCII
        if max_entries_read == None:
            max_entries_read = np.inf
        if return_directional_info:
            with open(path_to_dump_file, 'r') as f:
                current_record_count = 0
                for line in f:
                    current_record_count += 1
                    if current_record_count > max_entries_read: break
                    line_str_values = line.replace('D', 'E').split()
                    raw_values = [float(i) for i in line_str_values]
                    rawrecord = rawRecord(*raw_values)
                    # calculate r, rho, theta (w.r.t. z-axis), and phi (w.r.t. x axis)
                    r = np.sqrt(rawrecord.x ** 2 + rawrecord.y ** 2 + rawrecord.z ** 2)
                    rho = np.sqrt(rawrecord.x ** 2 + rawrecord.y ** 2)
                    dir_vector = [rawrecord.u, rawrecord.v, rawrecord.w]
                    theta = np.arccos(np.clip(np.dot(dir_vector, [0, 0, 1]), -1.0, 1.0)) * angle_units_mult
                    phi = np.arctan2(rawrecord.y, rawrecord.x) * angle_units_mult
                    record = Record(*raw_values, r, theta, phi)
                    records_list.append(record)
        else: # just return data in dump file
            with open(path_to_dump_file, 'r') as f:
                current_record_count = 0
                for line in f:
                    current_record_count += 1
                    if current_record_count > max_entries_read: break
                    line_str_values = line.replace('D', 'E').split()
                    raw_values = [float(i) for i in line_str_values]
                    record = Record(*raw_values)
                    records_list.append(record)
    #print(record)

    if return_Pandas_dataframe:
        # Make Pandas dataframe from list of records
        records_df = pd.DataFrame(records_list, columns=Record._fields)

    if return_namedtuple_list and return_Pandas_dataframe:
        return records_list, records_df
    elif return_namedtuple_list:
        return records_list
    elif return_Pandas_dataframe:
        return records_df
    else:
        return None

def parse_ttrack_file(path_to_dtrk_file,return_metadata=False):
    '''
    Description:
        Parses the output file of a T-Track tally generated by PHITS.  Note that this specific function assumes that the T-Track
        tally was one automatically generated by and corresponding to a T-Dchain tally but in principle works with any T-Track tally.
        This works for region, xyz, and tetrahedral mesh geometries in either the original or reduced format.
        It is currently only designed for tallies tracking a single particle (or "all").

    Inputs:
        - `path_to_dtrk_file` = path to the T-Track tally output file to be parsed
        - `return_metadata` = Boolean indicating whether additional information is outputted with the flux (D=`False`)

    Outputs:
        - `flux` = a RxEx4 array containing regionwise fluxes [x-lower/x-upper/flux/abs_error]
        - `dtrk_metadata` (only returned if `return_metadata=True`) = list of length two
               - `dtrk_metadata[0]` = string denoting axis type 'eng' (old full format) or 'dchain' (new reduced format)
               - `dtrk_metadata[1]` = string denoting mesh type as either 'reg', 'xyz', or 'tet'
    '''

    # Extract text from file
    f = open(path_to_dtrk_file)
    file_text = f.read()
    lines = file_text.split('\n')
    f.close()

    # Determine geometry type (mesh = reg, xyz, or tet)
    for line in lines:
        if 'mesh =' in line:
            meshtype = line.replace('mesh =','').strip().split()[0]
            break

    # Determine if original or reduced format (axis = eng or axis = dchain or axis=x/y/z)
    for line in lines:
        if 'axis =' in line:
            axistype = line.replace('axis =','').strip().split()[0]
            break

    if meshtype=='xyz':
        nx, ny, nz = 0, 0, 0
        for line in lines:
            if 'nx =' in line:
                nx = int(line.replace('nx =','').strip().split()[0])
                break
        for line in lines:
            if 'ny =' in line:
                ny = int(line.replace('ny =','').strip().split()[0])
                break
        for line in lines:
            if 'nz =' in line:
                nz = int(line.replace('nz =','').strip().split()[0])
                break
        nreg = nx*ny*nz


    dtrk_metadata = [axistype,meshtype]

    # Determine number of regions
    if axistype=='eng':
        nreg = file_text.count('#   no. =')
    elif axistype in ['x','y','z']:
        #nreg = nx*ny*nz
        if axistype=='x': nbins = nx
        if axistype=='y': nbins = ny
        if axistype=='z': nbins = nz
    elif axistype=='dchain':
        for li, line in reversed(list(enumerate(lines))):
            #print(line)
            if '0    0   0.0000E+00  0.0000' in line:
                nreg = int(lines[li-1].split()[0])
                break

    if axistype=='dchain':
        nEbins = 1968
    else:
        for line in lines:
            if 'ne =' in line:
                nEbins = int(line.replace('ne =','').strip().split()[0])
                break

    if meshtype=='xyz':
        flux = np.zeros((nx,ny,nz,nEbins,4))
    else:
        flux = np.zeros((nreg,nEbins,4))

    if axistype=='eng':
        in_flux_lines = False
        ei = 0
        ri = -1

        for line in lines:
            if '#   no. =' in line:
                ri += 1
            if '#  e-lower      e-upper ' in line:
                in_flux_lines = True
                continue
            if in_flux_lines:
                flux[ri,ei,:] = [float(x) for x in line.split()]
                flux[ri,ei,3] = flux[ri,ei,3]*flux[ri,ei,2] # convert relative error to absolute error
                ei += 1
                if ei == nEbins:
                    in_flux_lines = False
                    ei = 0

    elif axistype in ['x','y','z']:
        xi, yi, zi, ei = 0, 0, 0, 0
        ie_edges, ix_edges, iy_edges, iz_edges = [],[],[],[]
        in_flux_lines = False
        for line in lines:
            if '#   no. =' in line:
                parts = line.split()
                if 'ie' in parts: ei = int(parts[2+parts.index('ie')])-1
                if 'ix' in parts: xi = int(parts[2+parts.index('ix')])-1
                if 'iy' in parts: yi = int(parts[2+parts.index('iy')])-1
                if 'iz' in parts: zi = int(parts[2+parts.index('iz')])-1
            if '#   e =' in line:
                parts = line.split()
                ie_edges.append([float(parts[4]),float(parts[6])])
            if '#   x =' in line:
                parts = line.split()
                ix_edges.append([float(parts[4]),float(parts[6])])
            if '#   y =' in line:
                parts = line.split()
                iy_edges.append([float(parts[4]),float(parts[6])])
            if '#   z =' in line:
                parts = line.split()
                iz_edges.append([float(parts[4]),float(parts[6])])

            if '#  {}-lower      {}-upper '.format(axistype,axistype) in line:
                in_flux_lines = True
                continue

            if in_flux_lines:
                flux[xi,yi,zi,ei,:] = [float(x) for x in line.split()]
                flux[xi,yi,zi,ei,3] = flux[xi,yi,zi,ei,3]*flux[xi,yi,zi,ei,2] # convert relative error to absolute error
                if axistype=='x':
                    xi += 1
                    if xi==nbins:
                        in_flux_lines = False
                        xi=0
                if axistype=='y':
                    yi += 1
                    if yi==nbins:
                        in_flux_lines = False
                        yi=0
                if axistype=='z':
                    zi += 1
                    if zi==nbins:
                        in_flux_lines = False
                        zi=0



    elif axistype=='dchain':
        ebins = [20.0,
        1.964033E+01,1.947734E+01,1.931570E+01,1.915541E+01,1.899644E+01,1.883880E+01,1.868246E+01,1.852742E+01,1.837367E+01,1.822119E+01,1.806998E+01,1.792002E+01,1.777131E+01,1.762383E+01,1.747757E+01,1.733253E+01,1.718869E+01,1.704605E+01,1.690459E+01,1.676430E+01,1.662518E+01,
        1.648721E+01,1.635039E+01,1.621470E+01,1.608014E+01,1.594670E+01,1.581436E+01,1.568312E+01,1.555297E+01,1.542390E+01,1.529590E+01,1.516897E+01,1.504309E+01,1.491825E+01,1.479444E+01,1.467167E+01,1.454991E+01,1.442917E+01,1.430943E+01,1.419068E+01,1.407291E+01,
        1.395612E+01,1.384031E+01,1.372545E+01,1.361155E+01,1.349859E+01,1.338657E+01,1.327548E+01,1.316531E+01,1.305605E+01,1.294770E+01,1.284025E+01,1.273370E+01,1.262802E+01,1.252323E+01,1.241930E+01,1.231624E+01,1.221403E+01,1.211267E+01,1.201215E+01,1.191246E+01,
        1.181360E+01,1.171557E+01,1.161834E+01,1.152193E+01,1.142631E+01,1.133148E+01,1.123745E+01,1.114419E+01,1.105171E+01,1.095999E+01,1.086904E+01,1.077884E+01,1.068939E+01,1.060068E+01,1.051271E+01,1.042547E+01,1.033895E+01,1.025315E+01,1.016806E+01,1.008368E+01,
        1.000000E+01,9.917013E+00,9.834715E+00,9.753099E+00,9.672161E+00,9.591895E+00,9.512294E+00,9.433354E+00,9.355070E+00,9.277435E+00,9.200444E+00,9.124092E+00,9.048374E+00,8.973284E+00,8.898818E+00,8.824969E+00,8.751733E+00,8.679105E+00,8.607080E+00,8.535652E+00,
        8.464817E+00,8.394570E+00,8.324906E+00,8.255820E+00,8.187308E+00,8.119363E+00,8.051983E+00,7.985162E+00,7.918896E+00,7.853179E+00,7.788008E+00,7.723377E+00,7.659283E+00,7.595721E+00,7.532687E+00,7.470175E+00,7.408182E+00,7.346704E+00,7.285736E+00,7.225274E+00,
        7.165313E+00,7.105850E+00,7.046881E+00,6.988401E+00,6.930406E+00,6.872893E+00,6.815857E+00,6.759294E+00,6.703200E+00,6.647573E+00,6.592406E+00,6.537698E+00,6.483443E+00,6.429639E+00,6.376282E+00,6.323367E+00,6.270891E+00,6.218851E+00,6.167242E+00,6.116062E+00,
        6.065307E+00,6.014972E+00,5.965056E+00,5.915554E+00,5.866462E+00,5.817778E+00,5.769498E+00,5.721619E+00,5.674137E+00,5.627049E+00,5.580351E+00,5.534042E+00,5.488116E+00,5.442572E+00,5.397406E+00,5.352614E+00,5.308195E+00,5.264143E+00,5.220458E+00,5.177135E+00,
        5.134171E+00,5.091564E+00,5.049311E+00,5.007408E+00,4.965853E+00,4.924643E+00,4.883775E+00,4.843246E+00,4.803053E+00,4.763194E+00,4.723666E+00,4.684465E+00,4.645590E+00,4.607038E+00,4.568805E+00,4.530890E+00,4.493290E+00,4.456001E+00,4.419022E+00,4.382350E+00,
        4.345982E+00,4.309916E+00,4.274149E+00,4.238679E+00,4.203504E+00,4.168620E+00,4.134026E+00,4.099719E+00,4.065697E+00,4.031957E+00,3.998497E+00,3.965314E+00,3.932407E+00,3.899773E+00,3.867410E+00,3.835316E+00,3.803488E+00,3.771924E+00,3.740621E+00,3.709579E+00,
        3.678794E+00,3.648265E+00,3.617989E+00,3.587965E+00,3.558189E+00,3.528661E+00,3.499377E+00,3.470337E+00,3.441538E+00,3.412978E+00,3.384654E+00,3.356566E+00,3.328711E+00,3.301087E+00,3.273692E+00,3.246525E+00,3.219583E+00,3.192864E+00,3.166368E+00,3.140091E+00,
        3.114032E+00,3.088190E+00,3.062562E+00,3.037147E+00,3.011942E+00,2.986947E+00,2.962159E+00,2.937577E+00,2.913199E+00,2.889023E+00,2.865048E+00,2.841272E+00,2.817693E+00,2.794310E+00,2.771121E+00,2.748124E+00,2.725318E+00,2.702701E+00,2.680272E+00,2.658030E+00,
        2.635971E+00,2.614096E+00,2.592403E+00,2.570889E+00,2.549554E+00,2.528396E+00,2.507414E+00,2.486605E+00,2.465970E+00,2.445505E+00,2.425211E+00,2.405085E+00,2.385126E+00,2.365332E+00,2.345703E+00,2.326237E+00,2.306932E+00,2.287787E+00,2.268802E+00,2.249973E+00,
        2.231302E+00,2.212785E+00,2.194421E+00,2.176211E+00,2.158151E+00,2.140241E+00,2.122480E+00,2.104866E+00,2.087398E+00,2.070076E+00,2.052897E+00,2.035860E+00,2.018965E+00,2.002210E+00,1.985595E+00,1.969117E+00,1.952776E+00,1.936570E+00,1.920499E+00,1.904561E+00,
        1.888756E+00,1.873082E+00,1.857538E+00,1.842122E+00,1.826835E+00,1.811675E+00,1.796640E+00,1.781731E+00,1.766944E+00,1.752281E+00,1.737739E+00,1.723318E+00,1.709017E+00,1.694834E+00,1.680770E+00,1.666821E+00,1.652989E+00,1.639271E+00,1.625667E+00,1.612176E+00,
        1.598797E+00,1.585530E+00,1.572372E+00,1.559323E+00,1.546383E+00,1.533550E+00,1.520823E+00,1.508202E+00,1.495686E+00,1.483274E+00,1.470965E+00,1.458758E+00,1.446652E+00,1.434646E+00,1.422741E+00,1.410934E+00,1.399225E+00,1.387613E+00,1.376098E+00,1.364678E+00,
        1.353353E+00,1.342122E+00,1.330984E+00,1.319938E+00,1.308985E+00,1.298122E+00,1.287349E+00,1.276666E+00,1.266071E+00,1.255564E+00,1.245145E+00,1.234812E+00,1.224564E+00,1.214402E+00,1.204324E+00,1.194330E+00,1.184418E+00,1.174589E+00,1.164842E+00,1.155175E+00,
        1.145588E+00,1.136082E+00,1.126654E+00,1.117304E+00,1.108032E+00,1.098836E+00,1.089717E+00,1.080674E+00,1.071706E+00,1.062812E+00,1.053992E+00,1.045245E+00,1.036571E+00,1.027969E+00,1.019438E+00,1.010978E+00,1.002588E+00,9.942682E-01,9.860171E-01,9.778344E-01,
        9.697197E-01,9.616723E-01,9.536916E-01,9.457772E-01,9.379285E-01,9.301449E-01,9.224259E-01,9.147709E-01,9.071795E-01,8.996511E-01,8.921852E-01,8.847812E-01,8.774387E-01,8.701570E-01,8.629359E-01,8.557746E-01,8.486728E-01,8.416299E-01,8.346455E-01,8.277190E-01,
        8.208500E-01,8.140380E-01,8.072825E-01,8.005831E-01,7.939393E-01,7.873507E-01,7.808167E-01,7.743369E-01,7.679109E-01,7.615382E-01,7.552184E-01,7.489511E-01,7.427358E-01,7.365720E-01,7.304594E-01,7.243976E-01,7.183860E-01,7.124243E-01,7.065121E-01,7.006490E-01,
        6.948345E-01,6.890683E-01,6.833499E-01,6.776790E-01,6.720551E-01,6.664779E-01,6.609470E-01,6.554620E-01,6.500225E-01,6.446282E-01,6.392786E-01,6.339734E-01,6.287123E-01,6.234948E-01,6.183206E-01,6.131893E-01,6.081006E-01,6.030542E-01,5.980496E-01,5.930866E-01,
        5.881647E-01,5.832837E-01,5.784432E-01,5.736429E-01,5.688824E-01,5.641614E-01,5.594796E-01,5.548366E-01,5.502322E-01,5.456660E-01,5.411377E-01,5.366469E-01,5.321934E-01,5.277769E-01,5.233971E-01,5.190535E-01,5.147461E-01,5.104743E-01,5.062381E-01,5.020369E-01,
        4.978707E-01,4.937390E-01,4.896416E-01,4.855782E-01,4.815485E-01,4.775523E-01,4.735892E-01,4.696591E-01,4.657615E-01,4.618963E-01,4.580631E-01,4.542618E-01,4.504920E-01,4.467535E-01,4.430460E-01,4.393693E-01,4.357231E-01,4.321072E-01,4.285213E-01,4.249651E-01,
        4.214384E-01,4.179410E-01,4.144727E-01,4.110331E-01,4.076220E-01,4.042393E-01,4.008846E-01,3.975578E-01,3.942586E-01,3.909868E-01,3.877421E-01,3.845243E-01,3.813333E-01,3.781687E-01,3.750304E-01,3.719181E-01,3.688317E-01,3.657708E-01,3.627354E-01,3.597252E-01,
        3.567399E-01,3.537795E-01,3.508435E-01,3.479320E-01,3.450446E-01,3.421812E-01,3.393415E-01,3.365254E-01,3.337327E-01,3.309631E-01,3.282166E-01,3.254928E-01,3.227916E-01,3.201129E-01,3.174564E-01,3.148219E-01,3.122093E-01,3.096183E-01,3.070489E-01,3.045008E-01,
        3.019738E-01,2.994678E-01,2.985000E-01,2.972000E-01,2.969826E-01,2.945181E-01,2.920740E-01,2.896501E-01,2.872464E-01,2.848626E-01,2.824986E-01,2.801543E-01,2.778293E-01,2.755237E-01,2.732372E-01,2.709697E-01,2.687210E-01,2.664910E-01,2.642794E-01,2.620863E-01,
        2.599113E-01,2.577544E-01,2.556153E-01,2.534941E-01,2.513904E-01,2.493042E-01,2.472353E-01,2.451835E-01,2.431488E-01,2.411310E-01,2.391299E-01,2.371455E-01,2.351775E-01,2.332258E-01,2.312903E-01,2.293709E-01,2.274674E-01,2.255797E-01,2.237077E-01,2.218512E-01,
        2.200102E-01,2.181844E-01,2.163737E-01,2.145781E-01,2.127974E-01,2.110314E-01,2.092801E-01,2.075434E-01,2.058210E-01,2.041130E-01,2.024191E-01,2.007393E-01,1.990734E-01,1.974214E-01,1.957830E-01,1.941583E-01,1.925470E-01,1.909491E-01,1.893645E-01,1.877930E-01,
        1.862346E-01,1.846891E-01,1.831564E-01,1.816364E-01,1.801291E-01,1.786342E-01,1.771518E-01,1.756817E-01,1.742237E-01,1.727779E-01,1.713441E-01,1.699221E-01,1.685120E-01,1.671136E-01,1.657268E-01,1.643514E-01,1.629875E-01,1.616349E-01,1.602936E-01,1.589634E-01,
        1.576442E-01,1.563359E-01,1.550385E-01,1.537519E-01,1.524760E-01,1.512106E-01,1.499558E-01,1.487113E-01,1.474772E-01,1.462533E-01,1.450396E-01,1.438360E-01,1.426423E-01,1.414586E-01,1.402847E-01,1.391205E-01,1.379660E-01,1.368210E-01,1.356856E-01,1.345596E-01,
        1.334429E-01,1.323355E-01,1.312373E-01,1.301482E-01,1.290681E-01,1.279970E-01,1.269348E-01,1.258814E-01,1.248368E-01,1.238008E-01,1.227734E-01,1.217545E-01,1.207441E-01,1.197421E-01,1.187484E-01,1.177629E-01,1.167857E-01,1.158165E-01,1.148554E-01,1.139022E-01,
        1.129570E-01,1.120196E-01,1.110900E-01,1.101681E-01,1.092538E-01,1.083471E-01,1.074480E-01,1.065563E-01,1.056720E-01,1.047951E-01,1.039254E-01,1.030630E-01,1.022077E-01,1.013595E-01,1.005184E-01,9.968419E-02,9.885694E-02,9.803655E-02,9.722297E-02,9.641615E-02,
        9.561602E-02,9.482253E-02,9.403563E-02,9.325525E-02,9.248135E-02,9.171388E-02,9.095277E-02,9.019798E-02,8.944945E-02,8.870714E-02,8.797098E-02,8.724094E-02,8.651695E-02,8.579897E-02,8.508695E-02,8.438084E-02,8.368059E-02,8.298615E-02,8.250000E-02,8.229747E-02,
        8.161451E-02,8.093721E-02,8.026554E-02,7.959944E-02,7.950000E-02,7.893887E-02,7.828378E-02,7.763412E-02,7.698986E-02,7.635094E-02,7.571733E-02,7.508897E-02,7.446583E-02,7.384786E-02,7.323502E-02,7.262726E-02,7.202455E-02,7.142684E-02,7.083409E-02,7.024626E-02,
        6.966330E-02,6.908519E-02,6.851187E-02,6.794331E-02,6.737947E-02,6.682031E-02,6.626579E-02,6.571586E-02,6.517051E-02,6.462968E-02,6.409333E-02,6.356144E-02,6.303396E-02,6.251086E-02,6.199211E-02,6.147765E-02,6.096747E-02,6.046151E-02,5.995976E-02,5.946217E-02,
        5.896871E-02,5.847935E-02,5.799405E-02,5.751277E-02,5.703549E-02,5.656217E-02,5.609278E-02,5.562728E-02,5.516564E-02,5.470784E-02,5.425384E-02,5.380360E-02,5.335710E-02,5.291430E-02,5.247518E-02,5.203971E-02,5.160785E-02,5.117957E-02,5.075484E-02,5.033364E-02,
        4.991594E-02,4.950170E-02,4.909090E-02,4.868351E-02,4.827950E-02,4.787884E-02,4.748151E-02,4.708747E-02,4.669671E-02,4.630919E-02,4.592488E-02,4.554376E-02,4.516581E-02,4.479099E-02,4.441928E-02,4.405066E-02,4.368510E-02,4.332257E-02,4.296305E-02,4.260651E-02,
        4.225293E-02,4.190229E-02,4.155455E-02,4.120970E-02,4.086771E-02,4.052857E-02,4.019223E-02,3.985869E-02,3.952791E-02,3.919988E-02,3.887457E-02,3.855196E-02,3.823203E-02,3.791476E-02,3.760011E-02,3.728808E-02,3.697864E-02,3.667176E-02,3.636743E-02,3.606563E-02,
        3.576633E-02,3.546952E-02,3.517517E-02,3.488326E-02,3.459377E-02,3.430669E-02,3.402199E-02,3.373965E-02,3.345965E-02,3.318198E-02,3.290662E-02,3.263353E-02,3.236272E-02,3.209415E-02,3.182781E-02,3.156368E-02,3.130174E-02,3.104198E-02,3.078437E-02,3.052890E-02,
        3.027555E-02,3.002430E-02,2.977514E-02,2.952804E-02,2.928300E-02,2.903999E-02,2.879899E-02,2.856000E-02,2.850000E-02,2.832299E-02,2.808794E-02,2.785485E-02,2.762369E-02,2.739445E-02,2.716711E-02,2.700000E-02,2.694166E-02,2.671808E-02,2.649635E-02,2.627647E-02,
        2.605841E-02,2.584215E-02,2.562770E-02,2.541502E-02,2.520411E-02,2.499495E-02,2.478752E-02,2.458182E-02,2.437782E-02,2.417552E-02,2.397489E-02,2.377593E-02,2.357862E-02,2.338295E-02,2.318890E-02,2.299646E-02,2.280562E-02,2.261636E-02,2.242868E-02,2.224255E-02,
        2.205796E-02,2.187491E-02,2.169338E-02,2.151335E-02,2.133482E-02,2.115777E-02,2.098218E-02,2.080806E-02,2.063538E-02,2.046413E-02,2.029431E-02,2.012589E-02,1.995887E-02,1.979324E-02,1.962898E-02,1.946608E-02,1.930454E-02,1.914434E-02,1.898547E-02,1.882791E-02,
        1.867166E-02,1.851671E-02,1.836305E-02,1.821066E-02,1.805953E-02,1.790966E-02,1.776104E-02,1.761364E-02,1.746747E-02,1.732251E-02,1.717876E-02,1.703620E-02,1.689482E-02,1.675461E-02,1.661557E-02,1.647768E-02,1.634094E-02,1.620533E-02,1.607085E-02,1.593748E-02,
        1.580522E-02,1.567406E-02,1.554398E-02,1.541499E-02,1.528706E-02,1.516020E-02,1.503439E-02,1.490963E-02,1.478590E-02,1.466319E-02,1.454151E-02,1.442083E-02,1.430116E-02,1.418247E-02,1.406478E-02,1.394806E-02,1.383231E-02,1.371752E-02,1.360368E-02,1.349079E-02,
        1.337883E-02,1.326780E-02,1.315770E-02,1.304851E-02,1.294022E-02,1.283283E-02,1.272634E-02,1.262073E-02,1.251599E-02,1.241212E-02,1.230912E-02,1.220697E-02,1.210567E-02,1.200521E-02,1.190558E-02,1.180678E-02,1.170880E-02,1.161163E-02,1.151527E-02,1.141970E-02,
        1.132494E-02,1.123095E-02,1.113775E-02,1.104532E-02,1.095366E-02,1.086276E-02,1.077261E-02,1.068321E-02,1.059456E-02,1.050664E-02,1.041944E-02,1.033298E-02,1.024723E-02,1.016219E-02,1.007785E-02,9.994221E-03,9.911282E-03,9.829031E-03,9.747463E-03,9.666572E-03,
        9.586352E-03,9.506797E-03,9.427903E-03,9.349664E-03,9.272074E-03,9.195127E-03,9.118820E-03,9.043145E-03,8.968099E-03,8.893675E-03,8.819869E-03,8.746676E-03,8.674090E-03,8.602106E-03,8.530719E-03,8.459926E-03,8.389719E-03,8.320095E-03,8.251049E-03,8.182576E-03,
        8.114671E-03,8.047330E-03,7.980548E-03,7.914319E-03,7.848641E-03,7.783507E-03,7.718914E-03,7.654857E-03,7.591332E-03,7.528334E-03,7.465858E-03,7.403901E-03,7.342458E-03,7.281525E-03,7.221098E-03,7.161172E-03,7.101744E-03,7.042809E-03,6.984362E-03,6.926401E-03,
        6.868921E-03,6.811918E-03,6.755388E-03,6.699327E-03,6.643731E-03,6.588597E-03,6.533920E-03,6.479697E-03,6.425924E-03,6.372597E-03,6.319712E-03,6.267267E-03,6.215257E-03,6.163678E-03,6.112528E-03,6.061802E-03,6.011496E-03,5.961609E-03,5.912135E-03,5.863072E-03,
        5.814416E-03,5.766164E-03,5.718312E-03,5.670858E-03,5.623797E-03,5.577127E-03,5.530844E-03,5.484945E-03,5.439427E-03,5.394287E-03,5.349521E-03,5.305127E-03,5.261101E-03,5.217441E-03,5.174143E-03,5.131204E-03,5.088622E-03,5.046393E-03,5.004514E-03,4.962983E-03,
        4.921797E-03,4.880952E-03,4.840447E-03,4.800277E-03,4.760441E-03,4.720936E-03,4.681758E-03,4.642906E-03,4.604375E-03,4.566165E-03,4.528272E-03,4.490693E-03,4.453426E-03,4.416468E-03,4.379817E-03,4.343471E-03,4.307425E-03,4.271679E-03,4.236230E-03,4.201075E-03,
        4.166211E-03,4.131637E-03,4.097350E-03,4.063347E-03,4.029627E-03,3.996186E-03,3.963023E-03,3.930135E-03,3.897520E-03,3.865175E-03,3.833099E-03,3.801290E-03,3.769744E-03,3.738460E-03,3.707435E-03,3.676668E-03,3.646157E-03,3.615898E-03,3.585891E-03,3.556133E-03,
        3.526622E-03,3.497355E-03,3.468332E-03,3.439549E-03,3.411005E-03,3.382698E-03,3.354626E-03,3.326787E-03,3.299179E-03,3.271800E-03,3.244649E-03,3.217722E-03,3.191019E-03,3.164538E-03,3.138276E-03,3.112233E-03,3.086405E-03,3.060792E-03,3.035391E-03,3.010202E-03,
        2.985221E-03,2.960447E-03,2.935879E-03,2.911515E-03,2.887354E-03,2.863392E-03,2.839630E-03,2.816065E-03,2.792695E-03,2.769519E-03,2.746536E-03,2.723743E-03,2.701139E-03,2.678723E-03,2.656494E-03,2.634448E-03,2.612586E-03,2.590904E-03,2.569403E-03,2.548081E-03,
        2.526935E-03,2.505965E-03,2.485168E-03,2.464545E-03,2.444092E-03,2.423809E-03,2.403695E-03,2.383747E-03,2.363965E-03,2.344347E-03,2.324892E-03,2.305599E-03,2.286465E-03,2.267490E-03,2.248673E-03,2.230012E-03,2.211506E-03,2.193153E-03,2.174953E-03,2.156904E-03,
        2.139004E-03,2.121253E-03,2.103650E-03,2.086192E-03,2.068879E-03,2.051710E-03,2.034684E-03,2.017798E-03,2.001053E-03,1.984447E-03,1.967979E-03,1.951647E-03,1.935451E-03,1.919389E-03,1.903461E-03,1.887665E-03,1.871999E-03,1.856464E-03,1.841058E-03,1.825780E-03,
        1.810628E-03,1.795602E-03,1.780701E-03,1.765923E-03,1.751268E-03,1.736735E-03,1.722323E-03,1.708030E-03,1.693855E-03,1.679798E-03,1.665858E-03,1.652034E-03,1.638324E-03,1.624728E-03,1.611245E-03,1.597874E-03,1.584613E-03,1.571463E-03,1.558422E-03,1.545489E-03,
        1.532663E-03,1.519944E-03,1.507331E-03,1.494822E-03,1.482417E-03,1.470115E-03,1.457915E-03,1.445816E-03,1.433817E-03,1.421919E-03,1.410118E-03,1.398416E-03,1.386811E-03,1.375303E-03,1.363889E-03,1.352571E-03,1.341346E-03,1.330215E-03,1.319176E-03,1.308228E-03,
        1.297372E-03,1.286605E-03,1.275928E-03,1.265339E-03,1.254839E-03,1.244425E-03,1.234098E-03,1.223857E-03,1.213700E-03,1.203628E-03,1.193639E-03,1.183734E-03,1.173910E-03,1.164168E-03,1.154507E-03,1.144926E-03,1.135425E-03,1.126002E-03,1.116658E-03,1.107391E-03,
        1.098201E-03,1.089088E-03,1.080050E-03,1.071087E-03,1.062198E-03,1.053383E-03,1.044641E-03,1.035972E-03,1.027375E-03,1.018849E-03,1.010394E-03,1.002009E-03,9.936937E-04,9.854473E-04,9.772694E-04,9.691593E-04,9.611165E-04,9.531405E-04,9.452307E-04,9.373865E-04,
        9.296074E-04,9.218928E-04,9.142423E-04,9.066553E-04,8.991312E-04,8.916696E-04,8.842699E-04,8.769316E-04,8.696542E-04,8.624372E-04,8.552801E-04,8.481824E-04,8.411435E-04,8.341631E-04,8.272407E-04,8.203756E-04,8.135676E-04,8.068160E-04,8.001205E-04,7.934805E-04,
        7.868957E-04,7.803654E-04,7.738894E-04,7.674671E-04,7.610981E-04,7.547820E-04,7.485183E-04,7.423066E-04,7.361464E-04,7.300373E-04,7.239790E-04,7.179709E-04,7.120126E-04,7.061038E-04,7.002441E-04,6.944330E-04,6.886701E-04,6.829550E-04,6.772874E-04,6.716668E-04,
        6.660928E-04,6.605651E-04,6.550832E-04,6.496469E-04,6.442557E-04,6.389092E-04,6.336071E-04,6.283489E-04,6.231345E-04,6.179633E-04,6.128350E-04,6.077492E-04,6.027057E-04,5.977040E-04,5.927438E-04,5.878248E-04,5.829466E-04,5.781089E-04,5.733114E-04,5.685536E-04,
        5.638354E-04,5.591563E-04,5.545160E-04,5.499142E-04,5.453506E-04,5.408249E-04,5.363368E-04,5.318859E-04,5.274719E-04,5.230946E-04,5.187536E-04,5.144486E-04,5.101793E-04,5.059455E-04,5.017468E-04,4.975830E-04,4.934537E-04,4.893587E-04,4.852976E-04,4.812703E-04,
        4.772763E-04,4.733156E-04,4.693877E-04,4.654923E-04,4.616294E-04,4.577984E-04,4.539993E-04,4.502317E-04,4.464953E-04,4.427900E-04,4.391154E-04,4.354713E-04,4.318575E-04,4.282736E-04,4.247195E-04,4.211949E-04,4.176995E-04,4.142332E-04,4.107955E-04,4.073865E-04,
        4.040057E-04,4.006530E-04,3.973281E-04,3.940308E-04,3.907608E-04,3.875180E-04,3.843021E-04,3.811129E-04,3.779502E-04,3.748137E-04,3.717032E-04,3.686185E-04,3.655595E-04,3.625258E-04,3.595173E-04,3.565338E-04,3.535750E-04,3.506408E-04,3.477309E-04,3.448452E-04,
        3.419834E-04,3.391454E-04,3.363309E-04,3.335398E-04,3.307719E-04,3.280269E-04,3.253047E-04,3.226051E-04,3.199279E-04,3.172729E-04,3.146399E-04,3.120288E-04,3.094394E-04,3.068715E-04,3.043248E-04,3.017993E-04,2.992948E-04,2.968110E-04,2.943479E-04,2.919052E-04,
        2.894827E-04,2.870804E-04,2.846980E-04,2.823354E-04,2.799924E-04,2.776688E-04,2.753645E-04,2.730793E-04,2.708131E-04,2.685657E-04,2.663370E-04,2.641267E-04,2.619348E-04,2.597611E-04,2.576054E-04,2.554676E-04,2.533476E-04,2.512451E-04,2.491601E-04,2.470924E-04,
        2.450418E-04,2.430083E-04,2.409917E-04,2.389917E-04,2.370084E-04,2.350416E-04,2.330910E-04,2.311567E-04,2.292384E-04,2.273360E-04,2.254494E-04,2.235784E-04,2.217230E-04,2.198830E-04,2.180583E-04,2.162487E-04,2.144541E-04,2.126744E-04,2.109095E-04,2.091592E-04,
        2.074234E-04,2.057021E-04,2.039950E-04,2.023021E-04,2.006233E-04,1.989584E-04,1.973073E-04,1.956699E-04,1.940461E-04,1.924358E-04,1.908388E-04,1.892551E-04,1.876845E-04,1.861269E-04,1.845823E-04,1.830505E-04,1.815315E-04,1.800250E-04,1.785310E-04,1.770494E-04,
        1.755802E-04,1.741231E-04,1.726781E-04,1.712451E-04,1.698239E-04,1.684146E-04,1.670170E-04,1.656310E-04,1.642565E-04,1.628933E-04,1.615415E-04,1.602010E-04,1.588715E-04,1.575531E-04,1.562456E-04,1.549489E-04,1.536631E-04,1.523879E-04,1.511232E-04,1.498691E-04,
        1.486254E-04,1.473920E-04,1.461688E-04,1.449558E-04,1.437529E-04,1.425599E-04,1.413768E-04,1.402036E-04,1.390401E-04,1.378862E-04,1.367420E-04,1.356072E-04,1.344818E-04,1.333658E-04,1.322590E-04,1.311615E-04,1.300730E-04,1.289935E-04,1.279231E-04,1.268615E-04,
        1.258087E-04,1.247646E-04,1.237292E-04,1.227024E-04,1.216842E-04,1.206744E-04,1.196729E-04,1.186798E-04,1.176949E-04,1.167182E-04,1.157496E-04,1.147890E-04,1.138364E-04,1.128917E-04,1.119548E-04,1.110258E-04,1.101044E-04,1.091907E-04,1.082845E-04,1.073859E-04,
        1.064947E-04,1.056110E-04,1.047345E-04,1.038654E-04,1.030034E-04,1.021486E-04,1.013009E-04,1.004603E-04,9.962658E-05,9.879981E-05,9.797990E-05,9.716679E-05,9.636043E-05,9.556076E-05,9.476773E-05,9.398128E-05,9.320136E-05,9.242791E-05,9.166088E-05,9.090021E-05,
        9.014586E-05,8.939776E-05,8.865588E-05,8.792015E-05,8.719052E-05,8.646695E-05,8.574939E-05,8.503778E-05,8.433208E-05,8.363223E-05,8.293819E-05,8.224991E-05,8.156734E-05,8.089044E-05,8.021915E-05,7.955344E-05,7.889325E-05,7.823854E-05,7.758926E-05,7.694537E-05,
        7.630682E-05,7.567357E-05,7.504558E-05,7.442280E-05,7.380518E-05,7.319270E-05,7.258529E-05,7.198293E-05,7.138556E-05,7.079316E-05,7.020566E-05,6.962305E-05,6.904527E-05,6.847228E-05,6.790405E-05,6.734053E-05,6.678169E-05,6.622749E-05,6.567789E-05,6.513285E-05,
        6.459233E-05,6.405630E-05,6.352471E-05,6.299754E-05,6.247474E-05,6.195628E-05,6.144212E-05,6.093223E-05,6.042657E-05,5.992511E-05,5.942781E-05,5.893464E-05,5.844556E-05,5.796053E-05,5.747954E-05,5.700253E-05,5.652948E-05,5.606036E-05,5.559513E-05,5.513376E-05,
        5.467623E-05,5.422248E-05,5.377251E-05,5.332626E-05,5.288373E-05,5.244486E-05,5.200963E-05,5.157802E-05,5.114999E-05,5.072551E-05,5.030456E-05,4.988709E-05,4.947309E-05,4.906253E-05,4.865538E-05,4.825160E-05,4.785117E-05,4.745407E-05,4.706026E-05,4.666972E-05,
        4.628243E-05,4.589834E-05,4.551744E-05,4.513971E-05,4.476511E-05,4.439361E-05,4.402521E-05,4.365985E-05,4.329753E-05,4.293822E-05,4.258189E-05,4.222851E-05,4.187807E-05,4.153054E-05,4.118589E-05,4.084410E-05,4.050514E-05,4.016900E-05,3.983565E-05,3.950507E-05,
        3.917723E-05,3.885211E-05,3.852969E-05,3.820994E-05,3.789285E-05,3.757838E-05,3.726653E-05,3.695727E-05,3.665057E-05,3.634642E-05,3.604479E-05,3.574566E-05,3.544902E-05,3.515484E-05,3.486310E-05,3.457378E-05,3.428686E-05,3.400233E-05,3.372015E-05,3.344032E-05,
        3.316281E-05,3.288760E-05,3.261467E-05,3.234401E-05,3.207560E-05,3.180942E-05,3.154544E-05,3.128365E-05,3.102404E-05,3.076658E-05,3.051126E-05,3.025805E-05,3.000695E-05,2.975793E-05,2.951098E-05,2.926607E-05,2.902320E-05,2.878235E-05,2.854349E-05,2.830662E-05,
        2.807171E-05,2.783875E-05,2.760773E-05,2.737862E-05,2.715141E-05,2.692609E-05,2.670264E-05,2.648104E-05,2.626128E-05,2.604335E-05,2.582722E-05,2.561289E-05,2.540033E-05,2.518954E-05,2.498050E-05,2.477320E-05,2.456761E-05,2.436373E-05,2.416154E-05,2.396104E-05,
        2.376219E-05,2.356499E-05,2.336944E-05,2.317550E-05,2.298317E-05,2.279244E-05,2.260329E-05,2.241572E-05,2.222969E-05,2.204522E-05,2.186227E-05,2.168084E-05,2.150092E-05,2.132249E-05,2.114554E-05,2.097006E-05,2.079603E-05,2.062345E-05,2.045231E-05,2.028258E-05,
        2.011426E-05,1.994734E-05,1.978180E-05,1.961764E-05,1.945484E-05,1.929339E-05,1.913328E-05,1.897449E-05,1.881703E-05,1.866087E-05,1.850601E-05,1.835244E-05,1.820013E-05,1.804910E-05,1.789931E-05,1.775077E-05,1.760346E-05,1.745738E-05,1.731250E-05,1.716883E-05,
        1.702635E-05,1.688506E-05,1.674493E-05,1.660597E-05,1.646816E-05,1.633150E-05,1.619597E-05,1.606156E-05,1.592827E-05,1.579609E-05,1.566500E-05,1.553500E-05,1.540608E-05,1.527823E-05,1.515144E-05,1.502570E-05,1.490101E-05,1.477735E-05,1.465472E-05,1.453310E-05,
        1.441250E-05,1.429289E-05,1.417428E-05,1.405665E-05,1.394000E-05,1.382431E-05,1.370959E-05,1.359582E-05,1.348299E-05,1.337110E-05,1.326014E-05,1.315010E-05,1.304097E-05,1.293274E-05,1.282542E-05,1.271898E-05,1.261343E-05,1.250876E-05,1.240495E-05,1.230201E-05,
        1.219991E-05,1.209867E-05,1.199827E-05,1.189870E-05,1.179995E-05,1.170203E-05,1.160492E-05,1.150861E-05,1.141311E-05,1.131839E-05,1.122446E-05,1.113132E-05,1.103894E-05,1.094733E-05,1.085648E-05,1.076639E-05,1.067704E-05,1.058843E-05,1.050056E-05,1.041342E-05,
        1.032701E-05,1.024130E-05,1.015631E-05,1.007203E-05,9.988446E-06,9.905554E-06,9.823351E-06,9.741830E-06,9.660985E-06,9.580812E-06,9.501303E-06,9.422455E-06,9.344261E-06,9.266715E-06,9.189814E-06,9.113550E-06,9.037919E-06,8.962916E-06,8.888536E-06,8.814772E-06,
        8.741621E-06,8.669077E-06,8.597135E-06,8.525790E-06,8.455037E-06,8.384871E-06,8.315287E-06,8.246281E-06,8.177848E-06,8.109982E-06,8.042680E-06,7.975936E-06,7.909746E-06,7.844105E-06,7.779009E-06,7.714454E-06,7.650434E-06,7.586945E-06,7.523983E-06,7.461544E-06,
        7.399622E-06,7.338215E-06,7.277317E-06,7.216925E-06,7.157034E-06,7.097640E-06,7.038739E-06,6.980326E-06,6.922399E-06,6.864952E-06,6.807981E-06,6.751484E-06,6.695455E-06,6.639892E-06,6.584789E-06,6.530144E-06,6.475952E-06,6.422210E-06,6.368914E-06,6.316060E-06,
        6.263645E-06,6.211665E-06,6.160116E-06,6.108995E-06,6.058298E-06,6.008022E-06,5.958164E-06,5.908719E-06,5.859684E-06,5.811056E-06,5.762832E-06,5.715008E-06,5.667581E-06,5.620547E-06,5.573904E-06,5.527647E-06,5.481775E-06,5.436284E-06,5.391169E-06,5.346430E-06,
        5.302061E-06,5.258061E-06,5.214426E-06,5.171153E-06,5.128239E-06,5.085681E-06,5.043477E-06,4.918953E-06,4.797503E-06,4.679053E-06,4.563526E-06,4.450853E-06,4.340961E-06,4.233782E-06,4.129250E-06,4.000000E-06,3.927860E-06,3.830880E-06,3.736300E-06,3.644050E-06,
        3.554080E-06,3.466330E-06,3.380750E-06,3.300000E-06,3.217630E-06,3.137330E-06,3.059020E-06,2.983490E-06,2.909830E-06,2.837990E-06,2.767920E-06,2.720000E-06,2.659320E-06,2.600000E-06,2.550000E-06,2.485030E-06,2.421710E-06,2.382370E-06,2.360000E-06,2.300270E-06,
        2.242050E-06,2.185310E-06,2.130000E-06,2.100000E-06,2.059610E-06,2.020000E-06,1.974490E-06,1.930000E-06,1.884460E-06,1.855390E-06,1.840000E-06,1.797000E-06,1.755000E-06,1.711970E-06,1.670000E-06,1.629510E-06,1.590000E-06,1.544340E-06,1.500000E-06,1.475000E-06,
        1.440000E-06,1.404560E-06,1.370000E-06,1.337500E-06,1.300000E-06,1.267080E-06,1.235000E-06,1.202060E-06,1.170000E-06,1.150000E-06,1.123000E-06,1.110000E-06,1.097000E-06,1.080000E-06,1.071000E-06,1.045000E-06,1.035000E-06,1.020000E-06,9.960000E-07,9.860000E-07,
        9.720000E-07,9.500000E-07,9.300000E-07,9.100000E-07,8.764250E-07,8.600000E-07,8.500000E-07,8.194500E-07,7.900000E-07,7.800000E-07,7.415500E-07,7.050000E-07,6.825600E-07,6.531500E-07,6.250000E-07,5.952800E-07,5.669600E-07,5.400000E-07,5.315800E-07,5.196200E-07,
        5.000000E-07,4.850000E-07,4.670100E-07,4.496800E-07,4.330000E-07,4.139900E-07,4.000000E-07,3.910000E-07,3.699300E-07,3.500000E-07,3.346600E-07,3.200000E-07,3.145000E-07,3.000000E-07,2.800000E-07,2.635100E-07,2.480000E-07,2.335800E-07,2.200000E-07,2.091400E-07,
        1.988100E-07,1.890000E-07,1.800000E-07,1.697100E-07,1.600000E-07,1.530300E-07,1.463700E-07,1.400000E-07,1.340000E-07,1.150000E-07,1.000000E-07,9.500000E-08,8.000000E-08,7.700000E-08,6.700000E-08,5.800000E-08,5.000000E-08,4.200000E-08,3.500000E-08,3.000000E-08,
        2.500000E-08,2.000000E-08,1.500000E-08,1.000000E-08,6.900000E-09,5.000000E-09,3.000000E-09,1.000010E-11
        ]
        ebins = ebins[::-1]
        in_flux_lines = False
        for line in lines:
            if '# num ie flux r.err' in line:
                in_flux_lines = True
                continue
            if '0    0   0.0000E+00  0.0000' in line:
                in_flux_lines = False
                break
            if in_flux_lines:
                vals = line.split()
                ri = int(vals[0])-1
                ei = int(vals[1])-1
                fval = np.float(vals[2])
                ferr = np.float(vals[3])

                flux[ri,ei,0] = ebins[ei]
                flux[ri,ei,1] = ebins[ei+1]
                flux[ri,ei,2] = fval
                flux[ri,ei,3] = fval*ferr

    if return_metadata:
        return flux, dtrk_metadata
    else:
        return flux






def parse_tdeposit_file(path_to_tdeposit_file,return_metadata=False,return_samepage_data=False):
    '''
    Description:
        Parses the output file of a T-Deposit tally generated by PHITS.  This works for region, xyz, and tetrahedral mesh geometries.
        It has only been tested for output=deposit, axis=eng/x/y/z.  It is currently only designed for tallies tracking a single
        particle (or "all").  It can handle tallies with the `samepage` parameter used.

    Inputs:
        - `path_to_tdeposit_file` = path to the T-Deposit tally output file to be parsed
        - `return_metadata` = Boolean indicating whether additional information is outputted with the flux (D=`False`)

    Outputs:
        - `deposit` = a RxEx4 array containing regionwise T-Deposit tally output [Elower/Eupper/deposit/abs_error]
        - `deposit_metadata` (only returned if `return_metadata=True`) = list of length two
               - `deposit_metadata[0]` = string denoting axis type 'eng' (old full format) or 'dchain' (new reduced format)
               - `deposit_metadata[1]` = string denoting mesh type as either 'reg', 'xyz', or 'tet'
        - `samepage_data` (only returned if `return_samepage_data=True`) = list of length one
               - `samepage_data[0]` = list containing column header float values for regions/bins of PHITS samepage parameter
    '''

    # Extract text from file
    f = open(path_to_tdeposit_file)
    file_text = f.read()
    lines = file_text.split('\n')
    f.close()

    # Determine geometry type (mesh = reg, xyz, or tet)
    for line in lines:
        if 'mesh =' in line:
            meshtype = line.replace('mesh =','').strip().split()[0]
            break

    # Determine if original or reduced format (axis = eng or axis = dchain)
    for line in lines:
        if 'axis =' in line:
            axistype = line.replace('axis =','').strip().split()[0]
            break

    if axistype=='eng':
        a1ch_str = 'e'
    else:
        a1ch_str = axistype
    num_bins_str = 'n'+a1ch_str
    # Double check
    #for li, line in enumerate(lines):
    #    if li>500: break
    #    if '#  e-lower      e-upper      neutron     r.err ' in line:
    #        axistype='eng'
    #        break

    # Determine if samepage=1
    samepage=False
    col_values = []
    for li, line in enumerate(lines):
        if '-lower' in line and '-upper' in line and 'r.err' in line:
            if len(line.split())>5:
                samepage = True
                nreg = int((len(line.split())-3)/2)
                line_parts = [x for x in line.split()]
                for lpi, lp in enumerate(line_parts):
                    if lpi%2==0 or lpi==1: continue
                    col_values.append(float(lp))

    deposit_metadata = [axistype,meshtype]
    samepage_data = [col_values]

    # Determine number of regions
    if not samepage:
        nreg = file_text.count('#   no. =')

    search_str = num_bins_str+' ='
    for line in lines:
        if search_str in line:
            nEbins = int(line.replace(search_str,'').strip().split()[0])
            break

    deposit = np.zeros((nreg,nEbins,4))

    in_deposit_lines = False
    ei = 0
    ri = -1

    search_str = '#  '+a1ch_str+'-lower      '+a1ch_str+'-upper  '
    for line in lines:
        if '#   no. =' in line:
            ri += 1
        if search_str in line:
            in_deposit_lines = True
            continue
        if in_deposit_lines:
            if samepage:
                line_parts = [float(x) for x in line.split()]
                for regi in range(nreg):
                    deposit[regi, ei, 0] = line_parts[0]
                    deposit[regi, ei, 1] = line_parts[1]
                    deposit[regi, ei, 2] = line_parts[2+2*regi]
                    deposit[regi, ei, 3] = line_parts[3+2*regi]*deposit[regi, ei, 2]
                ei += 1
                if ei == nEbins:
                    in_deposit_lines = False
                    ei = 0
            else:
                deposit[ri,ei,:] = [float(x) for x in line.split()]
                deposit[ri,ei,3] = deposit[ri,ei,3]*deposit[ri,ei,2] # convert relative error to absolute error
                ei += 1
                if ei == nEbins:
                    in_deposit_lines = False
                    ei = 0

    if return_metadata and return_samepage_data:
        return deposit, deposit_metadata, samepage_data
    elif return_metadata:
        return deposit, deposit_metadata
    elif return_samepage_data:
        return deposit, samepage_data
    else:
        return deposit


def parse_dyld_files(path_to_dyld_file,iredufmt=None):
    '''
    Description:
        Parses the output files of a T-Yield tally generated by PHITS with axis=dchain.  This function assumes
        that the T-Yield tally was one automatically generated by and corresponding to a T-Dchain tally (axis=dchain).
        This works for region, xyz, and tetrahedral mesh geometries in either the original or reduced format.

    Inputs:
        - `path_to_dyld_file` = path to the T-Yield tally output file to be parsed
                           (the *_err.dyld file of the same name is automatically searched for and read, if present)
        - `iredufmt` = (DEPRICATED; this is now determined automatically)
                   integer 1 or 0 specifying how the xyz meshes are ordered relative to the internal region numbers.
                   In the new format (1), region indices are incremented as x->y->z (x=innermost loop); this is reversed in the old format (0).
                   Ultimately, this corresponds to the same iredufmt parameter in PHITS/DCHAIN, 1='new' and 0='old'.
                   This variable is only used for xyz meshes where this ordering matters.

    Outputs:
        - `yields` = a RxNx2 array containing regionwise yields (and their absolute uncertainties) for all nuclides produced in T-Yield
        - `nuclide_names_yld` = a length N list of all nuclide names in order
    '''

    def ZAM_to_Dname(ZAM):
        '''
        Description:
            Converts a ZZZAAAM number to a DCHAIN-formatted nuclide name

        Inputs:
            - `ZZZAAAM` = nuclide identification ineger, calculated as 10000\*Z + 10\*A + m

        Outputs:
            - `Dname` = nuclide identification string in DCHAIN format
        '''
        elms = ["n ",\
                "H ","He","Li","Be","B ","C ","N ","O ","F ","Ne",\
                "Na","Mg","Al","Si","P ","S ","Cl","Ar","K ","Ca",\
                "Sc","Ti","V ","Cr","Mn","Fe","Co","Ni","Cu","Zn",\
                "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y ","Zr",\
                "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",\
                "Sb","Te","I ","Xe","Cs","Ba","La","Ce","Pr","Nd",\
                "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",\
                "Lu","Hf","Ta","W ","Re","Os","Ir","Pt","Au","Hg",\
                "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",\
                "Pa","U ","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",\
                "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",\
                "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
        m = int(str(ZAM)[-1])
        A = int(str(ZAM)[-4:-1])
        Z = int(str(ZAM)[:-4])
        sym = elms[Z]
        A_str = '{:>3}'.format(A)
        m_str_list = [' ','m','n']
        m_str = m_str_list[m]
        Dname = sym + A_str + m_str
        return Dname

    # Extract text from file
    f = open(path_to_dyld_file)
    file_text = f.read()
    lines = file_text.split('\n')
    f.close()

    # determine if in reduced format
    iredufmt=0
    for li, line in enumerate(lines):
        if "# num nucleusID yield r.err" in line:
            iredufmt=1
            break
        if "isotope production #" in line:
            iredufmt=0
            break


    # Get error data if available
    if iredufmt==0:
        try:
            f_err = open(path_to_dyld_file.replace('.dyld','_err.dyld'))
            file_text_err = f_err.read()
            lines_err = file_text_err.split('\n')
            f_err.close()
            err_dyld_found = True
        except:
            file_text_err = None
            lines_err = None
            err_dyld_found = False

    # Determine geometry type (mesh = reg, xyz, or tet)
    for line in lines:
        if 'mesh =' in line:
            meshtype = line.replace('mesh =','').strip().split()[0]
            break

    # If xyz mesh, need to find mesh dimensions:
    if meshtype=='xyz':
        for line in lines:
            if 'nx =' in line:
                nx = int(line.replace('nx =','').strip().split()[0])
            elif 'ny =' in line:
                ny = int(line.replace('ny =','').strip().split()[0])
            elif 'nz =' in line:
                nz = int(line.replace('nz =','').strip().split()[0])
                break

    # Find starting line
    for li, line in enumerate(lines):
        if 'nuclear yield (or production)' in line:
            li_start = li
            break

    if iredufmt==1:
        # Count number of nuclides present in whole file
        nreg = 0
        nuc_id_list = []
        for li, line in enumerate(lines):
            if li <= li_start+3: continue # in header
            vals = line.strip().split()
            if int(vals[0])==0: break # reached end
            if int(vals[0])>nreg: nreg = int(vals[0])
            zzzaaam = int(vals[1])
            if zzzaaam not in nuc_id_list: nuc_id_list.append(zzzaaam)

        nnuc = len(nuc_id_list)
        yields = np.zeros((nreg,nnuc,2))
        nuclide_names_yld = []

        # Get names
        nuc_id_list = sorted(nuc_id_list)
        for id in nuc_id_list:
            nuclide_names_yld.append(ZAM_to_Dname(id))

        # Get values
        for li, line in enumerate(lines):
            if li <= li_start+3: continue # in header
            vals = line.strip().split()
            if int(vals[0])==0: break # reached end
            ri = int(vals[0]) - 1
            zzzaaam = int(vals[1])
            ni = nuc_id_list.index(zzzaaam)
            yields[ri,ni,0] = np.float(vals[2])
            yields[ri,ni,1] = np.float(vals[3])*np.float(vals[2])

    else: # old ''traditional'' format
        # Count number of nuclides present in whole file
        nnuc = 0
        for li, line in enumerate(lines):
            if li <= li_start+2: continue # skip header lines
            if 'isotope production' in line:
                N_bounds = line.strip().split('=')[-1].split()
                N_bounds = [int(i) for i in N_bounds]
                nnuc += N_bounds[1] - N_bounds[0] + 1

        # Determine number of regions
        nreg = 0
        for li, line in enumerate(lines):
            if li <= li_start+4: continue # skip header lines
            if len(line) < 2: break # reached end of first element block
            nreg += 1

        yields = np.zeros((nreg,nnuc,2))
        nuclide_names_yld = []

        # Extract yield data
        ni = 0 # nuclide index
        ni_newstart = 0
        ri = 0 # region index
        for li, line in enumerate(lines):
            if li <= li_start+2: continue # skip header lines
            if len(line) < 2: continue # skip line breaks

            if 'isotope production' in line:
                # extract Z and A info
                Z = int(line.strip().split('-')[0])
                N_bounds = line.strip().split('=')[-1].split()
                N_bounds = [int(i) for i in N_bounds]
                N_list = []
                for i in range(N_bounds[1]-N_bounds[0]+1):
                    N_list.append(N_bounds[0]+i)
                nisotopes = len(N_list)
                A_list = [N+Z for N in N_list]
                ni_newstart = len(nuclide_names_yld)
                for A in A_list:
                    ZAM = 10*A + 10000*Z
                    nuclide_names_yld.append(ZAM_to_Dname(ZAM))
                on_buffer_line = True
                continue

            if on_buffer_line:
                ri = 0
                on_buffer_line = False
                continue

            if '# Information for Restart Calculation' in line: break # reached end of useful info

            # Only lines making it to this point will be ones with region and yield data
            vals = line.strip().split()
            if meshtype=='xyz':
                yvals = vals[3:]
                if err_dyld_found: yvals_rerr = lines_err[li].strip().split()[3:]
                jx,jy,jz = int(vals[0]),int(vals[1]),int(vals[2])
                rii = jz + (jy-1)*nz + (jx-1)*(nz*ny)
                #if iredufmt==1:
                #    rii = jx + (jy-1)*nx + (jz-1)*(nx*ny)
                #else:
                #    rii = jz + (jy-1)*nz + (jx-1)*(nz*ny)
            else:
                yvals = vals[1:]
                if err_dyld_found: yvals_rerr = lines_err[li].split()[1:]
                rii = ri

            for i in range(nisotopes):
                yields[rii,ni_newstart+i,0] = np.float(yvals[i])
                if err_dyld_found: yields[rii,ni_newstart+i,1] = np.float(yvals_rerr[i])*yields[rii,ni_newstart+i,0]

            ri += 1

    return yields, nuclide_names_yld





'''
**************************************************************************************************
----------------------------------- PLOTTING-RELATED FUNCTIONS -----------------------------------
**************************************************************************************************
'''


def generate_line_bar_coordinates(xbins,yvals,yerrs=[]):
    """
    Description:
        Converts a set of bin boundaries and bin contents to coordinates mapping a bar plot if drawn with a line

    Inputs:
      - `xbins` = list of length N+1 bin boundary values
      - `yvals` = list of length N bin content values
      - `yerrs` = (optional) list of length N absolute uncertainties of bin content values

    Outputs:
      - `newx` = list of length 2N + 2 of x-coordinates mapping a 'bar plot' of the input histogram data
      - `newy` = list of length 2N + 2 of y-coordinates mapping a 'bar plot' of the input histogram data
      - `newyerr` = (optional) list of length 2N + 2 of y-coordinates mapping a 'bar plot' of the input histogram data
    """
    if len(yvals) != (len(xbins)-1):
        pstr = 'xbins should be a list of bin edges of length one more than yvals, the values associated with the contents of each bin' + '\n'
        pstr += 'provided input arrays had lengths of {} for xbins and {} for yvals'.format(str(len(xbins)),str(len(yvals)))
        print(pstr)
        return 0
    newx = [xbins[0],xbins[0]]
    newy = [0,yvals[0]]
    if len(yerrs)!=0: newyerr = [0,yvals[0]]
    for i in range(len(xbins)-2):
        newx.append(xbins[i+1])
        newx.append(xbins[i+1])
        newy.append(yvals[i])
        newy.append(yvals[i+1])
        if len(yerrs)!=0:
            newyerr.append(yerrs[i])
            newyerr.append(yerrs[i+1])
    newx.append(xbins[-1])
    newx.append(xbins[-1])
    newy.append(yvals[-1])
    newy.append(0)
    if len(yerrs)!=0:
        newyerr.append(yerrs[-1])
        newyerr.append(0)
        return newx, newy, newyerr
    else:
        return newx, newy

def colors_list_6(di):
    '''
    Colorbrewer qualitative color cycle scheme 6 (modified)
    See: https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=6
    '''
    #colors_list = ['b','g','r','c','m','y'] # Python 3 old default
    #colors_list = ['#b2182b','#d6604d','#f4a582','#92c5de','#4393c3','#2166ac'] # blue to red cold
    #colors_list = ['#d73027','#f46d43','#fdae61','#abd9e9','#74add1','#4575b4'] # blue to red warm
    #colors_list = ['#762a83','#9970ab','#c2a5cf','#a6dba0','#5aae61','#1b7837'] # purple to green
    #colors_list = ['#40004b','#762a83','#9970ab','#5aae61','#1b7837','#00441b'] # purple to green darker
    #colors_list = ["#afa83a","#7f63b8","#56ae6c","#b84c7d","#ac863f","#b94d3d"] # iWantHue 1
    #colors_list = ['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02'] # qualitative dark 1
    colors_list = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#a65628'] # qualitative dark 2
    return colors_list[di%6]

def colors_list_12(di):
    '''
    Colorbrewer qualitative color cycle scheme 6 (expanded)
    See: https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=6
    '''
    colors_list = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#a65628','#8dd3c7','#bebada','#fb8072','#80b1d3','#fdb462','#b3de69']
    return colors_list[di%12]

def colors_list_10(di):
    '''
    Default cycle as of matplotlib v3.1.1
    See: https://matplotlib.org/3.1.1/users/dflt_style_changes.html
    '''
    colors_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    return colors_list[di%10]

def colors_list_20(di):
    '''
    List of 20 'distinct' colors
    See: https://sashamaps.net/docs/resources/20-colors/
    '''
    colors_list = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4', '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9']
    return colors_list[di%20]

def colors_list_64(di):
    '''
    List of 64 'distinct' colors
    See: https://stackoverflow.com/a/20298027
    '''
    colors_list = ['#00FF00','#0000FF','#FF0000','#01FFFE','#FFA6FE','#FFDB66','#006401','#010067','#95003A','#007DB5','#FF00F6','#FFEEE8','#774D00','#90FB92','#0076FF','#D5FF00','#FF937E','#6A826C','#FF029D','#FE8900','#7A4782','#7E2DD2','#85A900','#FF0056','#A42400','#00AE7E','#683D3B','#BDC6FF','#263400','#BDD393','#00B917','#9E008E','#001544','#C28C9F','#FF74A3','#01D0FF','#004754','#E56FFE','#788231','#0E4CA1','#91D0CB','#BE9970','#968AE8','#BB8800','#43002C','#DEFF74','#00FFC6','#FFE502','#620E00','#008F9C','#98FF52','#7544B1','#B500FF','#00FF78','#FF6E41','#005F39','#6B6882','#5FAD4E','#A75740','#A5FFD2','#FFB167','#009BFF','#E85EBE','#000000']
    return colors_list[di%64]

def get_colormap(cmap_str):
    '''
    Description:
        Retrieve a matplotlib colormap using just its string name
        See available colormaps: https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html

    Dependencies:
      - `from matplotlib import cm`

    Inputs:
      - `cmap_str` = string of name of colormap

    Outputs:
      - callable colormap object which can be provided to plotting functions or evaluated for any value from 0 to 1
    '''
    return cm.get_cmap(cmap_str)

def truncate_colormap(cmap, min_val=0.0, max_val=1.0, n=100):
    '''
    Description:
        Truncate a colormap object's bounds to a subset of the original colormap, renormalizing new bounds to [0,1].
        For instance, the upper and lower 20% of a colormap could be removed with `cmap=truncate_colormap(cmap, min_val=0.2, max_val=0.8)`.

    Dependencies:
      - `from matplotlib.colors import LinearSegmentedColormap`
      - `import numpy as np`

    Inputs:
      - `cmap` = callable colormap object or string of matplotlib colormap name to be truncated and rescaled
      - `min_val` = float specifying new lower bound of cmap in [0,1) (D=`0.0`)
      - `max_val` = float specifying new upper bound of cmap in (0,1] (D=`1.0`)
      - `n` = integer specifying number of bins cmap will be subdivided into (D=`100`); note that nearest neighbor
              linear interpolation will be used when providing values to and evaluating the new colormap.
              Higher values of `n` just correspond to a higher-quality and more accurate interpolation.

    Outputs:
      - callable colormap object which can be provided to plotting functions or evaluated for any value from 0 to 1
    '''
    if isinstance(cmap,str): cmap = get_colormap(cmap)
    new_cmap = LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=min_val, b=max_val),
        cmap(np.linspace(min_val, max_val, n)))
    return new_cmap


def add_colorbar_onto_plot(fig, colormap, cm_val_min, cm_val_max, boundaries=None, orientation='horizontal',
                           location_from_left=0.25, location_from_bottom=0.80, width=0.5, height=0.05,
                           label_text='colorbar', label_fontsize=14, spacing='proportional', drawedges=False,
                           extend='neither', extendfrac=None, extendrect=False, ticks=None, tick_format=None
                           ):
    '''
    Description:
        Overlay a colorbar on top of an existing figure, such as one made by `fancy_plot()`.  Note that this is more for
        "hacking in" a color bar with your own specified values and boundaries that is overlaid on top of the plot area.
        For a more "proper" colorbar figure, please see the `fancy_3D_plot()` function.

    Inputs:
       (required)

      - `fig` = pyplot figure (same as the output `fig` of `fancy_plot()`)
      - `colormap` = callable colormap object which can be evaluated for any value from 0 to 1, such as is outputted from
            the `get_colormap()` and `truncate_colormap()` functions.
      - `cm_val_min` = the minimum value (`float`) represented by color on the color bar
      - `cm_val_max` = the maximum value (`float`) represented by color on the color bar

    Inputs:
       (optional)

      - `boundaries` = if desired, provide a list of numbers to be used as the discrete color "bins" on the color bar (D=`None`)
      - `orientation` = specify orientation of the colorbar as `'horizontal'` or `'vertical'` (D=`'horizontal'`)
      - `location_from_left` = horizontal location of colorbar on the `fig`, specified as the fraction of the `fig` width from the left edge (D=`0.25`)
      - `location_from_bottom` = vertical location of colorbar on the `fig`, specified as the fraction of the `fig` height from the bottom edge (D=`0.80`)
      - `width` = width of colorbar as a fraction of the width of `fig` (D=`0.25`)
      - `height` = height of colorbar as a fraction of the height of `fig` (D=`0.25`)
      - `label_text` = label for the colorbar (D=`'colorbar'`)
      - `label_fontsize` = font size of the label text (D=`14`)
      - `extend` = Select one: {`'neither'`, `'both'`, `'min'`, `'max'`} (D=`'neither'`) Make pointed end(s) for out-of-range values
             (unless 'neither'). These are set for a given colormap using the colormap set_under and set_over methods.
      - `extendfrac` = If set to `None`, both the minimum and maximum triangular colorbar extensions will have a length of 5% of the interior colorbar length (this is the default setting).
             If set to 'auto', makes the triangular colorbar extensions the same lengths as the interior boxes (when spacing is set to `'uniform'`) or the same lengths as the respective adjacent interior boxes (when spacing is set to `'proportional'`).
             If a scalar, indicates the length of both the minimum and maximum triangular colorbar extensions as a fraction of the interior colorbar length. A two-element sequence of fractions may also be given, indicating the lengths of the minimum and maximum colorbar extensions respectively as a fraction of the interior colorbar length.
      - `extendrect` = A Boolean, if `False` the minimum and maximum colorbar extensions will be triangular (the default). If `True` the extensions will be rectangular.(D=`False`)
      - `spacing` = Select one: {'uniform', 'proportional'} (D=`'proportional'`) For discrete colorbars (BoundaryNorm or contours), `'uniform'` gives each color the same space; `'proportional'` makes the space proportional to the data interval.
      - `ticks` = (D=`None`) If `None`, ticks are determined automatically from the input; otherwise, provide a list of ticks or Locator
      - `tick_format` = (D=`None`) If `None`, ScalarFormatter is used. Format strings, e.g., `"%4.2e"` or `"{x:.2e}"`, are supported. An alternative Formatter may be given instead.
      - `drawedges` = A Boolean (D=`False`) specifying whether to draw lines at color boundaries.

    Outputs:
      - `cax` = colorbar axes
      - `cbar` = colorbar object

    '''
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html
    cax = fig.add_axes([location_from_left, location_from_bottom, width, height])  # left, bottom, width, height
    sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=cm_val_min, vmax=cm_val_max))
    sm._A = []
    cbar = plt.colorbar(sm, cax=cax, boundaries=boundaries, orientation=orientation, spacing=spacing,
                        extend=extend, extendfrac=extendfrac, extendrect=extendrect,
                        ticks=ticks, format=tick_format, drawedges=drawedges
                        )  #
    cbar.set_label(label=label_text, size=label_fontsize)  # weight='bold')
    return cax, cbar




def makeErrorBoxes(ax,xdata,ydata,xerror,yerror,fc='None',ec='k',alpha=1.0,lw=0.5):
    '''
    Description:
        Generate uncertainty/error "boxes" which are overlaid on points

    Dependencies:
      - `import numpy as np`
      - `import matplotlib.pyplot as plt`
      - `from matplotlib.collections import PatchCollection`
      - `from matplotlib.patches import Rectangle`

    Inputs:
       (required)

      - `ax` = axis handles onto which error boxes will be drawn
      - `xdata` = a list/array of x data
      - `ydata` = a list/array of y data
      - `xerror` = a list/array of 2 lists/arrays of x absolute uncertainties as [x_lower_errors, x_upper_errors]
      - `yerror` = a list/array of 2 lists/arrays of y absolute uncertainties as [y_lower_errors, y_upper_errors]

    Inputs:
       (optional)

      - `fc` = face color of boxes (D=`None`)
      - `ec` = edge color of boxes (D=`'k'`, black)
      - `alpha` = opacity of box filling (D=`1.0`)
      - `lw` = line width of box edge (D=`0.5`)

    Notes:
        For best results, repeat this function twice, first rendering the edges and then a second time for the filling as shown below:
        makeErrorBoxes(xdata,ydata,xerrbox,yerrbox,fc='None',ec=nx_color,alpha=1.0,lw=0.5)
        makeErrorBoxes(xdata,ydata,xerrbox,yerrbox,fc=nx_color,ec='None',alpha=0.1,lw=0.5)
    '''
    xdata,ydata,xerror,yerror = np.array(xdata),np.array(ydata),np.array(xerror),np.array(yerror)
    # Create list for all the error patches
    errorboxes = []

    # Loop over data points; create box from errors at each point
    for xc,yc,xe,ye in zip(xdata,ydata,xerror.T,yerror.T):
        rect = Rectangle((xc-xe[0],yc-ye[0]),xe.sum(),ye.sum())
        errorboxes.append(rect)

    # Create patch collection with specified colour/alpha
    pc = PatchCollection(errorboxes,facecolor=fc,alpha=alpha,edgecolor=ec,linewidth=lw)

    # Add collection to axes
    ax.add_collection(pc)

def fancy_plot(
               # Required data
               xdata_lists,ydata_lists,

               # Dictionaries
               dictionaries=None,

               # Optional data
               data_labels=[],  xerr_lists=[[]],  yerr_lists=[[]],
               # Standard basic settings (optional)
               figi=1, title_str='title',  x_label_str='x-axis',  y_label_str='y-axis',
               x_limits=[],  y_limits=[],  x_scale='log',  y_scale='log',  color='#FDFEFC', alpha=1.0,
               linestyle='', linewidth=1,
               marker='.', markersize=5, markerfacecolor=None, markeredgecolor=None, markeredgewidth=None,
               errorstyle='bar-band', error_band_opacity=0.15,
               elinewidth=None, capsize=None,
               fig_width_inch=9.5,  fig_height_inch=6.5, title_fs=16,  axis_fs=14,
               f_family='sans-serif',f_style='normal',f_variant='normal',f_weight='normal',

               # Advanced settings (optional)
               # Legend settings
               legend_position='outside right', legend_anchor=None, legend_ncol=1, legend_alpha=None, legend_columnspacing=None,
               # Errorbar settings
               errorbox_xdata_l=[[]], errorbox_xdata_r=[[]], errorbox_ydata_l=[[]], errorbox_ydata_u=[[]],
               errorbox_fc='k', errorbox_fa=0.1, errorbox_ec='k', errorbox_ea=1.0, errorbox_ew=0.5,
               # Subplot settings
               fig=None, ax=None, spnrows=1, spncols=1, spindex=1,
               man_sp_placement = False, spx0=0.1, spy0=0.1, sph0=0.4, spw0=0.4
               ):
    '''
    Description:
        Function which makes very customizable and beautiful plots.  It is intended to be used when plotting multiple datasets at once with a legend but can also handle individual datasets

    Dependencies:
      - `import numpy as np`
      - `import matplotlib.pyplot as plt`

    Inputs:
      (Required)

      - `xdata_lists` = a list containing lists/arrays of x data (or single list of xdata applied to all ydata in y_data_lists)
      - `ydata_lists` = a list containing lists/arrays of y data (or single list of ydata)

      OR

      - `dictionaries` (see below)

    Dictionaries:
      - `dictionaries` = a list containing dictionary objects for each dataset to be plotted (or single dictionary object).

            This provides an alternate way of providing this function with data to be plotted.  If wanting to use exclusively dictionaries,
            set `xdata_lists=None` and `ydata_lists=None`; otherwise, the two modes may be used together.
            The dictionaries are converted to the "standard" list of lists/strings/etc format native to this function.
            Below are listed the input keywords for these dictionaries; where not the same as the normal variables for this function,
            the equivalent name is provided in parentheses.

            - Required: `'xdata'` (xdata_lists), `'ydata'` (ydata_lists)
            - Optional (basic): `'data_label'` (data_labels), `'xerr'` (xerr_lists), `'yerr'` (yerr_lists),
                        `'color'`, `'alpha'`, `'linestyle'`, `'linewidth'`, `'marker'`, `'markersize'`,
                        `'markerfacecolor'`, `'markeredgecolor'`, `'markeredgewidth'`,
                        `'errorstyle'`, `'error_band_opacity'`, `'elinewidth'`, `'capsize'`
            - Optional (advanced): `'errorbox_xdata_l'`, `'errorbox_xdata_r'`, `'errorbox_ydata_l'`, `'errorbox_ydata_u'`,
                        `'errorbox_fc'`, `'errorbox_fa'`, `'errorbox_ec'`, `'errorbox_ea'`, `'errorbox_ew'`

            For any entry omitted from a dictionary, the value provided to the function is checked first; otherwise the default value is assumed.
            For example, for entries missing the `'color'` keyword, the value provided to the color variable is used.  If it has not been changed from
            its default value, then the default behavior is used.

    Inputs:
       (Optional, basic)

      - `data_labels` = a list of strings to be used as data labels in the legend (D=`[]`, no legend generated)
      - `xerr_lists` = a list containing lists/arrays of x data absolute uncertainties (or single list of xdata errors applied to all ydata in y_data_lists) (D=`[[]]`, No error)
      - `yerr_lists` = a list containing lists/arrays of y data absolute uncertainties (or single list of ydata errors) (D=`[[]]`, No error)
      - `figi` = figure index (D=`1`)
      - `title_str` = string to be used as the title of the plot (D=`'title'`)
      - `x_label_str` = string to be used as x-axis title (D=`'x-axis'`)
      - `y_label_str` = string to be used as y-axis title (D=`'y-axis'`)
      - `x_limits` = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=auto-calculated based on x_data_lists)
      - `y_limits` = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=auto-calculated based on y_data_lists)
      - `x_scale` = x-axis scale, either `"linear"`, `"log"`, `"symlog"`, or `"logit"`
      - `y_scale` = y-axis scale, either `"linear"`, `"log"`, `"symlog"`, or `"logit"`
      - `color` = list of color strings to be used of same length as y_data_lists (or individual color string) (D=Matplotlib default color cycle)
      - `alpha` = list of (or individual) alpha values (D=`1.0`)
      - `linestyle` = list of (or individual) strings denoting linestyle: `''`, `'-'`, `'--'`, `'-.'`, or `':'` (D=`''`)
      - `linewidth` = list of (or individual) int/float of the width of line (D=`1`)
      - `marker` = list of (or individual) marker styles (D=`'.'`) For all options, see: https://matplotlib.org/3.1.0/api/markers_api.html
      - `markersize` = list of (or individual) int/float of marker size (D=`5`)
      - `markerfacecolor` = list of (or individual) marker face colors (D=`None`, use value of `'color'`)
      - `markeredgecolor` = list of (or individual) marker edge colors (D=`None`, use value of `'color'`)
      - `markeredgewidth` = list of (or individual) int/float of marker edge widths (D=`None`)
      - `errorstyle` = list of (or individual) strings specifying how y-error is represented (D=`'bar-band'`, `['bar-band','bar','band']`)
      - `error_band_opacity` = list of (or individual) int/float of error band opacities (D=`0.15`)
      - `elinewidth` = list of (or individual) int/float  line width of error bar lines (D=`None`, use current `linewidth`)
      - `capsize` = list of (or individual) int/float of length of the error bar caps in points (D=`None`)
      - `fig_width_inch` = figure width in inches (D=`9.5`)
      - `fig_height_inch` = figure height in inches (D=`6.5`)
      - `title_fs` = title font size (D=`16`)
      - `axis_fs` = axis label font size (D=`14`)
      - `f_family` = string specifying font family (D=`'sans-serif'`); options include: `['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']`
      - `f_style` = string specifying font style (D=`'normal'`); options include: `['normal', 'italic', 'oblique']`
      - `f_variant` = string specifying font variant (D=`'normal'`); options include: `['normal', 'small-caps']`
      - `f_weight` = string specifying font weight (D=`'normal'`); options include: `['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']`


    Inputs:
       (Optional, advanced)

       Legend settings

      - `legend_position` = one of the default matplotlib legend position strings (`'best'`,`'upper right'`,`'lower center'`,`'lower left'`,etc.) to place the legend inside the plot or
                        `'outside right'` or `'outside bottom'` to place the legend outside of the plot area (D=`'outside right'`, if legend is to be used)
      - `legend_anchor` = legend anchor position (x=left-right position, y=bottom-top position) only used when legend position is set to one of the "outside" options
                        (D=`None` which becomes `(1.0,0.75)` if position is `'outside right'` or `(0.5,-0.17)` if position is `'outside bottom'`)
                        Note that only one coordinate usually should be adjusted.  If using an `'outside right'` legend, only the y-coordinate needs to be manipulated
                        to scoot the legend up/down.  Likewise, for `'outside bottom'` legends only the x-coordinate needs adjusting for tuning left/right position
      - `legend_ncol` = number of columns in legend (D=`1` in all cases except for legend_position=`'outside bottom'` where D=`len(ydata_lists)`)
      - `legend_alpha` = alpha of legend background (D=`None`, auto determined by matplotlib)
      - `legend_columnspacing` = column spacing of legend (D=`None`, auto determined by matplotlib)

       Error boxes (can be used in addition to or in lieu of normal error bars)

      - `errorbox_xdata_l` = a list containing lists/arrays of errorbox left widths from center (x-data lower error)
      - `errorbox_xdata_r` = a list containing lists/arrays of errorbox right widths from center (x-data upper error)
      - `errorbox_ydata_l` = a list containing lists/arrays of errorbox lower heights from center (y-data lower error)
      - `errorbox_ydata_u` = a list containing lists/arrays of errorbox upper heights from center (y-data upper error)

          *Error boxes will only be drawn if at least one x list and one y list of the four above arrays is specified; unspecified lists will default to zero error.*

      - `errorbox_fc` = list of (or individual) error box face color (D=`'k'`, black)
      - `errorbox_fa` = list of (or individual) error box face alpha (D=`0.1`)
      - `errorbox_ec` = list of (or individual) error box edge color (D=`'k'`, black)
      - `errorbox_ea` = list of (or individual) error box edge alpha (D=`1.0`)
      - `errorbox_ew` = list of (or individual) error box edge width (D=`0.5`)

       Subplots

      - `fig` = figure handles from existing figure to draw on (D=`None`, `fig=None` should always be used for initial subplot unless a figure canvas has already been generated)
      - `ax` = axis handles from an existing figure to draw on (D=`None`, `ax=None` should always be used for initial subplot)
      - `spnrows` = number of rows in final subplot (D=`1`)
      - `spncols` = number of columns in final subplot (D=`1`)
      - `spindex` = index of current subplot (between 1 and spnrows*spncols) (D=`1`)
      - `man_sp_placement` = logical variable controlling manual sizing/placement of subplots using below variables (D=`False`, use automatic sizing)
      - `spx0` = distance from canvas left edge where this plotting area should begin (D=`0.1`), generally a number around 0~1
      - `spy0` = distance from canvas bottom edge where this plotting area should begin (D=`0.1`), generally a number around 0~1
      - `spw0` = width of this plotting area on the canvas (D=`0.4`), generally a number around 0~1
      - `sph0` = height of this plotting area on the canvas (D=`0.4`), generally a number around 0~1

    Outputs:
      - `fig` = pyplot figure
      - `ax`  = pyplot figure plot/subplot axes handles
    '''
    include_legend = True # used to toggle legend on/off
    single_dataset = False # Assume multiple datasets entered, but this can be tested to see if it is the case or not.

    # At the very start, check for dictionaries
    if dictionaries != None:
        # determine if single entry or list of entries
        if isinstance(dictionaries, dict):
            dictionaries = [dictionaries]
        num_dict = len(dictionaries)

        dxdata_lists = []
        dydata_lists = []
        ddata_labels = []
        dxerr_lists  = []
        dyerr_lists  = []

        dcolor, dalpha, dlinestyle, dlinewidth, dmarker, dmarkersize, dmarkerfacecolor, dmarkeredgecolor, dmarkeredgewidth = [], [], [], [], [], [], [], [], []
        derrorstyle, derror_band_opacity, delinewidth, dcapsize = [], [], [], []
        derrorbox_xdata_l, derrorbox_xdata_r, derrorbox_ydata_l, derrorbox_ydata_u = [], [], [], []
        derrorbox_fc, derrorbox_fa, derrorbox_ec, derrorbox_ea, derrorbox_ew = [], [], [], [], []

        keylist = ['xdata','xdata_lists','ydata','ydata_lists','data_label','data_labels','xerr','xerr_lists','yerr','yerr_lists',
                   'color','alpha', 'linestyle', 'linewidth', 'marker', 'markersize', 'markerfacecolor', 'markeredgecolor','markeredgewidth',
                    'errorstyle', 'error_band_opacity', 'elinewidth, capsize',
                    'errorbox_xdata_l', 'errorbox_xdata_r', 'errorbox_ydata_l', 'errorbox_ydata_u',
                    'errorbox_fc', 'errorbox_fa', 'errorbox_ec', 'errorbox_ea', 'errorbox_ew']

        settings_realvars=[color   ,  alpha,  linestyle,  linewidth,  marker,  markersize,  markerfacecolor,  markeredgecolor,  markeredgewidth,  errorstyle,  error_band_opacity,  elinewidth,  capsize,  errorbox_xdata_l,  errorbox_xdata_r,  errorbox_ydata_l,  errorbox_ydata_u,  errorbox_fc,  errorbox_fa,  errorbox_ec,  errorbox_ea,  errorbox_ew]
        settings_keys  = ['color'  ,'alpha','linestyle','linewidth','marker','markersize','markerfacecolor','markeredgecolor','markeredgewidth','errorstyle','error_band_opacity','elinewidth','capsize','errorbox_xdata_l','errorbox_xdata_r','errorbox_ydata_l','errorbox_ydata_u','errorbox_fc','errorbox_fa','errorbox_ec','errorbox_ea','errorbox_ew']
        settings_vars  = [dcolor   , dalpha, dlinestyle, dlinewidth, dmarker, dmarkersize, dmarkerfacecolor, dmarkeredgecolor, dmarkeredgewidth, derrorstyle, derror_band_opacity, delinewidth, dcapsize, derrorbox_xdata_l, derrorbox_xdata_r, derrorbox_ydata_l, derrorbox_ydata_u, derrorbox_fc, derrorbox_fa, derrorbox_ec, derrorbox_ea, derrorbox_ew]
        settings_defalts=['#FDFEFC', 1.0   , ''        , 1         , '.'    , 5          , None            , None            , None            , 'bar-band' , 0.15               , None       , None    , []               , []               , []               , []               , 'k'         , 0.1         , 'k'         , 1.0         , 0.5         ]

        for i in range(num_dict):
            d = dictionaries[i]
            if not isinstance(d, dict):
                print('Index {} of dictionaries list is not a dictionary! Quitting...'.format(i))
                return None

            # Check for any unrecognizable keys
            dkeys = list(d.keys())
            for dkey in dkeys:
                if dkey not in keylist:
                    print('Encountered unknown keyword {} in dictionary entry at index {}.  Ignoring it...'.format(dkey,i))

            # Check for each key that will be used
            if 'xdata' in d:
                dxdata_lists.append(d['xdata'])
            elif 'xdata_lists' in d:
                dxdata_lists.append(d['xdata_lists'])
            else:
                print('Dictionary at index {} is missing xdata.  Quitting...'.format(i))
                return None

            if 'ydata' in d:
                dydata_lists.append(d['ydata'])
            elif 'ydata_lists' in d:
                dydata_lists.append(d['ydata_lists'])
            else:
                print('Dictionary at index {} is missing ydata.  Quitting...'.format(i))
                return None

            if 'data_label' in d:
                ddata_labels.append(d['data_label'])
            elif 'data_labels' in d:
                ddata_labels.append(d['data_labels'])
            else:
                ddata_labels.append(None)

            if 'xerr' in d:
                dxerr_lists.append(d['xerr'])
            elif 'xerr_lists' in d:
                dxerr_lists.append(d['xerr_lists'])
            else:
                dxerr_lists.append([])

            if 'yerr' in d:
                dyerr_lists.append(d['yerr'])
            elif 'yerr_lists' in d:
                dyerr_lists.append(d['yerr_lists'])
            else:
                dyerr_lists.append([])

            for ski in range(len(settings_keys)):
                if settings_keys[ski] in d:
                    settings_vars[ski].append(d[settings_keys[ski]])
                elif not isinstance(settings_realvars[ski],(list,np.ndarray)): # if main entry is not a list, use it instead of default value
                    settings_vars[ski].append(settings_realvars[ski])
                else:
                    settings_vars[ski].append(settings_defalts[ski])

        # Now combine with data entered normally, if applicable
        if xdata_lists != None and ydata_lists != None:
            # combine
            if not isinstance(xdata_lists[0],(list,np.ndarray)):
                xdata_lists = [xdata_lists]
            xdata_lists = xdata_lists + dxdata_lists

            if not isinstance(ydata_lists[0],(list,np.ndarray)):
                ydata_lists = [ydata_lists]
            num_normal_datasets = len(ydata_lists)
            num_dict_datasets = len(dydata_lists)
            ydata_lists = ydata_lists + dydata_lists

            if data_labels==[]:
                if not all(x==None for x in ddata_labels):
                    data_labels = num_normal_datasets*[None] + ddata_labels
            else:
                data_labels = data_labels + ddata_labels

            if xerr_lists == [[]]:
                if not all(x==[] for x in dxerr_lists):
                    xerr_lists = num_normal_datasets*[[]] + dxerr_lists
            else:
                xerr_lists = xerr_lists + dxerr_lists

            if yerr_lists == [[]]:
                if not all(x==[] for x in dyerr_lists):
                    yerr_lists = num_normal_datasets*[[]] + dyerr_lists
            else:
                yerr_lists = yerr_lists + dyerr_lists

            for ski in range(len(settings_keys)):
                if settings_keys[ski] in ['errorbox_xdata_l','errorbox_xdata_r','errorbox_ydata_l','errorbox_ydata_u']:
                    # the special exceptions which can be lists
                    if settings_realvars[ski] == [[]]:
                        if not all(x==[] for x in settings_vars[ski]):
                            settings_realvars[ski] = num_normal_datasets*[[]] + settings_vars[ski]
                    else:
                        settings_realvars[ski] = settings_realvars[ski] + settings_vars[ski]
                else:
                    # for each possible setting option which could be a single value or list
                    if not isinstance(settings_realvars[ski],(list,np.ndarray)): # if main entry isn't a list
                        if not all(x==settings_realvars[ski] for x in settings_vars[ski]): # if not all dict entries are same as main entry
                            settings_realvars[ski] = num_normal_datasets*[settings_realvars[ski]] + settings_vars[ski]
                    else: # just combine the two lists
                        #print(settings_vars[ski])
                        settings_realvars[ski] = settings_realvars[ski] + settings_vars[ski]
            color,  alpha,  linestyle,  linewidth,  marker,  markersize,  markerfacecolor,  markeredgecolor,  markeredgewidth, errorstyle,  error_band_opacity,  elinewidth,  capsize, errorbox_xdata_l,  errorbox_xdata_r,  errorbox_ydata_l,  errorbox_ydata_u, errorbox_fc,  errorbox_fa,  errorbox_ec,  errorbox_ea,  errorbox_ew = settings_realvars

        else: # the only data present are in dictionary form
            xdata_lists = dxdata_lists
            ydata_lists = dydata_lists

            if all([x == None for x in ddata_labels]):
                data_labels = None
            else:
                data_labels = ddata_labels

            xerr_lists  = dxerr_lists
            yerr_lists  = dyerr_lists

            for ski in range(len(settings_keys)):
                if settings_keys[ski] in ['errorbox_xdata_l','errorbox_xdata_r','errorbox_ydata_l','errorbox_ydata_u']:
                    # the special exceptions which can be lists
                    if all(x==[] for x in settings_vars[ski]):
                        settings_vars[ski] = [[]] # set the error box parameters to appear as expected if empty
            color,  alpha,  linestyle,  linewidth,  marker,  markersize,  markerfacecolor,  markeredgecolor,  markeredgewidth, errorstyle,  error_band_opacity,  elinewidth,  capsize, errorbox_xdata_l,  errorbox_xdata_r,  errorbox_ydata_l,  errorbox_ydata_u, errorbox_fc,  errorbox_fa,  errorbox_ec,  errorbox_ea,  errorbox_ew = settings_vars

    # End of dictionary entry handling

    # Determine if error boxes are to be drawn
    draw_error_boxes = False
    if (errorbox_xdata_l!=[[]] or errorbox_xdata_r!=[[]]) and (errorbox_ydata_l!=[[]] or errorbox_ydata_u!=[[]]):
        draw_error_boxes = True

    if (not xdata_lists) and (not ydata_lists):
        print('Warning: Both xdata and ydata lists are empty (figure index = {}, titled "{}")'.format(figi,title_str))
        single_dataset = True
        include_legend = False
        xdata_lists = [[]]
        ydata_lists = []
        xerr_lists = [[]]
        yerr_lists = []
    elif (not xdata_lists):
        print('Warning: xdata list is empty (figure index = {}, titled "{}")'.format(figi,title_str))
    elif (not ydata_lists):
        print('Warning: ydata list is empty (figure index = {}, titled "{}")'.format(figi,title_str))

    # If using a single dataset (user inputs a single list, not a list of list(s)
    #if len(np.shape(ydata_lists)) != 1: # not just a simple list
    if (all(isinstance(el, (int, float)) for el in ydata_lists)): # input ydata is a single dataset, not a list of lists/arrays, convert to a list containing a single list for compatability with remainder of code
        single_dataset = True
        ydata_lists = [ydata_lists]
        yerr_lists = [yerr_lists]
        include_legend = False
        if draw_error_boxes:
            errorbox_xdata_l = [errorbox_xdata_l]
            errorbox_xdata_r = [errorbox_xdata_r]
            errorbox_ydata_l = [errorbox_ydata_l]
            errorbox_ydata_u = [errorbox_ydata_u]

    if not data_labels: include_legend = False

    nds = len(ydata_lists)

    # Allow use of single set of xdata for multiple sets of ydata
    if (not single_dataset) and (all(isinstance(el, (int, float)) for el in xdata_lists)): # ydata is list of lists, xdata is a single list.  Assume same xdata for each set of ydata
        xdata2 = []
        for i in range(nds):
            xdata2.append(xdata_lists)
        xdata_lists = xdata2

        if (all(isinstance(el, (int, float)) for el in xerr_lists)): # ydata is list of lists, xerr_data is a single list.  Assume same xerr_data for each set of ydata
            xerr2 = []
            for i in range(nds):
                xerr2.append(xerr_lists)
            xerr_lists = xerr2

        if draw_error_boxes:
            errorbox_xdata_l2 = []
            errorbox_xdata_r2 = []
            for i in range(nds):
                errorbox_xdata_l2.append(errorbox_xdata_l)
                errorbox_xdata_r2.append(errorbox_xdata_r)
            errorbox_xdata_l = errorbox_xdata_l2
            errorbox_xdata_r = errorbox_xdata_r2


    fst = title_fs #16
    fs = axis_fs #14
    y_min = 1.0e10  # later used to set y-axis minimum
    y_max = 1.0e-14 # later used to set y-axis maximum
    x_min = 1.0e5   # later used to set x-axis minimum
    x_max = 1.0e1   # later used to set x-axis maximum

    plt.rc('font', family=f_family, style=f_style, variant=f_variant, weight=f_weight)

    if fig==None:
        fig = plt.figure(figi)
    #bg_color = '#FFFFFF' #'#E1E4E6'
    #fig.patch.set_facecolor(bg_color)
    #fig.patch.set_alpha(1.0)
    ax = plt.subplot(int(spnrows), int(spncols), int(spindex))

    for i in range(nds):
        xdata = xdata_lists[i]
        ydata = np.array(ydata_lists[i])
        xerr=None
        yerr=None
        xerr_present = False
        yerr_present = False
        if len(xerr_lists[0])>0:
            xerr = xerr_lists[i]
            if np.sum(xerr)==0:
                xerr = None
            else:
                xerr_present = True
        if len(yerr_lists[0])>0:
            yerr = yerr_lists[i]
            if np.sum(yerr)==0:
                yerr = None
            else:
                yerr_present = True

        if include_legend:
            label_str = data_labels[i]
        else:
            label_str = ''

        # Get settings which may be constant or vary by dataset (lists)
        if isinstance(color, (list,np.ndarray)):
            c = color[i]
        else:
            c = color
        if isinstance(alpha, (list,np.ndarray)):
            alp = alpha[i]
        else:
            alp = alpha
        if isinstance(linestyle, (list,np.ndarray)):
            ls = linestyle[i]
        else:
            ls = linestyle
        if isinstance(linewidth, (list,np.ndarray)):
            lw = linewidth[i]
        else:
            lw = linewidth
        if isinstance(marker, (list,np.ndarray)):
            mkr = marker[i]
        else:
            mkr = marker
        if isinstance(markersize, (list,np.ndarray)):
            mks = markersize[i]
        else:
            mks = markersize
        if isinstance(errorstyle, (list,np.ndarray)):
            ers = errorstyle[i]
        else:
            ers = errorstyle
        if isinstance(error_band_opacity, (list,np.ndarray)):
            ebo = error_band_opacity[i]
        else:
            ebo = error_band_opacity
        if isinstance(elinewidth, (list,np.ndarray)):
            elw = elinewidth[i]
        else:
            elw = elinewidth
        if isinstance(capsize, (list,np.ndarray)):
            ecs = capsize[i]
        else:
            ecs = capsize
        if isinstance(markerfacecolor, (list,np.ndarray)):
            mfc = markerfacecolor[i]
        else:
            mfc = markerfacecolor
        if isinstance(markeredgecolor, (list,np.ndarray)):
            mec = markeredgecolor[i]
        else:
            mec = markeredgecolor
        if isinstance(markeredgewidth, (list,np.ndarray)):
            mew = markeredgewidth[i]
        else:
            mew = markeredgewidth

        # Make actual plot
        if (not xerr_present and not yerr_present) or (ers=='band' and not xerr_present):
            if color=='#FDFEFC' or color[0]=='#FDFEFC': # assume user will never actually want/input this specific white color
                p = ax.plot(xdata,ydata,label=label_str,ls=ls,lw=lw,marker=mkr,ms=mks,mfc=mfc,mec=mec,mew=mew,alpha=alp)
            else:
                p = ax.plot(xdata,ydata,label=label_str,c=c,ls=ls,lw=lw,marker=mkr,ms=mks,mfc=mfc,mec=mec,mew=mew,alpha=alp)
        else:
            if color=='#FDFEFC' or color[0]=='#FDFEFC': # assume user will never actually want/input this specific white color
                p = ax.errorbar(xdata,ydata,xerr=xerr,yerr=yerr,label=label_str,ls=ls,lw=lw,marker=mkr,ms=mks,elinewidth=elw,capsize=ecs,mfc=mfc,mec=mec,mew=mew,alpha=alp)
            else:
                p = ax.errorbar(xdata,ydata,xerr=xerr,yerr=yerr,label=label_str,c=c,ls=ls,lw=lw,marker=mkr,ms=mks,elinewidth=elw,capsize=ecs,mfc=mfc,mec=mec,mew=mew,alpha=alp)

        if (ers=='bar-band' or ers=='band') and (yerr_present or xerr_present):
            if color=='#FDFEFC' or color[0]=='#FDFEFC': # assume user will never actually want/input this specific white color
                c = p[0].get_color() # need to grab whatever color was just used
            if yerr_present:
                if len(np.shape(yerr))==1:
                    ax.fill_between(xdata, np.array(ydata)-np.array(yerr), np.array(ydata)+np.array(yerr),color=c,alpha=ebo)
                else:
                    ax.fill_between(xdata, np.array(ydata)-np.array(yerr[0,:]), np.array(ydata)+np.array(yerr[1,:]),color=c,alpha=ebo)
            else: # Fix this later to also accomodate cases where both x and y error are present?
                if len(np.shape(xerr))==1:
                    ax.fill_betweenx(ydata, np.array(xdata)-np.array(xerr), np.array(xdata)+np.array(xerr),color=c,alpha=ebo)
                else:
                    ax.fill_betweenx(ydata, np.array(xdata)-np.array(xerr[0,:]), np.array(xdata)+np.array(xerr[1,:]),color=c,alpha=ebo)

        if draw_error_boxes:
            draw_error_box_for_this_dataset = True
            # Ensure x and y error arrays are correctly sized, accounting for possible datasets without error boxes
            # determine which, if either, x errors are 'None'
            if (errorbox_xdata_l!=[[]] and errorbox_xdata_r==[[]]):
                erb_x_l = errorbox_xdata_l[i]
                if len(erb_x_l) != len(ydata):
                    draw_error_box_for_this_dataset = False
                else:
                    erb_x_r = 0*np.array(erb_x_l)
            elif (errorbox_xdata_l==[[]] and errorbox_xdata_r!=[[]]):
                erb_x_r = errorbox_xdata_r[i]
                if len(erb_x_r) != len(ydata):
                    draw_error_box_for_this_dataset = False
                else:
                    erb_x_l = 0*np.array(erb_x_r)
            else: # both datasets possibly present
                erb_x_l = errorbox_xdata_l[i]
                erb_x_r = errorbox_xdata_r[i]
                if len(erb_x_l) != len(ydata) and len(erb_x_r) != len(ydata):
                    draw_error_box_for_this_dataset = False
                elif len(erb_x_l) != len(ydata) or len(erb_x_r) != len(ydata):
                    if len(erb_x_l) != len(ydata):
                        erb_x_l = 0*np.array(erb_x_r)
                    elif len(erb_x_r) != len(ydata):
                        erb_x_r = 0*np.array(erb_x_l)

            # determine which, if either, y errors are 'None'
            if (errorbox_ydata_l!=[[]] and errorbox_ydata_u==[[]]):
                erb_y_l = errorbox_ydata_l[i]
                if len(erb_y_l) != len(ydata):
                    draw_error_box_for_this_dataset = False
                else:
                    erb_y_u = 0*np.array(erb_y_l)
            elif (errorbox_ydata_l==[[]] and errorbox_ydata_u!=[[]]):
                erb_y_u = errorbox_ydata_u[i]
                if len(erb_y_u) != len(ydata):
                    draw_error_box_for_this_dataset = False
                else:
                    erb_y_l = 0*np.array(erb_y_u)
            else: # both datasets possibly present
                erb_y_l = errorbox_ydata_l[i]
                erb_y_u = errorbox_ydata_u[i]
                if len(erb_y_l) != len(ydata) and len(erb_y_u) != len(ydata):
                    draw_error_box_for_this_dataset = False
                elif len(erb_y_l) != len(ydata) or len(erb_y_u) != len(ydata):
                    if len(erb_y_l) != len(ydata):
                        erb_y_l = 0*np.array(erb_y_u)
                    elif len(erb_y_u) != len(ydata):
                        erb_y_u = 0*np.array(erb_y_l)

            if draw_error_box_for_this_dataset:
                xerrbox = [erb_x_l,erb_x_r]
                yerrbox = [erb_y_l,erb_y_u]

                # Get settings which may be constant or vary by dataset (lists)
                if isinstance(errorbox_fc, (list,np.ndarray)):
                    efc = errorbox_fc[i]
                else:
                    efc = errorbox_fc
                if isinstance(errorbox_ec, (list,np.ndarray)):
                    eec = errorbox_ec[i]
                else:
                    eec = errorbox_ec
                if isinstance(errorbox_ea, (list,np.ndarray)):
                    eea = errorbox_ea[i]
                else:
                    eea = errorbox_ea
                if isinstance(errorbox_fa, (list,np.ndarray)):
                    efa = errorbox_fa[i]
                else:
                    efa = errorbox_fa
                if isinstance(errorbox_ew, (list,np.ndarray)):
                    eew = errorbox_ew[i]
                else:
                    eew = errorbox_ew

                makeErrorBoxes(ax,xdata,ydata,xerrbox,yerrbox,fc='None',ec=eec   ,alpha=eea,lw=eew) # outline
                makeErrorBoxes(ax,xdata,ydata,xerrbox,yerrbox,fc=efc   ,ec='None',alpha=efa,lw=eew) # fill face




        if len(ydata) != 0:
            if all([yi==None for yi in ydata]):
                print("\t\tfancy_plot warning: Encountered set of only 'None' at index {}".format(i))
            elif len(ydata[np.nonzero(ydata)]) != 0:
                if min(ydata[np.nonzero(ydata)])<y_min: y_min = min(ydata[np.nonzero(ydata)])
                #if min(ydata)<y_min: y_min = min(ydata)
                if max(ydata[ydata!=None])>y_max: y_max = max(ydata[ydata!=None])
                if min(xdata)<x_min: x_min = min(xdata)
                if max(xdata)>x_max: x_max = max(xdata)

    if title_str.strip() != '':
        window_title = slugify(title_str) # "comparison_fig"
    else:
        window_title = 'Figure ' + str(figi)
    #window_title = window_title.replace('b','',1) # remove leading 'b' character from slugify process
    fig.canvas.manager.set_window_title(window_title)

    # hangle figure/legend positioning/sizing
    # First, figure size
    default_fig_x_in = fig_width_inch
    default_fig_y_in = fig_height_inch
    fig_x_in = default_fig_x_in
    fig_y_in = default_fig_y_in
    fig.set_size_inches(fig_x_in,fig_y_in)

    mpl_leg_pos_names = ['best','upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center']
    custom_leg_pos_names = ['outside right', 'outside bottom']

    if include_legend and legend_position in custom_leg_pos_names:
        if legend_anchor==None:
            if legend_position=='outside right':
                legend_anchor = (1.0,0.75)
            elif legend_position=='outside bottom':
                legend_anchor = (0.5,-0.17)
        leg1_anchor = legend_anchor # varied items
        handles_l1, labels_l1 = ax.get_legend_handles_labels()
        if legend_position == 'outside right':
            legend1 = ax.legend(handles_l1, labels_l1,loc='upper left',bbox_to_anchor=leg1_anchor,ncol=legend_ncol,framealpha=legend_alpha,columnspacing=legend_columnspacing)
        elif legend_position == 'outside bottom':
            if legend_ncol == 1 and len(data_labels) > 1: legend_ncol = len(data_labels)
            legend1 = ax.legend(handles_l1, labels_l1,loc='upper center',bbox_to_anchor=leg1_anchor,ncol=legend_ncol,framealpha=legend_alpha,columnspacing=legend_columnspacing)
        ax.add_artist(legend1)
        fig.canvas.draw()
        f1 = legend1.get_frame()
        l1_w0_px, l1_h0_px = f1.get_width(), f1.get_height()
        l_w0_in, l_h0_in = l1_w0_px/fig.dpi, l1_h0_px/fig.dpi  # width and height of legend, in inches
    else:
        l_w0_in, l_h0_in = 0.0, 0.0
        if include_legend and legend_position not in custom_leg_pos_names: # use matplotlib default-style legend inside plot area
            ax.legend(loc=legend_position,ncol=legend_ncol,framealpha=legend_alpha,columnspacing=legend_columnspacing)

    n_title_lines = 0
    if title_str.strip() != '':
        n_title_lines = 1 + title_str.count('\n')
    n_xlabel_lines = 0
    if x_label_str.strip() != '':
        n_xlabel_lines = 1 + x_label_str.count('\n')
    n_ylabel_lines = 0
    if y_label_str.strip() != '':
        n_ylabel_lines = 1 + y_label_str.count('\n')

    # These values are good, do not change them.  (derived while working on SHAEDIT project)
    x0bar = 0.60 + 0.200*n_ylabel_lines # inches, horizontal space needed for ylabel
    y0bar = 0.45 + 0.200*n_xlabel_lines # inches, vertical space needed for xticks/numbers, xlabel and any extra lines it has
    t0bar = 0.10 + 0.300*n_title_lines  # inches, vertical space needed for title
    del_l_in = 0.15               # inches, extra horizontal padding right of legend

    # adjust legend spacing depending on its position
    if legend_position=='outside right':
        l_h0_in = 0.0
    elif legend_position=='outside bottom':
        l_w0_in = 0.0

    # Plot window placement and sizing
    x0 = x0bar/fig_x_in                                      # distance from left edge that plot area begins
    y0 = y0bar/fig_y_in + (l_h0_in/fig_y_in)                 # distance from bottom edge that plot area begins
    h0 = 1 - (y0bar+t0bar)/fig_y_in - (l_h0_in/fig_y_in)     # height of plot area, set to be full height minus space needed for title, x-label, and potentially an outside bottom legend
    w0 = 1 - x0 - (l_w0_in/fig_x_in) - (del_l_in/fig_x_in)   # width of plot area, set to be full width minus space needed for y-label and potentially an outside right legend

    if man_sp_placement:
        if spx0!=None: x0 = spx0
        if spy0!=None: y0 = spy0
        if sph0!=None: h0 = sph0
        if spw0!=None: w0 = spw0

    # Set size and location of the plot on the canvas
    box = ax.get_position()
    # all vals in [0,1]: left, bottom, width, height
    if not man_sp_placement and (spnrows != 1 or spncols != 1):
        pstr  = 'Warning: It is highly encouraged that subplots be positioned manually.\n'
        pstr += '   This is done by setting man_sp_placement=True and then adjusting\n'
        pstr += '   the parameters spx0, spy0, sph0, and spw0 for each subplot.\n'
        pstr += '   The current plot was automatically sized by matplotlib.\n'
        print(pstr)
    else:
        ax.set_position([x0, y0, w0, h0])


    plt.title(title_str,fontsize=fst)
    plt.xlabel(x_label_str,fontsize=fs)
    plt.ylabel(y_label_str,fontsize=fs)
    plt.xscale(x_scale)
    plt.yscale(y_scale)
    plt.grid(visible=True, which='major', linestyle='-', alpha=0.25)
    plt.grid(visible=True, which='minor', linestyle='-', alpha=0.10)
    # ensure at least minimum number of decades are present on a plot by increasing padding if necessary
    zoom_mult = 1.0
    x_log_buffer = 0.15*zoom_mult
    y_log_buffer = 0.2*zoom_mult
    min_x_decs = 2
    min_y_decs = 2

    x_scale='linear'

    if not x_limits:
        if x_scale == 'log': # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
            if (np.log10(x_max)-np.log10(x_min)+2*x_log_buffer) < min_x_decs:
                x_log_buffer = 0.5*(min_x_decs - (np.log10(x_max)-np.log10(x_min)))
            plt.xlim([10**(np.log10(x_min)-x_log_buffer),10**(np.log10(x_max)+x_log_buffer)])
    else:
        plt.xlim(x_limits)

    if not y_limits:
        if y_scale == 'log': # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
            if (np.log10(y_max)-np.log10(y_min)+2*y_log_buffer) < min_y_decs:
                y_log_buffer = 0.5*(min_y_decs - (np.log10(y_max)-np.log10(y_min)))
            plt.ylim([10**(np.log10(y_min)-y_log_buffer),10**(np.log10(y_max)+y_log_buffer)])
    else:
        plt.ylim(y_limits)

    return fig, ax






def fancy_3D_plot(
               # Required data
               xdata_lists,ydata_lists,zdata_lists,

               # Optional data
               plot_styles=None, data_labels=[],
               # Standard basic settings (optional)
               figi=1, title_str='',  x_label_str='x-axis',  y_label_str='y-axis', z_label_str='z-axis',
               x_limits=[],  y_limits=[],  z_limits=[], use_mpl_limits=True, x_scale='linear',  y_scale='linear',  z_scale='linear',
               OoB_z_handling = 'NaN',

               fig_width_inch=9.5,  fig_height_inch=6.5, title_fs=16,  axis_fs=14,
               f_family='sans-serif',f_style='normal',f_variant='normal',f_weight='normal',
               rasterize=False,

               fig=None, ax=None, spnrows=1, spncols=1, spindex=1,
               man_sp_placement = False, spx0=0.1, spy0=0.1, sph0=0.4, spw0=0.4,

               color='#FDFEFC', cmap='viridis', facecolors=None, depthshade=True, linestyle='-', linewidth=1,
               marker='.', markersize=5, markerfacecolor=None, markeredgecolor=None, markeredgewidth=None,
               rstride=1,cstride=1,rcount=50,ccount=50,
               alpha=None,

               # Color map options
               x_meaning='mid',y_meaning='mid',
               cbar_fs=None,cbar_size=5,cbar_pad=0.1,

               # Legend settings
               legend_position='outside bottom', legend_anchor=None, legend_ncol=1, legend_alpha=None,
               ):
    '''
    Description:
        Generate a 3D plot containing an arbitrary number of datasets.  The z-axis of each of the datasets can either be a 1-D list (describing
           scatter points or a line) or a 2-D NumPy array (describing a surface); the x and y axes must be 1-D and match the correct dimension
           of the z-axis dataset.

    Dependencies:
      - `import numpy as np`
      - `import matplotlib.pyplot as plt`
      - `from mpl_toolkits.mplot3d import Axes3D`
      - `import matplotlib.ticker as mticker`
      - `from mpl_toolkits.mplot3d.axis3d import Axis`
      - `import matplotlib.projections as proj`
      - `from matplotlib.colors import colorConverter`

    Inputs:
       (Required)

      - `xdata_lists` = a list containing lists/arrays of 1-D x data (or single list of xdata applied to all zdata in `z_data_lists`)
      - `ydata_lists` = a list containing lists/arrays of 1-D y data (or single list of ydata applied to all zdata in `z_data_lists`)
      - `zdata_lists` = a list containing lists/arrays of z datasets (or a single list/array),
           - individual z datasets can be provided in either of two different formats:
               - 1) 1-D lists (of the same dimension of the corresponding x and y lists)
               - 2) 2-D NumPy arrays whose whidth and height match the dimensions of the x and y lists.

    Inputs:
       (Optional, basic, generic)

      - `plot_styles` = list of (or individual) strings denoting the plot style to be used for each dataset. Options include:
          + 1-D `['line','scatter','trisurface']`   (D=`'line'`)
          + 2-D `['surface','wireframe','trisurface','contour','filledcontour']`   (D=`'trisurface'`)
          + 2-D_colormaps `['map_pcolormesh','map_filledcontour','map_contour']`
      - `data_labels` = a list of strings to be used as data labels in the legend (D=`[]`, no legend generated) (labels do not work for contours)
      - `figi` = figure index (D=`1`)
      - `title_str` = string to be used as the title of the plot (D=`''`)
      - `x_label_str` = string to be used as x-axis title (D=`'x-axis'`)
      - `y_label_str` = string to be used as y-axis title (D=`'y-axis'`)
      - `z_label_str` = string to be used as z-axis title (D=`'z-axis'`)
      - `x_limits` = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=auto-calculated based on `x_data_lists`)
      - `y_limits` = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=auto-calculated based on `y_data_lists`)
      - `z_limits` = length 2 list specifying minimum and maximum z-axis bounds [zmin,zmax] (D=auto-calculated based on `z_data_lists`)
      - `use_mpl_limits` = boolean specifying if Matplotlib default (`True`) or specially calculated (`False`) log-scale axis limits are used when they aren't specified (D=`True`)
      - `x_scale` = x-axis scale, either `"linear"` or `"log"`
      - `y_scale` = y-axis scale, either `"linear"` or `"log"`
      - `z_scale` = z-axis scale, either `"linear"` or `"log"`
      - `OoB_z_handling` = string denoting how z values outside of z_limits, if provided, will be handled. (D=`'NaN'`, other option are `'limits'` and `'None'`)
                       By default, out of bounds (OoB) values are replaced with `NaN`.  If this is set to `'limits'`, OoB values are set equal to the lower/upper limit provided.
                       If `'None'`, no values are replaced (this may cause errors with 3-D plots).
      - `fig_width_inch` = figure width in inches (D=`9.5`)
      - `fig_height_inch` = figure height in inches (D=`6.5`)
      - `title_fs` = title font size (D=`16`)
      - `axis_fs` = axis label font size (D=`14`)
      - `f_family` = string specifying font family (D=`'sans-serif'`); options include: `['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']`
      - `f_style` = string specifying font style (D=`'normal'`); options include: `['normal', 'italic', 'oblique']`
      - `f_variant` = string specifying font variant (D=`'normal'`); options include: `['normal', 'small-caps']`
      - `f_weight` = string specifying font weight (D=`'normal'`); options include: `['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']`
      - `rasterize` = Boolean specifying if the ploted data (not labels) should be rasterized (D=`False`); `dpi` can be specified in the `savefig` call

    Inputs:
       (Optional, basic, 3D plot type specific)

        The below options are only applicable to specific `plot_styles`; this is denoted by the leftmost column.

      - `L P S W T C F` (L=`'line'`, P=`'scatter'`(points), S=`'surface'`, W=`'wireframe'`, T=`'trisurface'`, C=`'contour'`, F=`'filledcontour'`; `'o'` indicates options used by each plot type)
      - `o o o o o o o` |  `alpha` = list of (or individual) int/float of the alpha/opacity of each point/curve/surface/etc. (D=`None`)
      - `o o o o o o o` |  `color` = list of color strings to be used of same length as z_data_lists (or individual color string) (D=Matplotlib default color cycle)
      - `. . o . o o o` |  `cmap` = list of colormaps to be used of same length as z_data_lists, this will overwrite 'color' (or individual colormap) (D=`None`)
      - `o . . o . o .` |  `linestyle` = list of (or individual) strings denoting linestyle: `''`, `'-'`, `'--'`, `'-.'`, or `':'` (D=`'-'`)
      - `o . . o . o .` |  `linewidth` = list of (or individual) int/float of the width of line (D=`1`)
      - `o o . . . . .` |  `marker` = list of (or individual) marker styles (D=`'.'`) For all options, see: https://matplotlib.org/3.1.0/api/markers_api.html
      - `o o . . . . .` |  `markersize` = list of (or individual) int/float of marker size (D=`5`)
      - `o o . . . . .` |  `markerfacecolor` = list of (or individual) marker face colors (D=`None`, use value of `'color'`)
      - `o o . . . . .` |  `markeredgecolor` = list of (or individual) marker edge colors (D=`None`, use value of `'color'`)
      - `o o . . . . .` |  `markeredgewidth` = list of (or individual) int/float of marker edge widths (D=`None`)
      - `. o . . . . .` |  `depthshade` = list of (or individual) booleans to enable/disable marker shading for appearance of depth (D=`True`)
      - `. . o o . . .` |  `rstride` = [DEPRECATED] list of (or individual) int/float of array row strides (D=`1`)
      - `. . o o . . .` |  `cstride` = [DEPRECATED] list of (or individual) int/float of array column strides (D=`1`)
      - `. . o o . . .` |  `rcount`  = list of (or individual) int/float of maximum number of rows used (D=`50`)
      - `. . o o . . .` |  `ccount`  = list of (or individual) int/float of maximum number of columns used (D=`50`)
      - `. . o . . . .` |  `facecolors` = list of (or individual) array mapping colors to each facet of the zdata (D=`None`) overwrites cmap

    Inputs:
       (Optional, 2D colormap type specific)

      - `x_meaning` = string specifying if x values describe x min, x max, or central x value for each corresponding z (D=`'mid'`); options include: `['min','max','mid']` (think of like bin min/max/mid)
      - `y_meaning` = string specifying if y values describe y min, y max, or central y value for each corresponding z (D=`'mid'`); options include: `['min','max','mid']`
      - `cbar_fs` = color bar label font size (D=`axis_fs` (D=`14`))
      - `cbar_size` = color bar size expressed as an integer/float between 0 and 100 (D=`5`) (think of as percentage width)
      - `cbar_pad` = color bar padding (should be between 0 and 1) (D=`0.1`)


    Inputs:
       (Optional, advanced)

       Subplots

         - `fig` = figure handles from existing figure to draw on (D=`None`, `fig=None` should always be used for initial subplot unless a figure canvas has already been generated)
         - `ax` = axis handles from an existing figure to draw on (D=`None`, `ax=None` should always be used for initial subplot)
         - `spnrows` = number of rows in final subplot (D=`1`)
         - `spncols` = number of columns in final subplot (D=`1`)
         - `spindex` = index of current subplot (between 1 and spnrows*spncols) (D=`1`)
         - `man_sp_placement` = logical variable controlling manual sizing/placement of subplots using below variables (D=`False`, use automatic sizing)
         - `spx0` = distance from canvas left edge where this plotting area should begin (D=`0.1`), generally a number around 0~1
         - `spy0` = distance from canvas bottom edge where this plotting area should begin (D=`0.1`), generally a number around 0~1
         - `spw0` = width of this plotting area on the canvas (D=`0.4`), generally a number around 0~1
         - `sph0` = height of this plotting area on the canvas (D=`0.4`), generally a number around 0~1

       Legend settings

         - `legend_position` = one of the default matplotlib legend position strings (`'best'`,`'upper right'`,`'lower center'`,`'lower left'`,etc.) to place the legend inside the plot or
                           `'outside right'` or `'outside bottom'` to place the legend outside of the plot area (D=`'outside bottom'`, if legend is to be used)
         - `legend_anchor` = legend anchor position (x=left-right position, y=bottom-top position) only used when legend position is set to one of the "outside" options
                           (D=`None` which becomes `(1.0,0.75)` if position is `'outside right'` or `(0.5,-0.17)` if position is `'outside bottom'`)
                           Note that only one coordinate usually should be adjusted.  If using an `'outside right'` legend, only the y-coordinate needs to be manipulated
                           to scoot the legend up/down.  Likewise, for `'outside bottom'` legends only the x-coordinate needs adjusting for tuning left/right position
         - `legend_ncol` = number of columns in legend (D=`1` in all cases except for legend_position=`'outside bottom'` where D=`len(ydata_lists)`)
         - `legend_alpha` = alpha of legend background (D=`None`, auto determined by matplotlib)


    '''
    '''
        Notes: 
        
        Leftover string not yet used for 2D colormap specific options: 
        The below options are only applicable to specific plot styles; this is denoted by the leftmost column.
        P C F (P='map_pcolormesh', C='map_contour', F='map_filledcontour'; 'o' indicates options used by each plot type)
    '''

    # This allows for implementation of hacked in minor gridlines
    class axis3d_custom(Axis): # https://stackoverflow.com/questions/31684448/how-to-color-a-specific-gridline-tickline-in-3d-matplotlib-scatter-plot-figure
        def __init__(self, adir, v_intervalx, d_intervalx, axes, *args, **kwargs):
            Axis.__init__(self, adir, v_intervalx, d_intervalx, axes, *args, **kwargs)
            self.gridline_colors = []
        def set_gridline_color(self, *gridline_info):
            '''Gridline_info is a tuple containing the value of the gridline to change
            and the color to change it to. A list of tuples may be used with the * operator.'''
            self.gridline_colors.extend(gridline_info)
        def draw(self, renderer):
            # filter locations here so that no extra grid lines are drawn
            Axis.draw(self, renderer)
            which_gridlines = []
            if self.gridline_colors:
                locmin, locmax = self.get_view_interval()
                if locmin > locmax:
                    locmin, locmax = locmax, locmin

                # Rudimentary clipping
                majorLocs = [loc for loc in self.major.locator() if
                             locmin <= loc <= locmax]
                for i, val in enumerate(majorLocs):
                    for colored_val, color in self.gridline_colors:
                        if val == colored_val:
                            which_gridlines.append((i, color))
                colors = self.gridlines.get_colors()
                for val, color in which_gridlines:
                    colors[val] = colorConverter.to_rgba(color)
                self.gridlines.set_color(colors)
                self.gridlines.draw(renderer, project=True)

    class XAxis(axis3d_custom):
        def get_data_interval(self):
            'return the Interval instance for this axis data limits'
            return self.axes.xy_dataLim.intervalx

    class YAxis(axis3d_custom):
        def get_data_interval(self):
            'return the Interval instance for this axis data limits'
            return self.axes.xy_dataLim.intervaly

    class ZAxis(axis3d_custom):
        def get_data_interval(self):
            'return the Interval instance for this axis data limits'
            return self.axes.zz_dataLim.intervalx

    class Axes3D_custom(Axes3D):
        """
        3D axes object.
        """
        name = '3d_custom'

        def _init_axis(self):
            '''Init 3D axes; overrides creation of regular X/Y axes'''
            self.w_xaxis = XAxis('x', self.xy_viewLim.intervalx,
                                self.xy_dataLim.intervalx, self)
            self.xaxis = self.w_xaxis
            self.w_yaxis = YAxis('y', self.xy_viewLim.intervaly,
                                self.xy_dataLim.intervaly, self)
            self.yaxis = self.w_yaxis
            self.w_zaxis = ZAxis('z', self.zz_viewLim.intervalx,
                                self.zz_dataLim.intervalx, self)
            self.zaxis = self.w_zaxis

            for ax in self.xaxis, self.yaxis, self.zaxis:
                ax.init3d()
    proj.projection_registry.register(Axes3D_custom)


    use_custom_3d_axis_class =  False # custom axes broken in newer version of matplotlib?




    valid_plot_styles = ['line','scatter','surface','wireframe','trisurface','contour','filledcontour','map_pcolormesh','map_filledcontour','map_contour']
    pls_by_dims = [['line','scatter','trisurface'],['surface','wireframe','trisurface','contour','filledcontour','map_pcolormesh','map_filledcontour','map_contour']]
    pls_maps = ['map_pcolormesh','map_filledcontour','map_contour']

    if data_labels:
        include_legend = True # used to toggle legend on/off
    else:
        include_legend = False
    single_dataset = False # Assume multiple datasets entered, but this can be tested to see if it is the case or not.



    if (not xdata_lists) and (not ydata_lists):
        print('Warning: Both xdata and ydata lists are empty (figure index = {}, titled "{}")'.format(figi,title_str))
        single_dataset = True
        include_legend = False
        xdata_lists = [[]]
        ydata_lists = [[]]
    elif (not xdata_lists):
        print('Warning: xdata list is empty (figure index = {}, titled "{}")'.format(figi,title_str))
    elif (not ydata_lists):
        print('Warning: ydata list is empty (figure index = {}, titled "{}")'.format(figi,title_str))

    # First, determine the number of datasets which have been provided
    # This is solely determined from the z axis entries.
    # A z list consisting of only floats/ints is interpreted only as being coordinates to corresponding
    # x and y lists of the same length.
    # If wanting to generate a plot with one axis whose values are unchanging in each dataset, please make that x or y.

    # The Z list can either be an individual an item or a list of supported structures.
    # Acceptable entries for Z are:
    #  - list of values to plot a line or scatter
    #  - 2D array (numpy, not a list of lists) whose shape matches the lengths of corresponding 1D arrays of x and y data

    if isinstance(zdata_lists, list):
        if (all(isinstance(el, (int, float)) for el in zdata_lists)): # just a single list of z coordinates provided
            ndatasets = 1
            zdata_lists = [zdata_lists]
        elif len(zdata_lists)==1: # provided just a single dataset which could either be a list of values or 2D numpy array
            ndatasets = 1
        else: # provided a number of datasets which could be composed of lists of values and/or 2D numpy arrays
            ndatasets = len(zdata_lists)
    elif isinstance(zdata_lists, np.ndarray):
        if len(np.shape(zdata_lists)) == 1: # single 1D array
            ndatasets = 1
            zdata_lists = zdata_lists.tolist()
        elif len(np.shape(zdata_lists)) == 2: # single 2D array
            ndatasets = 1
            zdata_lists = [zdata_lists]
        elif len(np.shape(zdata_lists)) == 3: # divide 3D array into multiple 2D slices
            ndatasets = np.shape(zdata_lists)[2]
            original_zdata_lists = zdata_lists
            zdata_lists = []
            zdata_lists = [original_zdata_lists[:,:,i] for i in range(np.shape(original_zdata_lists)[2])]
        else:
            print('Dimensions of zdata_lists numpy array is incorrect')
            return 0
    else:
        print('zdata_lists is invalid.  Please enter either a list (of lists) or numpy array')
        return 0

    if ndatasets>1:
        if isinstance(plot_styles, list):
            for i in plot_styles:
                if i in pls_maps:
                    print('Only 1 dataset is allowed per call of fancy_3D_plot when a map plot style is selected.')
                    return 0
        else:
            if plot_styles in pls_maps:
                print('Only 1 dataset is allowed per call of fancy_3D_plot when a map plot style is selected.')
                return 0

    # Determine if 2D color map or 3D plot
    plot_2D_map = False
    plot_pcolormesh = False
    if isinstance(plot_styles, list):
        if plot_styles[0] in pls_maps:
            plot_2D_map = True
            if plot_styles[0]=='map_pcolormesh': plot_pcolormesh = True
    else:
        if plot_styles in pls_maps:
            plot_2D_map = True
            if plot_styles=='map_pcolormesh': plot_pcolormesh = True

    zlen = ndatasets

    # At this point, zdata_lists if just a list containing either 1D lists or 2D numpy arrays
    # For each z dataset, determine if a list of z coords (1D) or xy map (2D) array
    nzdims = []
    for i in range(len(zdata_lists)):
        nzdims.append(len(np.shape(np.array(zdata_lists[i]))))


    # Now determine how the provided x and y data map onto the provided z data

    # Check if either x or y data lists are lists of floats/ints rather than a list of lists
    xdata_only_vals = (all(isinstance(el, (int, float)) for el in xdata_lists))
    ydata_only_vals = (all(isinstance(el, (int, float)) for el in ydata_lists))

    if xdata_only_vals:
        xdata_lists = [xdata_lists for i in range(ndatasets)]
    if ydata_only_vals:
        ydata_lists = [ydata_lists for i in range(ndatasets)]

    xlen = len(xdata_lists)
    ylen = len(ydata_lists)

    # Check that all dimensions fit correctly and are consistent
    for i in range(ndatasets):
        xvals = xdata_lists[i]
        yvals = ydata_lists[i]
        zvals = zdata_lists[i]

        if nzdims[i]==1: # 1D list
            zlength = len(zvals)
            zwidth = 1
        else: # 2D array
            zlength = np.shape(zvals)[0]
            zwidth = np.shape(zvals)[1]

        if zwidth==1: # points / line
            if not (len(xvals) == zlength and len(yvals) == zlength):
                print('Dimension mismatch of dataset i={} with x-length={}, y-length={}, and z-length={}, aborting.'.format(str(i),str(len(xvals)),str(len(yvals)),str(zlength)))
                return 0
        else: # surface
            if not (len(xvals) == zlength and len(yvals) == zwidth): # if not fitting expected dimensions
                if ((len(yvals) == zlength and len(xvals) == zwidth) or (plot_pcolormesh and (len(yvals) == zlength+1 or len(xvals) == zwidth+1))): # z vals need to be transposed
                    zdata_lists[i] = zdata_lists[i].T
                    print('Warning: Transpozing Z dataset i={} with x-length={}, y-length={}, and original z-shape from {} to {}.'.format(str(i),str(len(xvals)),str(len(yvals)),str(np.shape(zvals)),str(np.shape(zdata_lists[i]))))
                elif plot_pcolormesh and (len(yvals) == zwidth+1 or len(xvals) == zlength+1):
                    print('Note: For Z dataset i={} with x-length={}, y-length={}, and original z-shape from {} to {} can only be used with map_pcolormesh due to shape.'.format(str(i),str(len(xvals)),str(len(yvals)),str(np.shape(zvals)),str(np.shape(zdata_lists[i]))))
                else:
                    print('Dimension mismatch of dataset i={} with x-length={}, y-length={}, and z-shape={}, aborting.'.format(str(i),str(len(xvals)),str(len(yvals)),str(zlength)))
                    return 0




    fst = title_fs #16
    fs = axis_fs #14
    z_min = 1.0e10  # later used to set z-axis minimum
    z_max = 1.0e-14 # later used to set z-axis maximum
    y_min = 1.0e10  # later used to set y-axis minimum
    y_max = 1.0e-14 # later used to set y-axis maximum
    x_min = 1.0e5   # later used to set x-axis minimum
    x_max = 1.0e1   # later used to set x-axis maximum

    if z_scale == 'log':
        z_min = np.log10(z_min)
        z_max = np.log10(z_max)

    if y_scale == 'log':
        y_min = np.log10(y_min)
        y_max = np.log10(y_max)

    if x_scale == 'log':
        x_min = np.log10(x_min)
        x_max = np.log10(x_max)


    plt.rc('font', family=f_family, style=f_style, variant=f_variant, weight=f_weight)

    if fig==None:
        fig = plt.figure(figi)

    if plot_2D_map:
        ax = fig.add_subplot(spnrows, spncols, spindex)
    elif use_custom_3d_axis_class:
        ax = fig.add_subplot(spnrows, spncols, spindex, projection='3d_custom')
    else:
        ax = fig.add_subplot(spnrows, spncols, spindex, projection='3d')

    #bg_color = '#FFFFFF' #'#E1E4E6'
    #fig.patch.set_facecolor(bg_color)
    #fig.patch.set_alpha(1.0)
    #ax = plt.subplot(spnrows, spncols, spindex)

    for i in range(ndatasets):

        if include_legend:
            label_str = data_labels[i]
        else:
            label_str = ''

        if isinstance(plot_styles, list):
            pls = plot_styles[i]
        elif plot_styles==None:
            if nzdims[i]==1:
                pls = 'line'
            else:
                pls = 'trisurface'
        else:
            pls = plot_styles
            if pls not in valid_plot_styles:
                print('Submitted plot style "{}" for index {} dataset is not a valid entry.  Valid options include: '.format(pls,str(i)),valid_plot_styles,"Aborting.")
                return 0
            elif pls not in pls_by_dims[int(nzdims[i]-1)]:
                print('Submitted plot style "{}" for index {} dataset is not a valid entry for a {}-D dataset.  Valid options include: '.format(pls,str(i),str(nzdims[i])),pls_by_dims[int(nzdims[i]-1)],'Aborting.')
                return 0

        # Get settings which may be constant or vary by dataset (lists)
        if isinstance(color, list):
            c = color[i]
        else:
            c = color
        if c=='#FDFEFC': c= None

        if isinstance(cmap, list):
            cmp = cmap[i]
        else:
            cmp = cmap
        if isinstance(cmap,str): cmp = plt.get_cmap(cmp)

        if isinstance(linestyle, list):
            ls = linestyle[i]
        else:
            ls = linestyle
        if isinstance(linewidth, list):
            lw = linewidth[i]
        else:
            lw = linewidth
        if isinstance(marker, list):
            mkr = marker[i]
        else:
            mkr = marker
        if isinstance(markersize, list):
            mks = markersize[i]
        else:
            mks = markersize
        if isinstance(markerfacecolor, list):
            mfc = markerfacecolor[i]
        else:
            mfc = markerfacecolor
        if isinstance(markeredgecolor, list):
            mec = markeredgecolor[i]
        else:
            mec = markeredgecolor
        if isinstance(markeredgewidth, list):
            mew = markeredgewidth[i]
        else:
            mew = markeredgewidth
        if isinstance(depthshade, list):
            depthshade_i = depthshade[i]
        else:
            depthshade_i = depthshade

        if isinstance(rstride, list):
            rstride_i = rstride[i]
        else:
            rstride_i = rstride
        if isinstance(cstride, list):
            cstride_i = cstride[i]
        else:
            cstride_i = cstride
        if isinstance(rcount, list):
            rcount_i = rcount[i]
        else:
            rcount_i = rcount
        if isinstance(ccount, list):
            ccount_i = ccount[i]
        else:
            ccount_i = ccount
        if isinstance(facecolors, list):
            facecolors_i = facecolors[i]
        else:
            facecolors_i = facecolors
        if isinstance(alpha, list):
            alpha_i = alpha[i]
        else:
            alpha_i = alpha


        # Make actual plot

        xvals = np.array(xdata_lists[i]).astype(float)
        yvals = np.array(ydata_lists[i]).astype(float)
        zvals = np.array(zdata_lists[i]).astype(float)

        # If user provided axis bounds, enforce them now
        if x_limits:
            if x_limits[0]: xvals[xvals<x_limits[0]] = np.nan
            if x_limits[1]: xvals[xvals>x_limits[1]] = np.nan
        if y_limits:
            if y_limits[0]: yvals[yvals<y_limits[0]] = np.nan
            if y_limits[1]: yvals[yvals>y_limits[1]] = np.nan
        if z_limits:
            if OoB_z_handling=='NaN':
                if z_limits[0]: zvals[zvals<z_limits[0]] = np.nan
                if z_limits[1]: zvals[zvals>z_limits[1]] = np.nan
            elif OoB_z_handling=='limits':
                if z_limits[0]: zvals[zvals<z_limits[0]] = z_limits[0]
                if z_limits[1]: zvals[zvals>z_limits[1]] = z_limits[1]


        if z_scale == 'log':
            zvals[(zvals<=0)] = np.nan
            zvals = np.log10(zvals)
        if y_scale == 'log':
            yvals[yvals<=0] = np.nan
            yvals = np.log10(yvals)
        if x_scale == 'log':
            xvals[xvals<=0] = np.nan
            xvals = np.log10(xvals)

        if len(yvals) != 0:
            if len(yvals[np.nonzero(yvals)]) != 0:
                if min(yvals[np.nonzero(yvals)])<y_min: y_min = min(yvals[np.nonzero(yvals)])
                #if min(yvals)<y_min: y_min = min(yvals)
                if np.nanmax(yvals)>y_max: y_max = np.nanmax(yvals)
                if np.nanmin(xvals)<x_min: x_min = np.nanmin(xvals)
                if np.nanmax(xvals)>x_max: x_max = np.nanmax(xvals)
                if np.nanmin(zvals)<z_min: z_min = np.nanmin(zvals)
                if np.nanmax(zvals)>z_max: z_max = np.nanmax(zvals)


        if nzdims[i]==1: # 1D list
            zlength = len(zvals)
            zwidth = 1
        else: # 2D array
            zlength = np.shape(zvals)[0]
            zwidth = np.shape(zvals)[1]


        # Plotting functions

        if nzdims[i]==1:
            # line
            if pls=='line':
                ax.plot(xvals,yvals,zvals,label=label_str,rasterized=rasterize,
                        color=c,linestyle=ls,linewidth=lw,alpha=alpha_i,
                        marker=mkr,markersize=mks,markerfacecolor=mfc,markeredgecolor=mec,markeredgewidth=mew)

            # scatter
            elif pls=='scatter':
                if not c: c = mfc # if no color defined, check to see if marker face color was defined
                ax.scatter(xvals,yvals,zvals,label=label_str,rasterized=rasterize,
                           color=c,depthshade=depthshade_i,alpha=alpha_i,
                           marker=mkr,s=mks**2,linewidths=mew,edgecolors=mec)

            # trisurface
            elif pls=='trisurface':
                if cmp != None:
                    c = None
                if facecolors != None:
                    c = None
                    cmap = None
                ps1 = ax.plot_trisurf(xvals,yvals,zvals,label=label_str,rasterized=rasterize,
                                color=c,cmap=cmp,facecolors=facecolors_i,alpha=alpha_i)
                ps1._facecolors2d=ps1._facecolors3d
                ps1._edgecolors2d=ps1._edgecolors3d

            else:
                print('Encountered incompatability with plot style {} and data dimensionality {} for data index {}.  Aborting.'.format(pls,str(nzdims[i]),str(i)))

        else:
            xvals_original,yvals_original = xvals,yvals
            xvals,yvals = np.meshgrid(xvals,yvals)

            # surface
            if pls=='surface':
                if cmp != None:
                    c = None
                if facecolors != None:
                    c = None
                    cmap = None
                ps1 = ax.plot_surface(xvals,yvals, zvals.T,label=label_str,rasterized=rasterize,
                                color=c,cmap=cmp,facecolors=facecolors_i,alpha=alpha_i,
                                rcount=rcount_i,ccount=ccount_i,
                                antialiased=False,
                                vmin=z_min,vmax=z_max) # this line was once not needed
                ps1._facecolors2d=ps1._facecolor3d
                ps1._edgecolors2d=ps1._edgecolor3d

            # wireframe
            elif pls=='wireframe':
                ax.plot_wireframe(xvals,yvals, zvals.T,label=label_str,rasterized=rasterize,
                                  color=c,linestyle=ls,linewidth=lw,alpha=alpha_i,
                                  rcount=rcount_i,ccount=ccount_i)

            elif pls=='trisurface':
                xvals = np.reshape(xvals, -1)
                yvals = np.reshape(yvals, -1)
                xtri = []
                ytri = []
                ztri = []
                for yi in range(np.shape(zvals)[1]):
                    for xi in range(np.shape(zvals)[0]):
                        ztri.append(zvals[xi,yi])
                        #xtri.append(xdata_lists[i][xi])
                        #ytri.append(ydata_lists[i][yi])

                if cmp != None:
                    c = None
                if facecolors != None:
                    c = None
                    cmap = None

                ps1 = ax.plot_trisurf(xvals,yvals,ztri,label=label_str,rasterized=rasterize,
                                color=c,cmap=cmp,facecolors=facecolors_i,alpha=alpha_i)
                ps1._facecolors2d=ps1._facecolors3d
                ps1._edgecolors2d=ps1._edgecolors3d

            # contour
            elif pls=='contour':
                if cmp != None: c = None
                ax.contour(xvals,yvals, zvals.T,rasterized=rasterize,
                           colors=c,cmap=cmp,linestyles=ls,linewidths=lw,alpha=alpha_i)

            # filled contour
            elif pls=='filledcontour':
                if cmp != None: c = None
                ax.contourf(xvals,yvals, zvals.T,rasterized=rasterize,
                            colors=c,cmap=cmp,alpha=alpha_i)



            # map contour
            elif pls=='map_pcolormesh':
                if cmp != None: c = None
                # first, check if x and y dims are 1 larger than z dims
                expand_x, expand_y = False, False
                if np.shape(yvals)[0]==np.shape(zvals)[1]:
                    expand_y = True
                if np.shape(xvals)[1]==np.shape(zvals)[0]:
                    expand_x = True
                # make x any y bigger by 1 since pcolormesh takes all edges, not just midpoints
                if expand_x:
                    dx = xvals[:,1:] - xvals[:,:-1]
                    if x_meaning=='min':
                        newx = (xvals[:,-1]+dx[:,-1]).reshape(len(xvals[:,0]),1)
                        xvals = np.hstack(( xvals , newx ))
                        yvals = np.hstack(( yvals, yvals[:,-1].reshape(len(yvals[:,-1]),1)))
                    if x_meaning=='max':
                        newx = (xvals[:,0]-dx[:,0]).reshape(len(xvals[:,0]),1)
                        xvals = np.hstack(( newx , xvals ))
                        yvals = np.hstack(( yvals[:,0].reshape(len(yvals[:,0]),1), yvals  ))
                    if x_meaning=='mid':
                        newx = (xvals[:,0]-0.5*dx[:,0]).reshape(len(xvals[:,0]),1)
                        dx =np.hstack((dx, np.tile(dx[:, [-1]], 1)))
                        xvals = xvals + 0.5*dx
                        xvals = np.hstack(( newx , xvals ))
                        yvals = np.hstack(( yvals[:,0].reshape(len(yvals[:,0]),1), yvals  ))
                if expand_y:
                    dy = yvals[1:] - yvals[:-1]
                    if y_meaning=='min':
                        newy = yvals[-1,:]+dy[-1,:]
                        yvals = np.vstack(( yvals , newy ))
                        xvals = np.vstack(( xvals, xvals[-1,:] ))
                    if y_meaning=='max':
                        newy = yvals[0,:]-dy[0,:]
                        yvals = np.vstack(( newy, yvals ))
                        xvals = np.vstack(( xvals[0,:] , xvals ))
                    if y_meaning=='mid':
                        newy = yvals[0,:]-0.5*dy[0,:]
                        dy =np.vstack((dy, np.tile(dy[[-1],:], 1)))
                        yvals = yvals + 0.5*dy
                        yvals = np.vstack(( newy , yvals ))
                        xvals = np.vstack(( xvals[0,:], xvals  ))

                pcm2d = ax.pcolormesh(xvals,yvals, zvals.T,rasterized=rasterize,
                           cmap=cmp,linestyles=ls,linewidths=lw,alpha=alpha_i)


            # map contour (normal or filled)
            elif pls=='map_filledcontour' or pls=='map_contour':
                if cmp != None: c = None
                if x_meaning!='mid':
                    # shift x values to be midpoints
                    dx = xvals[:,1:] - xvals[:,:-1]
                    if x_meaning=='min':
                        dx =np.hstack((dx, np.tile(dx[:, [-1]], 1)))
                        xvals = xvals + 0.5*dx
                    if x_meaning=='max':
                        dx = np.hstack((np.tile(dx[:, [0]], 1), dx))
                        xvals = xvals - 0.5*dx
                if y_meaning!='mid':
                    # shift y values to be midpoints
                    dy = yvals[1:] - yvals[:-1]
                    if y_meaning=='min':
                        dy =np.vstack((dy, np.tile(dy[[-1],:], 1)))
                        yvals = yvals + 0.5*dy
                    if y_meaning=='max':
                        dy = np.vstack((np.tile(dy[[0],:], 1), dy))
                        yvals = yvals - 0.5*dy
                        #print(yvals)

                if pls=='map_contour':
                    pcm2d = ax.contour(xvals,yvals, zvals.T,rasterized=rasterize,
                                cmap=cmp,linestyles=ls,alpha=alpha_i)
                else:
                    pcm2d = ax.contourf(xvals,yvals, zvals.T,rasterized=rasterize,
                                cmap=cmp,linestyles=ls,alpha=alpha_i)

            else:
                print('Encountered incompatability with plot style {} and data dimensionality {} for data index {}.  Aborting.'.format(pls,str(nzdims[i]),str(i)))



    if title_str.strip() != '':
        window_title = slugify(title_str) # "comparison_fig"
    else:
        window_title = 'Figure ' + str(figi)
    #window_title = window_title.replace('b','',1) # remove leading 'b' character from slugify process
    fig.canvas.manager.set_window_title(window_title)

    # hangle figure/legend positioning/sizing
    # First, figure size
    default_fig_x_in = fig_width_inch
    default_fig_y_in = fig_height_inch
    fig_x_in = default_fig_x_in
    fig_y_in = default_fig_y_in
    fig.set_size_inches(fig_x_in,fig_y_in)


    mpl_leg_pos_names = ['best','upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center']
    custom_leg_pos_names = ['outside right', 'outside bottom']

    if include_legend and legend_position in custom_leg_pos_names:
        if legend_anchor==None:
            if legend_position=='outside right':
                legend_anchor = (1.0,0.75)
            elif legend_position=='outside bottom':
                legend_anchor = (0.5,-0.05)
        leg1_anchor = legend_anchor # varied items
        handles_l1, labels_l1 = ax.get_legend_handles_labels()
        if legend_position == 'outside right':
            legend1 = ax.legend(handles_l1, labels_l1,loc='upper left',bbox_to_anchor=leg1_anchor,ncol=legend_ncol,framealpha=legend_alpha)
        elif legend_position == 'outside bottom':
            if legend_ncol == 1 and len(data_labels) > 1: legend_ncol = len(data_labels)
            legend1 = ax.legend(handles_l1, labels_l1,loc='upper center',bbox_to_anchor=leg1_anchor,ncol=legend_ncol,framealpha=legend_alpha)
        ax.add_artist(legend1)
        fig.canvas.draw()
        f1 = legend1.get_frame()
        l1_w0_px, l1_h0_px = f1.get_width(), f1.get_height()
        l_w0_in, l_h0_in = l1_w0_px/fig.dpi, l1_h0_px/fig.dpi  # width and height of legend, in inches
    else:
        l_w0_in, l_h0_in = 0.0, 0.0
        if include_legend and legend_position not in custom_leg_pos_names: # use matplotlib default-style legend inside plot area
            ax.legend(loc=legend_position,ncol=legend_ncol,framealpha=legend_alpha)

    n_title_lines = 0
    if title_str.strip() != '':
        n_title_lines = 1 + title_str.count('\n')
    n_xlabel_lines = 0
    if x_label_str.strip() != '':
        n_xlabel_lines = 1 + x_label_str.count('\n')
    n_ylabel_lines = 0
    if y_label_str.strip() != '':
        n_ylabel_lines = 1 + y_label_str.count('\n')
    n_zlabel_lines = 1
    if z_label_str.strip() != '':
        n_zlabel_lines = 1 + z_label_str.count('\n')

    if plot_2D_map:
        # These values are good, do not change them.  (derived while working on SHAEDIT project)
        # INCORPORATE WIDTH OF COLORBAR AND ITS LABEL?
        x0bar = 0.60 + 0.200*n_ylabel_lines # inches, horizontal space needed for ylabel
        y0bar = 0.45 + 0.200*n_xlabel_lines # inches, vertical space needed for xticks/numbers, xlabel and any extra lines it has
        t0bar = 0.10 + 0.300*n_title_lines  # inches, vertical space needed for title
        del_l_in = 0.15               # inches, extra horizontal padding right of legend
    else:
        # These values are good, do not change them.  (derived while working on on this function specifically for 3D plotting)
        x0bar = 0.00 + 0.200*(n_zlabel_lines-1) # inches, horizontal space needed for ylabel
        y0bar = 0.45 + 0.200*max(n_xlabel_lines,n_ylabel_lines) # inches, vertical space needed for xticks/numbers, xlabel and any extra lines it has
        t0bar = 0.10 + 0.300*n_title_lines  # inches, vertical space needed for title
        del_l_in = 0.15               # inches, extra horizontal padding right of legend

    # adjust legend spacing depending on its position
    if legend_position=='outside right':
        l_h0_in = 0.0
    elif legend_position=='outside bottom':
        l_w0_in = 0.0

    # Plot window placement and sizing
    x0 = x0bar/fig_x_in                                      # distance from left edge that plot area begins
    y0 = y0bar/fig_y_in + (l_h0_in/fig_y_in)                 # distance from bottom edge that plot area begins
    h0 = 1 - (y0bar+t0bar)/fig_y_in - (l_h0_in/fig_y_in)     # height of plot area, set to be full height minus space needed for title, x-label, and potentially an outside bottom legend
    w0 = 1 - x0 - (l_w0_in/fig_x_in) - (del_l_in/fig_x_in)   # width of plot area, set to be full width minus space needed for y-label and potentially an outside right legend

    if man_sp_placement:
        x0 = spx0
        y0 = spy0
        h0 = sph0
        w0 = spw0

    # Set size and location of the plot on the canvas
    box = ax.get_position()
    # all vals in [0,1]: left, bottom, width, height
    if not man_sp_placement and (spnrows != 1 or spncols != 1):
        pstr  = 'Warning: It is highly encouraged that subplots be positioned manually.\n'
        pstr += '   This is done by setting man_sp_placement=True and then adjusting\n'
        pstr += '   the parameters spx0, spy0, sph0, and spw0 for each subplot.\n'
        pstr += '   The current plot was automatically sized by matplotlib.\n'
        print(pstr)
    else:
        ax.set_position([x0, y0, w0, h0])


    if plot_2D_map:

        ax.set_title(title_str,fontsize=fst)
        plt.xlabel(x_label_str,fontsize=fs)
        plt.ylabel(y_label_str,fontsize=fs)
        plt.xscale(x_scale)
        plt.yscale(y_scale)

        zoom_mult = 1.0
        x_log_buffer = 0.15*zoom_mult
        y_log_buffer = 0.2*zoom_mult
        min_x_decs = 2
        min_y_decs = 2

        x_scale='linear'
        if not x_limits:
            if x_scale == 'log': # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
                if (np.log10(x_max)-np.log10(x_min)+2*x_log_buffer) < min_x_decs:
                    x_log_buffer = 0.5*(min_x_decs - (np.log10(x_max)-np.log10(x_min)))
                plt.xlim([10**(np.log10(x_min)-x_log_buffer),10**(np.log10(x_max)+x_log_buffer)])
        else:
            plt.xlim(x_limits)

        if not y_limits:
            if y_scale == 'log': # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
                if (np.log10(y_max)-np.log10(y_min)+2*y_log_buffer) < min_y_decs:
                    y_log_buffer = 0.5*(min_y_decs - (np.log10(y_max)-np.log10(y_min)))
                plt.ylim([10**(np.log10(y_min)-y_log_buffer),10**(np.log10(y_max)+y_log_buffer)])
        else:
            plt.ylim(y_limits)

        if z_limits:
            if z_scale == 'log':
                zlogmin = None
                zlogmax = None
                if z_limits[0]: zlogmin=np.log10(z_limits[0])
                if z_limits[1]: zlogmax=np.log10(z_limits[1])
                pcm2d.set_clim(vmin=zlogmin, vmax=zlogmax)
            else:
                pcm2d.set_clim(vmin=z_limits[0], vmax=z_limits[1])

        def fmt(x, pos):
            a, b = '{:.2e}'.format(x).split('e')
            b = int(b)

            if z_scale=='log':
                return r'$10^{{{:g}}}$'.format(x)
            else:
                if b < -2 or b > 3:
                    return r'${:g} \times 10^{{{}}}$'.format(np.float(a), b)
                else:
                    return '{:g}'.format(x)

        divider = make_axes_locatable(ax)
        cbar_size_str = '{:g}'.format(cbar_size) + '%'
        cax = divider.append_axes("right", size=cbar_size_str, pad=cbar_pad)

        cbar = plt.colorbar(pcm2d, cax=cax, format=ticker.FuncFormatter(fmt))
        if cbar_fs==None:
            cbar_fs = fs
        cbar.set_label(z_label_str,fontsize=cbar_fs)
        #cbar.solids.set_rasterized(True)
        cbar.solids.set_edgecolor("face")
        #cbar.set_alpha(alpha_i)
        #cbar.draw_all()

        ax.set_position([x0, y0, w0, h0])

    else: # if 3D-plot
        ax.set_title(title_str,fontsize=fst)
        plt.xlabel(x_label_str,fontsize=fs)
        plt.ylabel(y_label_str,fontsize=fs)
        ax.set_zlabel(z_label_str,fontsize=fs)
        # Current matplotlib set_scale commands for log scale are borked completely beyond use, manually add log support
        #ax.set_xscale(x_scale)
        #ax.set_yscale(y_scale)
        #ax.set_zscale(z_scale)
        #plt.grid(b=True, which='major', linestyle='-', alpha=0.25) # doesn't affect 3D axis
        #plt.grid(b=True, which='minor', linestyle='-', alpha=0.10)
        # ensure at least minimum number of decades are present on a plot by increasing padding if necessary
        zoom_mult = 1.0
        x_log_buffer = 0.15*zoom_mult
        y_log_buffer = 0.2*zoom_mult
        z_log_buffer = 0.2*zoom_mult
        min_x_decs = 1
        min_y_decs = 1
        min_z_decs = 1

        manually_calculate_axis_bounds = not use_mpl_limits # if False, use default Matplotlib axis bounds; if True, use specially calculated axis bounds

        if not x_limits:
            if x_scale == 'log' and manually_calculate_axis_bounds: # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
                if ((x_max)-(x_min)+2*x_log_buffer) < min_x_decs:
                    x_log_buffer = 0.5*(min_x_decs - ((x_max)-(x_min)))
                ax.set_xlim([((x_min)-x_log_buffer),((x_max)+x_log_buffer)])
        else:
            if x_scale=='log':
                xlimsnew = []
                for limi in range(2):
                    if x_limits[limi]:
                        xlimsnew.append(np.log10(x_limits[limi]))
                    else:
                        xlimsnew.append(None)
                ax.set_xlim(xlimsnew)
            else:
                ax.set_xlim(x_limits)

        if not y_limits:
            if y_scale == 'log' and manually_calculate_axis_bounds: # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
                if ((y_max)-(y_min)+2*y_log_buffer) < min_y_decs:
                    y_log_buffer = 0.5*(min_y_decs - ((y_max)-(y_min)))
                ax.set_ylim([((y_min)-y_log_buffer),((y_max)+y_log_buffer)])
        else:
            if y_scale=='log':
                ylimsnew = []
                for limi in range(2):
                    if y_limits[limi]:
                        ylimsnew.append(np.log10(y_limits[limi]))
                    else:
                        ylimsnew.append(None)
                ax.set_ylim(ylimsnew)
            else:
                ax.set_ylim(y_limits)


        if not z_limits:
            if z_scale == 'log' and manually_calculate_axis_bounds: # use fancy code to determine bounds, otherwise, let matplotlib automatically generate boundaries
                if ((z_max)-(z_min)+2*z_log_buffer) < min_z_decs:
                    z_log_buffer = 0.5*(min_z_decs - ((z_max)-(z_min)))
                ax.set_zlim([((z_min)-z_log_buffer),((z_max)+z_log_buffer)])
        else:
            if z_scale=='log':
                zlimsnew = []
                for limi in range(2):
                    if z_limits[limi]:
                        zlimsnew.append(np.log10(z_limits[limi]))
                    else:
                        zlimsnew.append(None)
                ax.set_zlim(zlimsnew)
            else:
                ax.set_zlim(z_limits)

        act_xmin, act_xmax = ax.get_xlim()
        act_ymin, act_ymax = ax.get_ylim()
        act_zmin, act_zmax = ax.get_zlim()


        def round_up_to_nearest_multiple(val,mult=1):
            round_val = np.ceil(val/mult)*mult
            if isinstance(mult,int) or (abs(round_val)%1<0.01): round_val = int(round_val)
            return round_val

        def round_down_to_nearest_multiple(val,mult=1):
            round_val = np.floor(val/mult)*mult
            if isinstance(mult,int) or (abs(round_val)%1<0.01): round_val = int(round_val)
            return round_val

        def get_ints_between_2_vals(vmin,vmax):
            stepval = 1
            #vmini, vmaxi = int(np.ceil(vmin)),int(np.floor(vmax))
            if (vmax-vmin) <=1:
                stepval = 0.25
            elif (vmax-vmin) <=2:
                stepval = 0.5
            vmini = round_up_to_nearest_multiple(vmin,stepval)
            vmaxi = round_down_to_nearest_multiple(vmax,stepval)
            tick_list = list(np.arange(vmini,vmaxi+stepval,stepval))
            return tick_list

        def get_log_minor_ticks_between_bounds(vmin,vmax):
            minor_tick_list = []
            # get powers of min and max
            minpower = np.sign(vmin)*divmod(abs(vmin),1)[0] # integer portion of vmin
            maxpower = np.sign(vmax)*divmod(abs(vmax),1)[0] # integer portion of vmax
            # determine leading number in base 10
            min_lead_digit = divmod(((10**vmin)/(10**minpower)),1)[0] + 1
            max_lead_digit = divmod(((10**vmax)/(10**maxpower)),1)[0]
            cdigit = min_lead_digit
            cpower = minpower
            cval = cdigit*(10**cpower)
            maxval = max_lead_digit*(10**maxpower)
            while cval < maxval:
                minor_tick_list.append(np.log10(cval))
                cdigit += 1
                if cdigit == 10:
                    cdigit = 2
                    cpower += 1
                cval = cdigit*(10**cpower)
            return minor_tick_list


        def log_tick_formatter(vals_list):
            tstr_list = []
            for val in vals_list:
                tstr = r'10$^{{{:g}}}$'.format(val)
                tstr_list.append(tstr)
            return tstr_list

        if z_scale == 'log':
            zticks = get_ints_between_2_vals(act_zmin, act_zmax)
            ztick_labs = log_tick_formatter(zticks)
            ax.set_zticks(zticks)
            ax.set_zticklabels(ztick_labs)

        if y_scale == 'log':
            yticks = get_ints_between_2_vals(act_ymin, act_ymax)
            ytick_labs = log_tick_formatter(yticks)
            ax.set_yticks(yticks)
            ax.set_yticklabels(ytick_labs)

        if x_scale == 'log':
            xticks = get_ints_between_2_vals(act_xmin, act_xmax)
            xtick_labs = log_tick_formatter(xticks)
            ax.set_xticks(xticks)
            ax.set_xticklabels(xtick_labs)

        #ax.set_yticks(yticks+np.log10(np.array([2,3,4,5,8])).tolist())
        #yticks = yticks + np.log10(np.array([2,3,4,5,8])).tolist()


        grid_alpha = 0.25
        grid_alpha_minor = 0.05

        if x_scale == 'log':
            ax.xaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha_minor)
        else:
            ax.xaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha)
        if y_scale == 'log':
            ax.yaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha_minor)
        else:
            ax.yaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha)
        if z_scale == 'log':
            ax.zaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha_minor)
        else:
            ax.zaxis._axinfo["grid"]['color'] = (0,0,0,grid_alpha)


        if use_custom_3d_axis_class:
            # If log scale, add minor grid lines
            if x_scale == 'log':
                xticks_minor = get_log_minor_ticks_between_bounds(act_xmin, act_xmax)
                xgridlines = []
                for i in range(len(xticks)):
                    xgridlines.append((xticks[i],(0,0,0,grid_alpha)))
                for i in range(len(xticks_minor)):
                    xgridlines.append((xticks_minor[i],(1,1,1,grid_alpha_minor)))
                ax.set_xticks(xticks+xticks_minor)
                ax.xaxis.set_gridline_color(*xgridlines)
            if y_scale == 'log':
                yticks_minor = get_log_minor_ticks_between_bounds(act_ymin, act_ymax)
                ygridlines = []
                for i in range(len(yticks)):
                    ygridlines.append((yticks[i],(0,0,0,grid_alpha)))
                for i in range(len(yticks_minor)):
                    ygridlines.append((yticks_minor[i],(0,0,0,grid_alpha_minor)))
                ax.set_yticks(yticks+yticks_minor)
                ax.yaxis.set_gridline_color(*ygridlines)
            if z_scale == 'log':
                zticks_minor = get_log_minor_ticks_between_bounds(act_zmin, act_zmax)
                zgridlines = []
                for i in range(len(zticks)):
                    zgridlines.append((zticks[i],(0,0,0,grid_alpha)))
                for i in range(len(zticks_minor)):
                    zgridlines.append((zticks_minor[i],(0,0,0,grid_alpha_minor)))
                ax.set_zticks(zticks+zticks_minor)
                ax.zaxis.set_gridline_color(*zgridlines)


        # For some more info, see https://dawes.wordpress.com/2014/06/27/publication-ready-3d-figures-from-matplotlib/
        # Tick positioning
        [t.set_va('center') for t in ax.get_yticklabels()]
        [t.set_ha('center') for t in ax.get_yticklabels()]
        [t.set_va('center') for t in ax.get_xticklabels()]
        [t.set_ha('center') for t in ax.get_xticklabels()]
        [t.set_va('center') for t in ax.get_zticklabels()]
        [t.set_ha('center') for t in ax.get_zticklabels()]
        ''
        tick_infactor = 0.0
        tick_outfactor = 0.2

        # adjusts length of ticks on inside/outside of plot
        ax.xaxis._axinfo['tick']['inward_factor']  = tick_infactor
        ax.xaxis._axinfo['tick']['outward_factor'] = tick_outfactor
        ax.yaxis._axinfo['tick']['inward_factor']  = tick_infactor
        ax.yaxis._axinfo['tick']['outward_factor'] = tick_outfactor
        ax.zaxis._axinfo['tick']['inward_factor']  = tick_infactor
        ax.zaxis._axinfo['tick']['outward_factor'] = tick_outfactor

        # Background
        ax.xaxis.pane.set_edgecolor('black')
        ax.yaxis.pane.set_edgecolor('black')
        #ax.zaxis.pane.set_edgecolor('black')
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        #ax.view_init(elev=10, azim=135)


    return fig, ax


def fancy_save_plot(fig,dir_path=None,filename=None,extensions=['.png','.pdf'],facecolor=(0, 0, 0, 0),**savefig_kwargs):
    '''
    Description:
        Save a provided Matplotlib/Pyplot figure handle as an image file.

    Dependencies:
    
        - `import matplotlib.pyplot as plt`
        - `slugify()` function from Hunters_tools (if `filename=None`)

    Input:
       (required)
       
        - `fig` = Matplotlib/Pyplot figure handle (e.g., `fig, ax = plt.subplots()`)

    Inputs:
       (optional)
       
        - `dir_path` = (D=`None`) string or Path object denoting the path to the directory where image(s) are to 
               be saved; if `None`, the current working directory is used.
        - `filename` = (D=`None`) string denoting the filename of the plot image; if `None`, an attempt will be made
               to retrieve the title of the plot and use the `slugify()` version of it as the filename. 
               Failing that, the figure window's name will be used.  And failing that, it will simply be named "plot".
        - `extensions` = (D=`['.png','.pdf']`) a single string or list of strings of the file extension(s) for the figure to be saved as; 
               listed [here](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.filetypes)
               or using `plt.gcf().canvas.get_supported_filetypes()` you can see a list of options.
        - `facecolor` = (D=`(0, 0, 0, 0)`) `facecolor` argument of [`plt.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
        - `**savefig_kwargs` extra keyword arguments to be passed directly to [`plt.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
    Output:
        - (none)
    '''
    import matplotlib.pyplot as plt
    from pathlib import Path
    if isinstance(extensions, str): extensions = [extensions]
    if dir_path == None: dir_path = Path.cwd()
    if filename == None:
        filename = 'plot'
        try:
            filename = slugify(fig.axes[0].get_title())
        except:
            filename = slugify(fig.canvas.get_window_title())
    if filename.strip() == '': filename = 'plot'
    for ext in extensions:
        plot_filename = filename + ext  # or use fig.canvas.get_window_title()
        plot_save_path = Path.joinpath(dir_path, plot_filename)
        fig.savefig(plot_save_path, facecolor=facecolor,**savefig_kwargs)
    return




'''
**************************************************************************************************
----------------------------------- END OF DEFINED FUNCTIONS -------------------------------------
**************************************************************************************************
'''















debugging_table_generators = False
if debugging_table_generators:
    tab = [
            ['1',1.00,r'$\beta^-$',r'\texttt{B-} '],
            ['2','3.00',r'$IT$     ',r'\texttt{IT} '],
            ['3','n/a ',r'$(n,x)$  ',r'\texttt{nx} '],
            ['4','2.00',r'$\beta^+/e.c.$',r'\texttt{B+} '],
            ['5','4.00',r'$\alpha$',r'\texttt{\char32 a} '],
            ['6','5.00',r'$n$',r'\texttt{\char32 n} '],
            ['7','6.00',r'$s.f.$',r'\texttt{sf} '],
            ['8','--',r'$other$',r'\texttt{or} ']]

    col_heads = ['a','b']
    col_head_span = [2,2]
    row_heads = [['o','t','f','s'],['a','b','c']]
    row_head_span = [2,[3,3,2]]
    #print(np.shape(tab))
    y = Latex_table_generator(tab,row_headers=row_heads,row_header_spans=row_head_span,column_headers=col_heads,column_header_spans=col_head_span,title='test',
                              hline_row_indices=6,cline_row_cstart_cend_indices_triplets=[[2,1,1],[3,2,2],[4,1,1]])
    #x = Excel_table_generator(y)
    print(y)


debugging_fancy_3d_plot = False
if debugging_fancy_3d_plot:
    figi = 0

    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z1 = np.linspace(-2, 2, 100)
    r1 = z1**2 + 1

    xdata_lists = [ np.linspace(0,2*np.pi,50)+1,np.linspace(0,2*np.pi,50)+1,np.linspace(0,2*np.pi,20)+1,np.linspace(0,2*np.pi,20)+1,np.linspace(0,2*np.pi,20)+1,np.linspace(0,2*np.pi,20)+1,np.linspace(0,2*np.pi,20)+1]
    ydata_lists = [ np.linspace(2,100,50),np.linspace(2,100,50),100*(np.cos(xdata_lists[2]-1)+1),100*(np.cos(xdata_lists[2]-1)+1),100*(np.cos(xdata_lists[2]-1)+1),100*(np.cos(xdata_lists[2]-1)+1),100*(np.cos(xdata_lists[2]-1)+1)]
    X, Y =  np.meshgrid(xdata_lists[2], ydata_lists[2])
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    multx=1.3
    zdata_lists = [np.exp(xdata_lists[0])/7, np.exp(xdata_lists[1])/4, 20*(Z+1.1), 20*(Z+1.1)+50*multx, 20*(Z+1.1)+100*multx, 20*(Z+1.1)+150*multx , 20*(Z+1.1)+200*multx ]


    pls=['scatter', 'line', 'surface','trisurface','filledcontour','contour','wireframe']

    # include only some plots
    incli = [ 0   ,  1    ,    2     ,    3       ,      4        ,    5    ,    6      ]
    #incli = [ 2 ]
    xdata_lists = [xdata_lists[i] for i in incli]
    ydata_lists = [ydata_lists[i] for i in incli]
    zdata_lists = [zdata_lists[i] for i in incli]
    pls         = [pls[i]         for i in incli]

    labs = pls

    xlims = [1e0,1e1]
    ylims = [1e0,1e3]
    zlims = [1e0,1e3]

    fancy_3D_plot(
            # REQUIRED INPUTS
                xdata_lists,                    # a list containing lists/arrays of 1-D x data (or single list of xdata applied to all zdata in z_data_lists)
                ydata_lists,                    # a list containing lists/arrays of 1-D y data (or single list of ydata applied to all zdata in z_data_lists)
                zdata_lists,                    # a list containing lists/arrays of z datasets (or a single list/array), individual entries are either 1-D lists or 2-D NumPy arrays

            # OPTIONAL (basic) KEYWORD ARGUMENTS (for all plot styles)
                plot_styles=pls,                # list of (or individual) strings denoting the plot style to be used for each dataset. valid options for 1/2-D z-data = ['line','scatter','trisurface']/['surface','wireframe','trisurface','contour','filledcontour']
                data_labels=labs,                 # a list of strings to be used as data labels in the legend
                figi=figi,                      # figi = figure index (D=1)
                #title_str=title_str,            # title_str = string to be used as the title of the plot (D='title')
                #x_label_str=x_label_str,        # x_label_str = string to be used as x-axis title (D='x-axis')
                #y_label_str=y_label_str,        # y_label_str = string to be used as y-axis title (D='y-axis')
                x_limits=xlims,                 # x_limits = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=[], auto-calculated based on x_data_lists)
                y_limits=ylims,                 # y_limits = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=[], auto-calculated based on y_data_lists)
                z_limits=zlims,                 # z_limits = length 2 list specifying minimum and maximum z-axis bounds [zmin,zmax] (D=[], auto-calculated based on z_data_lists)
                use_mpl_limits=True,           # use_mpl_limits = use Matplotlib axis limits (True) or specially calculated limits (False) for log scale when limits aren't specified
                title_fs=16,                    # title_fs = title font size (D=16)
                axis_fs=14,                     # axis_fs = axis label font size (D=14)
                f_family='sans-serif',          # f_family = string specifying font family (D='sans-serif'); options include: ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
                f_style='normal',               # f_style = string specifying font style (D='normal'); options include: ['normal', 'italic', 'oblique']
                f_variant='normal',             # f_variant = string specifying font variant (D='normal'); options include: ['normal', 'small-caps']
                f_weight='normal',              # f_weight = string specifying font weight (D='normal'); options include: ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
                fig_width_inch=8.0,             # fig_width_inch = figure width in inches (D=9.5)
                fig_height_inch=6.25,           # fig_height_inch = figure height in inches (D=6.5)

                x_scale='log',               # x_scale = x-axis scale, either "linear", "log", "symlog", or "logit" (D='linear')
                y_scale='log',               # y_scale = y-axis scale, either "linear", "log", "symlog", or "logit" (D='linear')
                z_scale='log',               # z_scale = z-axis scale, either "linear", "log", "symlog", or "logit" (D='linear')

            # OPTIONAL (basic) KEYWORD ARGUMENTS (for specific plot styles)
                #color=plotting_colors_list,     # color = list of color strings to be used of same length as y_data_lists (or individual color string) (D='#FDFEFC', results in Matplotlib default color cycle)
                #linestyle='--',                   # line style, choose from: '', '-', '--', '-.', or ':' (D='')
                #linewidth=5,                    # line width (D=1)
                marker='o',                     # marker style (D='.'), choose from those listed at https://matplotlib.org/3.1.0/api/markers_api.html
                markersize=5,                   # marker size (D=5)
                markerfacecolor='g',
                markeredgecolor='r',
                markeredgewidth=2,
                alpha = 0.5,

                #OoB_z_handling = None, #'limits',

            # OPTIONAL (advanced) KEYWORD ARGUMENTS
                fig = None,                      # figure handles from existing figure to draw on (D=None, fig=None should always be used for initial subplot unless a figure canvas has already been generated)
                ax = None,                       # axis handles from an existing figure to draw on (D=None, ax=None should always be used for initial subplot)
                spnrows=1,                       # number of rows in final subplot (D=1)
                spncols=1,                       # number of columns in final subplot (D=1)
                spindex=1,                       # index of current subplot (between 1 and spnrows*spncols) (D=1)
                man_sp_placement = False,        # logical variable controlling manual sizing/placement of subplots using below variables (D=False, use automatic sizing)
                spx0=0.1,                        # distance from canvas left edge where this plotting area should begin (D=0.1), generally a number around 0~1
                spy0=0.5,                        # distance from canvas bottom edge where this plotting area should begin (D=0.1), generally a number around 0~1
                sph0=0.4,                        # width of this plotting area on the canvas (D=0.4), generally a number around 0~1
                spw0=0.8                         # height of this plotting area on the canvas (D=0.4), generally a number around 0~1

                  )






    plt.show()






debugging_fancy_plot = False
if debugging_fancy_plot:

    # For the sake of convenience, the fancy_plot function being called with all options listed and described is included here.
    # This can be easily copy/pasted into other scripts and retooled for the specific application at hand.

    xdata_lists = [np.linspace(0,2*np.pi,50),np.linspace(0,2*np.pi,40)]
    ydata_lists = [np.sin(xdata_lists[0]), np.cos(xdata_lists[1]) ]
    data_labels = ['sine','cosine']
    figi = 1
    title_str = 'demo of fancy_plot'
    x_label_str = 'x-axis label'
    y_label_str = 'y-axis label'

    yerr_lists = [0.05*np.sin(xdata_lists[0]), 0.2*np.cos(xdata_lists[1]) ]

    rand_err = 0.5*np.random.rand(40)
    xerboxl = [[],rand_err*xdata_lists[1]]
    xerboxr = [[],rand_err*xdata_lists[1]]
    yerboxl = [[],rand_err*ydata_lists[1]]
    yerboxu = [[],rand_err*ydata_lists[1]]


    d1 = {'xdata':np.array([1,2,3,4]),'ydata':np.array([-1,0,0.5,0.25]),'alpha':1.0}
    d2 = {'xdata':[1,2,3,4],'ydata':[-0.5,-0.75,-0.5,0],'markersize':15}
    dictionaries = [d1, d2]

    #xdata_lists, ydata_lists = None, None

    fig, ax = fancy_plot(
                    # REQUIRED INPUTS
                         xdata_lists,                    # a list containing lists/arrays of x data (or single list of xdata applied to all ydata in y_data_lists)
                         ydata_lists,                    # a list containing lists/arrays of y data (or single list of ydata)

                    # DICTIONARIES
                         dictionaries = dictionaries,

                    # OPTIONAL (basic) KEYWORD ARGUMENTS
                         data_labels=[],        # a list of strings to be used as data labels in the legend
                         #xerr_lists=xerr_lists,          # xerr_lists = a list containing lists/arrays of x data absolute uncertainties (or single list of xdata errors applied to all ydata in y_data_lists) (D=[[]], No error)
                         yerr_lists=yerr_lists,          # yerr_lists = a list containing lists/arrays of y data absolute uncertainties (or single list of ydata errors) (D=[[]], No error)
                         figi=figi,                      # figi = figure index (D=1)
                         title_str=title_str,            # title_str = string to be used as the title of the plot (D='title')
                         x_label_str=x_label_str,        # x_label_str = string to be used as x-axis title (D='x-axis')
                         y_label_str=y_label_str,        # y_label_str = string to be used as y-axis title (D='y-axis')
                         #x_limits=xlims,                 # x_limits = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=[], auto-calculated based on x_data_lists)
                         #y_limits=ylims,                 # y_limits = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=[], auto-calculated based on y_data_lists)
                         title_fs=16,                    # title_fs = title font size (D=16)
                         axis_fs=14,                     # axis_fs = axis label font size (D=14)
                         f_family='sans-serif',          # f_family = string specifying font family (D='sans-serif'); options include: ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
                         f_style='normal',               # f_style = string specifying font style (D='normal'); options include: ['normal', 'italic', 'oblique']
                         f_variant='normal',             # f_variant = string specifying font variant (D='normal'); options include: ['normal', 'small-caps']
                         f_weight='normal',              # f_weight = string specifying font weight (D='normal'); options include: ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
                         fig_width_inch=5.0,             # fig_width_inch = figure width in inches (D=9.5)
                         fig_height_inch=4.25,           # fig_height_inch = figure height in inches (D=6.5)

                         x_scale='linear',                  # x_scale = x-axis scale, either "linear", "log", "symlog", or "logit" (D='log')
                         y_scale='linear',                  # y_scale = y-axis scale, either "linear", "log", "symlog", or "logit" (D='log')
                         #color=plotting_colors_list,     # color = list of color strings to be used of same length as y_data_lists (or individual color string) (D='#FDFEFC', results in Matplotlib default color cycle)
                         alpha=0.1,                        # alpha = list of (or individual) alpha values (D=1.0)
                         linestyle='',                   # line style, choose from: '', '-', '--', '-.', or ':' (D='')
                         linewidth=1,                    # line width (D=1)
                         marker=['.','o'],                     # marker style (D='.'), choose from those listed at https://matplotlib.org/3.1.0/api/markers_api.html
                         markersize=5,                   # marker size (D=5)
                         markerfacecolor=['k','g'],
                         markeredgecolor=None,
                         markeredgewidth=None,
                         errorstyle = 'bar-band',        # list of (or individual) strings specifying how y-error is represented (D='bar-band', ['bar-band','bar','band']
                         error_band_opacity = 0.15,      # list of (or individual) int/float of error band opacities (D=0.15)
                         elinewidth=None,                # error bar line width (D=None, use linewidth value)
                         capsize=None,                   # error bar cap width (D=None)

                    # OPTIONAL (advanced) KEYWORD ARGUMENTS
                         legend_position='outside bottom',# legend_position = placement of legend using a default matplotlib string ('best','upper right','lower left',etc.) inside plot area or outside using 'outside right' or 'outside bottom' (D='outside right')
                         legend_anchor = None,           # legend_anchor = legend anchor position (D=(1.0,0.75) if outside right, (0.5,-0.17) if outside bottom), only used for 'outside' legend positions
                         legend_ncol = 1,                # legend_ncol = number of columns in legend (D=1) (if 'outside bottom' position, ncol=1 causes the function to default to ncol=len(data_labels) instead)
                         legend_alpha = None,             # legend_alpha = alpha of legend background

                         #errorbox_xdata_l = xerboxl,     # a list containing lists/arrays of errorbox left widths from center (x-data lower error)
                         #errorbox_xdata_r = xerboxr,     # a list containing lists/arrays of errorbox right widths from center (x-data upper error)
                         #errorbox_ydata_l = yerboxl,     # a list containing lists/arrays of errorbox lower heights from center (y-data lower error)
                         #errorbox_ydata_u = yerboxu,     # a list containing lists/arrays of errorbox upper heights from center (y-data upper error)
                         #errorbox_fc = 'k',              # errorbox_fc = error box face color (D='k')
                         #errorbox_fa = 0.1,              # errorbox_fa = error box face alpha (D=0.1)
                         #errorbox_ec = 'k',              # errorbox_ec = error box edge color (D='k', black)
                         #errorbox_ea = 1.0,              # errorbox_ea = error box edge alpha (D=0.1)
                         #errorbox_ew = 0.5               # errorbox_ew = error box edge width (D=0.5)

                         fig = None,                      # figure handles from existing figure to draw on (D=None, fig=None should always be used for initial subplot unless a figure canvas has already been generated)
                         ax = None,                       # axis handles from an existing figure to draw on (D=None, ax=None should always be used for initial subplot)
                         spnrows=1,                       # number of rows in final subplot (D=1)
                         spncols=1,                       # number of columns in final subplot (D=1)
                         spindex=1,                       # index of current subplot (between 1 and spnrows*spncols) (D=1)
                         man_sp_placement = False,        # logical variable controlling manual sizing/placement of subplots using below variables (D=False, use automatic sizing)
                         spx0=0.1,                        # distance from canvas left edge where this plotting area should begin (D=0.1), generally a number around 0~1
                         spy0=0.5,                        # distance from canvas bottom edge where this plotting area should begin (D=0.1), generally a number around 0~1
                         sph0=0.4,                        # width of this plotting area on the canvas (D=0.4), generally a number around 0~1
                         spw0=0.8                         # height of this plotting area on the canvas (D=0.4), generally a number around 0~1

                         )


'''
fig, ax = fancy_plot(
                # REQUIRED INPUTS
                     xdata_lists,                    # a list containing lists/arrays of x data (or single list of xdata applied to all ydata in y_data_lists)
                     ydata_lists,                    # a list containing lists/arrays of y data (or single list of ydata)
                
                # OPTIONAL (basic) KEYWORD ARGUMENTS
                     data_labels=data_labels,        # a list of strings to be used as data labels in the legend
                     #xerr_lists=xerr_lists,          # xerr_lists = a list containing lists/arrays of x data absolute uncertainties (or single list of xdata errors applied to all ydata in y_data_lists) (D=[[]], No error)
                     yerr_lists=yerr_lists,          # yerr_lists = a list containing lists/arrays of y data absolute uncertainties (or single list of ydata errors) (D=[[]], No error)
                     figi=figi,                      # figi = figure index (D=1)
                     title_str=' ',            # title_str = string to be used as the title of the plot (D='title')
                     x_label_str='x_label_str',        # x_label_str = string to be used as x-axis title (D='x-axis')
                     y_label_str=y_label_str,        # y_label_str = string to be used as y-axis title (D='y-axis')
                     #x_limits=xlims,                 # x_limits = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=[], auto-calculated based on x_data_lists)
                     #y_limits=ylims,                 # y_limits = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=[], auto-calculated based on y_data_lists)
                     title_fs=16,                    # title_fs = title font size (D=16)
                     axis_fs=14,                     # axis_fs = axis label font size (D=14)
                     fig_width_inch=5.0,             # fig_width_inch = figure width in inches (D=9.5)
                     fig_height_inch=4.25,           # fig_height_inch = figure height in inches (D=6.5)
                     
                     x_scale='linear',                  # x_scale = x-axis scale, either "linear", "log", "symlog", or "logit" (D='log')
                     y_scale='linear',                  # y_scale = y-axis scale, either "linear", "log", "symlog", or "logit" (D='log')
                     #color=plotting_colors_list,     # color = list of color strings to be used of same length as y_data_lists (or individual color string) (D='#FDFEFC', results in Matplotlib default color cycle)
                     linestyle='',                   # line style, choose from: '', '-', '--', '-.', or ':' (D='')
                     linewidth=1,                    # line width (D=1)
                     marker='.',                     # marker style (D='.'), choose from those listed at https://matplotlib.org/3.1.0/api/markers_api.html
                     markersize=5,                   # marker size (D=5)
                     elinewidth=None,                # error bar line width (D=None, use linewidth value)
                     capsize=None,                   # error bar cap width (D=None)
                
                # OPTIONAL (advanced) KEYWORD ARGUMENTS
                     legend_position='upper right',# legend_position = placement of legend using a default matplotlib string ('best','upper right','lower left',etc.) inside plot area or outside using 'outside right' or 'outside bottom' (D='outside right')
                     legend_anchor = None,           # legend_anchor = legend anchor position (D=(1.0,0.75) if outside right, (0.5,-0.17) if outside bottom), only used for 'outside' legend positions
                     legend_ncol = 1,                # legend_ncol = number of columns in legend (D=1) (if 'outside bottom' position, ncol=1 causes the function to default to ncol=len(data_labels) instead)
                     legend_alpha = None,             # legend_alpha = alpha of legend background
                     
                     #errorbox_xdata_l = xerboxl,     # a list containing lists/arrays of errorbox left widths from center (x-data lower error)
                     #errorbox_xdata_r = xerboxr,     # a list containing lists/arrays of errorbox right widths from center (x-data upper error) 
                     #errorbox_ydata_l = yerboxl,     # a list containing lists/arrays of errorbox lower heights from center (y-data lower error)
                     #errorbox_ydata_u = yerboxu,     # a list containing lists/arrays of errorbox upper heights from center (y-data upper error)
                     #errorbox_fc = 'k',              # errorbox_fc = error box face color (D='k')
                     #errorbox_fa = 0.1,              # errorbox_fa = error box face alpha (D=0.1)
                     #errorbox_ec = 'k',              # errorbox_ec = error box edge color (D='k', black)
                     #errorbox_ea = 1.0,              # errorbox_ea = error box edge alpha (D=0.1)
                     #errorbox_ew = 0.5               # errorbox_ew = error box edge width (D=0.5)
                     
                     fig = fig,
                     ax = ax,
                     spnrows=2, 
                     spncols=1, 
                     spindex=2,
                     man_sp_placement = False,
                     spx0=0.1, 
                     spy0=0.1, 
                     sph0=0.4, 
                     spw0=0.8
                     
                     )
'''

'''
      - errorbox_xdata_l = a list containing lists/arrays of errorbox left widths from center (x-data lower error)  
      - errorbox_xdata_r = a list containing lists/arrays of errorbox right widths from center (x-data upper error) 
      - errorbox_ydata_l = a list containing lists/arrays of errorbox lower heights from center (y-data lower error)
      - errorbox_ydata_u = a list containing lists/arrays of errorbox upper heights from center (y-data upper error)
      *** Error boxes will only be drawn if at least one x list and one y list of the four above arrays is specified; unspecified lists will default to zero error
      - errorbox_fc = error box face color (D='k')
      - errorbox_fa = error box face alpha (D=0.1)
      - errorbox_ec = error box edge color (D='k', black)
      - errorbox_ew = error box edge width (D=0.5)
      - errorbox_ea = error box edge alpha (D=0.1)
'''








if debugging_fancy_plot or debugging_fancy_3d_plot:
    plt.show()
