from setuptools import setup, find_packages

setup(
    name="osi-network-projects",  # Name for the combined project
    version="0.1.0",
    description="Tools for exploring networking concepts: HTTP Analyzer and TCP Monitors",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src", exclude=["tests*", "tests.*"]),  # Discover HTTP and TCP packages in src/
    package_dir={"": "src"},  # Map root namespace to src/
    install_requires=[
        "colorama>=0.4.4",  # Shared dependency for terminal colors
        "scapy>=2.4.5",  # For packet capture (used by tcp_monitor)
        "psutil>=5.8.0",  # For TCP monitor
        "cryptography>=3.4.0",  # For SSL/TLS support in HTTP analyzer
    ],
    extras_require={
        # Development dependencies for testing and linting
        "dev": [
            "pytest>=8.3.5",
            "pytest-cov==6.1.1",
            "python-dateutil==2.9.0"
        ],
    },
    entry_points={
        "console_scripts": [
            # Define CLI commands for HTTP Analyzer and TCP Monitor
            "http-analyzer=http_analyzer.__main__:main",
            "tcp-monitor=tcp_monitor.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",  # Minimum Python version required
)
