import yt_dlp
import whisper
import os
from pathlib import Path
import subprocess

def download_audio_from_youtube(url, output_path="audio"):
    """Scarica l'audio da un video YouTube"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info['title']
        return f"{output_path}/{title}.wav"

def transcribe_audio(audio_path, model_name="medium"):
    """Trascrizione audio con Whisper"""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, verbose=True,language='it')
    return result

def save_transcription_with_timestamps(result, output_file):
    """Salva la trascrizione con timestamp in un file .txt"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("TRASCRIZIONE CON TIMESTAMP\n")
        f.write("=" * 50 + "\n\n")
        
        for segment in result['segments']:
            start_time = segment['start']
            end_time = segment['end']
            text = segment['text'].strip()
            
            # Formato timestamp [mm:ss - mm:ss]
            start_min, start_sec = divmod(start_time, 60)
            end_min, end_sec = divmod(end_time, 60)
            
            timestamp = f"[{int(start_min):02d}:{int(start_sec):02d} - {int(end_min):02d}:{int(end_sec):02d}]"
            f.write(f"{timestamp} {text}\n")
        
        f.write("\n" + "=" * 50 + "\n")
        f.write("TRASCRIZIONE COMPLETA:\n\n")
        f.write(result['text'])

def main():
    input_source = input("Inserisci l'URL del video YouTube o il percorso del file audio locale: ")
    
    # Se inizia con "http", consideralo un URL YouTube
    if input_source.startswith("http"):
        try:
            print("Scaricamento audio in corso...")
            audio_file = download_audio_from_youtube(input_source)
            print(f"Audio scaricato: {audio_file}")
            
            # skip manual conversion; Whisper can load MP3 directly
            print("Trascrizione in corso...")
            transcription = transcribe_audio(audio_file)
            
            p2 = Path(audio_file)
            output_file = str(p2.parent / f"{p2.stem}_transcription.txt")
            print("Salvataggio trascrizione...")
            save_transcription_with_timestamps(transcription, output_file)
            
            print(f"Trascrizione completata e salvata in: {output_file}")
        except Exception as e:
            print(f"Errore: {e}")
    else:
        # Gestisce file audio locale
        audio_file = input_source
        if not os.path.exists(audio_file):
            print(f"Il file {audio_file} non esiste.")
            return
        
        try:
            print("Trascrizione in corso...")
            transcription = transcribe_audio(audio_file)
            
            p = Path(audio_file)
            output_file = str(p.parent / f"{p.stem}_transcription.txt")
            print("Salvataggio trascrizione...")
            save_transcription_with_timestamps(transcription, output_file)
            
            print(f"Trascrizione completata e salvata in: {output_file}")
        except Exception as e:
            print(f"Errore: {e}")

if __name__ == "__main__":
    main()