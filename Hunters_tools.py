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

### Science/Engineering Functions 

- `time_str_to_sec_multiplier`      : determine multiplier to convert a time unit to seconds
- `seconds_to_dhms`                 : convert a time in seconds to a string of human-relatable time units
- `seconds_to_ydhms`                : convert a time in seconds to a string of human-relatable time units (also with years)
- `SI_prefix_converter`             : returns a multiplier to convert from one SI prefix to another
- `Element_Z_to_Sym`                : returns elemental symbol provided the atomic number Z
- `Element_Sym_to_Z`                : returns an atomic number Z provided the elemental symbol
- `Element_ZorSym_to_name`          : returns a string of the name of an element provided its atomic number Z or symbol
- `Element_ZorSym_to_mass`          : returns the average atomic mass of an element provided its atomic number Z or symbol
- `nuclide_to_Latex_form`           : form a LaTeX-formatted string of a nuclide provided its information
- `nuclide_plain_str_to_latex_str`  : convert a plaintext string for a nuclide to a LaTeX formatted raw string
- `nuclide_plain_str_ZZZAAAM`       : convert a plaintext string for a nuclide to an integer ZZZAAAM value
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
- `rebinner`                        : rebin a set of y-data to a new x-binning structure (edges not necessarily preserved)
- `calc_GCR_intensity`              : calculate GCR intensity for a provided solar modulation, ion, and energy
- `assemble_GCR_flux`               : assemble GCR spectra for desired elements/ions
- `ICRP116_effective_dose_coeff`    : returns effective dose of a mono-energetic particle of some species and some geometry
- `fetch_MC_material`               : returns a string of a formatted material for MCNP or PHITS


### Plotting-related Functions 

- `generate_line_bar_coordinates`   : convert a set of bin-wise data to line coordinates to plot normally looking like bars
- `colors_list_6`                   : return 1 of 6 color values from ColorBrewer
- `colors_list_12`                  : return 1 of 12 color values from ColorBrewer
- `colors_list_10`                  : return 1 of 10 color values from the new matplotlib default from v3 1 1
- `get_colormap`                    : retrieve a matplotlib colormap using just its string name
- `truncate_colormap`               : truncate a colormap to new upper/lower bounds to a subset of the original colormap
- `makeErrorBoxes`                  : draw uncertainties as a box surrounding a point (can be used with/instead of crosshair-style error bars)
- `fancy_plot`                      : very comprehensive plotter for 2D datasets, an accumulation of all of my past plotting commands/settings
- `fancy_3D_plot`                   : very comprehensive plotter for 3D datasets on 3D axes, an accumulation of all of my past plotting commands/settings

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
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mticker
from matplotlib import cm
from scipy.interpolate import CubicSpline, lagrange, interp1d

from mpl_toolkits.mplot3d.axis3d import Axis
import matplotlib.projections as proj
from matplotlib.colors import colorConverter, LinearSegmentedColormap
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable


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
        
        if color_min_val==None: col_min_val = np.min(color_val_table)
        if color_max_val==None: col_max_val = np.max(color_val_table)
        
        color_val_table[color_val_table<col_min_val] = col_min_val
        color_val_table[color_val_table>col_max_val] = col_max_val
        
        if color_scale=='log':
            if np.any(color_val_table<0):
                print('Warning: col_min_val<0 & core_table contains negative values and thus cannot be color scaled logarithmically; reverting to linear color scale.')
            else:
                if np.any(color_val_table==0):
                    print('Warning: core_table contains zero values; they will be ignored while assigning colors.')
                color_val_table[color_val_table==0] = np.NaN # set to NaN and use this as a flag to ignore later
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

def nuclide_plain_str_ZZZAAAM(nuc_str):
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


'''
**************************************************************************************************
----------------------------------- PLOTTING-RELATED FUNCTIONS -----------------------------------
**************************************************************************************************
'''


