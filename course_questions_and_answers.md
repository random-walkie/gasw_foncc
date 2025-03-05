# Fundamentals of Cloud Computing and Networks Q&A
> This document contains questions and answers related to the course content (24/25).

## Week 1: Overview & Cloud Introduction

**What is cloud computing?**
<details>
  <summary>Answer</summary>

Cloud computing is a technology that allows users to access and use computing resources (servers, storage, databases, networking, software) over the internet on a pay-as-you-go basis. It's a type of distributed system that provides services to a shared pool of resources, eliminating the need for organisations to invest in and maintain physical infrastructure, offering flexibility and scalability.
</details>

**What is the NIST definition of cloud computing?**
<details>
  <summary>Answer</summary>

According to the U.S. National Institute of Standards and Technology (NIST): "Cloud computing is a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model promotes availability and is composed of five essential characteristics, three service models, and four deployment models."
</details>

**What are the five essential characteristics of cloud computing?**
<details>
  <summary>Answer</summary>

1. On-demand self-service - Users can provision resources without requiring human interaction with service providers
2. Broad network access - Capabilities are available over the network and accessed through standard mechanisms
3. Multi-tenancy/Resource pooling - Computing resources serve multiple consumers using a multi-tenant model
4. Rapid elasticity - Resources can be elastically provisioned and released to scale with demand
5. Measured service - Resource usage is monitored, controlled, reported, and charged appropriately
</details>

**What is the difference between grid computing and cloud computing?**
<details>
  <summary>Answer</summary>

Grid computing:
- Application oriented
- Tasks are divided into sub-tasks and allocated to machines
- Interconnected computers working on a large-scale task
- Usually owned by an organisation within a corporate network
- Management is decentralised

Cloud computing:
- Service oriented
- Provides services on demand
- Accessed via internet
- Owned by an infrastructure provider
- Management is centralised
</details>

**What is virtualisation and why is it important for cloud computing?**
<details>
  <summary>Answer</summary>

virtualisation is the main enabling technology for cloud computing. It involves partitioning a single physical server into multiple logical servers. Once divided, each logical server behaves like a physical server and can run an operating system and applications independently. A hypervisor is software that runs virtual machines. virtualisation separates resources and services from the physical system, enabling partitioning, isolation, and encapsulation.
</details>

**What are the types of virtualisation?**
<details>
  <summary>Answer</summary>

1. Network virtualisation - Combining available resources in a network by splitting bandwidth into channels
2. Storage virtualisation - Pooling physical storage from multiple devices to appear as a single storage device
3. Server virtualisation - Masking server resources to increase resource sharing and reduce complexity
</details>

**What is a hypervisor and what are its types?**
<details>
  <summary>Answer</summary>

A hypervisor is software that runs virtual machines. It's close to the hardware to facilitate multiple operating systems and schedules hardware resources for other OSs. Types include:
1. Type 1 (Native) - Sits directly on hardware (e.g., Microsoft Hyper-V)
2. Type 2 (Hosted) - Runs as software on other hardware and OS (e.g., VMWare player)
</details>

**What are the types of client virtualisation?**
<details>
  <summary>Answer</summary>

1. Session-based - Server runs a single OS with multiple sessions for users
2. Operating system streaming - OS is passed to users as required with some processing on server, some on client
3. Virtual Desktop Infrastructure - Server runs virtual PCs that are sent to users
4. PC blade - A server blade containing several PCs allocated to users
</details>

## Week 2: Cloud Models & Patterns

**What are the three main cloud service models?**
<details>
  <summary>Answer</summary>

1. SaaS (Software as a Service) - Complete applications offered as a service on demand
2. PaaS (Platform as a Service) - Development environment encapsulated and offered as a service
3. IaaS (Infrastructure as a Service) - Computing infrastructure provided as a service
</details>

**What is SaaS and what are its characteristics?**
<details>
  <summary>Answer</summary>

Software as a Service (SaaS) offers complete applications as a service on demand. A single instance of software runs on the cloud and services multiple end users or client organisations. It's usually subscription-based or pay-as-you-go (sometimes free). Applications are accessible from various client devices, and users don't manage the underlying cloud infrastructure except for limited user-specific application settings. Examples include Google Apps, Salesforce, and Office 365.
</details>

**What is PaaS and what are its characteristics?**
<details>
  <summary>Answer</summary>

