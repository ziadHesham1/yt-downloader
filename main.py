import os

yt_command = 'yt-dlp'

# qualities
audio_quality = 'bestaudio'
video_360 = 'bestvideo[height<=360]+bestaudio'
video_480 = 'bestvideo[height<=480]+bestaudio'
best_video = 'bestvideo+bestaudio'
worst_video = 'worstvideo+bestaudio'
folder_name = 'RenameMe'
single_video_path = f'yt-dlp-downloads/Videos/{folder_name}/%(autonumber)s'
playlist_path = 'yt-dlp-downloads/playlists/%(playlist)s/%(playlist_index)s'
channel_path = 'yt-dlp-downloads/channels/%(uploader)s/%(playlist)s/%(playlist_index)s'

f_argument = ''
o_argument = ''
a_argument = ''
external_downloader_argument = '--external-downloader "aria2c" --external-downloader-args "-x 16 -s 16 -k 1M"'

print('Welcome to yt-dlp helper (❁´◡`❁)')
print('What are you going to download today?\n 1 - single\n 2 - playlist\n 3 - channel')
# take user input
download_type = int(input())
if download_type == 1:
    o_argument += single_video_path
elif download_type == 2:
    o_argument += playlist_path
elif download_type == 3:
    o_argument += channel_path

print('Do you want to download it as: \n 1 - audio\n 2 - video')
# take user input
download_format = int(input())
if download_format == 1:
    f_argument += audio_quality
elif download_format == 2:
    print('Choose your preferred quality: \n 1 - 360p\n 2 - 480p\n 3 - best\n 4 - worst')
    quality_choice = int(input())
    if quality_choice == 1:
        f_argument += video_360
    elif quality_choice == 2:
        f_argument += video_480
    elif quality_choice == 3:
        f_argument += best_video
    elif quality_choice == 4:
        f_argument += worst_video

print('Do you want to download a: \n 1 - single link\n 2 - multiple links')
# take user input
download_mode = int(input())
if download_mode == 1:
    url = input('Enter the URL to download: ')
    a_argument = url
else:
    folder_choice = input('Do you want to give a name to the download folder(y/n)? ')
    if folder_choice.lower() == 'y':
        folder_name = input('Enter the name of the download folder: ')
        os.makedirs(f'yt-dlp-downloads/Videos/{folder_name}', exist_ok=True)
        file_name = 'list.txt'
        # if there's a file with the same name make it name(1) or what ever the number of files
        with open(file_name, 'w') as f:
            while True:
                url = input('Enter a URL (or type "done" to finish): ')
                if url == 'done':
                    break
                f.write(url + '\n')
        a_argument = f'@{file_name}'
        # delete the text file after the download is completed
        os.remove(file_name)

output = f'{yt_command} -f {f_argument} -o {o_argument} {external_downloader_argument} {a_argument}'
# run output in cmd in the path E:\Downloads\yt-dlp to start downloading
os.system(f'cd E:\\Downloads\\yt-dlp && {output}')
