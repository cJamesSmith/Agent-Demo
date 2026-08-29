# 72 小时出海决策室

> 一门通过构建真实网页，学习 Claude Code 核心工作方式的动手课。

## 你的身份

你不是程序员，而是公司国际业务负责人。CEO 要求团队在 72 小时内回答：

1. 越南、印度尼西亚、泰国，应该优先进入哪个市场？
2. 建议基于哪些证据？
3. 战略偏好变化后，结论是否仍然成立？

你将使用 Claude Code，把 `inputs/` 中的虚构业务资料制作成一个可交互的高管决策网页。

## 你会学到什么

| 能力 | 在项目中的作用 | 企业类比 |
|---|---|---|
| Planning | 先阅读资料并提交实施方案 | 项目立项与方案评审 |
| Memory | 持续遵循受众、合规和表达规则 | 员工手册 |
| Skills | 复用高管决策网页的方法论 | 标准作业程序 |
| Subagents | 并行引入市场、财务和设计视角 | 跨职能项目组 |
| Slash Commands | 控制、检查和恢复 Agent 工作 | 管理控制台 |

## 最终成果

你会得到 `site/` 目录，其中包含：

- CEO 摘要和推荐市场
- 三国关键指标比较
- 增长、利润、风险三种战略情景
- 可调节的权重滑块
- 自动更新的排名和推荐解释
- 风险热力图与 90 天行动计划
- 可追溯的来源、假设和数据缺口

## 项目地图

```text
inputs/       需要 Agent 阅读的虚构业务材料
lessons/      学生按顺序完成的课程
prompts/      可直接复制到 Claude Code 的提示词
.claude/      Memory 以外的 Skills 与 Subagents
starter/      未完成的网页骨架
checks/       阶段性自检工具
reference/    讲师兜底成品（请先不要打开）
```

## 学习路径

按顺序打开以下文件：

1. [`lessons/00-setup.md`](lessons/00-setup.md) — 熟悉项目并做准备
2. [`lessons/01-planning.md`](lessons/01-planning.md) — 先计划，不改文件
3. [`lessons/02-memory.md`](lessons/02-memory.md) — 认识项目长期规则
4. [`lessons/03-skills.md`](lessons/03-skills.md) — 调用组织方法论
5. [`lessons/04-subagents.md`](lessons/04-subagents.md) — 组建虚拟专家团队
6. [`lessons/05-build.md`](lessons/05-build.md) — 构建并运行网页
7. [`lessons/06-slash-commands.md`](lessons/06-slash-commands.md) — 审查、比较和恢复
8. [`lessons/07-reflect.md`](lessons/07-reflect.md) — 总结与迁移到真实工作

标准课堂约 60–90 分钟；讲师可使用 `COURSE-GUIDE.md` 中的快速路径压缩到 25–35 分钟。

## 两种输入要分清

课程会用下面两种标记：

**输入 Claude Code：**

```text
请先阅读 inputs 目录……
```

**在终端运行：**

```bash
python3 checks/check-project.py setup
```

如果你正在 Claude Code 交互界面里，需要亲自执行终端命令，可以输入：

```text
! python3 checks/check-project.py setup
```

## 三条课堂规则

1. 不要先看 `reference/site/`，它是故障兜底，不是答案起点。
2. 在批准计划前，不让 Agent 修改网页。
3. 不只看 Agent 说了什么，还要用浏览器、检查器和审查命令验证结果。

## 数据声明

本项目中的公司、人物、访谈、市场数字和结论全部为教学目的虚构，不代表真实市场研究，不应用于实际投资或经营决策。
