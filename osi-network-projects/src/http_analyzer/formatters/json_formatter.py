"""JSON formatting utilities for HTTP Analyzer CLI.

This module provides functions for pretty-printing and highlighting JSON content.
"""

import json
import re
from http_analyzer.formatters.terminal_colors import Colors


def format_json(json_data, color=True, indent=2):
    """Format JSON data with optional syntax highlighting.

    Args:
        json_data: The JSON data (dict, list, etc.) to format
        color: Whether to use ANSI color codes for syntax highlighting
        indent: Number of spaces for indentation

    Returns:
        Formatted JSON string
    """
    # Convert to pretty-printed JSON string
    if isinstance(json_data, str):
        try:
            # Try to parse as JSON if it's a string
            json_data = json.loads(json_data)
        except json.JSONDecodeError:
            # If it's not valid JSON, return as is
            return json_data

    json_str = json.dumps(json_data, indent=indent)

    # Apply syntax highlighting if requested
    if color:
        # Highlight JSON keys
        json_str = re.sub(r'("[\w-]+"):', r'{}\1{}:'.format(Colors.YELLOW, Colors.RESET), json_str)

        # Highlight string values
        json_str = re.sub(r': (".*?")', r': {}\1{}'.format(Colors.GREEN, Colors.RESET), json_str)

        # Highlight numbers
        json_str = re.sub(r': (\d+)', r': {}\1{}'.format(Colors.CYAN, Colors.RESET), json_str)

        # Highlight booleans and null
        json_str = re.sub(r': (true|false|null)', r': {}\1{}'.format(Colors.MAGENTA, Colors.RESET), json_str)

    return json_str