# R86 当前复现入口的前向 CLI 修复

原 `actual_closed_full_disk_marker.py` 的最后一行把 `flush=True` 传给了 `json.dumps`。首次实际执行继承该行的独立 R89 完整构造器时，数学构造器已经返回、metadata 已完整保存，但末尾控制台输出真实 exit 1，异常为 `JSONEncoder.__init__() got an unexpected keyword argument flush`。原 R86 历史记录当时写的是未执行，本次不倒写成历史已有一次失败。

按 root 明确授权，当前 R86 入口只把该行改成 `print(json.dumps(...), flush=True)`。旧 SHA `6bdee23d100270d8a46340eee70324090c167fa185e75041dfd75cbb044e6ee3` 可由这一行的逆替换准确重构；新 SHA 为 `220564b2d4b47a693abaa5b9c2dc13062532eb4fd983a00659d58398cc06fefd`。所有数学类 AST 已实际逐项相同，源场参数/定义和证明无修改。

**R86 文档推荐的当前命令现已真实完整返回 exit 0（session 97179）**。其完整 1152 段共享 node index 与原 `e9cb47aef29e77e2c2e5af2a335e942c8933ae2a952b31fed37883ab25e0911b` 逐字节一致；构造器报告 SHA 为 `7ef58cfe6bbc095f0f4f003a59849505cca650855a804377e358aba3b6b93d38`。

R89 已先有独立的正确 CLI v2，真实 session 90707 也 exit 0；其核心数学类不导入 R86 模块，旧首源/首报告/exit 1 继续保存。两次成功只重验完整构造器/来源和共享 node 身份，没有重算 native、BVP、活动矩积分或连续 metric 证书。详见同名小 JSON 的全部真实 source/console/report SHA。
