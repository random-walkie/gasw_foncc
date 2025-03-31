# Mock Exam 2: Network Architecture and Communications

## Part 1: Option Selection Questions (10 marks)

For these questions, select the appropriate option or options that correctly complete the statement or answer the question.

### Question 1
Select all correctly matched pairs of OSI layer and corresponding PDU (Protocol Data Unit):
- [ ] Physical layer - Bit
- [ ] Network layer - Frame
- [ ] Transport layer - Segment
- [ ] Data Link layer - Packet
- [ ] Application layer - Data
- [ ] Presentation layer - Segment
- [ ] Session layer - Datagram

<details>
<summary>Show answer</summary>

**Answer:** Physical layer - Bit, Transport layer - Segment, Application layer - Data

*Explanation: Each OSI layer uses a specific type of PDU. The correct pairs are: Physical layer - Bit, Data Link layer - Frame, Network layer - Packet, Transport layer - Segment, and Application/Presentation/Session layers - Data. The terms Datagram is sometimes used for UDP packets at the Transport layer but isn't a standard OSI PDU name.*
</details>

### Question 2
Select all protocols that operate at the Application layer of the OSI model:
- [ ] TCP
- [ ] IP
- [ ] HTTP
- [ ] FTP
- [ ] Ethernet
- [ ] SMTP
- [ ] UDP

<details>
<summary>Show answer</summary>

**Answer:** HTTP, FTP, SMTP

*Explanation: HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), and SMTP (Simple Mail Transfer Protocol) all operate at the Application layer (Layer 7) of the OSI model. TCP and UDP are Transport layer protocols, IP is a Network layer protocol, and Ethernet operates at the Data Link and Physical layers.*
</details>

### Question 3
Select all types of addresses used in networking:
- [ ] Logical addresses
- [ ] Physical addresses
- [ ] Port numbers
- [ ] Socket addresses
- [ ] Protocol addresses
- [ ] Gateway addresses
- [ ] Broadcast addresses

<details>
<summary>Show answer</summary>

**Answer:** Logical addresses, Physical addresses, Port numbers, Socket addresses, Broadcast addresses

*Explanation: Logical addresses (IP addresses) identify devices at the Network layer. Physical addresses (MAC addresses) identify devices at the Data Link layer. Port numbers identify applications or services. Socket addresses combine IP addresses and port numbers. Broadcast addresses are special addresses used to send data to all devices on a network. "Protocol addresses" is not a standard networking term, and gateway addresses would fall under logical addresses.*
</details>

### Question 4
Select all technologies or protocols used for network security:
- [ ] Symmetric key cryptography
- [ ] Asymmetric key cryptography
- [ ] Hash functions
- [ ] NAT (Network Address Translation)
- [ ] OSPF (Open Shortest Path First)
- [ ] SSL/TLS (Secure Sockets Layer/Transport Layer Security)
- [ ] DHCP (Dynamic Host Configuration Protocol)

<details>
<summary>Show answer</summary>

**Answer:** Symmetric key cryptography, Asymmetric key cryptography, Hash functions, SSL/TLS

*Explanation: Symmetric and asymmetric key cryptography are encryption methods used for securing data. Hash functions are used for data integrity and password storage. SSL/TLS provides secure communications over a network. NAT helps with IPv4 address conservation and provides some security by hiding internal addresses, but it's primarily an addressing technology. OSPF is a routing protocol. DHCP is for IP address assignment.*
</details>

### Question 5
Select all services provided by the Transport layer:
- [ ] Path determination
- [ ] Flow control
- [ ] Error detection and recovery
- [ ] Encryption and decryption
- [ ] Segmentation and reassembly
- [ ] Port addressing
- [ ] Physical addressing

<details>
<summary>Show answer</summary>

**Answer:** Flow control, Error detection and recovery, Segmentation and reassembly, Port addressing

*Explanation: The Transport layer (Layer 4) provides several key services: flow control to prevent overwhelming receivers, error detection and recovery to ensure reliable delivery, segmentation of data into manageable pieces and reassembly at the destination, and port addressing to identify specific applications. Path determination is a Network layer function, encryption/decryption is typically a Presentation layer function, and physical addressing is a Data Link layer function.*
</details>

## Part 2: Multiple-Choice Questions (90 marks)

### Question 1
Which statement best describes the process of encapsulation in networking?
- A) Adding encryption to data before transmission
- B) Compressing data to reduce its size
- C) Adding headers and trailers as data passes down the protocol stack
- D) Converting signals from digital to analog form

<details>
<summary>Show answer</summary>

**Answer: C) Adding headers and trailers as data passes down the protocol stack**

*Explanation: Encapsulation is the process where each layer of the protocol stack adds its own header (and sometimes trailer) information to the data unit received from the layer above. This creates a nested structure, with the original data surrounded by control information from each layer, enabling proper handling at the corresponding layer on the receiving end.*
</details>

