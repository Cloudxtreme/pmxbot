import time

from tests.functional import PmxbotHarness

class TestPmxbotLog(PmxbotHarness):
	def test_no_op(self):
		"""
		Test that the harness is working.
		"""

	def test_bot_running_after_feeds_parsed(self):
		"""
		The RSS feed parser attempts to fetch feeds after 30 seconds and save
		entries 60 seconds after that, so wait
		that long and make sure the bot is still running.
		"""
		time.sleep(99)
		assert self.bot.poll() is None, "Bot is no longer running"