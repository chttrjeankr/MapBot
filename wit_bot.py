from wit import Wit
import config
import googleMapsApiModule
import logging

client = Wit(config.wit_token)
THRESHOLD_CONFIDENCE = 0.8


def get_response(classification, search_query=None):
    logging.debug(classification)
    logging.debug(search_query)
    if classification == "bye":
        return "Bye, I'll miss you."

    if classification == "greetings":
        return "Hi, I'm MapBot"

    functions_mapping = {
        "direction": googleMapsApiModule.direction,
        "timezone": googleMapsApiModule.timezone,
        "geocoding": googleMapsApiModule.geocoding,
        "mapsstatic": googleMapsApiModule.mapsstatic,
        "elevation": googleMapsApiModule.elevation,
        "places": googleMapsApiModule.places,
    }
    result = functions_mapping[classification](search_query)
    return result


while True:
    user_query = input("YOU: ")
    resp = client.message(user_query)
    entities = resp["entities"]
    classification = None

    intent = entities.get("intent")
    if intent:
        confidence = intent[0]["confidence"]
        if confidence > THRESHOLD_CONFIDENCE:
            classification = intent[0]["value"]

            location = entities.get("location")
            locations = []
            if location:
                for loc in location:
                    confidence = loc["confidence"]
                    if confidence > THRESHOLD_CONFIDENCE:
                        try:
                            locations.append(loc["resolved"]["values"][0]["name"])
                        except Exception:
                            locations.append(loc["value"])
            if classification == "places":
                query_text = resp["_text"]
                response = get_response(classification, query_text)
            elif classification == "direction":
                response = get_response(classification, locations)
            else:
                response = get_response(classification, locations[0])
            print(f"BOT: {response}")

        else:
            print("did_not_understand(...)")
            pass

    bye = entities.get("bye")
    if bye:
        confidence = bye[0]["confidence"]
        if confidence > THRESHOLD_CONFIDENCE:
            classification = "bye"
            response = get_response(classification)
            print(f"BOT: {response}")
            break
        else:
            print("did_not_understand(...)")
            pass

    greetings = entities.get("greetings")
    if greetings:
        confidence = greetings[0]["confidence"]
        if confidence > THRESHOLD_CONFIDENCE:
            classification = "greetings"
            response = get_response(classification)
            print(f"BOT: {response}")
        else:
            print("did_not_understand(...)")
            pass
