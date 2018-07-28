import requests
import os
import json

g_counter = 0
all_images = []


def get_instagram_citydata(url, cursor=''):
    global g_counter, all_images
    g_counter += 1
    if g_counter > 3:
        return
    counter = 0
    if cursor != '':
        reqd_url = '&'.join([url, cursor])
    else:
        reqd_url = url
    response = requests.get(reqd_url)
    reqd_data = response.json()['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    for ind_img in reqd_data:
        all_images.append(ind_img['node']['display_url'])
        print(g_counter, counter, ind_img['node']['display_url'])
        counter += 1
    cursor = response.json()['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    print(cursor, len(list(set(all_images))))
    get_instagram_citydata(url, cursor=cursor)
    raw_input('Wait here')



if __name__ == '__main__':
    reqd_path = 'https://www.instagram.com/explore/tags/travelaustin/?__a=1'
    get_instagram_citydata(reqd_path)