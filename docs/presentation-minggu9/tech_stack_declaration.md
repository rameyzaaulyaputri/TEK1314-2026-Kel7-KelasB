## Deklarasi Tech Stack & Replikasi — Kelompok 7

Dokumen ini memetakan teknologi backend pada Proyek IoT asli **MUSH (Made Up Slowly Here)** ke Target Node replika yang digunakan dalam simulasi SOC Minggu ke-9 s.d. Minggu ke-15, sesuai Bagian III Panduan PBL Pertemuan ke-9.

> **Prinsip:** Target Node di lab BUKAN sistem produksi MUSH. Seluruh data bersifat dummy/sintetis. Tidak ada scanning atau eksploitasi yang menyentuh infrastruktur asli Pagi Farm.

---

### Tabel Pemetaan Tech Stack

| Komponen | Pada Proyek IoT Asli (MUSH) | Direplikasi sebagai (Target Node) | Catatan Kesesuaian |
| :--- | :--- | :--- | :--- |
| **Sistem Operasi backend** | Linux (VPS Cloud) | **Ubuntu Server 24.04 LTS** | Sama-sama Linux dan merupakan rilis LTS yang umum dipakai untuk deployment VPS, sehingga perilaku sistem (manajemen service via systemd, netplan, OpenSSH modern) representatif terhadap backend asli. |
| **Database/penyimpanan data** | **PostgreSQL** (TCP 5432) | **PostgreSQL** (TCP 5432) | **Sesuai penuh — tidak ada simplifikasi.** Engine, port, dan perilaku query identik dengan proyek asli. |
| **Protokol komunikasi sensor** | **HTTP REST** (`POST /api/readings`, `GET /api/drums`, `GET /api/latest`) | **HTTP REST** (Flask, endpoint `/api/readings`, port 80) | Sesuai — replika memakai pola REST API yang sama (endpoint tanpa otentikasi untuk pembacaan data sensor), merepresentasikan desain API asli MUSH. |
| **Dashboard/monitoring** | Web dashboard (HTTPS, responsive, polling 10 detik) | **Aplikasi web custom (Flask)** — dashboard batch fermentasi dengan tabel data sensor dan form catatan | **Simplifikasi disengaja (HTTP, bukan HTTPS).** Struktur halaman (data sensor per batch, catatan/notes) meniru fungsi dashboard asli; traffic sengaja dibiarkan HTTP agar dapat diamati plain-text oleh Monitoring Node (Security Onion) tanpa perlu dekripsi TLS. |

---

### Justifikasi Simplifikasi

1. **HTTPS → HTTP.** Satu-satunya simplifikasi yang tersisa setelah migrasi ke Ubuntu Server + PostgreSQL. Dilakukan agar Blue Team dapat menganalisis isi request/response secara langsung di Security Onion (Zeek `http.log`), sesuai tujuan pembelajaran deteksi jaringan pada tahap ini.
2. **Revisi dari rancangan awal:** pada draf sebelumnya Target Node sempat direncanakan menggunakan Metasploitable 2 (Ubuntu 8.04) dengan MySQL/DVWA sebagai simplifikasi cepat. Setelah dievaluasi, kelompok memutuskan membangun Target Node baru di atas Ubuntu Server 24.04 LTS dengan PostgreSQL asli dan aplikasi web custom (Flask) agar replikasi lebih akurat terhadap tech stack MUSH yang sesungguhnya, khususnya pada komponen database.
3. **Celah keamanan ditanam secara sengaja** pada aplikasi web custom (SQL Injection pada form login, Stored XSS pada form catatan batch, endpoint API tanpa autentikasi) untuk mendukung skenario serangan pada `docs/redteam/attack_plan.md`, merepresentasikan kerentanan yang relevan dengan pola implementasi REST API dan dashboard berbasis web pada umumnya.

### Relevansi untuk Mitra (Pagi Farm)

Karena database (PostgreSQL) dan protokol komunikasi (HTTP REST) pada replika ini **identik** dengan backend asli MUSH, temuan kerentanan (SQL Injection, kredensial lemah, endpoint tanpa autentikasi) dan kontrol mitigasinya (parameterized query, least-privilege database user, rate-limiting, firewall) sangat relevan untuk diterapkan langsung pada backend MUSH yang sesungguhnya, dengan penyesuaian minor pada implementasi HTTPS/TLS asli.
