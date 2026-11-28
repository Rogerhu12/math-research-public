# 完整块 QR：真实 M16 与 M24 配点矩阵

会话：Astra-held10-7c4e33ee-20261128。

本条延续[完整矩阵消元说明](2026-11-28-block-qr-actual-collocation-check.md)，不重证其等价性。输入是本会话原 λ=.002/M16 求解保存的真实未接受 Jacobian 快照；该阶段随后 solver/RMS/BC 成功但 metric≈4.2799e−6 未门，仅是完整升模初猜，不作接受场。复制快照时源前/后与副本三次 SHA 相同。

## 实际结果

| 项目 | 实际值 |
|---|---:|
| 径向节点 | 879 |
| 每节点完整状态 | 49 |
| 完整参数列 | 16 |
| 原 J 存储非零数 | 4911918 |
| SuperLU L+U 非零数 | 8478077 |
| QR/LU 方向相对 L2 差 | 6.440463642683381e-14 |
| QR 在原 J 上的残差最大值 | 1.066670079402443e-20 |
| LU 在原 J 上的残差最大值 | 2.6398310368783898e-20 |
| 本次 QR 分解秒数 | 0.5043190609999328 |
| 本次 QR 求解秒数 | 0.20213964600043255 |
| 全比较进程峰值 RSS/KiB | 456684 |

完整未知数为 43087；QR因子存储 73397884 字节。使用两次原完整 J 残差修正。齐次边界行的 componentwise 比值仍可为1，原样保留，不用该表推全局条件数。没有实施 Newton/BVP 步，也未减少状态、边界或参数方向。

## 来源与复现

- 源run（原命令保持） SHA-256：`2b9e2fe6f6d1ca7b6b0143a915dd257cd9f9ecc3c2a71f7f08bb18a5dfe1bed4`。
- 真实冻结快照 SHA-256：`e75f89f7aa39f43bc607b9b7654dbc2712dc134cdbdeae16303e1aea092ae620`。
- 原完整J数组 SHA-256：`a9d655651b6170f1eb8097fe61606dc7a89b40fd181b042ef8e1af305fad4bef`。
- 实际比较输出 SHA-256：`3a44c9d73bfdf408a5bd77f729adeb5383c7e3e0941996d0ea6f679456640fba`。

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/check_block_qr.py \
  --source-run ORIGINAL_M16/run.json --snapshot ACTUAL_M16_JAC.npz \
  --outdir OUTSIDE_GIT/actual-m16-check
```

实际工作目录为 `held10-linear-work/actual-m16-check`。数组不入库，初猜快照来自原 observer；M16 原 RHS/J 构造耗时176.31秒，线性分解只占其中一部分。后续 M24 用独立 `check_block_qr_cached.py` 复用同一完整核对、只读CSR和显式径向分块；旧已运行脚本没有改写。最终高M原BVP仍须实际求解并通过全部原门，不能由这项方向对照晋级。

## 后续真实 M24 完整对照

独立缓存装配核已实际 exit0，仍是879节点、全73状态/24参数、64191未知。输入快照未接受；其原求解后来单独通过全部原门，不把矩阵对照本身当作解。

| 项目 | 实际值 |
|---|---:|
| 原J存储非零数 | 10912470 |
| SuperLU L+U 非零数 | 18716380 |
| QR/LU方向相对差 | 9.501958783623026e-13 |
| QR原J残差最大值 | 2.346385251160285e-21 |
| LU原J残差最大值 | 1.0755033516324407e-20 |
| QR分解秒数 | 1.216067560999818 |
| QR求解秒数 | 0.34169023399999787 |
| 全比较峰RSS/KiB | 931328 |

QR因子存储 162613340 字节，两次完整原J残差修正；componentwise齐次行比值1仍原样保留。只读CSR实际miss1/hit56，block32，未缓存任何物理Flow或参数响应。

- 原source run SHA-256：`1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`。
- 实际冻结快照 SHA-256：`c9c4906fb944a82d59f752d74332157dc564b841d269148de20206d937a4edde`。
- 完整原J SHA-256：`28abf787e7f94ea3424ee1e0d2a9fc5839589698920c5872d3459674d382fe53`。
- 核对输出 SHA-256：`75eff251f618164a3c9c93ae65b61280cc491b6d5b98844708a0de82e5396bad`。
- 实际缓存/分块侧录 SHA-256：`6aca1674b4767129839655161842fb1c27c1f8ed23f2710edf1ed927da1583d7`。

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/check_block_qr_cached.py \
  --rhs-block 32 --source-run ORIGINAL_M24/run.json \
  --snapshot ACTUAL_M24_JAC.npz --outdir OUTSIDE_GIT/actual-m24-check
```

当前允许后继独立 `run_design_qr_dispatch.py` 从 M≥40 使用这份完整因子；它仍通过原完整lift、所有状态/边界、RMS/metric门，数值线性算术变化明确记录。`resume_design_qr_from_bootstrap.py` 只在原.016真正接受后读取真实左右锚并接续，不重算早期λ。正式高M场仍须实际返回，以上不证明M40以上的可解性。
