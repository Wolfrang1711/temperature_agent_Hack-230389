# TemperatureX

## Project Description

The TemperatureX Web Application is a Flask-based Temperature Alert Agent built using Fetch.AI's uAgent library that provides a simple interface for users to input their desired location and temperature range and then displays real-time temperature status updates on the webpage, i.e., sends alert/notification to the user when the current temperature in their chosen location goes below the minimum or above the maximum threshold they've set. 

## How to Run the Project
Follow these steps to run the project:

1. Clone or download this repository to your local machine:

```bash
   git clone https://github.com/Wolfrang1711/hackAI_temp_agent.git
   ```

2. Open New Terminal in your VS Code and run this

```bash
   poetry install
   ```

3. Go to the shell by running 

```bash
   poetry shell
   ```
4. Then navigate to the src directory

    
```bash
   cd src
   ```
5. Then run the main file
   
```bash
   python main.py
   ```

## Special Considerations 

The application uses the uagents library for agent-based communication. Ensure that you have this library properly installed and configured in your project.
