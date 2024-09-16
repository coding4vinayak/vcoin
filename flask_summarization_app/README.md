

# Summarization App

This Flask application provides summarization capabilities for text, audio, and images. Users can interact with a web interface to summarize different types of input.

## Project Structure

- **`app.py`**: Main Flask application file.
- **`static/`**: Contains static files such as CSS and JavaScript.
  - **`styles.css`**: Stylesheet for the application.
  - **`scripts.js`**: JavaScript file for additional functionality.
- **`templates/`**: Contains HTML templates for different views.
  - **`index.html`**: Homepage template.
  - **`text_summarization.html`**: Template for text summarization.
  - **`audio_summarization.html`**: Template for audio summarization.
  - **`image_summarization.html`**: Template for image summarization.
- **`summarizer/`**: Contains Python modules for different types of summarization.
  - **`__init__.py`**: Initialization file for the summarizer package.
  - **`text_summarizer.py`**: Module for text summarization using a transformer model.
  - **`audio_summarizer.py`**: Module for audio summarization, including speech-to-text.
  - **`image_summarizer.py`**: Module for image summarization using image captioning.
- **`requirements.txt`**: Lists the required Python packages.
- **`README.md`**: This file.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/flask_summarization_app.git
   cd flask_summarization_app
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**

   ```bash
   python app.py
   ```

5. **Access the Application**

   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to start using the application.

## Features

- **Text Summarization**: Enter text and receive a summarized version.
- **Audio Summarization**: Upload an audio file to get a summarized text.
- **Image Summarization**: Upload an image and receive a description of the contents.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created with ❤️ by Coding4Vinayak