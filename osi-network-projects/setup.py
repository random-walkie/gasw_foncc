from setuptools import setup, find_packages

setup(
    name="osi-network-projects",
    version="0.1.0",
    description="Tools for exploring networking concepts: HTTP Analyzer and TCP Monitors",
    author="Your Name",
    author_email="your.email@example.com",

    # Find all packages in src directory
    packages=find_packages(where="src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},

    # Explicitly include test packages if you want them installed
    # This is optional and depends on your specific needs
    package_data={
        # Include test data files if any
        "": ["*.txt", "*.json", "*.csv"],
    },

    # Test suite configuration
    test_suite="tests",

    setup_requires=[
        'setuptools>=61.0.0'
    ],

    install_requires=[
        "colorama>=0.4.4",
        "scapy>=2.4.5",
        "psutil>=5.8.0",
        "cryptography>=3.4.0",
    ],

    extras_require={
        "dev": [
            "pytest>=8.3.5",
            "pytest-cov==6.1.1",
            "python-dateutil==2.9.0",
            "attrs>=21.4.0"
        ],
        "html": [
            "beautifulsoup4>=4.9.3"
        ],
        "full": [
            "beautifulsoup4>=4.9.3"
        ]
    },

    # Configure test discovery and running
    options={
        'test': {
            'test_suite': 'tests',
        }
    },

    entry_points={
        "console_scripts": [
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

    python_requires=">=3.7",
)