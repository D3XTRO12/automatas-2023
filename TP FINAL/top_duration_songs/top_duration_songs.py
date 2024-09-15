import csv

class SongDurationTop:
    
    @staticmethod
    def list_top_songs_by_duration():
        csv_file = 'Listado_temas_2023.csv'

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                songs_data = list(reader)
                
                songs_data = [song for song in songs_data if song['Duration_ms']]   #Filtra las filas con valores no vacíos en 'Duration_ms'
                
                printed_songs = set()                                    #Almacena las canciones ya impresas
                sorted_songs = sorted(
                    songs_data,
                     key=lambda x: float(x['Duration_ms']),                #Ordenar la lista de canciones por duración(milisegundos)
                     reverse=True
                )

                print("\nTop 10 songs by duration:")
                for i, song in enumerate(sorted_songs, start=1):
                    duration_seconds = float(song['Duration_ms']) / 1000
                    minutes, seconds = divmod(duration_seconds, 60)
                    duration_formatted = f"{int(minutes):02d}:{int(seconds):02d}"

                    
                    if song['Track'] not in printed_songs:                              
                        print(f"{i}. Song: {song.get('Track', 'N/A')}, Duration: {duration_formatted}")         #Verifica si la canción ya ha sido impresa
                        printed_songs.add(song['Track'])

                        if len(printed_songs) == 10:
                            input("Press Enter to continue...")
                            break                          #Si ya se imprimieron 10 canciones, se detiene el ciclo

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Press Enter to continue...")
