document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("submit-city")
    .addEventListener("click", function (event) {
      let city = document.getElementById("city-search").value;
      // Call your Django backend instead of the weather API directly
      fetch("/api/get_weather/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ city: city }),
      })
        .then((response) => response.json())
        .then((weatherData) => {
          if (weatherData.error) {
            displayError(weatherData.error);
            return;
          }
          let context = {
            city: city,
            temperature: Math.round(weatherData.main.temp - 273),
            description: weatherData.weather[0].description,
            main: weatherData.weather[0].main,
            humidity: weatherData.main.humidity,
            wind_speed: weatherData.wind.speed,
            countrycode: weatherData.sys.country,
            timezone: weatherData.timezone / 3600,
          };
          let countryCode = context.countrycode;
          let apiKey2 = "bdc_75be7cba49a640f4802475b138167479";
          let codeUrl = `https://api-bdc.net/data/country-info?code=${countryCode}&localityLanguage=en&key=${apiKey2}`;

          fetch(codeUrl)
            .then((response) => response.json())
            .then((data) => {
              context.countryName = data.name; // Add the country name to the context
              displayWeather(context);
              console.log(context.main);
              changeBackgroundImage(imageUrl, context);
            })
            .catch((error) => {
              displayError("Failed to fetch country information");
            });
        })

        .catch((error) => {
          displayError("City not found");
        });

  

      function getWindDirection(wind_speed) {
        let directions = [
          "N",
          "NNE",
          "NE",
          "ENE",
          "E",
          "ESE",
          "SE",
          "SSE",
          "S",
          "SSW",
          "SW",
          "WSW",
          "W",
          "WNW",
          "NW",
          "NNW",
        ];
        let index = Math.round(wind_speed / 22.5 + 0.5);
        return directions[index % 16];
      }

      function displayWeather(context) {
        let windDirection = getWindDirection(context.wind_speed);
        // Update the DOM with the weather information
        document.getElementById("weather").textContent = context.description;
        document.getElementById(
          "temperature"
        ).textContent = `${context.temperature}°C`;
        document.getElementById(
          "city-name"
        ).textContent = ` ${context.countryName}, ${context.city}`;
        document.getElementById(
          "wind"
        ).textContent = `${windDirection}, ${context.wind_speed} km/h`;
      }

      const apIKey = "49S8sYPnL8EJ6Q3vS66MkRg41Ls8cvUCJrJLv2rG5MWdC64JoodbgJRS";
      const apiUrl = `https://api.pexels.com/v1/search?query=${city}&per_page=1`;
      async function fetchImage() {
        try {
          const response = await fetch(apiUrl, {
            headers: { Authorization: apIKey },
          });
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          const data = await response.json();
          const imageUrl = data.photos[0].src.original;
          document.getElementById("background-image").src = imageUrl;
        } catch (error) {
          console.error("Error fetching image:", error);
        }
      }
      fetchImage();

      document.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
          displayWeather(context)
          console.log("You have clicked enter")
        }
      })
    });

  function displayError(message) {
    // Update the DOM with the error message
    document.getElementById("weatherResult").innerHTML = `<p>${message}</p>`;
  }

  function displayTime() {
    let time = new Date();
    let hour = time.getHours();
    let minutes = time.getMinutes();

    // Format hours and minutes to always have two digits
    if (hour < 10) {
      hour = `0${hour}`;
    }
    if (minutes < 10) {
      minutes = `0${minutes}`;
    }

    // Set the textContent of the element with id 'span2'
    document.getElementById("span2").textContent = `${hour}:${minutes}`;
  }

  // Optionally, you can call the function to test it
  displayTime();

  function displayDate() {
    let date = new Date();
    let day = date.getDay();
    let month = date.getMonth();
    let year = date.getFullYear();

    const monthNames = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    const dayNames = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];

    document.getElementById("span1").textContent = `${
      dayNames[date.getDay()]
    }, ${monthNames[month]}, ${day + 8}`;

    document.querySelector(".date").textContent = `${
      dayNames[date.getDay()]
    }, ${monthNames[month]}`;
  }



  displayDate();


  setInterval(displayTime, 1000);

});
