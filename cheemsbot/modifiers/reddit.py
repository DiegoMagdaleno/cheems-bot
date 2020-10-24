# Reddit modifier to allow galleries to be shown.
# Inheritance is used to create a new class.
from typing import Optional
from praw.models.reddit.submission import Submission
from praw.models.reddit.base import RedditBase
from praw.models.reddit.base import InvalidURL
from praw.reddit import Reddit

# Brings gallery support to PRAW
class SubmissionWithGallery(Submission):
    @staticmethod
    def id_from_url(url: str) -> str:
        parts = RedditBase._url_parts(url)
        if "comments" not in parts and "gallery" not in parts:
            submission_id = parts[-1]
            if "r" in parts:
                raise InvalidURL(
                    url, message="Invalid URL (subreddit, not submission): {}"
                )
        elif "gallery" in parts:
            submission_id = parts[parts.index("gallery") + 1]
        else:
            submission_id = parts[parts.index("comments") + 1]
        
        if not submission_id.isalnum():
            raise InvalidURL(url)
        return submission_id


class RedditWithGallery(Reddit):
    def submission( 
        self, id: Optional[str] = None, url: Optional[str] = None
    ) -> SubmissionWithGallery:
        return SubmissionWithGallery(self, id=id, url=url)