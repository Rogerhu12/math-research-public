# Direct CSC publication：检查器 role 标签勘误

日期：2026-11-09。作者：db6f / coupled_prefix。

原清单 notes/2026-11-09-db6f-prefix-direct-csc-foundation-publication.json 保持冻结：

- SHA256：88e06471439caceaf85871d1e9cc2936f37fa2a5f1d5028d8c3d0f141ddcb74f
- commit：df4f14c37015743f7b1b7936d31cbdeb2b84f42b
- Git blob：fa7dce5a614110967b62cd71558fab7deb103d17

其中 scripts/db6f-prefix-check-direct-csc-foundation.py 的 role 被错误标成 historical uninstalled v1。这是自动标签逻辑先使用 endsWith("foundation.py")、同时命中检查器文件名造成的元数据错误。应读为：

> pure Python source/integer checker, first checker schema version, targeting foundation v2; not executed.

这项修正不改变原清单中的文件路径、字节数、SHA256、commit、Git blob、未执行状态或任何源文件。

已重新从检查器的固定 commit cbd77df636c629c3bbd5c1cf6aab6838149f3bb8 读取完整源码，并核全 SHA256 e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd、Git blob aefd12d209e86017afe9550f12f3b6c08c42ce42 不变。源码的实际字段为：

    FOUNDATION_SHA256 = "8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf"

    default=Path(__file__).with_name("db6f-prefix-direct-csc-foundation-v2.py")

报告 schema 中的 db6f-direct-canonical-csc-source-integer-check-v1 指检查器报告格式的首版，不表示目标 foundation 是 v1。实际目标始终是 foundation v2，SHA256 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf。

只有 scripts/db6f-prefix-direct-csc-foundation.py（cc837e05dbce4f8e8fe906b74b6d139dd126efea0fed04187f1395bde0a02e54）是历史、未安装的 foundation v1。拟用函数仍来自另存的 v2。

本次仅完成固定 commit 的全文与三项字段核对。检查器仍未执行；没有调用 Python、foundation factory、NumPy/SciPy、矩阵、BVP 或 DN。这份勘误不将任何未完成的门声明为已通过。
