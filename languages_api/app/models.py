from .config import db, marshmallow

official_languages = db.Table("official_languages",
  db.Column('country_id', db.Integer, db.ForeignKey('country.country_id')),
  db.Column('language_id', db.Integer, db.ForeignKey('language.language_id'))
)

  
# Countries Model
class Country(db.Model):
  country_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  official_langs = db.relationship('Language', secondary=official_languages, backref=db.backref('country_languages', lazy='dynamic'))


class Language(db.Model):
  language_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))


def map_language_to_country(countries_instance, languages_instance, mapper):
  for country in countries_instance:
      languages = mapper[country.name]
      for language in languages:
          language = Language.query.filter_by(name=language).first()
          language.country_languages.append(country)
          db.session.commit()
