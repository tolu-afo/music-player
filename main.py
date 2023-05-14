import os
import wave
from os import path
from pydub import AudioSegment
import simpleaudio as sa


MP3_FOLDER = './music'
WAV_FOLDER = './_music'

def convert_music():
    # get music from music folder
    for f in os.listdir(WAV_FOLDER):
        os.remove(path.join(WAV_FOLDER, f))

    mp3s = os.listdir(MP3_FOLDER)
    
    # convert songs from mp3 to wav

    def mp3_to_wav(name, vol=0):
        """Takes in song name, converts mp3 to wav"""
        song_name = name.split('.')[0]
        new_name = f'{song_name}.wav'
        sound = AudioSegment.from_mp3(f'{MP3_FOLDER}/{name}')

        # add converted songs to second folder      
        dst = f'{WAV_FOLDER}/{new_name}'
        sound.export(dst, format="wav")
        return new_name

    wavs = {}
    for ind, mp3 in enumerate(mp3s):
        wavs.update({ind+1 : mp3_to_wav(mp3).split('.')[0]}) 

    return wavs

def get_song(song_name) -> sa.WaveObject:
    """Takes in song name and plays song"""
    wave_read = wave.open(path.join(WAV_FOLDER, song_name), 'rb')
    audio_data = wave_read.readframes(wave_read.getnframes())
    num_channels = wave_read.getnchannels()
    bytes_per_sample = wave_read.getsampwidth()
    sample_rate = wave_read.getframerate()

    wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
    return wave_obj
    
def list_songs(songs:dict):
    print('Here are your songs to choose from!')
    for k in songs.keys():
        print(f'{k}: {songs.get(k)}')
    print("Type in s:[song_number] to select a song")

def set_volume(curr_song, vol):
    
    return get_song(f'{curr_song}.wav', vol)

def main():
    # end, s:song number, v:vol, play, pause, list
    end_cond = False
    curr_song = None
    curr_song_name = ''
    started = False
    songs = convert_music()
    list_songs(songs)


    while not end_cond:
        print('Commands: s:[song_number], play, pause, list, end')
        user_input = input("What would you like us to do?: ")
        if user_input == 'end':
            print('ending playback! Thank you have a good day!')
            end_cond = True
        elif user_input[0] == 's':
            song_number = user_input[2::]
            song_name = songs[int(song_number)]
            curr_song_name = song_name
            curr_song = get_song(f'{song_name}.wav')
            started = False
            print(f'you selected {song_name}')
        elif user_input == 'play':
            if started:
                curr_song.resume()
            else:
                curr_song = curr_song.play()
                started = True
        elif user_input == 'pause':
            curr_song.pause()
        elif user_input == 'list':
            list_songs(songs)
        else:
            print('Something Went Wrong. Try Again!')
        print(" ")


if __name__ == '__main__':
    main()