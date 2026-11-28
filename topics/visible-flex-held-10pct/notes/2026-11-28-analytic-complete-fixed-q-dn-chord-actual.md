# R85 的完整 q 列、25 维 DN 联合块与固定 δ 弦线实算

2026-11-28，独立入口
`scripts/resume_20261128/analytic/complete_fixed_q_dn_chord_block.py`
实际返回。工具 session `53092` 真实 exit `0`；完整过程
`93.4151611979978 s`，自观测峰值 `444564 KiB`。
没有新组装 J，没有请求 native，没有求 BVP，也没有产生接受的固定 g 场。
本条是 R85 已证明更新式的实际有限维输入与回代，不重证明 R85。

## 1. 各对象的实际点必须区分

| 对象 | 实际来源与角色 |
| --- | --- |
| 完整 $J_*$ | 保存的 `c9c4906f...` 输入对应的旧点 M24 CSR，SHA `1814497d...` |
| 全部 24 列 $\widehat V$ | 上一条已返回的完整 `64191` 维旧矩阵响应 |
| 新 $v_q$、完整 $F_L$ | 在已接受 raw `4f503380...` 的全 `879` 节点、全 y/p 上本次重新评价 |
| $G$、$g(H_0)$ | 同一接受 raw H 的真实 full-H/J/audit 包 `81f6eb0f...`，全部 height-J 保留 |

旧点与接受点的 x 和 pscale 逐字节相同，y、p 不同。新 q 列和 G
在同一个接受点；J 与 V 仍在旧点。因此全部 25 维结论明确是
**混合点弦线矩阵**结论，不能替换成当前点的完整 DN Jacobian。
没有从已删的旧 wq 或旧 χL 标量重建向量。

## 2. 完整物理 q 列的实际生成合同

采用原 `material_lambda_tangent_predictor.build_model` 的原物理构造。
保持完整 x/y/p、p0 所给的实际 δ、原高阶物理 support 控制、
gauge q=.06、warp_reference_q=.06（实际 warp_e=.48）、
完整 profile/port、字面 radial chart、参数尺度以及原 mean=1168 规则不变。
只令支持核心主振幅

$$
q_{\rm actual}=q_{\rm source}e^\eta
$$

在 η=0 附近变化。它不是 Fourier 状态前的 gauge q，也不是 warp 参数。
使用 η 步长 `1e-5` 与 `5e-6` 的中心差分。

每个扰动都完整清除 core、Flow、exact-lift 与参数 jet 缓存；原
collocation midpoint 链、全部 inlet/terminal 行以及原 RMS 两个非中点
域采样都实际评价。没有创建 global-J 或全 COO 索引。
每次实际核 E、W、D、gauge、全部 H、原 p/y、pscale、完整配置与图不变。
尾的 P 在固定 H、固定背景下没有这个支持主振幅参数，故不遗漏额外
直接 q 导数项；终端 q 列实际逐项恰为零。完整 g 保持的是该有限原问题的
合同，不声称另做了新的 physical-mean 或连续度量审计。

四个扰动原域门均过，全部 q 列的两步长相对差
`6.217328342495664e-10`。恢复主振幅并清缓存后，完整原 F_L
逐字节回到本次基值：

$$
\|F_L\|_\infty=4.3983177284010555\times10^{-11},\qquad
\|F_L\|_2=8.526117482241262\times10^{-11}.
$$

这次是实际再评价完整 F_L，不再仅引用历史最大值。
有限差分稳定性仍是数值观测，不是导数的严格误差包络。

## 3. 25 维联合块和 χ 的实际值

在同一个完整旧矩阵因子上解
$J_*\widehat w_q=v_q$，再构造 R85 的全部联合块

$$
\mathcal S_{25}=
\begin{pmatrix}
I+GC\widehat V&GC\widehat w_q\\
e^T\widehat V&e^T\widehat w_q
\end{pmatrix}.
$$

