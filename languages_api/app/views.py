from app import app
from .models import Language
from .wording import (
    invalid_route_error_message,
    language_not_found,
)
from sqlalchemy import func
import json



@app.route('/countries/<language_name>', methods=['GET'])
def get_countries(language_name):
  language_results = Language.query.filter(func.lower(Language.name)==func.lower(language_name)).first()
  if language_results == None:
      return json.dumps(language_not_found)
  countries = []
  for country in language_results.country_languages:
      countries.append(country.name)
  results = {language_name: countries}
  return json.dumps(results, indent = 4)

@app.errorhandler(404)
def handle_bad_request(e):
    return json.dumps(invalid_route_error_message)