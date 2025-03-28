# Actors and Directors Who Cooperated At Least Three Times

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).agg(count=('director_id', 'count')).reset_index()
    df = df[df['count'] >= 3][['actor_id', 'director_id']]
    print(df)
    return df

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

actors_and_directors(actor_director)