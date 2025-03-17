# Fundamentals of Networks and Cloud Computing: Q&A Study Guide

## Week 1: Introduction to Cloud Computing

**Q1: What is cloud computing according to NIST?**
<details>
<summary>Answer</summary>

According to the National Institute of Standards and Technology (NIST), cloud computing is:

"A model for enabling convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction."

This cloud model promotes availability and is composed of five essential characteristics, three service models, and four deployment models.
</details>

**Q2: What are the five essential characteristics of cloud computing?**
<details>
<summary>Answer</summary>

1. **On-demand self-service**: Users can provision computing capabilities automatically without requiring human interaction with service providers

2. **Broad network access**: Capabilities are accessible over the network through standard mechanisms by heterogeneous client platforms (e.g., mobile phones, tablets, laptops)

3. **Multi-tenancy/Resource pooling**: Provider's resources are pooled to serve multiple consumers using a multi-tenant model, with resources dynamically assigned according to demand

4. **Rapid elasticity**: Capabilities can be elastically provisioned and released to scale rapidly with demand; resources appear unlimited to consumers

5. **Measured service**: Resource usage is monitored, controlled, reported, and charged using metering capability
</details>

**Q3: What is virtualization and how does it enable cloud computing?**
<details>
<summary>Answer</summary>

**Virtualization** is the main enabling technology for cloud computing. It involves partitioning a single physical server into multiple logical servers, each capable of running an operating system and applications independently.

Key aspects:
- **Separates** resources and services from the physical system
- **Partitioning**: Single physical system providing many applications and OS's
- **Isolation**: Each VM is isolated from others; if one crashes, it doesn't affect others
- **Encapsulation**: VM can be presented as an entity; application crashes don't affect others

A **hypervisor** is software that runs virtual machines and can be:
- **Type 1 (Native)**: Sits directly on hardware (e.g., MS Hyper-V)
- **Type 2 (Hosted)**: Runs as software on other hardware/OS (e.g., VMware Player)

Virtualization enables cloud computing by allowing efficient resource utilization, isolation, and dynamic allocation.
</details>

**Q4: Compare Grid Computing and Cloud Computing.**
<details>
<summary>Answer</summary>

**Grid Computing**:
- Application oriented
- Tasks are divided into sub-tasks and allocated to machines
- Interconnected computers working on a large-scale task
- Usually owned by an organization within a corporate network
- Management is decentralized

**Cloud Computing**:
- Service oriented
- Provides services on demand
- Accessed via internet
- Owned by an infrastructure provider
- Management is centralized
</details>

**Q5: What are the benefits of cloud computing from a consumer perspective?**
<details>
<summary>Answer</summary>

From a consumer perspective, cloud computing offers:
- Accessibility via a browser or web service API
- No need to buy computer hardware/software
- Pay-for-use model (only pay for what you use)
- Scalability to handle varying workloads
- Reduced maintenance overhead
- Access to advanced services and technologies
</details>

## Week 2: Cloud Models and Patterns

**Q6: Describe the three main cloud service models.**
<details>
<summary>Answer</summary>

1. **Software as a Service (SaaS)**:
    - A complete application offered as a service on demand
    - Single instance serves multiple end users/organizations
    - Users access via client devices
    - Users don't manage underlying infrastructure
    - Examples: Google Apps, Salesforce, Microsoft 365, Slack

2. **Platform as a Service (PaaS)**:
    - Development environment offered as a service
    - Users deploy applications using provider-supported languages/tools
    - Users control deployed apps but not underlying infrastructure
    - Examples: Google App Engine, AWS Elastic Beanstalk, Heroku, Microsoft Azure

3. **Infrastructure as a Service (IaaS)**:
    - Provision of fundamental computing resources (processing, storage, networks)
    - Users deploy and run arbitrary software including OS and applications
    - Users control OS, storage, and applications but not underlying cloud infrastructure
    - Examples: AWS EC2, Google Compute Engine, Microsoft Azure IaaS
</details>

**Q7: What is the relationship between control and convenience in cloud service models?**
<details>
<summary>Answer</summary>

There's an inverse relationship between control and convenience across the service models:

- **IaaS**: Highest control, lowest convenience
    - Users manage OS, middleware, runtime, applications
    - More administration responsibility

