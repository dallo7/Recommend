import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df1 = pd.read_csv("newDfForTraining.csv")


def recommend_cars(car_name, data=df1):
    df = data
    correlation_matrix = df.corr()

    recommended_cars = set()

    recommendations = correlation_matrix[car_name].sort_values(ascending=False)[1:5]
    recommendations = recommendations[recommendations.index.str.startswith("carName_")]
    # print(recommendations)

    # Add unique recommendations to the set
    for car in recommendations.index:
        recommended_cars.add(car)

    # Fill in with more recommendations if needed, ensuring uniqueness
    while len(recommended_cars) < 4:
        top_correlations = correlation_matrix[car_name].sort_values(ascending=False)[1:]
        for car in top_correlations.index:
            if car not in recommended_cars and car.startswith("carName_"):
                recommended_cars.add(car)
            if len(recommended_cars) == 4:
                break
    loop = pd.Series(list(recommended_cars))
    test = []
    for i in list(loop):
        test.append(i.replace("carName_", ""))

    return test


def recommend_cosine(car_name, df1=df1, top_n=4):
    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(df1.T)

    # Create a dataframe from the similarity matrix
    df_sim = pd.DataFrame(similarity_matrix, index=df1.columns, columns=df1.columns)

    # Exclude the selected car
    df_sim = df_sim.drop(car_name, axis=0)

    # Only consider cars that start with 'carName_'
    df_sim = df_sim.filter(regex='^carName_', axis=0)

    # Get the top_n most similar cars
    similar_cars = df_sim[car_name].sort_values(ascending=False)[:top_n]
    # print(similar_cars)

    test = []
    for i in list(similar_cars.index):
        test.append(i.replace("carName_", ""))

    return list(test)


# Test the function
# print(recommend_cosine('carName_ritz'))
