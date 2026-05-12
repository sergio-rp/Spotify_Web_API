from Pages.base_api import BaseAPI
from Config import settings

class AlbumsAPI(BaseAPI):
    def get_album(self, album_id):
        return self.get(settings.GET_ALBUM_URL + album_id)