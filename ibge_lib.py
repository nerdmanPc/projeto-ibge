from unicodedata import name
import urllib3
import json

# Runs query, check for erors and load response -> untested
def query_ibge(query_url, request_fn):
    response = request_fn(query_url)
    if response.status != 200:
        raise Exception(f'ERRO DE CONSULTA {response.status}, URL: {query_url}')
    return json.loads(response.data)

AGGR_URL = 'https://servicodados.ibge.gov.br/api/v3/agregados'

# Returns the URL for the 'aggregates' query. Can be filtered by subject.
def aggregates_url(subject=None):
    if subject is None:
        return AGGR_URL
    else:
        return AGGR_URL + f'?assunto={subject}'

# Returns the URL for the 'locations by aggregate' query 
def locations_url(aggregate, levels):
    levels_str = '|'.join(levels)
    return AGGR_URL + f'/{aggregate}/localidades/{levels_str}'

# Returns the URL for the 'metadata by aggregate' query
def metadata_url(aggregate):
    return AGGR_URL + f'/{aggregate}/metadados'

# Returns the URL for the 'periods by aggregate' query
def periods_url(aggregate):
    return AGGR_URL + f'/{aggregate}/periodos'

# Returns the URL for the 'variables by aggregate' query
def all_variables_url(aggregate, locations='BR'):
    return AGGR_URL + f'/{aggregate}/variaveis/all?localidades={locations}'

def variables_url(aggregate, variables, classifications=None, locations=['BR'], periods=['-6']):
    periods_str = '|'.join(periods)
    variables_str = '|'.join(variables)
    locations_str = '|'.join(locations)
    classifications_fmt = ''
    if not(classifications is None):
        classifications_str = '|'.join(classifications)
        classifications_fmt = f'&classificacao={classifications_str}'
    return AGGR_URL + f'/{aggregate}/periodos/{periods_str}/variaveis/{variables_str}?localidades={locations_str}{classifications_fmt}'

def filter_researches(reseaches, keyword: str):
    filter_fn = lambda x: x['nome'].casefold().rfind(keyword.casefold()) != -1
    filter_it = filter(filter_fn, reseaches)
    return list(filter_it)

def has_keywords(text: str, kewwords: str):
    text = text.casefold()
    keywords = kewwords.casefold()
    kw_list = keywords.split()
    for kw in kw_list:
        if text.find(kw) == -1:
            return False
    return True

def filter_aggregates(research, keywords: str):
    aggregates = research['agregados']
    filter_fn = lambda aggr: has_keywords(aggr['nome'], keywords) 
    return list(filter(filter_fn, aggregates))

def get_var_ids(variables):
    format_fn = lambda x: f"{ x['id'] }: { x['variavel'] }"
    return '\n'.join( map(format_fn, variables) )