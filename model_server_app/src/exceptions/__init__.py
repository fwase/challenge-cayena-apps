class NotFoundModelException(Exception):
    def __init__(self, model_name):
        self.message = f"Not found model: {model_name}"

class InconsistencyFeaturesException(Exception):
    def __init__(self):
        self.message = f"Maybe features was empty or not match features size with model"
