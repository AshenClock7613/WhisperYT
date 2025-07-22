# WhisperYT

WhisperYT is a simple yet powerful command-line tool that leverages OpenAI's Whisper model to transcribe audio from YouTube videos or local audio files. The project generates a text file with a full transcription and detailed timestamps for each dialogue segment.

## Features

*   **Transcribe from YouTube**: Paste a YouTube video URL to automatically download the audio and transcribe it.
*   **Transcribe Local Files**: Provide the path to an audio file on your computer to get a transcription.
*   **Detailed Timestamps**: The output includes a timestamped version of the transcription in a `[mm:ss - mm:ss]` format for easy navigation.
*   **Full Transcription**: In addition to timestamped segments, the complete, raw text transcription is also provided in a single block.
*   **Italian Language Support**: Optimized for transcribing audio in the Italian language.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python 3.8+**
*   **FFmpeg**: Whisper and yt-dlp require FFmpeg for processing audio files.
    *   **On Windows**: Download the executable from the [official website](https://ffmpeg.org/download.html) and add the `bin` folder to your system's PATH.
    *   **On macOS**: You can easily install it with Homebrew: `brew install ffmpeg`
    *   **On Linux**: Use your distribution's package manager: `sudo apt update && sudo apt install ffmpeg`

## Installation

1.  **Clone or Download the Repository**
    If the project is on Git, you can clone it:
    ```bash
    git clone https://github.com/AshenClock7613/WhisperYT.git
    cd WhisperYT
    ```
    Alternatively, download the `stt.py` and `requirements.txt` files and save them in a new folder.

2.  **Install Dependencies**
    Install the required Python libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your command line:

```bash
python stt.py
```
You will be prompted to enter a source. You can provide either:

1.  **A YouTube video URL**:
    ```
    Enter the YouTube video URL or the path to a local audio file: https://www.youtube.com/watch?v=xxxxxxxxxxx
    ```

2.  **A path to a local audio file**:
    ```
    Enter the YouTube video URL or the path to a local audio file: /path/to/my/audio_file.mp3
    ```

The script will display its progress (downloading, transcribing, saving) and, upon completion, will show the path to the `.txt` file containing the transcription.

### Output Example

When the process is complete, a file named `<original_filename>_transcription.txt` will be created in the same folder as the audio file (or in the `audio/` directory for YouTube links). The file's content will look like this:

```txt
TRASCRIZIONE CON TIMESTAMP
==================================================

[00:00 - 00:05] This is the first segment of the transcription.
[00:06 - 00:10] And this is the second segment, with its timestamp.
[00:11 - 00:15] Each sentence or portion of speech is separated this way.

==================================================
TRASCRIZIONE COMPLETA:

This is the first segment of the transcription. And this is the second segment, with its timestamp. Each sentence or portion of speech is separated this way.
```
## Dependencies

*   [**openai-whisper**](https://github.com/openai/whisper): A robust, state-of-the-art automatic speech recognition (ASR) model.
*   [**yt-dlp**](https://github.com/yt-dlp/yt-dlp): A fork of `youtube-dl` with additional features and fixes, used for downloading videos from YouTube.
