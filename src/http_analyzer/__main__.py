#!/usr/bin/env python3
"""
Entry point for HTTP Request Analyzer.

This module serves as the main entry point for the application,
handling top-level exception management and CLI invocation.
"""

import sys
import logging
from http_analyzer.cli import HTTPAnalyzerCLI

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    # Configure basic logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create and run CLI
    cli = HTTPAnalyzerCLI()

    try:
        exit_code = cli.run()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unhandled error: {e}", exc_info=True)
        print(f"Unhandled error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()