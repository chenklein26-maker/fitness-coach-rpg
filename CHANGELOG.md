# CHANGELOG

## v0.2 · 2026-08

### 架构升级
- 日志拆分：单一 FITNESS-LOG 拆成 PROFILE / CURRENT-STATE / CURRENT-PLAN / sessions / story，Markdown 给人读 + JSON 给机器读
- 确定性脚本：4 个零依赖 Python 脚本（init / append / update / validate），把"必须准确"的部分交给确定性逻辑
- 单一事实源：属性只存 CURRENT-STATE.json，story/STATE 用 character_ref 引用不复制
- 降级路径：无 Python 环境时 AI 可手写 JSON

### Skill 规范化
- frontmatter 精简为 name + description（跨平台触发兼容）
- skills/ 目录清空，STORY-ENGINE 移至 references/

### 训练规则
- 恢复判断从"只看停练天数"升级为"停练基线 + 6 修正因子"
- 高级技巧解锁改为多条件（训练经验 / 无疼痛 / 动作稳定 / 恢复），不再仅凭 Lv.3

### 交互
- 6 种交互模式（快速开始 / 制定计划 / 实时跟练 / 复盘 / 复训 / 剧情）
- 初始化降阻力：首次只问 4 项，其余后续补齐

### RPG 奖励
- EXP 奖励健康行为（诚实记录疼痛 / 合理降重 / 长期一致性），不奖励大重量硬撑
- PR 从 +20 降为 +10（里程碑，非主要来源）

### 测试
- 回归测试 4 自动场景 + 8 场景文档

## v0.1 · 2026-05
- 公开预览版首发
- 可复用 SKILL.md + 三类示例档案 + 通用叙事引擎 + 默认世界模板
