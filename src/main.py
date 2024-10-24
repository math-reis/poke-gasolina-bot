import os
import re
import tweepy
import random
from urllib.request import Request, urlopen
from dotenv import load_dotenv

####################################################################
######################## API AUTHENTICATION ########################
####################################################################

load_dotenv()

api_keys = os.getenv("api_keys")
api_keys_secret = os.getenv("api_keys_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
bearer_token = os.getenv("bearer_token")

auth = tweepy.OAuthHandler(api_keys, api_keys_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

client = tweepy.Client(bearer_token = bearer_token)

####################################################################
############################ GET TWEET #############################
####################################################################

def get_tweet():

    ufNumber = random.randint(1, 27)

    if ufNumber == 1:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/acre/rio-branco/68'
        uf = 'Rio Branco/AC'

    if ufNumber == 2:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/alagoas/maceio/1695'
        uf = 'Maceió/AL'

    if ufNumber == 3:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/amapa/macapa/301'
        uf = 'Macapá/AP'

    if ufNumber == 4:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/amazonas/manaus/112'
        uf = 'Manaus/AM'

    if ufNumber == 5:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/bahia/salvador/2161'
        uf = 'Salvador/BA'

    if ufNumber == 6:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/ceara/fortaleza/948'
        uf = 'Fortaleza/CE'

    if ufNumber == 7:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/espirito-santo/vitoria/3173'
        uf = 'Vitória/ES'

    if ufNumber == 8:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/goias/goiania/5412'
        uf = 'Goiânia/GO'

    if ufNumber == 9:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/maranhao/sao-luis/635'
        uf = 'São Luís/MA'

    if ufNumber == 10:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/mato-grosso/cuiaba/5214'
        uf = 'Cuiabá/MT'

    if ufNumber == 11:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/mato-grosso-do-sul/campo-grande/5118'
        uf = 'Campo Grande/MS'

    if ufNumber == 12:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/minas-gerais/belo-horizonte/2308'
        uf = 'Belo Horizonte/MG'

    if ufNumber == 13:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/para/belem/170'
        uf = 'Belém/PA'

    if ufNumber == 14:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/paraiba/joao-pessoa/1335'
        uf = 'João Pessoa/PB'

    if ufNumber == 15:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/parana/curitiba/4005'
        uf = 'Curitiba/PR'

    if ufNumber == 16:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/pernambuco/recife/1596'
        uf = 'Recife/PE'

    if ufNumber == 17:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/piaui/teresina/881'
        uf = 'Teresina/PI'

    if ufNumber == 18:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/rio-de-janeiro/rio-de-janeiro/3239'
        uf = 'Rio de Janeiro/RJ'

    if ufNumber == 19:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/rio-grande-do-norte/natal/1161'
        uf = 'Natal/RN'

    if ufNumber == 20:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/rio-grande-do-sul/porto-alegre/4927'
        uf = 'Porto Alegre/RS'

    if ufNumber == 21:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/rondonia/porto-velho/37'
        uf = 'Porto Velho/RO'

    if ufNumber == 22:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/roraima/boa-vista/139'
        uf = 'Boa Vista/RR'

    if ufNumber == 23:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/santa-catarina/florianopolis/4398'
        uf = 'Florianópolis/SC'

    if ufNumber == 24:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/sao-paulo/sao-paulo/3830'
        uf = 'São Paulo/SP'

    if ufNumber == 25:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/sergipe/aracaju/1753'
        uf = 'Aracaju/SE'

    if ufNumber == 26:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/tocantins/palmas/399'
        uf = 'Palmas/TO'

    if ufNumber == 27:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/distrito-federal/brasilia/5564'
        uf = 'Brasília/DF'

    else:
        url = 'https://precodoscombustiveis.com.br/pt-br/city/brasil/sao-paulo/sao-paulo/3830'
        uf = 'São Paulo/SP'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()

    html = webpage.decode("utf-8")

    partialPreco = re.findall('<span style="font-size:28px;">(.*)</span>', html)[0]

    preco = (partialPreco.replace('.', ','))[0:7]

    frase = f'O preço médio da gasolina em {uf} é {preco}'

    partialIdPokemon = partialPreco.replace('R$ ', '')

    idPokemon = (partialIdPokemon.replace('.', ''))[:3]

    intIdPokemon = int(idPokemon)

    if intIdPokemon > 898:
        idPokemon = str(idPokemon)[:2]

    urlImage = f'https://www.pokemon.com/br/pokedex/{idPokemon}'

    req = Request(urlImage, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()

    html = webpage.decode("utf-8")

    pokemonName = (re.findall('<h5>(.*)</h5>', html))[0]

    pokemon = f'{pokemonName} Nº {idPokemon}'

    tweet = f"{frase}\n\n{pokemon}\n\n{urlImage}"

    return tweet

####################################################################
##################### LATEST TWEETS VALIDATION #####################
####################################################################

tweet = get_tweet()

latest_tweet1 = api.user_timeline(screen_name = 'PokeGasolina', count = 1)[0]
latest_tweet2 = api.user_timeline(screen_name = 'PokeGasolina', count = 2)[1]
latest_tweet3 = api.user_timeline(screen_name = 'PokeGasolina', count = 3)[2]
latest_tweet4 = api.user_timeline(screen_name = 'PokeGasolina', count = 4)[3]
latest_tweet5 = api.user_timeline(screen_name = 'PokeGasolina', count = 5)[4]
latest_tweet6 = api.user_timeline(screen_name = 'PokeGasolina', count = 6)[5]

if tweet[0:40] == latest_tweet1.text[0:40] and tweet[0:40] == latest_tweet2.text[0:40] and tweet[0:40] == latest_tweet3.text[0:40] and tweet[0:40] == latest_tweet4.text[0:40] and tweet[0:40] == latest_tweet5.text[0:40] and tweet[0:40] == latest_tweet6.text[0:40]:
    tweet = get_tweet()
else:
    api.update_status(tweet)

####################################################################
########################## FOLLOW REQUEST ##########################
####################################################################

query = 'Gasolina Preço OR Combustível Preço OR Combustível'

response = client.search_recent_tweets(query, max_results = 10, tweet_fields = ['author_id'])

for tweet in response.data:
    list = [tweet.author_id]

    for author in list:
        api.create_friendship(user_id=author)
