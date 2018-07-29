# import cPickle as pickle
# r = [{
#         "url": "https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv",
#         "location": "Austin",
#         "description":["adventure" , "music" , "food"]
#     },
#     {
#         "url": "https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I",
#         "location": "Germany",
#         "description":["hills" , "music" , "culture"]
#     }
#     ]
# output = open('myfile.pkl', 'wb')
# pickle.dump(r, output)
# # print r
# # print "!!!!!!!!!!!!!!"
# output.close()

# # r1 = [{
# #         "url": "https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv",
# #         "location": "Yellowstone",
# #         "description":["adventure" , "hicking" , "travel"]
# #     }]
# # # read python dict back from the file
# pkl_file = open('myfile.pkl', 'rb')
# old_reco = pickle.load(pkl_file)
# pkl_file.close()
# # mydict2.append(r1)
# # output = open('myfile.pkl', 'wb')
# # pickle.dump(mydict2, output)
# # output.close()
# # print mydict2

# import collections

# top_cities = collections.Counter({'new york': 4, 'salt lake city, utah': 4, 'anchorage, alaska': 3, 'seattle, washington': 3, 'nashville, tennessee': 3, 'denver, colarado': 1, 'san francisco, california': 1, 'honolulu, hawaii': 1})

# top_cities_images = {'salt lake city, utah': ['https://farm1.staticflickr.com/894/40687683560_b945f77b52_b.jpg', 'https://farm2.staticflickr.com/1741/42156113944_f73b3f8edf_b.jpg', 'https://farm2.staticflickr.com/1781/42159689264_e828943338_b.jpg', 'https://farm1.staticflickr.com/835/29470811218_0daf8aee46_b.jpg', 'https://farm8.staticflickr.com/7401/27213769551_f440a35409_b.jpg', 'https://farm2.staticflickr.com/1788/43214700341_ef6ccf2267_b.jpg', 'https://farm1.staticflickr.com/840/29700455278_2c727c9623_b.jpg', 'https://farm1.staticflickr.com/883/41854709085_cb0404686f_b.jpg'], 'new york': ['https://farm1.staticflickr.com/836/42618851734_23227013c4_b.jpg', 'https://farm1.staticflickr.com/979/42332606021_dd09119a2a_b.jpg', 'https://farm5.staticflickr.com/4712/25980574568_50e0977e25_b.jpg', 'https://farm1.staticflickr.com/788/40166504234_d28c497250_b.jpg', 'https://farm9.staticflickr.com/8048/8079672377_7c10099930_b.jpg', 'https://farm1.staticflickr.com/944/41853860571_77dd5b578a_b.jpg'], 'anchorage, alaska': ['https://farm1.staticflickr.com/870/40710335115_3b7a704b85_b.jpg', 'https://farm2.staticflickr.com/1744/42588246061_2ac774251f_b.jpg', 'https://farm1.staticflickr.com/788/40503343935_f25b72ddbf_b.jpg', 'https://farm1.staticflickr.com/833/41794621370_8ba6382615_b.jpg', 'https://farm5.staticflickr.com/4795/39884752905_ed091c1da5_b.jpg', 'https://farm2.staticflickr.com/1763/42310728675_dac811d6a8_b.jpg', 'https://farm2.staticflickr.com/1736/27525700387_87cea64d94_b.jpg', 'https://farm1.staticflickr.com/505/19724164602_2e748b70d7_b.jpg', 'https://farm5.staticflickr.com/4777/26921056228_04a8e280b0_b.jpg']}
# tags = {'salt lake city, utah': [u'summer', u'office', u'cute', u'young', u'contemporary', u'paper', u'rough', u'style', u'group', u'sky', u'lake', u'texture', u'desktop', u'window', u'wood', u'exhibition', u'pretty', u'retro', u'town', u'woman', u'garden', u'geology', u'dark', u'historic', u'glazed', u'shadow', u'tourism', u'furniture', u'Summer', u'idyllic', u'sand', u'vector', u'architecture', u'man', u'rock', u'tower', u'picture frame', u'square', u'old', u'people', u'house', u'seat', u'street', u'design', u'perspective', u'sight', u'portrait', u'girl', u'cactus', u'chair', u'Entrance', u'flower', u'leaf', u'fog', u'hill', u'scenery', u'business', u'nature', u'commercial', u'illustration', u'round out', u'water', u'step', u'relaxation', u'stone', u'island', u'industry', u'Gothic', u'castle', u'expression', u'road', u'exotic', u'Yoga', u'family', u'wall', u'one', u'indoors', u'seashore', u'goth like', u'art', u'landscape', u'city', u'ancient', u'vacation', u'tropical', u'no person', u'vehicle', u'valley', u'war', u'empty', u'group together', u'urban', u'entrance', u'glass items', u'door', u'Wedding', u'downtown', u'cloud', u'construction', u'adult', u'steel', u'flora', u'room', u'inside', u'tree', u'growth', u'transportation system', u'outdoors', u'beautiful', u'fashion', u'sea', u'petal', u'modern', u'decoration', u'Surroundings', u'home', u'facade', u'monochrome', u'mountain', u'ball-shaped', u'silhouette', u'vintage', u'travel', u'isolated', u'luxury', u'many', u'beach', u'wheel', u'symbol', u'disjunct', u'panoramic', u'View', u'building', u'light', u'ocean', u'landmark'], 
# 'new york': [u'summer', u'office', u'cute', u'young', u'contemporary', u'paper', u'Yoga', u'chair', u'apartment', u'group', u'rose', u'sky', u'lake', u'texture', u'desktop', u'bouquet', u'window', u'wood', u'exhibition', u'hill', u'town', u'woman', u'garden', u'dark', u'historic', u'wedding', u'front', u'shadow', u'tourism', u'furniture', u'Summer', u'idyllic', u'gift', u'sand', u'vector', u'architecture', u'man', u'rock', u'public show', u'tower', u'picture frame', u'square', u'old', u'crowd', u'people', u'house', u'seat', u'street', u'design', u'perspective', u'sea', u'home', u'girl', u'shining', u'disjunct', u'flower', u'leaf', u'pavement', u'fog', u'retro', u'scenery', u'business',u'nature', u'blooming', u'commercial', u'illustration', u'water', u'step', u'relaxation', u'stage', u'stone', u'island', u'industry', u'Gothic', u'military', u'castle', u'expression', u'road', u'exotic', u'love', u'family', u'wall', u'one', u'indoors', u'seashore', u'goth like', u'table', u'mist', u'landscape', u'city', u'art', u'ancient', u'vacation', u'tropical', u'no person', u'splash', u'vehicle', u'valley', u'war', u'empty', u'group together', u'urban', u'entrance', u'glass items', u'door', u'Wedding', u'downtown', u'construction', u'adult', u'steel', u'flora', u'room', u'inside', u'tree', u'roof', u'growth', u'transportation system', u'outdoors', u'property', u'Balcony', u'beautiful', u'fashion', u'sight', u'estate', u'Bicycling', u'petal', u'modern', u'decoration', u'Surroundings', u'single', u'exterior', u'portrait', u'facade', u'monochrome', u'mountain', u'ball-shaped', u'silhouette', u'sit', u'vintage', u'travel', u'romance', u'luxury', u'many', u'beach',u'wheel', u'symbol', u'Entrance', u'panoramic', u'floral', u'View', u'building', u'light', u'ocean', u'boat', u'landmark', u'model'], 
# 'anchorage, alaska': [u'summer', u'office', u'cute', u'young', u'contemporary', u'biker', u'Yoga', u'chair', u'apartment', u'group', u'sky', u'lake', u'desktop', u'window', u'wood', u'hill', u'steel', u'turquoise', u'garden', u'dark', u'shadow', u'tourism',u'furniture', u'Summer', u'bay', u'pavement', u'vector', u'architecture', u'rock', u'square', u'art', u'people', u'house', u'seat', u'growth', u'design', u'perspective', u'sea', u'portrait', u'disjunct', u'flower', u'leaf', u'sand', u'fog', u'retro', u'scenery', u'business', u'nature', u'blooming', u'commercial', u'illustration', u'water', u'relaxation', u'cyclist', u'stone', u'island', u'industry', u'military', u'expression', u'road', u'exotic', u'bike', u'love', u'family', u'wall', u'one', u'indoors', u'seashore', u'table', u'mist', u'landscape', u'city', u'vacation', u'tropical', u'no person', u'splash', u'Wedding', u'valley', u'war', u'empty', u'urban', u'glass items', u'door', u'vehicle', u'downtown', u'cloud', u'construction', u'adult', u'town', u'flora', u'room', u'inside', u'tree', u'seated', u'crystal', u'street', u'transportation system', u'View', u'outdoors', u'beautiful', u'sight', u'Bicycling', u'petal', u'modern', u'decoration', u'Surroundings', u'single', u'home', u'monochrome', u'mountain', u'vintage', u'travel', u'romance', u'old', u'luxury', u'beach', u'wheel', u'symbol', u'Entrance', u'panoramic', u'wire', u'floral', u'man', u'building', u'light', u'ocean', u'boat']}

# new_reco = []
# city_list = top_cities.most_common(3)
# for x in city_list:
#     loc = x[0]
#     new_json = {
#         "location": loc,
#         "url": [top_cities_images[loc][0],top_cities_images[loc][1],top_cities_images[loc][2]],
#         "description": [tags[loc][0],tags[loc][1],tags[loc][2]]
#     }
#     new_reco.append(new_json)
# #print new_reco

# old_reco.extend(new_reco)
# print old_reco
# unique_reco = {v['location']:v for v in old_reco}.values()
# pkl_file = open('myfile.pkl', 'wb')
# pickle.dump(unique_reco, pkl_file)
# print unique_reco

import os.path
file_name = "123"+".pkl"
if not os.path.isfile(file_name): 
    print "not"
    file = open(file_name, 'w+')
    file.close()
   

