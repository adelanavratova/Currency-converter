# Currency-converter
This code is a simple currency converter that allows users to convert currency from one form to another. Users can input an amount in the base currency and select a target currency for conversion, and then receive the converted amount.

## Table of Contents
- [Installation of Libraries](#installation-of-libraries)
- [Usage](#usage)
- [Files](#files) 
- [Functions](#functions)
- [Learnings and Takeaways](#learnings-and-takeaways)
- [Contact](#contact)

## Installation of Libraries
Before using this program, make sure you have the required libraries installed. Use the following commands to install the necessary libraries:
#### Instalation via pip:
To install the required libraries, run the following command in your command line:
```bash
    pip install requests forex-python
```
## USAGE
#### Running the Program:
To run the program, simply execute the script in Python.
```bash
    python currency_converter.py
```
#### Required Information:
Upon running the program, you will be prompted to input the amount in the base currency and select both base and target currencies for conversion.
#### Internet Connection:
If an internet connection is available, the program will automatically fetch the current currency exchange rates. Otherwise, it will utilize the last available offline data.
#### Currency Conversion:
After entering the required information, the program will perform the currency conversion and display the resulting amount.

## Files
**currency_converter.py**: Main script for running the program.  
**list_of_currencies.txt**: List of supported currencies.  
**last_rates.txt**: Last available currency exchange rates.  

## Functions
**communication()**: Function for communicating with the user and inputting the amount and currencies.  
**transfer()**: Function for currency conversion using current exchange rates.  
**transfer_offline()**: Function for currency conversion using the last available offline data.  
**put_offline_rates()**: Function for updating offline data.  
**is_not_connection()**: Function for handling situations where an internet connection is unavailable.  
**check_internet_connection()**: Function for checking internet connection availability.  

## Learnings and Takeaways
During the development of this currency conversion application, I improved several skills:  
#### Handling User Input: 
I refined my ability to handle user input, including validation and error handling, as evident in the communication() function.  
#### File Operations: 
I gained experience in reading from and writing to files using Python's built-in functions, as demonstrated in functions like transfet_offline() and put_offline_rates().
#### HTTP Requests and Internet Connectivity:
I deepened my understanding of making HTTP requests and checking internet connectivity status, as seen in the check_internet_connection() function.  
#### Exception Handling: 
I further honed my skills in handling exceptions for graceful error handling and unexpected input, as visible in the try-except block within the communication() function.  

This project serves as evidence of my commitment to creating quality, functional software solutions and continuously striving to improve and expand my skills. It is characterized by well-structured code that meets both user requirements and industry standards.

## Contact
For any inquiries or issues, feel free to contact the developer via email: **adelanavratova@seznam.cz**
Enjoy using this program!
