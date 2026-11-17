# 真 .995 → .997：短有限 IVP 与 Taylor2 终端目标的分离诊断

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：只读数值证据。未更换边界或求解另一 BVP；两次容差吻合不是严格误差包围。**

在 M128 Schur BVP 运行期间，核查当前 .995→.997 目标的二阶外推是否足以
解释端部 Gram 超门。取真 .995 的完整 M112 state，使用已有向内 scalar，
以同一 M112/N2048 完整有限 Frenet RHS 做 DOP853 短积分；原 core 和其
物理角密度 `rho` 在此 IVP 诊断中固定。

两组 `rtol/atol=1e−10/1e−13`、`1e−12/1e−15` 均真正到达 .997，
分别用了 38、50 次 RHS 调用。末系数最大差 `1.93058e−13`，
投到同一 .995 Schur109 行后的差 `2.82577e−16`。

## 1. 目标系数比较

记 `y₂=y₀+Δs y′₀+.5Δs²y″₀`，`Δs=.002`，`yIVP` 为更紧容差的末值。

| 比较量 | 数值 |
|---|---:|
| `max|yIVP−y₂|` | 5.77887567201e−8 |
| `||yIVP−y₂||₂` | 9.87682865706e−8 |
| 同一 .995 Schur109 行的目标差 `max|L(yIVP−y₂)|` | 7.51936697891e−9 |
| 同一 .995 原 principal109 行的目标差 | 1.71140961946e−10 |

行定义及连接项见
[`frenet-schur-diagnostic`](2026-11-17-parallel-geometry-frenet-schur-diagnostic.md)。
这些差量没有被直接注入任何已接受 BVP。

## 2. 字面末端几何

在 8192 个角上读取同一有限系数的实际 `F_φ`；末端 `F_s` 取
N2048 原有限 RHS 的系数，再在该 8192 网格评价。参考 metric 使用原 .995
core 的 `rho` 和真正 inward scalar。没有用未投影法向速度代替实际 `F_s`。

| 对象与径向导数定义 | 最大采样相对 Gram op |
|---|---:|
| 真 .995 state + 同一有限 RHS | 4.24722999828e−7 |
| Taylor2 末 state + 该 state 的有限 RHS | 1.76006408933e−6 |
| 真短 IVP .997 末 state + 其有限 RHS | 2.11127705567e−6 |

IVP 最坏角约 `.434883553366`，该点归一化 Gram 三项为
`rr=1.47226e−7`、`cross=8.49222e−8`、`angular=−2.10808e−6`；
峰主要来自角向误差。较松容差的末端 Gram 为 `2.11140773809e−6`。

若把二阶多项式本身连同导数 `y′₀+Δs y″₀` 当作一条映射，其末端 Gram
为 `1.31054532411e−4`。这只是区分导数定义的控制项；原 BVP 从未采用
该多项式作最终几何，故不能把此数归到已接受 BVP 身上。

本次更准确的短 IVP 末值自身仍超过 `1e−6`，因而没有给出“单换更准确
目标即已达标”的候选。它也没有排除更准确目标经完整 BVP 调整 core 后
可能改善；本次没有进行这项后续 BVP。

## 3. 重现与身份

源：[`2026-11-17-parallel-geometry-terminal-target-probe.py`](2026-11-17-parallel-geometry-terminal-target-probe.py)，
SHA256 `b6fea795cc807add91b7c78418b211982733ceb76f09f89e08f34c8a67b2b93d`。
冻结 Schur helper SHA：
`426635e625e3f80b2b7eea238df1a7f9ac9285fafa5f87a79fd0e2c3d645cd6b`。

输入 .995 SHA：
`d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`；
scalar 载体 .997 SHA：
`11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`。

在课题目录执行：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-terminal-target-probe.py \
  --reference "$SCRATCH/parallel-continue0995-m112.json.gz" \
  --metric "$SCRATCH/parallel-inward0997-m112.json.gz" \
  --end .997 --read-angles 8192 \
  --out "$SCRATCH/parallel-0995-0997-terminal-target-probe.json"
```

本次输出 SHA：
`e9e7709c9a8d2e32b7efa86736f8041a53ba629dcd23bc6350a781ee8cf7f3da`。
raw 保存在 scratch，不入库。
