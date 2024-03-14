from fastapi import APIRouter

from .products.views import router as products_router
from .demo_auth.views import router as basic_auth_router

router = APIRouter()
router.include_router(
    router=products_router,
    prefix="/products",
)

router.include_router(
    router=basic_auth_router,
)
