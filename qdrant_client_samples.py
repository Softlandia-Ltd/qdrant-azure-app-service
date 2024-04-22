import asyncio
import qdrant_client
from azure.identity.aio import DefaultAzureCredential

credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)


async def get_token():
    result = await credential.get_token(
        "api://your_app_id/.default"
    )
    return result.token


# HTTP client
http_client = qdrant_client.AsyncQdrantClient(
    url="your_app_name.azurewebsites.net",
    https=True,
    port=443,
    auth_token_provider=get_token,
)

# gRPC client
qrpc_client = qdrant_client.AsyncQdrantClient(
    url="your_app_name.azurewebsites.net",
    https=True,
    grpc_port=443,
    prefer_grpc=True,
    auth_token_provider=get_token,
)


async def main():
    async with credential:
        await http_client.get_collections()
        await qrpc_client.get_collections()


if __name__ == "__main__":
    asyncio.run(main())
