

## Full Stack Automation Final Project - (Python)

## About/Project Overview
This project is designed for automation testing, it's built as an infrastructure using the Python language.
The project is structured as an infrastructure using the page object design pattern and layered architecture to ensure maintainability and scalability across different clients and browsers.
It supports diverse testing applications including Web, API, Mobile, database, Electron, and desktop testing.

## Project Overview
Supports testing for the following applications/services:
- Web applications - Client-side Testing
- Mobile applications - Client-side Testing
- Electron Applications - Client-side Testing
- Desktop Applications - Client-side Testing
- API Testing - Server-side Testing
- Database Testing - Server-side testing

## Infrastructure Utilizes:
The testing infrastructure is built with the following components to enhance automation capabilities:
- **Page Object Design Pattern**: Used to create reusable and maintainable code by keeping the page elements separated from test scripts.
- **Project Layers**: Organized into extension workflows, test cases, and utility classes to improve code clarity.
- **Support of different client browsers**: Testing can be utilized for different client browsers applications
- **Failure Mechanism**: Event listener to enhance debugging during test failures.
- **External File Support**: Facilitates data-driven testing by supporting external files like CSV, Excel, etc.
- **Visual Testing**: Implements visual testing to catch UI bugs/issues (Applitools Program).

## Infrastructure Key Operations
Infrastructure key distinguishable operations
- **Common Operations**: A utility class that encapsulates common operations and functionalities.
- **Workflow Sections**: Separates the business logic from the testing execution, organizing the flow of processes and enhancing the clarity and maintainability of test scripts.
- **Test Cases Section**: Organizes each test to display only key factors or information about the test. Focusing on essential details to facilitate quick understanding and efficient test management.
- **Page Objects Section**: Describes how the framework interacts with, identifies, and organizes web elements, ensuring a clear separation between the test code and the web UI, which enhances test maintenance
- and reduces code duplication.
- **Verification sections**: Our testing framework utilizes standard assertions to check specific conditions and verify that the software behaves as expected. In addition to standard assertions, we integrate smart assertions, which enhance our testing capabilities by allowing multiple conditions to be evaluated before a test is considered to fail. 

## List of Project Applications
This project covers a diverse range of applications/services to demonstrate its testing capabilities across various platforms:

1. **Tel Aviv Hotel Web Page (Web Testing)**: A WordPress website that I built - https://mpeleg90.com/omri/
2. **Grafana API (API Testing)**: Utilized API testing to ensure the functionality and reliability of Grafana's API interactions.
3. **NBA Website Database (Database Testing)**: A database of NBA teams and players from the 2018/2019 season, I created the database by web scraping various sports sites.
4. **MetricConversion Application (Mobile Testing)**: Tested for its ability to handle different metric conversion functionalities on mobile devices.
5. **Calculator Application (Desktop Testing)**: A desktop application.
6. **ToDo List Application (Electron Testing)**: An Electron-based application, tested to verify its functionality and performance as a task management tool.

## Tools and Frameworks Used in the Project
This project utilizes different tools and frameworks to facilitate comprehensive testing across multiple platforms:

- **Selenium**: For automating browser actions and managing web application testing.
- **Pytest**: Used for organizing and running tests, providing a powerful framework for assertions and test setups.
- **Listeners**: Integrated within the testing framework to capture and log test execution events.
- **Requests Library**: Employed for API testing, enabling straightforward HTTP requests to test and validate API functionalities.
- **XAMPP**: Utilized to operate a local database server, facilitating the management of backend data.
- **phpMyAdmin**: Provides a graphical interface to handle the database operations, allowing for easy viewing and management of database changes.
- **Jenkins**: Manages and automates test execution, supporting continuous integration and continuous delivery.
- **Allure Reporting**: Generates comprehensive and visually appealing test reports, highlighting test outcomes and facilitating detailed analysis.
- **Appium Studio**: Used for mobile testing, providing tools necessary for effective automation of mobile applications.
- **WinAppDriver Service**: Enables automation of desktop environments, crucial for desktop application testing.

## Installation and Setup

To get started with the different types of testing in this project, follow these instructions for each application:

**Web Testing**
- Open the Website: Access the Tel Aviv Hotel web page by navigating to [https://mpeleg90.com/omri/](https://mpeleg90.com/omri/) on supported browsers.

**API Testing**
- Download Grafana Server: To set up the environment for API testing, download and install the Grafana server from the [official Grafana website](https://grafana.com/grafana/download).

**Mobile Testing**
- Download and Install Appium Studio: To conduct mobile testing, you will need to download and install Appium Studio.
- Import Mobile apk File: Import the [`MetricConversions_v2.0.3.apk`](./utilities). Then set up your application on the Appium studio.

**Database Testing**
- Operate the XAMPP Server: To perform database testing, start the XAMPP server with Apache and MySQL modules running. This setup will help you manage the local database server.
- Import Database File: Import the [`nba_teams_2019.sql`](./utilities). This step will populate your MySQL database with the necessary data for testing the NBA website database.

**Electron Testing**
- Install Electron App: To set up Electron testing, install the application - https://atidcollege.co.il/downloads/electron/TodoList-Setup.exe

**Desktop Testing**
- Install WinAppDriver Service: To facilitate the automation of desktop applications, install the WinAppDriver Service. This tool is essential for enabling UI automation for Windows applications.
- open the Calculator Application that you intend to test (desktop calculator application)
  
## Test Execution
Test execution is automated using Jenkins, integrated with Allure for reporting business purposes:
1. **Jenkins**: Manages the running of tests, overseeing the execution across different environments and ensuring continuous integration.
2. **Allure Reports**: Generates detailed and interactive reports, providing insights into test results and facilitating debugging of failures.
 Additionally, Allure captures screenshots of failures to aid in visual troubleshooting.


### How to Run Tests
To execute the tests, configure your Jenkins pipeline to include the necessary test suites and trigger them as per your CI/CD setup. Results can be viewed in Allure for detailed analysis.