Platform as a Service (PaaS) provides a development environment encapsulated as a service. Consumers purchase access to platforms that enable them to deploy their own applications using supported programming languages, libraries, services, and tools. Users control deployed applications but not the underlying cloud infrastructure. PaaS is used by developers for in-house application development. Examples include Google App Engine, AWS Elastic Beanstalk, and Windows Azure.
</details>

**What is IaaS and what are its characteristics?**
<details>
  <summary>Answer</summary>

Infrastructure as a Service (IaaS) provides fundamental computing resources like processing, storage, networks, and other resources where users can deploy and run arbitrary software including operating systems and applications. Users control operating systems, storage, and deployed applications but not the underlying cloud infrastructure. Examples include Amazon EC2, Google Compute Engine, and Digital Ocean.
</details>

**How can cloud service models be compared to making a cake?**
<details>
  <summary>Answer</summary>

- Traditional On-premises: Like making a cake from scratch - you buy all ingredients, mix them, bake the cake, and clean up afterward
- IaaS: Like having pre-measured ingredients provided - you still mix, bake and clean up
- PaaS: Like having the batter ready - you just bake the cake and clean up
- SaaS: Like buying a cake from a bakery - everything is done for you
</details>

**What are the four cloud deployment models?**
<details>
  <summary>Answer</summary>

1. Public Cloud - Available to all, provided by third-party service providers
2. Private Cloud - Available within a single organisation, can be internally or externally hosted
3. Hybrid Cloud - Combination of public and private cloud types
4. Community Cloud - Shared by several organisations in a collaborative platform
</details>

**What are cloud application design principles?**
<details>
  <summary>Answer</summary>

1. Scaling elasticity - Identifying bottlenecks for horizontal (more machines) or vertical (more compute power) scaling
2. Redundancy - Replicating and partitioning databases for reliability
3. Error correction - Implementing self-healing and failover mechanisms
4. Evolution - Designing for high cohesion and loose coupling to facilitate changes
</details>

**What are common cloud patterns and what challenges do they address?**
<details>
  <summary>Answer</summary>

1. Queue-based Load Levelling - Buffers between tasks and services (Availability)
2. Throttling - Controls resource consumption (Availability)
3. Cache-Aside - Improves data access performance (Data Management)
4. Sharding - Partitions databases horizontally or vertically (Data Management)
5. Backends for Frontends - Creates separate backend services for specific frontend applications (Design and Implementation)
6. Static Content Hosting - Delivers static web pages separately (Design and Implementation)
7. Gateway Aggregation - Aggregates multiple requests into a single request (Managing and Monitoring)
8. Priority Queue - Manages service level agreements between users or functions (Messaging)
9. Retry - Handles faults transparently (Resiliency)
10. Bulkhead - Isolates elements for fault tolerance (Resiliency)
11. Federated Identity - Delegates authentication to external providers (Security)
</details>

## Week 3: Cloud Architecture & Services

**What is N-tier cloud architecture?**
<details>
  <summary>Answer</summary>

N-tier architecture is a traditional approach where dependencies are managed by dividing applications into layers (e.g., presentation, business logic, and data access). It's often used with IaaS and is a natural fit for migrating existing layered systems to the cloud, though updating such systems can be difficult.
</details>

**What is microservices architecture?**
<details>
  <summary>Answer</summary>

Microservices architecture involves software made up of small, independent services, each handling a single capability. Services are loosely coupled and communicate through APIs. This architecture works well with complexity, innovation, and high-velocity updates but requires the right development culture.
</details>

**What are the key differences between N-tier and microservices architectures?**
<details>
  <summary>Answer</summary>

N-tier architecture:
- organised in horizontal layers
- Components are tightly coupled
- Single codebase and deployment
- Scales vertically (larger machines)
- Updates affect entire application
- Failure affects entire application

Microservices architecture:
- organised around business capabilities
- Components are loosely coupled
- Multiple codebases and deployments
- Scales horizontally (more instances)
- Updates affect individual services
- Failure is isolated to specific services
</details>

**What is a container in cloud computing?**
<details>
  <summary>Answer</summary>

A container is a standalone, all-in-one package that includes an executable and any dependencies. Containers can run on laptops, servers, or virtual machines, making them portable and scalable. Unlike virtual machines, containers share the host OS kernel but isolate application processes.
</details>

**What are Docker and Kubernetes?**
<details>
  <summary>Answer</summary>

- Docker is an open-source platform for creating, deploying, and running containers.
- Kubernetes is an open-source platform for orchestrating containers, handling deployment, scaling, and management, including those built by Docker.
</details>

