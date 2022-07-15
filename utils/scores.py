from datetime import datetime as dt
import json




_path = './scores.json'

class Scores:
    def save(clicked:int, missed:int, time:int) -> None:
        with open(_path, 'r+') as _scores:
            scores = json.load(_scores)

            cps = (clicked-missed)/time
            print(cps)
            if scores['best']['cps'] < cps:
                print('You beat your best score!')

                scores['best'] = {
                    'time': time,
                    'clicked': clicked,
                    'missed': missed,
                    'cps': cps,
                    'date': str(dt.now())
                }
            else:
                scores['sessions'].append({
                    'time': time,
                    'clicked': clicked,
                    'missed': missed,
                    'cps': cps,
                    'date': str(dt.now())
                })

            _scores.seek(0, 0)
            _scores.truncate()
            json.dump(scores, _scores, indent=4)


