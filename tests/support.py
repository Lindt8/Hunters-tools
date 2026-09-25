"""Select a headless backend before importing the toolkit."""

import atexit
import os
from pathlib import Path
import tempfile

# Keep disposable Matplotlib configuration inside the project, not in ~/.matplotlib.
_config = tempfile.TemporaryDirectory(prefix='.runtime-', dir=Path(__file__).parent)
atexit.register(_config.cleanup)
os.environ['MPLCONFIGDIR'] = _config.name

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import Hunters_tools as ht
