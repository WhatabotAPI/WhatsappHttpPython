import json
import asyncio
import aiohttp

class WhatabotHTTPClient:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.phone = "YOUR_PHONE_NUMBER"
        self.url = "https://api.whatabot.io/Whatsapp/RequestSendMessage"
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }

    async def send_message(self, text):
        data = {
            "ApiKey": self.api_key,
            "Text": text,
            "Phone": self.phone
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, json=data) as response:
                if response.status == 200:
                    print("Message sent successfully")
                else:
                    print(f"Failed to send message. Status code: {response.status}")

async def main():
    client = WhatabotHTTPClient()
    
    #Here you can implement the logic you need and call cliend.send_message
    await client.send_message("Hello from Whatabot!")

if __name__ == "__main__":
    asyncio.run(main())
