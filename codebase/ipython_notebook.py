
###########################################################
### Settings
###########################################################

# Print all statements rather than just the last one
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# High-resolution plot output for retina displays
%config InlineBackend.figure_format ='retina'

# Print entire table

pd.set_option('display.max_columns', None)
pd.reset_option(“max_columns”)

pd.set_option(“max_colwidth”, None)

pd.set_option("max_rows", None)

pd.set_option(‘precision’, 2)


# Black auto formatting
%load_ext lab_blacker

# Figure settings
sns.set_style('darkgrid')
sns.mpl.rcParams['figure.figsize'] = (10.0, 6.0)


###########################################################
### Cool stuff
###########################################################

# Execute shell commands
!conda list | grep pandas

# Use wildcards to find objects in namespace
*df*?

# Use cached input and output values
In[101], Out[101]

# Syntactic sugar for glob
notebooks = !ls * fgu*
notebooks

# (Then) shell out to subcommand (e.g. execute file from inside notebook)
!echo {notebooks[1]}

# Time function calls as they happen with tqdm
#Replace .map() by .progress_map(), same for .apply() and .applymap()

from tqdm import tqdm_notebook
tqdm_notebook().pandas()

data['column_1'].progress_map(lambda x: x.count('e'))


###########################################################
### Magic functions
###########################################################

# Info and brief info about magic function
%magic
%magic - brief

# Debugging (instead of putting print statement throughout code)
%debug
%pdb

# Install package using conda from current kernel
%conda install < packagename >

# Run different notebook from within notebook
%run <path_to_notebook/name_of_notebook>

# Write code to python file / read code from python file
%%writefile pythoncode.py
%pycat pythoncode.py

# All objects in namespace displayed and as a list
%who
%who_ls

# Run c or something else inside notebook
%% cc



# Time cell
%% timeit   # Average of 100,000 runs
%% time     # Time of single run
