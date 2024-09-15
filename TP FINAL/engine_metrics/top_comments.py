import csv

class CommentsMetricsEngine:
    @staticmethod
    def list_top_songs_by_comments():
        # Nombre del archivo CSV (ajusta según tu caso)
        csv_file = 'Listado_temas_2023.csv'

        try:
            # Abrir el archivo CSV en modo lectura con codificación utf-8
            with open(csv_file, 'r', encoding='utf-8') as file:
                # Crear un lector CSV
                reader = csv.DictReader(file)

                # Convertir el contenido del archivo a una lista de diccionarios
                songs_data = list(reader)

                # Filtrar las filas con valores no vacíos en 'Comments'
                songs_data = [song for song in songs_data if song['Comments']]

                # Crear un diccionario para almacenar las canciones únicas con sus métricas
                unique_songs = {}

                # Iterar sobre las canciones y actualizar el diccionario con las métricas máximas
                for song in songs_data:
                    track_name = song['Track']
                    current_comments = float(song['Comments'])

                    if track_name not in unique_songs or current_comments > float(unique_songs[track_name]['Comments']):
                        unique_songs[track_name] = song.copy()

                # Ordenar la lista de canciones por comentarios
                sorted_songs = sorted(
                    unique_songs.values(),
                    key=lambda x: float(x['Comments']),
                    reverse=True
                )

                # Imprimir las primeras 5 canciones
                print("\nTop 5 songs by comments:")
                for i, song in enumerate(sorted_songs[:5], start=1):
                    # Ajusta la clave según el nombre real de la columna en tu archivo CSV (en este caso, 'Track')
                    print(f"{i}. Song: {song.get('Track', 'N/A')}, Comments: {song['Comments']}")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")