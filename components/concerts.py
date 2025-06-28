import json

def load_concerts(file_path='data/concerts.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def filter_concerts_by_genre(concerts, selected_genres):
    return [concert for concert in concerts if any(g in concert['genre'] for g in selected_genres)]