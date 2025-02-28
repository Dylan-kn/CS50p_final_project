import sys
import csv
import random


def main():
    cities = read_csv()
    game = questions(cities)
    result = calculate_city_scores(game)
    print(f"\nPack your bags and get ready. You are moving to...........{result}!!! :) \n")

def read_csv():
    try:
        #open csv file
        with open('world_cities_project.csv', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        sys.exit("File not found")

def input_validation(s):
    while True:
        answer = input(s).strip().lower()
        if answer in ['yes', 'no', 'y', 'n']:
            return answer
        else:
            print("\nPlease provide a 'yes' or 'no' answer")


def questions(cities):
        #check if there is data in cities
        if not cities:
            raise ValueError("Cannot load data")

        try:
            #make every city in cities scores initialized
            city_scores = {city['City']: 0 for city in cities}

            #initial inquiry
            answer = input_validation("Are you ready to play the game? ")
            if answer == 'no' or answer == 'n':
                print("Alright fine. Whatever... See ya! ")
                sys.exit("Exited game")

            #question number 1
            answer = input_validation("\nYou find yourself in a new city. You are here to scout new places to live.\n"
                        "No more dreaming, no more thinking - on a mission to find where your life will take you next.\n"
                        "You exit your hotel, the morning fog is thick, new scents, new sounds. The concierge mentioned the city's world-class train network.\n"
                        "Fast, reliable, used by countless people every day. The station looms ahead.\n"
                        "Is this the kind of life you crave? Shoulder to shoulder, moving through the city as one?\n"
                        "Or do you seek the freedom of your own wheels, free of timetables and tracks? Do you hop on the train? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Public_Transport']) #convert to integer for further use

            #question number 2
            answer = input_validation("\nThe city vibrates with energy. You have been walking all morning and your legs are getting tired.\n"
                        "You're exhausted and craving some reprieve. Where's the quiet?\n"
                        "You check your map and find a sprawling park with lake and all, on the outskirts of the city.\n"
                        "Above all else, you are craving some calm, some quiet. But the city has other temptations... quiet cafès, calm museums.\n"
                        "Do you need the element of nature woven into your life?\n"
                        "Or can you thrive without? Do you make your way to the lake? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Nature_Access'])

            #question number 3
            answer = input_validation("\nNightfall has come. You just had dinner and are walking back to your hotel.\n"
                        "Past lively bars, open mic cafès and the occasional dark alleyway you wish you hadn't turned down.\n"
                        "As you walk you notice the lively nature of the city, that subtle unpredictability.\n"
                        "Some might find comfort in structure, in a sense of order. Others likely crave a thrill, a feeling of the unexpected.\n"
                        "You ask yourself, do you prefer a city where you feel completely safe at all hours? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Safety'])

            #question number 4
            answer = input_validation("\nYou are enjoying yourself. You are taking a lunch break, daydreaming of what it might be like to live here.\n"
                        "Routines, favorite spots, endless curiousity. Then the bill arrives.\n"
                        "Uff, not the cheapest. Certainly more than your last city. You look up at the fancy apartments.\n"
                        "High-end clothing stores, great restaurants. Is the price of living worth it? Maybe a city\n"
                        "where your money stretches further is the wiser choice.\n"
                        "Do you prefer a city with lower cost of living? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Cost_of_Living'])

            #question number 5
            answer = input_validation("\nIt is the next day. You slept well, although the new bed and bustling city noises kept you up for a while.\n"
                        "You make your way to a new part of the city. An active area, full of commuters on their way to work.\n"
                        "Tourists admiring the lights, children running around. You stop and look at the\n"
                        "seemingly endless stream of faces. Seems like there's always something happening.\n"
                        "You feel alive and sharp...or is it overwhelming?\n"
                        "You ask yourself, do you crave the buzz of a densely packed city? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Density_Crowds'])

            #question number 6
            answer = input_validation("\nThe sun has set, the city transforms. Neon lights light up the streets, music all around.\n"
                        "Bars, theaters, cafès, clubs, rooftop parties, jazz clubs, people...the night is alive.\n"
                        "You have a decision to make. One option is to pursue the rhythm of the night, seeing where it leads.\n"
                        "The other is to seek the quieter comforts of your hotel room, perhaps a nightcap at the bar.\n"
                        "Do you go out tonight, eager to see what happens? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Nightlife_Entertainment'])

            #question number 7
            answer = input_validation("\nA new day has begun. You're feeling rested and at peace. So far the trip has been all you could have wanted.\n"
                        "But that's all well and good. You remember what you came here for. You are not just visitng, you are scouting.\n"
                        "Looking for a place to call home, to build a career and a life.\n"
                        "You pass vibrant co-working spaces, offices and shops. For some, a thriving job market is paramount.\n"
                        "For others it holds less meaning. Do you seek a place with a strong job market? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Job_Market'])

            #question number 8
            answer = input_validation("\nAll this thinking has got you craving some refreshments. You stop at a cafè in hopes of ordering a drink.\n"
                        "The signs aren't in English, nor does the barista seem to understand you.\n"
                        "He smiles and reassures you in that friendly, internationally recognizable way.\n"
                        "Some cities embrace English speakers, making life seamless. Elswhere you are excpected to adapt, adjust to the local language and culture.\n"
                        "Do you want a place where English is widely spoken? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['English_Friendly'])

            #question number 9
            answer = input_validation("\nYou managed to fumble your way into a coffee, and even somewhat enjoyed the struggle.\n"
                        "You step back outside and are struck by the intense heat of the day.\n"
                        "Some cities are temperate year round, offering smooth and consistent weather.\n"
                        "Others require a steadfast nature, whether it be to withstand bitter cold, intense heat, or endless rain.\n"
                        "Do you like a city known for good weather conditions? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Climate'])

            #question number 10
            answer = input_validation("\nAlas, you find some shade and think of your next move.\n"
                        "You have so many options. Museums, landmarks, theaters, art galleries and much more.\n"
                        "Does a city's cultural offering make you feel alive? Or is your mind elsewhere?\n"
                        "The question remains, do you long for cities with a plethora of cultural offerings? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Cultural_Attractions'])

            #question number 11
            answer = input_validation("\nAll this thinking has made you hungry. You smell the aromas of endless kitchens cooking, sizzling, frying, grilling\n"
                        "poaching, baking...Some cities are known for their culinary arts. High quality restaurants on every corner.\n"
                        "Other cities offer more simple, dependable meals.\n"
                        "Do you want a city with an ecelectic, thriving food scene? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Food_Scene'])

            #question number 12
            answer = input_validation("\nYour night has come to an end after a fantastic meal at the local restaurant. You decide to stroll back to the hotel.\n"
                        "Your flight back home leaves in the morning, so you are keen to get some sleep.\n"
                        "You are almost home when you notice something. An endless stream of garbage seems to line the streets.\n"
                        "Does this city recycle? Do people here care about eco-friendliness? You think about the fact that\n"
                        "some cities are filled with bike paths, rooftop gardens, and spotless streets. Others place less value\n"
                        "on sustainability. Do you? ")
            if answer == 'yes' or answer == 'y':
                for city in cities:
                    city_scores[city['City']] += int(city['Eco_Friendliness'])

        except EOFError:
            sys.exit("Exited game")

        return city_scores


def calculate_city_scores(city_scores):
    try:
        #determine highest scoring value
        highest_score = max(city_scores.values())

        #then get all cities with that highest scoring value
        perfect_city = []
        for city, score in city_scores.items():
            if score == highest_score:
                perfect_city.append(city)

        #choose a random city of the highest scoring, if there are multiple winners
        return random.choice(perfect_city)

    except TypeError:
        print("TypeError")
        return None
    except ValueError:
        print("ValueError")
        return None


if __name__ == '__main__':
    main()
