import streamlit as st
import lyricsgenius

# Streamlit Secrets から API キーを取得
GENIUS_ACCESS_TOKEN = st.secrets["GENIUS_ACCESS_TOKEN"]
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

def get_lyrics(artist, song):
    try:
        song_data = genius.search_song(song, artist)
        if song_data:
            return song_data.lyrics
        else:
            return "歌詞が見つかりませんでした。"
    except Exception as e:
        return f"エラーが発生しました: {e}"
