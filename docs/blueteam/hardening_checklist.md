# Hardening Checklist — Kelompok 7 (Target Node: Metasploitable 2)

Status: **Selesai** / **Sebagian** / **Belum**
Bukti lengkap (screenshot/output) disimpan di `docs/blueteam/evidence/`.

---

## Kategori A — Access & Authentication

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| A1 | Nonaktifkan login root langsung via SSH (`PermitRootLogin no`) | Belum | `evidence/a1-sshd-config-before.png`, `evidence/a1-sshd-config-after.png`, `evidence/a1-login-root-rejected.png` |
| A2 | Ganti password default akun `msfadmin` | Belum | `evidence/a2-login-old-fail.png`, `evidence/a2-login-new-success.png` |
| A3 | Rate-limit percobaan login (fail2ban) — *kendala: repo Ubuntu 8.04 EOL, sedang dicari alternatif* | Belum | — |

## Kategori B — Service & Attack Surface

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| B1 | Nonaktifkan service tidak terpakai (Telnet, dll.) | Belum | `evidence/b1-netstat-before.png`, `evidence/b1-netstat-after.png` |
| B2 | Firewall whitelist port 22/80/3306 dari IP Attacker saja | Belum | `evidence/b2-nmap-before.txt`, `evidence/b2-nmap-after.txt` |
| B3 | Ganti kredensial default MySQL root | Belum | `evidence/b3-mysql-login-old-fail.png`, `evidence/b3-mysql-login-new-success.png` |

## Kategori C — Data & Application

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| C1 | Naikkan DVWA Security Level low → medium, dokumentasikan perbedaan filtering input | Belum | `evidence/c1-dvwa-source-low.png`, `evidence/c1-dvwa-source-medium.png` |
| C2 | Logging aktivitas mencurigakan aktif di Security Onion (Zeek http.log) | Belum | `evidence/c2-zeek-http-log.png` |
| C3 | Least-privilege user database untuk aplikasi (bukan root) | Belum | `evidence/c3-db-config-before.png`, `evidence/c3-db-config-after.png` |

---

## Ringkasan

- Total kontrol direncanakan: **9** (memenuhi minimum 8, tersebar di 3 kategori ≥2 masing-masing)
- Status saat Minggu ke-9: seluruh kontrol dalam tahap **perencanaan**, eksekusi dimulai setelah checkpoint sesuai Roadmap Bagian VI (Minggu ke-10/11)
- Verifikasi akhir: `nmap -sV 192.168.7.5` before vs after, dilampirkan sebagai `evidence/nmap-diff.txt`
