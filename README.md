# Research Notes

个人调研报告与技术笔记的静态站点，通过 GitHub Pages 在线访问。

**在线地址**: [https://jy815678-cpu.github.io/research-notes/](https://jy815678-cpu.github.io/research-notes/)

---

## 目录结构

```
research-notes/
├── src/                    # Markdown 源文件
│   └── pace/
│       ├── skill-tree.md
│       └── space-computing.md
├── tools/
│   └── md-to-html.py       # 转换脚本
├── output/                 # 生成的 HTML（推送到 gh-pages 分支）
└── README.md
```

## 本地构建

```bash
# 安装依赖
pip install markdown pymdown-extensions pygments

# 生成 HTML
python3 tools/md-to-html.py

# 推送更新
cd output
git add -A
git commit -m "Update site"
git push origin gh-pages
```

## 添加新报告

1. 将 Markdown 文件放入 `src/新的主题/` 目录
2. 运行 `python3 tools/md-to-html.py`
3. 在 `output/` 目录提交并推送到 `gh-pages` 分支

首页导航会自动更新。
