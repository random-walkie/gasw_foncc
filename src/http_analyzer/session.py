from http_analyzer.request import HTTPRequest
from http_analyzer.content import ContentHandler
from http_analyzer.client import HTTPClient
from urllib.parse import urlparse

class HTTPSession:
    """Handles HTTP session management and request/response exchange.

    This class demonstrates Session Layer (Layer 5) functionality by maintaining
    state across multiple HTTP requests, tracking cookies, and managing connections.
    """

    def __init__(self):
        """Initialize a new HTTP session."""
        # Initialize session-level attributes:
        # - Dictionary to store cookies received from servers
        # - Request history list (if implementing history tracking)
        # - Default headers for all requests
        self.history = []
        self.cookies = {}
        self.default_headers = {
            "User-Agent": "HTTPAnalyzer/1.0",
            "Accept": "*/*",
        }

        #Create the client that will handle actual HTTP communication
        # This separates the concerns - Session (Layer 5) vs Transport (Layer 4)
        self.client = HTTPClient()
        self.content_handler = ContentHandler()

    def post(self, url, data=None, headers=None, json=None, timeout=200):
        """Send a POST request to the specified URL.

        Args:
            url: Target URL for the request
            data: Dictionary, bytes, or file-like object to send in the request body
            headers: Dictionary of HTTP headers to send
            json: JSON data to send in the request body (alternative to data)
            timeout: Socket timeout in seconds

        Returns:
            HTTPResponse: The response from the server
        """
        # Validate input parameters
        # - Check that URL is properly formatted
        # - Ensure data and json aren't both provided (should use one or the other)
        parsed_url = urlparse(url)
        if data is not None and json is not None:
            raise ValueError("Cannot provide both 'data' and 'json' parameters to post().")

        # Prepare request headers
        # - Start with default headers
        # - Merge in any session cookies for this domain
        # - Merge in any user-provided headers
        request_headers = self.default_headers.copy()
        domain = parsed_url.netloc
        if domain in self.cookies:
            cookie_str = "; ".join([f"{k}={v}" for k, v in self.cookies[domain].items()])
            request_headers["Cookie"] = cookie_str
        if headers is not None:
            request_headers.update(headers)

        # Prepare request body based on data or json parameter
        # - If json is provided, serialize to JSON string and set Content-Type
        # - If data is provided as dict, encode as form data
        # - If data is provided as bytes, use as-is
        request_body = None
        if json is not None:
            request_body, content_type = self.content_handler.encode_content(json, "application/json")
            request_headers["Content-Type"] = content_type
        elif data is not None:
            if isinstance(data, dict):
                form_items = []
                for key, value in data.items():
                    form_items.append(f"{key}={value}")
                request_body = "&".join(form_items).encode("utf-8")
                request_headers["Content-Type"] = "application/x-www-form-urlencoded"
            elif isinstance(data, bytes):
                request_body = data
            else:
                request_body = str(data).encode("utf-8")
                request_headers["Content-Type"] = "text/plain"


        # Create an HTTPRequest object for this request
        # - Method should be "POST"
        # - Include the URL, headers, and body
        request_obj = HTTPRequest(method="POST", url=url, headers=request_headers, body=request_body)

        # Use the HTTP client to send the request and get the response
        # - This delegates the socket handling to the client class
        # - Let the client handle connection establishment and request sending
        response_obj = self.client.send_request(request_obj, timeout=timeout)

        # Process session-related response headers        
        # Extract and store cookies from Set-Cookie headers
        if "Set-Cookie" in response_obj.headers:
            # Initialize cookies dict for this domain if needed
            if domain not in self.cookies:
                self.cookies[domain] = {}
            # Handle the list of cookie headers
            for cookie_header in response_obj.headers["Set-Cookie"]:
                cookie_parts = cookie_header.split(";")[0].strip()
                if "=" in cookie_parts:
                    name, value = cookie_parts.split("=", 1)
                    self.cookies[domain][name] = value

        # Update session state based on other headers (e.g., content-type, cache-control)
        response_content_type = response_obj.headers.get("Content-Type", None)
        if response_content_type:
            self.default_headers["Accept"] = response_content_type

        # Add to request/response history
        self.history.append((request_obj, response_obj))

        # Return the response object
        return response_obj

    def get(self, url, headers=None, timeout=200):
        """Send a GET request to the specified URL.

        Args:
            url: Target URL for the request
            headers: Dictionary of HTTP headers to send
            timeout: Socket timeout in seconds

        Returns:
            HTTPResponse: The response from the server
        """
        # Similar implementation to post(), but using GET method
        # - Prepare headers including cookies
        # - Create request object
        # - Send request through client
        # - Process response headers for cookies
        # - Return response

        # Parse the URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Prepare request headers
        request_headers = self.default_headers.copy()
        if domain in self.cookies:
            cookie_str = "; ".join([f"{k}={v}" for k, v in self.cookies[domain].items()])
            request_headers["Cookie"] = cookie_str
        if headers is not None:
            request_headers.update(headers)

        # Create an HTTPRequest object for this request
        request_obj = HTTPRequest(method="GET", url=url, headers=request_headers, body=None)

        # Use the HTTP client to send the request and get the response
        response_obj = self.client.send_request(request_obj, timeout=timeout)

        # Process session-related response headers
        if "Set-Cookie" in response_obj.headers:
            # Initialize cookies dict for this domain if needed
            if domain not in self.cookies:
                self.cookies[domain] = {}
            # Handle the list of cookie headers
            for cookie_header in response_obj.headers["Set-Cookie"]:
                cookie_parts = cookie_header.split(";")[0].strip()
                if "=" in cookie_parts:
                    name, value = cookie_parts.split("=", 1)
                    self.cookies[domain][name] = value

        # Update session state based on other headers
        response_content_type = response_obj.headers.get("Content-Type", None)
        if response_content_type:
            self.default_headers["Accept"] = response_content_type

        # Add to request/response history
        self.history.append((request_obj, response_obj))

        # Return the response object
        return response_obj
        

    def close(self) -> None:
        """Close the session and release resources."""
        # Close the HTTP client to release connections
        self.client.close()

    def __del__(self) -> None:
        """Destructor to ensure resources are released."""
        # Call close() method
        self.close()