# 同 runner 的明确新源码后继入口

日期：2026-11-28 UTC。此项是确定的执行接线准备，不是新增数学结论；尚未 fetch/clone 或执行任何新数值命令。

已审 v3 仅允许首棵冻结树内的脚本。现在已确定后续固定 g 的 actual-DN 与资源适配仍需新源码，因此将 `scripts/resume_20261128/design/ci_frozen_followup_entry.py` 本身纳入首棵树。后续 root 使用新的 request id 调用它；v3 先清理并回收旧 active 的完整自有会话，再启动新请求。

helper 要求明确的新源码 40hex commit、明确已读规则 40hex commit、本题 Python 入口及其 argv。它在同一 WORK 下尚不存在的新独占目录，用固定公开仓库 URL 作 blob:none 部分克隆，核真实 main 和所选源码提交的两份 README 均与已读锚无差异，再建立指定 commit 的 detached 稀疏源码树。完整已检出文件逐项绑定 SHA、大小与清单 SHA；返回后重核同一清单。旧源仓库仅有两次只读 `rev-parse HEAD`，不改旧树、旧字段、旧来源标签，也不删任何文件。

入口 argv 在 `--` 后传递：`@ORIGINAL_REPO@` 明确指原字段来源树；`@SOURCE_REPO@` 明确指新入口树；`@WORK@` 仍是同 runner 上保留全部真实场的目录。外层 helper 的 `--original-repo` 用 v3 已有的 `@REPO@` 参数传入。后继入口自己的旗标必须按其真实 CLI 指定，不能把新的源码根标签写回旧 run 记录。

新子进程继承 v3 的同一自有会话，由已经实核的生命周期清理覆盖；不再建新 session。公开 fetch 无需令牌，所有子进程剔除 token/secret/password 环境，禁用交互凭据。helper 限固定仓库、本题 scripts 的 Python 文件及本题 source/work 路径；没有新增跨项目或任意远程执行权限。

实际 AST/compile/--help 检查通过；结构核验确认旧 repo 只有两次 rev-parse、无 unlink/remove/rmtree、无 start_new_session。没有运行 Git 或 BVP。v3 worker、request 与其数学链完全未改。冻结源及检查元数据见同名 JSON；实际后继必须另行绑定 root 选定的新提交和真实返回。
