from flask_restful import Resource,reqparse
import sqlalchemy
import os
from .game import Game

engine = sqlalchemy.create_engine(
    os.environ['GALOOK_DATABASE_URL']
)

class Games(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        args = parser.parse_args()
        title = args['title']
        q = f"SELECT id FROM games WHERE title LIKE '%{title}%'"
        result = engine.execute(sqlalchemy.text(q))
        game_ids = []
        for row in result:
            game_ids.append(row['id'])
        
        # 該当するゲームがなかった
        if not game_ids:
            return {
                'status': 404, 
                'message': f'game including {title} in title is not found'
            }, 404

        games = []
        for game_id in game_ids:
            games.append(Game().get(game_id)['game'])

        return {
            'status': 200,
            'message': 'OK',
            'games': games
        }

