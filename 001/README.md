# 001 - Interactive Console Application

This is a simple interactive console application that demonstrates basic input/output handling with error management.

## Features

- Continuously prompts user for input
- Processes user input and displays responses
- Handles keyboard interrupts gracefully
- Includes error handling for unexpected exceptions

## How to Use

1. Run the script
2. Enter input when prompted
3. View responses from the application
4. Press Ctrl+C to exit gracefully

## Code Structure

The application consists of:
- A main loop that continuously accepts user input
- Exception handling for KeyboardInterrupt and general exceptions
- Input processing and response generation
- Graceful exit handling when user interrupts the program

## Error Handling

The application handles:
- KeyboardInterrupt (Ctrl+C) - exits gracefully with "Goodbye!" message
- General exceptions - displays error messages without crashing
