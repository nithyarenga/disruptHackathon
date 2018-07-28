import os
import cPickle as pickle
import collections
import operator
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import RidgeClassifierCV
from sklearn.model_selection import cross_val_score
import rest_calls
# import instagram_data


def build_all_rows(combined_scores, reqd_cols):
    matrix = []
    outcome = []
    location_counter = 0
    location_dict = {}
    for location, location_files in combined_scores.items():
        print('Location and Tag', location, location_counter)
        for filename, all_tags_score in location_files.items():
            ind_row = {}
            for ind_tag in reqd_cols:
                try:
                    val = all_tags_score[ind_tag]
                except KeyError:
                    val = 0.0
                ind_row.setdefault(ind_tag, val)
            matrix.append(ind_row)
            outcome.append({'Outcome': location_counter})
        location_counter += 1
        location_dict.setdefault(location_counter, location)
    matrix = pd.DataFrame(matrix)
    outcome = pd.DataFrame(outcome)
    return matrix, outcome, location_dict


def curate_imagescores(flickr_results):
    all_reqd_tags = []
    combined_scores = {}
    for ind_location, location_results in flickr_results.items():
        top_tags = {}
        for filename, model_results in location_results.items():
            for ind_model in ['travel', 'general']:
                try:
                    for ind_tag, score in model_results[ind_model].items():
                        combined_scores.setdefault(ind_location, {}).setdefault(filename, {}).setdefault(ind_tag, score)
                        top_tags.setdefault(ind_tag, []).append(1)
                except KeyError:
                    pass
                    # print('Missed Tag {}'.format(ind_model))
        tag_counter = {}
        overall_counter = []
        for tag, counter in top_tags.items():
            tag_counter.setdefault(tag, len(counter))
            overall_counter.append(len(counter))
        tag_counter_list = [tag for (tag, val) in sorted(tag_counter.items(), key=operator.itemgetter(1), reverse=True)
                            if val >= 50]
        all_reqd_tags.extend(tag_counter_list)
    all_reqd_tags = list(set(all_reqd_tags))
    return combined_scores, all_reqd_tags


def build_matrix_df(pickle_filename):
    flickr_results = pickle.load(open(pickle_filename))
    combined_scores, all_reqd_tags = curate_imagescores(flickr_results)
    matrix, outcome, location_dict = build_all_rows(combined_scores, all_reqd_tags)
    data = {'matrix': matrix, 'outcome': outcome, 'rows': all_reqd_tags, 'location_dict': location_dict}
    pickle.dump(data, open(os.path.join('./cache', 'flickr_data.pickle'), 'w+'))
    print(matrix.wildlife.tolist())
    dt = DecisionTreeClassifier(random_state=0).fit(matrix, outcome)
    pickle.dump(dt, open(os.path.join('./cache', 'flickr_model_decisiontree.pickle'), 'w+'))
    print('Feature Importance', dt.feature_importances_)
    predict = dt.predict_proba(matrix)
    print('Probability', predict)
    act_predict = dt.predict(matrix)
    print(act_predict.tolist())
    score = dt.score(matrix, outcome)
    print('Shape', score)
    rc = RidgeClassifierCV(cv=3, normalize=True).fit(matrix, outcome)
    pickle.dump(rc, open(os.path.join('./cache', 'flickr_model_ridgeclasscv.pickle'), 'w+'))
    rc_df = rc.decision_function(matrix)
    for ind_row in rc_df:
        print(list(ind_row))
    #print(rc_df)
    raw_input('Done With Creating Model')


def run_instagram_model(group_id, image_urls):
    instagram_results = rest_calls.instagram_image_analysis(group_id, image_urls)
    instagram_scores, instagram_tags = curate_imagescores(instagram_results)
    # Loading Flickr Data
    training_data = pickle.load(open(os.path.join('./cache', 'flickr_data.pickle')))
    reqd_model = pickle.load(open(os.path.join('./cache', 'flickr_model_decisiontree.pickle')))
    # Building Test Matrix
    location_dict = training_data['location_dict']
    reqd_tags = training_data['rows']
    test_matrix, dummy_outcome, dummy_location = build_all_rows(instagram_scores, reqd_tags)
    #print(test_matrix)
    results = reqd_model.predict(test_matrix)
    results_proba = reqd_model.predict_proba(test_matrix)
    #print('->', results_proba)
    return collections.Counter([location_dict[i] for i in results])


if __name__ == "__main__":
    flickr_model = False
    if flickr_model:
        flickr_results_file = os.path.join('./cache', 'all_flicker_results.pickle')
        build_matrix_df(flickr_results_file)
        raw_input('Check')
    predict_instagram = True
    # if predict_instagram:
    #     print(run_instagram_model(instagram_data.instagram_package['group_id'], instagram_data.instagram_package['urls']))