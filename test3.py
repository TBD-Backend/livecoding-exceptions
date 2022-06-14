from services.DogAPI import dog_api, DogAPIError

facts = None

try:
    facts = dog_api.get_facts(10)
except DogAPIError:
    print("Could not make request")


print(facts)
