import asyncio
import aiohttp

url = "https://example.com" # Put the URL you want to visit here

# User agent to spoof (Chrome 120 on Windows 10)
userAgent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

async def fetch(session):
    async with session.get(url, headers=userAgent) as response:
        print(f"Visited {url}, Status: {response.status}")
        await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in range(10)]
        await asyncio.gather(*tasks)

asyncio.run(main())