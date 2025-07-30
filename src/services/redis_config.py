import os
import redis
import logging

logger = logging.getLogger(__name__)

if os.getenv("ENV", "dev") == "dev":
    from dotenv import load_dotenv
    load_dotenv()

def get_redis_client() -> redis.Redis | None:
    env = os.getenv("ENV", "dev")
    try:
        if env == "prod":
            client = redis.Redis(
                host=os.getenv("REDIS_HOST"),
                port=int(os.getenv("REDIS_PORT", 6379)),
                decode_responses=False,
                socket_connect_timeout=2, 
                socket_timeout=2,         
            )
        else:
            client = redis.Redis(
                host="localhost",
                port=6379,
                db=0,
                decode_responses=False,
                socket_connect_timeout=2,
                socket_timeout=2,
            )
        client.ping()
        return client
    except redis.RedisError as e:
        logger.warning(f"Redis not available, fallback to no cache: {e}")
        return None
