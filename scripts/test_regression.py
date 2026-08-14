#!/usr/bin/env python3
"""回归测试集（P7）。

自动验证脚本能测的场景。AI 行为场景见 references/test-scenarios.md。

用法：
    python scripts/test_regression.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta

ROOT = Path(__file__).resolve().parent.parent
STARTER = ROOT / "assets" / "starter-profile"
USER_DATA = ROOT / "user-data"  # 测试用，被 .gitignore 忽略

PASSED = 0
FAILED = 0


def setup():
    if USER_DATA.exists():
        shutil.rmtree(USER_DATA)
    shutil.copytree(STARTER, USER_DATA)


def teardown():
    if USER_DATA.exists():
        shutil.rmtree(USER_DATA)


def run_script(args, stdin=None):
    cmd = [sys.executable, str(ROOT / "scripts" / args[0])] + args[1:]
    return subprocess.run(cmd, input=stdin, capture_output=True, text=True, encoding="utf-8")


def check(name, condition, detail=""):
    global PASSED, FAILED
    if condition:
        PASSED += 1
        print(f"  ✅ {name}")
    else:
        FAILED += 1
        print(f"  ❌ {name} {detail}")


def test_lbs_to_kg():
    """场景4：公斤与磅混用，是否被识别转换。"""
    setup()
    today = datetime.now().strftime("%Y-%m-%d")
    session = '{"session_type":"push","exercises":[{"exercise":"bench","sets":[{"weight_lbs":100,"reps":8,"rpe":8}],"pain":{"location":null,"severity":0}}]}'
    run_script(["append_session.py"], stdin=session)
    f = USER_DATA / "sessions" / f"{today}.json"
    data = json.loads(f.read_text(encoding="utf-8"))
    w = data["exercises"][0]["sets"][0].get("weight_kg")
    check("lbs→kg 转换", w is not None and abs(w - 45.36) < 0.1, f"got {w}")
    check("weight_lbs 已删除", "weight_lbs" not in data["exercises"][0]["sets"][0])
    teardown()


def test_same_day_no_overwrite():
    """场景5：同一天重复记录，追加不覆盖。"""
    setup()
    today = datetime.now().strftime("%Y-%m-%d")
    s1 = '{"session_type":"push","exercises":[{"exercise":"bench","sets":[{"weight_kg":40,"reps":8,"rpe":8}],"pain":{"location":null,"severity":0}}]}'
    s2 = '{"session_type":"push","exercises":[{"exercise":"row","sets":[{"weight_kg":30,"reps":10,"rpe":8}],"pain":{"location":null,"severity":0}}]}'
    run_script(["append_session.py"], stdin=s1)
    run_script(["append_session.py"], stdin=s2)
    data = json.loads((USER_DATA / "sessions" / f"{today}.json").read_text(encoding="utf-8"))
    check("两组都保留（追加不覆盖）", len(data["exercises"]) == 2, f"got {len(data['exercises'])}")
    teardown()


def test_35day_baseline():
    """场景2：中断35天，days_since_last 反映。"""
    setup()
    old = (datetime.now() - timedelta(days=35)).strftime("%Y-%m-%d")
    s = '{"session_type":"push","exercises":[{"exercise":"bench","sets":[{"weight_kg":40,"reps":8,"rpe":8}],"pain":{"location":null,"severity":0}}]}'
    run_script(["append_session.py", "--date", old], stdin=s)
    run_script(["update_summary.py"])
    state = json.loads((USER_DATA / "CURRENT-STATE.json").read_text(encoding="utf-8"))
    d = state["recovery"]["days_since_last"]
    check("中断35天 days_since_last≈35", d is not None and 34 <= d <= 36, f"got {d}")
    teardown()


def test_long_history():
    """场景7：历史日志很长时，脚本仍能完成更新。"""
    setup()
    base = datetime.now() - timedelta(days=50)
    for i in range(50):
        d = (base + timedelta(days=i)).strftime("%Y-%m-%d")
        s = '{"session_type":"push","exercises":[{"exercise":"bench","sets":[{"weight_kg":%d,"reps":8,"rpe":8}],"pain":{"location":null,"severity":0}}]}' % (40 + i)
        run_script(["append_session.py", "--date", d], stdin=s)
    r = run_script(["update_summary.py"])
    check("50天 update_summary 完成", r.returncode == 0, r.stderr[:200] if r.stderr else "")
    r2 = run_script(["validate_state.py"])
    check("50天 validate 通过", r2.returncode == 0, r2.stderr[:200] if r2.stderr else "")
    teardown()


def main():
    print("运行回归测试...\n")
    test_lbs_to_kg()
    test_same_day_no_overwrite()
    test_35day_baseline()
    test_long_history()
    print(f"\n{'=' * 40}")
    print(f"通过 {PASSED} / 失败 {FAILED}")
    teardown()
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
