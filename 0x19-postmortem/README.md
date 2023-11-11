Postmortem for Web Stack Debugging: Nginx Misconfiguration Event Synopsis:

A misconfiguration on the Nginx server caused downtime and performance difficulties for our web application on [Date and Time]. The incorrect setup led to incorrect routing and compromised the web stack's ability to operate as intended.

[17th October, 2023 at 11:38pm WAT]: The test script and checkers failed.

[18th October, 2023 at 8:15pm WAT]: Upon preliminary investigation, it was found that the web traffic-handling Nginx server was not set correctly.

Incident Information:
What Didn't Work:

Nginx Configuration Error: Incoming requests were incorrectly routed due to a misconfigured Nginx server. I experienced sporadic connection failures, Nginx wasn't listenening on port 8080 and HTTP 502 errors as a result.

Root Cause:
Configuration Error: I had made a recent modification to the Nginx configuration files resulted in error, which was the cause of the misconfiguration.

Action Taken:
I uninstalled the nginx that i had previously installed and made sure to clean up the configuration files. After which i re-installed it, and this time, i set up tge configuration file with the correct setup information and requirements.

Lesson Learned:
Now, i understand a lot better that it is of utmost importance to pay attention to the littlelest details, there is no small bug in software development. A little error or bug will affect everything and anything.

Conclusion:
The Nginx misconfiguration incident served as a valuable learning experience. Following the given set of instructions to the later is key. 
