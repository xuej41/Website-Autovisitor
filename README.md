# Website Autovisitor

These scripts demonstrate how to perform multiple concurrent HTTP requests to a specified URL.

The scripts use Python's `asyncio` and `aiohttp` libraries. It is designed for scenarios where speed and efficiency are critical, such as web scraping or API testing.

## Usage
1. Install the required library:

```python
pip install aiohttp
```

2. Modify the url variable in the script to the desired target URL.
3. Run the script:

```python
python async.py
```

4. The script will send 10 concurrent requests to the specified URL and print the HTTP status for each request.

### Example Output
```
Visited https://example.com, Status: 200
Visited https://example.com, Status: 200
Visited https://example.com, Status: 200
...
```

### When to Use
- When you need to perform multiple HTTP requests concurrently.
- For tasks like web scraping or API testing where speed and efficiency are critical.
