import os

VALID_EMAIL = os.getenv("VALID_EMAIL")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
WRONG_PASSWORD = os.getenv("WRONG_PASSWORD",)
UNREGISTERED_EMAIL = os.getenv("TEST_UNREGISTERED_EMAIL", "nobody_registered@example.com")

# invalid data - invalid format of email
INVALID_EMAIL = "test1gg.com"