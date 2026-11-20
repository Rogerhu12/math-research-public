# 当前 M24 桥与真 4.625 尾背景的统一参考度量

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：已证明，端点区间和精确有理转换已实际执行。** 本条为当前 M24 图选择一次明确的新全局目标度量 $\widehat g$：仅在桥的最后 $1/1000$ 长度内对目标半径作端点 Hermite 修正，使其与 n4 已定义的真 4.625 尾背景在物理弧长坐标下具有精确共同半径二 jet。

R60 的实际图 $F_*$、真均值和位置全部保持不变；从原 $g_*$ 到新 $\widehat g$ 的完整相对 Gram 转换已支付，得到

$$
 \|\widehat g^{-1/2}(F_*^*e-\widehat g)\widehat g^{-1/2}\|_{\rm op}
 <9.301\,10^{-7}
 \quad\text{于整个桥段}.
\tag{1}
$$

这不是在已冻结原 $g_*$ 下的精化，而是冻结最终完整参考之前的一次显式定义选择。它只接合目标度量，**不接合尚未返回的非旋转尾场**。

## 1. 必须区分的实际 cut 数据

本条绑定 [R60](../results/R60-actual-m24-c2-bridge-and-continuous-metric.md) 的同一输入。run SHA-256 为 `c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a`，physical SHA-256 为 `f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d`。

该 run 中传给 `ShortBridge` 的 `physical_tail_cut` 实际为

```
radius            0.3
backgroundSlope   0.08000000000000027
backgroundSecond -1.866666666666673
```

后两项是原 JS cut 查询值，不应当作真背景输入参数的精确公式。当前真背景由 `q060_true_background_oracle.py` 固定：160 个原 binary 校准根和唯一真实积分归一化 $\alpha_*$ 不变，外端精确锚定

$$
 R_c=\frac{5404319552844595}{18014398509481984},\qquad
 w_c=\frac{5764607523034235}{72057594037927936},\qquad
 w_{R,c}=-\frac{7w_c}{R_c}=-\frac{8070450532247929}{4323455642275676}.
\tag{2}
$$

真 oracle 的定位是 `(cell,segment,x)=(0,8,1)`。在这里外混合函数及其一阶导数为零，故 (2) 的 cut jet 与 $\alpha_*$ 无关；程序直接返回这些恒等式，没有选取 $\alpha_*$ 区间中点，也没有重算背景积分。

旧 JS 值减去真值的精确差是

$$
 w_{\rm JS}-w_c=\frac{19}{72057594037927936},
\quad
 (w_R)_{\rm JS}-w_{R,c}
 =-\frac{14941442363739515}{2433889152438200360801677606912}.
\tag{3}
$$

## 2. 统一物理坐标及目标两 jet

真旋转背景使用物理半径 $R$，上侧为 $Z=Z_c-[h(R)-h(R_c)]$，其中 $h_R=w(R)$。其材料度量为

$$
 g_{\rm tail}=E(R)dR^2+R^2d\theta^2,
 \qquad E(R)=1+w(R)^2.
$$

将朝内的弧长坐标规定为

$$
 s-s_e=\int_R^{R_c}\sqrt{E(r)}\,dr.
\tag{4}
$$

这是物理 $R$ 坐标的变换，不把源 `x` 定位坐标当成全局 $C^2$ 坐标。由 (4) 在 cut 直接得到

$$
 R(s_e)=R_c,\quad
 R_s(s_e)=-\frac1{\sqrt{E_c}},\quad
 R_{ss}(s_e)=-\frac{w_cw_{R,c}}{E_c^2},\qquad E_c=1+w_c^2.
\tag{5}
$$

因此目标半径必须精确匹配 (5)，不能只匹配旧 JS 的 `E/Ep` 或浮点斜率。

## 3. 当前真桥端点并不字面吻合

R60 的桥半径是冻结相位的真原函数 $a_*$，其末相位解析延拓到实际 $s_e$。若当前冻结参数为 $p,\varepsilon,L_1,L_2,L_3$，实际桥跨度为

$$
 L_s=\frac{4191465360069805}{4503599627370496},\qquad
 u_e=\frac{L_s-L_1-L_2}{L_3},
$$

则必须使用

$$
 \phi_e=p-\varepsilon u_e^2,\qquad
 \phi'_e=-2\varepsilon u_e/L_3,
\quad a_*'(s_e)=-\sin\phi_e,\quad
 a_*''(s_e)=-\cos\phi_e\,\phi'_e.
\tag{6}
$$

实际 $u_e>1$，不能在这里重新套用末端 `clip`。80 位外向区间在同一被冻结参数上计算 (5) 减去 (6)，得到

$$
 \begin{aligned}
 d_1&=-E_c^{-1/2}-a_*'(s_e)
 \in[-3.8393935033519557,-3.839393503351955]10^{-17},\\
 d_2&=-w_cw_{R,c}/E_c^2-a_*''(s_e)
 \in[-2.307938832091436,-2.3079388320914355]10^{-15}.
 \end{aligned}
\tag{7}
$$

两个区间均严格不含零，故实际参考导数确有微差。

半径不能从原 GL64 设计式推断精确相等。复用已完成的 [桥 GL64／真 primitive 证书](2026-11-20-short-bridge-gl64-primitive-jet-certificate.md)：将其端点拉回到真 R59 参考的零阶差、同 literal 参数真 primitive 差，以及冻结 plateau 正弦常数误差按三角不等式相加，得

$$
 |a_*(s_e)-R_c|\le7.679517527964208\,10^{-12}<10^{-11}.
