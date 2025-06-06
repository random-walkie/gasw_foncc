# Fundamentals of Networks and Cloud Computing

This repository contains my coursework, projects, and study materials for the Fundamentals of Networks and Cloud Computing course. The repository serves as a comprehensive resource for learning networking concepts with a particular focus on the OSI model.

## OSI Layer Learning Projects
`osi-networks-projects` is a collection of hands-on projects that demonstrate networking concepts across all OSI layers:

1. **TCP Connection Monitor [IN PROGRESS]** - Explores OSI Layers 1-4 (Physical, Data Link, Network, Transport) by capturing and analyzing TCP connections.

2. **HTTP Request Analyzer** - Explores OSI Layers 5-7 (Session, Presentation, Application) by implementing a custom HTTP client that can analyze requests and responses.

These projects are designed to provide practical experience with theoretical networking concepts that appear in the course curriculum and exams.

### Installation and Setup for `osi-networks-projects`

To work with the networking projects included in this repository:

```bash
# Clone the repository
git clone https://github.com/random-walkie/gasw_foncc.git
cd gasw_foncc/osi-network-projects/

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install all components and dependencies
pip install -e .
```

### Project Usage

After installation, you can use each tool via its command-line interface:

```bash
# TCP Connection Monitor
tcp-monitor --interface eth0 --duration 60

# HTTP Request Analyzer
http-analyzer https://example.com --verbose --pretty-html
```

See the individual project READMEs for more detailed usage instructions:
- [TCP Connection Monitor Documentation](tcp-connection-monitor/README.md)
- [HTTP Request Analyzer Documentation](osi-network-projects/src/http_analyzer/README.md)

### Disclosure Statement
The `osi-networks-project` is the result of a collaborative development effort between me and [Claude](https://claude.ai), an AI assistant created by Anthropic.

#### Repository Contents
The project was conceived and developed through an interactive, iterative process. While the initial conceptualization and architectural decisions were made by me, the implementation details,
code writing, and refinement were achieved through a collaborative dialogue with AI assistance.

#### Roles and Contributions

##### Me:

+ Project conceptualization
+ Domain expertise in networking and OSI model
+ Overall architectural guidance
+ Code implementation
+ Iterative refinement of code and documentation
+ Critical review and validation

##### Claude (Anthropic AI):

+ Code implementation
+ Architectural suggestions
+ Detailed technical documentation
+ Test case generation
+ Iterative refinement of code and documentation

#### Transparency
This project exemplifies the potential of human-AI collaboration in software development. While the AI provided substantial technical assistance, all critical decisions and final approvals were made by the human developer.

#### Ethical Considerations

The project was developed with a strong educational focus.
All code was generated with careful consideration of best practices.
The collaboration aimed to create a learning resource for network protocol understanding

#### Disclaimer
This project is an experimental collaboration and is provided as an educational tool. Users should exercise their own judgment and conduct their own testing.


## Coursework
This section contains my completed coursework assignments, including:
- Weekly lab exercises
- Assignment submissions

## Exam Preparation
Materials to help study for exams:
- Concept summaries
- Practice questions
- Diagrams illustrating important network concepts



## Learning Approach

This repository is organized to support a hands-on, practical approach to learning networking concepts. The combination of theoretical study materials and working code projects is designed to reinforce understanding of how network communications function at each layer of the OSI model.

The projects demonstrate:
- How data is encapsulated and transmitted between OSI layers
- The responsibilities and functions of each layer
- How protocols implement these functions in practice
- The relationships between different networking components

## Course Information

**Course Code:** M1l325895   
**Term:** Spring 2025

## License

MIT.

## Acknowledgments
Special thanks to Anthropic for developing Claude, an AI assistant that can engage in meaningful, collaborative software development.
