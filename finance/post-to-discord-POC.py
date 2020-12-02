
import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("https://discord.com/api/webhooks/783558803601358849/LdnpgLiJ9y20_haK-81w_P8JbjzX1f664VO2dBcZgBSNoeOw52GXGezHWq33illwrMvm", adapter=RequestsWebhookAdapter())
webhook.send("Hello World")
