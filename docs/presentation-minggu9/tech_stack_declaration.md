## Deklarasi Tech Stack & Replikasi — Kelompok 7

Dokumen ini memetakan teknologi backend pada Proyek IoT asli **MUSH (Made Up Slowly Here)** ke Target Node replika yang digunakan dalam simulasi SOC Minggu ke-9 s.d. Minggu ke-15, sesuai Bagian III Panduan PBL Pertemuan ke-9.

> **Prinsip:** Target Node di lab BUKAN sistem produksi MUSH. Seluruh data bersifat dummy/sintetis. Tidak ada scanning atau eksploitasi yang menyentuh infrastruktur asli Pagi Farm.

---

### Tabel Pemetaan Tech Stack

| Komponen | Pada Proyek IoT Asli (MUSH) | Direplikasi sebagai (Target Node) | Catatan Kesesuaian |
| :--- | :--- | :--- | :--- |
| **Sistem Operasi backend** | Linux (VPS Cloud) | **Ubuntu 8.04** (Metasploitable 2) | Sama-sama keluarga Linux. Versi tidak identik, tetapi perilaku layanan HTTP/MySQL/SSH di atasnya representatif untuk tujuan simulasi serangan. |
| **Database/penyimpanan data** | **PostgreSQL** (TCP 5432) | **MySQL** (port 3306, bawaan Metasploitable 2) | **Simplifikasi disengaja.** Engine berbeda, tetapi kelas kerentanan yang disasar (SQL Injection, ekstraksi data, kredensial lemah) berlaku umum pada RDBMS relasional, bukan spesifik-engine. Teknik dan mitigasi yang dipelajari tetap relevan untuk PostgreSQL asli. |
| **Protokol komunikasi sensor** | **HTTP REST** (`POST /api/readings`, `GET /api/drums`, `GET /api/latest`) | **HTTP** (port 80, DVWA) | Sesuai — proyek asli memang memakai HTTP REST (bukan MQTT), sehingga DVWA berbasis HTTP representatif. |
| **Dashboard/monitoring** | Web dashboard (HTTPS, responsive, polling 10 detik) | **DVWA** (aplikasi web PHP) | **Simplifikasi disengaja.** Replika memakai HTTP (bukan HTTPS) agar traffic dapat diamati plain-text oleh Monitoring Node (Security Onion) tanpa perlu dekripsi TLS. |

---

### Justifikasi Simplifikasi

1. **PostgreSQL → MySQL.** Dipilih karena Metasploitable 2 sudah menyediakan MySQL + DVWA secara bawaan, teruji, dan stabil untuk kebutuhan praktikum. Fokus simulasi adalah pola serangan (SQLi, brute-force, data exfiltration) dan pola deteksi di Security Onion, bukan perbedaan sintaks SQL antarengine.
2. **HTTPS → HTTP.** Dilakukan agar Blue Team dapat menganalisis isi request/response secara langsung di Security Onion (Zeek `http.log`), sesuai tujuan pembelajaran deteksi jaringan pada tahap ini.
3. **OS backend asli belum dikonfirmasi versinya**, sehingga dituliskan sebagai "Linux (VPS Cloud)" tanpa mengarang versi spesifik.

### Relevansi untuk Mitra (Pagi Farm)

Karena pola serangan (SQL Injection, brute-force, exfiltrasi data) dan kontrol mitigasinya (parameterized query, rate-limiting, firewall) berlaku lintas-platform, temuan dari simulasi ini tetap relevan untuk diterapkan pada backend MUSH yang sesungguhnya, dengan penyesuaian sintaks pada implementasi PostgreSQL dan HTTPS asli.
