import cv2
import sys
import os

def extract_frames(video_path, output_dir, interval=30, img_prefix='frame'):
    cap = cv2.VideoCapture(video_path)
    count = 0
    frame_number = 0
    
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if frame_number % interval == 0:
            frame_path = f"{output_dir}/{img_prefix}_{count}.jpg"
            print("The Image Generated : ", frame_path)

            cv2.imwrite(frame_path, frame)
            count += 1
        frame_number += 1
        
    cap.release()


def get_params(cmd_params):
   params_dict = {}
   for i in range(1, len(cmd_params), 2):
       params_dict[cmd_params[i]] = cmd_params[i + 1]
   return params_dict


if __name__ == "__main__":
    if len(sys.argv) > 1:
        params = get_params(sys.argv)

        if params["-input"] and params["-output"]:
            if not os.path.exists(params["-output"]):
                os.makedirs(params["-output"])
                
            extract_frames(params["-input"], params["-output"], int(params["-interval"]), params["-image_prefix"])

