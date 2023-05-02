from flask import Flask, render_template
from app.utils import file_opener


class FlaskView:

    def __init__(self, expected_route):
        self.app = Flask(__name__)
        self.routing_user(expected_route)
        self.app.run(debug=True, use_reloader=False, port=8080)

    def routing_user(self, expected_route):
        if expected_route == "players_sorted_by_name":
            self.app.add_url_rule("/", view_func=self.players_ordered_by_name)
        return

    def players_ordered_by_name(self):
        data = file_opener("players")
        del data["player_0"]
        data_sorted = sorted(data.items(), key=lambda player: player[1]['name'].lower())
        data_ready = {element[0]: element[1] for element in data_sorted}
        title = "Liste de tous les joueurs par ordre alphabétique"
        return render_template('players.html', data=[data_ready, title])




"""
-- liste de tous les joueurs par ordre alphabétique ; DONE
-- liste de tous les tournois ;
-- nom et dates d’un tournoi donné ;
-- liste des joueurs du tournoi par ordre alphabétique ;
-- liste de tous les tours du tournoi et de tous les matchs du tour.
"""