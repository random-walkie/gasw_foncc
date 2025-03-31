# Mock Exam 3: Network Security and Advanced Concepts

## Part 1: Option Selection Questions (10 marks)

For these questions, select the appropriate option or options that correctly complete the statement or answer the question.

### Question 1
Select all items that are classified as physical transmission media in computer networks:
- [ ] Ethernet cables
- [ ] Fiber optic cables
- [ ] Wi-Fi
- [ ] Bluetooth
- [ ] Coaxial cables
- [ ] TCP/IP
- [ ] Microwave

<details>
<summary>Show answer</summary>

**Answer:** Ethernet cables, Fiber optic cables, Coaxial cables

*Explanation: Physical transmission media refers to the tangible pathways over which network communication travels. Ethernet cables (twisted pair copper), fiber optic cables, and coaxial cables are all physical media. Wi-Fi, Bluetooth, and Microwave are wireless technologies that use electromagnetic waves through the air (not physical media). TCP/IP is a protocol suite, not a transmission medium.*
</details>

### Question 2
Select all cybersecurity attack types discussed in the lecture materials:
- [ ] Cyberstalking
- [ ] Buffer overflow
- [ ] Phishing
- [ ] SQL injection
- [ ] Botnet attacks
- [ ] SYN flood
- [ ] Cross-site scripting

<details>
<summary>Show answer</summary>

**Answer:** Cyberstalking, Buffer overflow, Phishing, SQL injection, Botnet attacks, SYN flood

*Explanation: The lecture materials covered several types of cybersecurity attacks, including cyberstalking (online harassment), buffer overflow (exploiting memory allocation vulnerabilities), phishing (social engineering to steal credentials), SQL injection (inserting malicious SQL code), botnet attacks (using networks of compromised computers), and SYN flood (a type of DoS attack). Cross-site scripting was not specifically covered in the provided lecture slides.*
</details>

### Question 3
Select all factors that affect network latency:
- [ ] Type of transmission media
- [ ] Distance between source and destination
- [ ] Network congestion
- [ ] Network protocol overhead
- [ ] Number of intermediate devices
- [ ] Size of data being transmitted
- [ ] MAC address length

<details>
<summary>Show answer</summary>

**Answer:** Type of transmission media, Distance between source and destination, Network congestion, Network protocol overhead, Number of intermediate devices

*Explanation: Latency (the delay in data transmission) is affected by several factors including the type of transmission media (e.g., fiber vs. copper), physical distance between communicating devices, network congestion (traffic volume), protocol overhead (processing time for headers/acknowledgments), and the number of intermediate devices (routers/switches) data must pass through. While data size affects throughput and overall transfer time, it doesn't directly impact latency. MAC address length is standardized and doesn't affect latency.*
</details>

### Question 4
Select all security principles that are part of the CIA triad:
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

*Explanation: The CIA triad consists of three fundamental security principles: Confidentiality (ensuring data is accessible only to authorized users), Integrity (ensuring data remains accurate and unaltered), and Availability (ensuring systems and data are accessible when needed). The other options—Authentication, Authorization, Accountability, and Non-repudiation—are important security concepts but not part of the CIA triad itself.*
</details>

### Question 5
Select all characteristics of packet-switched networks:
- [ ] Dedicated end-to-end path for the entire communication session
- [ ] Messages divided into packets
- [ ] Packets may take different routes to destination
- [ ] Fixed bandwidth allocation throughout communication
- [ ] Efficient use of available bandwidth
- [ ] Packets reassembled at destination
- [ ] Connection must be established before data transfer

<details>
<summary>Show answer</summary>

**Answer:** Messages divided into packets, Packets may take different routes to destination, Efficient use of available bandwidth, Packets reassembled at destination

*Explanation: Packet-switched networks divide messages into packets, allow packets to take different routes to the destination, use bandwidth efficiently by sharing network resources among multiple communications, and require packets to be reassembled at the destination. Circuit-switched networks (not packet-switched) establish dedicated end-to-end paths and allocate fixed bandwidth for the entire session. Connection establishment before data transfer is characteristic of connection-oriented protocols (like TCP) but isn't inherent to all packet-switched networks.*
</details>

## Part 2: Multiple-Choice Questions (90 marks)

### Question 1
Which wireless network media access control method uses timing schemes and request-to-send/clear-to-send mechanisms to reduce collisions?
- A) CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
- B) CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
- C) Token Passing
- D) Polling

<details>
<summary>Show answer</summary>

**Answer: B) CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)**

*Explanation: CSMA/CA is specifically designed for wireless networks where devices cannot directly detect collisions. It implements collision avoidance through timing schemes and RTS/CTS (Request to Send/Clear to Send) mechanisms. Devices first check if the medium is free, then transmit a notification of intent to use the medium, wait for acknowledgment, and only then send data. This approach attempts to prevent collisions before they happen, unlike CSMA/CD which detects collisions after they occur in wired networks.*
</details>

### Question 2
What is the primary limitation of symmetric key cryptography in network security?
- A) It is too slow for practical use
- B) It provides inadequate encryption strength
- C) Securely distributing the shared key between communicating parties
- D) It can only encrypt small amounts of data

<details>
<summary>Show answer</summary>

**Answer: C) Securely distributing the shared key between communicating parties**

