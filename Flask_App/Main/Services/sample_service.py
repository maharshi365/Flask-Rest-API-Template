from .. import db
from Main.Models.sample import Sample

def sample_get():
    return Sample.query.all()

def sample_set(data):
    new_sample = Sample(sample_data=data)
    db.session.add(new_sample)
    db.session.commit()
    response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
    return response_object, 201