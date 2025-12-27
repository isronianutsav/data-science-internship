# 📡 Chat Application Using Python🐍

This repository contains a Python implementation of **UDP-based message communication** using the built-in `socket` library.  
The project demonstrates how data can be transmitted between two systems using **IP addressing and port-based networking**.

---

## 📌 Project Overview

This project focuses on **network-level communication** using the **User Datagram Protocol (UDP)**.  
It enables one system to send messages and another system to receive them without establishing a persistent connection.

The implementation is suitable for:
- Networking fundamentals practice
- Computer Networks laboratory work
- Understanding low-level data transfer in Python

---

## ⚠️ Mandatory Network Condition

> ✅ **Both the sender and receiver must be connected to the same internet network**
> - Same Wi-Fi network **or**
> - Same Local Area Network (LAN)

> ❌ Communication will fail if systems are on different networks without port forwarding or tunneling.

---

## 🛠 Libraries Used

### 🔹 `socket`
The `socket` module is a **built-in Python library** used for network communication.

It provides:
- Creation of network sockets
- Support for IPv4 addressing (`AF_INET`)
- Implementation of UDP communication (`SOCK_DGRAM`)
- Functions for sending and receiving data packets
- Low-level access to networking protocols

This project uses the `socket` module to:
- Establish UDP endpoints
- Send encoded messages between systems
- Receive data packets over a defined port

No external libraries are required.

---

## ⚙️ Communication Details
- **Protocol:** UDP (User Datagram Protocol)
- **Addressing:** IPv4
- **Data Encoding:** ASCII
- **Buffer Size:** 1024 bytes(You can increase or decrease it)
- **Connection Type:** Connectionless

---

## 🔑 Execution Requirements
- Python 3.x installed on both systems
- Sender and receiver on the **same network**
- Correct IP address configuration
- Matching port numbers
- Firewall allowing UDP traffic

---

## ▶️ How to Run
1. Start the receiver program on the receiving system.
2. Run the sender program on the sending system.
3. Enter the message in the sender terminal to transmit data.

---

## 📚 Learning Outcomes
- Understanding UDP-based networking
- Practical exposure to socket programming
- Knowledge of IP and port-based communication
- Foundation for advanced networking concepts

---

## 🚀 Future Enhancements
- Separation of sender and receiver scripts
- Implementation of TCP-based communication
- Error handling and logging
- Message acknowledgment system
- Multi-client support

---

## 👤 Author
**isronianutsav**  
B.Tech Engineering Student  
Python | Networking | Systems Programming 🚀
