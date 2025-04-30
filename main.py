import sqlite3
            
# Membuat koneksi ke database
connection = sqlite3.connect('movie.db')

# Membuat cursor untuk menjalankan SQL-query
cursor = connection.cursor()

# Simbol * menunjukkan semua
cursor.execute("SELECT * FROM movies")

# Atau kita bisa memilih hanya bidang yang kita butuhkan (kita akan membahasnya lebih detail di pelajaran berikutnya)
cursor.execute("SELECT title FROM movies")

#tugas pertama liat popularitas
cursor.execute("""SELECT title, budget, popularity
FROM movies
ORDER BY popularity DESC
LIMIT 1""")

#tugas kedua liat budget termahal di tahun 2009
cursor.execute("""SELECT title, budget
FROM movies
WHERE release_date LIKE '2009%'
ORDER BY budget DESC
LIMIT 1""")

#tugas ketiga liat slogan
cursor.execute("""SELECT title
FROM movies
WHERE tagline like 'The battle within.%'""")

#tugas keempat liat vote
cursor.execute("""SELECT title, vote_count
FROM movies
WHERE release_date < '1980-01-01' AND vote_average > 8
ORDER BY vote_count DESC
LIMIT 1""")

# Menggunakan metode fetchall() untuk mendapatkan hasil
result = cursor.fetchall()

# Menampilkan hasil
for row in result:
    print(row)

# Menutup koneksi ke database setelah digunakan
connection.close()