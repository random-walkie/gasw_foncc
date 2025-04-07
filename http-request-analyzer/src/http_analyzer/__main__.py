#!/usr/bin/env python3
"""
Entry point for HTTP Request Analyzer.

This module serves as the main entry point for the application,
handling top-level exception management and CLI invocation.
"""

import sys
from src.http_analyzer.cli import HTTPAnalyzerCLI

def main():
    """Main entry point for the application."""
    cli = HTTPAnalyzerCLI()

    try:
        exit_code = cli.run()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unhandled error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()