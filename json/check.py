import jsonschema # type: ignore
import json
import uuid
kds_schema = open('./kds-schema.json')
nlu_kds_json = open('./nlu.kds.json')
schema = json.load(kds_schema)
nlu_kds = json.load(nlu_kds_json )
res=jsonschema.validate(instance=nlu_kds,schema=schema)
print(res)
print("---------------------------------------------")
print(uuid.uuid1())
# No error, the JSON is valid.

## ValidationError: '30' is not of type 'number'
#
#validate(instance={"name": "John"}, schema=schema)
## No error, the JSON is valid.
#
#validate(instance={"age": 30}, schema=schema)
## ValidationError: 'name' is a required property
#
#validate(instance={"name": "John", "age": 30, "job": "Engineer"}, schema=schema)
## No error, the JSON is valid. By additional fields are allowed.
