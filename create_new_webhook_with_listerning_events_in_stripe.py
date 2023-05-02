import stripe

# Set your API key
stripe.api_key = "sk_test_adsfasdfawerqwerwe3F"

# Set the URL of your endpoint
endpoint_url = "https://abc.edf.adfd.com/paymentCallback/stripe/cb/12341234asfasdf23423423403"

# Create a webhook endpoint
webhook_endpoint = stripe.WebhookEndpoint.create(
    url=endpoint_url,
    enabled_events=["setup_intent.created", "setup_intent.succeeded", "setup_intent.setup_failed", "setup_intent.requires_action"]
)

# Print the ID of the webhook endpoint
print(f"Webhook endpoint created with ID: {webhook_endpoint.id}")
