# Mock Exam 1: Comprehensive Network Fundamentals

## Part 1: Option Selection Questions (10 marks)

For these questions, you'll need to select the appropriate option or options that correctly complete the statement or answer the question.

### Question 1
Select all the components that are classified as end devices in a network:
- [ ] Routers
- [ ] Computers
- [ ] Switches
- [ ] VoIP phones
- [ ] Firewalls
- [ ] Network printers
- [ ] Wireless access points

<details>
<summary>Show answer</summary>

**Answer:** Computers, VoIP phones, Network printers

*Explanation: End devices are the interfaces between humans and communication networks. They include computers, network printers, VoIP phones, and mobile devices. Routers, switches, firewalls, and wireless access points are intermediary devices that make up the network infrastructure.*
</details>

### Question 2
Select all network topologies that use a central connection point:
- [ ] Bus
- [ ] Star
- [ ] Mesh
- [ ] Ring
- [ ] Tree

<details>
<summary>Show answer</summary>

**Answer:** Star, Tree

*Explanation: Star topology connects all devices to a central hub or switch. Tree topology is hierarchical but also uses central connection points at each level. Bus, mesh, and ring topologies do not rely on central connection points.*
</details>

### Question 3
Identify all the protocols that operate at the Transport layer:
- [ ] HTTP
- [ ] TCP
- [ ] IP
- [ ] UDP
- [ ] Ethernet
- [ ] FTP
- [ ] SMTP

<details>
<summary>Show answer</summary>

**Answer:** TCP, UDP

*Explanation: The Transport layer (Layer 4) protocols include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). HTTP, FTP, and SMTP are Application layer protocols. IP is a Network layer protocol. Ethernet operates at the Data Link and Physical layers.*
</details>

### Question 4
Select all statements that correctly describe characteristics of packet-switched networks:
- [ ] Resources are reserved for the duration of the connection
- [ ] Messages are broken into packets
- [ ] All packets must follow the same path
- [ ] Packets can take different paths to the destination
- [ ] Connection establishment is required before data transfer
- [ ] Network resources can be shared among multiple communications

<details>
<summary>Show answer</summary>

**Answer:** Messages are broken into packets, Packets can take different paths to the destination, Network resources can be shared among multiple communications

*Explanation: In packet-switched networks, messages are divided into packets that can take different paths to reach their destination. This allows network resources to be shared efficiently among multiple communications. Resource reservation and mandatory connection establishment are characteristics of circuit-switched networks.*
</details>

### Question 5
Select all components of the CIA triad in information security:
- [ ] Confidentiality
- [ ] Integrity
- [ ] Authentication
- [ ] Availability
- [ ] Authorization
- [ ] Accountability
- [ ] Non-repudiation

<details>
<summary>Show answer</summary>

**Answer:** Confidentiality, Integrity, Availability

*Explanation: The CIA triad consists of Confidentiality (ensuring information is accessible only to authorized users), Integrity (maintaining the accuracy and consistency of data), and Availability (ensuring systems are available when needed). The other items are important security concepts but not part of the CIA triad.*
</details>

## Part 2: Multiple-Choice Questions (90 marks)

### Question 1
Which statement best describes the relationship between the OSI and TCP/IP models?
- A) The TCP/IP model has more layers than the OSI model
- B) The OSI model has more layers than the TCP/IP model
- C) Both models have the same number of layers
- D) The models are unrelated and serve different purposes

<details>
<summary>Show answer</summary>

**Answer: B) The OSI model has more layers than the TCP/IP model**

*Explanation: The OSI model has seven layers (Physical, Data Link, Network, Transport, Session, Presentation, and Application), while the TCP/IP model traditionally has four layers (Network Access, Internet, Transport, and Application). The OSI model is more detailed, particularly in the upper layers.*
</details>

