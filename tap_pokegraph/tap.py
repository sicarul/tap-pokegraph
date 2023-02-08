"""PokeGraph tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_pokegraph.streams import (
    AllPokemonStream
)

STREAM_TYPES = [
    AllPokemonStream,
]


class TapPokeGraph(Tap):
    """PokeGraph tap class."""
    name = "tap-pokegraph"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="http://localhost:8090",
            description="The url for the graphql-pokemon API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapPokeGraph.cli()
