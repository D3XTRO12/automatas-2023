from engine_metrics import *
from ratio_metrics import *
from search_song import *
from add_new_song import AddSong
from top_duration_songs import *
from top_artist import *
from clear import *
def start_menu():
    while True:
            print("<<<<<Music system list>>>>>")
            print("1 = List Top 5 songs by different metrics:")
            print("2 = Get Top 5 by ratio: ")
            print("3 = Search for a song by name:")
            print("4 = Add a new song:")
            print("5 = Get Top 10 songs by duration:")
            print("6 = Get Top 10 artists:")
            print("7 = <<Exit>")
            selection = input("CHOOSE THE OPTION[1/2/3/4/5/6/7]  = ")
            if selection == '1':
                while True:
                    print("<<<<<Music system list>>>>>")
                    print("1 = List Top 5 songs by likes:")
                    print("2 = List Top 5 songs by comments:")
                    print("3 = List Top 5 songs by views:")
                    print("4 = <<Back To The Principal Menu>")
                    selection = input("CHOOSE THE OPTION[1/2/3/4]  = ")
                    if selection == '1':
                        SongMetricsEngine.list_top_songs_by_likes()
                        input("Press Enter to continue...")
                        clear_console()
                    elif selection == '2':
                        CommentsMetricsEngine.list_top_songs_by_comments()
                        input("Press Enter to continue...")
                        clear_console()
                    elif selection == '3':
                        ViewsMetricsEngine.list_top_songs_by_views()
                        input("Press Enter to continue...")
                        clear_console()
                    elif selection == '4':
                        clear_console()
                        break
                    else:
                        print("\n Invalid option. Please try again.")
                        clear_console()

            elif selection == '2':

                RatioMetricsEngine.list_for_ratio()
                clear_console()

            elif selection == "3":
                
                SearchSongEngine.search_song()
                clear_console()

            elif selection == "4":
               while True:
                    print("<<<<<Music system list>>>>>")
                    print("1 = Add a new song:")
                    print("2 = Add multiple songs from a file:")
                    print("3 = <<Back To The Principal Menu>")
                    selection = input("CHOOSE THE OPTION[1/2/3]  = ")
                    if selection == '1':
                        AddSong.add_new_song()
                        input("Press Enter to continue...")
                        clear_console()

                    elif selection == '2':
                        AddSong.add_multiple_songs_from_file()  #no funciona aun, falta terminar y ver que pide en verdad el profesor
                        input("Press Enter to continue...")
                        clear_console()

                    elif selection == '3':
                        clear_console()
                        break
                    else:
                        print("\n Invalid option. Please try again.")

            elif selection == "5":

                SongDurationTop.list_top_songs_by_duration()
                clear_console()
                    
            elif selection == '6':
                
                TopArtistViews.list_top_artists_by_views()
                clear_console()

            elif selection == '7':

                clear_console()
                print("¡Thanks For Use The App Music System!")
                break

            else:
                clear_console()
                print("\n Invalid option. Please try again.")

start_menu()