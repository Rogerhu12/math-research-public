# 新 beta0 尾部：正性最小点与归一残差峰并不重合

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
本笔只读诊断此前已登记失败的 beta0=3.625、旧 q=.025 H 向量下的
末次 Newton 状态。它仍为失败状态，未重新求解、未改接受门槛。

## 两个不同的位置

原有限 state RK 的逐 stage 复算重现全局残差
`1.718001964099018e-8`，576 个 stage 均能完成原局部 root。

- 最小 A 为 .055370968986246404，在 stage40、raw cell0、segment3
  的 [.875,1] 子区间内，局部 x=.96875、r=.2351341362351268、
  w=.00192640557860886。该 stage 的归一残差仅
  8.208790939904194e-11。
- 最大残差在 stage46、同一 cell 的 segment3 [.125,.25] 子区间。
  其 min A=.9991230970809378，远离 A 的原局部门槛；决定残差的是
  normalized momentum component13，即 mode18 分量。

所以这一失败的正性谷与残差峰不同，不能把末次线搜索停滞直接
解释成 A 正性容量已经用尽。

## 浮点粒度的具体量级

保持原 `scaleFor(target)`，查看最大残差所在的**同一个分量**：

| stage | 分量 | 节点值 | 原归一尺度 | 该分量 1 ULP / scale | 残差的 ULP 数 |
|---:|---:|---:|---:|---:|---:|
| 46 | 13 | -953.7607154180643 | .00020513899535722373 | 5.541941819674251e-10 | 31 |
| 44 | 12 | 1516.747986184226 | .00008410275917708902 | 2.7035221872384466e-9 | 6 |
| 45 | 13 | 1117.2310315065765 | .00018929906836907579 | 1.2011346775353502e-9 | 10 |

stage44 一个分量的单 ULP/scale 已超过原 `2e-9` 接受门槛。这是
**该失败状态**的表示精度事实，不证明该有限离散方程不存在其他
可表示解，也不授权放宽门槛。stage44 的最大局部 root 相对残差
约 2.15e-16，而 stage46 达到约 7.76e-14；仅收紧 local root 也
不能先验保证所有 stage 的全局残差都会降低。

前一笔新 g q=.02 accepted 场没有这份失败场的强高谐波幅度。
本项目继续沿实际 accepted 场的小步幅值分支，并保留这份高幅
失败场作诊断；这里不主张已证明全尾多解或分支折叠。

## 可复现入口

`scripts/resume_m3/locate_trial_tail_stages.mjs` 接收
`SOURCE_TOPIC RECORD_GZ OUT_JSON`。它从原 physical factory 与
subdivision 重建几何，逐 stage 建立原 split state engine，以原
cusp-aware RK 节点计算状态流、D/S/A 和 root residual；不形成全局
Jacobian、不运行 Newton。已 accepted 与显式失败的输入在输出
`inputAccepted` / `inputFailure` 中分别保留，不能互换。
`annotate_trial_ulp.py --record RECORD_GZ --diagnostic OUT_JSON --out RECORD_JSON`
核对输入散列后，以 NumPy `spacing` 添加同一残差分量的 binary64 ULP
标量；保留诊断脚本和这一步处理各自的源码散列。

`beta3625_q025_trial_stage_record.json` 保存 source/input SHA-256、
最小 A、最大 residual 与最大 root residual 各 8 个位置的标量。
输入 hash 为
`6ccbb5ac2f8517fd6d7a15af4900641b5e7f43d3a5c5e84f8142c9530c92e2ec`。
场和网格不入仓库。
