# Data Representation Project 2023  
### Introduction  
This is the Project for the Data Representation Module. This project involves creating a blog for my fantasy NFL league. The project utilizes Python coding, a Flask server with a REST API, a database table for storing data, a web interface for user interaction, and authentication for secure access.  

The main goal of this project is to provide a platform where league members can share their thoughts, updates, and analysis about the NFL fantasy league. It allows users to create blog posts, view existing posts, comment on posts, and interact with other league members in a secure and organized manner. It also allows them to link to handy websites for fantasy NFL info and analysis, and of course to your favourite social media sites.  

### Features  
1. **Flask Server with REST API**
The project leverages the Flask web framework to build a server that provides a REST API. This API serves as the interface for various operations such as creating blog posts, retrieving posts,editing and deleting comments, and of course, managing user setup and authentication.  

2. **Database Table**  
A database table is used to store all the necessary data for the blog. This includes information about blog posts, comments, and user accounts. The table is designed to efficiently manage and retrieve data for seamless user experience.  

3. **Web Interface**  
The project includes a web interface that allows users to interact with the blog. The interface provides an intuitive and user-friendly platform for creating, viewing, and commenting on blog posts. Users can also manage their own posts and profile settings through the interface.  

4. **Authentication**  
To ensure secure access and protect user data and posts, the project incorporates authentication mechanisms. Users are required to sign up and log in with their credentials to access the blog. Authentication prevents unauthorized access and allows for personalized user experiences.  
It also allow you to reset forgotten passwords by sending a token to your email address (Valid email address required for this).  

### Prerequisites  
Before getting started, ensure that the following components are installed on your system:  

Python (version 3.8 or higher)  
pip (package installer for Python)  
Setup and Installation  
1. **Clone the repository**  
First, clone this repository to an appropriate location on your local machine using the following command:  

```
git clone https://github.com/Lynch08/Data_Rep-_Proj_2023.git
```
2. **Set up a virtual environment**
A virtual environment is recommended to manage project dependencies. Follow the steps below to set up a virtual environment using venv:

##### Move into the project directory
```
cd ../Project
```
##### Create a new virtual environment
**Enter command:**    
```
python -m venv venv
```
#### Activate the virtual environment
##### For Windows:
**Enter command:**  
```
venv\Scripts\activate.bat 
```
##### For macOS/Linux:
**Enter command:**    
```
source venv/bin/activate  
```
3. **Install project dependencies**  
To install the required dependencies, use the package manager pip:  
```
pip install -r requirements.txt  
```
4. **Run the project**  
Once the setup is complete, you can run the project using the following command in the project location:  
```
python run.py  
```

### Register/Login to the Web Interface
Congratulations! You have successfully set up the project and are ready to use the web interface.  
Once the Flask server(Fblog) is running follow this link http://127.0.0.1:5000 - this works using the Chrome or Edge browsers.  
Once you have navigated to the home page you can see the test posts that I have entered using different accounts but you are not yet logged in.
From here you have 2 options.

1. Set up your own account using the "Register" button on the top right of the home page.  
This will allow you to set up a brand new account using new credentials.  

OR

2. I have set up a specific account for you to log in as (Only email and Password required for login): 

**Password:** Data_Rep_2023  
**Email:** Abeatty@demo.ie  

(Not Required for Login - Display Name Only)   
**Username:** Abeatty  

### Navigation  after Login
Once you are logged in you may notice that the headings on the far right of the navigation bar have changed slightly. You can navigate between the "Homepage", "About" page, "New Post" Page, "Account" details page and "Logout" - these buttons are on the heading bar.  

**Homepage:** Shows most recent posts (you can click on the posts to see them in full and edit/delete the posts that of the user you are logged in as).  
**About Page:** This is an Introdution Page to the team "owners" in the league.
**New Post Page:** This gives you empty fields to fill in the title and content of your next post.  
**Account Page:** This returns your account info, allows you to edit your username or email address as required. It also allows you to upload an image as a profile pic.  
**Logout:** Logs you out as whatever user you are currently logged in as.  

**Sidebar and links:** There is also a sidebar of useful links that will bring you to some of the most used pages relating to the League. Finally at the bottom of the page there are social media icons that will bring you to the login page of wherever you would like to go.

### Reset password.
If you would like to try out the functionality of resetting a password, logout and then go to the login button and navigate to the *Forgot Password* link at the bottom of the Log In box.
NB: A valid email address must be accociated with the account for this functionality to work. Also, I believe this will only work from a windows device, it was not coded for MAC devices, yet.

### Conclusion

In conclusion, this Python and data representation project has successfully combined the power of Python programming, data analysis, and Flask API to create a dynamic web interface for an NFL Fantasy Football Blog. Throughout this project, I have achieved our goals of providing a user-friendly and interactive platform for players in my fantasy football league to provide and access valuable links or just fun information and insights from other users.

Using Flask, a flexible web framework, we were able to create a decent user experience (This could definitly be improved and will be once my friends start using it and giving suggestions in September.)  

Throughout the development process, I faced challenges such as database creation, API and Web page design. However, with planning and problem-solving techniques, I successfully overcame most of these hurdles and delivered a functional and user-friendly web interface. One aspect that I found extremely challanging was the Web Design, I was able to get plenty of resources from websites like W3Schools, however I found that many of my design ideas did not look as good on the webpages as they did in my minds eye.


### Refrences:
##### Documentation and tutorials
 - [HTML W3schools](https://www.w3schools.com/html/)  
 - [Python Tutorials - Flask Form](https://pythonspot.com/flask-web-forms/)
 - [JavaScript W3schools](https://www.w3schools.com/js/default.asp)  
 - [HTML/DOM W3schools](https://www.w3schools.com/js/js_htmldom.asp)  
 - [Classes W3schols](https://www.w3schools.com/python/python_classes.asp)  
 - [Create and Import modules in Python - Geeks for Geeks](https://www.geeksforgeeks.org/create-and-import-modules-in-python/)  
 - [How to Create and Import a Custom Module in Python - Stackoverflow](https://stackoverflow.com/questions/37072773/how-to-create-and-import-a-custom-module-in-python)  
 - [Python Modules and Packages – An Introduction - Real Python](https://realpython.com/python-modules-packages/)
 - [Python Classes: The Power of Object-Oriented Programming - Real Python](https://realpython.com/python-classes/) 
 - [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)  
 - [Flask Setup - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)  


##### Videos
- [Importing Your Own Python Modules Properly](https://www.youtube.com/watch?v=GxCXiSkm6no)
- [Python Flask Tutorial: Full-Featured Web App Parts 1-9](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=RDQMHJcZNIpAfbc&start_radio=1)
- [Python Website Full Tutorial - Flask, Authentication, Databases & More](https://www.youtube.com/watch?v=dam0GPOAvVI)
- [Web Development with Python Tutorial – Flask & Dynamic Database-Driven Web Apps](https://www.youtube.com/watch?v=yBDHkveJUf4)
- [Python Requests Authentication Examples - Basic Auth, Custom Headers w/ Code](https://www.youtube.com/watch?v=TMxmkHdhfr8)
- [How to Send Emails with Flask Using Python](https://www.youtube.com/watch?v=L7Cslucyyyo)
- [Python Website Full Tutorial - Flask, Authentication, Databases & More](https://www.youtube.com/watch?v=dam0GPOAvVI)
- [How to Validate a Password Using Python (Simple)](https://www.youtube.com/watch?v=EGgjPCrzQkQ)
- [Python Flask Authentication Tutorial - Learn Flask Login](https://www.youtube.com/watch?v=71EU8gnZqZQ) 




