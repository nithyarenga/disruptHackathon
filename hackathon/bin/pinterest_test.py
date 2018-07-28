import pprint
import requests
import os


from pinterest import Pinterest


token = 'ATqdVkIaTuvNa6SNYXYZbVbr8SCSFUNGH6KkQLJFGO-iRUArBgAAAAA'
folderPath =  './test'

pinterest = Pinterest(username_or_email='gopinath.sundaramurthy@gmail.com', password='ipog123')


logged_in = pinterest.login()
print('Logged In', logged_in)

boards_personal = pinterest.boards()
print(boards_personal)

boards = pinterest.search_boards(query='Austin Texas', next_page=True)

for ind_board in boards:
    id = ind_board['id']
    #print(ind_board['name'], ind_board['url'])
    #raw_input()

print('Required Board', boards_personal[0]['id'])
response = requests.get(
    'https://api.pinterest.com/v1/boards/'+str(boards_personal[0]['id'])+'/pins/',
    params={'access_token': token,
            })


imageDatas = response.json()['data']
#print(imageDatas)
#raw_input('2')
for imageData in imageDatas:
    note = imageData['note']
    imageUrl = imageData['url']
    print(note, imageUrl)
    #imageDesc = imageData['description']
    #imageSig = imageData['image_signature']

    #extensions = imageUrl.split('.')
    #extension = extensions[len(extensions)-1]

    #f = open(folderPath+"/"+imageSig+"."+extension,'wb')
    #f.write(urlopen(imageUrl).read())
    #f.close()


raw_input('Wait Here')
for ind_image in response.json()['data']:
    print(ind_image['url'])
    raw_input('Wait')

print(response.json())
print(response.url)
print('Yay')

if __name__ == "__main__":
    board_id = ''