### Question 2
What is the main function of the Network layer in the OSI model?
- A) Providing reliable data transfer between applications
- B) Converting data into signals for transmission
- C) Routing packets between different networks using logical addressing
- D) Establishing sessions between applications

<details>
<summary>Show answer</summary>

**Answer: C) Routing packets between different networks using logical addressing**

*Explanation: The Network layer (Layer 3) is responsible for path determination and logical addressing (using IP addresses) to enable data delivery between different networks.*
</details>

### Question 3
Which of the following correctly describes encapsulation in the context of networking?
- A) The process of encrypting data for secure transmission
- B) The process of adding headers and trailers as data passes down the protocol stack
- C) The process of compressing data to reduce bandwidth usage
- D) The process of translating domain names to IP addresses

<details>
<summary>Show answer</summary>

**Answer: B) The process of adding headers and trailers as data passes down the protocol stack**

*Explanation: Encapsulation is the process where each layer adds its own header (and sometimes trailer) information to the data received from the layer above, effectively wrapping the original data in layer-specific information needed for proper handling at the receiving end.*
</details>

### Question 4
What is the purpose of a subnet mask in IP addressing?
- A) To encrypt IP addresses for secure transmission
- B) To identify which portion of an IP address represents the network and which represents the host
- C) To translate between IPv4 and IPv6 addresses
- D) To prevent IP address spoofing

<details>
<summary>Show answer</summary>

**Answer: B) To identify which portion of an IP address represents the network and which represents the host**

*Explanation: A subnet mask is a 32-bit number that "masks" an IP address, defining which bits represent the network portion and which bits represent the host portion. This allows routers to determine if a destination is on the local network or requires routing to another network.*
</details>

### Question 5
Which statement accurately describes the difference between symmetric and asymmetric key cryptography?
- A) Symmetric uses the same key for encryption and decryption, while asymmetric uses different keys
- B) Symmetric is more secure, while asymmetric is faster
- C) Symmetric works with any data size, while asymmetric has size limitations
- D) Symmetric requires a third party, while asymmetric is peer-to-peer

<details>
<summary>Show answer</summary>

**Answer: A) Symmetric uses the same key for encryption and decryption, while asymmetric uses different keys**

*Explanation: Symmetric key cryptography uses a single shared key for both encryption and decryption. Asymmetric key cryptography uses a pair of mathematically related keys—a public key for encryption and a private key for decryption.*
</details>

### Question 6
What is the primary function of the Data Link layer's LLC sublayer?
- A) Converting bits into signals for transmission
- B) Managing media access and handling collisions
- C) Providing an interface between the Network layer and the MAC sublayer
- D) Establishing end-to-end connections between applications

<details>
<summary>Show answer</summary>

**Answer: C) Providing an interface between the Network layer and the MAC sublayer**

*Explanation: The Logical Link Control (LLC) sublayer provides the interface between the Network layer and the MAC sublayer. It identifies which network layer protocol is being used and handles communication between the upper and lower layers.*
</details>

### Question 7
Which network organization type would be most appropriate for a small home office with 3-4 computers that need to share files occasionally?
- A) Client-server network
- B) Peer-to-peer network
- C) Full mesh network
- D) Hierarchical network

<details>
<summary>Show answer</summary>

**Answer: B) Peer-to-peer network**

*Explanation: A peer-to-peer network is well-suited for small environments with few computers that need to share resources occasionally. It's easy to set up, less complex, and lower cost than a client-server network, which would be excessive for just 3-4 computers.*
</details>

### Question 8
Which statement best describes the relationship between Ethernet and the OSI model?
- A) Ethernet is a protocol that operates only at the Physical layer
- B) Ethernet is a protocol that operates at the Network layer
- C) Ethernet is a protocol that operates at both the Data Link and Physical layers
- D) Ethernet is a protocol that operates at all seven layers of the OSI model

<details>
<summary>Show answer</summary>

**Answer: C) Ethernet is a protocol that operates at both the Data Link and Physical layers**

