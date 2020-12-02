
import requests
import secrets
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url(secrets.discord_hook, adapter=RequestsWebhookAdapter())
webhook.send("Hello World")
