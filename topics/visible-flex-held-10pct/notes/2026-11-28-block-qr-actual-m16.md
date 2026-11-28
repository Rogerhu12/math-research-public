# 完整块 QR：真实 M16 配点矩阵

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
