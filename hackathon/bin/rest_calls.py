import requests
import json
import cPickle as pickle
import hashlib
import os
from urllib import urlencode
from copy import deepcopy
from clarifai.rest import ClarifaiApp
from glob import glob


clarifia_apikey_old = 'f36980edd0654cd994869d9c597f0166' # All free runs complete
clarifia_apikey = 'd301c4c8bf9a486289f11eea3b52ccae'

rest_errors = {
    200: 'All Ok Gopi',
    301: 'Redirecting',
    400: 'bad request',
    401: 'not authenticated',
    403: 'access is forbidden',
    404: 'server not found'
}

# Flickr Details
flickr_image_search_params = {
    'img_search_params': {
        'method':'flickr.photos.search',
        'api_key': '92cd8d03af0235c7f0301a87dabedb55',
        'format': 'json',
        'nojsoncallback': 1,
        'per_page': 500,
        'has_geo': 'true',
        'tags': 'mountain',
        'sort': 'relevance',
        'content_type': 1,
        'page': 1,
        'accuracy': 10,
    },
    'base_url': 'https://api.flickr.com/services/rest/'
}

secret= '64bed323a4ead17e'
#'api_sig': '7b52eaafd63c0ad69f696a3edf332f94',

#flickr_img_format = "https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg".format()

flickr_img_search = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={key_id}&tags={}&has_geo={}&per_page={}&format={}&nojsoncallback={}&api_sig={api_sig}'


class RequestAPI(object):
    def __init__(self):
        self.m = hashlib.md5()
        self.file_directory = './cache/'
        if not os.path.isdir(self.file_directory):
            os.mkdir(self.file_directory)

    def check_response_error(self, response_data):
        status = True
        if str(response_data.status_code) == '200':
            return status
        elif str(response_data.code) == '100':
            status = False
        elif response_data.stat == 'fail':
            status = False
        return status

    def complete_response(self, url, params):
        reqd_url = self.create_url(url, params)
        hash_filename = "{}.pickle".format(hashlib.sha224(reqd_url).hexdigest())
        file_path = os.path.join(self.file_directory, hash_filename)
        if os.path.isfile(file_path):
            print("Loading Cache")
            reqd_data = pickle.load(open(file_path))
        else:
            reqd_data = self.handle_api(url, params)
            if not self.check_response_error(reqd_data):
                reqd_data = {}
            else:
                pickle.dump(reqd_data, open(file_path, 'w+'))
                print('Data Cached')
        return reqd_data

    def create_url(self, url, param):
        qstr = urlencode(param)
        return url + qstr

    def handle_api(self, base_url, params):
        response = requests.get(base_url, params=params)
        print('Status of the Call', rest_errors[response.status_code])
        print('URL', response.url)
        return response


def parse_flikr_json(json_data):
    photos = json_data['photos']
    counter = 0
    all_images = []
    for ind_photo in photos['photo']:
        flickr_url = "https://farm{farmid}.staticflickr.com/{serverid}/{id}_{secret}_b.jpg".format(farmid=ind_photo['farm'], serverid=ind_photo['server'], id=ind_photo['id'], secret=ind_photo['secret'])
        #print("{} of {} Photo Title {}: {}".format(counter, total_count, ind_photo['title'], flickr_url))
        all_images.append(flickr_url)
        counter += 1
    return all_images


class ManageCacheFolder(object):
    def __init__(self, process_tag):
        print("Manage The folders for caching")
        self.cache_folder = './cache/'
        self.cache_format = '{}_pickle'.format(process_tag)
        if not os.path.isdir(self.cache_folder):
            os.mkdir(self.cache_folder)
        self.file_hash = self._list_existing_files(self.cache_folder, self.cache_format)

    def _list_existing_files(self, folder, file_format):
        file_hash = {}
        all_files =  glob(os.path.join(folder, '*.{}'.format(file_format)))
        for ind_file in all_files:
            file_hash.setdefault(os.path.basename(ind_file).split('.')[0], True)
        return file_hash

    def _create_hashfilename(self, url):
        hash_id = hashlib.sha224(url).hexdigest()
        hash_filename = "{}.{}".format(hash_id, self.cache_format)
        return hash_id, hash_filename

    def _check_url_status(self, url):
        hash_id, hash_filename = self._create_hashfilename(url)
        hash_status = True
        try:
            self.file_hash[hash_id]
        except KeyError:
            self.file_hash[hash_id] = True
            hash_status = False
        return hash_status, hash_filename