*Explanation: Ethernet is a LAN technology that spans both the Data Link layer (handling MAC addressing and frame formatting) and the Physical layer (dealing with the electrical, mechanical, and procedural specifications for transmission).*
</details>

### Question 9
What is the main advantage of UDP over TCP?
- A) Guaranteed delivery of all packets
- B) Connection establishment before data transfer
- C) Lower latency due to no acknowledgment or retransmission mechanisms
- D) Flow control to prevent overwhelming the receiver

<details>
<summary>Show answer</summary>

**Answer: C) Lower latency due to no acknowledgment or retransmission mechanisms**

*Explanation: UDP provides lower latency than TCP because it doesn't establish connections, doesn't guarantee delivery, and doesn't implement acknowledgment or retransmission mechanisms. This makes it faster but less reliable, ideal for time-sensitive applications where occasional packet loss is acceptable.*
</details>

### Question 10
What does port number 443 typically represent in networking?
- A) HTTP traffic
- B) HTTPS (secure HTTP) traffic
- C) FTP traffic
- D) SMTP traffic

<details>
<summary>Show answer</summary>

**Answer: B) HTTPS (secure HTTP) traffic**

*Explanation: Port 443 is the standard port for HTTPS (Hypertext Transfer Protocol Secure) traffic, which is HTTP traffic encrypted using SSL/TLS. This allows for secure web browsing and confidential data transfer.*
</details>

### Question 11
Which technology is used to allow multiple devices on a private network to share a single public IP address?
- A) DNS (Domain Name System)
- B) DHCP (Dynamic Host Configuration Protocol)
- C) NAT (Network Address Translation)
- D) ARP (Address Resolution Protocol)

<details>
<summary>Show answer</summary>

**Answer: C) NAT (Network Address Translation)**

*Explanation: Network Address Translation (NAT) allows multiple devices within a private network to share a single public IP address. NAT maps private IP addresses to a public IP address when devices communicate with external networks, helping conserve IPv4 addresses and adding security by hiding internal network addresses.*
</details>

### Question 12
What is the primary purpose of the Physical layer in the OSI model?
- A) To establish end-to-end connections between applications
- B) To determine the best path for data transmission
- C) To manage access to the shared medium
- D) To convert data into signals for transmission over the physical medium

<details>
<summary>Show answer</summary>

**Answer: D) To convert data into signals for transmission over the physical medium**

*Explanation: The Physical layer (Layer 1) is responsible for the actual transmission of raw bit streams over a physical medium. It defines the electrical, mechanical, and procedural specifications, converting binary data into the appropriate signals (electrical, light, radio waves) for the transmission medium.*
</details>

### Question 13
In which type of attack does an attacker exploit improperly validated input to execute arbitrary SQL commands on a database?
- A) Man-in-the-middle attack
- B) Denial of Service attack
- C) SQL injection attack
- D) Buffer overflow attack

<details>
<summary>Show answer</summary>

**Answer: C) SQL injection attack**

*Explanation: SQL injection attacks occur when an attacker inserts or "injects" malicious SQL code into input fields that are later passed to a database for execution. This can allow attackers to access, modify, or delete database content unauthorized if input validation is inadequate.*
</details>

### Question 14
What is the purpose of CSMA/CD in Ethernet networks?
- A) To encrypt data for secure transmission
- B) To manage collisions when multiple devices try to transmit simultaneously
- C) To compress data for more efficient transmission
- D) To authenticate devices before allowing network access

<details>
<summary>Show answer</summary>

**Answer: B) To manage collisions when multiple devices try to transmit simultaneously**

*Explanation: Carrier Sense Multiple Access with Collision Detection (CSMA/CD) is a media access control method used in early Ethernet networks. It allows devices to detect when multiple stations are transmitting simultaneously (causing a collision), stop transmission, wait a random time, and then retry, thus managing collisions on shared media.*
</details>

