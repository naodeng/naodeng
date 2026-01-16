# GitHub Actions 工作流说明

本目录包含用于自动更新 GitHub Profile README 的工作流配置。

## 📋 工作流

### Update README (`update-readme.yml`)

**功能：**
- 自动更新英文版 README 的最新博客文章列表
- 自动更新中文版 README 的最新博客文章列表
- 自动修复博客文章列表的格式问题

**触发条件：**
- 每天 UTC 时间 00:00 自动运行
- 手动触发（workflow_dispatch）
- 推送到 main/master 分支时

**工作流程：**
1. 从 RSS feed 获取最新博客文章（英文版）
2. 从 RSS feed 获取最新博客文章（中文版）
3. 运行 Python 脚本修复格式问题
4. 提交并推送更改

**博客文章更新：**
- 英文版 RSS Feed: `https://naodeng.com.cn/index.xml`
- 中文版 RSS Feed: `https://naodeng.com.cn/zh/index.xml`
- 最大文章数: 6 篇
- 更新位置: `<!-- BLOG-POST-LIST:START -->` 和 `<!-- BLOG-POST-LIST:END -->` 之间

## 🔧 格式修复脚本

### fix_blog_format.py

这个 Python 脚本会自动修复 `blog-post-workflow` 可能产生的格式问题：

**问题：** 博客文章列表可能显示在一行，没有换行
```markdown
- [文章1](链接1)- [文章2](链接2)- [文章3](链接3)
```

**修复后：**
```markdown
- [文章1](链接1)
- [文章2](链接2)
- [文章3](链接3)
```

**工作原理：**
1. 读取 README 文件
2. 查找 `<!-- BLOG-POST-LIST:START -->` 和 `<!-- BLOG-POST-LIST:END -->` 之间的内容
3. 使用正则表达式检测格式问题
4. 在每个 `](...)` 和 `- [` 之间添加换行符
5. 保存修复后的文件

## 🚀 手动触发工作流

1. 进入 GitHub 仓库的 Actions 标签页
2. 选择 "Update README" 工作流
3. 点击 "Run workflow" 按钮
4. 选择分支并确认运行

## 🐛 故障排查

### 博客文章格式仍然混乱

如果工作流运行后格式仍然有问题：

1. **检查工作流日志**
   - 进入 Actions 标签页
   - 查看最近的运行记录
   - 检查 "Fix Blog Post Formatting" 步骤的输出

2. **手动运行修复脚本**
   ```bash
   cd naodeng
   python .github/scripts/fix_blog_format.py
   ```

3. **检查 RSS Feed**
   - 确认 RSS feed URL 可访问
   - 验证 feed 格式正确

### 工作流失败

1. 检查 Actions 标签页中的错误日志
2. 确认仓库权限设置正确（需要 `contents: write`）
3. 验证 RSS feed URL 是否可访问
4. 检查 Python 脚本是否有语法错误

### 博客文章未更新

1. 确认 RSS feed 有新内容
2. 检查 README 中是否包含正确的注释标记
3. 查看工作流日志中的详细错误信息
4. 手动触发工作流测试

## 📝 自定义配置

### 修改更新频率

编辑 `cron` 表达式来改变运行频率：
```yaml
schedule:
  - cron: '0 0 * * *'    # 每天 00:00
  - cron: '0 */6 * * *'  # 每 6 小时
  - cron: '0 */12 * * *' # 每 12 小时
```

### 修改博客文章数量

在工作流文件中修改 `max_post_count` 参数：
```yaml
max_post_count: 10  # 显示 10 篇最新文章
```

### 修改 RSS Feed

更改 `feed_list` 参数：
```yaml
feed_list: "https://your-blog.com/feed.xml"
```

## 🔐 安全注意事项

- 所有工作流使用 `GITHUB_TOKEN`，无需额外配置
- Token 权限已限制为最小必要权限（`contents: write`）
- 建议定期检查工作流日志
- Python 脚本只修改 README 文件，不会访问其他文件

## 📚 相关资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Blog Post Workflow](https://github.com/gautamkrishnar/blog-post-workflow)
- [Python 正则表达式文档](https://docs.python.org/3/library/re.html)

## 🧪 本地测试

你可以在本地测试格式修复脚本：

```bash
# 进入项目目录
cd naodeng

# 运行修复脚本
python .github/scripts/fix_blog_format.py

# 查看更改
git diff README.md README_CN.md
```

如果脚本正常工作，你会看到：
- `✓ Fixed formatting in README.md` - 如果有修复
- `✓ Format looks good in README.md` - 如果格式正确