*Explanation: The primary limitation of symmetric key cryptography is the key distribution problem—how to securely share the secret key between communicating parties before encrypted communication can begin. If an attacker intercepts the key during transmission, they could decrypt all subsequent communications. This challenge led to the development of asymmetric (public key) cryptography and key exchange algorithms like Diffie-Hellman, which allow secure key establishment over insecure channels. Symmetric encryption is actually faster than asymmetric methods and provides strong security when implemented properly.*
</details>

### Question 3
In a cyberstalking scenario, which statement is NOT true according to the lecture materials?
- A) 40% of victims are men
- B) 44% of victims endure offline stalking
- C) Most offenders are unknown to the victims
- D) 71% of victims are under 40 years old

<details>
<summary>Show answer</summary>

**Answer: C) Most offenders are unknown to the victims**

*Explanation: According to the cyberstalking statistics presented in the lecture materials, approximately 70% of offenders are known to their victims. The other statements are correct: about 40% of victims are men (60% women), 44% of victims also experience offline stalking, and 71% of victims are under 40 years of age. These statistics highlight that cyberstalking is often connected to real-world relationships rather than being primarily from anonymous strangers.*
</details>

### Question 4
What makes a hash function suitable for password storage?
- A) It produces the same output for different inputs
- B) It allows quick decryption when needed
- C) It creates a fixed-length output for any input length
- D) It enables recovery of the original password if forgotten

<details>
<summary>Show answer</summary>

**Answer: C) It creates a fixed-length output for any input length**

*Explanation: Hash functions are suitable for password storage because they create a fixed-length output (hash value) for any input length and are designed to be one-way functions—it should be computationally infeasible to reverse the process and determine the original input from the hash value. This means passwords can be stored as hashes rather than in plaintext. When a user attempts to log in, the system hashes the entered password and compares it to the stored hash. If they match, the password is correct, but the system never needs to know the actual password.*
</details>

### Question 5
Which network topology provides the highest level of redundancy but at the highest cost?
- A) Bus topology
- B) Star topology
- C) Ring topology
- D) Mesh topology

<details>
<summary>Show answer</summary>

**Answer: D) Mesh topology**

*Explanation: A mesh topology provides the highest level of redundancy because each device is connected directly to many or all other devices in the network. If one connection fails, data can be routed through alternative paths. This redundancy makes mesh networks highly fault-tolerant and reliable, but also the most expensive to implement due to the large number of connections required. Each device needs multiple network interfaces, and cabling costs (in wired implementations) are substantially higher than other topologies.*
</details>

### Question 6
What is the main issue addressed by Network Address Translation (NAT)?
- A) Network security vulnerabilities
- B) IPv4 address exhaustion
- C) Slow network performance
- D) Incompatible network protocols

<details>
<summary>Show answer</summary>

**Answer: B) IPv4 address exhaustion**

*Explanation: Network Address Translation (NAT) was primarily developed to address IPv4 address exhaustion. NAT allows multiple devices on a private network to share a single public IP address when communicating with external networks. This conservation of public IP addresses helped extend the usable life of the IPv4 addressing scheme as the Internet grew. While NAT does provide some security benefits by hiding internal network addresses, this was a secondary benefit rather than its main purpose.*
</details>

### Question 7
What is a primary advantage of fiber optic cables over copper cables?
- A) Lower cost of installation
- B) Easier to splice and repair
- C) Greater resistance to electromagnetic interference
- D) Higher flexibility and durability

<details>
<summary>Show answer</summary>

**Answer: C) Greater resistance to electromagnetic interference**

*Explanation: A primary advantage of fiber optic cables over copper cables is their complete immunity to electromagnetic interference (EMI) and radio frequency interference (RFI). Because fiber optics use light signals rather than electrical signals, they are not affected by electrical noise from nearby equipment, power lines, or other sources of interference. This makes fiber ideal for environments with high electromagnetic interference or where sensitive data must be transmitted without the risk of signal degradation or interception. Other advantages include higher bandwidth, longer transmission distances, and greater security, but these weren't listed as options.*
</details>

### Question 8
Which of the following is NOT a countermeasure for DDoS attacks?
- A) Using firewalls with simple allow/deny rules
- B) Implementing rate-limiting on network equipment
- C) Deploying honeypots to attract attackers
- D) Using blackholing to drop attack traffic

<details>
<summary>Show answer</summary>

**Answer: C) Deploying honeypots to attract attackers**

*Explanation: Deploying honeypots is not a direct countermeasure for DDoS attacks. Honeypots are decoy systems designed to attract attackers to study their techniques or divert them from actual targets, but they don't mitigate active DDoS attacks. Effective DDoS countermeasures include firewalls with allow/deny rules to filter malicious traffic, rate-limiting to prevent overwhelming connections, blackholing (null routing) to drop attack traffic, and DDoS defense systems that can distinguish between legitimate and attack traffic. Honeypots are more useful for general threat intelligence than for defending against ongoing DDoS attacks.*
</details>

### Question 9
What is a "trapdoor" in the context of asymmetric cryptography?
- A) A security vulnerability in the encryption algorithm
- B) A mathematical function that is easy to compute in one direction but difficult to reverse
- C) A backdoor built into encryption systems for government access
- D) A method for quickly decrypting messages in emergency situations

<details>
<summary>Show answer</summary>

**Answer: B) A mathematical function that is easy to compute in one direction but difficult to reverse**

