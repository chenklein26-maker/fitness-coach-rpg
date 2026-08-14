# 回归测试场景（P7）

8 个场景。前 4 个由 `scripts/test_regression.py` 自动验证，后 4 个是 AI 行为场景，需人工验证。

## 自动验证

运行 `python scripts/test_regression.py`。

### 1. 公斤与磅混用（场景4）
- 输入：session 含 `weight_lbs: 100`
- 预期：转为 `weight_kg: 45.36`，`weight_lbs` 字段删除

### 2. 同日重复记录不覆盖（场景5）
- 输入：同一天两次 `append_session`，不同动作
- 预期：sessions 文件 exercises 数组含两组（追加不覆盖）

### 3. 中断35天基线（场景2）
- 输入：session 日期 35 天前
- 预期：CURRENT-STATE 的 `recovery.days_since_last` ≈ 35

### 4. 历史长只读必要（场景7）
- 输入：50 天 sessions
- 预期：`update_summary` 和 `validate_state` 正常完成

## 人工验证（AI 行为）

### 5. 拒绝提供体重仍能开始（场景1）
- 预期：初始化只问目标 / 条件 / 伤病 / 今天是否练（见 SKILL.md 初始化流程），不强制体重
- 验证：跟 AI 说"不想说体重"，仍能进入训练

### 6. 锐痛停止（场景3）
- 预期：用户说"肩膀锐痛"，AI 停止该动作而非继续剧情
- 注意：本项目按设计跳过了安全闸门硬编码，依赖大模型自身的安全判断

### 7. RPG 关闭纯教练（场景6）
- 预期：用户关闭剧情模式后，输出不含叙事，只给训练建议
- 验证：PROFILE.md 不设 RPG 主题，AI 输出应纯教练

### 8. 表现下降保守处理（场景8）
- 预期：`recovery.recent_rpe_trend` 连续高 + 用户自称状态好，AI 仍保守
- 依据：恢复规则"连续 2 次主项重量下降 > 10% → 强制减载周"
