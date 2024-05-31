from roboflow import Roboflow
#########################################################
rf = Roboflow(api_key="Rw8HnFE67kKd916j4yqM")
project = rf.workspace().project("shelf-scanners")
model = project.version("2").model
#########################################################



job_id, signed_url, expire_time = model.predict_video(
    r"C:\Users\jorda\Desktop\training\banana.training.mp4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

print(results)