这里 $e$ 选择原加性 δ 坐标 `64167`，$C$ 是原完整物理 H
选择器，系数为固定 $\sigma q=-.06$。没有删去任何原控制或尾模式。
实际得到

| 量 | 数值观测 |
| --- | ---: |
| $e^T\widehat w_q$ | `2.471194976987832e-5` |
| $\widehat\chi_N=e^T\widehat w_q-e^T\widehat V(I+GC\widehat V)^{-1}GC\widehat w_q$ | `2.471081061471873e-5` |
| 粗步长的 $\widehat\chi_N$ | `2.471082063681317e-5` |
| χ 两步长相对差 | `4.0557530054505983e-7` |
| 完整 wq 两步长相对差 | `3.31058436832683e-7` |
| 原完整 $J_*\widehat w_q-v_q$ 无穷残差 | `3.3306690738754696e-16` |

本条没有把旧已登记、同点 Robin χL 值替代成上表的新旧点弦线量。
χ 数值非零支持继续实际固定 g 求解；其符号尚未成为当前物理 DN 的严格结论。

## 4. 全残差保留的固定 δ 仿射方向

此次还以真正完整的 $F_N=F_L+Ug(H_0)$ 为右端，
先解 $J_*z=-F_N$，再解全部 25 行

$$
\mathcal S_{25}\binom{t}{\eta}
=\binom{GCz}{e^Tz},\qquad
\Delta Z=z-\widehat Vt-\widehat w_q\eta.
$$

这样原固定 δ 的约束 $e^T\Delta Z=0$ 没有被丢掉。
实际 $\|F_N\|_\infty=0.0010942059056917477$，
$\eta=1.4991713675388688e-5$。对原完整旧矩阵、完整 q 列以及
全部 DN 端口更新回代，仿射残差无穷范数为
`1.362028979184915e-18`，二范数为 `1.7007673447494863e-18`；
δ 约束残差数值恰为 `0.0`，小系统残差无穷范数
`1.3552527156068805e-20`。

这是完整仿射弦线方向，仍不是当前点完整 Newton 步。
没有把该方向应用到新固定模型或宣称原非线性域/RMS/metric/physical-H
门已过。当前点内部 J 差、有限差分误差、尾 DP 误差和非线性余项仍未付。

## 5. 字面联合块的严格条件数检查

将本次舍入后 $\mathcal S_{25}$ 及数值逆视为精确 dyadic 数，
原有 Fraction 检查给 $\|I-T\mathcal S_{25}\|_\infty<1$。
完整分子分母见 JSON。仅将末兼容行精确乘 $2^{15}$，所有方程与
未知量都保留；再对该字面缩放矩阵作同一严格计算，得到

$$
\eta_{\rm inv}<6.202\times10^{-16},\qquad
\|\mathcal S_{25,\rm scaled}^{-1}\|_\infty<4.326992,\qquad
\operatorname{cond}_\infty(\mathcal S_{25,\rm scaled})<15.786970.
$$

小数上界取在精确有理上界之外；精确证书全部保存在同名 JSON。
行缩放说明这里的较小未缩放兼容量不能直接解释为几何近核。
这些严格界只认证**保存的字面混合点小矩阵**，没有认证当前物理小块、
完整原 J 或全 DN 的逆。没有以此替代 R85 补充中尚需支付的响应误差预算。

## 6. 可追溯输出和范围

工作目录为
`/workspace/scratch/7c4e33ee17de/held10-analytic-work/lambda002-m24-fixed-q-dn-chord-block-20261128-a`。
原 `joint-block.json` SHA256
`413aa6c2191d7467171bc22a1429d4ed71ab6f2a76e260a86a940282ed897d90`；
精确行缩放 sidecar SHA256
`4481bc1e0710fe4c7cfbd468d9dbed66f505a48817315e1e207b6c08ea595f0b`。
新完整 q/wq、F_L 与仿射方向都留在该目录的
`complete-q-and-chord-vectors.npz`，实际 SHA 见小记录；科学数组不进仓库。
本条不产生新曲面、固定 g 精化、λ=1 接受或本题完成声明。