**What are some common cloud services for web applications?**
<details>
  <summary>Answer</summary>

1. Active Directory - Authentication services
2. DNS - Hosting service for domains
3. App Service - Platform for creating and deploying apps
4. Front Door - Load balancing and security
5. Content Delivery Network - Caching content for lower latency
6. SQL Server/Database - Data storage and management
7. Storage Blob - Object storage for unstructured data
</details>

**What cloud services are typically used for game applications?**
<details>
  <summary>Answer</summary>

1. Traffic Manager - Directs client requests to appropriate service endpoints
2. PlayFab - Game-specific backend services
3. Content Delivery Network - Cached content delivery
4. Storage - Unstructured data storage
5. Database for MySQL - Relational database storage
6. Game Analytics - Performance and player behavior analysis
</details>

## Week 4: Cloud Data

**What are common cloud data services?**
<details>
  <summary>Answer</summary>

Common cloud data services include:
1. Simple Storage Service (S3) - Object storage for any type of data
2. Elastic Block Storage - Fast storage for data-intensive apps
3. Elastic File System - Fast, fully managed file storage
4. Relational Database Service (RDS) - SQL databases with high throughput
5. Elastic Cache - Fast performance, low latency caching
6. Aurora - SQL database compatible with MySQL
7. Timestream - Time series database
8. Neptune - Graph database for highly connected data
9. Lake Formation - Data lake for unstructured data
10. Redshift - Data warehouse for structured data
11. Kinesis - Real-time data analytics
12. Glue - ETL workflow automation
</details>

**What is data analysis in the cloud?**
<details>
  <summary>Answer</summary>

Data analysis in cloud computing involves searching large stores of data to discover patterns and trends beyond simple analysis. It examines data to identify meaningful insights that can guide business decisions.
</details>

**What are some data analysis techniques?**
<details>
  <summary>Answer</summary>

1. Support Vector Machine (SVM) - Finding lines or hyperplanes that separate data points
2. Regression Analysis - Investigating relationships between dependent and independent variables
3. Network Analysis - Examining relationships between nodes in a graph
4. Sentiment Analysis - Identifying and categorising opinions in text data
</details>

**What is machine learning in the cloud?**
<details>
  <summary>Answer</summary>

Machine learning (ML) in the cloud uses mathematical algorithms to train predictive models. It analyses relationships between data points to predict unknown values by exploring source data, training and validating models, and deploying them as services.
</details>

**What are some machine learning applications?**
<details>
  <summary>Answer</summary>

1. Search Engine Results Refinement - Improving results based on user behavior
2. Virtual Personal Assistants - Customising responses based on previous interactions
3. Social Media Features - Friend suggestions, face recognition, and content recommendations
4. Image Style Transfer - Applying artistic styles to images
5. Predictive Analytics - Forecasting future values or behaviors
</details>

**What are the stages of machine learning model preparation and training?**
<details>
  <summary>Answer</summary>

1. Source data collection
2. Data cleaning (removing duplicates, etc.)
3. Data analysis using correlations and regressions
4. Model training with a subset of data
5. Model validation using withheld data
6. Model deployment as a web service
</details>

## Week 5: Cloud Issues

**What is a SWOT analysis of cloud computing?**
<details>
  <summary>Answer</summary>

Strengths:
- Flexibility in service models
- Scalability to meet changing demand
- Reliability of service over time
- Availability of working services
- Resilience despite changing circumstances
- Sustainability compared to individual data centers

Weaknesses:
- Dependency on vendors (vendor lock-in)
- Data ownership concerns
- Infrastructure requirements for connectivity
- Inherent latency compared to on-premises
- Service quality guarantees limited by SLAs
- Legacy systems migration challenges

Opportunities:
- Ease of utilisation through service selection
- Simplified maintenance through centralisation
- Access to services for innovation
- Potentially lower costs through pay-as-you-go
- Low barrier to entry for small organisations
- Energy savings through resource optimisation

Threats:
- Cross-compatibility issues between providers
- Hidden costs beyond initial pricing
- Knowledge and expertise requirements
- Adoption resistance within organisations
- Security challenges in complex environments
- Geopolitical concerns about data sovereignty
</details>

**What is the shared responsibility model in cloud security?**
<details>
  <summary>Answer</summary>

The shared responsibility model divides security responsibilities between cloud providers and customers. Generally, providers are responsible for securing the cloud infrastructure (hardware, software, networking), while customers are responsible for data, applications, identity management, and client-side protection. The exact division depends on the service model (IaaS, PaaS, SaaS).
</details>