### Question 15
Which of the following best describes the difference between a router and a switch?
- A) Routers operate at the Data Link layer, while switches operate at the Network layer
- B) Routers connect different networks using logical addressing, while switches connect devices within the same network using physical addressing
- C) Routers create collision domains, while switches create broadcast domains
- D) Routers handle wired connections, while switches handle wireless connections

<details>
<summary>Show answer</summary>

**Answer: B) Routers connect different networks using logical addressing, while switches connect devices within the same network using physical addressing**

*Explanation: Routers operate at the Network layer (Layer 3) and use logical addressing (IP addresses) to route traffic between different networks. Switches operate at the Data Link layer (Layer 2) and use physical addressing (MAC addresses) to forward frames to devices within the same local network.*
</details>

### Question 16
What is a primary advantage of IPv6 over IPv4?
- A) Simpler header structure
- B) Vastly expanded address space
- C) Faster routing
- D) Better security by default

<details>
<summary>Show answer</summary>

**Answer: B) Vastly expanded address space**

*Explanation: The primary advantage of IPv6 is its vastly expanded address space, using 128-bit addresses compared to IPv4's 32-bit addresses. This provides approximately 340 undecillion unique addresses (3.4 × 10^38), solving the IPv4 address exhaustion problem.*
</details>

### Question 17
Which of the following is NOT a characteristic of symmetric key cryptography?
- A) Uses the same key for encryption and decryption
- B) Faster than asymmetric cryptography
- C) Relies on public and private key pairs
- D) Good for encrypting large amounts of data

<details>
<summary>Show answer</summary>

**Answer: C) Relies on public and private key pairs**

*Explanation: Using public and private key pairs is a characteristic of asymmetric (public key) cryptography, not symmetric key cryptography. Symmetric cryptography uses a single shared key for both encryption and decryption, is faster than asymmetric methods, and is efficient for encrypting large amounts of data.*
</details>

### Question 18
What is the function of the Presentation layer in the OSI model?
- A) Establishing and terminating connections between applications
- B) Data translation, compression, and encryption
- C) Determining the best path for data transmission
- D) Managing device-to-device communication on a local network

<details>
<summary>Show answer</summary>

**Answer: B) Data translation, compression, and encryption**

*Explanation: The Presentation layer (Layer 6) is responsible for data translation (e.g., ASCII to EBCDIC), compression to reduce size (both lossy and lossless), and encryption/decryption to ensure security. It ensures that data from the application layer is readable by the receiving system.*
</details>

### Question 19
What is the main purpose of the Session layer in the OSI model?
- A) To establish, manage, and terminate sessions between applications
- B) To route packets between different networks
- C) To convert data into signals for transmission
- D) To provide reliable data transfer between hosts

<details>
<summary>Show answer</summary>

**Answer: A) To establish, manage, and terminate sessions between applications**

*Explanation: The Session layer (Layer 5) establishes, maintains, and terminates communication sessions between applications. It handles session checkpointing and recovery, and controls dialogue between communicating devices (simplex, half-duplex, or full-duplex).*
</details>

### Question 20
What is throughput in the context of networking?
- A) The maximum speed advertised by your internet service provider
- B) The measure of the transfer of bits across the media over a given period of time
- C) The time it takes for a packet to travel from source to destination
- D) The maximum capacity of a network cable

<details>
<summary>Show answer</summary>

**Answer: B) The measure of the transfer of bits across the media over a given period of time**

*Explanation: Throughput measures the actual transfer of bits across the network media over a given period. It represents the actual performance achieved, which may be lower than the theoretical bandwidth due to various factors like overhead, congestion, and latency.*
</details>

### Question 21
Which statement best describes the difference between a hub and a switch?
- A) Hubs operate at the Network layer, while switches operate at the Data Link layer
- B) Hubs forward data to all connected devices, while switches selectively forward data based on MAC addresses
- C) Hubs are used for wireless networks, while switches are used for wired networks
- D) Hubs provide greater bandwidth than switches

