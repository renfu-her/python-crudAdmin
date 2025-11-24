# CRUDAdmin 管理界面

这是一个使用 [CRUDAdmin](https://benavlabs.github.io/crudadmin/) 构建的 FastAPI 管理界面示例项目。

## 功能特性

- 🔒 内置用户认证系统
- 📊 自动生成的管理界面
- 🛡️ 安全特性（CSRF 保护、速率限制等）
- 📝 事件跟踪和审计日志
- 🎨 现代化的响应式 UI

## 快速开始

### 1. 安装依赖

项目使用 `uv` 作为包管理器：

```bash
uv sync
```

### 2. 配置环境变量（可选）

复制 `.env.example` 到 `.env` 并修改配置：

```bash
cp .env.example .env
```

### 3. 运行应用

```bash
uv run python main.py
```

或者使用 uvicorn：

```bash
uv run uvicorn main:app --reload
```

### 4. 访问管理界面

- **管理界面**: http://localhost:8000/admin
- **API 文档**: http://localhost:8000/docs
- **默认管理员账号**:
  - 用户名: `admin`
  - 密码: `admin123`

⚠️ **重要**: 生产环境请务必更改默认密码和 SECRET_KEY！

## 项目结构

```
.
├── main.py          # FastAPI 应用和 CRUDAdmin 配置
├── models.py        # SQLAlchemy 数据库模型
├── schemas.py       # Pydantic 数据验证 schemas
├── pyproject.toml   # 项目配置和依赖
└── README.md        # 项目说明
```

## 已配置的模型

### User (用户)
- 用户名、邮箱、全名
- 激活状态
- 创建和更新时间

### Product (产品)
- 产品名称、描述
- 价格、库存
- 可用状态
- 创建和更新时间

## 自定义配置

### 添加新模型

1. 在 `models.py` 中定义 SQLAlchemy 模型
2. 在 `schemas.py` 中创建对应的 Pydantic schemas
3. 在 `main.py` 中使用 `admin.add_view()` 添加模型

示例：

```python
# 在 main.py 中添加
admin.add_view(
    model=YourModel,
    create_schema=YourModelCreate,
    update_schema=YourModelUpdate,
    allowed_actions={"view", "create", "update", "delete"}
)
```

### 生产环境配置

参考 [CRUDAdmin 文档](https://benavlabs.github.io/crudadmin/#usage) 配置：

- Redis session backend
- PostgreSQL/MySQL 数据库
- HTTPS 和安全 cookies
- IP 限制和速率限制

## 依赖

- Python >= 3.11
- FastAPI
- CRUDAdmin (with memcached and mysql extras)
- SQLAlchemy 2.0+
- Pydantic 2.0+

## 参考文档

- [CRUDAdmin 官方文档](https://benavlabs.github.io/crudadmin/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/)

## 许可证

MIT

