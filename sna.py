import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk membaca data dari file CSV
def read_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Fungsi untuk membuat dan menggambar grafik menggunakan Networkx dan Matplotlib
def draw_graph_from_csv(file_path):
    # Membaca data dari file CSV
    df = read_csv_data(file_path)

    # Membangun grafik menggunakan Networkx
    G = nx.from_pandas_edgelist(df, source='source', target='target')

    # Menentukan posisi simpul dalam gambar
    pos = nx.spring_layout(G)

    # Menggambar simpul dan sambungan
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Grafik dari File CSV")
    
# Menampilkan gambar grafik
    plt.show()

if __name__ == "__main__":
    csv_file_path = "setdata.csv"
    draw_graph_from_csv(csv_file_path)
