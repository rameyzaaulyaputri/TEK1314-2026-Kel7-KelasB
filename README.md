# TEK1314-2026-Kel7-KelasB
- Galih Virgian          (J0404241029)
- Riris Mulyanti Yusup   (J0404241061)
- Nita Putri Azahra      (J0404241068)
- Rameyza Aulya Putri    (J0404241162)

## Deskripsi Skenario — Kelompok 7

Kelompok 7 mensimulasikan serangan siber terhadap aplikasi web yang terhubung dengan basis data, dengan Target Node berupa **Ubuntu Server 24.04 LTS yang menjalankan PostgreSQL dan aplikasi web custom (Flask)**, dirancang sebagai replika tech stack backend proyek IoT MUSH (lihat `docs/presentation-minggu9/tech_stack_declaration.md`). Red Team akan mendemonstrasikan eksploitasi celah keamanan berupa:
- SQL Injection dan Cross-Site Scripting (XSS) melalui port 80 (HTTP)
- Ekstraksi data sensitif dari database melalui port 5432 (PostgreSQL)
- Brute-force autentikasi melalui port 22 (SSH)

Seluruh aktivitas serangan akan dipantau oleh Monitoring Node (Security Onion) yang ditempatkan pada segmen jaringan `intnet-kel7` (192.168.7.0/24) dengan Promiscuous Mode aktif untuk menangkap seluruh lalu lintas jaringan.

> **Catatan:** Target Node semula direncanakan menggunakan Metasploitable 2/DVWA (MySQL) sebagai simplifikasi cepat. Rancangan direvisi menjadi Ubuntu Server + PostgreSQL + aplikasi web custom agar replikasi tech stack lebih akurat terhadap backend proyek IoT asli (PostgreSQL, bukan MySQL).