class ClarifiaImageAnalysis(object):
    def __init__(self, group_id):
        print("setting up Clarifia image analysis")
        self.app = ClarifaiApp(api_key=clarifia_apikey)
        self.travel_model = self.app.models.get('travel-v1.0')
        self.general_model = self.app.models.get('general-v1.3')
        self.manage_files = ManageCacheFolder(group_id)

    def predict_image(self, url, cache_folder, cache_filename):
        multiple_response = {}
        multiple_response['general'] = self.general_model.predict_by_url(url=url)
        status_general = multiple_response['general']['status']['description']
        multiple_response['travel'] = self.travel_model.predict_by_url(url=url)
        status_travel = multiple_response['travel']['status']['description']
        print(status_general, status_travel)
        if status_general == 'Ok' and status_travel == 'Ok':
            print('Image url {} Passed'.format(url))
            pickle.dump(multiple_response, open(os.path.join(cache_folder, cache_filename), 'w+'))
        else:
            print('Clarifia Failed for image url {}! Check System, Gopi'.format(url))
            raw_input('Wait Here got Gopi')
        print('Response Cached for url {}'.format(url))
        return multiple_response

    def image_response(self, url):
        hash_status, hash_filename = self.manage_files._check_url_status(url)
        print('Image Response', hash_status, hash_filename)
        if hash_status:
            reqd_data = pickle.load(open(os.path.join(self.manage_files.cache_folder, hash_filename)))
        else:
            reqd_data = self.predict_image(url, self.manage_files.cache_folder, hash_filename)
        return hash_filename, reqd_data

    def analyze_response(self, response_data):
        reqd_concepts = {}
        for ind_model in ['travel', 'general']:
            for ind_output in response_data[ind_model]['outputs']:
                for concept_val in ind_output['data']['concepts']:
                    if concept_val['value'] > 0.3:
                        reqd_concepts.setdefault(ind_model, {}).setdefault(concept_val['name'], concept_val['value'])
        return reqd_concepts

    def analyze_multiple_images(self, urls):
        all_image_results = {}
        for ind_image_url in urls:
            filename, response_data = self.image_response(ind_image_url)
            reqd_response = self.analyze_response(response_data)
            all_image_results.setdefault(filename, reqd_response)
        return all_image_results


def flickr_image_analysis(all_tags, search_params):
    api_details = RequestAPI()
    clarafia = ClarifiaImageAnalysis('flickr')
    all_results = dict()
    for ind_tag in all_tags:
        print ("Currently processing {} tags".format(ind_tag))
        reqd_params = deepcopy(search_params)
        reqd_params['img_search_params']['tags'] = ind_tag
        reqd_links = api_details.complete_response(reqd_params['base_url'], reqd_params['img_search_params'])
        reqd_images = parse_flikr_json(reqd_links.json())
        result = clarafia.analyze_multiple_images(reqd_images)
        all_results.setdefault(ind_tag, result)
    return all_results


def instagram_image_analysis(group_id, all_images):
    results = {}
    clarafia = ClarifiaImageAnalysis(group_id)
    results.setdefault(group_id, clarafia.analyze_multiple_images(all_images))
    return results


if __name__ == '__main__':

    all_tags = ['denver, colarado', 'austin, texas', 'seattle, washington', 'nashville, tennessee', 'san francisco, california', 'new york', 'honolulu, hawaii', 'salt lake city, utah', 'anchorage, alaska', 'miami, florida']
    group_id = 'test'
    flicker_run = True
    instagram_run = True
    if flicker_run:
        all_flicker_results = flickr_image_analysis(all_tags, flickr_image_search_params)
        pickle.dump(all_flicker_results, open(os.path.join('./cache', 'all_flicker_results.pickle'), 'w+'))
        raw_input('Flickr - Wait Here')
    if instagram_run:
        instagram_results = instagram_image_analysis(instagram_package['group_id'], instagram_package['urls'])
        pickle.dump(instagram_results, open(os.path.join('./cache', 'all_instragram_results.pickle'), 'w+'))
        raw_input('Woa')