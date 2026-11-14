# R65 来源守卫的首个实际尝试

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）。日期：2026-11-12。

首入口 `closure_taylor_cut_slope.py` 正式 exit 1，0.462 秒，wait4 峰值 25736 KiB；在任何背景积分或 Taylor 步之前退出。它误把 R29 的 R22 参数 ledger 与 R26 实半径 ledger 要求成相同 SHA。两 ledger 本来是不同证明对象，并且都严格引用同一个 frozen ready。

新 v2 逐项核 R29 所列 R22 ledger 的真实文件 SHA、全部 source checks，以及它与 R26 的共同 ready SHA；原 source 实现 SHA 也照旧严格核对。只改这一来源链守卫，源函数、Taylor/PB、Wronskian、精度和模式都不变。原源码与失败 resource 保留。v2 数值状态尚未据准备推断。

新源码 SHA256：`8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea`。
