import urllib3
import json

def query_ibge(query_url, request_fn):
    response = request_fn(query_url)
    if response.status != 200:
        raise f'ERRO {response.status}'
    return json.loads(response.data)

AGGR_URL = 'https://servicodados.ibge.gov.br/api/v3/agregados'

def aggregates_url(subject=None):
    if subject is None:
        return AGGR_URL
    else:
        return AGGR_URL + f'?assunto={subject}'

def locations_url(aggregate, levels):
    levels_str = '|'.join(levels)
    return AGGR_URL + f'/{aggregate}/localidades/{levels_str}'

def metadata_url(aggregate):
    return AGGR_URL + f'/{aggregate}/metadados'

def periods_url(aggregate):
    return AGGR_URL + f'/{aggregate}/periodos'

def all_variables_url(aggregate, locations='BR'):
    return AGGR_URL + f'/{aggregate}/variaveis/all?localidades={locations}'

def specific_variables_url(aggregate, variables, locations=['BR'], periods=['-6'], classifications=None):
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

def filter_aggregates(researches, keyword: str):
    aggregates = []
    for research in researches:
        aggregates.extend(research['agregados'])
    filter_fn = lambda x: x['nome'].casefold().rfind(keyword.casefold()) != -1
    filter_it = filter(filter_fn, aggregates)
    return list(filter_it)