### Question 2
What is the primary function of the Presentation layer in the OSI model?
- A) Establishing and terminating sessions
- B) Data translation, encryption, and compression
- C) Managing network congestion
- D) Routing packets between networks

<details>
<summary>Show answer</summary>

**Answer: B) Data translation, encryption, and compression**

*Explanation: The Presentation layer (Layer 6) is responsible for data translation (converting between different formats), encryption/decryption (ensuring data confidentiality), and compression/decompression (reducing data size for transmission). These functions ensure that data from the application layer is presented in a form that the receiving system can understand.*
</details>

### Question 3
What is the difference between lossy and lossless compression in the Presentation layer?
- A) Lossy compression is reversible, while lossless compression is irreversible
- B) Lossy compression loses some original data, while lossless compression preserves all original data
- C) Lossy compression is used for text, while lossless compression is used for images
- D) Lossy compression requires more processing power than lossless compression

<details>
<summary>Show answer</summary>

**Answer: B) Lossy compression loses some original data, while lossless compression preserves all original data**

*Explanation: Lossless compression preserves all the original data when the file is decompressed, making it identical to the original. Lossy compression permanently discards some less-critical data to achieve higher compression ratios. Lossy compression is typically used for media files (images, audio, video) where minor quality loss is acceptable, while lossless is used where perfect reconstruction is required, like text documents or program files.*
</details>

### Question 4
Which technology is used in token ring networks to prevent collisions?
- A) CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
- B) CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
- C) Token passing
- D) Polling

<details>
<summary>Show answer</summary>

**Answer: C) Token passing**

*Explanation: Token ring networks use token passing to prevent collisions. A special frame called a token circulates around the ring, and only the station that possesses the token is allowed to transmit data. This ensures that only one device can transmit at a time, eliminating the possibility of collisions. CSMA/CD is used in Ethernet, CSMA/CA in wireless networks, and polling in certain controlled access networks.*
</details>

### Question 5
Which statement most accurately describes the relationship between PDUs (Protocol Data Units) and the OSI model?
- A) Each layer uses the same PDU format
- B) Each layer uses a different name for its PDU
- C) PDUs are only used at the lower three layers of the OSI model
- D) PDUs are only relevant to the TCP/IP model, not the OSI model

<details>
<summary>Show answer</summary>

**Answer: B) Each layer uses a different name for its PDU**

*Explanation: Each layer of the OSI model uses a different name for its Protocol Data Unit (PDU). Application/Presentation/Session layers use data, Transport layer uses segments, Network layer uses packets, Data Link layer uses frames, and the Physical layer uses bits. These different names reflect the different formatting and handling of data at each layer.*
</details>

### Question 6
In a networking context, what does the term "throughput" measure?
- A) The maximum theoretical bandwidth of a network
- B) The actual amount of data transferred over a period of time
- C) The time delay between sending and receiving data
- D) The number of connections a server can handle simultaneously

<details>
<summary>Show answer</summary>

**Answer: B) The actual amount of data transferred over a period of time**

*Explanation: Throughput measures the actual amount of data successfully transferred through a network connection over a given period of time, typically expressed in bits per second (bps) or a multiple thereof (Kbps, Mbps, Gbps). It differs from bandwidth, which represents the theoretical maximum capacity. Various factors including overhead, congestion, and latency often cause throughput to be lower than the theoretical bandwidth.*
</details>

### Question 7
What happens during the de-encapsulation process at the receiving end of a network communication?
- A) The original message is compressed to save bandwidth
- B) The original message is encrypted for security
- C) Headers and trailers are removed as data moves up the protocol stack
- D) Headers and trailers are added as data moves up the protocol stack

<details>
<summary>Show answer</summary>

**Answer: C) Headers and trailers are removed as data moves up the protocol stack**

*Explanation: De-encapsulation is the reverse of encapsulation and occurs at the receiving device. As data moves up through the OSI layers, each layer removes (strips off) the header and trailer information that was added by the corresponding layer on the sending device. This continues until the original data reaches the Application layer.*
</details>

### Question 8
Which statement correctly describes circuit-switched networks?
- A) Data is broken into packets that can take different paths to the destination
- B) A dedicated communication path is established before data transfer begins
- C) Network resources are shared among multiple communications simultaneously
- D) Each packet contains addressing information for independent routing

<details>
<summary>Show answer</summary>

**Answer: B) A dedicated communication path is established before data transfer begins**

*Explanation: In circuit-switched networks, a dedicated physical communication path is established between sender and receiver before any data transfer occurs. This path remains reserved for the entire duration of the communication session, even during periods of silence. Traditional telephone networks are a classic example of circuit switching. This contrasts with packet-switched networks, where data is divided into packets that can take different paths and network resources are shared.*
</details>

### Question 9
What is the main difference between a MAC address and an IP address?
- A) MAC addresses are used in LANs, while IP addresses are used in WANs
- B) MAC addresses are physical addresses assigned to network interfaces, while IP addresses are logical addresses assigned to network devices
- C) MAC addresses can be changed by the user, while IP addresses are fixed
- D) MAC addresses are 32 bits long, while IP addresses are 48 bits long