*Explanation: In asymmetric cryptography, a "trapdoor" refers to a mathematical function that is relatively easy to compute in one direction but computationally difficult to reverse without specific additional information. This property forms the foundation of public key cryptography. For example, multiplying two large prime numbers is relatively straightforward, but factoring their product back into the original primes is extremely difficult without knowing one of the primes beforehand. The "trapdoor" is the secret information (like a private key) that makes the reverse computation feasible for the authorized party but infeasible for anyone else.*
</details>

### Question 10
In the context of SQL injection attacks, what does the input string "1=1" attempt to exploit?
- A) Buffer overflow vulnerabilities
- B) Weak password policies
- C) Always-true conditions in SQL queries
- D) Cross-site scripting vulnerabilities

<details>
<summary>Show answer</summary>

**Answer: C) Always-true conditions in SQL queries**

*Explanation: In SQL injection attacks, the string "1=1" is used to exploit inadequate input validation by creating a condition that is always true. When inserted into a SQL query, this condition can trick the database into returning all records or bypassing authentication checks. For example, in a login form where the query might be "SELECT * FROM users WHERE username='input1' AND password='input2'", injecting "' OR '1'='1" for the username would modify the query to "SELECT * FROM users WHERE username='' OR '1'='1' AND password='input2'". Since 1=1 is always true, this could return all user records, potentially allowing unauthorized access.*
</details>

### Question 11
What is the primary purpose of the MD5 algorithm in network security?
- A) Encrypting data for transmission
- B) Generating random encryption keys
- C) Creating message digests for integrity verification
- D) Establishing secure communication channels

<details>
<summary>Show answer</summary>

**Answer: C) Creating message digests for integrity verification**

*Explanation: The primary purpose of the MD5 (Message Digest 5) algorithm is to create fixed-size message digests (hashes) that serve as "fingerprints" of data for integrity verification. By comparing the hash value of received data with the expected hash, recipients can verify that the data hasn't been altered during transmission. However, it's important to note that while this was the original purpose of MD5, the algorithm is now considered cryptographically broken due to vulnerability to collision attacks. Modern systems have largely replaced MD5 with more secure hash functions like SHA-256 for integrity verification.*
</details>

### Question 12
Which Internet Protocol version introduced significantly expanded address space as its primary improvement?
- A) IPv4
- B) IPv5
- C) IPv6
- D) IPv7

<details>
<summary>Show answer</summary>

**Answer: C) IPv6**

*Explanation: IPv6 (Internet Protocol version 6) was developed primarily to address the limitation of IPv4's address space. IPv6 uses 128-bit addresses compared to IPv4's 32-bit addresses, creating an astronomically larger address space (approximately 3.4 × 10^38 addresses versus IPv4's 4.3 billion). This expansion was the principal improvement and motivation behind IPv6's development, addressing the exhaustion of available IPv4 addresses due to the Internet's growth. IPv6 also introduced other improvements like simplified headers, built-in security, and better support for mobile networks, but the expanded address space was the primary driver.*
</details>

### Question 13
What is the main difference between goodput and throughput in network performance metrics?
- A) Goodput measures wired connections while throughput measures wireless connections
- B) Goodput measures download speed while throughput measures upload speed
- C) Goodput measures useful data transfer while throughput includes protocol overhead
- D) Goodput is a theoretical maximum while throughput is the actual measured performance

<details>
<summary>Show answer</summary>

**Answer: C) Goodput measures useful data transfer while throughput includes protocol overhead**

*Explanation: The main difference between goodput and throughput is that goodput measures the amount of useful application data transferred in a given time period, excluding protocol overhead, retransmissions, and other non-application data. Throughput, on the other hand, measures the total amount of data transferred, including all headers, acknowledgments, retransmissions, and other protocol overhead. Goodput represents what the application actually receives, while throughput represents the total network utilization. This means goodput is always less than or equal to throughput and provides a better measure of effective application performance.*
</details>

### Question 14
Which of the following is a characteristic of peer-to-peer networks?
- A) Centralized administration
- B) Dedicated server requirements
- C) Simple setup but limited scalability
- D) Higher security than client-server models

<details>
<summary>Show answer</summary>

**Answer: C) Simple setup but limited scalability**

*Explanation: Peer-to-peer networks are characterized by simple setup procedures but limited scalability. In these networks, computers share resources directly without requiring a dedicated server, making them easy and inexpensive to establish for small workgroups. However, as the network grows, the lack of centralized administration becomes problematic, and performance can degrade. Peer-to-peer networks typically don't have centralized administration (ruling out option A), don't require dedicated servers (ruling out option B), and generally offer lower security than client-server models due to the distributed nature of access controls (ruling out option D).*
</details>

### Question 15
What does a subnet mask of 255.255.0.0 indicate about an IP address?
- A) It's a Class A address with the default subnet mask
- B) It's a Class B address with the default subnet mask
- C) It's a Class C address with the default subnet mask
- D) It's a custom subnetting scheme that doesn't match standard classes

<details>
<summary>Show answer</summary>

**Answer: B) It's a Class B address with the default subnet mask**

*Explanation: A subnet mask of 255.255.0.0 (or /16 in CIDR notation) indicates that the first 16 bits (two octets) of the IP address represent the network portion, while the last 16 bits (two octets) represent the host portion. This corresponds to the default subnet mask for a Class B address under the traditional classful IP addressing scheme. Class B addresses have the first bit as 1 and the second bit as 0, giving a range of 128.0.0.0 to 191.255.255.255. The default subnet masks for Class A, B, and C are 255.0.0.0 (/8), 255.255.0.0 (/16), and 255.255.255.0 (/24) respectively.*
</details>