- **PaaS**: Medium control, medium convenience
    - Users manage applications and data
    - Provider manages runtime, middleware, OS

- **SaaS**: Lowest control, highest convenience
    - Users only manage their data and limited configuration
    - Everything else is managed by the provider

This trade-off is often compared to making a cake:
- IaaS: Making from scratch with basic ingredients
- PaaS: Using a pre-made mix but still baking yourself
- SaaS: Buying a fully prepared cake
</details>

**Q8: What are the four cloud deployment models?**
<details>
<summary>Answer</summary>

1. **Public Cloud**:
    - Available to all users
    - Provided by third-party service providers
    - Resources available to general public
    - Examples: AWS, Microsoft Azure, Google Cloud

2. **Private Cloud**:
    - Available within a single organization
    - Can be internally or externally hosted
    - Used by a single organization
    - Greater control and security

3. **Hybrid Cloud**:
    - Combination of public and private cloud types
    - Usually private for sensitive data and strategic applications
    - Public for less critical services
    - Allows data and application portability

4. **Community Cloud**:
    - Shared by several organizations
    - Collaborative platform for distinct organizations
    - Shared applications and common concerns
    - Example: Government clouds shared by multiple agencies
</details>

**Q9: What are the key cloud application design principles?**
<details>
<summary>Answer</summary>

Key cloud application design principles include:

1. **Scaling elasticity**:
    - Horizontal scaling: Adding more machines/workers
    - Vertical scaling: Adding more compute power (CPUs)
    - Identifying bottlenecks (e.g., split read/write databases)

2. **Redundancy**:
    - Replicating databases (with integrity resolution)
    - Partitioning data:
        - Horizontal shards (e.g., customers A-H)
        - Vertical (frequently vs. rarely used fields)
        - Functional (access by context)

3. **Error correction**:
    - Self-healing (degrade gracefully, focus on critical functions)
    - Failover (run multiple instances/workers)

4. **Evolution**:
    - High cohesion, loose coupling
    - Restricted interfaces
</details>

**Q10: What are some common cloud design patterns and their purposes?**
<details>
<summary>Answer</summary>

Cloud design patterns address specific challenges:

**Availability**:
- Queue-based Load Leveling: Buffers between tasks and services
- Throttling: Controls resource consumption by setting limits

**Data Management**:
- Cache-Aside: Improves repeat access performance
- Sharding: Horizontal/vertical database partitioning

**Design and Implementation**:
- Backends for Frontends: Specialized backends for different client types
- Static Content Hosting: Separate delivery of static web content

**Messaging**:
- Priority Queue: Handles different service level agreements
- Asynchronous Request-Reply: Decouples frontend from backend processing

**Resiliency**:
- Retry: Transparent fault handling
- Bulkhead: Isolates application elements into pools

**Security**:
- Federated Identity: Delegates authentication to external providers
- Valet Key: Client token for managing restricted access
</details>

## Week 3: Cloud Architecture and Services

**Q11: What is the difference between N-tier architecture and Microservices architecture?**
<details>
<summary>Answer</summary>

**N-tier Architecture**:
- Traditional architecture dividing application into layers
- Typical layers: presentation, business logic, data access
- Often used with IaaS
- **Strengths**: Natural fit for migration from on-premises
- **Weaknesses**: Updating layered systems can be difficult depending on modularity

**Microservices Architecture**:
- Software made up of small independent services
- Each service provides a single capability
- Services communicate through APIs
- Implementation can change as long as API remains consistent
- **Strengths**: Works well with complexity, innovation, and high-velocity updates
- **Weaknesses**: Requires correct development team culture and infrastructure
</details>

**Q12: What is a container in cloud computing?**
<details>
<summary>Answer</summary>

A **container** is a standalone, all-in-one package that includes an executable and all its dependencies. Key characteristics:

- Self-contained unit that can run on a laptop, server, or virtual machine
- Portable across different environments
- Scalable for different workloads
- Provides isolation between applications

Containers differ from virtual machines:
- Containers share the host OS kernel but have isolated user spaces
- VMs have their own OS and kernel
- Containers are lighter, start faster, and use fewer resources than VMs

Common container technologies:
- **Docker**: Open-source platform for creating, deploying, and running containers
- **Kubernetes**: Platform for orchestrating containers (deployment, scaling, management)
</details>

