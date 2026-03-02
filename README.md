# holyMyPics 全人类最神秘的图像聚集地

此项目由Qt图形化图片管理器, 和我多年收集得来的神秘图片组成
你可以轻易地通过程序检索, 复制, 添加, 删除图片

## 技术栈

- Python 3.9+
- PySide6 (Qt for Python) – GUI 框架
- SQLite3 – 本地数据库
- Pillow – 图像处理与缩略图生成
- pyperclip – 剪贴板操作

## 安装与运行

1. 克隆仓库：
   ```bash
   git clone https://github.com/yourname/holymypics.git
   cd holymypics
   ```
2. 运行程序：
    双击运行`run.sh`或者`run.bat`
    ```bash
    ./.venv/bin/python3.14 main.py
    ```
    或者
    ```bash
    uv run main.py
    ```
    首次运行会自动创建 `pics.db` 和 `pics/` 目录。

## 使用简介
- **添加文件**：点击右下角“添加文件”，选择图片，输入昵称和标签（多个标签用逗号分隔），提交即可。
- **搜索**：在左侧标签列表（可通过“显示所有标签”添加）和右侧昵称输入框输入条件，点击“搜索”按钮。
- **查看/编辑图片**：点击任意缩略图，在详情窗口中可以修改信息、复制路径、打开文件夹等。
---
## 项目结构
```
holymypics/
├── main.py              # 程序入口
├── utils/
│   ├── database.py      # 数据库初始化及查询接口
│   ├── fileworks.py     # 文件操作（哈希、复制、删除）
│   ├── slots.py         # 所有槽函数（业务逻辑）
│   └── widgets.py       # 自定义控件（ImageLabel, ImageViewer）
├── pics/                # 存储文件的目录（自动创建）
└── pics.db              # SQLite 数据库（自动创建）
```
---
## 许可证
MIT
