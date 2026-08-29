# 课程检查器

检查器只依赖 Python 标准库，用于确认课程结构和网页关键挂钩存在。

## 检查课程配置

```bash
python3 checks/check-project.py setup
```

验证输入资料、8 节课程、`CLAUDE.md`、Skill 和三个只读 Subagents。

## 检查学生网页

```bash
python3 checks/check-project.py student
```

在完成第 5 课、根目录出现 `site/` 后运行。它检查关键区域和计算/渲染挂钩，不证明视觉和业务逻辑完全正确。

## 检查讲师参考网页

```bash
python3 checks/check-project.py reference
```

确认参考网页包含情景、权重、排名、风险、证据结构，并且没有外部网络依赖。

## 全部检查

```bash
python3 checks/check-project.py all
```

在学生还没有创建 `site/` 前，`all` 预期会在 student 阶段失败。这是正常的学习检查点，而不是课程包损坏。

## 为什么还需要人工验证

结构检查不会发现所有问题。还需要：

- 在浏览器切换全部情景；
- 操作滑块并确认总和为 100%；
- 检查推荐解释是否同步；
- 在手机宽度和键盘下使用；
- 用 `/code-review` 检查计算与证据一致性。
