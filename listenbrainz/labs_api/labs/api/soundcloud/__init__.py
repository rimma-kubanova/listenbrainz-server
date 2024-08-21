from typing import Optional

from listenbrainz.labs_api.labs.api.metadata_index import BaseMetadataIndexOutput


class SoundcloudIdFromMBIDOutput(BaseMetadataIndexOutput):
    soundcloud_track_ids: Optional[list[str]]