<details>
<summary>Show answer</summary>

**Answer: B) Hubs forward data to all connected devices, while switches selectively forward data based on MAC addresses**

*Explanation: Hubs are simple Layer 1 devices that repeat signals to all ports, creating a single collision domain. Switches are Layer 2 devices that learn MAC addresses and selectively forward frames only to the specific port where the destination device is connected, creating separate collision domains for each port.*
</details>

### Question 22
What is the purpose of the MAC address table in a switch?
- A) To encrypt MAC addresses for secure transmission
- B) To map IP addresses to MAC addresses
- C) To map MAC addresses to the physical switch ports where devices are connected
- D) To authenticate users before allowing network access

<details>
<summary>Show answer</summary>

**Answer: C) To map MAC addresses to the physical switch ports where devices are connected**

*Explanation: A switch builds and maintains a MAC address table (also called a forwarding table or CAM table) that maps MAC addresses of connected devices to the physical ports on the switch. This allows the switch to intelligently forward frames only to the port where the destination device is connected, improving network efficiency.*
</details>

### Question 23
In the context of TCP/IP communication, what is a socket?
- A) A physical connector on a network device
- B) The combination of an IP address and a port number
- C) A programming interface for network communication
- D) The encryption key used for secure communication

<details>
<summary>Show answer</summary>

**Answer: B) The combination of an IP address and a port number**

*Explanation: In TCP/IP networking, a socket is the combination of an IP address and a port number, uniquely identifying an endpoint for communication. The IP address identifies the host, while the port number identifies the specific application or service on that host.*
</details>

### Question 24
What type of attack involves overwhelming a server with a flood of TCP SYN packets without completing the handshake?
- A) SQL injection attack
- B) Man-in-the-middle attack
- C) SYN flood attack
- D) Phishing attack

<details>
<summary>Show answer</summary>

**Answer: C) SYN flood attack**

*Explanation: A SYN flood attack is a form of denial-of-service attack where an attacker sends a succession of TCP SYN packets to a target, but never completes the three-way handshake. This leaves the server with numerous half-open connections, consuming resources until they time out, potentially preventing legitimate connections.*
</details>

### Question 25
What is the main function of the Open Shortest Path First (OSPF) protocol?
- A) Translating domain names to IP addresses
- B) Routing packets between autonomous systems
- C) Calculating shortest paths for packet routing within an autonomous system
- D) Managing dynamic IP address assignment

<details>
<summary>Show answer</summary>

**Answer: C) Calculating shortest paths for packet routing within an autonomous system**

*Explanation: OSPF (Open Shortest Path First) is a link-state routing protocol that uses the Dijkstra algorithm to calculate the shortest path between routers within an autonomous system. It enables routers to build a complete view of network topology and determine the best route for forwarding packets.*
</details>

### Question 26
Which of the following best describes the purpose of a firewall in network security?
- A) To encrypt data transmitted across the network
- B) To filter network traffic based on predetermined security rules
- C) To detect and remove malware from network packets
- D) To authenticate users before allowing network access

<details>
<summary>Show answer</summary>

**Answer: B) To filter network traffic based on predetermined security rules**

*Explanation: A firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies. It acts as a barrier between a trusted internal network and untrusted external networks, allowing or blocking traffic based on a set of security rules.*
</details>

### Question 27
What does CSMA/CA stand for, and where is it primarily used?
- A) Carrier Sense Multiple Access with Collision Avoidance, used in wireless networks
- B) Carrier Sense Multiple Access with Collision Detection, used in wired Ethernet
- C) Centralized System Multiple Access with Collision Avoidance, used in token ring networks
- D) Connected Segment Multiple Access with Collision Awareness, used in fiber networks

<details>
<summary>Show answer</summary>

**Answer: A) Carrier Sense Multiple Access with Collision Avoidance, used in wireless networks**

