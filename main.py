import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from crudadmin import CRUDAdmin
from models import (
    Base, User, Product, ProductImage,
    Order, OrderStatus, OrderItem,
    Cart, CartItem,
    Ads, News, Article, FAQ, ArticleCategory
)
from schemas import (
    UserCreate, UserUpdate,
    ProductCreate, ProductUpdate,
    ProductImageCreate, ProductImageUpdate,
    OrderCreate, OrderUpdate,
    OrderItemCreate, OrderItemUpdate,
    CartCreate, CartUpdate,
    CartItemCreate, CartItemUpdate,
    AdsCreate, AdsUpdate,
    NewsCreate, NewsUpdate,
    ArticleCreate, ArticleUpdate,
    FAQCreate, FAQUpdate,
    ArticleCategoryCreate, ArticleCategoryUpdate
)

# 数据库配置
# 使用 SQLite 作为开发数据库，生产环境可以改为 PostgreSQL 或 MySQL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")

# 创建数据库引擎
engine = create_async_engine(DATABASE_URL, echo=True)

# 创建 session 工厂
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


# 数据库 session 依赖
async def get_session():
    async with async_session_maker() as session:
        yield session


# 创建 CRUDAdmin 实例
admin = CRUDAdmin(
    session=get_session,
    SECRET_KEY=os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production"),
    initial_admin={
        "username": "admin",
        "password": "admin123"  # 生产环境请使用强密码
    },
    # 可选：启用事件跟踪
    track_events=True,
    theme="light-theme"
)


# 添加模型到 admin 界面
# CRUDAdmin 會根據模型的 __module__ 屬性自動分組
# 我們通過修改模型的 __module__ 屬性來實現分組

# 用戶管理
User.__module__ = "models.user_management"
admin.add_view(
    model=User,
    create_schema=UserCreate,
    update_schema=UserUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

# 購物車管理
Product.__module__ = "models.shopping_cart"
ProductImage.__module__ = "models.shopping_cart"
Order.__module__ = "models.shopping_cart"
OrderItem.__module__ = "models.shopping_cart"
Cart.__module__ = "models.shopping_cart"
CartItem.__module__ = "models.shopping_cart"

admin.add_view(
    model=Product,
    create_schema=ProductCreate,
    update_schema=ProductUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=ProductImage,
    create_schema=ProductImageCreate,
    update_schema=ProductImageUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=Order,
    create_schema=OrderCreate,
    update_schema=OrderUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=OrderItem,
    create_schema=OrderItemCreate,
    update_schema=OrderItemUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=Cart,
    create_schema=CartCreate,
    update_schema=CartUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=CartItem,
    create_schema=CartItemCreate,
    update_schema=CartItemUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

# 內容管理
Ads.__module__ = "models.content_management"
News.__module__ = "models.content_management"
ArticleCategory.__module__ = "models.content_management"
Article.__module__ = "models.content_management"
FAQ.__module__ = "models.content_management"

admin.add_view(
    model=Ads,
    create_schema=AdsCreate,
    update_schema=AdsUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=News,
    create_schema=NewsCreate,
    update_schema=NewsUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=ArticleCategory,
    create_schema=ArticleCategoryCreate,
    update_schema=ArticleCategoryUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=Article,
    create_schema=ArticleCreate,
    update_schema=ArticleUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)

admin.add_view(
    model=FAQ,
    create_schema=FAQCreate,
    update_schema=FAQUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)


# FastAPI 应用生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 初始化数据库表
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # 初始化 admin 界面
    await admin.initialize()
    yield
    
    # 清理资源
    await engine.dispose()


# 创建 FastAPI 应用
app = FastAPI(
    title="CRUDAdmin 示例应用",
    description="使用 CRUDAdmin 构建的管理界面",
    version="1.0.0",
    lifespan=lifespan
)

# 挂载 admin 界面到 /admin 路径
app.mount("/admin", admin.app)


# 根路径
@app.get("/")
async def root():
    return {
        "message": "欢迎使用 CRUDAdmin",
        "admin_url": "/admin",
        "docs_url": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
