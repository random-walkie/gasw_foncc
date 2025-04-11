"""
A simple fallback HTML parser for when BeautifulSoup is unavailable.
"""

class HTMLFallbackParser:
    """A simple fallback HTML parser for when BeautifulSoup is unavailable."""

    def __init__(self, html_content, encoding='utf-8'):
        """Initialize with HTML content."""
        self.html = self._decode_content(html_content, encoding)

    @staticmethod
    def _decode_content(content, encoding):
        """Decode bytes content to string if needed."""
        if isinstance(content, bytes):
            try:
                return content.decode(encoding)
            except UnicodeDecodeError:
                return content.decode(encoding, errors='replace')
        return content

    def extract_metadata(self):
        """Extract basic metadata from HTML."""
        return {
            'title': self._extract_title(),
            'meta_tags': self._extract_meta_tags(),
            'links': self._extract_links()
        }

    def _extract_title(self):
        """Extract the title from HTML."""
        title_start = self.html.lower().find('<title>')
        if title_start == -1:
            return None

        title_end = self.html.lower().find('</title>', title_start)
        if title_end == -1:
            return None

        return self.html[title_start + 7:title_end].strip()

    def _extract_meta_tags(self):
        """Extract meta tags from HTML."""
        meta_tags = {}
        start_idx = 0

        while True:
            meta_start = self.html.lower().find('<meta', start_idx)
            if meta_start == -1:
                break

            meta_end = self.html.find('>', meta_start)
            if meta_end == -1:
                break

            meta_tag = self.html[meta_start:meta_end+1]
            name, content = self._parse_meta_tag(meta_tag)

            if name and content:
                meta_tags[name] = content

            start_idx = meta_end + 1

        return meta_tags

    @staticmethod
    def _parse_meta_tag(meta_tag):
        """Parse a meta tag to extract name/property and content."""
        name = None
        content = None

        # Try to find name attribute
        name_start = meta_tag.find('name="')
        if name_start != -1:
            name_start += 6
            name_end = meta_tag.find('"', name_start)
            if name_end != -1:
                name = meta_tag[name_start:name_end]

        # Try to find property attribute if name wasn't found
        if name is None:
            prop_start = meta_tag.find('property="')
            if prop_start != -1:
                prop_start += 10
                prop_end = meta_tag.find('"', prop_start)
                if prop_end != -1:
                    name = meta_tag[prop_start:prop_end]

        # Try to find content attribute
        content_start = meta_tag.find('content="')
        if content_start != -1:
            content_start += 9
            content_end = meta_tag.find('"', content_start)
            if content_end != -1:
                content = meta_tag[content_start:content_end]

        return name, content

    def _extract_links(self):
        """Extract links from HTML."""
        links = []
        start_idx = 0

        while True:
            link_start = self.html.lower().find('<a ', start_idx)
            if link_start == -1:
                break

            link_end = self.html.find('</a>', link_start)
            if link_end == -1:
                break

            link_tag = self.html[link_start:link_end + 4]
            link_info = self._parse_link_tag(link_tag)

            if link_info and link_info.get('href'):
                links.append(link_info)

            start_idx = link_end + 4

        return links

    @staticmethod
    def _parse_link_tag(link_tag):
        """Parse a link tag to extract href and text."""
        href = None
        text = "Link"  # Default text

        # Extract href
        href_start = link_tag.find('href="')
        if href_start != -1:
            href_start += 6
            href_end = link_tag.find('"', href_start)
            if href_end != -1:
                href = link_tag[href_start:href_end]

        # Extract text content
        close_tag_pos = link_tag.find('>')
        if close_tag_pos != -1 and close_tag_pos + 1 < len(link_tag) - 4:
            text = link_tag[close_tag_pos + 1:len(link_tag) - 4].strip()

        return {'text': text, 'href': href} if href else None

    def extract_forms(self):
        """Extract form information from HTML."""
        forms = []
        start_idx = 0

        while True:
            form_start = self.html.lower().find('<form', start_idx)
            if form_start == -1:
                break

            form_end = self.html.find('</form>', form_start)
            if form_end == -1:
                break

            form_tag = self.html[form_start:form_end + 7]
            form_data = self._parse_form_tag(form_tag)
            forms.append(form_data)

            start_idx = form_end + 7

        return forms

    def _parse_form_tag(self, form_tag):
        """Parse a form tag to extract action, method, and fields."""
        # Extract action
        action = self._extract_attribute(form_tag, 'action')

        # Extract method
        method = self._extract_attribute(form_tag, 'method') or "GET"
        method = method.upper()

        return {
            'action': action,
            'method': method,
            'fields': self._extract_form_fields(form_tag)
        }

    def _extract_form_fields(self, form_html):
        """Extract fields from a form HTML string."""
        fields = []

        # Process input fields
        fields.extend(self._extract_input_fields(form_html))

        # Process textarea fields
        fields.extend(self._extract_textarea_fields(form_html))

        # Process select fields
        fields.extend(self._extract_select_fields(form_html))

        return fields

    def _extract_input_fields(self, form_html):
        """Extract input fields from form HTML."""
        fields = []
        start_idx = 0

        while True:
            input_start = form_html.lower().find('<input', start_idx)
            if input_start == -1:
                break

            input_end = form_html.find('>', input_start)
            if input_end == -1:
                break

            input_tag = form_html[input_start:input_end+1]
            field = self._parse_input_tag(input_tag)
            fields.append(field)

            start_idx = input_end + 1

        return fields

    def _parse_input_tag(self, input_tag):
        """Parse an input tag to extract field attributes."""
        # Extract name
        name = self._extract_attribute(input_tag, 'name')

        # Extract type
        type_val = self._extract_attribute(input_tag, 'type') or "text"

        # Extract value
        value = self._extract_attribute(input_tag, 'value') or ""

        return {
            'name': name,
            'type': type_val,
            'value': value
        }

    def _extract_textarea_fields(self, form_html):
        """Extract textarea fields from form HTML."""
        fields = []
        start_idx = 0

        while True:
            textarea_start = form_html.lower().find('<textarea', start_idx)
            if textarea_start == -1:
                break

            textarea_end = form_html.find('</textarea>', textarea_start)
            if textarea_end == -1:
                break

            textarea_tag = form_html[textarea_start:textarea_end+11]
            field = self._parse_textarea_tag(textarea_tag)
            fields.append(field)

            start_idx = textarea_end + 11

        return fields

    def _parse_textarea_tag(self, textarea_tag):
        """Parse a textarea tag to extract field attributes."""
        # Extract name
        name = self._extract_attribute(textarea_tag, 'name')

        # Find the closing tag
        close_tag_pos = textarea_tag.find('>')
        if close_tag_pos == -1:
            value = ""
        else:
            # Calculate the end of the content - start of closing tag
            close_content_pos = textarea_tag.find('</textarea>', close_tag_pos)
            if close_content_pos == -1:
                value = ""
            else:
                # Extract the content between tags
                value = textarea_tag[close_tag_pos + 1:close_content_pos].strip()

        return {
            'name': name,
            'type': 'textarea',
            'value': value
        }

    def _extract_select_fields(self, form_html):
        """Extract select fields from form HTML."""
        fields = []
        start_idx = 0

        while True:
            select_start = form_html.lower().find('<select', start_idx)
            if select_start == -1:
                break

            select_end = form_html.find('</select>', select_start)
            if select_end == -1:
                break

            select_tag = form_html[select_start:select_end+9]
            field = self._parse_select_tag(select_tag)
            fields.append(field)

            start_idx = select_end + 9

        return fields

    def _parse_select_tag(self, select_tag):
        """Parse a select tag to extract field attributes."""
        # Extract name
        name = self._extract_attribute(select_tag, 'name')

        return {
            'name': name,
            'type': 'select',
            'value': ''  # Could extract options but keeping it simple
        }

    @staticmethod
    def _extract_attribute(tag, attr_name):
        """Extract an attribute value from an HTML tag."""
        attr_str = f'{attr_name}="'
        attr_start = tag.find(attr_str)

        if attr_start == -1:
            return ""

        attr_start += len(attr_str)
        attr_end = tag.find('"', attr_start)

        if attr_end == -1:
            return ""

        return tag[attr_start:attr_end]

    def __str__(self):
        """Return the HTML content as string."""
        return self.html