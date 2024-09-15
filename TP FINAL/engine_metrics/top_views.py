import csv

class ViewsMetricsEngine:
    @staticmethod
    def list_top_songs_by_views():
        csv_file = 'Listado_temas_2023.csv'
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                songs_data = list(reader)
                songs_data = [song for song in songs_data if song['Views']]

                unique_songs = {}

                for song in songs_data:
                    track_name = song['Track']
                    current_views = float(song['Views'])

                    if track_name not in unique_songs or current_views > float(unique_songs[track_name]['Views']):
                        unique_songs[track_name] = song.copy()
                sorted_songs = sorted(
                    unique_songs.values(),
                    key=lambda x: float(x['Views']),
                    reverse=True
                )
                print("\nTop 5 songs by views:")
                for i, song in enumerate(sorted_songs[:5], start=1):
                    print(f"{i}. Song: {song.get('Track', 'N/A')}, Views: {song['Views']}")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")