\tag{8}
$$

这里真 R59 参考的端点半径按其定义恰为 $R_c$。式 (8) 是有意粗取的已付范围，不声称 $a_*(s_e)$ 等于有限 GL 查询；本次没有重复任何全桥积分。

## 4. 一次明确的新目标半径

设 $L=1/1000$、$u=(s_e-s)/L$，并沿用精确端点基

$$
 h_0=1-10u^3+15u^4-6u^5,\quad
 h_1=u-6u^3+8u^4-3u^5,\quad
 h_2=\tfrac12u^2-\tfrac32u^3+\tfrac32u^4-\tfrac12u^5.
$$

令 $d_0=R_c-a_*(s_e)$ 是唯一真积分所定义的实际差，$d_1,d_2$ 按 (7) 的精确实数表达式定义。在 $s_e-L\le s\le s_e$ 设

$$
 \widehat a(s)=a_*(s)+\sum_{j=0}^2(-L)^j h_j(u)d_j,
\tag{9}
$$

段外保持 $\widehat a=a_*$。不是在 (8) 的区间中任取一个 $d_0$。精确有理恒等式给出修正在 $s_e-L$ 的两 jet 全零，在 $s_e$ 的第 $j$ 阶导数恰为 $d_j$。因此新半径在右端精确取 (5) 的两 jet，可与真尾半径作 $C^2$ 接合；左端保持既有前缀—桥接口不变。

Bernstein 上界给出整个末段修正的 $0/1/2$ 阶范围

$$
 |\widehat a-a_*|\le1.0000000015472972\,10^{-11},
$$

$$
 |\widehat a'-a_*'|\le5.000000007736486\,10^{-8},\qquad
 |\widehat a''-a_*''|\le.0002000000004653431.
\tag{10}
$$

后两项由很短补丁及粗零阶差放大而来，不是实际曲率变化。**实际图没有改动**，所以 R60 的外在曲率、支撑、尺寸都仍为原值。新目标是整个桥上的

$$
 \widehat g=ds^2+\widehat a(s)^2d\theta^2,
\tag{11}
$$

前缀区域保持此前的目标，尾区域取 (4) 拉回的真背景目标。最终正式精化须冻结 (9) 中所有定义，不能每个网格重选 $d_j$ 或背景归一化。

## 5. 原 R60 图的真正 Gram 转换

设 $E_*$ 是原目标 $g_*$ 下的完整相对误差矩阵，R60 已证明 $\|E_*\|_{\rm op}<9.3\,10^{-7}$。在固定材料坐标中，置 $C=\operatorname{diag}(1,a_*/\widehat a)$，则同一实际图满足精确恒等式

$$
 \widehat E=C E_* C+(C^2-I).
\tag{12}
$$

令 $b$ 为 (10) 的零阶上界。既有真桥半径下界为 $a_*>.299$，故 $\widehat a>.299-b>0$。取 $\eta=b/(.299-b)$，有

$$
 \|\widehat E\|_{\rm op}
 \le(1+\eta)^2(9.3\,10^{-7})+2\eta+\eta^2
 \le9.300668896944213\,10^{-7}<9.301\,10^{-7}.
\tag{13}
$$

式 (13) 是精确有理数运算和外向展示端点，不是仅宣称两参考“足够接近”。段外 $C=I$。由于 $F_*$ 和 $M_*$ 都未改，位置和外在几何原样继承；本条未把新 $\widehat a$ 代回 Frenet 求解器而暗中生成另一个图。

参考度量接好不等于 Cartesian 图接好。现有非旋转尾状态、其物理 $R$ 共享两 jet 和真实 mean 高度仍须逐项匹配实际桥端；不能从 (5)、(9) 推出这项尚未完成的接缝。

## 6. 实际执行和复现

源 `scripts/resume_m3/certify_m24_bridge_tail_reference_seam.py` 已实际 `exit 0`，最终本地调用耗时约 .113 秒。真尾 oracle 的积分计数为 **0**。关键散列：

| 文件 | SHA-256 |
|---|---|
| 本条源码 | `4da750d6b18071f23edcdc484cec9e67140c0b8c11697e57fbfb1853ef0572f8` |
| 完整执行输出（scratch） | `532536975977e00290efa3af6fe4d19fe0e24e5a23db3fb69616c4e6de8e74e2` |
| 真背景 oracle | `d133b3ed5b9e5b5a8e15e3a6bb49b3969b65abbd77fbb17a9d0af835d28c1901` |
| 复用桥真 primitive 证书 | `d9f7adabdf1621f97c637795c0b342bf18c9c05b07579325929c705637aef1dd` |

在本课题目录运行，`$WORK` 指运行数据父目录：

```bash
python scripts/resume_m3/certify_m24_bridge_tail_reference_seam.py \
  --source-run "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --bridge-jet-certificate "$WORK/n4-work/short-bridge-m24-gl64-extended-gap.json" \
  --tail-constants "$WORK/n4-work/q060-tail-geometry/constants.json" \
  --tail-normalization-certificate "$WORK/n4-work/q060-tail-geometry/tight-integrals-certificate.json" \
  --tail-oracle scripts/resume_n4/q060_true_background_oracle.py \
  --length 1/1000 \
  --out "$WORK/geometry-work/m24-bridge-tail-reference-seam-certificate.json"
```

完整数组／输出不入库；精简执行记录只保存源、参数、散列及上述标量结论。

[精简实际执行记录](2026-11-20-m24-bridge-tail-reference-execution.json)保留输入与输出哈希及新增目标的全部标量预算。
