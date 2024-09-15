import csv
import re
class SearchSongEngine:

    def search_song():
        csv_file = 'Listado_temas_2023.csv' #Archivo CSV
        search_query = input("Enter the song you want to search: ") #Cancion a buscar
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                #Lista para almacenar datos de canciones
                tracks_data = list(reader)
                
                search_pattern = re.compile(re.escape(search_query), re.IGNORECASE) #expresión regular para la búsqueda
                
                matching_songs = [track for track in tracks_data if search_pattern.search(track.get('Track', ''))]      #Filtrar las canciones
                while True:
                    if matching_songs:
                        print(f"\nSongs matching the search query '{search_query}':")
                        for i, song in enumerate(matching_songs, start=1):
                            print(f"{i}. Song: {song.get('Track', 'N/A')}, Artist: {song.get('Artist', 'N/A')}, Likes: {song.get('Likes', 'N/A')}, Views: {song.get('Views', 'N/A')}, Comments: {song.get('Comments', 'N/A')}")
                        input("Press Enter to continue...")
                        break
                    else:
                        print(f"No songs found matching the search query '{search_query}'. Invalid or non-existent song.")
                        input("Press Enter to continue...")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Press Enter to continue...")