*Explanation: CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) is a protocol used in wireless networks (802.11 Wi-Fi). Unlike CSMA/CD, which detects collisions after they occur, CSMA/CA attempts to avoid collisions by using timing schemes and request-to-send/clear-to-send mechanisms, which is necessary in wireless environments where devices may not be able to detect collisions directly.*
</details>

### Question 28
Which of the following is NOT a characteristic of circuit-switched networks?
- A) Dedicated communication path established before data transfer
- B) Resources reserved for the duration of the communication
- C) Packets can take different paths to the destination
- D) Connection must be terminated to free up resources

<details>
<summary>Show answer</summary>

**Answer: C) Packets can take different paths to the destination**

*Explanation: Taking different paths to the destination is a characteristic of packet-switched networks, not circuit-switched networks. In circuit-switched networks, a dedicated communication path is established before data transfer and remains fixed for the entire session, with resources reserved even during periods of silence.*
</details>

### Question 29
What is the primary function of a hash function in information security?
- A) To encrypt data for secure transmission
- B) To compress data for efficient storage
- C) To generate a fixed-size value to verify data integrity
- D) To authenticate users before allowing access

<details>
<summary>Show answer</summary>

**Answer: C) To generate a fixed-size value to verify data integrity**

*Explanation: A hash function takes input data of any size and produces a fixed-length output value (hash), which serves as a digital fingerprint of the input data. The primary purpose is to verify data integrity—any change to the original data, no matter how small, will produce a different hash value, indicating the data has been altered.*
</details>

### Question 30
Which of the following best describes the function of the Address Resolution Protocol (ARP)?
- A) Translating domain names to IP addresses
- B) Mapping IP addresses to MAC addresses on a local network
- C) Assigning IP addresses to hosts dynamically
- D) Routing packets between different networks

<details>
<summary>Show answer</summary>

**Answer: B) Mapping IP addresses to MAC addresses on a local network**

*Explanation: The Address Resolution Protocol (ARP) maps IP addresses to MAC addresses on a local network. When a device needs to communicate with another device on the same local network, it uses ARP to discover the MAC address associated with the destination IP address, which is necessary for Layer 2 (data link) communication.*
</details>

### Question 31
What is latency in the context of networking?
- A) The maximum data transfer rate of a network
- B) The delay between sending and receiving data
- C) The total amount of data that can be transmitted
- D) The number of network hops required to reach a destination

<details>
<summary>Show answer</summary>

**Answer: B) The delay between sending and receiving data**

*Explanation: Latency is the time delay between when data is sent and when it is received. It represents how long it takes for data to travel from source to destination, and is typically measured in milliseconds. High latency can negatively impact interactive applications like online gaming, video conferencing, and VoIP calls.*
</details>

### Question 32
What does a subnet mask of 255.255.255.0 indicate about an IP address?
- A) All hosts on the subnet can communicate directly
- B) The first 24 bits represent the network portion of the address
- C) There are 254 usable host addresses available
- D) The address belongs to a Class A network

<details>
<summary>Show answer</summary>

**Answer: B) The first 24 bits represent the network portion of the address**

*Explanation: A subnet mask of 255.255.255.0 (or /24 in CIDR notation) indicates that the first 24 bits (the first three octets) of an IP address represent the network portion, while the last 8 bits (the last octet) represent the host portion. This allows for 254 usable host addresses on that network (256 minus the network and broadcast addresses).*
</details>

### Question 33
What is the primary purpose of a Virtual Private Network (VPN)?
- A) To increase internet connection speed
- B) To create a secure, encrypted connection over a less secure network
- C) To manage dynamic IP address assignment
- D) To filter network traffic based on security rules

<details>
<summary>Show answer</summary>

**Answer: B) To create a secure, encrypted connection over a less secure network**

