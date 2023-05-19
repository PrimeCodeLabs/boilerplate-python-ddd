# Your Project Name

This is a boilerplate Python application using DDD (Domain-Driven Design) and various technologies such as CQRS, PostgreSQL, AWS EventBridge, AWS SQS, AWS Lambda, and Serverless Framework.

## Project Structure

The project follows a modular structure with separate directories for different layers and components.

- `src/application`: Contains the application layer responsible for handling use cases, commands, events, schemas, and services.
- `src/domain`: Contains the domain layer with domain models and repositories.
- `src/infrastructure`: Contains the infrastructure layer responsible for interacting with external services.
- `src/lambdas`: Contains the lambda functions for user operations.

## Getting Started

To get started with the project, follow these steps:

1. Install the required dependencies using `pip`: pip install -r requirements.txt

2. Configure the AWS credentials and other environment variables.

3. Deploy the application using Serverless Framework: serverless deploy

## Testing

The project includes unit tests for different components. To run the tests, use the following command: python -m unittest discover tests

## License

This project is licensed under the [MIT License](LICENSE).