**Q13: Describe the basic components of a typical cloud web application architecture.**
<details>
<summary>Answer</summary>

A typical cloud web application architecture includes:

1. **Front Door/Load Balancer**: Routes HTTP requests to web front end, provides security

2. **Content Delivery Network (CDN)**: Caches publicly available content for lower latency

3. **Web Front End**: Organizes requests for frontend interactivity, uses app service plan and queue functions

4. **Data Storage & Cache**:
    - Cache for frequent requests
    - Database for persistent data
    - Global services (e.g., Cosmos DB)

5. **Authentication**: Services like Active Directory for user authentication

6. **DNS**: Hosting service for domain names

Key services involved:
- App Service: Platform for creating/deploying apps
- App Service Plan: Provides VMs
- SQL Server: Logical view of databases
- Storage Blob: Object storage for unstructured data
</details>

**Q14: What are some examples of specialized cloud services for different industries?**
<details>
<summary>Answer</summary>

Cloud providers offer specialized services for different industries and use cases:

**Movie Recommendations**:
1. Front-end website collects user-movie interaction data
2. Historical data stored in blob storage
3. Data Science Virtual Machine (DSVM) used for experimentation
4. Machine Learning coordinates experimentation
5. Trained model preserved in database
6. Model deployed to web/app service

**Games**:
1. Traffic Manager directs client requests to appropriate endpoints
2. Game-specific backend services (e.g., PlayFab)
3. CDN and Storage for cached content and game resources
4. Databases for game data and analytics
5. Leaderboard implementation with caching for performance

These specialized services allow for optimized industry-specific solutions without rebuilding basic infrastructure.
</details>

## Week 4: Cloud Data

**Q15: What are the main types of cloud data services?**
<details>
<summary>Answer</summary>

Cloud providers offer various data services:

**Storage Services**:
- **Simple Storage Service (S3)**: General object storage
- **Elastic Block Storage**: Fast storage for data-intensive apps
- **Elastic File System**: Fully managed, fast file storage

**Database Services**:
- **Relational Database Service (RDS)**: SQL databases with high throughput
- **Aurora**: SQL database compatible with MySQL
- **Elastic Cache**: For use with RDS, provides low-latency performance
- **Timestream**: Time series database
- **Neptune**: Graph database for highly connected datasets

**Data Preparation**:
- **Lake Formation**: Data lake for unstructured data
- **Redshift**: Data warehouse for structured data
- **Glue**: ETL (Extract, Transform, Load) service that automates data preparation
- **Data Exchange**: For purchasing third-party data
</details>

**Q16: What is data analysis in the context of cloud computing?**
<details>
<summary>Answer</summary>

**Data Analysis** in cloud computing involves searching large stores of data to discover patterns and trends that go beyond simple analysis. Common techniques include:

1. **Support Vector Machine (SVM)**: Finds a line or hyperplane that best separates groups of data points

2. **Regression Analysis**: Predictive modeling technique that investigates relationships between dependent and independent variables; used for forecasting and finding causal relationships

3. **Network Analysis**: Family of algorithms based on graph theory that examines relationships between nodes; used in social media and search engines (e.g., Google PageRank)

4. **Sentiment Analysis**: Identifies and categorizes opinions in text data to determine attitudes (positive, negative, neutral) toward products, brands, or services
</details>

**Q17: What is machine learning in the cloud and what are its applications?**
<details>
<summary>Answer</summary>

**Machine Learning (ML)** in the cloud involves training predictive models based on mathematical algorithms to analyze relationships between data points and predict unknown values.

The ML process typically includes:
1. Exploring source data to determine relationships
2. Training and validating models to find optimal prediction
3. Deploying the optimal model as a service

Common cloud applications of ML:
- **Search Engine Refinement**: Learning from user interactions with results
- **Virtual Personal Assistants**: Collecting and refining information based on previous interactions
- **Social Media**: Friend suggestions, face recognition, content recommendations
- **Image Style Transfer**: Applying artistic styles to images
- **Recommendation Systems**: Suggesting products, content, or connections

Cloud providers offer ML services like:
- **SageMaker** (AWS)
- **Azure ML** (Microsoft)
- **Rekognition** (image processing)
- **Lex** (speech processing)
</details>