*Explanation: A Virtual Private Network (VPN) creates a secure, encrypted connection over a less secure network, such as the public internet. It provides privacy, anonymity, and security by creating an encrypted "tunnel" for data transmission, protecting the data from eavesdropping, and often masking the user's original IP address.*
</details>

### Question 34
Which of the following is a characteristic of a packet-switched network but NOT a circuit-switched network?
- A) Guaranteed bandwidth for the duration of the communication
- B) Resources are allocated on demand
- C) Connection must be established before data transfer
- D) Fixed path for the entire communication session

<details>
<summary>Show answer</summary>

**Answer: B) Resources are allocated on demand**

*Explanation: In packet-switched networks, resources are allocated on demand as needed for each packet, allowing efficient sharing of network resources. In contrast, circuit-switched networks allocate dedicated resources for the entire duration of a communication session, regardless of whether data is actively being transmitted.*
</details>

### Question 35
In the context of networking, what is a protocol?
- A) The physical medium used for data transmission
- B) A set of rules governing communication between network devices
- C) A network security device that filters traffic
- D) A unique identifier assigned to a network device

<details>
<summary>Show answer</summary>

**Answer: B) A set of rules governing communication between network devices**

*Explanation: A protocol is a set of rules and conventions that govern how data is formatted, transmitted, received, and processed in a network. Protocols define the syntax, semantics, and synchronization of communication, ensuring that different devices and systems can understand each other and exchange information correctly.*
</details>

### Question 36
What happens during the de-encapsulation process as data moves up the OSI layers?
- A) Headers and trailers are added at each layer
- B) Data is compressed for efficient transmission
- C) Headers and trailers are removed at each layer
- D) Data is encrypted for secure transmission

<details>
<summary>Show answer</summary>

**Answer: C) Headers and trailers are removed at each layer**

*Explanation: De-encapsulation is the process that occurs as data moves up the OSI layers at the receiving device. At each layer, the corresponding header (and trailer, if present) that was added during encapsulation is removed, and the resulting data is passed to the layer above. This continues until the original data reaches the Application layer.*
</details>

### Question 37
What is the primary difference between a private IP address and a public IP address?
- A) Private addresses are assigned by DHCP, while public addresses are statically assigned
- B) Private addresses can only be used with IPv4, while public addresses work with both IPv4 and IPv6
- C) Private addresses are used within local networks and not routable on the internet, while public addresses are globally unique and routable on the internet
- D) Private addresses are more secure than public addresses

<details>
<summary>Show answer</summary>

**Answer: C) Private addresses are used within local networks and not routable on the internet, while public addresses are globally unique and routable on the internet**

*Explanation: Private IP addresses are used within local networks and are not routable across the public internet. They come from specific reserved ranges (like 192.168.x.x, 10.x.x.x, 172.16-31.x.x). Public IP addresses are globally unique, assigned by internet authorities, and used for communication across the public internet.*
</details>

### Question 38
What type of attack attempts to trick users into revealing sensitive information by masquerading as a trustworthy entity?
- A) DoS (Denial of Service) attack
- B) Buffer overflow attack
- C) Phishing attack
- D) SQL injection attack

<details>
<summary>Show answer</summary>

**Answer: C) Phishing attack**

*Explanation: Phishing is a type of social engineering attack where attackers attempt to trick users into revealing sensitive information (like passwords, credit card numbers, or personal data) by masquerading as a trustworthy entity. This is often done through fraudulent emails, websites, or messages that appear to be from legitimate organizations.*
</details>

### Question 39
What is the main limitation of symmetric key cryptography in a network environment?
- A) It is too slow for practical use
- B) It provides inadequate encryption strength
- C) It cannot encrypt large amounts of data
- D) Securely distributing the shared key between parties

<details>
<summary>Show answer</summary>

**Answer: D) Securely distributing the shared key between parties**

*Explanation: The main limitation of symmetric key cryptography in a network environment is the key distribution problem—how to securely share the secret key between communicating parties before secure communication begins. If an attacker intercepts the key during transmission, they can decrypt all subsequent communications.*
</details>

