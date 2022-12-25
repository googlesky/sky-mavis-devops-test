import json
import requests

def get_vulnerabilities(org, repo, manifest_id, api_token):
    """
    Retrieves the vulnerabilities for an image from Quay.
    
    Parameters:
        org (str): The organization.
        repo (str): The repository.
        manifest_id (str): The image's manifest ID.
        api_token (str): The Quay API token.
    
    Returns:
        list: A list of vulnerabilities.
    """
    # Set up the API endpoint and headers
    api_endpoint = f"https://quay.io/api/v1/repository/{org}/{repo}/manifest/{manifest_id}/vuln/oss"
    headers = {
        "Authorization": "Bearer " + api_token
    }

    # Send the request and retrieve the response
    response = requests.get(api_endpoint, headers=headers)

    # Parse the response as JSON
    data = response.json()

    # Return the vulnerabilities
    return data["vulnerabilities"]

def main():
    # Read the list of images from standard input
    images = json.loads(input())

    # Set the API token
    api_token = "<api_token>"

    # Initialize the output list
    output = []

    # Iterate over the list of images
    for image in images:
        # Retrieve the vulnerabilities for the image
        vulnerabilities = get_vulnerabilities(image["Organisation"], image["Repository"], image["Tag"], api_token)

        # Add the image and vulnerabilities to the output list
        output.append({
            "Organisation": image["Organisation"],
            "Repository": image["Repository"],
            "Tag": image["Tag"],
            "Manifest": image["Manifest"],
            "Vulnerabilities": vulnerabilities
        })

    # Print the output list as JSON
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