## Week 5: Cloud Issues

**Q18: What are the key strengths of cloud computing?**
<details>
<summary>Answer</summary>

Key strengths of cloud computing include:

- **Flexibility**: Various service models (IaaS, PaaS, SaaS) to meet different needs
- **Scalability**: Ability to scale up/down resources in response to demand
- **Elasticity**: Dynamic adaptation to traffic fluctuations
- **Reliability**: Services consistently available over time
- **Availability**: Services working properly when accessed
- **Resilience**: Services working despite changing circumstances
- **Sustainability**: Potential for more efficient resource utilization
</details>

**Q19: What are the main weaknesses of cloud computing?**
<details>
<summary>Answer</summary>

Major weaknesses of cloud computing include:

- **Dependency/Vendor Lock-in**: Difficulty moving between cloud providers
- **Data Ownership**: Questions about who controls data and derived insights
- **Infrastructure Requirements**: Need for reliable, high-bandwidth connectivity
- **Inherent Latency**: Operations potentially slower than on-premises
- **Service Quality Guarantees**: Limited compensation for outages
- **Legacy Systems and Migration**: Challenges in moving existing systems to cloud
</details>

**Q20: What are the opportunities presented by cloud computing?**
<details>
<summary>Answer</summary>

Key opportunities of cloud computing:

- **Ease of Utilization**: Simple selection of services
- **Simplified Maintenance/Upgrade**: Centralized management
- **Access to Services for Innovation**: Advanced data analysis and machine learning
- **Lower Cost**: Potential cost savings (capital vs. operational expenses)
- **Low Barrier to Entry**: Easier for small businesses to access enterprise-grade technology
- **Energy Saving**: Potential reduction in energy consumption through shared resources
</details>

**Q21: What are the threats or challenges when adopting cloud computing?**
<details>
<summary>Answer</summary>

Significant threats and challenges to cloud adoption:

- **Cross-Compatibility**: Issues moving between different cloud platforms
- **Hidden Costs**: Unexpected expenses, especially for advanced features
- **Knowledge & Expertise**: Steep learning curves and specialized skills required
- **Adoption Resistance**: Organizational reluctance to change
- **Security**: Traditional and new threats in a complex environment
- **Geopolitics**: Data sovereignty and international legal concerns
</details>

**Q22: What is the Shared Responsibility Model in cloud security?**
<details>
<summary>Answer</summary>

The **Shared Responsibility Model** defines how security responsibilities are divided between cloud providers and customers:

**Cloud Provider Responsibilities** typically include:
- Physical security of data centers
- Network infrastructure
- Host infrastructure
- Virtualization layer

**Customer Responsibilities** typically include:
- Data security and encryption
- Identity and access management
- Application security
- Operating system configuration

The exact division varies by service model:
- In **IaaS**, customers have more security responsibilities
- In **PaaS**, some responsibilities shift to the provider
- In **SaaS**, providers handle most security aspects, but customers retain responsibility for data and access management

Understanding this model is crucial to ensuring comprehensive security coverage without gaps.
</details>

## Week 6: Networks Introduction

**Q23: What is a computer network?**
<details>
<summary>Answer</summary>

Interconnected computing devices that can exchange data and share resources with each other using communications protocols over physical or wireless technologies.
</details>

**Q24: What are the three categories of network components?**
<details>
<summary>Answer</summary>

1. **End Devices** - Interface between humans and communication networks (computers, printers, VoIP phones, mobile devices)
2. **Intermediary Devices** - Network infrastructure (switches, routers, wireless access points, firewalls)
3. **Media** - Connectivity (metallic cables, fiber optic cables, wireless transmission)
</details>

**Q25: What are the two main functions of intermediary devices?**
<details>
<summary>Answer</summary>

1. Filter the flow of data based on security settings
2. Direct data (e.g., along alternate pathways where there is a link failure)
</details>

**Q26: Compare peer-to-peer and client-server networks.**
<details>
<summary>Answer</summary>

**Peer-to-Peer:**
- **Advantages**: Easy to set up, less complex, lower cost
- **Disadvantages**: No centralized administration, not as secure, not scalable, lower performance

**Client-Server:**
- **Advantages**: Centralized administration, more secure, scalable, higher performance
- **Disadvantages**: Harder to set up, more complex, higher cost
</details>

