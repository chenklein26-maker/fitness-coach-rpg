# Fitness Coach RPG 🎮💪

> 一个可开新档的 AI 健身教练框架：训练记录、RPG 属性成长、剧情推进三者联动

![License](https://img.shields.io/github/license/chenklein26-maker/fitness-coach-rpg)

一个可开新档的 AI 健身教练框架：训练记录、RPG 属性成长、剧情推进三者联动，但世界观、角色和主线由使用者自己探索与定义。

这不是某个固定角色的存档分享，而是一套可复用的玩法系统。你可以把它当作：

- 本地文件驱动的 AI 健身教练
- 带长期成长感的训练记录系统
- 可自定义世界观的训练叙事框架

**English:** A reusable AI fitness coach framework powered by local Markdown logs, long-term progression, and optional story mode.

---

## ✨ 核心特性

- 📝 **智能训练记录**：自动追踪重量、次数、RPE、体感反馈
- 📊 **渐进式成长**：等级、属性、经验值系统
- 🎭 **剧情模式**：训练转化为叙事，打造专属冒险
- 🔄 **恢复感知**：智能判断中断后的恢复强度
- 🎨 **高度自定义**：教练风格、RPG主题、世界观自由设定
- 📁 **本地持久化**：Markdown 文件存储，安全可控
- 🤖 **持续学习**：越用越懂你的训练偏好

---

## Quick Intro (EN)

Fitness Coach RPG helps you build a long-running training system with:

- workout logging (weight, reps, RPE, notes)
- recovery-aware planning (including comeback after breaks)
- optional RPG progression and story mode
- local-file structure for long-term continuity and customization

If you want to run your own "save file" instead of inheriting someone else's story world, this repo is built for that.

---

## 适合谁

- 想把训练记录做得更长期、更有反馈感的人
- 喜欢 RPG 成长、称号、属性、剧情推进的人
- 希望 AI 不只是记录训练，还能长期陪练的人

---

## 越用越智能

这个 Skill 不是一次性工具——它随着你的使用变得越来越懂你。

- **每次训练后跟 AI 聊几句**：不只是记数据，说说今天的体感、哪里酸、心情怎样。AI 会记住你的偏好、弱项和进步节奏
- **训练记录越多，建议越精准**：AI 会参考你上周的重量、上次的 RPE、甚至两个月前的旧伤来调整今天的计划
- **你的对话是它的记忆**：你说过"右肩不太舒服"或"早上训练状态更好"——下次它会主动问

简单说：**别只把训练日志当记事本，把它当教练。你越用它，它越懂你。**

---

## 选择你的教练

预设训练方法论来自**凯圣王×谭指导**（偏向力量增长和三分化训练）。如果你的目标是塑形、减脂、瑜伽或体态矫正，我们提供了一份 **[教练风格指南](references/coach-guide.md)**，介绍了 6 位不同方向的健身博主：

| 教练 | 方向 | 适合 |
|:---|:---|:---|
| **周六野 Zoey** | 塑形、减脂 | 新手到中级，温柔鼓励 |
| **帕梅拉 Pamela Reif** | HIIT、全身塑形 | 有基础，追求效率 |
| **林芊妤 Coffee Lam** | 瑜伽、瑜伽塑形 | 喜欢瑜伽和拉伸 |
| **欧阳春晓** | 瘦腿、体态矫正 | 关注腿型和体态 |
| **韩小四** | 温和减脂 | 零基础、怕受伤 |
| **海洋饼干** | 减脂、全身塑形 | 中等强度，训练饮食并重 |

初始化时告诉 AI "我想跟周六野练" 或 "力量日跟凯圣王，有氧跟帕梅拉"——选你喜欢的就好。

---

## 你会得到什么

- 一个带训练日志、属性成长、恢复判断的教练系统
- 一套可选开启的剧情模式
- 一组可自定义的世界模板、叙事模板和训练方法论参考
- 一套本地文档结构，方便长期维护与迁移

---

## 🚀 快速开始

1. 将本仓库放进你的 AI 工作区或 Skill 工作区。
2. 在 AI 对话中说“开始训练”或“初始化档案”。
3. AI 会自动读取示例模板并引导你完成首次设定。

> 💡 **提示**：AI Agent 会自动处理文件创建，无需手动操作。

---

### 📋 手动操作方式

```bash
# 克隆项目
git clone https://github.com/chenklein26-maker/fitness-coach-rpg.git
cd fitness-coach-rpg

# 方式一：用脚本初始化（需要 Python 3.8+）
python scripts/init_profile.py --name 你的名字 --theme 武侠

# 方式二：手动复制模板
cp -r assets/starter-profile user-data
# 然后编辑 user-data/PROFILE.md 和 CURRENT-STATE.json 填入你的信息
```

> 脚本零外部依赖，只用 Python 标准库。没有 Python 环境？见下方[降级路径](#降级路径)。

### 两种起步方式

- **懒得自己搭世界？** 把 `worlds/default/` 里的 `WORLD-LOG.md` 复制到 `user-data/story/WORLD.md`，这是一套完整的预置世界（共振法则剑与魔法）。
- **想自己创建世界？** 用 `assets/starter-profile/story/WORLD.md` 模板，从零填自己的设定。

---

## 运行环境

本 Skill 更适合运行在支持以下能力的 AI 环境中：

- 可读取和写入本地文件
- 可持续访问同一工作区中的多个 Markdown 文件
- 最好支持时间获取、长期上下文或 Skill/工具调用

它不是“复制到任意聊天窗口就能完整运行”的纯提示词项目，更接近一个依赖本地文件结构的工作区模板。

### 降级路径

没有 Python 环境，或环境不支持完整 Skill 机制时，也能用：

- AI 直接手写 `user-data/sessions/YYYY-MM-DD.json`（格式见 `assets/starter-profile/example-session.json`，字段简单，AI 能写准）
- AI 手动维护 `user-data/CURRENT-STATE.json` 的 exp/level/属性（脚本只是让更新更可靠，不是必需）
- 把 `CURRENT-STATE.json` 和 `story/WORLD.md` 当作长期上下文资料
- 让 AI 根据这些文件提供训练建议、复盘和剧情推进

### 关于能力依赖

`SKILL.md` 不再使用 `requires` 字段。需要的能力：

- 时间获取：系统时间工具或手动输入
- 文件读写：本地 JSON/Markdown 读写
- 可选：Python 3.8+（用于脚本，没有也能跑）

---

## 目录结构

```text
├── README.md
├── SKILL.md
├── CHANGELOG.md
├── references/
│   ├── coach-wang-tan-method.md
│   ├── coach-guide.md
│   ├── narrative-templates.md
│   ├── rpg-rules.md
│   └── story-engine.md
├── worlds/
│   └── default/
│       ├── WORLD-LOG.md
│       └── STORY-LOG.md
├── assets/
│   └── starter-profile/
│       ├── PROFILE.md
│       ├── CURRENT-PLAN.md
│       ├── CURRENT-STATE.json
│       ├── example-session.json
│       └── story/
│           ├── WORLD.md
│           └── STATE.json
├── scripts/
│   ├── init_profile.py
│   ├── append_session.py
│   ├── update_summary.py
│   └── validate_state.py
└── examples/
    ├── completed-save/
    │   ├── README.md
    │   ├── CURRENT-STATE.json
    │   ├── sessions/
    │   │   └── 2026-07-29.json
    │   └── story/
    │       └── STATE.json
    ├── MINIMAL-RUN.md
    ├── AUTHOR-WORLD-SAMPLE.md
    └── AUTHOR-DESIGN-NOTES.md
```

---

## 核心设计

- `user-data/PROFILE.md`
  静态个人档案（姓名、目标、设备、教练体系、伤病史）。
- `user-data/CURRENT-STATE.json`
  动态状态快照（等级、属性、EXP、recovery、recent_bests），由 `update_summary.py` 维护。
- `user-data/CURRENT-PLAN.md`
  本周训练计划，由 AI 或用户维护。
- `user-data/sessions/YYYY-MM-DD.json`
  每日训练记录（动作、组数、重量、RPE、疼痛），追加不覆盖。
- `user-data/story/WORLD.md`
  静态世界设定。记录世界规则、角色背景、NPC 和地点。
- `user-data/story/STATE.json`
  动态剧情状态（章节、任务、伏笔）。
- `references/story-engine.md`
  训练如何映射到叙事的通用逻辑，不绑定固定主线。

---

## 自定义建议

你可以只改 3 件事，就做出自己的版本：

1. 换教练方法论
   预设的是凯圣王×谭指导（力量/增肌向），不同训练目标可选 [教练风格指南](references/coach-guide.md) 中的其他教练。也可以完全替换为你熟悉的其他训练体系。

2. 换 RPG 主题
   在 `references/rpg-rules.md` 中新增你的称号体系和主题语言。

3. 换世界观
   不想自己搭？直接用 `worlds/default/` 里的预置世界。想从头来？从 `assets/starter-profile/story/WORLD.md` 开始定义你自己的设定。

---

示例内容仅用于说明结构，不代表唯一玩法。每个使用者都可以开出自己的档，定制自己的世界和角色。

`examples/` 中的设计笔记和世界示例用于启发，不要求照搬。

---

## 👤 关于作者

- **小红书**：[@龙酱](https://www.xiaohongshu.com/user/profile/5c63da27000000001202556a)
- **GitHub**：https://github.com/chenklein26-maker/fitness-coach-rpg

---

## 许可

详见 [LICENSE](./LICENSE)。
