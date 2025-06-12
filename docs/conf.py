"""
Configuration file for the overall book - Designing Actuarial Packages in Python and R.
"""
import sys
sys.path.append('..')
from actpak.constants import BUILD_VERSION

project: str = 'actpak'
copyright: str = '2025' # noqa
author: str = 'Gene Dan'

version = BUILD_VERSION

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None