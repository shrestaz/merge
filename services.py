import requests

api_key = "YOUR_API_KEY"

# Replace api_key with your Merge production API Key
def create_link_token():
    body = {
        "end_user_origin_id": '',  # unique entity ID
        "end_user_organization_name": '',  # your user's organization name
        "end_user_email_address": '',  # your user's email address
        "categories": ["hris"],  # choose your category
    }

    headers = {"Authorization": f"Bearer {api_key}"}

    link_token_url = "https://api.merge.dev/api/integrations/create-link-token"
    link_token_result = requests.post(link_token_url, data=body, headers=headers)
    link_token = link_token_result.json().get("link_token")

    return link_token


def retrieve_account_token(public_token):
    headers = {"Authorization": f"Bearer {api_key}"}

    account_token_url = "https://api.merge.dev/api/integrations/account-token/{}".format(public_token)
    account_token_result = requests.get(account_token_url, headers=headers)

    account_token = account_token_result.json().get("account_token")
    return account_token  # Save this in your database
