# 三阶探索的成功运行源码版本

2026-11-10，geometric_closure。此记录只做代码身份说明，不增加数学结论。

两个 frozen 文件由本会话已记录的源码编辑逐项逆变换恢复；旧运行前没有单独
固定源码哈希，以下哈希为现在实际恢复文件的哈希，不冒称事前回执。运行参数、
自然退出及各摘要身份另外保留。

## 已完成的成功运行

1. `scripts/78718-geometry-cubic-cap-scan-frozen-initial.py` 恢复标量修复后的早期源码，
   BVP tol=max(50*rtol,1e-9)，尚无错误捕获分支。成功的无根 n=3,5,6 扫描
   使用此版，未触发 BVP；同一版本的 n=4 BVP 尝试因节点上限退出，未生成成功摘要。
2. `scripts/78718-geometry-cubic-cap-scan-frozen-default.py` 精确恢复暴露 BVP 容差
   参数之前的源文件。该版已经修复标量 NumPy 赋值错误，默认 IVP rtol=1e-10、
   BVP tol=max(100*rtol,1e-7)，有失败时记录错误的分支。
   它对应 `cubic-n4-b0`、`cubic-n4-bm005`、`cubic-n4-bp005`、`cubic-n4-bm006`、`cubic-n4-bm010`
   的成功探索摘要。
3. 当前 `scripts/78718-geometry-cubic-cap-scan.py` 只在上述算法上增加显式
   `bvp_tol` 函数参数、`--bvp-tol` CLI 参数和回执中的该字段；默认算法不变。
   该版连同 `scripts/78718-geometry-cubic-cap-root.py` 用于 `cubic-joint-zero-r1`、
   `cubic-joint-zero-r2`；同一版用于 `cubic-fixed-r1-finer`、`cubic-fixed-r2-finer`。
   两次根搜索和两次固定参数加密运行全部实际正常退出。

## 失败尝试

更早的初稿因标量数组赋值报错，修复后的一次过严二阶 BVP 容差导致
15,000 节点用尽。这两次没有生成成功回执或可用数学证据，失败已在研究稿中注明。
不把上述失败源码身份混入任何成功摘要。

## 冻结哈希

- `78718-geometry-cubic-cap-scan-frozen-default.py`：SHA256 `1a7e639161997997cf42c84d706d6f0e4f200bcb89a4af697b25adbcca7c704f`，8207 B。
- `78718-geometry-cubic-cap-scan.py`：SHA256 `fcece3952e9e8a217121cdb499656777f11ae0bff17dd87fde9d45e060c1b095`，8345 B。
- `78718-geometry-cubic-cap-root.py`：SHA256 `c3f16f05b0eb20fa94601e02e7acdd5c4fc62506334e41e71541aed205797cf6`，1510 B。
- `78718-geometry-check-cubic-cap.py`：SHA256 `3e87566b952e07249a9db390fa12eed833f20815f60412762babb703ff20fdc6`，1613 B。
- `78718-geometry-cubic-cap-scan-frozen-initial.py`：SHA256 `f69b1dbd903545c0f04f8ce0059061bf011a23e425f4e0f22d19e5a0bd0f4ca2`，7942 B。
