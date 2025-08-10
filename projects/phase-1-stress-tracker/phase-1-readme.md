# Stress Tracker

A simple Python application for tracking and visualizing personal stress levels over time.

## Project Overview

This mini-project is part of a Python learning journey (Days 16-20) focused on building practical data tracking and visualization skills. The stress tracker helps users monitor their daily stress patterns and visualize trends to better understand their well-being.

## Features

- **User Data Management**: Store personal information including name, heart rate, and stress levels
- **Data Persistence**: Save tracking data to files for long-term storage
- **Trend Visualization**: Generate charts and graphs using Matplotlib to visualize stress patterns
- **Input Validation**: Robust data validation to ensure accurate entries
- **Daily Refinements**: Continuously improved with 12-minute daily coding sessions

## Technical Requirements

- **Python 3.7+**
- **Required Libraries**:
  - `matplotlib` - for data visualization
  - `pandas` - for data manipulation
  - `numpy` - for array management
  - `datetime` - for timestamp management
  - `json` - for string to object and object to string management

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd stress-tracker
   ```

2. Install required dependencies:
   ```bash
   pip install matplotlib pandas numpy
   ```

## Usage

1. Run the main application:

   ```bash
   python stress_tracker.py
   ```

2. Follow the prompts to:

   - Enter your name
   - Record your current heart rate
   - Rate your stress level (1-10 scale)

3. View your stress trends through automatically generated charts

## Data Structure

This information would 100% be better utilized and managed in a relational database.
the only reason I am using a file is for writing and reading from a file for the pure operations.
Database work will come in a future project.

The application stores data using Python dictionaries with the following structure:

```python
[
    {
        "name": "John",
        "entries": [
            {
                "date": "2024-01-15",
                "heart_rate": 72,
                "stress_level": 4
            }
        ]
    }
]
```

## Visualization Features

- **Stress Trends**: Line charts showing stress levels over time
- **Heart Rate Correlation**: Scatter plots comparing heart rate vs stress levels
- **Weekly Summaries**: Bar charts for weekly stress averages
- **Statistical Insights**: Mean, standard deviation, and trend analysis

## Learning Objectives

- [x] Dictionary-based data storage
- [x] File I/O operations
- [x] Data visualization with Matplotlib
- [x] Input validation and error handling
- [x] Code refinement and iteration

Stretch Goals for this specific project

- [ ] Export functionality (CSV/PDF)

## Daily Development Cycle

Each day includes a focused 12-minute refinement session:

- **Day 16**: Core Functionality and File Structure
- **Day 17**: Obtain user input, validation, log entries
- **Day 18**: Use pandas and matplotlib to plot and summarize data
- **Day 19**: Delete data if user requests
- **Day 20**: Code optimization and documentation

## Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to:

- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Share your own stress tracking insights

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

Built as part of a structured Python learning curriculum focusing on practical application development and data visualization skills.

---

_"Taking care of your mental health is just as important as taking care of your physical health." - Track, visualize, and improve your well-being one data point at a time._
