# 恢复准确前腿参考，并永久保存第 419 段

2026-11-12，reproduce_newton。

## 1. 已完成的恢复和身份检查

冻结的 δ₄ shared1032 入口已重新完成前腿：550 个 accepted steps、10770 次 RHS
调用。35 个原始 NPZ/gzip 分片及其 `trace.json` 共 36 个文件，字节数和 SHA256
均与环境中断前保存的记录完全一致。随后使用原冻结入口重新生成有限参考：

- U/L 的 23 个系数分片全部逐字节复现，550 段的准确时间网格不变；完整前腿
  manifest 也逐字节相同，SHA256 为
  `43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0`。
- 有限修正传播子 (Q_f) 的 12 个分片全部逐字节复现，完整 manifest SHA256 为
  `f1e7556a13aef2a4e5661fc00c1e9c4eda961335fb8685d26bcef550b7b147ce`。

只有在上述完整比对通过后，才将重新生成的分片补回旧规范 manifest 所指目录。
没有换参数、换参考、重标源哈希或把一次近似数值相等当作同一准确对象。
对应小型恢复报告分别是：

| 报告 | SHA256 |
|---|---|
| `2026-11-12-step4-forward-raw-recovery-hash-check.json` | `69beb3bd9f5edd22cd3e93173a6b7ca29ee2a3c639c26de4046d4e6c8afd4278` |
| `2026-11-12-step4-forward-reference-recovery-hash-check.json` | `e42b5c76200a2bd7276d31a361411c9e1f47f1b5e76263297f28e6c549d2fb94` |
| `2026-11-12-step5-Q-forward-recovery-hash-check.json` | `3d79b52499e3c8a7847577cb14969e2e7812f51819190eebbbc60b5957e0dc6b` |

这些是精确数据身份检查，仍不把原浮点积分变成真实流证明。后腿原始重算和完整
前腿 (Y_x) 非零门正在另外进行，不属于本节的完成结论。

## 2. 一段即可独立重放的准确输入

新的永久小包为

`data/phase_ring_continuation/step5_forward419_exact_reference_package.npz.gz`，

SHA256 `bf9e219a46415dc330a089d56be73eccb7329fe0e99b8fcdc1aa43f2fe9b8c04`，
259998 字节。它完整保存：

1. 第 419 段 U/L 的八个 Bernstein 控制，每个控制所有 (k=0,\ldots,516) 模；
2. 同段 (Q_f) 的八个控制，每个控制所有 (k=0,\ldots,128) 模；
3. 前腿终点的完整 (Q_{f,\mathrm{end}}) 有限多项式；
4. 初值修正 (a) 的完整整数和 (2^{122}) 分母定义；
5. 原 descriptor、四个原参考/Q manifest、初值修正及 target object/root/H 的
   原始 JSON 文本，每个文本保留原字节 SHA256；
6. 原完整系数分片的路径、SHA256、字节数、选取段/控制索引，以及每个保存数组的
   dtype、shape 和 C-order 原始字节 SHA256。

所有系数直接从已经核对原 SHA256 的分片复制，不做插值、DFT、重采样或舍入。
写出后再次打开原完整分片，把六个数组与包内解码结果逐字节比较，包括零的符号。
六项均通过。所有原 JSON 文本在加载包时也重新编码并核验其字节数及哈希。

实现 `scripts/fourfold_retarget_reference_segment_package.py` 的 SHA256 为
`3863aae2e5259d17023d6ba3a8cfc3e55bbf8fef431803dca27ccec140e1d0b2`。
提取报告 `notes/2026-11-12-step5-forward419-reference-package-extraction.json`
的 SHA256 为 `f14720477f5837114365d5ff466e2fb0a13eac917227774646cdfc14b50fb37b`。

## 3. 数学定义保持不变

原数值参考来自准确仿射参数

\[
 \delta_4=-7789866024620307/4611686018427387904.
\]

新的参考用于目标

\[
 \delta_5=-7789843107295549/4611686018427387904,
\]

但有限参考本身只是明确选择的函数。它保留准确符号乘积

\[
 Y_{5,f}(u,x)=x/4+U_{4,f}(u,x)+Q_f(u,x)a(x),
\qquad a=h_5/4-U_{4,f,\mathrm{start}}.
\]