### Question 16
Which of the following is a major limitation of Network Address Translation (NAT)?
- A) It significantly increases network latency
- B) It prevents the use of encryption in network communications
- C) It complicates peer-to-peer applications and direct connections
- D) It requires specialized hardware that is expensive to deploy

<details>
<summary>Show answer</summary>

**Answer: C) It complicates peer-to-peer applications and direct connections**

*Explanation: A major limitation of Network Address Translation (NAT) is that it complicates peer-to-peer applications and direct connections. Because NAT hides internal network addresses, external devices typically cannot initiate connections to devices behind NAT. This creates challenges for applications like VoIP, online gaming, and file sharing that require direct peer-to-peer communication. While NAT introduces a small amount of processing overhead, it doesn't significantly increase latency (A). NAT doesn't prevent encryption (B)—encrypted traffic can pass through NAT devices. And NAT functionality is built into most routers and firewalls today, not requiring expensive specialized hardware (D).*
</details>

### Question 17
What is the purpose of the Physical layer in the OSI model?
- A) To establish logical connections between applications
- B) To route data between different networks
- C) To control access to the shared medium
- D) To transmit raw bit streams over a physical medium

<details>
<summary>Show answer</summary>

**Answer: D) To transmit raw bit streams over a physical medium**

*Explanation: The purpose of the Physical layer (Layer 1) in the OSI model is to transmit raw bit streams over a physical medium. This layer defines the electrical, mechanical, and procedural specifications for activating, maintaining, and deactivating physical connections. It's responsible for converting digital data (represented as binary 1s and 0s) into signals appropriate for the transmission medium, such as electrical voltages, light pulses, or radio waves. The Physical layer deals with aspects like signal timing, voltage levels, data rates, physical connectors, and transmission modes.*
</details>

### Question 18
In the context of cybersecurity, what does the term "phishing" refer to?
- A) Scanning networks for vulnerable systems
- B) Using social engineering to trick users into revealing sensitive information
- C) Intercepting network traffic between two parties
- D) Exploiting buffer overflow vulnerabilities in applications

<details>
<summary>Show answer</summary>

**Answer: B) Using social engineering to trick users into revealing sensitive information**

*Explanation: Phishing refers to social engineering attacks that attempt to trick users into revealing sensitive information like passwords, credit card numbers, or personal data by masquerading as a trustworthy entity. Typically, attackers send fraudulent emails, messages, or create fake websites that appear to be from legitimate organizations (like banks, social media platforms, or payment services). These communications often create a sense of urgency and direct users to fake login pages designed to capture credentials. Phishing relies primarily on manipulating human psychology rather than technical vulnerabilities, making it a persistent threat regardless of technical security measures.*
</details>

### Question 19
Which statement best describes the Diffie-Hellman key exchange algorithm?
- A) It's used to encrypt data using a pre-shared secret key
- B) It's a method for authenticating users based on public key certificates
- C) It allows two parties to securely establish a shared key over an insecure channel
- D) It's a symmetric encryption algorithm that uses block ciphers

<details>
<summary>Show answer</summary>

**Answer: C) It allows two parties to securely establish a shared key over an insecure channel**

*Explanation: The Diffie-Hellman key exchange algorithm allows two parties to securely establish a shared secret key over an insecure communication channel without requiring prior secret sharing. It uses mathematical properties that make it computationally infeasible for an eavesdropper to determine the shared secret, even when they can observe all the communications. The parties exchange public values and each performs calculations with their private values to arrive at the same shared secret. This shared key can then be used for symmetric encryption. Diffie-Hellman addresses the key distribution problem in symmetric cryptography without actually transmitting the key itself.*
</details>

### Question 20
What distinguishes the MAC (Media Access Control) sublayer from the LLC (Logical Link Control) sublayer in the Data Link layer?
- A) MAC handles communication with upper layers, while LLC manages physical medium access
- B) MAC is implemented in hardware, while LLC is typically implemented in software
- C) MAC deals with error correction, while LLC handles addressing
- D) MAC is used in wired networks, while LLC is used in wireless networks

<details>
<summary>Show answer</summary>

**Answer: B) MAC is implemented in hardware, while LLC is typically implemented in software**

*Explanation: A key distinction between the MAC and LLC sublayers is that the MAC sublayer is typically implemented in hardware (within the network interface card), while the LLC sublayer is usually implemented in software (often as a device driver). The MAC sublayer is hardware-specific and handles direct communication with the physical medium, including media access methods, physical addressing, and frame formatting. The LLC sublayer provides a hardware-independent interface to the Network layer above, identifying which network layer protocol is being used. This separation allows different physical networks to present a consistent interface to the upper layers.*
</details>

### Question 21
What type of attack attempts to overwhelm a system by flooding it with more traffic than it can handle?
- A) Man-in-the-middle attack
- B) SQL injection attack
- C) Denial of Service attack
- D) Buffer overflow attack

<details>
<summary>Show answer</summary>

**Answer: C) Denial of Service attack**

*Explanation: A Denial of Service (DoS) attack attempts to overwhelm a system, service, or network by flooding it with more traffic than it can handle, making it unavailable to legitimate users. These attacks consume server resources such as bandwidth, processing power, or memory until the target system becomes slow, crashes, or can no longer respond to legitimate requests. DDoS (Distributed Denial of Service) attacks are a more powerful variant where multiple compromised systems (a botnet) are coordinated to launch the attack simultaneously. Unlike the other options, which exploit vulnerabilities to gain unauthorized access or execute code, DoS attacks primarily aim to disrupt availability rather than breach security.*
</details>

