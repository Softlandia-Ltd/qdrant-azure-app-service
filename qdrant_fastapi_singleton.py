from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from qdrant_client import AsyncQdrantClient
from azure.identity.aio import DefaultAzureCredential

# replace with Managed Identity Credential in production
credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)


async def get_token():
    result = await credential.get_token(
        "api://your_app_id/.default"
    )
    return result.token


class Qdrant:
    def __init__(self):
        self._client = AsyncQdrantClient(
            url="your_app_name.azurewebsites.net",
            https=True,
            grpc_port=443,
            prefer_grpc=True,
            auth_token_provider=get_token,
        )

    async def get_collections(self):
        return await self._client.get_collections()


@asynccontextmanager
async def lifespan(app: FastAPI):
    qdrant = Qdrant()
    # singleton
    app.dependency_overrides[Qdrant] = lambda: qdrant
    yield
    await qdrant._client.close()
    await credential.close()


app = FastAPI(lifespan=lifespan)


@app.get("/collections")
async def get_collections(qdrant_client: Qdrant = Depends(Qdrant)):
    results = await qdrant_client.get_collections()
    return results
