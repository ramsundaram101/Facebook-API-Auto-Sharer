import json
import pandas as pd
from facebook import GraphAPI
import datetime
import argparse

#Function to convert boolena string to bool for argparser
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(description='Facebook API Auto Sharer')
parser.add_argument('--timestamps', default=False, type=str2bool, help='Do you want a CSV file of Groups the post was shared on with Timestamps?')
parser.add_argument('--info_folder', default='info.json', type=str, help='Folder path to info.json file')
parser.add_argument('--grps_folder', default='fb_grps.txt', type=str, help='Folder path to fb_grps txt file')
parser.add_argument('--timestamp_folder', default='', type=str, help='Folder path to output csv')

args = parser.parse_args()

#Reads a json file
def read_json(filename):
    with open(filename) as f:
        info = json.load(f)
    return info

#Reads FB grps from comma-separated .txt file
def read_grps(filename):
    file = open(filename, "r")
    data = file.read()
    data_list = data.split(",")
    try:
        file.close()
    except:
        pass
    return data_list

#Establishes connection to FB's graph API
def obtain_graphapi(info):
    try:
        graph = GraphAPI(access_token=info['access_token'])
        return graph
    except:
        print("An error has occured. Please retry or check your access token")
        return


if __name__ == '__main__':
    
    info = read_json(args.info_folder)

    graph = obtain_graphapi(info)
    
    message = info['message'] #THe message or caption
    link = info['link'] #The link/FB post you want to share
    groups = read_grps(args.grps_folder) 
    timestamp_df = pd.DataFrame(columns = ['Group Name', 'Group ID', 'Timestamp']) #Creates empty DataFrame to store timestamps

    #For loop through the groups
    for group in groups:
        try:
            graph.put_object(group,'feed', message=message,link=link) #Posts in grp feed
            if(args.timestamps):
                #If timestamps is True, appends timestamp and grp info to DataFrame 
                grp_info = graph.get_object(id=group, fields = 'name')
                grp_info['Timestamp'] = str(datetime.datetime.now())
                timestamp_df.loc[len(timestamp_df.index)] = grp_info.values()
        except:
            grp_info = graph.get_object(id=group, fields = 'name')
            print("Unable to post in "+grp_info['name']+". You might not have permission to post there.")

    if(args.timestamps):
        timestamp_df.to_csv(args.timestamp_folder+info['sheet_name']+'.csv')