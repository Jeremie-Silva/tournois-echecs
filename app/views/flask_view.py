from flask import Flask, render_template
from app.utils import file_opener


class FlaskView:

    def __init__(self, expected_route, tournament_selected=""):
        self.app = Flask(__name__)
        self.tournament_selected = tournament_selected
        self.routing_user(expected_route)
        self.app.run(debug=True, use_reloader=False, port=8080)

    def routing_user(self, expected_route):
        if expected_route == "players_sorted_by_name":
            self.app.add_url_rule("/", view_func=self.players_list_sorted_by_name)
        elif expected_route == "tournaments_list":
            self.app.add_url_rule("/", view_func=self.tournaments_list)
        elif expected_route == "tournament_selected_name_date":
            self.app.add_url_rule("/", view_func=self.tournament_selected_name_date)
        elif expected_route == "tournament_players_list_sorted_by_name":
            self.app.add_url_rule("/", view_func=self.tournament_players_list_sorted_by_name)
        elif expected_route == "tournament_matchs_list":
            self.app.add_url_rule("/", view_func=self.tournament_matchs_list)
        else:
            return

    def players_list_sorted_by_name(self):
        data = file_opener("players")
        del data["player_0"]
        data_sorted = sorted(data.items(), key=lambda player: player[1]['name'].lower())
        data_reformat = {element[0]: element[1] for element in data_sorted}
        list_players = [value for key, value in data_reformat.items()]
        title = "Liste de tous les joueurs par ordre alphabétique"
        return render_template('players_list.html', data=[list_players, title])

    def tournaments_list(self):
        data = file_opener("tournaments")
        title = "Liste de tous les tournois"
        tournaments_list = [value["name"] for key, value in data.items()]
        return render_template('tournaments_list.html', data=[tournaments_list, title])

    def tournament_selected_name_date(self):
        data = file_opener("tournaments")
        title = f"Nom et date du tournoi : {self.tournament_selected}"
        tournament = {key: value for key, value in data.items() if value["name"] == self.tournament_selected}
        tournament_name_date = [value for key, value in tournament.items()]
        return render_template('tournament_name_date.html', data=[tournament_name_date, title])

    def tournament_players_list_sorted_by_name(self):
        data = file_opener("tournaments")
        title = f"Liste des joueurs du tournoi : {self.tournament_selected}"
        player_list = data[f"tournament_{self.tournament_selected}"]["players_list"]
        sorted_player_list = sorted(player_list, key=lambda player: player['name'].lower())
        return render_template('players_list.html', data=[sorted_player_list, title])

    def tournament_matchs_list(self):
        data = file_opener("tournaments")
        title = f"liste de tous les matchs du tournoi : {self.tournament_selected}"
        rounds_dict = {key: value for key, value in data[f"tournament_{self.tournament_selected}"].items() if "round_" in str(key)}
        return render_template('round_list.html', data=[rounds_dict, title])