### Question 22
What protocol is responsible for translating domain names to IP addresses?
- A) DHCP (Dynamic Host Configuration Protocol)
- B) ARP (Address Resolution Protocol)
- C) DNS (Domain Name System)
- D) SMTP (Simple Mail Transfer Protocol)

<details>
<summary>Show answer</summary>

**Answer: C) DNS (Domain Name System)**

*Explanation: The Domain Name System (DNS) is responsible for translating human-readable domain names (like www.example.com) into machine-readable IP addresses (like 93.184.216.34) that computers use to identify each other on networks. DNS operates through a distributed database structure, with different servers responsible for different portions of the domain namespace. When a user enters a domain name, the system queries DNS servers to resolve it to the corresponding IP address, allowing network communication to proceed. This translation allows people to use memorable domain names instead of having to remember numeric IP addresses.*
</details>

### Question 23
Which security principle ensures that information is accessible when required?
- A) Confidentiality
- B) Integrity
- C) Availability
- D) Non-repudiation

<details>
<summary>Show answer</summary>

**Answer: C) Availability**

*Explanation: Availability is the security principle that ensures information and systems are accessible and operational when required by authorized users. This principle focuses on maintaining hardware reliability, implementing fault tolerance, ensuring prompt system maintenance, and creating business continuity and disaster recovery plans. Threats to availability include hardware failures, software errors, denial of service attacks, natural disasters, and power outages. While confidentiality protects against unauthorized access and integrity ensures data accuracy and trustworthiness, availability ensures that legitimate users can access resources when needed.*
</details>

### Question 24
What is the purpose of a port number in TCP/IP networking?
- A) To identify the physical port on a network device
- B) To specify the sending and receiving application or service
- C) To determine the priority of the data packet
- D) To indicate the size of the data being transmitted

<details>
<summary>Show answer</summary>

**Answer: B) To specify the sending and receiving application or service**

*Explanation: The purpose of a port number in TCP/IP networking is to specify the particular application or service involved in the communication. While IP addresses identify the host devices, port numbers identify specific processes or services running on those hosts. This allows multiple network applications to operate simultaneously on the same device. Port numbers are 16-bit values (ranging from 0 to 65535) that serve as endpoints for communication. For example, web servers typically listen on port 80 for HTTP traffic and port 443 for HTTPS traffic. The combination of an IP address and a port number forms a socket, which uniquely identifies a specific endpoint for communication.*
</details>

### Question 25
What is a collision domain in Ethernet networks?
- A) A group of devices that receive all broadcasts sent on the network
- B) A segment where packets from different sources cannot be transmitted simultaneously without causing errors
- C) A logical division of a network created by routers
- D) A physical area where wireless signals interfere with each other

<details>
<summary>Show answer</summary>

**Answer: B) A segment where packets from different sources cannot be transmitted simultaneously without causing errors**

*Explanation: A collision domain is a network segment where data packets from different devices can collide if transmitted simultaneously, causing errors that require retransmission. In traditional Ethernet networks using CSMA/CD, devices must take turns transmitting on the shared medium to avoid collisions. Hubs create a single collision domain for all connected devices, meaning only one device can transmit at a time. Switches improve network efficiency by creating separate collision domains for each port, allowing multiple simultaneous transmissions. This is different from a broadcast domain (option A), which is a group of devices that receive all broadcasts and is typically separated by routers rather than switches.*
</details>

### Question 26
Which of the following is NOT a characteristic of IPv6?
- A) 128-bit addressing
- B) Simplified header format
- C) Network Address Translation requirement
- D) Built-in support for authentication and privacy

<details>
<summary>Show answer</summary>

**Answer: C) Network Address Translation requirement**

*Explanation: Network Address Translation (NAT) requirement is not a characteristic of IPv6. In fact, one of the benefits of IPv6 is that it eliminates the need for NAT due to its vast address space. NAT was developed primarily to address IPv4 address exhaustion, but with IPv6's 128-bit addressing providing approximately 3.4 × 10^38 unique addresses, every device can have a globally unique address without address conservation techniques like NAT. The other options are actual IPv6 characteristics: it uses 128-bit addressing (vastly expanding the address space), features a simplified header format (improving processing efficiency), and includes built-in support for authentication and privacy (through the IPsec protocol).*
</details>

### Question 27
What is the main purpose of the RSA algorithm in cryptography?
- A) Generating random numbers for encryption keys
- B) Compressing data before encryption
- C) Public key encryption and digital signatures
- D) Accelerating symmetric encryption operations

<details>
<summary>Show answer</summary>

**Answer: C) Public key encryption and digital signatures**

*Explanation: The main purpose of the RSA algorithm in cryptography is to provide public key (asymmetric) encryption and digital signature capabilities. Named after its inventors (Rivest, Shamir, and Adleman), RSA uses a pair of mathematically related keys—a public key that can be freely shared for encryption and a private key kept secret for decryption. This allows secure communication without prior key exchange and enables digital signatures for authentication and non-repudiation. RSA's security is based on the computational difficulty of factoring the product of two large prime numbers. While significantly slower than symmetric algorithms, RSA is often used to securely exchange symmetric keys or for signing documents rather than bulk data encryption.*
</details>

