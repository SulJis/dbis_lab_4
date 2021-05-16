encoding = "cp1251"
batches_path = "batches"
datasets_path = "data"
logs_path = "logs"
output_path = "output"
batch_rows = 1000
pipeline = [
    {
        "$match": {
                "engTestStatus": "Зараховано"
            }
    },
    {
        "$group": {
            "_id": {
                "Region": "$REGNAME",
                "Year": "$year"
            },
            "avgBall": {
                "$avg": "$engBall100"
            }
        }
    },
    {
        "$sort": {
            "_id.Region": 1,
            "_id.Year": 1

        }
    }
]
