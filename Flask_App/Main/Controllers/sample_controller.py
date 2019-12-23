from flask import request
from flask_restplus import Resource, Namespace, fields

from ..Services.sample_service import sample_get, sample_set

class SampleDTO:
    api = Namespace(name="Sample", description="Sample releated operations")
    sample = api.model('sample',{
        'sample_data': fields.String(required=True, description='sample data')
    })

api = SampleDTO.api
_sample = SampleDTO.sample

@api.route('/')
class SampleList(Resource):
    @api.doc('List of Sample Data')
    @api.marshal_list_with(_sample)
    def get(self):
        """List all registered users"""
        return sample_get()
    
    @api.response(201, 'Sample successfully created.')
    @api.doc('create new sample data')
    @api.expect(_sample, validate=True)
    def post(self):
        data = request.json
        return sample_set(data=data['sample_data'])