<details>
<summary>Show answer</summary>

**Answer: B) MAC addresses are physical addresses assigned to network interfaces, while IP addresses are logical addresses assigned to network devices**

*Explanation: MAC (Media Access Control) addresses are 48-bit physical addresses permanently assigned to network interface hardware by manufacturers. They operate at the Data Link layer and identify specific network interfaces. IP addresses are logical addresses that operate at the Network layer, can be assigned and changed through configuration, and identify devices on a network independent of their hardware. MAC addresses are used for local network communication, while IP addresses enable routing between different networks.*
</details>

### Question 10
Which of the following best describes the CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) method?
- A) It detects collisions after they occur and then takes corrective action
- B) It attempts to avoid collisions before they happen by using timing and coordination mechanisms
- C) It prevents collisions by using a central controller to grant permission to transmit
- D) It eliminates collisions by assigning fixed time slots to each device

<details>
<summary>Show answer</summary>

**Answer: B) It attempts to avoid collisions before they happen by using timing and coordination mechanisms**

*Explanation: CSMA/CA is a media access control method that attempts to avoid collisions before they happen. Devices first check if the medium is free, then transmit a notification of intent to use the medium, and finally send the data after receiving clearance. This method is particularly important in wireless networks where devices cannot detect collisions directly. It uses mechanisms like random backoff times and RTS/CTS (Request to Send/Clear to Send) to coordinate transmissions.*
</details>

### Question 11
What is the primary purpose of the Address Resolution Protocol (ARP)?
- A) To translate domain names to IP addresses
- B) To map IP addresses to MAC addresses
- C) To assign IP addresses dynamically to hosts
- D) To translate private IP addresses to public IP addresses

<details>
<summary>Show answer</summary>

**Answer: B) To map IP addresses to MAC addresses**

*Explanation: Address Resolution Protocol (ARP) is used to map an IP address (Network layer logical address) to a MAC address (Data Link layer physical address) on a local network. When a device needs to communicate with another device on the same local network, it uses ARP to discover the MAC address associated with the destination IP address, which is necessary for creating properly addressed frames at the Data Link layer.*
</details>

### Question 12
What is the main advantage of a mesh topology compared to other network topologies?
- A) Lower cost of implementation
- B) Simplified network management
- C) Higher fault tolerance and redundancy
- D) Reduced cabling requirements

<details>
<summary>Show answer</summary>

**Answer: C) Higher fault tolerance and redundancy**

*Explanation: The main advantage of a mesh topology is its high fault tolerance and redundancy. Because each device is connected to multiple other devices, if one connection fails, data can be routed through alternative paths. This redundancy makes mesh networks highly reliable and resilient to failures. However, these benefits come at the cost of increased complexity, higher implementation expense, and more cabling (in wired implementations).*
</details>

### Question 13
Which statement correctly describes the function of a port number in TCP/IP communication?
- A) Identifying a physical port on a network device
- B) Identifying the network portion of an IP address
- C) Identifying a specific application or service
- D) Identifying the transmission speed of a connection

<details>
<summary>Show answer</summary>

**Answer: C) Identifying a specific application or service**

*Explanation: Port numbers are 16-bit numbers used in TCP and UDP communication to identify specific applications or services running on a host. While IP addresses identify the host devices, port numbers distinguish between different applications on that device. For example, web servers typically use port 80 for HTTP and port 443 for HTTPS. This allows multiple network services to operate simultaneously on the same device.*
</details>

### Question 14
Which security principle ensures that information is accessible only to those authorized to have access?
- A) Integrity
- B) Availability
- C) Confidentiality
- D) Authentication

<details>
<summary>Show answer</summary>

**Answer: C) Confidentiality**

*Explanation: Confidentiality is the security principle that ensures information is accessible only to authorized individuals. It involves protecting sensitive information from unauthorized access through measures like encryption, access controls, and proper data classification. This is one of the three core principles of the CIA triad in information security, alongside Integrity (ensuring data remains accurate and unaltered) and Availability (ensuring data is accessible when needed).*
</details>

### Question 15
What is a primary characteristic of User Datagram Protocol (UDP)?
- A) Connection-oriented communication
- B) Guaranteed delivery of packets
- C) Flow control to prevent overwhelming the receiver
- D) Connectionless communication with no delivery guarantees

<details>
<summary>Show answer</summary>

**Answer: D) Connectionless communication with no delivery guarantees**

*Explanation: User Datagram Protocol (UDP) is characterized by connectionless communication with no delivery guarantees. It does not establish a connection before sending data, does not guarantee that packets will arrive, arrive in order, or arrive without duplication, and does not implement flow control or congestion control mechanisms. This simplicity results in lower overhead and faster transmission, making UDP suitable for applications where speed is more important than reliability, such as live streaming, online gaming, and DNS lookups.*
</details>

