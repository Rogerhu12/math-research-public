# 完整高度首次启动失败与修复

- 2026-11-27 15:49 Asia/Taipei，公开 run45960073755/job140375557226 在47秒内失败。
- 日志明确为 Python 无法打开旧 `full_p47_first_global_CM_height.py`：workflow 最后一行错指旧入口，sparse checkout 又误把旧源重复改为完整源。数学脚本未开始，未产生任何新高度或已完成指标。
- 修复完整脚本入口，并在 sparse checkout 恢复实际被导入及哈希核对的旧首高度源。所有数学脚本、参数、预算与原方法保持原值；请求增加 launcher_revision=2 及此次真实失败记录以重新触发。
- 真实终端 pull 于15:49仍报无可用执行环境，shell未运行；按根规则8继续连接器小文本同步与 expected_sha 非force发布。