**What security threats exist in cloud computing?**
<details>
  <summary>Answer</summary>

Old threats:
- User authentication challenges
- Data integrity concerns
- Confidentiality breaches
- Distributed Denial of Service (DDoS) attacks

New threats:
- Managing old threats in complex environments
- Reliance on security automation tools
- Responsibility gaps between customers and providers
- Misconfigurations (like "leaky buckets" in Amazon S3)
</details>

**What are some security best practices for cloud computing?**
<details>
  <summary>Answer</summary>

1. Clear, consistent leadership and management
2. Proactive monitoring of resources and access
3. Implementing intrusion detection systems
4. Micro-segmentation of resources
5. Understanding the shared responsibility model
</details>

**What are data localisation concerns in cloud computing?**
<details>
  <summary>Answer</summary>

Data localisation refers to legal requirements in some jurisdictions that mandate certain types of data must be stored within national boundaries. This creates challenges for global cloud services and may require region-specific deployments to comply with varying data protection laws, particularly in Europe and Asia.
</details>

## Network Fundamentals

**What are the advantages of client-server networks?**
<details>
  <summary>Answer</summary>

1. centralised resource management for easier administration
2. Enhanced security through centralised authentication
3. Better scalability as server capacity can be upgraded independently
4. Simplified backup processes with centralised data
5. Straightforward disaster recovery with critical data in one location
</details>

**What are the disadvantages of client-server networks?**
<details>
  <summary>Answer</summary>

1. Higher implementation costs for server hardware and licensing
2. Single points of failure affecting the entire network
3. Higher maintenance costs for server management
4. Need for specialised knowledge for administration
5. Potential network congestion with many simultaneous requests
</details>

**What are the advantages of peer-to-peer networks?**
<details>
  <summary>Answer</summary>

1. Lower implementation costs without specialised server hardware
2. Simplified setup accessible for small organisations
3. Resilience from lack of single points of failure
4. Direct resource sharing between computers
5. Decentralised operation without central management
</details>

**What are the disadvantages of peer-to-peer networks?**
<details>
  <summary>Answer</summary>

1. Limited scalability for large organisations
2. Security challenges from decentralised management
3. Backup complications with distributed data
4. Performance issues as computers handle dual roles
5. Increasingly difficult administration as networks grow
</details>

**What are the physical components of a network?**
<details>
  <summary>Answer</summary>

1. End devices - Computers, smartphones, printers, servers
2. Network interface cards (NICs) - Hardware connecting devices to networks
3. Transmission media - Copper cables, fiber optic cables, wireless signals
4. Connectors - Physical interfaces like RJ-45
5. Intermediary devices - Switches, routers, and other equipment
</details>

**What are examples of intermediary network devices?**
<details>
  <summary>Answer</summary>

1. Routers - Connect different networks and determine optimal data paths
2. Switches - Connect multiple devices within same network using MAC addresses
3. Access points - Connect wireless devices to wired networks via Wi-Fi
</details>

**What type of switching is used in modern networks?**
<details>
  <summary>Answer</summary>

Packet switching is used in modern networks. This method breaks data into small packets with addressing information and sends them across the network, potentially via different paths. At the destination, packets are reassembled in the correct order. This approach is more efficient than circuit switching because it allows networks to share capacity among many users.
</details>

**What is the difference between encoding and decoding?**
<details>
  <summary>Answer</summary>

Encoding is converting information into a form suitable for transmission (e.g., digital data into electrical signals), while decoding is interpreting received information by converting transmitted signals back into an understandable format.
</details>

**What is the difference between encapsulation and de-encapsulation?**
<details>
  <summary>Answer</summary>

Encapsulation places one message inside another message format, with each network layer adding headers/trailers to data before passing it down. De-encapsulation extracts the original message by removing these headers/trailers as data moves up through network layers at the receiving end.
</details>

**What is segmentation in networking?**
<details>
  <summary>Answer</summary>

Segmentation divides data streams into smaller pieces for transmission. Large files are broken into manageable segments for more efficient transmission, error recovery, and resource sharing.
</details>

**What are the differences between goodput, throughput, and bandwidth?**
<details>
  <summary>Answer</summary>

1. Goodput is the amount of usable data transferred over time, representing application-level throughput excluding protocol overhead and retransmissions.
2. Throughput is the actual measure of data successfully transferred over time, accounting for real-world limitations.
3. Bandwidth is the theoretical maximum capacity of a communications channel, measured in bits per second.
</details>