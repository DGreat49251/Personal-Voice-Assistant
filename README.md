# Personal-Voice-Assistant
<hr>
<h2>Personal Assistant using Python Speech Recognition and Voice Input from user with various features like opening several websites and applications etc.</h2>
<hr>
<p>Modules used: speech_recognition, datetime, wikipedia, webbrowser, win32com</p>
<p>Know more about these and their installation <a href="https://pypi.org/">here</a>.</p>
<hr>
<p>Functions used: asst_speaks(audio), greet(), user_speaks(), reg_browser(), main()</p>
<p>Let us see about these functions in detail.</p>
<hr>
<p><b>asst_speaks(audio)</b> - This function is used whenever the assistant has to speak. The 'audio' parameter is the text that it will speak which are based on evaluation of user input passed.</p>
<hr>
<p><b>greet()</b> - This function is used to generate the greeting message by detecting the hour when asked to greet the user like "Good Morning!", "Good Afternoon", "Good Evening" etc. By default it greets on loading the system.</p>
<hr>
<p><b>user_speaks()</b> - This is the audio input function from the user end. The audio that the user provides gets converted in the form of text in this function itself for processing.</p>
<hr>
<p><b>reg_browser()</b> - This function is used to register the browser (Google Chrome) in this case with the program. It is executed at the beginning of the execution of the program for hassle free execution og thr program.</p>
<hr>
<p><b>main()</b> - This function is the driver code for the entire program. Here is where all the functions are brought to operation. Firstly, the greet() and reg_browser() functions are executed. Then user is asked for input of command and as per the command the task is executed and this process continues...</p>
<hr>
<p>Features of the Voice Assistant:-
<ol><li>Tell about itself</li>
  <li>Tell about its creator</li>
  <li>Wikipedia something.</li>
  <li>Open Websites like Google, GeeksforGeeks, StackOverflow, Spotify, Hotstar etc. </li>
  <li>Tell date and time.</li></ol>
  <p>and much more...</p>
