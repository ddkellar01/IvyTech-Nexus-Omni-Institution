import sys
import os

# Automatically inject repository root into sys.path for pytest
repo_root = os.path.abspath(os.path.dirname(__file__))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)
