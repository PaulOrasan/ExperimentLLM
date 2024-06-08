# Application Documentation

The application supports experimentation with various Large Language Models on multiple datasets. It has three main components:
- The Data Viewer
- The Experiment Viewer
- The Model Interaction Viewer

## Data Viewer

The data viewer enables the user to load `Question and Answering` datasets with multiple splits (`train`, `test`).

The viewer offers custom progress loading and a full view of the dataset which can be made paginated.

The user can see data points, loading the `"Question"` and its corresponding `"Answer"`.

## Experiment Viewer

The experiment viewer enables the user to monitor ongoing experiments on test data samples. More, it allows the user to validate the outputs of the model and aid in the evaluation process.

The user is able to iterate through the test samples and see the output of the models which have been trained on the dataset.

The user can mark if the predictions are accurate and then save the validation.

On the bottom page, the user sees a live graphical plot of the accuracy of the models and the percentage of data samples which have been validated.

## The Chat Viewer

The Chat Viewer enables the user to interact with the trained models in a chat-bot fashion.

The viewer offers the possibility of loading each available model and storing the independent history of the conversations.

The user can type messages and have a conversation with the Deep Learning models.

### Backend

The API calls have been mocked to a custom, local implementation. The implementation can easily be translated into connecting to a remote backend server.

# Gradio Documentation

## Overview

Gradio is an open-source Python framework that simplifies the process of creating web-based user interfaces for machine learning models, data science workflows, and any kind of interactive applications. With Gradio, you can quickly develop web apps that allow users to interact with your models and algorithms through a user-friendly interface, without needing deep web development knowledge.

## Features

- **Ease of Use**: Build and share web applications with minimal code.
- **Interactivity**: Create interactive interfaces for various applications including image processing, text generation, and more.
- **Customizability**: Customize the appearance and functionality to suit your needs.
- **Integration**: Seamlessly integrate with popular machine learning libraries such as TensorFlow, PyTorch
     - Native integration with HuggingFace

## Authentication

Gradio provides several options for securing your web applications:
- **OAuth**: Integrate OAuth providers (like Google, GitHub) to manage user authentication.
- **Basic Authentication**: Implement simple username and password protection.
- **API Key**: Use API keys to control access to your application.
- **Custom Authentication**: Implement your own custom authentication logic to suit specific requirements.

## State

Gradio supports maintaining state in your applications, which can be useful for storing information across different sessions or within a single session.

### Global State
Global state in Gradio refers to data that is shared across all users and sessions. This is useful for storing shared resources or settings that need to be accessible application-wide.

- **Implementation**: Global state can be managed using global variables within the app or external databases.
- **Use Cases**: Shared counters, configuration settings, or models loaded into memory.

### Session State
Session state refers to data that is specific to a user's session. This is useful for tracking user-specific information, such as preferences or ongoing interactions within the app.

- **Implementation**: Gradio provides session state management by using session-specific variables.
- **Use Cases**: User progress, temporary data storage, or personalized settings.

## Hooks

Gradio provides hooks that allow you to execute custom code at various points in the app lifecycle. These hooks can be used to perform actions such as initializing resources, cleaning up resources, or modifying inputs and outputs dynamically.

- **Event Hooks**: Trigger actions before or after certain events, such as input submission or output rendering.
- **Custom Logic**: Implement custom logic to handle specific scenarios or enhance the user experience.

## Layout

Gradio's layout system allows you to design complex and responsive user interfaces. You can arrange components such as buttons, sliders, text boxes, and more in various layouts to create intuitive and user-friendly applications.

- **Rows and Columns**: Organize components using grids and columns to create structured layouts.
- **Tabs**: Use tabs to group related components and improve navigation.
- **Custom Layouts**: Design custom layouts using HTML, CSS and JS for more advanced use cases.
- **Component Store**: Use public components made available by users 

## Theme Builder

Gradio's theme builder enables you to customize the appearance of your web applications to match your brand or personal preferences. You can modify colors, fonts, and other visual elements to create a cohesive and attractive design.

- **Preset Themes**: Choose from a variety of preset themes to quickly change the look and feel of your app.
- **Custom Themes**: Create your own themes by specifying custom CSS styles and incorporating them into your app.
