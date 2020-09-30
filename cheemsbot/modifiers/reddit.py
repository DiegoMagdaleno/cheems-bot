# Reddit modifier to allow galleries to be shown.
# Inheritance is used to create a new class.
from Praw.models.listing.mixins import base
from Praw.models.reddit.submission import Submission
from 

class SubmissionWithGallery(Submission):
	
	@staticmethod
	def id_from_url(url: str) -> str:
		parts = RedditBase._url_parts(url)
		if "comments" not in parts and "gallery" not in parts:
			submissin_id = parts[-1]
			if "r" in parts:
				raise InvalidURL(
					url, message="Invalid URL (subreddit, not submission): {}"
				)