# get json data

import requests

response = requests.get('https://www.facebook.com/rootadmin777')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Try to parse the response content as JSON
        json_data = response.json()
        print(json_data)
    except Exception as e:
        # If there's an error parsing JSON, print the error message
        print(f"Error parsing JSON: {e}")
else:
    print(f"Error: {response.status_code}")
#--------------------------------------------------------------------------------------------------------------------------------
# re-format respons headers

headers = {
'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'accept-ch-lifetime': '4838400', 'accept-ch': 'viewport-width,dpr,Sec-CH-Prefers-Color-Scheme,Sec-CH-UA-Full-Version-List,Sec-CH-UA-Platform-Version,Sec-CH-UA-Model', 'Link': '<https://www.facebook.com/rootadmin777>; rel="canonical"', 'report-to': '{"max_age":259200,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/ajax\\/comet_error_reports\\/?device_level=unknown"}]}, {"max_age":3600,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/ajax\\/comet_error_reports\\/?device_level=unknown"}],"group":"network-errors"}', 'content-security-policy-report-only': "default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com *.fbcdn.net 'unsafe-eval';script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* 'unsafe-inline' blob: data: 'self' connect.facebook.net 'unsafe-eval';style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' http://localhost:3103 wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com https://api.mapbox.com https://*.tiles.mapbox.com;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com *.tenor.co media.tenor.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net *.giphy.com connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com https://*.giphy.com data:;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com https://sandbox.paywithmybank.com;worker-src *.facebook.com/static_resources/webworker_v1/init_script/ *.facebook.com/static_resources/webworker/init_script/ *.facebook.com/static_resources/sharedworker/init_script/ *.facebook.com/static_resources/webworker/map_libre/ *.facebook.com/sw/ *.facebook.com/sw;block-all-mixed-content;report-uri https://www.facebook.com/csp/reporting/?minimize=0;", 'content-security-policy': "default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com *.fbcdn.net 'unsafe-eval';script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* 'unsafe-inline' blob: data: 'self' connect.facebook.net 'unsafe-eval';style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' http://localhost:3103 wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com https://api.mapbox.com https://*.tiles.mapbox.com;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com *.tenor.co media.tenor.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net *.giphy.com connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com https://*.giphy.com data:;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com https://sandbox.paywithmybank.com;worker-src blob: *.facebook.com data:;block-all-mixed-content;upgrade-insecure-requests;", 'document-policy': 'force-load-at-top', 'permissions-policy': 'accelerometer=(), ambient-light-sensor=(), bluetooth=(), camera=(self), gyroscope=(), hid=(), idle-detection=(), magnetometer=(), microphone=(self), midi=(), payment=(), screen-wake-lock=(), serial=(), usb=()', 'cross-origin-resource-policy': 'same-origin', 'nel': '{"report_to":"network-errors","max_age":3600,"failure_fraction":0.01}', 'cross-origin-opener-policy': 'same-origin-allow-popups', 'Pragma': 'no-cache', 'Cache-Control': 'private, no-cache, no-store, must-revalidate', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'X-Frame-Options': 'DENY', 'Strict-Transport-Security': 'max-age=15552000; preload', 'Content-Type': 'text/html; charset="utf-8"', 'X-FB-Debug': 'tvWkNQ5zcPeGc5lhByaoJBgEFNuBrLTffmvO6Xvhp44N1wP3O7BQv7vanCMBeLG7jTaMNNFHrBARzcl7Ia7elw==', 'Date': 'Thu, 14 Sep 2023 12:22:02 GMT', 'Alt-Svc': 'h3=":443"; ma=86400', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive'

    # Add the rest of the headers here
}

with open('response_headers.txt', 'w') as file:
    for key, value in headers.items():
        file.write(f'{key}: {value}\n')


#--------------------------------------------------------------------------------------------------------------------------------
# return json data from seach query


response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')