包中没有把 (a) 改成 ((h_5-h_4)/4)，也没有对 (Q_fa) 的高模做截断。
所有正频率数组都采用归一化标签 (x) 的 (2\pi) 周期；负频率在各个实时间
多项式系数层取准确共轭。非实 (u) 上不能直接共轭正模的已评价函数值。

第 419 段的准确物理时间端点是

\[
 \tau_a=4466727694628647/9007199254740992,\quad
 \tau_b=282639970307159/562949953421312.
\]

归一化 (u\in[-1,1]) 满足

\[
 \tau=c+hu,\quad
 c=8988967219543191/18014398509481984,\quad
 h=55511830285897/18014398509481984.
\]

前腿场的分支号仍为 (-1)。目标 δ₅ object、root、H 的原哈希完整保留在包中。
原 descriptor 的历史说明仍提及 (q=\exp L)；本次没有改写它。R68 改用同一个
明确参考的 (q=Y_x)，由下节另行证明，不能把所存有限 (Q_f) 认作真实 Jacobian。

## 4. 无大分片依赖的加载检查

`load_package(path)` 只读取小包本身，返回准确数组、原 JSON 和元数据，不打开
原始 JSON/系数分片路径。已在 `/tmp` 工作目录运行其实际加载；在那里全部原
相对 JSON 和分片路径均不存在。所有内部数组和嵌入 JSON 的哈希仍核验通过。

记录为 `notes/2026-11-12-step5-forward419-reference-package-standalone-check.json`，
SHA256 `2f7d84c785dbf8a319f9f447d4786ca729b9589c43316d9739c00bb88964e4e6`。
因此，后续保有仓库源码和这个小包，就可以直接重放第 419 段有限参考，不必先
重建 1032 条数值射线或全部 1100 段参考。这里并没有声称其他时间段也随包保存。

只读检查命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_retarget_reference_segment_package.py \
  --check data/phase_ring_continuation/step5_forward419_exact_reference_package.npz.gz
```

实际原分片仍在时，可向新路径重新提取并独立比较：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_retarget_reference_segment_package.py \
  --descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --segment 419 \
  --out data/phase_ring_continuation/step5_forward419_exact_reference_package_replay.npz.gz \
  --report notes/2026-11-12-step5-forward419-reference-package-extraction-replay.json
```

## 5. 同一真实参考段的连续非零导数门

另用冻结的 `fourfold_reference_derivative_gate.py` 对恢复后**同一个 retarget**
运行了第 419 段全实时间、整个复标签带的门。所有八个 Bernstein 控制、完整
角圆、Taylor 格间余项和完整 (Q_fa) 导数费用均已包含。结果为：

| 归一化标签带宽 S | Re(Y_x) 严格下界 | Y_x 的模严格上界 |
|---|---:|---:|
| (1/512) | (0.0460642650582324) | (0.700692500887590) |
| (1/256) | (0.0460621460166260) | (0.711329329276094) |
| (1/128) | (0.0460536663551109) | (0.734753421076334) |
| (1/64) | (0.0460191272876495) | (0.792503672870634) |

这里每个数都向安全方向缩短。四个带均使用 (N=2048,p=6,160) bits，通过时
无需加密；总 CPU 约 2.776 秒。最宽带中完整 retarget (C^1) 费用最多
(1.052\times10^{-6})，已从下界扣除。

报告为 `notes/2026-11-12-step5-forward419-reference-derivative-gate.json.gz`，
SHA256 `bf0ce1df9cc088031f4b9f989e1c64f95cc32eddd71a81bf6984c10ebab67c37`。
它明确 `full_branch_nonzero_proved=false`：只覆盖第 419 段，不能转授全腿。
时间仍为**实** (u\in[-1,1])。若要证明复时间圆盘上也无零点，仍须另付
(q(u,x)-q(0,x)) 的完整变化或其他非零证书。

重放该局部门：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_reference_derivative_gate.py \
  --retarget-descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --first-segment 419 --max-segments 1 \
  --widths 1/512,1/256,1/128,1/64 --nodes 2048 --max-nodes 8192 \
  --taylor-order 6 --bits 160 \
  --out notes/2026-11-12-step5-forward419-reference-derivative-gate-replay.json.gz
```

目前此旧入口仍通过全参考路径读取数据；小包直接适配器将另行保留其身份并测试。
本包没有宣称完整真实缺陷、参数源、两腿返回、KAM 或闭曲面非线性条件已经完成。
