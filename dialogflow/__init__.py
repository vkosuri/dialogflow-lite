"""
API Ai python requests package
"""
import sys

if 'install' not in sys.argv and 'egg_info' not in sys.argv:
    from .dialogflow import Dialogflow

__version__ = '0.0.4'
__author__ = 'Mallikarjunarao Kosuri'
__email__ = 'malli.kv2@gmail.com'

