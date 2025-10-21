# Zero2AI — From Zero to AI Engineer ｜ 从零到 AI 工程师

[![version](docs/badges/version.svg)](./pyproject.toml) [![build](docs/badges/build.svg)](./Makefile) [![coverage](docs/badges/coverage.svg)](./docs/roadmap.md) [![license](docs/badges/license.svg)](./LICENSE) [![python](docs/badges/python.svg)](./pyproject.toml)



## 1. 📖 Introduction ｜ 简介

Zero2AI 是一个教你从零基础到完全掌握人工智能核心能力的开源项目。我们收集了优质的教育资源（博客、网站、课程、论文、书籍、笔记等），制定了一条清晰的自学路线，帮助你系统性地学习编程、数学、AI原理等核心技能，最终成长为AI算法工程师。

Zero2AI is an open-source project that takes you from absolute beginner to full mastery of core AI capabilities. We have curated high-quality educational resources—blogs, websites, courses, papers, books, notes, and more—and mapped out a clear self-study roadmap that guides you step-by-step through programming, mathematics, AI principles, and other essential skills, ultimately turning you into an AI algorithm engineer.


## 2. ✨ Core Features ｜ 核心内容

- 📚 **优质教育资源整合** ｜ 收集整理博客、网站、课程、论文、书籍、笔记等优质学习资源
- 🧭 **清晰自学路线** ｜ 制定从零基础到AI算法工程师的完整学习路径
- 📦 **可运行实践材料** ｜ 配套各个课程可运行的jupyternotebook与python文件
- 🧪 **内置测试验证** ｜ 示例内置快测，确保学习效果
- 🐳 **可复现环境** ｜ Docker / uv 一键部署，降低学习门槛
- 🎯 **系统性技能培养** ｜ 覆盖编程、数学、AI原理等核心能力
- 📖 **离线友好文档** ｜ 本地可离线文档，随时随地学习
- 🤝 **社区支持** ｜ 欢迎和我共同建设这个项目，共同进步

## 3. 🛠️ Environment Preparation ｜ 环境准备

### 系统要求 ｜ System Requirements

- **Python**: 3.12+ （推荐使用最新版本）
- **操作系统**: Windows 10+, macOS 10.15+, Ubuntu 18.04+ 
- **内存**: 至少 4GB RAM（推荐 8GB+）
- **存储空间**: 至少 2GB 可用空间

### 方式一：本地环境安装 ｜ Local Environment Setup

#### 1) 安装 Python 和 uv ｜ Install Python & uv

```bash
# 安装 Python 3.12+ (如果尚未安装)
# Windows: 从 https://python.org 下载安装包
# macOS: brew install python@3.12
# Ubuntu: sudo apt install python3.12 python3.12-venv

# 安装 uv (Python 包管理工具)
pip install uv>=0.6.15
```

#### 2) 克隆项目 ｜ Clone Project

```bash
git clone https://github.com/your-org/zero2ai.git && cd zero2ai
```

#### 3) 安装依赖 ｜ Install Dependencies

```bash
# 使用 uv 安装项目依赖
uv sync --frozen || uv sync
```

#### 4) 验证安装 ｜ Verify Installation

```bash
# 运行 Hello World 测试
uv run python -c "print('Hello, Zero2AI')"

# 预期输出：Hello, Zero2AI
```

### 方式二：Docker 环境（推荐）｜ Docker Environment (Recommended)

#### 1) 安装 Docker ｜ Install Docker

```bash
# Windows/macOS: 从 https://docker.com 下载 Docker Desktop
# Ubuntu: sudo apt install docker.io
```

#### 2) 构建和运行 ｜ Build & Run

```bash
# 克隆项目
git clone https://github.com/your-org/zero2ai.git && cd zero2ai

# 构建 Docker 镜像
docker build -t zero2ai:latest .

# 运行容器
docker run --rm -it zero2ai:latest
```

#### 3) 挂载学习目录（可选）｜ Mount Learning Directory (Optional)

