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
    # print(mp3s)
    
    # convert songs from mp3 to wav

    def mp3_to_wav(name):
        """Takes in song name, converts mp3 to wav"""
        song_name = name.split('.')[0]
        new_name = f'{song_name}.wav'
        sound = AudioSegment.from_mp3(f'{MP3_FOLDER}/{name}')

        # add converted songs to second folder      
        dst = f'{WAV_FOLDER}/{new_name}'
        sound.export(dst, format="wav")
        return new_name

    wavs = []
    for mp3 in mp3s:
        wavs.append(mp3_to_wav(mp3)) 

    return wavs

def play_song(song_name):
    """Takes in song name and plays song"""
    wave_read = wave.open(path.join(WAV_FOLDER, song_name), 'rb')
    audio_data  = wave_read.readframes(wave_read.getnframes())
    num_channels = wave_read.getnchannels()
    bytes_per_sample = wave_read.getsampwidth()
    sample_rate = wave_read.getframerate()

    wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    return
    

def main():
    wavs = convert_music()
    play_song(wavs[0])



if __name__ == '__main__':
    main()