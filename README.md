# automated-self-check

**You need to install:**

1- python

2- selnium

3- chrome driver

**To install python:**


Go to this website: https://www.python.org/downloads/

and click Download then install the application by next => next => finish 

**To install selenium:**

Start menu => search for "cmd" => then type:

pip install selenium


**To install chrome driver:**

Open chrome => open 3 dots on the top right => About => look up chrome version

Then go to this website: https://chromedriver.chromium.org/downloads

And download the version that is compatible with your chrome version

Note: There is no separate version for windows 64, just install windows 32 and it will work fine

After downloading it, put it in the same directory as python code and open the executable

Now, you are ready to go :)

To make this script runs everyday you can:

1- Create AWS account

2- Create lambda function

3- Write the script inside the function handler

4- Deploy

5- Add trigger

6- Cloudwatch

7- in the schedule expression write: cron(59 11 * * ? *)