```bash
# 将本地项目目录挂载到容器中，方便编辑和学习
docker run --rm -it -v $(pwd):/app zero2ai:latest
```

## 4. ⚡ Quick Start ｜ 快速开始

### 🎯 学习方式选择 ｜ Learning Path Options

你可以选择以下任一方式开始学习：

1. **循序渐进**：按照第1-10部分的顺序系统学习
2. **按需学习**：根据当前水平选择相应章节
3. **实践导向**：直接运行感兴趣的代码示例


### 🛠️ 开发工具推荐 ｜ Recommended Development Tools

- **代码编辑器**: VS Code, PyCharm, Jupyter Lab
- **终端工具**: Windows Terminal, iTerm2 (macOS), Terminal (Linux)
- **版本控制**: Git + GitHub Desktop
- **Python 环境**: uv (推荐) 或 conda

### 📚 学习建议 ｜ Learning Advice

1. **完成环境验证**：确保所有示例都能正常运行
2. **选择学习路径**：根据你的基础选择合适的学习顺序
3. **动手实践**：不要只看代码，一定要动手运行和修改
4. **记录笔记**：在学习过程中记录重要概念和代码片段
5. **参与社区**：遇到问题可以联系作者或参与讨论

### ⚠️ 常见问题 ｜ Troubleshooting

**Q: 运行 `uv sync` 时出现错误**
```bash
# 解决方案：更新 uv 到最新版本
pip install --upgrade uv
```

**Q: Jupyter Notebook 无法启动**
```bash
# 解决方案：安装 Jupyter
uv add jupyter
```

**Q: Docker 容器无法访问文件**
```bash
# 解决方案：检查文件权限和挂载路径
docker run --rm -it -v $(pwd):/app -w /app zero2ai:latest
```


## 5. 📚 Documentation Index ｜ 文档索引

### 🛤️ Learning Path Guide  ｜  学习路径指引 
你可以按已经规划好的章节从头开始学习，也可以根据自己的实际情况选择性地进行学习：
- **第1部分：环境搭建** ｜ Environment Setup：`src/第1部分：环境搭建/README.md`
- **第2部分：Python基础** ｜ Python Fundamentals：`src/第2部分：Python基础/README.md`
- **第3部分：数据结构** ｜ Data Structures：`src/第3部分：数据结构/README.md`
- **第4部分：LeetCode算法** ｜ LeetCode Algorithms：`src/第4部分：LeetCode算法/README.md`
- **第5部分：数学和计算机基础** ｜ Math & CS Foundations：`src/第5部分：数学和计算机基础/ML-foundations/README.md`
- **第6部分：AI基础理论** ｜ AI Theory Fundamentals：`src/第6部分：AI基础理论/README.md`
- **第7部分：AI核心库** ｜ Core AI Libraries：`src/第7部分：AI核心库/README.md`
- **第8部分：动手深度学习** ｜ Hands-on Deep Learning：`src/第8部分：动手深度学习/README.md`
- **第9部分：AI领域论文** ｜ AI Research Papers：`src/第9部分：AI领域论文/README.md`
- **第10部分：大模型** ｜ Large Language Models：`src/第10部分：大模型/README.md`

### 📋 Project Management ｜ 项目管理 
- Root overview ｜ 根概览：`docs/README.md`
- Roadmap ｜ 路线图：`docs/roadmap.md`
- Good First Issues ｜ 新手任务：`docs/good-first-issues.md`

## 6. 🤝 Contributing & Connecting Us ｜ 贡献 & 联系我们

Please read `CONTRIBUTING.md` before contributing. New contributors can start from `docs/good-first-issues.md`.

在参与前请阅读 `CONTRIBUTING.md`。新手建议从 `docs/good-first-issues.md` 开始。

Please send E-mail to [zhang-weiye@foxmail.com](mailto:zhang-weiye@foxmail.com) to contact the author. 

## 7. 📄 License & Acknowledgements ｜ 许可证与致谢

- License ｜ 许可证：`LICENSE` (MIT)
- Thanks to contributors and educators whose materials inspired the curated structure.



