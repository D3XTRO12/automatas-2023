import csv
from collections import defaultdict

class TopArtistViews:
    @staticmethod
    def list_top_artists_by_views():
        csv_file = 'Listado_temas_2023.csv'

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                artist_views = defaultdict(float)

                for song in reader:
                    artist = song.get('Artist', 'Unknown')
                    views_str = song.get('Views', '0')  #Obtiene el valor de 'Views', o usa '0' si es una cadena vacía
                    views = float(views_str) if views_str else 0.0  #Convierte a float si no está vacío, de lo contrario, usa 0.0
                    artist_views[artist] += views

                sorted_artists = sorted(artist_views.items(), key=lambda x: x[1], reverse=True)

                print("\nTop 10 artists by total views:")
                for i, (artist, views) in enumerate(sorted_artists[:10], start=1):
                    print(f"{i}. Artist: {artist}, Total Views: {views}")
                input("Press Enter to continue...")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Press Enter to continue...")
