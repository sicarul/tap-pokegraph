"""Stream type classes for tap-pokegraph."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_pokegraph.client import PokeGraphStream

class AllPokemonStream(PokeGraphStream):
    """Define custom stream."""
    name = "pokemon"
    base_object = 'getAllPokemon'
    
    schema = th.PropertiesList(
        th.Property("key", th.StringType),
        th.Property("baseForme", th.StringType),
        th.Property("baseSpecies", th.StringType),
        th.Property("baseStats", th.ObjectType(
            th.Property("attack", th.IntegerType),
            th.Property("defense", th.IntegerType),
            th.Property("hp", th.IntegerType),
            th.Property("specialattack", th.IntegerType),
            th.Property("specialdefense", th.IntegerType),
            th.Property("speed", th.IntegerType),
        )),
        th.Property("baseStatsTotal", th.IntegerType),
        th.Property("color", th.StringType),
        th.Property("evolutionLevel", th.StringType),
        
        th.Property("forme", th.StringType),
        th.Property("formeLetter", th.StringType),
        th.Property("gender", th.ObjectType(
            th.Property("female", th.StringType),
            th.Property("male", th.StringType),
        )),
        th.Property("height", th.NumberType),
        th.Property("num", th.IntegerType),
        th.Property("otherFormes", th.ArrayType(th.StringType)),
        th.Property("sprite", th.StringType),
        th.Property("types", th.ArrayType(th.ObjectType(
            th.Property("name", th.StringType),
        ))),
        th.Property("weight", th.NumberType),
    ).to_dict()

    primary_keys = ["key"]
    replication_key = None
    query = """
        getAllPokemon {
            key
            baseForme
            baseSpecies
            baseStats {
                attack
                defense
                hp
                specialattack
                specialdefense
                speed
            }
            baseStatsTotal
            color
            evolutionLevel
            
            forme
            formeLetter
            gender {
                female
                male
            }
            height
            num
            otherFormes
            sprite
            types {
                name
            }
            weight
        }
        """

