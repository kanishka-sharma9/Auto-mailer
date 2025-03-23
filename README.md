# Auto-mailer

An agentic application built using Crewai and Langgraph to generate response drafts to all your emails from the last 5 days. This project leverages Groq and LiteLLM to provide LLM inferencing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Auto-mailer, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/kanishka-sharma9/Auto-mailer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Auto-mailer
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Go to the following [Google Cloud Console API page](https://console.cloud.google.com/apis/api/gmail.googleapis.com/) and download the credentials.
2. Add the credentials to the root directory named `credentials.json`.
3. Ensure you have your email credentials and access configured.
4. Run the application:
    ```sh
    python main.py
    ```
5. The system will analyze your inbox and generate draft responses for emails received in the last 5 days.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add your message here"
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
