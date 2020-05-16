
class TaskScheduler:
    def __init__(self, bed_time, wake_up_time, ):
        self._bed_time = bed_time
        self._wake_up_time = wake_up_time

    def _block_time_is_busy(self, from_time, to_time, time_block):
        if time_block["from"].hour >= from_time or time_block["to"].hour <= to_time:
            return True

        return False

    def _get_shedule(self, task_duration, task_deadline, task_num_sessions):
        from datetime import datetime, timedelta
        now_date = datetime.now()
        schedule = []
        time_block_length = (task_duration/task_num_sessions)
        while (task_deadline - now_date) > timedelta(minutes=1):
            time_block = {}
            time_block["from"] = now_date
            to_date = now_date + timedelta(minutes=time_block_length)
            time_block["to"] = now_date + timedelta(minutes=time_block_length)
            time_block["task"] = None
            now_date = to_date

            # TODO Check if the block is busy in Google Calendar or Microsoft Calendar

            if not self._block_time_is_busy(from_time=self._bed_time, to_time=self._wake_up_time, time_block=time_block):
                schedule.append(time_block)

        return schedule

    def get_schedule_options(self, task_duration, task_deadline, task_num_sessions=1):

        return self._get_shedule(task_deadline=task_deadline, task_duration=task_duration, task_num_sessions=task_num_sessions)
