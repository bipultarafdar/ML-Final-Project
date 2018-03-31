import json
import csv
import glob
import os

script_dir = os.path.dirname(__file__)
path_src = ".\data_json\data"
path_dst = ".\data_json\data_csv\\"


def create_csv(json_fname):
    if json_fname.endswith(".json"):
        print("here", json_fname)
        json_fname = json_fname.replace(path_src, path_dst)
        json_fname = json_fname.replace(".json", ".csv")
    print(json_fname)
    f = csv.writer(open(json_fname, "w"))
    f.writerow(["name",
                "pid",
                "num_tracks",
                "num_albums",
                "num_followers",
                "track_pos",
                "artist_name",
                "track_name",
                "duration_ms",
                "album_name"])
    return f


def fill_csv(csv_file, json_data):
    for x in json_data["playlists"]:
        for y in x["tracks"]:
            csv_file.writerow([x["name"].encode("utf-8"),
                               x["pid"],
                               x["num_tracks"],
                               x["num_albums"],
                               x["num_followers"],
                               y["pos"],
                               y["artist_name"].encode("utf-8"),
                               y["track_name"].encode("utf-8"),
                               y["duration_ms"],
                               y["album_name"].encode("utf-8")])


if __name__ == "__main__":

    f1 = create_csv(path_dst + "data.csv")

    for filename in glob.glob(os.path.join(path_src, '*.json')):
        with open(filename, 'r') as file:
            # print(filename)
            data = json.load(file)
            f = create_csv(filename)
            fill_csv(f, data)
            fill_csv(f1, data)