**Q27: Describe the different network physical topologies.**
<details>
<summary>Answer</summary>

- **Bus**: All nodes attached to a shared medium; easy to extend but prone to collisions and cable cuts can be catastrophic
- **Star**: All nodes connect to a central point; high performance but central point is single point of failure
- **Mesh**: All nodes connect directly to each other; high performance but high cost, fault-tolerant but low scalability
- **Ring**: Nodes form a circle; uses token to solve collision problems but token loss becomes an issue
- **Tree**: Hierarchical structure typically used by telecoms (e.g., cable TV)
</details>

**Q28: What is the difference between circuit-switched and packet-switched networks?**
<details>
<summary>Answer</summary>

**Circuit-Switched Networks:**
- Establish dedicated end-to-end connection before data transfer (like early telephone systems)
- Connection remains even when no communication is occurring
- Limited number of circuits can be created

**Packet-Switched Networks:**
- Messages broken into packets with addressing information
- Packets can take various paths through the network
- Reassembled at destination
- Offers redundancy (multiple paths) and fault tolerance
- Modern networks and the Internet are packet-switched
</details>

## Week 6: Communication Concepts

**Q29: What is message encoding?**
<details>
<summary>Answer</summary>

Encoding is the process of converting information into another acceptable form for transmission. Decoding reverses this process to interpret the information.

For network transmission:
1. Messages are converted into bits by the sending host
2. Each bit is encoded into patterns (sounds, light waves, electrical impulses) based on the network media
3. The destination host receives and decodes the signals
</details>

**Q30: What is segmentation and why is it important?**
<details>
<summary>Answer</summary>

Segmentation is dividing data streams into smaller pieces for transmission.

**Advantages:**
- Different communications can be interleaved
- Increased reliability of network communications

**Disadvantage:**
- Increased level of complexity

The transport layer handles segmenting data for manageability and reassembling the segments at the destination.
</details>

**Q31: What is encapsulation in networking?**
<details>
<summary>Answer</summary>

Encapsulation is the process of placing one message format inside another message format. In networking, this means adding headers and sometimes trailers to data as it moves down the protocol stack.

De-encapsulation is the reverse process that occurs when the recipient removes the encapsulation layers.
</details>

## Week 6: Network Models and Protocols

**Q32: What is a protocol in networking?**
<details>
<summary>Answer</summary>

A protocol is a set of rules that determines:
- An identified sender and receiver
- Agreed upon method of communicating
- Common language and grammar
- Speed and timing of delivery
- Confirmation or acknowledgment requirements

Networking protocols define the formatting, addressing, routing, and error recovery methods for data transmission.
</details>

**Q33: What is the difference between a protocol model and a protocol suite?**
<details>
<summary>Answer</summary>

- **Protocol Model**: A framework for understanding how protocols work (e.g., OSI model)
- **Protocol Suite**: A collection of inter-related protocols (e.g., TCP/IP suite)
</details>

**Q34: Describe the OSI model and its layers.**
<details>
<summary>Answer</summary>

The OSI (Open Systems Interconnection) model is a conceptual framework with 7 layers:

1. **Physical**: Media, signal, and binary transmission
2. **Data Link**: Prepares data for transmission (MAC and LLC sub-layers); uses physical addressing
3. **Network**: Path determination and logical addressing (IP)
4. **Transport**: Segmentation, transfer, and reassembly; uses ports and sockets
5. **Session**: Manages data exchange and end-to-end connections
6. **Presentation**: Formats data (e.g., jpg) and handles encryption/decryption
7. **Application**: Network services to user applications (e.g., HTTP)

The OSI model provides an extensive list of functions that can occur at each layer and describes the interaction between layers.
</details>

**Q35: Compare the OSI model and the TCP/IP model.**
<details>
<summary>Answer</summary>

| OSI Model | Function | TCP/IP Model |
|-----------|----------|--------------|
| 7. Application<br>6. Presentation<br>5. Session | Network services, data formatting, connection management | Application |
| 4. Transport | Segmentation, transfer, reassembly | Transport (TCP, UDP) |
| 3. Network | Path determination, logical addressing | Internet (IPv4, IPv6) |
| 2. Data Link<br>1. Physical | Media access control, physical transmission | Network Access (Ethernet) |