### Question 16
What principle of the CIA triad ensures that data cannot be modified in an unauthorized or undetected manner?
- A) Confidentiality
- B) Integrity
- C) Availability
- D) Accountability

<details>
<summary>Show answer</summary>

**Answer: B) Integrity**

*Explanation: Integrity is the security principle that ensures data cannot be modified in an unauthorized or undetected manner. It ensures the accuracy, consistency, and trustworthiness of data throughout its entire lifecycle. Integrity is maintained through measures like hash functions, digital signatures, checksums, and access controls that prevent unauthorized changes. This is one of the three core principles of the CIA triad, alongside Confidentiality and Availability.*
</details>

### Question 17
What is the primary function of a switch in a local area network?
- A) To convert digital signals to analog signals
- B) To connect devices and forward frames based on MAC addresses
- C) To route packets between different networks
- D) To assign IP addresses to network devices

<details>
<summary>Show answer</summary>

**Answer: B) To connect devices and forward frames based on MAC addresses**

*Explanation: The primary function of a switch in a local area network (LAN) is to connect devices and intelligently forward frames based on MAC addresses. Switches operate at the Data Link layer (Layer 2) of the OSI model. They build and maintain MAC address tables that map MAC addresses to specific physical ports, allowing them to selectively forward frames only to the port where the destination device is connected, rather than broadcasting to all ports. This improves network efficiency by creating separate collision domains for each port.*
</details>

### Question 18
What is the function of the LLC (Logical Link Control) sublayer of the Data Link layer?
- A) Converting bits into signals for transmission on the physical medium
- B) Managing media access control and handling collisions
- C) Providing an interface between the Network layer and the MAC sublayer
- D) Routing packets between different networks

<details>
<summary>Show answer</summary>

**Answer: C) Providing an interface between the Network layer and the MAC sublayer**

*Explanation: The Logical Link Control (LLC) sublayer is the upper sublayer of the Data Link layer that provides an interface between the Network layer above and the Media Access Control (MAC) sublayer below. It identifies which network layer protocol is being used for each frame and handles communication between these layers. The LLC is typically implemented in software (like a device driver) and is hardware-independent, making it consistent across different types of network interfaces.*
</details>

### Question 19
Which statement best describes a socket in TCP/IP networking?
- A) A physical connector on a network device
- B) A software interface for inter-process communication
- C) The combination of an IP address and a port number
- D) A special buffer for temporary storage of network data

<details>
<summary>Show answer</summary>

**Answer: C) The combination of an IP address and a port number**

*Explanation: In TCP/IP networking, a socket is the combination of an IP address and a port number that uniquely identifies an endpoint for network communication. The IP address identifies the host device, while the port number identifies the specific application or service on that device. For example, a web server listening at IP address 192.168.1.1 on port 80 would have the socket 192.168.1.1:80. Sockets enable multiple network applications to operate simultaneously on the same host.*
</details>

### Question 20
Which protocol is responsible for dynamically assigning IP addresses to devices on a network?
- A) ARP (Address Resolution Protocol)
- B) DHCP (Dynamic Host Configuration Protocol)
- C) DNS (Domain Name System)
- D) ICMP (Internet Control Message Protocol)

<details>
<summary>Show answer</summary>

**Answer: B) DHCP (Dynamic Host Configuration Protocol)**

*Explanation: The Dynamic Host Configuration Protocol (DHCP) is responsible for automatically assigning IP addresses and providing other network configuration information (such as subnet mask, default gateway, and DNS server addresses) to devices on a network. This eliminates the need for manual IP configuration, making network administration easier and preventing address conflicts. DHCP operates using a client-server model where clients request addressing information from a DHCP server.*
</details>

### Question 21
What is the principal reason for the development of IPv6?
- A) To improve routing efficiency
- B) To address IPv4 address exhaustion
- C) To enhance network security
- D) To reduce protocol overhead

<details>
<summary>Show answer</summary>

**Answer: B) To address IPv4 address exhaustion**

*Explanation: The principal reason for developing IPv6 was to address IPv4 address exhaustion. IPv4 uses 32-bit addresses, providing approximately 4.3 billion possible addresses, which proved insufficient for the growing internet. IPv6 uses 128-bit addresses, creating an astronomically larger address space (approximately 3.4 × 10^38 addresses). While IPv6 does include other improvements like simplified headers, built-in security features, and better support for mobile networks, addressing the limitation of available IPv4 addresses was the primary motivation.*
</details>

### Question 22
What type of cryptography uses the same key for both encryption and decryption?
- A) Asymmetric cryptography
- B) Public key cryptography
- C) Symmetric cryptography
- D) Quantum cryptography

<details>
<summary>Show answer</summary>

**Answer: C) Symmetric cryptography**

