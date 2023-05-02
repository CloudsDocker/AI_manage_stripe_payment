import stripe

# Set your API key
stripe.api_key = "sk_test_vhSOG3L28bgfodllLH3wdTs8005TyE6NAF"

# to update existing webhook endpoint

# Set the ID of the existing webhook endpoint you want to modify
webhook_endpoint_id = "we_34535324523452345f3aS9Xtn"

# Get the existing webhook endpoint
webhook_endpoint = stripe.WebhookEndpoint.retrieve(webhook_endpoint_id)

# Add the events to the listener list for the webhook endpoint
webhook_endpoint.enabled_events += ["setup_intent.created", "setup_intent.succeeded", "setup_intent.setup_failed", "setup_intent.requires_action"]

# Save the changes to the webhook endpoint
webhook_endpoint.save()

# Print a confirmation message
print("Webhook endpoint updated successfully.")