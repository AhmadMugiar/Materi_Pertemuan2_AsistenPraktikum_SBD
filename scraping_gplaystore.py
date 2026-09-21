from google_play_scraper import reviews, Sort
import pandas as pd

# ID aplikasi 
app_id = "ID_APLIKASI"  # Ganti dengan ID aplikasi yang ingin diambil reviewnya

print("Mulai scraping review Google Play...")

result, continuation_token = reviews(
    app_id,
    lang="id",
    country="id",
    sort=Sort.MOST_RELEVANT,
    count=5000,
    filter_score_with=None
)

print(f"Jumlah review berhasil diambil: {len(result)}")

# Membuat DataFrame
data = pd.DataFrame(result)

# Simpan ke CSV
output_path = "data/dataset_reviews_scraper_gplay.csv"
data.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Data berhasil disimpan ke: {output_path}")