The OSI model is a conceptual framework, while TCP/IP is implemented in software in all major operating systems.
</details>

## Week 7: Protocol Data Units (PDUs)

**Q36: What are Protocol Data Units (PDUs) and how do they change across layers?**
<details>
<summary>Answer</summary>

PDUs are the data units at each layer of the OSI model:

1. **Data** - Layer 7 (Application/Presentation/Session)
2. **Segment** - Layer 4 (Transport, including TCP)
3. **Packet** - Layer 3 (Network, including IP)
4. **Frame** - Layer 2 (Data Link, including Ethernet)
5. **Bit** - Layer 1 (Physical)

Data encapsulation order: data → segment → packet → frame → bit   
Data de-encapsulation order: bit → frame → packet → segment → data
</details>

**Q37: What happens during encapsulation and de-encapsulation?**
<details>
<summary>Answer</summary>

**Encapsulation** (transmitting data):
- Each layer adds its header to the data from the layer above
- E.g., the network layer adds IP header information to the segment from the transport layer, creating a packet

**De-encapsulation** (receiving data):
- Each layer removes the header information and passes the data to the layer above
- E.g., the network layer checks the packet's IP header and, if the destination matches, removes the header and passes the segment to the transport layer
</details>

## Week 7: Application, Presentation, and Session Layers (Layers 7, 6, 5)

**Q38: What is the role of the Application Layer (Layer 7)?**
<details>
<summary>Answer</summary>

The Application Layer:
- Is closest to the end user
- Provides the interface between applications and the network
- Is responsible for data representation
- Is NOT the layer of software applications themselves
- Common protocols: HTTP, HTTPS, FTP, TFTP, IMAP, DNS

These protocols enable web browsing, file transfer, emails, and virtual terminals. For example, browsers are not in the application layer but use application layer protocols like HTTP/HTTPS.
</details>

**Q39: What is the role of the Presentation Layer (Layer 6)?**
<details>
<summary>Answer</summary>

The Presentation Layer has three primary functions:
1. **Data Formatting**: Converts data from the application layer into a machine-readable form (e.g., ASCII to binary)
2. **Compression**: Can be lossless (precise, no data lost) or lossy (approximation, data lost but smaller)
3. **Encryption/Decryption**: Secures data for transmission (e.g., SSL protocol)
</details>

**Q40: What is the role of the Session Layer (Layer 5)?**
<details>
<summary>Answer</summary>

The Session Layer:
- Creates, maintains, secures, and terminates dialogs between source and destination applications
- Handles data exchange to initiate dialogs, keep them active, and restart disrupted sessions
- Is especially useful in multimedia applications for timing different data types (e.g., audio and video)
- Example protocols: Server Message Block (SMB), NetBIOS
- Keeps track of multiple file downloads (e.g., text and images on a web page)
- Handles authentication and authorization
</details>

## Week 8: Transport Layer (Layer 4)

**Q41: What are the main functions of the Transport Layer?**
<details>
<summary>Answer</summary>

The Transport Layer is responsible for four basic processes:
1. **Message Segmentation**: Dividing data streams into smaller pieces
2. **Transfer & Reassembly**: Tracking individual communications between applications
3. **Error Control**: Handling lost or corrupted packets
4. **Flow Control**: Managing data transmission rates
</details>

**Q42: Compare TCP and UDP protocols.**
<details>
<summary>Answer</summary>

**TCP (Transmission Control Protocol):**
- Provides reliable delivery ensuring all data arrives
- Uses acknowledged delivery
- Makes larger demands on the network (more overhead)
- Connection-oriented
- Used for applications requiring high reliability

**UDP (User Datagram Protocol):**
- Provides basic functions for delivery without reliability
- Less overhead on the network
- Connectionless
- Used for applications where speed is more important than reliability

Developers choose between TCP and UDP based on their application requirements, balancing reliability against network overhead.
</details>

**Q43: What are port numbers and what is their purpose?**
<details>
<summary>Answer</summary>

Port numbers are unique identifiers assigned to network protocols (TCP/UDP) to facilitate communication between devices.

- They determine which application or service should handle incoming data
- Enable multiple applications to coexist on a single device
- Allow for efficient data exchange across networks

