from setuptools import setup, find_packages

setup(
    name="osi-network-projects",
    version="0.1.0",
    description="Tools for exploring the OSI networking model layers",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        # Shared dependencies
        "colorama>=0.4.4",  # For terminal colors

        # TCP Monitor dependencies
        "scapy>=2.4.5",     # For packet capture
        "psutil>=5.8.0",    # For network interface info

        # HTTP Analyzer dependencies
        "cryptography>=3.4.0",  # For SSL/TLS support
    ],
    entry_points={
        'console_scripts': [
            'tcp-monitor=tcp_monitor.__main__:main',
            'http-analyzer=http_analyzer.__main__:main',
        ],
    },
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=20.8b1",  # For formatting
            "mypy>=0.800",    # For type checking
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: System :: Networking",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)