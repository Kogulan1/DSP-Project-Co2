
import csv

def feature_selection_continuous_columns(X_preprocessed, models_dir):
    models_dir = models_dir
    continuous_columns = X_preprocessed.copy()
    num_corr_co2_emission = continuous_columns.corr()['CO2 Emissions(g/km)'][:-1]
    best_features = num_corr_co2_emission[abs(num_corr_co2_emission) > 0.35].sort_values(ascending=False)
    for feature in best_features.index:
     num_corr_co2_emission.drop(feature,inplace = True)

    print(best_features)

    for feature in num_corr_co2_emission.index:
        continuous_columns = continuous_columns.drop(feature,axis = 1,inplace = True)

    feature_selected_continuous_columns = continuous_columns.copy()
    print(feature_selected_continuous_columns)
    csv_write_feaature(feature_selected_continuous_columns)
    return feature_selected_continuous_columns


def csv_write_feaature(feature_selected_continuous_columns):
    print("Write_CSV",feature_selected_continuous_columns)
    #feature_selected_continuous_columns = feature_selected_continuous_columns.drop('CO2 Emissions(g/km)', inplace=True, axis=1)
    textfile = open("feature_selected_continuous_columns.txt", "w")
    for element in feature_selected_continuous_columns:
        textfile.write(element + "\n")
    textfile.close()