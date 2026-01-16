# GitHub Actions 工作流说明

本目录包含用于自动更新 GitHub Profile README 的工作流配置。

## 📋 工作流列表

### 1. Update README (`update-readme.yml`)

**功能：**
- 自动生成 GitHub 贡献蛇形动画
- 自动更新最新博客文章列表

**触发条件：**
- 每天 UTC 时间 00:00 自动运行
- 手动触发（workflow_dispatch）
- 推送到 main/master 分支时

**生成内容：**
- `github-contribution-grid-snake.svg` - 浅色主题蛇形图
- `github-contribution-grid-snake-dark.svg` - 深色主题蛇形图
- `github-contribution-grid-snake.gif` - 动画 GIF 版本

**所需权限：**
- `contents: write` - 用于提交更新

### 2. GitHub Profile Summary (`profile-summary.yml`)

**功能：**
- 更新 GitHub 统计数据卡片
- 生成个人资料摘要

**触发条件：**
- 每 6 小时自动运行一次
- 手动触发（workflow_dispatch）

**所需权限：**
- `contents: write` - 用于提交更新

## 🔧 配置说明

### 博客文章更新

博客文章通过 RSS feed 自动获取：
- Feed URL: `https://naodeng.com.cn/index.xml`
- 最大文章数: 6 篇
- 更新位置: README.md 中的 `<!-- BLOG-POST-LIST:START -->` 和 `<!-- BLOG-POST-LIST:END -->` 之间

### 蛇形动画

蛇形动画会被推送到 `output` 分支，可以通过以下 URL 访问：
```
https://raw.githubusercontent.com/naodeng/naodeng/output/github-contribution-grid-snake-dark.svg
```

## 🚀 手动触发工作流

1. 进入 GitHub 仓库的 Actions 标签页
2. 选择要运行的工作流
3. 点击 "Run workflow" 按钮
4. 选择分支并确认运行

## 📊 工作流状态徽章

可以在 README 中添加以下徽章来显示工作流状态：

```markdown
![Update README](https://github.com/naodeng/naodeng/actions/workflows/update-readme.yml/badge.svg)
![Profile Summary](https://github.com/naodeng/naodeng/actions/workflows/profile-summary.yml/badge.svg)
```

## 🔍 故障排查

### 工作流失败

1. 检查 Actions 标签页中的错误日志
2. 确认仓库权限设置正确
3. 验证 RSS feed URL 是否可访问
4. 检查 GitHub Token 权限

### 博客文章未更新

1. 确认 RSS feed 格式正确
2. 检查 README 中是否包含正确的注释标记
3. 查看工作流日志中的详细错误信息

### 蛇形动画未显示

1. 确认 `output` 分支已创建
2. 检查图片 URL 是否正确
3. 等待几分钟让 GitHub Pages 更新

## 📝 自定义配置

### 修改更新频率

编辑 `cron` 表达式来改变运行频率：
```yaml
schedule:
  - cron: '0 0 * * *'  # 每天 00:00
  - cron: '0 */6 * * *'  # 每 6 小时
  - cron: '0 */12 * * *'  # 每 12 小时
```

### 修改博客文章数量

在 `update-readme.yml` 中修改 `max_post_count` 参数：
```yaml
max_post_count: 10  # 显示 10 篇最新文章
```

## 🔐 安全注意事项

- 所有工作流使用 `GITHUB_TOKEN`，无需额外配置
- Token 权限已限制为最小必要权限
- 建议定期检查工作流日志

## 📚 相关资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Blog Post Workflow](https://github.com/gautamkrishnar/blog-post-workflow)
- [Snake Animation Generator](https://github.com/Platane/snk)
- [GitHub Profile README Generator](https://github.com/rahuldkjain/github-profile-readme-generator)
