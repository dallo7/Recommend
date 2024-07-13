# Car Recommendation Tool

## For Dash.Plotly Community

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-v2-orange)](https://dash.plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-orange.svg)](https://scikit-learn.org/stable/)
[![Made with ML](https://img.shields.io/badge/Made%20with-ML-red)](https://github.com/madewithml)
[![Recommendation Engine](https://img.shields.io/badge/Type-Recommendation%20Engine-brightgreen)](https://en.wikipedia.org/wiki/Recommender_system)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)                                                                                                    

This Dash application provides car recommendations based on various algorithms including popularity-based, content-based, and ensemble methods. It also includes a basic login system and integrates with an STK (Safaricom Toolkit) push service for purchasing recommended cars.

App hosted on render.com https://recommend-ofiw.onrender.com/  (when you click the link give it at least a minute for the service to restart) 

*** Integrated Mobile money (Safaricom's STK push)                                        
  

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Models & Data](#models--data)
- [Contributing](#contributing)

## Project Overview

**Purpose:** The Car Recommendation Tool offers personalized car recommendations to users using a variety of recommendation algorithms. It also facilitates seamless purchasing through STK push for Kenyan users.

**Target Users:**

- **Car Buyers:**  Can get personalized car recommendations based on their preferences or popular trends.
- **Car Dealerships:** Can use the tool to showcase their inventory and potentially increase sales.

## Features

- **Multiple Recommendation Engines:**
    - **Popularity-Based:** Recommends cars based on overall popularity.
    - **Content-Based:** Recommends cars based on similarity to user-selected or viewed cars.
    - **Ensemble:** Combines popularity and content-based approaches for more tailored suggestions.
- **Interactive UI:**
    - Car display with images and descriptions.
    - "Add to Cart" and "Remove from Cart" functionality.
    - Display of recommended cars.
    - "More Info" button with detailed tooltips.
- **STK Push Integration:** Facilitates payments for recommended cars using Safaricom's STK push service.
- **Login System:** Basic authentication for user access.


## Technologies

- **Dash:** Python framework for building web applications.
- **Dash Bootstrap Components (dbc):** For styling and layout.
- **BeautifulSoup4 (bs4):** For parsing HTML and handling image data.
- **Recommendation Algorithms:**
    - Popularity-based
    - Content-based
    - Ensemble (Hybrid)
- **STK Push Implementation:** Custom module (`stkPush.py`) for handling STK transactions.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install Dependencies:

    ```Bash
    pip install -r requirements.txt
    ```
3.  Run the App:
    ```Bash                                                                                                                        
    python app.py
    The app should be accessible at http://127.0.0.1:8050/
    ```          
4. Usage
* Access the App: Open your web browser and navigate to the app's URL.
* Login: Enter your credentials (or use the defaults).
* Browse Cars: View the available cars and their recommendations.
* Add/Remove Cars: Add or remove cars from your cart.
* Purchase: Enter your Safaricom phone number and click "Buy" to initiate an STK push transaction.

5. File Structure
* app.py: Main Dash application code.
* popularity.py: Module for popularity-based recommendations.
* popularityImg.py: Maps car names to image paths.
* descriptions.py: Contains car descriptions for tooltips.
* contentBasedFiltering.py: Module for content-based recommendations.
* popularityAndCollaborative.py: Module for ensemble recommendations.
* stkPush.py: Module for STK push functionality.

6. Models & Data
Recommendation Models:

* Popularity-Based: Recommends most frequently purchased or viewed cars.                                                                                                                                                                                                                                                                    
* Content-Based: Utilizes car attributes and similarities.
* Ensemble: Combines popularity and content-based approaches.
* Data: The application utilizes data (not provided in this code snippet) about cars, user interactions, and purchase history. This data is essential for the recommendation models.

Contributing
Contributions are welcome! Feel free to open issues or pull requests to suggest improvements or fix bugs.
                      
                      
                      
                      
                      
                      
                      
  
