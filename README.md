# L2Vista Chatbot

The L2Vista Chatbot is an AI-powered engine designed to enhance user interactions with the L2Vista platform.
By utilizing natural language processing (NLP) capabilities, the chatbot aims to provide users with an intuitive and conversational way to interact with the L2Vista platform.

## Getting Started

To run the L2Vista Chatbot, follow these steps:

1. Install the required dependencies using `pip`:

   ```bash
   $ pip install -r requirements.txt
   ```

2. Run the chatbot using `gunicorn`:

   ```bash
   $ gunicorn -w 1 -b 0.0.0.0:30327 flask_server:app
   ```

## Usage

Once the chatbot is up and running, you can interact with it using HTTP POST requests. Here's an example using `curl`:

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"human_input":"I would like to see transactions using the CCIP protocol that are heading to Mode."}' http://localhost:30327/chat
```

This example demonstrates how to send a user input to the chatbot for processing. The chatbot's response will include AI-generated output that aims to assist the user's request.

## Example Response

The chatbot's response will typically include the AI-generated output, as well as a parsed version of the user input for further processing. Here's an example response:

```json
{
  "ai_output": "I apologize for the confusion. Let me gather the transactions using the CCIP protocol that are heading to Mode for you. Please wait a moment while I retrieve the information.",
  "parsed": ["null", "mode", "ccip", "null"]
}
```
