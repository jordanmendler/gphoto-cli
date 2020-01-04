
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
SCOPES = 'https://www.googleapis.com/auth/photoslibrary.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('photoslibrary', 'v1', http=creds.authorize(Http()))

# Call the Photo v1 API and list my Albums
results = service.albums().list(
    pageSize=10, fields="nextPageToken,albums(id,title)").execute()
items = results.get('albums', [])
if not items:
    print('No albums found.')
else:
    print('Albums:')
    for item in items:
        print('{0} ({1})'.format(item['title'].encode('utf8'), item['id']))

## list specified album contents
'''service = build('photoslibrary', 'v1', credentials=creds)
albumId = 'AN5LCg2dhgcFxXip9PR6BUea4QMk3WlQR50QqJuA2hgF0VEjL28zQ0Zjqsmg6FHQMWDElr5ZtvN4'  # Please set the album ID.
results2 = service.mediaItems().search(body={'albumId': albumId}).execute()
print(results2)'''

#filter photos including me
results3 = service.mediaItems().search(body={
    "filters": {
      "contentFilter": {
        "includedContentCategories": [
          "SELFIES"
        ]
      }
    }
  }
).execute()

print(results3)
