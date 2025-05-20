# WeatherApp

A simple Django-based weather application.

## Features

- Displays weather information for a given location.
- User-friendly interface.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root and add your API keys:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

Visit `http://127.0.0.1:8000/` in your browser.

## License

MIT License