*Explanation: Symmetric cryptography (also called secret key cryptography) uses the same key for both encryption and decryption processes. This single shared key must be kept secret by all parties who need to encrypt or decrypt the data. While symmetric encryption is generally faster than asymmetric methods, its main challenge is securely distributing the key between communicating parties. Examples of symmetric encryption algorithms include AES, DES, and 3DES. Asymmetric or public key cryptography, by contrast, uses different keys for encryption and decryption.*
</details>

### Question 23
What is the main purpose of a Network Address Translation (NAT) device?
- A) To translate between different network protocols
- B) To allow multiple devices to share a single public IP address
- C) To convert domain names to IP addresses
- D) To filter network traffic based on security rules

<details>
<summary>Show answer</summary>

**Answer: B) To allow multiple devices to share a single public IP address**

*Explanation: The main purpose of Network Address Translation (NAT) is to allow multiple devices within a private network to share a single public IP address when communicating with external networks like the internet. NAT works by modifying network address information in packet headers as they pass through a routing device, mapping private IP addresses to the single public address (and different port numbers). This technology was developed to mitigate IPv4 address exhaustion and has the side benefit of providing some security by hiding internal network addresses.*
</details>

### Question 24
Which of the following is a limitation of Network Address Translation (NAT)?
- A) It increases network latency
- B) It complicates peer-to-peer applications
- C) It reduces network security
- D) It requires specialized hardware

<details>
<summary>Show answer</summary>

**Answer: B) It complicates peer-to-peer applications**

*Explanation: A significant limitation of Network Address Translation (NAT) is that it complicates peer-to-peer applications and services. Because NAT hides internal IP addresses, it can be difficult for external devices to initiate connections to devices behind NAT. This creates challenges for applications like VoIP, online gaming, and file sharing that require direct communication between peers. NAT traversal techniques like port forwarding, STUN, and TURN have been developed to address these issues, but they add complexity and may not always work reliably.*
</details>

### Question 25
What is the purpose of a MAC address table in a switch?
- A) To map domain names to IP addresses
- B) To map IP addresses to MAC addresses
- C) To map MAC addresses to switch ports
- D) To store device authentication credentials

<details>
<summary>Show answer</summary>

**Answer: C) To map MAC addresses to switch ports**

*Explanation: A MAC address table (also called a forwarding table or CAM table) in a switch maps MAC addresses of connected devices to the physical ports on the switch where they are connected. When a switch receives a frame, it checks the destination MAC address against this table to determine which port to forward the frame to, instead of broadcasting it to all ports. This allows the switch to intelligently forward traffic only to the necessary destinations, improving network efficiency by reducing unnecessary traffic.*
</details>

### Question 26
Which of the following is NOT a function of the Transport layer in the OSI model?
- A) Segmentation and reassembly of data
- B) End-to-end error recovery
- C) Flow control
- D) Path determination and routing

<details>
<summary>Show answer</summary>

**Answer: D) Path determination and routing**

*Explanation: Path determination and routing are not functions of the Transport layer (Layer 4); they are functions of the Network layer (Layer 3). The Transport layer is responsible for segmentation and reassembly of data, end-to-end error recovery and detection, flow control to prevent overwhelming the receiver, and identifying specific applications through port numbers. The Transport layer is concerned with reliable delivery between end hosts, while the Network layer handles routing data through intermediate networks.*
</details>

### Question 27
What does CSMA/CD stand for and where is it primarily used?
- A) Carrier Sense Multiple Access with Collision Detection, used in wired Ethernet
- B) Carrier Sense Multiple Access with Collision Detection, used in wireless networks
- C) Carrier Sense Multiple Access with Collision Delay, used in token ring networks
- D) Centralized System Multiple Access with Collision Detection, used in bus networks

<details>
<summary>Show answer</summary>

**Answer: A) Carrier Sense Multiple Access with Collision Detection, used in wired Ethernet**

*Explanation: CSMA/CD stands for Carrier Sense Multiple Access with Collision Detection and is primarily used in traditional wired Ethernet networks. It works by having devices first listen to see if the medium is free ("carrier sense"), allowing multiple devices to access the shared medium ("multiple access"), and detecting collisions when they occur so that transmissions can be stopped and retried after a random backoff period ("collision detection"). While historically important, CSMA/CD is less relevant in modern switched Ethernet environments where full-duplex connections minimize collisions.*
</details>

### Question 28
Which of the following correctly describes the three-way handshake in TCP connection establishment?
- A) SYN, SYN-ACK, ACK
- B) ACK, SYN, FIN
- C) SYN, ACK, FIN
- D) REQ, ACK, READY

<details>
<summary>Show answer</summary>

**Answer: A) SYN, SYN-ACK, ACK**

*Explanation: The TCP three-way handshake is a process used to establish a connection between client and server. It consists of three steps: (1) The client sends a SYN (synchronize) packet to the server to initiate the connection. (2) The server responds with a SYN-ACK (synchronize-acknowledge) packet, acknowledging the client's request and sending its own synchronization request. (3) The client sends an ACK (acknowledge) packet, acknowledging the server's synchronization request. After this three-way handshake, the TCP connection is established and data transfer can begin.*
</details>

