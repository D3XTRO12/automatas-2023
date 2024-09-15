import csv
import re

class AddSong:

    __archive = "Listado_temas_2023.csv"
    @staticmethod
    def convert_to_milliseconds():
        while True:
            duration_input = input("Enter duration (hours:minutes:seconds): ")
            try:
                hours, minutes, seconds = map(int, duration_input.split(':'))
                total_seconds = (hours * 3600) + minutes * 60 + seconds
                duration_ms = total_seconds * 1000
                return duration_ms
            except ValueError:
                print("Invalid input. Please enter valid numbers for hours, minutes, and seconds.")
                

    @staticmethod
    def validate_input(prompt, regex_pattern):
        while True:
            user_input = input(prompt)
            if re.match(regex_pattern, user_input):
                return user_input
            else:
                print(f"Invalid input format. Please enter a valid value.")
    @staticmethod
    def get_last_index():
        try:
            with open(AddSong.__archive, "r") as file:
                reader = csv.DictReader(file)
                # Obtenemos el último índice
                last_index = max(int(row["Index"]) for row in reader)
                return last_index
        except FileNotFoundError:
            # Si el archivo no existe, asumimos que es el primer índice
            return 0
    @staticmethod
    def add_new_song():
        new_row = {}

        # Obtener el último índice y asignar el nuevo índice
        last_index = AddSong.get_last_index()
        new_row["Index"] = last_index + 1

        # Pedir datos por consola
        new_row["Artist"] = input("Enter Artist: ")

        # Validar y pedir Spotify URL hasta que sea válida
        spotify_prompt = "Enter Spotify URL (artist/track): "
        spotify_url_pattern = re.compile(r'^(https?://)?(open\.spotify\.com/)(artist|track)/[a-zA-Z0-9_-]+(\?si=[a-zA-Z0-9]+)?$')
        new_row["URL_spotify"] = AddSong.validate_input(spotify_prompt, spotify_url_pattern)

        new_row["Track"] = input("Enter Track: ")
        new_row["Album"] = input("Enter Album: ")
        new_row["Album type"] = input("Enter Album type: ")

        #Validar Uri
        uri_prompt = "Enter Uri: "
        uri_pattern = re.compile(r'^spotify:track:[a-zA-Z0-9]+$')
        new_row["Uri"] = AddSong.validate_input(uri_prompt, uri_pattern)

        # Validar y pedir URL_youtube hasta que sea válida
        youtube_prompt = "Enter URL_youtube: "
        youtube_pattern = re.compile(r'^(https?://)?(www\.)?(youtu\.be/|youtube\.com/watch\?v=)([a-zA-Z0-9_-]+)$')
        new_row["URL_youtube"] = AddSong.validate_input(youtube_prompt, youtube_pattern)

        #Llamar a la función convert_to_milliseconds() y guardar el resultado en el diccionario
        new_row["Duration_ms"] = AddSong.convert_to_milliseconds()
        new_row["title"] = input("Enter title: ")

        # Escribir en el archivo csv
        with open(AddSong.__archive, "a", newline="") as file:
            fieldnames = ["Index", "Artist", "URL_spotify", "Track", "Album", "Album type", "Uri", "Duration_ms", "URL_youtube", "title"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(new_row)

        print("New row added successfully!")

    @staticmethod
    def add_multiple_songs_from_file():
        csv_file = AddSong.__archive
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                columns = ['Artist', 'URL_spotify', 'Track', 'Album', 'Album type', 'Uri', 'Duration_ms', 'URL_youtube', 'title']
                writer = csv.DictWriter(file, fieldnames=columns)

                file_path = input("Enter the path of the file with new songs: ")

                with open(file_path, 'r', encoding='utf-8') as input_file:
                    # Verificar si la primera línea es una fila de encabezados
                    header_line = input_file.readline().strip()
                    if header_line != ','.join(columns):
                        print("Error: Las columnas en el archivo de entrada no coinciden con las esperadas.")
                        return

                    # Iterar sobre las líneas restantes
                    for line in input_file:
                        line_data = dict(zip(columns, line.strip().split(',')))
                        writer.writerow(line_data)

                print("Multiple songs added successfully!")

        except FileNotFoundError:
            print(f"El archivo {csv_file} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

