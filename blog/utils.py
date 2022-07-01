from django.http import HttpRequest


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


def get_client_ip(request: HttpRequest) -> str:
    """Get the ip adddress of the client"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # On heroku, the original client IP address is the last IP in the
        # x-forwarded-for header.
        return x_forwarded_for.split(",")[-1]
    return request.META.get("REMOTE_ADDR")
