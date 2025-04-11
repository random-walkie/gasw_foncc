"""HTML formatting utilities for HTTP Analyzer CLI.

This module provides classes and functions for formatting HTML content
in a more readable way for terminal output.
"""

import re
from http_analyzer.html_handler import HTMLHandler
from http_analyzer.formatters.terminal_colors import Colors


class HTMLFormatter:
    """Handles the formatting of HTML content for terminal display."""

    @staticmethod
    def format_html(html_content, color=True):
        """Format HTML content for better readability in the terminal.

        Args:
            html_content: The HTML content to format
            max_width: Maximum line width for formatting
            color: Whether to use ANSI color codes

        Returns:
            Formatted HTML string
        """
        # Use HTMLHandler to parse the content
        parsed_html = HTMLHandler.parse_html(html_content)

        # Extract metadata
        metadata = HTMLHandler.extract_metadata(parsed_html)

        # Format the output
        output = []

        # Format document title
        if metadata['title']:
            if color:
                output.append(f"{Colors.BOLD}{Colors.GREEN}Document Title:{Colors.RESET} {metadata['title']}")
            else:
                output.append(f"Document Title: {metadata['title']}")

        # Format meta tags
        if metadata['meta_tags']:
            if color:
                output.append(f"\n{Colors.BOLD}{Colors.CYAN}Meta Tags:{Colors.RESET}")
            else:
                output.append("\nMeta Tags:")

            for name, content in metadata['meta_tags'].items():
                if color:
                    output.append(f"  {Colors.YELLOW}{name}:{Colors.RESET} {content}")
                else:
                    output.append(f"  {name}: {content}")

        # Format links
        if metadata['links']:
            if color:
                output.append(f"\n{Colors.BOLD}{Colors.BLUE}Links:{Colors.RESET}")
            else:
                output.append("\nLinks:")

            for link in metadata['links']:
                if color:
                    output.append(f"  {Colors.MAGENTA}{link['text']}:{Colors.RESET} {link['href']}")
                else:
                    output.append(f"  {link['text']}: {link['href']}")

        # Format forms if present
        forms = HTMLHandler.extract_forms(parsed_html)
        if forms:
            if color:
                output.append(f"\n{Colors.BOLD}{Colors.RED}Forms:{Colors.RESET}")
            else:
                output.append("\nForms:")

            for i, form in enumerate(forms):
                if color:
                    output.append(f"  {Colors.BOLD}Form #{i+1}:{Colors.RESET}")
                    output.append(f"    {Colors.YELLOW}Action:{Colors.RESET} {form['action']}")
                    output.append(f"    {Colors.YELLOW}Method:{Colors.RESET} {form['method']}")
                    output.append(f"    {Colors.YELLOW}Fields:{Colors.RESET}")
                else:
                    output.append(f"  Form #{i+1}:")
                    output.append(f"    Action: {form['action']}")
                    output.append(f"    Method: {form['method']}")
                    output.append(f"    Fields:")

                for field in form['fields']:
                    field_type = field['type']
                    field_name = field['name']
                    field_value = field['value']

                    if color:
                        output.append(f"      {Colors.CYAN}{field_name}{Colors.RESET} ({field_type}): {field_value}")
                    else:
                        output.append(f"      {field_name} ({field_type}): {field_value}")

        # Pretty-print the actual HTML structure
        if color:
            output.append(f"\n{Colors.BOLD}{Colors.GREEN}HTML Structure:{Colors.RESET}")
        else:
            output.append("\nHTML Structure:")

        # Get a pretty-formatted version of the HTML
        pretty_html = HTMLFormatter.pretty_print_html(html_content, color=color)
        output.append(pretty_html)

        return "\n".join(output)

    @staticmethod
    def pretty_print_html(html_content, indent_size=2, color=True):
        """Format HTML with proper indentation and syntax highlighting.

        Args:
            html_content: HTML content as string or bytes
            indent_size: Number of spaces for each indentation level
            color: Whether to use ANSI colors for syntax highlighting

        Returns:
            Formatted HTML string
        """
        if isinstance(html_content, bytes):
            try:
                html_content = html_content.decode('utf-8')
            except UnicodeDecodeError:
                html_content = html_content.decode('utf-8', errors='replace')

        # Remove existing whitespace between tags
        html_content = re.sub(r'>\s+<', '><', html_content)

        # Simple tag matcher
        tag_pattern = re.compile(r'<[^>]+>')

        # Process each line
        formatted_lines = []
        current_indent = 0

        # Split content by tags
        tokens = []
        last_pos = 0

        for tag_match in tag_pattern.finditer(html_content):
            start, end = tag_match.span()

            # Add text before the tag
            if start > last_pos:
                text = html_content[last_pos:start].strip()
                if text:
                    tokens.append(('text', text))

            # Add the tag
            tag = html_content[start:end]
            tokens.append(('tag', tag))

            last_pos = end

        # Add any remaining text
        if last_pos < len(html_content):
            text = html_content[last_pos:].strip()
            if text:
                tokens.append(('text', text))

        # Process the tokens to create formatted output
        for token_type, token in tokens:
            if token_type == 'tag':
                # Check if it's an opening tag, closing tag, or self-closing
                if token.startswith('</'):
                    # Closing tag
                    current_indent -= 1
                    if current_indent < 0:
                        current_indent = 0
                    if color:
                        formatted_lines.append(' ' * (current_indent * indent_size) + Colors.RED + token + Colors.RESET)
                    else:
                        formatted_lines.append(' ' * (current_indent * indent_size) + token)
                elif token.endswith('/>') or token in ['<br>', '<hr>', '<img>', '<input>', '<link>', '<meta>']:
                    # Self-closing tag
                    if color:
                        formatted_lines.append(' ' * (current_indent * indent_size) + Colors.YELLOW + token + Colors.RESET)
                    else:
                        formatted_lines.append(' ' * (current_indent * indent_size) + token)
                elif not token.startswith('<!'):
                    # Opening tag
                    if color:
                        formatted_lines.append(' ' * (current_indent * indent_size) + Colors.GREEN + token + Colors.RESET)
                    else:
                        formatted_lines.append(' ' * (current_indent * indent_size) + token)
                    current_indent += 1
                else:
                    # Comment or doctype
                    if color:
                        formatted_lines.append(' ' * (current_indent * indent_size) + Colors.BLUE + token + Colors.RESET)
                    else:
                        formatted_lines.append(' ' * (current_indent * indent_size) + token)
            else:
                # Text content
                formatted_lines.append(' ' * (current_indent * indent_size) + token)

        return '\n'.join(formatted_lines)