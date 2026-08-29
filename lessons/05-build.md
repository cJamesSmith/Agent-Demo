# 第 5 课：让 Agent 构建网页

**用时：15–25 分钟**

## 学习目标

- 从已经评审的计划开始执行，而不是重新随意生成。
- 让 Agent创建、运行并验证一个完整网页。
- 用自然语言进行一次战略方向变更。

## 步骤 1：开始实施

输入 Claude Code：

```text
请基于已经批准的计划、项目 Memory、executive-dashboard Skill，以及三个 Subagents 的综合结论，执行 @prompts/build-dashboard.txt
```

Agent 应创建根目录下的 `site/`，而不是修改 `reference/site/`。

## 步骤 2：结构检查

在终端运行：

```bash
python3 checks/check-project.py student
```

结构检查只能证明关键元素存在，不能证明网页好用。

## 步骤 3：运行网页

在终端运行：

```bash
python3 -m http.server 8000
```

打开：

```text
http://localhost:8000/site/
```

也可以直接让 Claude Code 使用 `/run`：

```text
/run
```

## 步骤 4：人工验收

逐项操作：

- 切换增长、利润、风险三种情景；
- 调整一个权重，排名应立即更新；
- 权重总和应始终为 100%；
- 展开来源和假设；
- 缩窄浏览器窗口，页面不应横向溢出；
- 推荐区应同时出现反对理由。

## 步骤 5：模拟高管临时改变偏好

输入：

```text
请执行 @prompts/executive-change.txt
```

观察 Agent 是否保留原有情景，并解释推荐变化，而不是只修改一个标题。

## 检查点

网页必须让观看者分辨：

- 数据表中的事实；
- 研究员或 Agent 的推断；
- 需要验证的假设。

下一步：[`06-slash-commands.md`](06-slash-commands.md)