### Question 40
What is the purpose of the Diffie-Hellman key exchange algorithm?
- A) To encrypt data for secure transmission
- B) To securely establish a shared secret key over an insecure channel
- C) To authenticate users before allowing network access
- D) To digitally sign messages for non-repudiation

<details>
<summary>Show answer</summary>

**Answer: B) To securely establish a shared secret key over an insecure channel**

*Explanation: The Diffie-Hellman key exchange algorithm allows two parties to securely establish a shared secret key over an insecure communication channel without requiring prior knowledge of each other. This shared key can then be used for symmetric encryption, solving the key distribution problem while never actually transmitting the key itself.*
</details>

### Question 41
What is the function of the File Transfer Protocol (FTP) in the TCP/IP protocol suite?
- A) Managing the transfer of hypertext documents
- B) Providing reliable file transfer between hosts on a network
- C) Mapping domain names to IP addresses
- D) Managing device-to-device communication on a local network

<details>
<summary>Show answer</summary>

**Answer: B) Providing reliable file transfer between hosts on a network**

*Explanation: File Transfer Protocol (FTP) is an Application layer protocol in the TCP/IP suite designed for transferring files between computers on a network. It provides functions for user authentication, directory navigation, and reliable file upload and download operations between clients and servers.*
</details>

### Question 42
Which of the following accurately describes the difference between goodput and throughput?
- A) Goodput is the theoretical maximum capacity, while throughput is the actual achieved rate
- B) Goodput is the amount of useful data transferred, while throughput includes protocol overhead
- C) Goodput is for wired networks, while throughput is for wireless networks
- D) Goodput includes error correction, while throughput does not

<details>
<summary>Show answer</summary>

**Answer: B) Goodput is the amount of useful data transferred, while throughput includes protocol overhead**

*Explanation: Goodput is the application-level throughput—the amount of useful data transferred (excluding protocol overhead, retransmissions, etc.) in a given time. Throughput is the total amount of data transferred, including all headers, acknowledgments, retransmissions, and other protocol overhead. Goodput is always less than or equal to throughput.*
</details>

### Question 43
What problem does Network Address Translation (NAT) help solve?
- A) Slow network performance
- B) IPv4 address exhaustion
- C) Weak encryption
- D) Inefficient routing

<details>
<summary>Show answer</summary>

**Answer: B) IPv4 address exhaustion**

*Explanation: Network Address Translation (NAT) was developed primarily to address IPv4 address exhaustion by allowing multiple devices within a private network to share a single public IP address. This conserves the limited pool of available public IPv4 addresses and extends the usable life of the IPv4 addressing scheme.*
</details>

### Question 44
What is the purpose of the Domain Name System (DNS) in networking?
- A) Assigning IP addresses to hosts dynamically
- B) Filtering network traffic based on domain names
- C) Translating domain names to IP addresses
- D) Routing packets between different networks

<details>
<summary>Show answer</summary>

**Answer: C) Translating domain names to IP addresses**

*Explanation: The Domain Name System (DNS) is responsible for translating human-readable domain names (like www.example.com) into machine-readable IP addresses (like 93.184.216.34) that computers use to identify each other on the network. This allows users to access websites using memorable domain names rather than numerical IP addresses.*
</details>

### Question 45
Which of the following is NOT a function of the Transport layer in the OSI model?
- A) Segmentation of data
- B) Flow control
- C) Error detection and recovery
- D) Path determination

<details>
<summary>Show answer</summary>

**Answer: D) Path determination**

*Explanation: Path determination is a function of the Network layer (Layer 3), not the Transport layer (Layer 4). The Transport layer is responsible for segmentation of data, ensuring reliable delivery through error detection and recovery, flow control to prevent overwhelming the receiver, and identifying the specific application or service through port numbers.*
</details>