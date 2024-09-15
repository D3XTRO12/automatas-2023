import csv
import re

class RatioMetricsEngine:
        @staticmethod
        def list_for_ratio():
            csv_file = 'Listado_temas_2023.csv'
            try:
                with open(csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)           #Lector CSV
                    tracks_data = list(reader)              #Lista para almacenar los datos de las canciones
                    tracks_data = [track for track in tracks_data if track['Likes'] and track['Views']]
                    # Calcular el ratio de likes por vistas
                    for track in tracks_data:
                        likes = float(track['Likes'])
                        views = float(track['Views'])
                        ratio = likes / views if views != 0 else 0
                        track['Ratio'] = ratio
                    sorted_tracks = sorted(
                        tracks_data,
                        key=lambda x: x['Ratio'],
                        reverse=True
                    )
                    print("\nTop 5 songs by likes/views ratio:")
                    for i, track in enumerate(sorted_tracks[:5], start=1):
                        print(f"{i}. Song: {track.get('Track', 'N/A')}, Likes/Views Ratio: {track['Ratio']:.2%}")
                    input("Press Enter to continue...")

            except FileNotFoundError:
                print(f"El archivo {csv_file} no fue encontrado.")
                input("Press Enter to continue...")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
                input("Press Enter to continue...") 