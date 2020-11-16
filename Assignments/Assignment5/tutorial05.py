import os
import re
os.system('cls')

def rename_FIR(folder_name):
    cwd = os.getcwd()
    cwd = os.path.join(cwd ,'Subtitles')
    cwd = os.path.join(cwd, folder_name[0])
    files = list(os.listdir(cwd))
    os.chdir(cwd)

    for file in files:
        try:
            detail = re.findall(r'\d+', file)
            episode_no = detail[0].strip()

            while(len(episode_no) < folder_name[2]):
                episode_no = '0' + episode_no

            file_ext = re.split(r'\.', file)[-1].strip()
            os.rename(file, folder_name[0] + ' - '+ ' Episode '+ episode_no + '.' + file_ext )
        except:
            os.remove(file) 
    

# def rename_Game_of_Thrones(folder_name):
#     # rename Logic 
    

# def rename_Sherlock(folder_name):
#     # rename Logic 
    

# def rename_Suits(folder_name):
#     # rename Logic 
    

# def rename_How_I_Met_Your_Mother(folder_name):
#     # rename Logic 

web_series = {1:'FIR',2:'Game of Thrones',3:'How I Met Your Mother',4:'Sherlock',5:'Suits'}

for key in web_series:
    print(key," ",web_series[key])

web_series_no = int(input("Enter a valid number corresponding to main title of web series: ")) 
season_padding = int(input("Enter the season number padding of Web Series: ")) 
episode_padding = int(input("Enter the episode number padding of Web Series:"))
folder_name = list((web_series[web_series_no], season_padding, episode_padding))  

if web_series_no == 1:
	rename_FIR(folder_name)
elif web_series_no == 2:
	rename_Game_of_Thrones(folder_name)
elif web_series_no == 3:
	rename_How_I_Met_Your_Mother(folder_name)
elif web_series_no == 4:
	rename_Sherlock(folder_name)
elif web_series_no == 5:
	rename_Suits(folder_name)
