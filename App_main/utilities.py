from threading import Thread

import requests


class NetworkAvaibility:
    
    def net_check(self):
        try:
            response = requests.get('https://www.google.com')
            if response.status_code == 200:
                self.internet_connection = True
        except requests.ConnectionError:
            self.internet_connection = False


class SongDuration:
    
    def song_time(self, inf):
        hours = int(inf // 3600)
        hour_other = inf % 3600

        mins = int(hour_other // 60)
        mins_other = hour_other % 60

        seconds = int(mins_other % 60)

        time_took = '{}:{}:{}'.format(
            hours if hours > 10 else '0' + str(hours),
            mins if mins > 10 else '0' + str(mins),
            seconds if seconds > 10 else '0' + str(seconds)
            )
        return time_took


class ThreadingStart:
    
    def start_thread(self, func):
        if self.threadd is None or not self.threadd.is_alive():
                        self.threadd = Thread(target=func)
                        self.threadd.start()