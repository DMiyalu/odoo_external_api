from .index import db, uid, password, url
import xmlrpc.client

class Partners:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    @classmethod
    def get_all_partners(cls):
        response = cls.models.execute_kw(db, uid, password,
            'res.partner', 'search_read',
            [], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        return response
    

    @classmethod
    def get_partner(cls, id):
        response = cls.models.execute_kw(db, uid, password,
            'res.partner', 'read',
            [id], {'fields': ['name', 'country_id', 'comment']})
        return response


    @classmethod
    def delete_partner(cls, id):
        response = cls.models.execute_kw(db, uid, password,
            'res.partner', 'unlink', [[id]])
        return response

    
    @classmethod
    def update_partner(cls, id, name):
        response = cls.models.execute_kw(db, uid, password,
            'res.partner', 'write', [[id], {'name': name}])
        return response


    @classmethod
    def create_partner(cls, name):
        response = cls.models.execute_kw(db, uid, password,
            'res.partner', 'create', [{'name': name}])
        return response