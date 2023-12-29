original_headers = {
    'Server': 'nginx/1.18.0 (Ubuntu)',
    'Date': 'Fri, 13 Oct 2023 20:54:58 GMT',
    'Content-Type': 'text/html; charset=utf-8',
    'Transfer-Encoding': 'chunked',
    'Connection': 'keep-alive',
    'Content-Encoding': 'gzip'
}

desired_order = ['Date', 'Server', 'Content-Type', 'Content-Encoding', 'Transfer-Encoding', 'Connection']

rearranged_headers = {key: original_headers[key] for key in desired_order}

print(rearranged_headers)
