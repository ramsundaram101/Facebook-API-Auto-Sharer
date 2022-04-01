# Facebook-API-Auto-Sharer
Automatically Shares FB Posts to a pre-provided list of grps

First, clone this repository. Open Command Prompt and enter the following command :

``git clone https://github.com/ramsundaram101/Facebook-API-Auto-Sharer``

Next,install requirements with the following command :
``pip install -r requirements.txt``

In the ``info.json`` file, access_token refers to your FB Graph API access token. You can learn how to get this token here : https://www.jcchouinard.com/facebook-graph-api-get-access-token/

In ``fb_grps.txt``, add comma-separated Facebook Group Numbers.

For example, if the group URL is https://www.facebook.com/groups/744128789503859, the group number is the last part, namely 744128789503859.

Now, you can run the code. To do this, in ``cmd``, run the following:
```
python [folder path to the cloned repo]/Auto_sharer.py --timestamps=[True/False] --info_folder=[folder path to info.json] --grps_folder=[folder path to fb_grps.txt] --timestamps_folder=[folder path to output timestamps.csv]
#Example- When one is inside the cloned repo
python Auto_sharer.py --timestamps=True --info_folder=./info.json --grps_folder=./fb_grps.txt --timestamps_folder=./
```
