# prequel-api #

An API for Prequel Adventure.

Defaults to host 0.0.0.0 and port 65010, with base url `/api`. These settings will be used when referring to endpoints.

## Methods ##

- `http://0.0.0.0:65010/api/latest` - Retrieves the latest update. Returns an `Update`.
- `http://0.0.0.0:65010/api/latest/<num>` - Retrieves latest <num> updates. Returns a list of `Update` models.
- `http://0.0.0.0:65010/api/from/<year>/<month>/<day>/` - Retrieves the update from the specified day.

## Models ##

`Article`s are JSON dictionaries. They contain:

- `title`: the title of the update ("Katia: Trade", "==>", etc.)
- `link`: the link to the update
- `summary`: A paragraph from the update, direct from the RSS feed
- `published`: The date the update was published, in ISO-6801 format.