### Question 28
What type of network topology uses a single shared connection line connecting all nodes?
- A) Star topology
- B) Ring topology
- C) Bus topology
- D) Mesh topology

<details>
<summary>Show answer</summary>

**Answer: C) Bus topology**

*Explanation: A bus topology uses a single shared communication line (backbone or trunk) that connects all network nodes. In this arrangement, all devices connect directly to this central cable, and data transmitted by any device travels along the shared medium and is received by all devices. Each device checks whether the data is intended for itself. Bus topologies were common in early Ethernet networks (10BASE2 and 10BASE5). While relatively easy to install for small networks and using less cable than other topologies, bus networks are prone to performance issues under heavy traffic and can be vulnerable to cable failures, as a break in the main cable can disable the entire network.*
</details>

### Question 29
Which protocol operates at the lowest layer of the TCP/IP model?
- A) HTTP
- B) TCP
- C) IP
- D) Ethernet

<details>
<summary>Show answer</summary>

**Answer: D) Ethernet**

*Explanation: Ethernet operates at the lowest layer of the TCP/IP model, which is the Network Access layer (corresponding to the Data Link and Physical layers in the OSI model). Ethernet defines standards for physical cabling, signaling, and frame formats for local area networks. It handles hardware addressing (MAC), media access control, and physical transmission of data. HTTP operates at the Application layer (highest layer), TCP at the Transport layer, and IP at the Internet layer. In the TCP/IP protocol stack, these protocols are arranged hierarchically with Ethernet at the bottom, followed by IP, then TCP, and finally HTTP at the top.*
</details>

### Question 30
What is the primary function of a hub in a computer network?
- A) To filter traffic based on MAC addresses
- B) To regenerate and retransmit signals to all connected ports
- C) To route packets between different networks
- D) To assign IP addresses to network devices

<details>
<summary>Show answer</summary>

**Answer: B) To regenerate and retransmit signals to all connected ports**

*Explanation: The primary function of a hub in a computer network is to regenerate and retransmit incoming signals to all connected ports (except the originating port). Hubs operate at the Physical layer of the OSI model and act as simple multiport repeaters. When a hub receives data on one port, it duplicates that data and sends it out all other ports without any filtering or processing of the data. This creates a single collision domain where only one device can transmit at a time. Hubs have largely been replaced by switches, which can filter traffic based on MAC addresses (option A). Routing packets between networks (option C) is a function of routers, and assigning IP addresses (option D) is typically handled by DHCP servers.*
</details>

### Question 31
What is the purpose of the ICMP protocol in networking?
- A) To establish reliable connections between hosts
- B) To assign IP addresses dynamically
- C) To report errors and provide network diagnostics
- D) To translate domain names to IP addresses

<details>
<summary>Show answer</summary>

**Answer: C) To report errors and provide network diagnostics**

*Explanation: The Internet Control Message Protocol (ICMP) serves primarily to report errors and provide network diagnostics. It's used by network devices to communicate error conditions and operational information about network health and connectivity. Common ICMP applications include the "ping" utility (which uses ICMP Echo Request and Echo Reply messages to test if a host is reachable) and "traceroute" (which uses ICMP Time Exceeded messages to discover network paths). When routers encounter problems delivering packets, they often send ICMP messages to notify the sender about issues like "destination unreachable" or "time exceeded." ICMP operates at the Network layer alongside IP but isn't used for regular data transport.*
</details>

### Question 32
Which statement best describes how switches learn MAC addresses?
- A) They are manually configured by network administrators
- B) They receive periodic updates from the DHCP server
- C) They examine the source address of incoming frames
- D) They query other switches on the network

<details>
<summary>Show answer</summary>

**Answer: C) They examine the source address of incoming frames**

*Explanation: Switches build and maintain their MAC address tables by examining the source MAC address of each incoming frame. When a frame arrives at a switch port, the switch records the source MAC address and associates it with the port on which the frame was received. This learning process happens dynamically without administrator intervention. If the destination MAC address of an incoming frame is already in the table, the switch forwards the frame only to the specific port where that destination device is connected. If the destination is unknown, the switch floods the frame to all ports except the one it arrived on. This dynamic learning process allows switches to efficiently forward traffic only where needed, reducing unnecessary network traffic.*
</details>

### Question 33
What distinguishes TCP from UDP?
- A) TCP operates at the Network layer while UDP operates at the Transport layer
- B) TCP uses IP addresses while UDP uses MAC addresses
- C) TCP provides reliable, connection-oriented delivery while UDP provides best-effort delivery
- D) TCP is used exclusively for web browsing while UDP is used for email

<details>
<summary>Show answer</summary>

**Answer: C) TCP provides reliable, connection-oriented delivery while UDP provides best-effort delivery**

*Explanation: The key distinction between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) is that TCP provides reliable, connection-oriented delivery while UDP provides unreliable, connectionless "best-effort" delivery. TCP establishes a connection before transmitting data, ensures packets arrive in order, implements error checking and recovery through acknowledgments and retransmissions, and includes flow control mechanisms. UDP, in contrast, simply sends packets without establishing a connection, provides no guarantee of delivery or ordering, and performs only basic error checking without recovery mechanisms. Both protocols operate at the Transport layer (not Network layer) and use IP addresses rather than MAC addresses for addressing. They're both used for various applications based on requirements for reliability versus speed.*
</details>

