# 第 6 课：Slash Commands——控制、审查与恢复

**用时：10–15 分钟**

## 学习目标

- 不依赖 Agent 的自我报告，检查实际修改。
- 用不同类型的审查发现问题。
- 知道如何回到安全状态。

## 1. `/diff`：看实际修改

输入：

```text
/diff
```

关注：Agent 修改了哪些文件？是否碰了 `inputs/`？是否加入了外部 CDN？

> 如果课程目录没有初始化 Git，`/diff` 的体验可能受限。此时让 Agent 列出 `site/` 新文件，并使用检查器；真实项目建议使用 Git。

## 2. `/code-review`：独立找正确性问题

输入：

```text
/code-review high site/
```

或者使用课程提示：

```text
请执行 @prompts/review.txt
```

审查重点：

- 评分方向是否写反；
- 权重归一化是否稳定；
- 数据来源是否与显示值一致；
- 键盘操作和窄屏布局是否可用。

## 3. `/simplify`：清理实现

`/code-review` 主要寻找正确性缺陷，`/simplify` 关注复用、简化和可维护性。二者不是同一个任务。

```text
/simplify site/
```

## 4. `/rewind`：恢复检查点

在做一个明显的视觉实验前输入：

```text
把整个网页改成荧光绿色，并隐藏来源区。
```

不要真的保留它。使用：

```text
/rewind
```

选择恢复代码和/或对话。讲师演示时也可以只说明选项，不执行破坏性修改。

## 5. `/memory` 与 `/skills`

它们不是生产网页的“魔法命令”，而是查看 Agent 长期背景和可复用能力的控制入口。

## 检查点

用一句话说明下面三者差异：

- `/code-review`
- `/simplify`
- `/rewind`

下一步：[`07-reflect.md`](07-reflect.md)
