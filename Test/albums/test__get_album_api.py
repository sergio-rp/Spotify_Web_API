from Pages.albums_api import AlbumsAPI
from Config import settings
import json


def test_get_album_positive(auth_headers):
    api = AlbumsAPI(auth_headers)
    response = api.get_album(settings.ALBUM_ID)
    data = response.json()

    print(json.dumps(data, indent=4))

    # STATUS
    assert response.status_code == 200

    # RESPONSE NOT EMPTY
    assert response.text != ""

    # ROOT TYPES
    assert isinstance(data, dict)

    # REQUIRED FIELDS
    required_fields = [
        "album_type",
        "total_tracks",
        "href",
        "id",
        "images",
        "name",
        "release_date",
        "type",
        "uri",
        "artists",
        "tracks"
    ]

    for field in required_fields:
        assert field in data

    # BASIC VALIDATIONS
    assert data["id"] == settings.ALBUM_ID

    assert data["type"] == "album"

    assert isinstance(data["name"], str)
    assert data["name"] != ""

    assert isinstance(data["total_tracks"], int)
    assert data["total_tracks"] > 0

    # URL VALIDATIONS
    assert data["href"].startswith(
        "https://api.spotify.com/v1/albums/"
    )

    assert data["external_urls"]["spotify"].startswith(
        "https://open.spotify.com/album/"
    )

    # URI VALIDATION
    assert data["uri"].startswith("spotify:album:")

    # RELEASE DATE
    assert isinstance(data["release_date"], str)

    assert data["release_date_precision"] in [
        "year",
        "month",
        "day"
    ]

    # IMAGES
    assert isinstance(data["images"], list)

    assert len(data["images"]) > 0

    for image in data["images"]:
        assert "url" in image
        assert "height" in image
        assert "width" in image

        assert image["url"].startswith("https://")

        assert isinstance(image["height"], int)
        assert isinstance(image["width"], int)

        assert image["height"] > 0
        assert image["width"] > 0

    # ARTISTS
    assert isinstance(data["artists"], list)

    assert len(data["artists"]) > 0

    for artist in data["artists"]:
        assert artist["type"] == "artist"

        assert isinstance(artist["name"], str)
        assert artist["name"] != ""

        assert artist["href"].startswith(
            "https://api.spotify.com/v1/artists/"
        )

        assert artist["uri"].startswith(
            "spotify:artist:"
        )

    # TRACKS OBJECT
    tracks = data["tracks"]