def generate_line_bar_coordinates(xbins,yvals):
    """
    Description:
        Converts a set of bin boundaries and bin contents to coordinates mapping a bar plot if drawn with a line
    
    Inputs:
      - `xbins` = list of length N+1 bin boundary values
      - `yvals` = list of length N bin content values 
    
    Outputs:
      - `newx` = list of length 2N + 2 of x-coordinates mapping a 'bar plot' of the input histogram data
      - `newy` = list of length 2N + 2 of y-coordinates mapping a 'bar plot' of the input histogram data
    """
    if len(yvals) != (len(xbins)-1):
        pstr = 'xbins should be a list of bin edges of length one more than yvals, the values associated with the contents of each bin' + '\n'
        pstr += 'provided input arrays had lengths of {} for xbins and {} for yvals'.format(str(len(xbins)),str(len(yvals)))
        print(pstr)
        return 0
    newx = [xbins[0],xbins[0]]
    newy = [0,yvals[0]]
    for i in range(len(xbins)-2):
        newx.append(xbins[i+1])
        newx.append(xbins[i+1])
        newy.append(yvals[i])
        newy.append(yvals[i+1])
    newx.append(xbins[-1])
    newx.append(xbins[-1])
    newy.append(yvals[-1])
    newy.append(0)
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
            
            if all([x == None for x in data_labels]):
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
    ax = plt.subplot(spnrows, spncols, spindex)
        
    for i in range(nds):
        xdata = xdata_lists[i]
        ydata = np.array(ydata_lists[i])
        xerr=None 
        yerr=None 
        xerr_present = False 
        yerr_present = False
        if len(xerr_lists[0])>0:
            xerr = xerr_lists[i]
            if sum(xerr)==0: 
                xerr = None
            else:
                xerr_present = True
        if len(yerr_lists[0])>0:
            yerr = yerr_lists[i]
            if sum(yerr)==0: 
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
            
        if (ers=='bar-band' or ers=='band') and yerr_present:
            if color=='#FDFEFC' or color[0]=='#FDFEFC': # assume user will never actually want/input this specific white color
                c = p[0].get_color() # need to grab whatever color was just used
            ax.fill_between(xdata, np.array(ydata)-np.array(yerr), np.array(ydata)+np.array(yerr),color=c,alpha=ebo)
            
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
    fig.canvas.set_window_title(window_title)
    
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
    
    
    plt.title(title_str,fontsize=fst)
    plt.xlabel(x_label_str,fontsize=fs)
    plt.ylabel(y_label_str,fontsize=fs)
    plt.xscale(x_scale)
    plt.yscale(y_scale)
    plt.grid(b=True, which='major', linestyle='-', alpha=0.25)
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.10)
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
    
    
    use_custom_3d_axis_class = True
    
    
    
    
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
            if x_limits[0]: xvals[xvals<x_limits[0]] = np.NaN
            if x_limits[1]: xvals[xvals>x_limits[1]] = np.NaN
        if y_limits:
            if y_limits[0]: yvals[yvals<y_limits[0]] = np.NaN
            if y_limits[1]: yvals[yvals>y_limits[1]] = np.NaN
        if z_limits:
            if OoB_z_handling=='NaN':
                if z_limits[0]: zvals[zvals<z_limits[0]] = np.NaN
                if z_limits[1]: zvals[zvals>z_limits[1]] = np.NaN
            elif OoB_z_handling=='limits':
                if z_limits[0]: zvals[zvals<z_limits[0]] = z_limits[0]
                if z_limits[1]: zvals[zvals>z_limits[1]] = z_limits[1]
        
        
        if z_scale == 'log':
            zvals[(zvals<=0)] = np.NaN
            zvals = np.log10(zvals)
        if y_scale == 'log':
            yvals[yvals<=0] = np.NaN
            yvals = np.log10(yvals)
        if x_scale == 'log':
            xvals[xvals<=0] = np.NaN
            xvals = np.log10(xvals)
               
        if len(yvals) != 0:
            if len(yvals[np.nonzero(yvals)]) != 0:
                if min(yvals[np.nonzero(yvals)])<y_min: y_min = min(yvals[np.nonzero(yvals)])
                #if min(yvals)<y_min: y_min = min(yvals)
                if max(yvals)>y_max: y_max = max(yvals)
                if min(xvals)<x_min: x_min = min(xvals)
                if max(xvals)>x_max: x_max = max(xvals)
                if np.min(zvals)<z_min: z_min = np.min(zvals)
                if np.max(zvals)>z_max: z_max = np.max(zvals)
        
        
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
                ax.plot(xvals,yvals,zvals,label=label_str,
                        color=c,linestyle=ls,linewidth=lw,alpha=alpha_i,
                        marker=mkr,markersize=mks,markerfacecolor=mfc,markeredgecolor=mec,markeredgewidth=mew)
            
            # scatter
            elif pls=='scatter':
                if not c: c = mfc # if no color defined, check to see if marker face color was defined
                ax.scatter(xvals,yvals,zvals,label=label_str,
                           color=c,depthshade=depthshade_i,alpha=alpha_i,
                           marker=mkr,s=mks**2,linewidths=mew,edgecolors=mec)
            
            # trisurface
            elif pls=='trisurface':
                if cmp != None: 
                    c = None
                if facecolors != None:
                    c = None
                    cmap = None
                ps1 = ax.plot_trisurf(xvals,yvals,zvals,label=label_str,
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
                ps1 = ax.plot_surface(xvals,yvals, zvals.T,label=label_str,
                                color=c,cmap=cmp,facecolors=facecolors_i,alpha=alpha_i,
                                rcount=rcount_i,ccount=ccount_i,
                                antialiased=False)
                ps1._facecolors2d=ps1._facecolors3d
                ps1._edgecolors2d=ps1._edgecolors3d
            
            # wireframe
            elif pls=='wireframe':
                ax.plot_wireframe(xvals,yvals, zvals.T,label=label_str,
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
                
                ps1 = ax.plot_trisurf(xvals,yvals,ztri,label=label_str,
                                color=c,cmap=cmp,facecolors=facecolors_i,alpha=alpha_i)
                ps1._facecolors2d=ps1._facecolors3d
                ps1._edgecolors2d=ps1._edgecolors3d
            
            # contour
            elif pls=='contour':
                if cmp != None: c = None
                ax.contour(xvals,yvals, zvals.T,
                           colors=c,cmap=cmp,linestyles=ls,linewidths=lw,alpha=alpha_i) 
                
            # filled contour
            elif pls=='filledcontour':
                if cmp != None: c = None
                ax.contourf(xvals,yvals, zvals.T,
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
                    
                pcm2d = ax.pcolormesh(xvals,yvals, zvals.T,
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
                        print(yvals)
                    
                if pls=='map_contour':
                    pcm2d = ax.contour(xvals,yvals, zvals.T,
                                cmap=cmp,linestyles=ls,alpha=alpha_i)
                else:
                    pcm2d = ax.contourf(xvals,yvals, zvals.T,
                                cmap=cmp,linestyles=ls,alpha=alpha_i)
            
            else:
                print('Encountered incompatability with plot style {} and data dimensionality {} for data index {}.  Aborting.'.format(pls,str(nzdims[i]),str(i))) 
            
        
    
    if title_str.strip() != '':
        window_title = slugify(title_str) # "comparison_fig"
    else:
        window_title = 'Figure ' + str(figi)
    #window_title = window_title.replace('b','',1) # remove leading 'b' character from slugify process
    fig.canvas.set_window_title(window_title)
    
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
                #x_limits=xlims,                 # x_limits = length 2 list specifying minimum and maximum x-axis bounds [xmin,xmax] (D=[], auto-calculated based on x_data_lists)
                #y_limits=ylims,                 # y_limits = length 2 list specifying minimum and maximum y-axis bounds [ymin,ymax] (D=[], auto-calculated based on y_data_lists)
                #z_limits=zlims,                 # z_limits = length 2 list specifying minimum and maximum z-axis bounds [zmin,zmax] (D=[], auto-calculated based on z_data_lists)
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