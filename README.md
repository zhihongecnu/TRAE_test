# Manim 示例项目

这是一个使用 Manim 创建的简单数学动画示例项目。

## 文件结构

- `example_scene.py`: 包含 Manim 场景定义的 Python 脚本。
- `README.md`: 本文件，项目说明。
- `.gitignore`: 指定 Git 应忽略的文件和目录。

## 如何运行

1.  **安装 Manim**: 如果你还没有安装 Manim，请根据你的操作系统和偏好，参照 [Manim 官方文档](https://docs.manim.community/en/stable/installation/index.html)进行安装。

2.  **渲染场景**: 打开终端或命令行，导航到项目目录，然后运行以下命令来渲染 `example_scene.py` 中的特定场景。例如，要渲染 `SquareToCircle` 场景：

    ```bash
    manim -pql example_scene.py SquareToCircle
    ```

    或者渲染 `BasicShapes` 场景：

    ```bash
    manim -pql example_scene.py BasicShapes
    ```

    或者渲染 `TextExample` 场景：

    ```bash
    manim -pql example_scene.py TextExample
    ```

    参数说明：
    - `-p`: 预览生成的动画。
    - `q`: 设置渲染质量，`l` 代表低质量（渲染速度快），`m` 代表中等质量，`h` 代表高质量，`k` 代表 4K 质量。
    - `l`: 低质量渲染。

    渲染完成后，视频文件将保存在 `media/videos/example_scene/480p15/` 目录下（具体路径可能因 Manim 版本和配置而异）。

3.  **批量渲染所有场景**: 项目中提供了一个 `render_scenes.sh` 脚本，可以一次性渲染 `example_scene.py` 中的所有场景。

    ```bash
    chmod +x render_scenes.sh
    ./render_scenes.sh
    ```
    该脚本会自动查找 `example_scene.py` 文件中定义的所有场景类，并逐个进行渲染。渲染的视频同样保存在 `media/videos/example_scene/480p15/` 目录下。

## 示例场景

-   `SquareToCircle`: 一个正方形变换成一个圆形的动画。
-   `BasicShapes`: 同时创建并显示圆形、正方形和三角形的动画。
-   `TextExample`: 展示如何创建和动画化文本及数学公式。

## GitHub Actions 自动化

本项目配置了 GitHub Actions，可以在每次向 `main` 分支推送代码或创建指向 `main` 分支的 Pull Request 时自动执行以下操作：

1.  **检出代码 (Checkout code)**: 获取最新的代码库。
2.  **设置 Python (Set up Python)**: 配置 Python 3.9 环境。
3.  **安装 Manim 及依赖 (Install Manim and dependencies)**: 安装 Manim 及其所需的系统依赖（如 FFmpeg, LaTeX 等）。
4.  **使渲染脚本可执行 (Make render script executable)**: 赋予 `render_scenes.sh` 执行权限。
5.  **渲染所有场景 (Render all scenes)**: 执行 `render_scenes.sh` 脚本来生成所有视频。
6.  **上传视频产物 (Upload video artifacts)**: 将 `media/videos/example_scene/480p15/` 目录下的所有视频文件作为构建产物 (artifact) 上传，名为 `manim-videos`。你可以在 GitHub Actions 的运行结果页面下载这些视频。

你可以在 `.github/workflows/manim_render.yml` 文件中查看和修改此工作流程的配置。

## Manim 简介

Manim 是一个用于创建精确数学动画的 Python 库。它最初由 Grant Sanderson (3Blue1Brown) 开发，用于制作他的数学教育视频。Manim 允许用户通过编程方式定义和控制动画的各个方面，从而能够创建出复杂且富有表现力的视觉效果来解释数学概念。

### 主要特性

-   **基于 Python**: 使用 Python 语言编写，易于学习和使用。
-   **LaTeX 支持**: 内置对 LaTeX 的强大支持，可以轻松渲染高质量的数学公式。
-   **面向对象**: 动画元素（称为 Mobjects）是 Python 对象，可以进行操作和变换。
-   **强大的动画控制**: 提供丰富的动画类型和控制选项，如 `Create`, `Transform`, `FadeIn`, `FadeOut`, `Write` 等。
-   **社区驱动**: Manim 有一个活跃的社区版本 (Manim Community)，不断进行开发和改进。

要了解更多信息，请访问 [Manim Community 网站](https://www.manim.community/)。