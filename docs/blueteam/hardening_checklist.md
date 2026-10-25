# Hardening Checklist — Kelompok 7 (Target Node: Ubuntu Server 24.04 LTS + PostgreSQL + Web App Custom)

Status: **Selesai** / **Sebagian** / **Belum**
Bukti lengkap (screenshot/output) disimpan di `docs/blueteam/evidence/`.

---

## Kategori A — Access & Authentication

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| A1 | Nonaktifkan login root langsung via SSH (`PermitRootLogin no`) + wajibkan key-based auth (`PasswordAuthentication no`, `ChallengeResponseAuthentication no`) | Selesai | `evidence/a1-sshd-config-before.png`, `evidence/a1-sshd-config-after.png`, `evidence/a1-ssh-key-login.png`, `evidence/a1-login-root-rejected.png` |
| A2 | Ganti password default akun admin VM | Selesai | `evidence/a2-login-old-success.png`, `evidence/a2-login-old-fail.png`, `evidence/a2-login-new-success.png` |
| A3 | Rate-limit percobaan login SSH (fail2ban) | Selesai | `evidence/a3-fail2ban-before.png`, `evidence/a3-fail2ban-config.png`, `evidence/a3-fail2ban-banned(kali).png`, `evidence/a3-fail2ban-banned(target).png` |

## Kategori B — Service & Attack Surface

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| B1 | Nonaktifkan service tidak terpakai, batasi Flask dev server agar tidak expose debug mode | Selesai | `evidence/b1-ss-before.png`, `evidence/b1-ss-after.png` |
| B2 | Firewall (ufw) whitelist port 22/80/5432 hanya dari IP Attacker/Monitoring | Sebagian | `evidence/b2-ufw-status-before.png`, `evidence/b2-ufw-status-after.png`, `evidence/b2-nmap-before.txt` |
| B3 | Ganti kredensial default PostgreSQL (`appuser`/`admin123`) | Selesai | `evidence/b3-pg-listen-before.png`, `evidence/b3-pg-roles-before.png`, `evidence/b3-pg-login-old-success.png`, `evidence/b3-pg-login-old-fail.png`, `evidence/b3-pg-login-new-success.png` |

## Kategori C — Data & Application

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| C1 | Perbaiki query login agar parameterized (hilangkan celah SQL Injection) | Sebagian | `evidence/c1-code-before.png`, `evidence/c1-code-before.py`, `evidence/c1-code-after.py`, `evidence/c1-sqli-blocked.png` |
| C2 | Logging aktivitas mencurigakan aktif di Security Onion (Zeek http.log) | Belum | — |
| C3 | Least-privilege user database untuk aplikasi (batasi privilege `appuser`, jangan jadi owner database setelah skema final) | Selesai | `evidence/c3-db-config-before.png`, `evidence/c3-db-config-after.png` |

---

## Ringkasan

| Kategori | Selesai | Sebagian | Belum | Total |
|---|---:|---:|---:|---:|
| A. Access & Authentication | 3 | 0 | 0 | 3 |
| B. Service & Attack Surface | 2 | 1 | 0 | 3 |
| C. Data & Application | 1 | 1 | 1 | 3 |
| **Total** | **6** | **2** | **1** | **9** |

### Catatan Revisi

Target Node semula direncanakan Metasploitable 2/DVWA (MySQL). Checklist ini direvisi menyesuaikan migrasi ke Ubuntu Server 24.04 LTS + PostgreSQL + aplikasi web custom (lihat `docs/presentation-minggu9/tech_stack_declaration.md`), sehingga detail kontrol B3 dan C1 disesuaikan dari konteks DVWA/MySQL menjadi PostgreSQL/Flask.
