# Bike to Brew

:bike: :arrow_right: :beer:

Bike to Brew was created to unite hobbies of biking enthusiasts and beer drinking connoisseurs. Promoting an eco-friendly way of travel with the rewards of a nice cold beverage. This was initially created as a fun project in Anahiem, CA and has become so relevant since moving to Boulder, CO. 

Bike to Brew is an API that returns nearby breweries from [Open Brewery API](https://www.openbrewerydb.org/) and respective biking distance from [Google Maps - Directions API](https://developers.google.com/maps/documentation/directions/get-directions#maps_http_directions_boston_concord_waypoints-txt) based on IP location via [Free Geolocation API](https://ipstack.com/) 

### Requirements
1. Create an account at [ipstack](https://ipstack.com/) to obtain an access key to use the API

2. Create a account for [Google Developers](https://developers.google.com/) and follow the [instructions](https://developers.google.com/maps/documentation/directions/get-directions#maps_http_directions_boston_concord_waypoints-txt) to enable your access key and Directions API usage. 

Add these to your .env file. A .env.example has been provided for you

## Installation

```python
# Clone this repository to your machine
git clone https://github.com/lamrosanna/bike2brew-flask
# Create a Docker Image
docker build -t bike2brew .
# Run the container 
docker run --publish 3000:3000 bike2brew
```

## Usage
Once the container is running, the app will respond with a JSON file with/without rideTime and distance to brewery. Distance and rideTime values are contingent on a Google Developer API key. The breweries returned are already sorted by shortest distance from your coordinates. 

```
# Example Responses
[
  {
    "brewery_type": "regional",
    "distance": "0.9 mi",
    "name": "Avery Brewing Co",
    "phone": null,
    "postal_code": "80301-3242",
    "rideTime": "5 mins",
    "state": "Colorado",
    "street": "4910 Nautilus Ct N",
    "website_url": null
  },
  {
    "brewery_type": "micro",
    "distance": "4.4 mi",
    "name": "Wild Woods Brewery",
    "phone": "3034841465",
    "postal_code": "80301-2724",
    "rideTime": "24 mins",
    "state": "Colorado",
    "street": "5460 Conestoga Ct",
    "website_url": "http://www.wildwoodsbrewery.com"
  }
]
```

## Contributing
Due to the costs of attributed to using Google Maps API, I hesitate to continue building this out further :see_no_evil: However please feel free to let me know about any features that you would to see added. Cheers! :beers:


## License
[MIT](https://choosealicense.com/licenses/mit/)