### Question 29
What is the primary purpose of a hash function in information security?
- A) Encrypting data for secure transmission
- B) Authenticating users to network resources
- C) Creating a fixed-size representation of data for integrity verification
- D) Generating random encryption keys

<details>
<summary>Show answer</summary>

**Answer: C) Creating a fixed-size representation of data for integrity verification**

*Explanation: The primary purpose of a hash function in information security is to create a fixed-size representation (hash value or digest) of data that can be used for integrity verification. Hash functions take input data of any size and produce a fixed-length output in a way that any change to the input data, no matter how small, results in a completely different hash value. This property makes hash functions valuable for verifying that data hasn't been altered, for storing passwords securely (by storing hashes rather than plaintext), and for digital signatures.*
</details>

### Question 30
What is the purpose of the Session layer in the OSI model?
- A) To establish, manage, and terminate dialogs between applications
- B) To translate data between different formats and encryption methods
- C) To route packets between different networks
- D) To control access to the physical medium

<details>
<summary>Show answer</summary>

**Answer: A) To establish, manage, and terminate dialogs between applications**

*Explanation: The Session layer (Layer 5) of the OSI model is responsible for establishing, managing, and terminating dialogs (sessions) between applications. It sets up and coordinates the communication between end-user application processes. This includes functions like establishing, maintaining, and synchronizing the dialogue between applications, managing the session through checkpointing and recovery procedures, and controlling whether communication can be half-duplex (one way at a time) or full-duplex (both ways simultaneously).*
</details>

### Question 31
What type of attack involves sending a large number of connection requests to a server without completing the connection process?
- A) SQL injection attack
- B) Cross-site scripting attack
- C) SYN flood attack
- D) Man-in-the-middle attack

<details>
<summary>Show answer</summary>

**Answer: C) SYN flood attack**

*Explanation: A SYN flood attack is a form of denial-of-service attack where an attacker sends a succession of SYN (synchronize) packets to a target server, but never completes the third step of the TCP three-way handshake. This leaves the server with numerous half-open connections waiting for completion. Each half-open connection consumes server resources until it times out, potentially exhausting the server's capacity to accept legitimate connections. This attack exploits the TCP connection establishment process to overwhelm system resources.*
</details>

### Question 32
What is the function of the File Transfer Protocol (FTP)?
- A) To transfer hypertext documents between web servers and browsers
- B) To provide reliable file transfer between systems on a network
- C) To map domain names to IP addresses
- D) To send email messages between mail servers

<details>
<summary>Show answer</summary>

**Answer: B) To provide reliable file transfer between systems on a network**

*Explanation: File Transfer Protocol (FTP) is an Application layer protocol designed to transfer files reliably between systems on a network. It provides functions for authenticating users, navigating directory structures, and transferring files in either direction. FTP uses a separate control connection for sending commands and a data connection for actually transferring files. While still used, FTP has security limitations as it typically sends data in unencrypted form, leading to the development of more secure alternatives like SFTP and FTPS.*
</details>

### Question 33
What is a benefit of using a client-server network model compared to a peer-to-peer model?
- A) Lower cost of implementation
- B) Simplified setup and maintenance
- C) Centralized administration and improved security
- D) Better performance for small networks

<details>
<summary>Show answer</summary>

**Answer: C) Centralized administration and improved security**

*Explanation: A major benefit of the client-server network model compared to peer-to-peer is centralized administration and improved security. Client-server networks use dedicated servers that centralize resource management, user authentication, access control, and security policies. This centralization makes it easier to implement consistent security measures, back up critical data, manage user accounts, and control resource access. While client-server networks are more complex and expensive to set up, the administrative and security advantages make them preferred for medium to large organizations.*
</details>

### Question 34
What is the main difference between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol)?
- A) TCP operates at the Network layer, while UDP operates at the Transport layer
- B) TCP provides connection-oriented, reliable delivery, while UDP provides connectionless, best-effort delivery
- C) TCP is used for web browsing, while UDP is used exclusively for email
- D) TCP supports broadcast transmissions, while UDP supports only unicast transmissions

<details>
<summary>Show answer</summary>

**Answer: B) TCP provides connection-oriented, reliable delivery, while UDP provides connectionless, best-effort delivery**

*Explanation: The main difference between TCP and UDP is that TCP provides connection-oriented, reliable delivery while UDP provides connectionless, best-effort delivery. TCP establishes a connection before data transfer, ensures data arrives in order, implements error detection and recovery through acknowledgments and retransmissions, and includes flow control mechanisms. UDP, in contrast, does not establish connections, provides no guarantees about delivery or ordering, and offers no flow control or error recovery. Both protocols operate at the Transport layer but serve different purposes, with TCP prioritizing reliability and UDP prioritizing speed and low overhead.*
</details>

