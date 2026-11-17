# 向内 .997 / M112：移动框架 Schur 边界真接受及实际 C² 读出

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：新的有限边值问题已真接受；实际共同 quintic 的采样 Gram 仍为
`2.42109e−6 > 1e−6`。没有闭面、全相位 reach 或完成标准声明。**

## 1. 本次只更换终端行

使用已有新向内 scalar 的真 .997 / M112 / N2048 场作为 warm，
`duration=0`，明确传入真 .995 场作为 `boundary_input`。
保留原浅端 229 行、全部 338 条 Frenet ODE、固定前三个 core 控制及同一个
向内 scalar 定义。角材料约定和由实际 core 计算 `rho` 的既有读法保持。

终端 109 行由
[`frenet-schur-diagnostic`](2026-11-17-parallel-geometry-frenet-schur-diagnostic.md)
中 .995 的移动实际法切框架构造：

\[
B=(T A+T_s)T^{-1},\qquad L=Q_{109}^{\mathsf T}T.
\]

`Q₁₀₉` 取 `B.T` 的实 Schur 列，选实部大于
`9.128643980674848` 的完整实块。切口间隙 `2.765403349864874`，
确有 109 维；没有截断共轭对。行目标保持原外推规则

\[
L\{y_{.995}+.002\,y'_{.995}+.5(.002)^2y''_{.995}\}.
\]

因此这是**新的有限终端条件定义**，不是完整非线性 tail DN。
显式 `boundary_input` 也确保 duration 0 时不会误用 warm JSON 保存的旧行。

## 2. 真正求解与共同 quintic

求解参数：`tol=1e−8`、`max_nodes=1800`、原 separated QR backend。
实际保持 510 节点。首次 QR 根矩阵条件估计 `3831.72087084`；
首个线性相对残差 `1.07e−11`，两次 Newton 全步接受。
最终 `success=true`，RMS `9.325584391011836e−9`，
边界残差 `2.7755575615628914e−17`。

再使用原 inward 共同 quintic 读者：每节点共用实际 0/1/2 jets，
509 胞元，每胞 4 等分，N2048，共 5,212,160 采样点。

| 真实 C² 读数 | 原主符号边界 .997 | 新移动 Schur 边界 .997 |
|---|---:|---:|
| 最大相对 Gram 算子范数 | 2.75357866284e−6 | 2.42109048665e−6 |
| Gram 最坏 s | .997 | .997 |
| Gram 最坏角 | 2.70594210983 | 0 |
| 最大主曲率绝对值 | 6.30172063576 | 6.30172604979 |
| 镜像 open-prefix 直径上界代理 | 3.50901958310 | 3.50901962098 |
| 对实际 core 见证的最小采样距离 | .960001035377 | .960001072900 |

新场最小采样 Gram 行列式 `.02756827132078923`，
core gap `.9600010728998606`，最小采样 `rho=.16603695769553584`。
Gram 峰减少约 12.1%，仍显著超过题目误差门；峰仍在真实末端。
solver 自带的 101 个径向样本不能替代这里的全胞元实际共同 quintic 读出。
本表各极值均为采样结果，不是连续区间包围或 reach 证明。

这一对照证实该 Schur 行可用于原完整有限系统的真实求解；它没有证实
端部误差会随角维数收敛，也不把此次部分改善当作封闭尾完成。

## 3. 来源与重现

输入：

| 对象 | SHA256 |
|---|---|
| 原 .997 warm `parallel-inward0997-m112.json.gz` | `11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327` |
| 真 .995 reference `parallel-continue0995-m112.json.gz` | `d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f` |
| 新接受 raw `parallel-inward0997-m112-schur.json.gz` | `dd566c28b0f3a51c1d052bd22d9644c707570afdb0dfcc927849568eb4f082dd` |
| 实际读出 `parallel-inward0997-m112-schur-readout.json` | `cbc9175ed34389876e47aa29e2e3d17043c14e4282127c62679f6d137e6d7620` |

新 driver：
[`2026-11-17-parallel-geometry-schur-bvp.py`](2026-11-17-parallel-geometry-schur-bvp.py)。
SHA256：`c7f477000cc149c2443c91b51956fc6df7b0e8d8114ad6c5d66bd646b1c7e50f`。
实际输出内保存其 SHA、冻结 Schur helper SHA、输入和 reference SHA、全部
终端行以及边界方法。原 solver、inward profile、Schur helper 均未修改。

在课题目录执行，raw 保存在 `$SCRATCH`：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-schur-bvp.py \
  --input "$SCRATCH/parallel-inward0997-m112.json.gz" \
  --boundary-input "$SCRATCH/parallel-continue0995-m112.json.gz" \
  --out "$SCRATCH/parallel-inward0997-m112-schur.json.gz" \
  --duration 0 --tol 1e-8 --max-nodes 1800

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  scripts/parallel_20261117_prefix_inward_readout.py \
  --input "$SCRATCH/parallel-inward0997-m112-schur.json.gz" \
  --out "$SCRATCH/parallel-inward0997-m112-schur-readout.json" \
  --angles 2048 --radial-subdivisions 4
```

读者保存的 base source SHA 为
`045533247125e318d5b5051f0e98b286f287126f51c6e616d938019f8432d29c`。
inward reader SHA 为
`75218531458ed3c5a91c215b8d57282fe9f547bb598adaee59da647855a5d76a`；
inward solver wrapper SHA 为
`86fd79df32938a5437bece1b1f7807e53976de4cfd8edf6e99ef1cca9bd88bfb`；
separated QR backend SHA 为
`c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39`。
Schur helper 与原 finite Jacobian / scalar 依赖身份见上述完整谱诊断。
原始大输出不入库。
