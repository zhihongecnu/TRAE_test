#!/bin/bash

# 脚本：render_scenes.sh
# 用途：渲染 example_scene.py 中的所有 Manim 场景

# 定义场景列表
# 从 example_scene.py 中自动提取所有 Scene 类的名称
SCENES=$(grep -oP 'class \K[a-zA-Z0-9_]+(?=\(Scene\))' example_scene.py)

if [ -z "$SCENES" ]; then
    echo "在 example_scene.py 中没有找到任何场景。"
    exit 1
fi

echo "找到以下场景："
for SCENE_NAME in $SCENES; do
    echo "- $SCENE_NAME"
done

echo "\n开始渲染..."

# 循环渲染每个场景
for SCENE_NAME in $SCENES; do
    echo "\n正在渲染场景: $SCENE_NAME"
    manim -ql example_scene.py $SCENE_NAME
    if [ $? -eq 0 ]; then
        echo "场景 $SCENE_NAME 渲染成功。"
    else
        echo "场景 $SCENE_NAME 渲染失败。"
    fi
done

echo "\n所有场景渲染完成。视频文件位于 media/videos/example_scene/480p15/ 目录中。"