### Question 35
Which protocol is used to translate domain names to IP addresses?
- A) ARP (Address Resolution Protocol)
- B) DHCP (Dynamic Host Configuration Protocol)
- C) DNS (Domain Name System)
- D) NAT (Network Address Translation)

<details>
<summary>Show answer</summary>

**Answer: C) DNS (Domain Name System)**

*Explanation: The Domain Name System (DNS) is the protocol used to translate human-readable domain names (like www.example.com) into machine-readable IP addresses (like 93.184.216.34). DNS operates as a distributed hierarchical database, with different servers responsible for different portions of the domain namespace. This system allows users to access network resources using memorable domain names rather than having to remember numeric IP addresses, effectively functioning as the "phone book" of the Internet.*
</details>

### Question 36
What security vulnerability is being exploited when an attacker inputs code like "' OR '1'='1" into a web form?
- A) Cross-site scripting
- B) SQL injection
- C) Buffer overflow
- D) Session hijacking

<details>
<summary>Show answer</summary>

**Answer: B) SQL injection**

*Explanation: The code "' OR '1'='1" is a classic example of a SQL injection attack. In this attack, malicious SQL code is inserted into input fields that are later passed to a database for execution. The statement '1'='1' is always true, so when this input is incorporated into a query without proper validation, it can trick the database into returning all records or granting unauthorized access. For example, in a login form, this might bypass authentication by creating a condition that's always true. SQL injection exploits inadequate input validation and can allow attackers to access, modify, or delete database content.*
</details>

### Question 37
What is the main advantage of Public Key Infrastructure (PKI) in network security?
- A) It's faster than symmetric key encryption
- B) It provides a framework for secure key distribution and authentication
- C) It requires less computational resources
- D) It's immune to all types of cyberattacks

<details>
<summary>Show answer</summary>

**Answer: B) It provides a framework for secure key distribution and authentication**

*Explanation: The main advantage of Public Key Infrastructure (PKI) in network security is that it provides a comprehensive framework for secure key distribution and authentication. PKI solves the key distribution problem inherent in symmetric cryptography by using asymmetric cryptography with public/private key pairs, digital certificates, and certificate authorities. This infrastructure enables secure communication between parties who have never previously exchanged secrets, allows for digital signatures to verify identity and ensure non-repudiation, and provides mechanisms for certificate validation and revocation. These capabilities make PKI fundamental to secure internet communication.*
</details>

### Question 38
What is the purpose of the Diffie-Hellman key exchange algorithm?
- A) To encrypt data for transmission across networks
- B) To authenticate users before granting network access
- C) To securely establish a shared secret key over an insecure channel
- D) To generate digital signatures for non-repudiation

<details>
<summary>Show answer</summary>

**Answer: C) To securely establish a shared secret key over an insecure channel**

*Explanation: The purpose of the Diffie-Hellman key exchange algorithm is to allow two parties to securely establish a shared secret key over an insecure communication channel without requiring prior shared secrets. The parties exchange public information but use mathematical properties that make it computationally infeasible for an eavesdropper to determine the shared secret. This shared key can then be used for symmetric encryption. Diffie-Hellman addresses the key distribution problem in symmetric cryptography without actually transmitting the key itself, providing forward secrecy for communications.*
</details>

### Question 39
What is the role of a subnet mask in IP addressing?
- A) To encrypt IP addresses for secure transmission
- B) To divide an IP address into network and host portions
- C) To translate between IPv4 and IPv6 addresses
- D) To compress IP headers for efficient transmission

<details>
<summary>Show answer</summary>

**Answer: B) To divide an IP address into network and host portions**

*Explanation: The role of a subnet mask in IP addressing is to divide an IP address into network and host portions. A subnet mask is a 32-bit number (in IPv4) that, when applied to an IP address, determines which bits identify the network and which bits identify the host on that network. This division enables routers to determine whether a destination is on the local network or requires routing to another network. Subnet masks also allow network administrators to subdivide a single network address space into multiple smaller networks (subnetting), improving address utilization and network management.*
</details>

### Question 40
What is latency in computer networking?
- A) The maximum data transfer rate of a network
- B) The delay between sending and receiving data
- C) The amount of data that can be transferred in a given time period
- D) The number of devices connected to a network

<details>
<summary>Show answer</summary>

**Answer: B) The delay between sending and receiving data**

*Explanation: Latency in computer networking refers to the delay between the moment data is sent and the moment it is received. It represents the time it takes for data to travel from the source to the destination, typically measured in milliseconds. Latency can be affected by physical distance, transmission medium, network congestion, processing delays at intermediate devices, and protocol overhead. Low latency is particularly important for real-time applications like video conferencing, online gaming, and financial trading systems where delays are noticeable and can impact performance.*
</details>

