# R860：原半线性函数域表达的首次真实源完整证书

日期：2026-11-16。状态：**本篇精确表达范围已证明并实际完成**；没有展开二元余子式，也没有完成后继 RR 或高度。

## 实际运行与范围

[公开 run43811325290](https://github.com/Rogerhu12/math-research-public/actions/runs/43811325290) 的数学 job133113508833 和规则 job133113412841 均成功，源提交 cb6f93b61fb58ec077ed38502479df33edd27404。core 为 4b70a64d3158ff7d0c5272562fab16722bc38af1fde466e93f7b6086d43724d5，wrapper 为 d9b7a23c8d09a633d8ec5ed720b247383b19c531af3bb833bb147129bbe43ca4，方法为 20fa1948b7d13990cca9c157ed5f349058f75422e4d13dda9e3f445223f6395a。

实际取得 37 个完成 stage：34 个原乘法矩阵系数组的来源检查，以及原源身份、完整系数索引和新表达 DAG。certificate 的构造计时为 2.0287725849999987 秒，core receipt 的总计时为 2.0298180470000062 秒；二者记录范围不同。原 R806 的矩阵乘法与 cyclic witness、原 R853 的三个共轭没有重算。

## 精确数学输出

保持原 272 阶正规整基、原 w=e₂/τ 和 z=σ/τ。令 A(z,T)=TI−W(z)，输出的 DAG 直接绑定原 W 每一个系数，而非只保存其名称或旧证书摘要。

它构造 D=adj(A)₀₀ 和 N=adj(A)₀,₇₂ 的行列式节点，后一项删原第72行与第0列，符号为正。D 的 T 次数 271、首项系数1、总次数界271；N 的 T 次数界270、总次数界272。依据[原证明](../notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md)7a200b7d和原不可约最小次数272，D(z,w)在函数域非零，且 β₇₂=N(z,w)/D(z,w)。

因此实际源完整表达包括 c_Y(z)=z−2β₇₂、c_Y(w)=w、c_Y(s)=−s 和 c_Y(β₇₂)=−β₇₂。任意给定真实 normal 向量 v 的后继表达使用同一分母，分子为有边框矩阵 [[TI−W,v],[e₀ᵗ,0]] 的行列式负值；此次没有虚构任何新的实例。

原 D₀=(q_Y/82)d/dq_Y、q_Y→−q_Y、偶权 automorphy 因子1和 c_Yτ=τ 同时保留。于是 δ 与 c_Y 交换，ν=82τ dq_Y/q_Y=dz/g 被固定，原 FM.27 的比较因子准确为1，c_Yg=g−2δβ₇₂。这里不需要假定 Γ 已计算。

D(z,w)非零是函数域断言，不是每个点上为单位。原完整正规环保留，不能将 K[z,w] 当作已正规化，也不能省略可去零点的处理。

## 实际来源与保存

首 runner 从 R815 最新保留输入中取 R806 的45个原件，从 R856 同一载体取 R805的7个原件，再取R853的9个原件。两个旧载体的53及569个成员全部逐件 bytes/SHA 核验后，只将必要的61原件放入新载体。R815 的124退出仅允许用作不变原输入运输，未被当作算子完成。

| 输出或载体 | 字节 | SHA256 |
|---|---:|---|
| 最终 certificate | 11274 | 4314f242bbcaaaad16523d5fcac185b57b7964da161579615731880d52f36843 |
| 完整原W系数索引 | 11539 | c522daaa220b8b554b733a224a187f3faab5c4641ee71e25867710bed23367c1 |
| 原半线性余子式表达DAG | 4670 | 8b9dcca65e39621c1de36da435c537b3902ad6aa355356cb5ba9a3e7a807407b |
| 37阶段manifest | 3887 | 83c0c84ae49906f837a094b131e3815ac7e4605847d7ebe954a925a6343c8c2d |
| 61原件source inventory | 14614 | 322aabc8c12a693cdfb1255d888c1361d2fe6b9688fe2e8162343ce1070ec749 |
| 61原件载体 | 109142444 | 5414b58fc224acf843160e948a5ebc28bc9689b4c037898350571a2e34cef72e |
| 全部58产物manifest | 9902 | a629f9f76a8ca1792314726b8aa3cffd45c2ec7b06c17c0f37e1dc1ba48cfe0a |

数学 configuration SHA256 为 d082df1a74457f952f74f748a68bd7308fbd6a0fabe98cf89002e352558a0117。原 producer 与完整配置在61件闭包内保持不变；新运输没有重标来源。

一日 artifact14200417324 为 110986106 bytes，SHA256 aca10fbe6f1296288fba262ca49bef2f4171f022ea4af88dfd1b486fd46cc9d4，到期 2026-11-17 05:37:44 UTC。主线程以11次HTTP Range实际传输1853801 bytes，取得manifest和57个小件并逐件SHA核对；大载体与整个ZIP此处没有再次下载重哈希。Actions 已完整核过必要原输入；后继读取载体时仍必须按原身份完整核验。

新二元余子式展开、幂基坐标、完整 normal 半线性矩阵、canonical/RR核、connection、period及height的完成旗标均为false。实际源完整表达的完成不能替代这些后继任务。下一新计算为 R864 原20×146 cusp限制的127维正则微分核。
