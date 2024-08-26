# Video to Image converter!

This is a Python script extract frames from a video file at regular intervals.

### Run

To run the script, clone the repository to your local machine, and the setup a Python virtual environment using the following command.

```
# Go to the folder
cd video-to-image-converter

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

Then, install all the dependencies

```
pip3 install -r requirements.txt
```

The you can convert the videos to images

```
python3 app.py -input {path_to_video} -output {save_folder} -interval {extract_frame_from_interval} -image_prefix {image_name_prefix}
```

Thank you 😊
