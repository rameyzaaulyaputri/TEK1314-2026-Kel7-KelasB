## Skema Perancangan IP Address (IP Plan) - Kelompok 7

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
| **Router-R1** | Gateway | `192.168.7.1` | `255.255.255.0` | Internal Network `intnet-kel7` | MikroTik RouterOS CHR | Default Gateway |
| **WRT300N-AP** | Access Point (bridge L2) | `192.168.7.2` | `255.255.255.0` | Internal Network `intnet-kel7` + `intnet-wifi` (bridge) | MikroTik RouterOS CHR | Management / Bridge AP |
| **Target-Server** | Target Node (Korban) | `192.168.7.5` | `255.255.255.0` | Internal Network `intnet-kel7` | Ubuntu Server 24.04 LTS + PostgreSQL + Web App (Flask) | Port 80 (HTTP), Port 5432 (PostgreSQL), Port 22 (SSH) |
| **Attacker-Laptop** | Attacker Node | `192.168.7.100` | `255.255.255.0` | Internal Network `intnet-wifi` | Kali Linux | N/A (Penetration Testing Tools) |
| **Monitoring-PC** | Monitoring Node | `192.168.7.200` | `255.255.255.0` | Internal Network `intnet-kel7` (Promiscuous Mode) | Security Onion | Promiscuous Mode / IDS / Network Monitoring |

---

### Catatan Perubahan dari Rancangan Awal (Minggu ke-4)

- **Target Node** semula direncanakan Metasploitable 2 / DVWA (MySQL), direvisi menjadi **Ubuntu Server 24.04 LTS dengan PostgreSQL** agar lebih akurat merepresentasikan tech stack backend asli proyek IoT MUSH (lihat `docs/presentation-minggu9/tech_stack_declaration.md`).
- **WRT300N-AP** diimplementasikan sebagai MikroTik CHR kedua yang menjalankan fungsi bridge Layer 2 (bukan access point fisik/wireless), karena CHR tidak mendukung interface wireless. Segmen `intnet-wifi` merepresentasikan jalur "wireless" Attacker secara logis.
- Penempatan Monitoring Node tidak lagi melalui switch mirror/SPAN port fisik, melainkan memanfaatkan sifat Internal Network VirtualBox yang bekerja sebagai satu segmen L2 bersama, dikombinasikan dengan **Promiscuous Mode = Allow All** pada adapter Security Onion yang terhubung ke `intnet-kel7`.
