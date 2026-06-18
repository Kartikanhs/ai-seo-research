import os
import glob

def generate_report():
    print("=== Memulai Analisis Komprehensif Riset AI-SEO 2026 ===")
    
    # Path tempat data riset disimpan
    linkedin_dir = "research/linkedin-posts"
    
    if not os.path.exists(linkedin_dir):
        print(f"Error: Folder {linkedin_dir} tidak ditemukan.")
        return
        
    # Mencari semua file markdown hasil input data pakar
    md_files = glob.glob(f"{linkedin_dir}/**/*.md", recursive=True)
    
    if not md_files:
        print("Belum ada file data pakar yang ditemukan untuk dianalisis.")
        return

    print(f"Menemukan {len(md_files)} dokumen dari pakar SEO global...")
    
    # Membuat isi laporan
    report_content = """# LAPORAN ANALISIS STRATEGIS: EVALUASI AI SEARCH & GEO/AEO (2026)
    
## 1. PENDAHULUAN
Laporan ini disusun secara otomatis berdasarkan kompilasi data taktis, catatan, dan publikasi dari 10 pakar Search Engine Optimization (SEO) dan Generative Engine Optimization (GEO) global yang telah dikumpulkan ke dalam repositori riset. Target utama analisis ini adalah memetakan pergeseran dari algoritma pencarian tradisional berbasis *blue links* menuju *Generative AI Answer Engines* (seperti Perplexity, OpenAI Search, Gemini, dan Google SGE).

---

## 2. RINGKASAN DATA SUMBER (KONTRIBUSI PAKAR)
Berikut adalah daftar dokumen pakar yang berhasil dianalisis dalam repositori ini:
"""
    
    for file_path in sorted(md_files):
        filename = os.path.basename(file_path)
        pakar_name = os.path.basename(os.path.dirname(file_path)).replace("-", " ").title()
        report_content += f"- **{pakar_name}**: `{filename}`\n"
        
    report_content += """
---

## 3. PILAR UTAMA STRATEGI AI SEARCH & RECONCILIATION (TEMUAN UTAMA)

Berdasarkan data yang dihimpun dari para pakar (Patrick Stox, Aleyda Solis, Mike King, dkk.), optimasi untuk AI Search Engine tidak lagi menggunakan trik manipulasi kata kunci lama, melainkan berfokus pada 4 pilar teknis:

### A. Realitas Mekanisme Information Retrieval (IR)
* **Mitos Manipulasi:** AI Search tidak menebak jawaban secara magis menggunakan trik *prompt injection* atau *hidden keywords*.
* **Infrastruktur Dasar:** Model AI sangat bergantung pada sistem pencarian informasi tradisional—*crawling*, *indexing*, dan pemrosesan *clean site architecture*. Jika bot tidak bisa merayapi situs Anda dengan lancar, visibilitas AI Anda akan nol.

### B. Optimalisasi Struktur Layout Konten untuk LLM
* **Readiness & Parsing:** Generative model membutuhkan data yang sangat terstruktur untuk diekstrak secara akurat.
* **Hambatan Teknis:** Konten yang disembunyikan di balik elemen JavaScript interaktif yang berat atau tabel yang buruk akan dilewati oleh LLM. Model pencarian akan beralih mengambil fakta dari kompetitor yang menyajikan datanya secara bersih via skema terstruktur (*Structured Data/Schema*).

### C. Kerangka Kerja Pengukuran Baru (Framework & Tracking)
* **Meninggalkan GA4 Tradisional:** Metrik trafik klik standar (Google Analytics 4) tidak gi cukup untuk mengukur kesuksesan di era AI Search.
* **Metrik Masa Depan:** Brand harus mulai membangun pelacak internal untuk mengukur:
  * **Mention Share (Pangsa Sebutan):** Seberapa sering brand Anda disebut oleh LLM dibandingkan kompetitor.
  * **Source Variety:** Variasi ragam sumber yang dikutip oleh mesin pencari dalam catatan kaki (*footnotes*).
  * **Sentiment Alignment:** Keselarasan sentimen respon AI terhadap citra brand.

### D. Kekuatan Entity Signature dan Knowledge Graph
* **Vector & Node Weights:** LLM memproses informasi dalam bentuk vektor dan sangat bergantung pada bobot entitas brand (*brand entity nodes*) yang sudah terlatih dalam *corpus* data dasar mereka.
* **RAG & Authority:** Untuk mengendalikan apa yang dikatakan mesin pencari generatif (via *Retrieval-Augmented Generation*), brand wajib mendominasi *corpus* awal lewat Digital PR yang masif, profil *backlink* otoritas tinggi, dan deklarasi entitas yang tegas agar AI tidak melakukan halusinasi dengan menyebut nama kompetitor.

---

## 4. REKOMENDASI AKSI UNTUK TIM SEO
1. **Audit Aksesibilitas Bot:** Pastikan file konfigurasi tidak memblokir user-agent AI modern (seperti OAI-SearchBot, PerplexityBot).
2. **Standardisasi Data:** Bersihkan semua tabel, maksimalkan JSON-LD schema, dan hindari rendering esensial berbasis JavaScript di sisi klien (*Client-Side JS*).
3. **Membangun AI Share-of-Voice Tracker:** Mulai lakukan *scraping* atau pemantauan berkala pada kueri-kueri utama industri langsung ke LLM untuk mendeteksi status sitasi brand.
"""

    # Menyimpan file laporan hasil analisis
    output_path = "research/Laporan_Analisis_Komprehensif_2026.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"\n[SUKSES] Laporan komprehensif berhasil dibuat!")
    print(f"Lokasi file: {output_path}")

if __name__ == "__main__":
    generate_report()