### Question 41
What is the function of the Domain Name System (DNS) in computer networking?
- A) To assign IP addresses to network devices dynamically
- B) To translate domain names to IP addresses
- C) To encrypt data for secure transmission across networks
- D) To map MAC addresses to IP addresses on a local network

<details>
<summary>Show answer</summary>

**Answer: B) To translate domain names to IP addresses**

*Explanation: The Domain Name System (DNS) serves as the "phone book" of the Internet by translating human-readable domain names (like www.example.com) into machine-readable IP addresses (like 192.0.2.1). This translation is essential because while domain names are easy for people to remember, computers and networking equipment need numeric IP addresses to route traffic across networks. DNS operates as a hierarchical, distributed database with various DNS servers responsible for different portions of the namespace, enabling users to access websites and services using memorable names instead of numerical addresses.*
</details>

### Question 42
What distinguishes a botnet from other types of network security threats?
- A) Botnets only target government networks
- B) Botnets use a network of compromised computers controlled by a central entity
- C) Botnets only steal sensitive data but cannot cause service disruption
- D) Botnets can only propagate through email attachments

<details>
<summary>Show answer</summary>

**Answer: B) Botnets use a network of compromised computers controlled by a central entity**

*Explanation: A botnet is a network of compromised computers ("zombies") that have been infected with malware allowing them to be remotely controlled by an attacker (the "bot herder"). What distinguishes botnets from other security threats is this distributed nature—they harness the collective computing power and bandwidth of many machines to perform coordinated activities. Botnets are commonly used for distributed denial-of-service (DDoS) attacks, spam distribution, crypto mining, credential theft, and other malicious activities. The distributed architecture makes botnets difficult to shut down, as disabling one compromised machine has minimal impact on the overall botnet functionality.*
</details>

### Question 43
Which statement best describes the principle of availability in the CIA security triad?
- A) Ensuring that data is accessible only to authorized individuals
- B) Ensuring that data cannot be modified in an unauthorized manner
- C) Ensuring systems, networks, and data are accessible when needed
- D) Ensuring that users can be uniquely identified on the network

<details>
<summary>Show answer</summary>

**Answer: C) Ensuring systems, networks, and data are accessible when needed**

*Explanation: Availability, one of the three pillars of the CIA (Confidentiality, Integrity, Availability) security triad, focuses on ensuring that systems, networks, and data are accessible and operational when authorized users need them. This principle involves implementing measures to maintain hardware reliability, providing adequate system performance, ensuring prompt system maintenance, and implementing business continuity and disaster recovery plans. Threats to availability include denial-of-service attacks, equipment failures, natural disasters, and system upgrades or maintenance that cause downtime. While confidentiality protects against unauthorized access and integrity ensures data accuracy, availability ensures legitimate users can access resources when required.*
</details>

### Question 44
What is the main function of the Open Shortest Path First (OSPF) protocol in networking?
- A) To secure communication between networks using encryption
- B) To translate between different network protocols
- C) To calculate the optimal routing paths within an autonomous system
- D) To manage quality of service for multimedia applications

<details>
<summary>Show answer</summary>

**Answer: C) To calculate the optimal routing paths within an autonomous system**

*Explanation: Open Shortest Path First (OSPF) is a link-state routing protocol that functions primarily to calculate optimal paths for routing data within an autonomous system (a collection of networks under common administrative control). OSPF works by having routers exchange information about their connections to build identical link-state databases. Each router then independently runs the Dijkstra algorithm on this database to calculate the shortest path to all possible destinations. OSPF responds quickly to network topology changes, supports variable-length subnet masking (VLSM), performs load balancing across equal-cost paths, and uses area-based hierarchy for scalability in large networks. It's commonly used in enterprise networks and by Internet service providers for internal routing.*
</details>

### Question 45
What is the primary difference between symmetric and asymmetric encryption in terms of key usage?
- A) Symmetric encryption is always faster but less secure than asymmetric encryption
- B) Symmetric encryption uses the same key for encryption and decryption, while asymmetric encryption uses different keys
- C) Symmetric encryption can only encrypt small amounts of data, while asymmetric encryption handles any data size
- D) Symmetric encryption is used for authentication, while asymmetric encryption is used only for confidentiality

<details>
<summary>Show answer</summary>

**Answer: B) Symmetric encryption uses the same key for encryption and decryption, while asymmetric encryption uses different keys**

*Explanation: The primary difference between symmetric and asymmetric encryption lies in their key usage. Symmetric encryption uses a single shared key for both encrypting and decrypting data. This makes it faster and more efficient for large data volumes, but creates the challenge of securely distributing the shared key. Asymmetric encryption (also called public key cryptography) uses mathematically related but different keys—a public key for encryption and a private key for decryption. This solves the key distribution problem, as the public key can be freely shared. While asymmetric encryption is computationally more intensive and slower, it provides functions like digital signatures and secure key exchange that are difficult with symmetric systems. In practice, many secure systems use both types together: asymmetric for initial key exchange, followed by symmetric encryption for bulk data transfer.*
</details>