### Question 34
What is the significance of port 443 in networking?
- A) It's used for FTP file transfers
- B) It's used for secure web browsing (HTTPS)
- C) It's used for remote terminal access (SSH)
- D) It's used for email transmission (SMTP)

<details>
<summary>Show answer</summary>

**Answer: B) It's used for secure web browsing (HTTPS)**

*Explanation: Port 443 is the standard port used for HTTPS (Hypertext Transfer Protocol Secure) traffic, which is HTTP traffic encrypted using SSL/TLS protocols. This port is significant because it enables secure web browsing, allowing for encrypted communication between web browsers and servers. When a URL begins with "https://", the browser connects to the server on port 443 by default. The encryption provided by HTTPS helps protect sensitive information such as login credentials, payment details, and personal information from being intercepted by attackers. Other standard ports include 21 for FTP, 22 for SSH, 25 for SMTP, and 80 for regular HTTP traffic.*
</details>

### Question 35
What type of attack involves sending malformed packets that exceed buffer capacity?
- A) Phishing attack
- B) Man-in-the-middle attack
- C) Buffer overflow attack
- D) SQL injection attack

<details>
<summary>Show answer</summary>

**Answer: C) Buffer overflow attack**

*Explanation: A buffer overflow attack involves sending malformed input data that exceeds the allocated buffer space in a program's memory. When a program doesn't properly validate input size before copying it to a buffer of fixed length, the excess data can overflow into adjacent memory locations. Attackers can exploit this vulnerability by carefully crafting the overflow data to include malicious code or modify program execution flow, potentially allowing them to execute arbitrary commands or gain unauthorized access to the system. Buffer overflow vulnerabilities have historically been one of the most common types of security flaws in software, particularly in programs written in languages like C and C++ that don't automatically perform bounds checking.*
</details>

### Question 36
Which term describes the maximum rate at which data can be transmitted over a network?
- A) Bandwidth
- B) Throughput
- C) Latency
- D) Jitter

<details>
<summary>Show answer</summary>

**Answer: A) Bandwidth**

*Explanation: Bandwidth refers to the maximum theoretical rate at which data can be transmitted over a network connection, measured in bits per second (bps) or its multiples (Kbps, Mbps, Gbps). It represents the capacity of the communication channel. Throughput measures the actual rate of successful data transfer over a period of time, which is often lower than bandwidth due to various overhead and limitations. Latency is the delay between sending and receiving data (measured in milliseconds), while jitter refers to the variation in latency over time. Bandwidth can be thought of as the width of a pipe—it determines the maximum volume that can flow through, but doesn't indicate how quickly the data actually travels from end to end.*
</details>

### Question 37
What is a major disadvantage of a bus topology in computer networks?
- A) It requires more cabling than other topologies
- B) A single point of failure can disable the entire network
- C) It's limited to only a few devices
- D) It's the most expensive topology to implement

<details>
<summary>Show answer</summary>

**Answer: B) A single point of failure can disable the entire network**

*Explanation: A major disadvantage of a bus topology is that it creates a single point of failure—a break anywhere in the main cable can disable the entire network. Since all devices connect to a single communication line, damage to this central cable or a problem with any connection can disrupt all network communications. This vulnerability makes bus networks less reliable than other topologies like star or mesh. Bus topologies actually use less cabling than other topologies (not more), can support numerous devices (though performance degrades with too many), and are typically less expensive to implement due to the minimal cabling requirements. Their simplicity and low cost must be weighed against the reliability concerns.*
</details>

### Question 38
What is the purpose of a Wireless Access Point (WAP) in a network?
- A) To assign IP addresses to wireless clients
- B) To connect wireless devices to a wired network
- C) To establish VPN connections for remote users
- D) To filter malicious traffic from entering the network

<details>
<summary>Show answer</summary>

**Answer: B) To connect wireless devices to a wired network**

*Explanation: The primary purpose of a Wireless Access Point (WAP) is to connect wireless devices to a wired network infrastructure. It acts as a bridge between wireless clients (laptops, smartphones, tablets, etc.) and the wired network, allowing these devices to communicate with the wired network and with each other. A WAP contains a radio transmitter/receiver and antenna for wireless communication, along with a wired network interface. While some access points may include additional features, their core function is providing this wireless-to-wired connectivity. IP address assignment is typically handled by DHCP servers (not the WAP itself), VPN connections are managed by VPN gateways, and traffic filtering is primarily a function of firewalls.*
</details>

### Question 39
What is the main purpose of DHCP in a network?
- A) To translate domain names to IP addresses
- B) To automatically assign IP addresses to network devices
- C) To secure communication between network devices
- D) To route traffic between different networks

<details>
<summary>Show answer</summary>

**Answer: B) To automatically assign IP addresses to network devices**

*Explanation: The main purpose of the Dynamic Host Configuration Protocol (DHCP) is to automatically assign IP addresses and other network configuration information to devices on a network. Without DHCP, network administrators would need to manually configure IP addresses for each device, which would be time-consuming and error-prone in large networks. DHCP simplifies network administration by automatically providing clients with IP addresses, subnet masks, default gateway addresses, DNS server addresses, and other configuration parameters. This automation reduces configuration errors, prevents IP address conflicts, and allows devices to easily join or leave the network without manual reconfiguration.*
</details>

### Question 40
What security vulnerability is being exploited when an attacker enters "%s%s%s%s%s%s" in an input field?
- A) SQL injection
- B) Buffer overflow
- C) Cross-site scripting
- D) Format string attack

