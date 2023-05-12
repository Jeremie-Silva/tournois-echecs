from flask import Flask, render_template
from app.utils import file_opener


class FlaskView:
    """The web view with Flask"""

    def __init__(self, expected_route: str, tournament_selected="Championnat de France") -> None:
        """The builder needs a specified route and optionally a tournament name. It creates the Flask application,
        defines the final route using another method and launches the web view on port 8080"""
        self.app: object = Flask(__name__)
        self.tournament_selected: str = tournament_selected
        self.routing_user(expected_route)
        self.app.run(debug=False, use_reloader=False, port=8080)

    def routing_user(self, expected_route: str) -> None:
        """The method needs a specified route and will associate the base url to the right view,
        which will be calculated by another method, according to the expected route"""
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

    def players_list_sorted_by_name(self) -> str:
        """The method does not need any parameters, it retrieves the data,
        applies the processing to obtain the list of all players sorted alphabetically by name,
        it will return the correct template associated with the processed data"""
        data: dict = file_opener("players")
        del data["player_0"]
        data_sorted: list = sorted(data.items(), key=lambda player: player[1]['name'].lower())
        data_reformat: dict = {element[0]: element[1] for element in data_sorted}
        list_players: list = [value for key, value in data_reformat.items()]
        title: str = "Liste de tous les joueurs par ordre alphabétique"
        return render_template('players_list.html', data=[list_players, title])

    def tournaments_list(self) -> str:
        """The method doesn't need any parameters, it retrieves the data,
        applies the processing to get the list of all the tournaments,
        it will return the right template associated to the processed data"""
        data: dict = file_opener("tournaments")
        title: str = "Liste de tous les tournois"
        tournaments_list: list = [value["name"] for key, value in data.items()]
        return render_template('tournaments_list.html', data=[tournaments_list, title])

    def tournament_selected_name_date(self) -> str:
        """The method does not need parameters, it retrieves the data,
        applies the processing to obtain a tournament selected by its name,
        it will return the correct template associated with the processed data"""
        data: dict = file_opener("tournaments")
        title: str = f"Nom et date du tournoi : {self.tournament_selected}"
        tournament: dict = {key: value for key, value in data.items() if value["name"] == self.tournament_selected}
        tournament_name_date: list = [value for key, value in tournament.items()]
        return render_template('tournament_name_date.html', data=[tournament_name_date, title])

    def tournament_players_list_sorted_by_name(self) -> str:
        """The method does not need any parameters, it retrieves the data,
        applies the processing to obtain the list of players sorted by name,
        of a tournament selected by its name,
        it will return the correct template associated with the processed data,
        or an error template if the tournament does not exist"""
        data: dict = file_opener("tournaments")
        title: str = f"Liste des joueurs du tournoi : {self.tournament_selected}"
        try:
            player_list: list = data[f"tournament_{self.tournament_selected}"]["players_list"]
            sorted_player_list: list = sorted(player_list, key=lambda player: player['name'].lower())
        except KeyError:
            return render_template('error.html', data=[self.tournament_selected])
        return render_template('players_list.html', data=[sorted_player_list, title])

    def tournament_matchs_list(self) -> str:
        """The method does not need any parameters, it retrieves the data,
        applies the processing to obtain the list of all the matches of a tournament selected by its name,
        it will thus return the right template associated with the processed data
        or an error template if the tournament does not exist"""
        data: dict = file_opener("tournaments")
        title: str = f"liste de tous les matchs du tournoi : {self.tournament_selected}"
        try:
            rounds_dict: dict = {key: value for key, value in data[f"tournament_{self.tournament_selected}"].items()
                                 if "round_" in str(key)}
        except KeyError:
            return render_template('error.html', data=[self.tournament_selected])
        return render_template('round_list.html', data=[rounds_dict, title])
