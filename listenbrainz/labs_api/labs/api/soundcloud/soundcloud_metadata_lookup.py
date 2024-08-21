from listenbrainz.labs_api.labs.api.metadata_index.metadata_index_from_metadata_lookup import \
    MetadataIndexFromMetadataQuery
from listenbrainz.labs_api.labs.api.soundcloud import SoundcloudIdFromMBIDOutput


class SoundcloudIdFromMetadataQuery(MetadataIndexFromMetadataQuery):
    """ Query to lookup soundcloud track ids using artist name, release name and track name. """

    def __init__(self):
        super().__init__("soundcloud")

    def names(self):
        return "soundcloud-id-from-metadata", "Soundcloud Track ID Lookup using metadata"

    def introduction(self):
        return """Given the name of an artist, the name of a release and the name of a recording (track)
                  this query will attempt to find a suitable match in Soundcloud."""

    def outputs(self):
        return SoundcloudIdFromMBIDOutput
