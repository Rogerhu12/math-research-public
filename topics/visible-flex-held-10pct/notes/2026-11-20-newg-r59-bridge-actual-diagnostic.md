# 新软启动 q060 的 λ0 与 λ.002：真实完整场的 R59 短桥有限诊断

**状态：两次只读诊断已实际运行，均 exit 0。仅为有限采样；不替代 R59 的连续条件证书。**

这次直接读取同一新软启动、相同 q060 尾参数的实际物理 quintic 场。
第一份是 \(q=.06,\lambda=0,\tau=1,S=.5,b=.2\) 的完整 reference-lift 重接状态；
第二份是其后的真实 \(\lambda=.002,\tau=1\) 原八条 linear DN BVP 返回。
\(\lambda=0\) 的核心仍是旧 support 核；\(\tau=1\) 只是后续圆化的设置，不表示它已成为 \(k=.2\) 的准确圆弧。

第二份 BVP 虽以 622 点、RMS \(9.927135\times10^{-7}\) 接受，
原完整 prefix metric 诊断为 \(3.1932070\times10^{-5}\)，未达到题目门；
两份都不是已支付真实 nonlinear tail 的闭面。本文仅回答短桥的条件几何预算是否与当前实际场相容。

## 1. 冻结诊断对象和坐标

[诊断源](../scripts/resume_m3/audit_r59_bridge_perturbation.py) 复用
[真实模型 adapter](../scripts/resume_m3/actual_m3_metric_model.py) 和
[物理 quintic loader](../scripts/resume_m3/audit_full_relative_metric.py)。
它从各自 run 记录重建同一新多段 profile、角图、core factory、完整 exact lift，
直接使用保存的 \(Y,Y_s,Y_{ss}\)，没有将它们替成 flow 右端，也没有调用 BVP 或尾求解器。

参考为 R59 的真实积分旋转桥。参考常数以 mpmath 60 位数值积分计算；
逐点参考查询采用 64 点 Gauss–Legendre 公式。实际高度保持原均值规则：
角均值固定为 512 点，径向高度按原每个物理 PPoly 区间的正权 GL6 公式计算。
本次没有给这些浮点评价或积分提供向外误差带，不能据此称连续证书已过。

实际桥整段正仿射拉回 R59 参考弧长，真实材料角由完整自适应角图给出。
两条对流项、二阶材料链式项、唯一高度均值及其导数均保留。
扰动 \(V\)、参考单位第一导数范数 \(\eta_1\) 和协变 Hessian 范数
\(\eta_2\) 严格按 R59 式 (15)–(17) 的公式评价。

每份实际扫描使用 700 个桥径向截面，来自 151 个等距截面、实际物理节点和节点中点的并集；
每截面 512 个计算角，均值始终固定 512。没有把角增密解释为连续尾界。

## 2. 实际有限结果

| 同一 R59 量 | λ0 完整 lift | λ.002 完整 lift | R59 连续条件阈值 |
|---|---:|---:|---:|
| 入口唯一高度均值 \(z_0\) | .4672758084 | .4672552880 | [.35,.51] |
| 节点 \(\max |V|\) | .0233759288 | .0234497432 | ≤.13 |
| 节点 \(\max \eta_1\) | .0941424421 | .0944465377 | ≤.12 |
| 节点 \(\max \eta_2\) | .3693273262 | .3706034090 | ≤5.5 |
| 节点实际 \(\max|F|\) | 1.1857295017 | 1.1857382074 | 条件后 <1.34 |
| 节点实际 \(\min F\cdot n\) | .8640180683 | .8639934911 | 条件后 >.087 |
| 节点实际 \(\max|\kappa_i|\) | 4.1642188267 | 4.1647339117 | 条件后 <12.3 |
| 原规则 cut 高度均值 | .8472322383 | .8472092764 | 条件后 (.6001,1.0213) |

两份中 \(|V|\)、\(\eta_1\)、\(\eta_2\) 的当前扫描极值都在桥入口。
\(\eta_1\) 的最大点为材料角 \(0\)，\(|V|\) 的最大点为材料角 \(\pi\)；
\(\eta_2\) 极值角不相同。完整输出保留这些峰的位置，而非只给一个平均误差。

因此，R59 的短桥条件在这两份真实场上均有明确的有限诊断余量。
这没有支付区间之间或角节点之间的上界，也没有把当前 \(\lambda=.002\)
未通过的 metric 门改成通过。它同样不保证以后 \(\lambda\to1\) 时仍落在此窗口中。

## 3. 已执行来源与 hash

源 SHA-256：

    535a10b11b8e4844af37c847cc57cb99316e65ffe05766e97c4f87641fb5bc4d

两次命令使用同一源：

    python geometry-work/audit_r59_bridge_perturbation.py \
      --source-run m3-work/newg-wide-lambda0-tau1-linear/run.json \
      --physical m3-work/newg-wide-lambda0-tau1-linear/physical.npz \
      --support-dir math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3 \
      --out geometry-work/newg-lambda0-r59-bridge-audit.json

    python geometry-work/audit_r59_bridge_perturbation.py \
      --source-run m3-work/newg-wide-lambda0p002-tau1-linear/run.json \
      --physical m3-work/newg-wide-lambda0p002-tau1-linear/physical.npz \
      --support-dir math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3 \
      --out geometry-work/newg-lambda0002-r59-bridge-audit.json

发布后的源位于 scripts/resume_m3，可替换命令首参数；
支持目录默认就是源所在目录。

| 对象 | SHA-256 |
|---|---|
| λ0 run | 37ce9f4f2592cc4e64153b49ec1824b3f5719fabfaa032abedbfda02751dabbe |
| λ0 physical | 6cbf6d6441045aba8dcb99101d7873ba82d54e11cfaa1095300f1a5f17115768 |
| λ0 诊断输出 | cbd4ebfb4377cb0d6c3db592aeb77d7638feb3b457eb970c92f8b835e7e3d78a |
| λ.002 run | be83041236a3832194d52aae6b21569e2e463b67548e4b0b0b1b8cd683f323a1 |
| λ.002 physical | a0d00429c4a6aac10165b07a4d8048dfe08aad4d3afda0dcbad7c4b30ab5bd5f |
| λ.002 诊断输出 | c475151ca48712e96e9353893f2b1d3f3f2693e41d12b40bf5250713e2c08241 |

实际数组和可重算输出未入库。下一份实际场若改变 mean provider、profile、
角图或完整参考，必须用其真实记录重建；不能套用本表。
