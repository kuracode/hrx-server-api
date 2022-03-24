from core import api
from flask import jsonify
from core.utils import all_games, realm_royale, smite, rogue_company, paladins
from flask_restx import Resource

ns = api.namespace('/', description='Hi-Rez Studios server status API')

@ns.route('/all-games/')
class AllGamesAPI(Resource):
    '''Shows server status for all the Hi-Rez Studios games'''
    def get(self):
        data = all_games()
        return jsonify(success=True, data=data, status=200)

@ns.route('/smite/')
class SmiteAPI(Resource):
    '''Shows server status for Hi-Rez Studio game Smite'''
    def get(self):
        data = smite()
        return jsonify(success=True, data=data, status=200)

@ns.route('/rogue-company/')
class RogueCompanyAPI(Resource):
    '''Shows server status for Hi-Rez Studio game Rogue Company'''
    def get(self):
        data = rogue_company()
        return jsonify(success=True, data=data, status=200)

@ns.route('/paladins/')
class PaladinsAPI(Resource):
    '''Shows server status for Hi-Rez Studio game Paladins'''
    def get(self):
        data = paladins()
        return jsonify(success=True, data=data, status=200)

@ns.route('/realm-royale/')
class RealmRoyaleAPI(Resource):
    '''Shows server status for Hi-Rez Studio game Paladins'''
    def get(self):
        data = realm_royale()
        return jsonify(success=True, data=data, status=200)