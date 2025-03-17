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

**Virtualization** is the main enabling technology for cloud computing. It refers to the partitioning of a single physical server into multiple logical servers, where each logical server behaves like a physical server and can run an operating system and applications independently.

A **hypervisor** is software that runs virtual machines and manages the virtualization.

**Key aspects of virtualization**:
- **Partitioning**: Single physical system providing many applications and OS's
- **Isolation**: Each VM is isolated from other VMs (one crashing doesn't affect others)
- **Encapsulation**: VM can be presented to an application as an entity

**Types of virtualization**:
- **Network Virtualization**: Combining available resources in a network by splitting bandwidth into channels
- **Storage Virtualization**: Pooling physical storage from multiple devices (e.g., SANs)
- **Server Virtualization**: Masking server resources (processors, RAM, OS) to increase resource sharing

Virtualization enables cloud computing by allowing efficient utilization of hardware, isolation between different users/applications, and flexible allocation of resources.
</details>

**Q4: Compare grid computing and cloud computing.**
<details>
<summary>Answer</summary>

| Grid Computing | Cloud Computing |
|----------------|-----------------|
| Application oriented | Service oriented |
| Tasks divided into sub-tasks and allocated to machines | Provides services on demand |
| Interconnected computers working on a large-scale task | Accessed via internet |
| Usually owned by an organization within a corporate network | Owned by an infrastructure provider |
| Management is decentralized | Management is centralized |
</details>

**Q5: What are the types of hypervisors?**
<details>
<summary>Answer</summary>

1. **Type 1 (Native)**:
    - Sit directly on the hardware
    - Example: Microsoft Hyper-V

2. **Type 2 (Hosted)**:
    - Run as software on other hardware and OS
    - Example: VMware Player
</details>

## Week 2: Cloud Service Models and Deployment Types

**Q6: What are the three main cloud service models?**
<details>
<summary>Answer</summary>

1. **Software as a Service (SaaS)**:
    - Complete application offered as a service on demand
    - Single instance serves multiple users/organizations
    - Users don't manage the infrastructure
    - Examples: Google Apps, Salesforce, MailChimp, Slack

2. **Platform as a Service (PaaS)**:
    - Development environment encapsulated and offered as a service
    - Users deploy applications using languages/tools supported by the provider
    - Users control deployed apps but not underlying infrastructure
    - Examples: Google App Engine, Force.com, AWS Elastic Beanstalk

3. **Infrastructure as a Service (IaaS)**:
    - Provision of processing, storage, networks, and computing resources
    - Users can deploy arbitrary software including OS and applications
    - Users control OS, storage, and apps but not underlying infrastructure
    - Examples: AWS EC2, Rackspace, Google Compute Engine
</details>

**Q7: What are the cloud deployment model types?**
<details>
<summary>Answer</summary>

1. **Public Cloud**:
    - Available for all
    - Third-party service provider makes services, storage, and resources available

2. **Private Cloud**:
    - Available within an organization
    - Used by a single organization; can be internally or externally hosted

3. **Hybrid Cloud**:
    - Combination of public and private cloud types
    - Usually private for sensitive data and strategic applications with public services

4. **Community Cloud**:
    - Shared by several organizations
    - A collaborative platform used by several distinct organizations to share applications
</details>

**Q8: What is the "cake analogy" for cloud service models?**
<details>
<summary>Answer</summary>

The cake analogy compares cloud service models to different ways of getting a cake:

1. **Traditional On-Premises (Make from scratch)**:
    - You control everything
    - Need all ingredients and equipment
    - Requires most effort and expertise

2. **IaaS (Pre-mixed ingredients)**:
    - Basic ingredients are provided
    - You still mix, bake, and decorate
    - Requires significant effort but less than from scratch

3. **PaaS (Cake in a pan, ready to bake)**:
    - Most components prepared for you
    - You just bake and decorate
    - Requires moderate effort

4. **SaaS (Fully baked cake from bakery)**:
    - Complete product ready to use
    - No preparation required
    - Minimal effort but least control
</details>

**Q9: What are the key cloud application design principles?**
<details>
<summary>Answer</summary>

1. **Scaling elasticity**:
    - Horizontal (more machines/workers)
    - Vertical (more compute power - CPUs)
    - Identify bottlenecks (e.g., split read/write databases)

2. **Redundancy**:
    - Replicate databases
    - Partition data:
        - Horizontal shards (subsets of data, e.g., customers A-H)
        - Vertical (frequently vs. less frequently used fields)
        - Functional (access by context - invoices vs. inventory)

3. **Error correction**:
    - Self-healing (degrade gracefully, focus on critical functions)
    - Failover (run multiple instances/workers)

4. **Evolution**:
    - High cohesion, loose coupling
    - Restricted interfaces to minimize dependency changes
</details>

**Q10: What are some common cloud design patterns and their purposes?**
<details>
<summary>Answer</summary>

**Availability Patterns**:
- **Queue-based Load Leveling**: Buffer between tasks and services
- **Throttling**: Control resource consumption by setting limits

**Data Management Patterns**:
- **Cache-Aside**: Load data from store and improve repeat access
- **Sharding**: Horizontal/vertical database partitioning

**Design and Implementation Patterns**:
- **Backends for Frontends**: Customize backends for specific frontend needs
- **Static Content Hosting**: Deliver static web pages separately

**Messaging Patterns**:
- **Priority Queue**: Support different service level agreements
- **Asynchronous Request-Reply**: Decouple backend from frontend processing

**Resiliency Patterns**:
- **Retry**: Handle faults transparently
- **Bulkhead**: Isolate application elements into pools for fault tolerance

**Security Patterns**:
- **Federated Identity**: Delegate authentication to external provider
- **Valet Key**: Client token for managing restricted access
</details>

## Week 3: Cloud Architecture and Services

**Q11: What's the difference between N-tier and Microservices architecture?**
<details>
<summary>Answer</summary>

**N-tier Architecture**:
- Traditional architecture dividing application into layers
- Typically includes presentation, business logic, and data access layers
- Often used with IaaS
- **Strengths**: Natural fit for migration from traditional systems
- **Weaknesses**: Updating layered systems can be difficult depending on modularity

**Microservices Architecture**:
- Software made up of small independent services
- Each service provides a single capability
- Services are loosely coupled and communicate through APIs
- Implementation can change as long as API remains consistent
- **Strengths**: Works well with complexity, innovation, and high-velocity updates
- **Weaknesses**: Requires appropriate development culture
</details>

**Q12: What are containers and how do they differ from virtual machines?**
<details>
<summary>Answer</summary>

**Containers**:
- Standalone, all-in-one packages including executable and dependencies
- Can run on laptop, server, or virtual machine
- Portable, scalable, and individualized
- Share the host OS kernel but have isolated user spaces

**Virtual Machines (VMs)**:
- Complete OS and application running on hypervisor
- Include full copy of an OS, application, binaries, and libraries
- Typically several GB in size

**Key Differences**:
- Containers are lighter weight (MB vs GB)
- Containers start in seconds vs minutes for VMs
- Containers share the OS kernel while VMs have complete OS copies
- VMs provide stronger isolation but with higher resource overhead
</details>

**Q13: What are some key AWS services for computing and containers?**
<details>
<summary>Answer</summary>

1. **Elastic Compute Cloud (EC2)**:
    - Most common building block
    - Create virtual computers with chosen OS, memory, compute power
    - Common use case: Web applications
    - Can be scaled with load balancers, Cloud Watch, and Auto Scaling

2. **Elastic Beanstalk**:
    - Includes auto-scaling for instances
    - Automates setup while allowing control of underlying instances

3. **Lightsail**:
    - Simplified deployment (e.g., WordPress site)
    - Less control but easier to use
    - Always-running server in the cloud

4. **Lambda (Serverless Computing)**:
    - Functions as a Service (FaaS)
    - No always-running server required
    - Triggered by events
    - Pay only for computing power used

5. **Container Services**:
    - **Docker**: Platform for creating, deploying, running containers
    - **Kubernetes**: Platform for orchestrating containers
    - **Elastic Container Service**: AWS service for managing containers
    - **App Runner**: Automates working with and deploying containers
</details>

**Q14: What is a typical web app architecture in the cloud?**
<details>
<summary>Answer</summary>

A typical modern web application might include:

1. **Front Door**: Load balancer that routes HTTP requests and provides security

2. **Content Delivery Network (CDN)**: Caches content for lower latency and faster delivery

3. **Web Front End**: Organizes requests for frontend interactivity, using app service plan and queue function

4. **Data Storage & Cache**:
    - Cache for frequent requests
    - Database for persistent data
    - Cosmos DB for global service

5. **Authentication**:
    - Active Directory for user authentication

6. **Infrastructure Services**:
    - DNS hosting
    - App service plan (provides VMs)
    - Storage blob (unstructured data)
</details>

## Week 4: Cloud Data and Analytics

**Q15: What are the main cloud data services offered by AWS?**
<details>
<summary>Answer</summary>

1. **Simple Storage Service (S3)**:
    - General object storage
    - Based on Amazon's internal storage system

2. **Elastic Block Storage (EBS)**:
    - Fast storage for data-intensive apps
    - Highly configurable

3. **Elastic File System (EFS)**:
    - Fast storage for data-intensive apps
    - Fully managed but higher cost

4. **Relational Database Service (RDS)**:
    - SQL database with high throughput
    - Scaling and backup capabilities
    - Used for mobile/online games

5. **Elastic Cache**:
    - Used with RDS for fast performance and low latency

6. **Aurora**:
    - SQL database compatible with MySQL
    - Includes serverless option (pay for database access only)

7. **Timestream**:
    - Time series database with built-in time-based queries

8. **Neptune**:
    - Graph database for highly connected data sets
    - Used for social graphs and recommendation engines
</details>

**Q16: What is the difference between a data lake and a data warehouse?**
<details>
<summary>Answer</summary>

**Data Lake (e.g., AWS Lake Formation)**:
- Stores unstructured data
- Raw data in its native format
- Flexible schema
- Used for varied data types and exploratory analysis

**Data Warehouse (e.g., AWS Redshift)**:
- Stores structured data
- Processed data with defined schema
- Used for business intelligence and reporting

Both are often used in preparation for data analysis.
</details>

**Q17: What are some AWS data analytics services?**
<details>
<summary>Answer</summary>

1. **Kinesis**: Real-time data analytics

2. **Glue**:
    - ETL (Extract, Transform, Load) service
    - Automates data preparation

3. **Glue Studio**: Code-free, serverless ETL

4. **Data Exchange**: Purchase data from third parties (e.g., market research)

5. **SageMaker**: Comprehensive machine learning platform
</details>

**Q18: Explain the difference between data analysis and machine learning.**
<details>
<summary>Answer</summary>

**Data Analysis**:
- Searching large stores of data to discover patterns and trends
- Uses statistical methods to understand existing data
- Focuses on summarizing past data to derive insights
- Examples: regression analysis, network analysis, sentiment analysis

**Machine Learning**:
- Uses sophisticated mathematical algorithms to segment data and evaluate probability of future events
- Builds models that learn from data to make predictions or decisions
- Focus on using past data to predict future outcomes
- Examples: image recognition, recommendation systems, natural language processing
</details>

**Q19: What are some machine learning techniques and applications?**
<details>
<summary>Answer</summary>

**Techniques**:
- **Support Vector Machines (SVM)**: Finds optimal boundaries between data classes
- **Neural Networks**: Layered structures mimicking human brain connections
- **Regression Models**: Predict relationships between variables
- **Clustering**: Group similar data points together

**Applications**:
1. **Search Engine Refinement**:
    - Algorithms watch user responses to search results
    - Learn from user behavior to improve future results

2. **Virtual Personal Assistants** (e.g., Alexa):
    - Collect and refine information based on previous interactions
    - Tailor results to user preferences

3. **Social Media Features**:
    - Friend suggestions based on connections and interactions
    - Face recognition in photos
    - Similar content recommendations (e.g., Pinterest pins)

4. **Image Style Transfer**:
    - Applying artistic styles to photographs
    - Generating new images with characteristics of input samples
</details>

## Week 5: Cloud Issues and Considerations

**Q20: What is a SWOT analysis of cloud computing?**
<details>
<summary>Answer</summary>

**Strengths**:
- Flexibility
- Scalability
- Reliability
- Availability
- Resilience
- Sustainability

**Weaknesses**:
- Dependency - vendor lock-in
- Data ownership
- Infrastructure requirements
- Inherent latency (operation time)
- Service quality guarantees
- Legacy systems and migration challenges

**Opportunities**:
- Ease of utilization
- Simplified maintenance and upgrade
- Access to services for innovation
- Lower cost
- Low barrier to entry
- Energy saving

**Threats**:
- Cross compatibility issues
- Hidden costs
- Knowledge & expertise requirements
- Adoption resistance
- Security concerns
- Geopolitical factors
</details>

**Q21: What is the shared responsibility model in cloud computing?**
<details>
<summary>Answer</summary>

The shared responsibility model defines what security responsibilities belong to the cloud provider versus the customer:

**Cloud Provider Typically Responsible For**:
- Physical security of data centers
- Network infrastructure
- Hypervisor security
- Host operating system security

**Customer Typically Responsible For**:
- Data security and encryption
- Identity and access management
- Application security
- Operating system security (for IaaS)
- Network and firewall configuration

The exact division varies by service model:
- In IaaS, customers have more responsibility
- In PaaS, responsibilities are more evenly shared
- In SaaS, the provider handles most security aspects

Understanding this model is crucial for proper cloud security implementation.
</details>

**Q22: What are the main security concerns in cloud computing?**
<details>
<summary>Answer</summary>

**Traditional Security Concerns**:
- User authentication
- Data integrity
- Confidentiality
- Distributed Denial of Service (DDoS) attacks

**Cloud-Specific Security Concerns**:
- Managing traditional threats in a complex environment
- Need for security automation tools
- Gaps in customer and provider responsibilities
- "Leaky buckets" (e.g., poorly configured Amazon S3 storage)
    - Example breaches: WWE, Verizon Wireless, Time Warner Cable

**Security Best Practices**:
- Clear consistent leadership/management
- Proactive monitoring
- Intrusion detection (ID/authentication, behavior anomaly)
- Micro-segmentation of resources
</details>

**Q23: What is data localization and why is it important?**
<details>
<summary>Answer</summary>

**Data Localization**:
- Legal requirements to store data within the borders of specific countries or regions
- Varies by jurisdiction (e.g., Europe vs. Asia have different requirements)

**Importance**:
- Compliance with local data protection laws
- Jurisdictional control over data
- Protection of citizens' privacy
- National security concerns

Cloud providers must manage these requirements across their global infrastructure, often creating region-specific data centers to accommodate these laws.
</details>

## Week 6: Networks Introduction

**Q24: What is a computer network?**
<details>
<summary>Answer</summary>

Interconnected computing devices that can exchange data and share resources with each other using communications protocols over physical or wireless technologies.
</details>

**Q25: What are the three categories of network components?**
<details>
<summary>Answer</summary>

1. **End Devices** - Interface between humans and communication networks (computers, printers, VoIP phones, mobile devices)
2. **Intermediary Devices** - Network infrastructure (switches, routers, wireless access points, firewalls)
3. **Media** - Connectivity (metallic cables, fiber optic cables, wireless transmission)
</details>

**Q26: What are the two main functions of intermediary devices?**
<details>
<summary>Answer</summary>

1. Filter the flow of data based on security settings
2. Direct data (e.g., along alternate pathways where there is a link failure)
</details>

**Q27: Compare peer-to-peer and client-server networks.**
<details>
<summary>Answer</summary>

**Peer-to-Peer:**
- **Advantages**: Easy to set up, less complex, lower cost
- **Disadvantages**: No centralized administration, not as secure, not scalable, lower performance

**Client-Server:**
- **Advantages**: Centralized administration, more secure, scalable, higher performance
- **Disadvantages**: Harder to set up, more complex, higher cost
</details>

**Q28: Describe the different network physical topologies.**
<details>
<summary>Answer</summary>

- **Bus**: All nodes attached to a shared medium; easy to extend but prone to collisions and cable cuts can be catastrophic
- **Star**: All nodes connect to a central point; high performance but central point is single point of failure
- **Mesh**: All nodes connect directly to each other; high performance but high cost, fault-tolerant but low scalability
- **Ring**: Nodes form a circle; uses token to solve collision problems but token loss becomes an issue
- **Tree**: Hierarchical structure typically used by telecoms (e.g., cable TV)
</details>

**Q29: What is the difference between circuit-switched and packet-switched networks?**
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

**Q30: What is message encoding?**
<details>
<summary>Answer</summary>

Encoding is the process of converting information into another acceptable form for transmission. Decoding reverses this process to interpret the information.

For network transmission:
1. Messages are converted into bits by the sending host
2. Each bit is encoded into patterns (sounds, light waves, electrical impulses) based on the network media
3. The destination host receives and decodes the signals
</details>

**Q31: What is segmentation and why is it important?**
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

**Q32: What is encapsulation in networking?**
<details>
<summary>Answer</summary>

Encapsulation is the process of placing one message format inside another message format. In networking, this means adding headers and sometimes trailers to data as it moves down the protocol stack.

De-encapsulation is the reverse process that occurs when the recipient removes the encapsulation layers.
</details>

## Week 6: Network Models and Protocols

**Q33: What is a protocol in networking?**
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

**Q34: What is the difference between a protocol model and a protocol suite?**
<details>
<summary>Answer</summary>

- **Protocol Model**: A framework for understanding how protocols work (e.g., OSI model)
- **Protocol Suite**: A collection of inter-related protocols (e.g., TCP/IP suite)
</details>

**Q35: Describe the OSI model and its layers.**
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

**Q36: Compare the OSI model and the TCP/IP model.**
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

**Q37: What are Protocol Data Units (PDUs) and how do they change across layers?**
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

**Q38: What happens during encapsulation and de-encapsulation?**
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

**Q39: What is the role of the Application Layer (Layer 7)?**
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

**Q40: What is the role of the Presentation Layer (Layer 6)?**
<details>
<summary>Answer</summary>

The Presentation Layer has three primary functions:
1. **Data Formatting**: Converts data from the application layer into a machine-readable form (e.g., ASCII to binary)
2. **Compression**: Can be lossless (precise, no data lost) or lossy (approximation, data lost but smaller)
3. **Encryption/Decryption**: Secures data for transmission (e.g., SSL protocol)
</details>

**Q41: What is the role of the Session Layer (Layer 5)?**
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

**Q42: What are the main functions of the Transport Layer?**
<details>
<summary>Answer</summary>

The Transport Layer is responsible for four basic processes:
1. **Message Segmentation**: Dividing data streams into smaller pieces
2. **Transfer & Reassembly**: Tracking individual communications between applications
3. **Error Control**: Handling lost or corrupted packets
4. **Flow Control**: Managing data transmission rates
</details>

**Q43: Compare TCP and UDP protocols.**
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

**Q44: What are port numbers and what is their purpose?**
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

**Q45: What is a socket in networking?**
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

**Q46: What are the main functions of the Network Layer?**
<details>
<summary>Answer</summary>

The Network Layer is responsible for:
1. **Routing & Path Determination**: Selecting the best path for data packets
2. **Addressing**: Providing logical addressing for end devices
</details>

**Q47: What is routing and how does it work?**
<details>
<summary>Answer</summary>

Routing is the process of directing packets to a destination host on another network:
- Packets must be processed by a router to travel to other networks
- Routers select paths and direct packets toward the destination host
- Each part of the route a packet takes is called a hop
- Path determination algorithms like OSPF (Open Shortest Path First) find the best route
</details>

**Q48: Explain IP addressing.**
<details>
<summary>Answer</summary>

IP addressing is a key function of network layer protocols:
- Enables data communication between hosts on same or different networks
- Both IPv4 and IPv6 provide hierarchical addressing
- An IP address has two parts: network prefix and host part
    - Network address: used by routers to forward packets to the proper network
    - Host address: used by the last router to deliver to the destination device
</details>

**Q49: What are the different types of IP addresses?**
<details>
<summary>Answer</summary>

- **Public IP**: Assigned to devices connected to the internet for global communication
- **Private IP**: Used within private networks for internal communication
- **Static IP**: Remains the same over time (used for servers, remote access)
- **Dynamic IP**: Assigned dynamically and can change (common for home internet)
</details>

**Q50: What is a subnet mask and how does it work?**
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

**Q51: What is Network Address Translation (NAT) and what issues does it have?**
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

**Q52: Compare IPv4 and IPv6.**
<details>
<summary>Answer</summary>

**IPv4**:
- 32-bit addresses (approximately