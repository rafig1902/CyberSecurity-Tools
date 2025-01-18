import requests

def get_virustotal_report(api_key, hash_value):
    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"
    headers = {
        "x-apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      
        data = response.json()

        
        scan_results = data.get('data', {}).get('attributes', {}).get('last_analysis_results', {})
        
        
        for engine, result in scan_results.items():
            if result['category'] == 'malicious':
                return "Malware detected!"
        
       
        return "No malware detected."
    else:
       
        return f"Error: {response.status_code}, {response.text}"


api_key = 'f075856gjfj7c13706c20a985768688c0f6dd57856785614ccbe76856785aac6c1c8cc7ac8c8d726e7f1c479248a10975'


hash_value = input("Please enter the hash value to check: ")


report = get_virustotal_report(api_key, hash_value)


print(report)
