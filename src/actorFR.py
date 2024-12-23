import pandas as pd
from collections import Counter
import imdb
ia = imdb.Cinemagoer()
actor_name = ia.get_person('0000168')
print(actor_name.keys())
exit()
# Load the DataFrame (replace 'your_data.csv' with your actual file)
df = pd.read_csv('data/watchlist_with_actors_writers.csv')

# Flatten the 'Actors' column and count frequencies
if 'Actors' in df.columns:
    # Combine all actor IDs into one list
    all_actors = [actor for actor_list in df['Actors'].apply(eval) for actor in actor_list if actor]
    # Count the frequencies of actor IDs
    actor_counts = Counter(all_actors)
    # Get the top 10 most common actors
    top_10_actors = actor_counts.most_common(20)
    print("Top 10 Most Frequent Actors:")
    for actor, count in top_10_actors:
        actor_name = ia.get_person(actor)
        print(f"{actor_name['name']} ({actor}): {count} fr: {count/max(len(actor_name['filmography']['actress']),len(actor_name['filmography']['actor']))}")


# Flatten the 'Writers' column and count frequencies
if 'Writers' in df.columns:
    # Combine all writer IDs into one list
    all_writers = [writer for writer_list in df['Writers'].apply(eval) for writer in writer_list if writer]
    # Count the frequencies of writer IDs
    writer_counts = Counter(all_writers)
    # Get the top 10 most common writers
    top_10_writers = writer_counts.most_common(20)
    print("\nTop 10 Most Frequent Writers:")
    for writer, count in top_10_writers:
        writer_name = ia.get_person(writer)
        print(f"{writer_name['name']} ({writer}): {count} fr: {count/len(writer_name['filmography']['writer'])}")
