# 第 3 课：Skills——把方法论做成可复用能力

**用时：8–12 分钟**

## 学习目标

- 查看当前项目提供的 Skill。
- 理解 Skill 与一次性 Prompt、Slash Command 的关系。
- 让 Agent 加载高管决策网页方法论。

## 步骤 1：列出 Skills

输入 Claude Code：

```text
/skills
```

找到 `executive-dashboard`。如果未出现，输入 `/reload-skills` 后重试。

## 步骤 2：明确调用

输入：

```text
/executive-dashboard 东南亚市场进入
```

然后追问：

```text
这个 Skill 为本项目增加了哪些仅靠 CLAUDE.md 没有提供的具体方法？
```

预期包括：评分规则、页面结构、证据标记、推荐与反对理由、敏感性分析。

## 步骤 3：观察渐进加载

Skill 的目录包含：

```text
.claude/skills/executive-dashboard/
├── SKILL.md
├── references/scoring.md
└── templates/page-outline.md
```

Agent 平时只看到 Skill 的名称和描述；被触发后才加载主说明，需要时再读取评分参考和页面模板。这叫“渐进披露”。

## Skill 与 Slash Command

- `/help`、`/memory` 等是内置 Slash Commands。
- 自定义能力现在推荐做成 Skill。
- 一个可由用户调用的 Skill 同时会提供 `/executive-dashboard` 这样的入口。
- Skill 还可以被 Agent 自动匹配，并能携带模板、脚本和参考资料。

## 检查点

请用一句话解释：

> Memory 保存 ________，Skill 保存 ________。

参考答案：持续适用的背景与规则；按需加载的专业方法和工作流。

下一步：[`04-subagents.md`](04-subagents.md)