Common port numbers:
- Port 80: HTTP (web browsing)
- Port 443: HTTPS (secure web browsing)
- Port 21: FTP (file transfer)
- Port 22: SSH (secure remote administration)
- Port 25: SMTP (email)
</details>

**Q44: What is a socket in networking?**
<details>
<summary>Answer</summary>

A socket is the combination of:
- Source IP address
- Destination IP address
- Source port number
- Destination port number

It uniquely identifies a communication session between applications. The IP address identifies the device/host, while the port number distinguishes between different applications on that device.
</details>

## Week 8: Network Layer (Layer 3)

**Q45: What are the main functions of the Network Layer?**
<details>
<summary>Answer</summary>

The Network Layer is responsible for:
1. **Routing & Path Determination**: Selecting the best path for data packets
2. **Addressing**: Providing logical addressing for end devices
</details>

**Q46: What is routing and how does it work?**
<details>
<summary>Answer</summary>

Routing is the process of directing packets to a destination host on another network:
- Packets must be processed by a router to travel to other networks
- Routers select paths and direct packets toward the destination host
- Each part of the route a packet takes is called a hop
- Path determination algorithms like OSPF (Open Shortest Path First) find the best route
</details>

**Q47: Explain IP addressing.**
<details>
<summary>Answer</summary>

IP addressing is a key function of network layer protocols:
- Enables data communication between hosts on same or different networks
- Both IPv4 and IPv6 provide hierarchical addressing
- An IP address has two parts: network prefix and host part
    - Network address: used by routers to forward packets to the proper network
    - Host address: used by the last router to deliver to the destination device
</details>

**Q48: What are the different types of IP addresses?**
<details>
<summary>Answer</summary>

- **Public IP**: Assigned to devices connected to the internet for global communication
- **Private IP**: Used within private networks for internal communication
- **Static IP**: Remains the same over time (used for servers, remote access)
- **Dynamic IP**: Assigned dynamically and can change (common for home internet)
</details>

**Q49: What is a subnet mask and how does it work?**
<details>
<summary>Answer</summary>

A subnet mask is a 32-bit number that:
- Separates IP addresses into network and host portions
- Determines which part of the IP address represents the network vs. the host
- Identifies the network address by "masking" the host portion
- Allows routers to efficiently route traffic between networks
- Enables efficient use of IP addresses and enhances security

Example: With mask 255.255.255.0, the first three octets identify the network, and the last octet identifies the host on that network.
</details>

**Q50: What is Network Address Translation (NAT) and what issues does it have?**
<details>
<summary>Answer</summary>

**NAT**: A technique that maps one IP address space into another, allowing multiple devices in a private network to share a single public IP address.

**How it works**:
- Data leaving private network: Source IP changed to public IP
- Data returning to private network: Destination IP translated back to appropriate private IP

**Benefits**:
- Conserves public IP addresses
- Enhances security by hiding internal addresses
- Enables internet connectivity for private network devices

**Issues**:
- Hampers direct peer-to-peer communication (VoIP, online gaming)
- Complicates hosting services (incoming connections blocked)
- Hinders IP-based identification (tracing malicious activities)
- Scalability issues in large networks
</details>

**Q51: Compare IPv4 and IPv6.**
<details>
<summary>Answer</summary>

**IPv4**:
- 32-bit addresses (approximately 4.3 billion addresses)
- Address depletion is a major issue
- Limited security features
- Requires NAT to extend address space

**IPv6**:
- 128-bit addresses (vastly larger address space)
- Improved packet handling
- Eliminates need for NAT
- Integrated security features
</details>

## Week 7-8: Protocol Implementation

**Q52: What is the TCP/IP Protocol Stack in action?**
<details>
<summary>Answer</summary>

The TCP/IP Protocol Stack in action involves multiple layers working together:

1. **Application Layer**: The data to be sent (e.g., HTML page from web server)
2. **Transport Layer**: TCP header is added to the data, creating segments and managing conversations between client and server
3. **Internet Layer**: IP header is added, creating packets with source/destination IP addresses
4. **Network Access Layer**: Ethernet information is added to both ends of the IP packet, creating a data link frame that can be delivered across the network

Each layer adds its own header information through encapsulation, and each receiving layer removes the corresponding header through de-encapsulation.
</details>
