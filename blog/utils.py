

def calculate_time_to_read(content: str) -> int:
    """
    Calculates the time to read a blog post given the content of the post.
    Defaults to 5 minutes if the calculated amount of time is less than 0
    minutes.
    Who will click on a post that says read in zero minutes. :|
    """
    content_splitted_into_list = content.split(" ")
    time_to_read = int(len(content_splitted_into_list) / 200)
    return time_to_read if time_to_read > 0 else 5


def get_client_ip(request):
    """Get the ip adddress of the client"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
