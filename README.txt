Installation:
    # ffprobe (linux):
        Run the following commands:
            1. sudo apt-get update
            2. sudo apt-get dist-upgrade
            3. sudo apt-get install ffmpeg


    # Web service:
        External package: Flask
        You can run the service in two ways:
            1. install the service packages using the requirements.txt file "pip install -r requirements.txt"
            2. use virtual_env- navigate to the project directory and run "source virtual_env/bin/activate"


Running the web service:

    Once you set your Python environment go to the "web_service directory" and run "python runserver.py"
    The server will listing to 8001
    * NOTICE:
        the service write its logs to the "/var/log" directory, by default this directory is own by the root user
        to avoid the app crashing while starting it please choose one of the following steps:
        1. create the logs dir manually and change its owner
        2. run the service as root (not recommended)

    Usage example:
        1. http://52.41.88.255:8001/info/frames?input=https://s3.amazonaws.com/icvt-tech-data/beamrvideo/sample.mov
        2. http://52.41.88.255:8001/info/frames?input=file:///tmp/ffprobe/sample.mov



Question #1

    1. Retrieve the video resolution:
        flags:

            -loglevel: enable to set the logging level, impact the output verbosity.

            -show_entries: enable to select entries in a specific section (in our case we want the
            height and width entries under the stream section).

            --print_format: specify the output format (json, xml etc.)

        command: ffprobe -loglevel error -show_entries stream=height,width -print_format json sample.mov


    2. Retrieve all video frames sizes:
        flags:
            -show_frames: show information about the file streams frames
            -select_stream: specify the stream type (v- video , a-audio)
            -show_entries: enable to select entries in a specific section (in our case we want the
            pkt_size entry under the frame section).
            --print_format: specify the output format (json, xml etc.)


        command: ffprobe -show_frames -select_streams v -show_entries frame=pkt_size -print_format json sample.mov


Question #2
    Output located in "/tmp/ffprobe/"
