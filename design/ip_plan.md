# Skema Perancangan IP Address (IP Plan) - Kelompok 7

Dokumen ini berisi alokasi alamat IP dan spesifikasi node untuk simulasi perancangan arsitektur jaringan proyek PBL Keamanan Siber.

* **Kelompok:** 7
* **Kelas:** B 
* **Subnet Network:** `192.168.7.0/24`
* **Subnet Mask:** `255.255.255.0`
* **Broadcast Address:** `192.168.7.255`

---

## Tabel Skema IP (IP Address Table)

| Hostname | Role / Node | IP Address | Subnet Mask | Interface / Koneksi | OS Direncanakan | Service / Port Target |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Router-R1** | Gateway | `192.168.7.1` | `255.255.255.0` | GigabitEthernet0/0 | Cisco IOS / Router OS | Default Gateway |
| **WRT300N-AP** | Access Point | `192.168.7.2` | `255.255.255.0` | Wireless / LAN | AP Firmware | Management / Wireless AP |
| **Target-Server** | Target Node (Korban) | `192.168.7.5` | `255.255.255.0` | Ethernet (Switch) | Metasploitable 2 / DVWA (Ubuntu Server) | Port 80 (HTTP), Port 3306 (MySQL), Port 22 (SSH) |
| **Attacker-Laptop** | Attacker Node | `192.168.7.100` | `255.255.255.0` | Wireless (Access Point) | Kali Linux | N/A (Penetration Testing Tools) |
| **Monitoring-PC** | Monitoring Node | `192.168.7.200` | `255.255.255.0` | Ethernet (Switch Mirror Port) | Security Onion | Promiscuous Mode / IDS / Network Monitoring |
