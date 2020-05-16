from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_cors import CORS
from scheduler import TaskScheduler
app = Flask(__name__)

CORS(app)


@app.route('/get_schedule_options', methods=["POST"])
def get_shedule_options():
    sheduler = TaskScheduler(bed_time=22, wake_up_time=8)
    task = request.get_json(force=True)
    try:

        schedule_options = sheduler.get_schedule_options(
            task_duration=int(task["duration"]),  task_deadline=datetime.fromisoformat(task["deadline"]), task_num_sessions=task["numSessions"] if "numSessions" in task else 1)

        response = jsonify(schedule_options)
        return response
    except KeyError:
        return {"message": "Not valid"}, 400