<details>
<summary>Show answer</summary>

**Answer: D) Format string attack**

*Explanation: When an attacker enters "%s%s%s%s%s%s" in an input field, they are attempting a format string attack. This type of attack exploits vulnerabilities in how a program handles format string specifiers (like %s, %d, %x) in user-supplied input. In vulnerable programs, particularly those written in C/C++, these format specifiers can be interpreted as commands rather than literal text when passed to formatting functions like printf() without proper validation. The %s specifier tells the function to read and print a string from the memory address in the corresponding argument. When there are no corresponding arguments (as in this attack), the function will read from whatever memory locations happen to be on the stack, potentially revealing sensitive information, causing crashes, or even allowing arbitrary code execution. This differs from buffer overflows, SQL injection, and cross-site scripting, which exploit different vulnerabilities.*
</details>

### Question 41
What is the role of the Presentation layer in the OSI model?
- A) Establishing and terminating connections between applications
- B) Data formatting, encryption, and compression
- C) Routing and forwarding data packets
- D) Providing reliable data transfer services

<details>
<summary>Show answer</summary>

**Answer: B) Data formatting, encryption, and compression**

*Explanation: The Presentation layer (Layer 6) in the OSI model is responsible for data formatting, encryption/decryption, and compression/decompression. It ensures that data sent from the Application layer of one system can be properly interpreted by the Application layer of another system, regardless of their internal data representations. This layer handles tasks such as character code translation (e.g., ASCII to EBCDIC), data format conversion, encryption for privacy, and data compression to reduce size. By managing these presentation concerns, this layer serves as a translator between applications and the network, ensuring that data is presented in a usable form to the receiving application regardless of differences in hardware or operating systems.*
</details>

### Question 42
What component of a network interface card (NIC) is responsible for the physical address?
- A) Transceiver
- B) Interface connector
- C) MAC address
- D) Network driver

<details>
<summary>Show answer</summary>

**Answer: C) MAC address**

*Explanation: The Media Access Control (MAC) address is the component of a network interface card (NIC) that serves as its physical address. A MAC address is a globally unique 48-bit (6-byte) identifier assigned to the NIC by the manufacturer and permanently stored in the hardware. This address functions as the device's physical address at the Data Link layer, identifying the specific network interface in local network communications. MAC addresses are written as six pairs of hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E). The transceiver handles signal transmission and reception, the interface connector provides the physical connection to the network medium, and the network driver is software that allows the operating system to communicate with the NIC.*
</details>

### Question 43
Which of the following is NOT a countermeasure for SQL injection attacks?
- A) Input validation and sanitization
- B) Using prepared statements with parameterized queries
- C) Implementing stronger password policies
- D) Limiting database permissions for applications

<details>
<summary>Show answer</summary>

**Answer: C) Implementing stronger password policies**

*Explanation: Implementing stronger password policies is not a direct countermeasure for SQL injection attacks. While stronger passwords improve security against unauthorized access through authentication systems, they don't address the fundamental vulnerability that allows SQL injection to occur—the improper handling of user input in database queries. Effective SQL injection countermeasures include input validation and sanitization (checking and cleaning user inputs), using prepared statements with parameterized queries (separating SQL code from data), and limiting database permissions (minimizing damage potential if an injection occurs). These measures directly target the vulnerability by ensuring that user input cannot alter the structure of SQL statements or by reducing the potential impact of a successful attack.*
</details>

### Question 44
What is the main limitation of using the MD5 algorithm for password storage?
- A) It's too computationally intensive for modern systems
- B) It produces hash values that are too long for efficient storage
- C) It's vulnerable to collision attacks and has been cryptographically broken
- D) It can only process passwords of certain lengths

<details>
<summary>Show answer</summary>

**Answer: C) It's vulnerable to collision attacks and has been cryptographically broken**

*Explanation: The main limitation of using MD5 for password storage is that it has been cryptographically broken and is vulnerable to collision attacks. Researchers have demonstrated that it's possible to generate different inputs that produce the same MD5 hash value (collisions), undermining its security for verification purposes. Additionally, MD5 is considered cryptographically weak because it lacks salt by default and can be computed very quickly, making it vulnerable to rainbow table attacks and brute-force methods. Modern password storage should use more secure algorithms specifically designed for password hashing, such as bcrypt, Argon2, or PBKDF2, which incorporate salting and are deliberately computationally intensive to resist brute-force attacks. MD5 is actually very fast (not computationally intensive), produces relatively short 128-bit hashes, and can process inputs of any length.*
</details>

### Question 45
Which of the following best describes the difference between a virus and a worm in computer security?
- A) Viruses affect hardware while worms affect software
- B) Viruses require user action to spread while worms can self-propagate
- C) Viruses steal information while worms cause system crashes
- D) Viruses target personal computers while worms target servers

<details>
<summary>Show answer</summary>

**Answer: B) Viruses require user action to spread while worms can self-propagate**

*Explanation: The key difference between computer viruses and worms is their propagation method. Viruses require some form of user action to spread—they attach themselves to legitimate files or programs and execute when the host file is activated. Users typically spread viruses by sharing infected files or opening malicious email attachments. Worms, on the other hand, can self-propagate without user intervention by exploiting network vulnerabilities or using system features to replicate and spread to other computers automatically. This self-propagation capability allows worms to spread much more rapidly across networks. Both viruses and worms can affect various types of systems and can be designed to steal information, cause damage, or create other malicious effects.*
</details>