class ChessClub:
    def __init__(self, national_id:str):
        self.national_id = self._validate_national_id(national_id)

    def _validate_national_id(self, national_id:str):
        if (
            national_id[0].isalpha() and 
            national_id[1].isalpha() and 
            national_id[2].isnumeric() and
            national_id[3].isnumeric() and
            national_id[4].isnumeric() and
            national_id[5].isnumeric() and
            national_id[6].isnumeric() and
            len(national_id) == 7
        ):
            return national_id
        else:
            return None
