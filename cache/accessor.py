import redis


def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host='localhost',
        port=6378,
        db=0
    )

def set_pomodoro_count():
    redis_smth = get_redis_connection()
    redis_smth.set("pomodoro_count", 1)