from flask_restful import Resource,reqparse
import sqlalchemy
import os
from .utils import get_plural

engine = sqlalchemy.create_engine(
    os.environ['GALOOK_DATABASE_URL']
)
game_columns = ('id', 'brand', 'category', 'story', 'subgenre', 'title', 'url', 'writer')

class Game(Resource):

    def get_tags(self, game_id, column):
        column_plural = get_plural(column)
        q = f"SELECT {column}_name FROM game_{column_plural} WHERE game_id = {game_id}"
        result = engine.execute(q)
        tags = []
        for row in result:
            tags.append(row[f'{column}_name'])
        return ','.join(tags)

    def get(self, game_id):
        q = f"SELECT * FROM games WHERE id = {game_id}"
        result = engine.execute(q)
        game = result.fetchone()

        # 該当するゲームがなかった
        if not game:
            return {
                'status': 404, 
                'message': f'game id {game_id} is not found'
            }, 404

        game = dict(game)
        game['category'] = self.get_tags(game_id, 'category')
        game['subgenre'] = self.get_tags(game_id, 'subgenre')
        game['writer'] = self.get_tags(game_id, 'writer')

        return {
            'status': 200,
            'message': 'OK',
            'game': {column: game[column] for column in game_columns}
        }