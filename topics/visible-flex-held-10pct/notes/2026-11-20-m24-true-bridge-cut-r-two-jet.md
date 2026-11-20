# 当前真 M24 桥切口的共同 Fourier 两阶数据合同

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。2026-11-20 UTC。

## 结论与对象

**已证明并已实际执行区间求值：** 对 [R60](../results/R60-actual-m24-c2-bridge-and-continuous-metric.md) 的当前 $\lambda=.002$、M24、共享 Hermite、真 primitive、mean1168 图，已导出切口在统一目标坐标

$$R=\widehat a(s)$$

下的完整 Cartesian Fourier 值、一阶与二阶导数。$\widehat a$ 是[已明确统一的目标半径](2026-11-20-m24-bridge-true-tail-reference-metric.md)，**并不是实际图的原半径 $a_*$**。实际 $a_*$ 的端值和导数微差保留在完整迹中，没有置零。

数据只绑定当前 linear 前缀图。它为未来 full H 尾提供一份可共同引用的精确数学结点定义与严格区间，不表示已经把 warm `.25 H`、`.5 H` 或其他未返回的 actual 前缀接上。

同一 1168 点均值及径向导数已严格包围为

$$
M_c\in[.07980484249261179,.07980484249296435],
$$

$$
(M_s)_c\in[1.8402691922751635,1.8402691922996577].
$$

全部均值节点的 Frenet 正根平方大于 $.00611737$。零模位置仍是原真实 primitive 符号 $Z_c$；[已付高度区间](2026-11-20-m24-cut-height-and-tail-mean-contract.md)只是它的包围，不从区间中任意选一个高度。

## 1. 精确消失的角图与核心 lift

输入 run / physical SHA 分别为

`c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a`，

`f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d`。

所有输入保持 R60 的同一公共二阶图。物理 $s$ 末端为原 binary64 `1.4252697037606197`，精确保留；$q$ 是原 binary64 `.06`。

角图是

$$\theta=\psi-e_*(s)\sin(3\psi)/3.$$

在切口，late cutoff $1-10u^3+15u^4-6u^5$ 于 $u=1$ 的值、一阶和二阶导数精确为零；乘任意同一共享 C² spline 后仍有

$$e_*(s_c)=e_*'(s_c)=e_*''(s_c)=0.$$

因此该点 $\theta=\psi$，且材料/计算坐标变换到二阶就是恒等：$\theta_\psi=1$，其余 $s$ 一阶、全部二阶偏导均为零。这里没有将 raw spline 的非零末值误作完整角图末值。

核心 lift 的右支持窗在 $.9s_b<s_b<s_c$；它在切口的一个开邻域恒为零，故其所有所需混合两阶也精确为零。这是支持窗事实，未重新求核心或拿有限 inlet 的零误差日志替代接缝证明。

## 2. 共同 Hermite 末端的实际数据

共同图在最终结点选择原最后一片的左端极限两阶。对储存的物理 quintic 以 exact binary rationals 解释、在精确 $s_c-x_{\rm last}$ 上有理 Horner 求值，并乘一次实际 $q$，得到 219 个精确有理数：

$$J_j=\partial_s^j(qY_*)(s_c),\qquad j=0,1,2.$$

没有再作一次独立舍入的曲线插值。$J_j$ 本身已经乘 $q$，后续使用不能再乘一次。

将每行写成 $(R_0,R_1,\ldots,R_{24},T_1,\ldots,T_{24},Z_1,\ldots,Z_{24})$。水平 Fourier 频率为

$$m=1,\quad 1\pm3j\ (1\le j\le24),$$

其系数为 $R_0$ 和 $(R_j\pm T_j)/2$，共 49 项。竖向则为 $\sum_{j=1}^{24}Z_j\cos(3j\theta)$，另单独保留均值槽。对应的有理系数也随数据保存。

于是切口在材料 $(s,\theta)$ 下的完整三行是

$$
\begin{aligned}
F_c&=A e_r+G_c+Z_c e_z,\\
(F_s)_c&=A_s e_r+(G_s)_c+M_c e_z,\\
(F_{ss})_c&=A_{ss}e_r+(G_{ss})_c+(M_s)_c e_z,
\end{aligned}
$$

其中 $A=a_*(s_c)$ 是 R60 原真实半径，不是目标 $R_c$。

## 3. 实际半径和目标半径必须分开

原桥的冻结参数 $p,\varepsilon,L_1,L_2,L_3$ 与末端 $u_c$ 保留。实际真 primitive 可明确写成

$$
\begin{aligned}
A={}&1-L_1\int_0^1\sin[p(3u^2-2u^3)]\,du-L_2\sin p\\
&-L_3\int_0^{u_c}\sin[p-\varepsilon u^2]\,du,\qquad
u_c=\frac{s_c-s_b-L_1-L_2}{L_3},
\end{aligned}
$$

$$A_s=-\sin(p-\varepsilon u_c^2),\qquad
A_{ss}=\frac{2\varepsilon u_c}{L_3}\cos(p-\varepsilon u_c^2).$$

末段按 R60 解析延拓到真实 $s_c$，不作 upper clipping。本次复用已付 primitive 误差界，给 $|A-R_c|<7.680\cdot10^{-12}$；没有重复背景积分。

统一目标的 cut 常数为

$$R_c=\operatorname{binary64}(.3),\quad w_c=\operatorname{binary64}(.08),\quad
w_{R,c}=-7w_c/R_c,\quad E_c=1+w_c^2,$$

$$\widehat a(s_c)=R_c,\qquad
\widehat a_s(s_c)=-E_c^{-1/2},\qquad
\widehat a_{ss}(s_c)=-w_cw_{R,c}/E_c^2.$$

已付接缝证书实际上证明 $A_s-\widehat a_s$ 是约 $3.839393503351955\cdot10^{-17}$ 的正数，$A_{ss}-\widehat a_{ss}$ 是约 $2.307938832091436\cdot10^{-15}$ 的正数。本文的完整 $F$ 迹保留这些量；仅为未来图方便把它们归零，会改变共同结点，不能称字面 C² 相接。

## 4. mean1168 的真实两阶来源

固定原来的 1168 个字面 binary64 $\psi_j$，权重精确为 $1/1168$。节点数组 SHA 为

`f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf`。

节点从已付同批缓存原样读取，没有改成符号等间距角或另一 finite rule。只使用其节点，不重新计算 R53 核心。

在切口，以实际 $A,A_s,A_{ss},J_0,J_1$ 构造完整截面 Frenet 速度，沿 $s$ 用一阶区间自动微分求导。$e=e'=e''=0$ 使原角图对流项及其 $s$ 导数同时消失，因此这里的简化公式与完整 mean1168 功能恰好相等。

例如令 $U=F_\theta/A,V=F_{\theta\theta}/A$，则

$$T=U/|U|,\quad N=\frac{V-(T\cdot V)T}{|V-(T\cdot V)T|},\quad
B=T\times N,$$

$$\kappa A=|U\times V|/|U|^3,\qquad
\alpha=-A_s/(\kappa A),\qquad
M_c=\frac1{1168}\sum_j(\alpha N+\sqrt{1-\alpha^2}B)_z(\psi_j).$$

这里始终用**实际 $a_*$ 与其斜率**来计算 R60 已定义的 $M$；不能因为目标已经统一为 $\widehat a$ 就重新用 $\widehat a$ 计算另一均值图。

三角函数在这些固定节点用高精度区间再朝外转 binary64；其余向量、平方根、有限求和使用冻结 R23 outward 核。真 $A$ 的既有范围、精确有理 $J_0,J_1$ 及真相位导数范围均作为输入。所有节点正根通过严格下界，得到开头的 $M_c,(M_s)_c$ 两个区间。

这只是所声明有限规则的精确数学函数，并未声称等于连续角平均或 tail 原 512/旧 seam 1536 的均值。

## 5. 按统一目标坐标转换完整迹

切口 $\widehat a_s\ne0$，因此在该点有合法局部坐标 $R=\widehat a(s)$。固定材料角时

$$
F_R=\frac{F_s}{\widehat a_s}=-\sqrt{E_c}\,F_s,
$$

$$
F_{RR}=\frac{F_{ss}-F_R\widehat a_{ss}}{\widehat a_s^2}
=E_c F_{ss}-\frac{w_cw_{R,c}}{\sqrt{E_c}}F_s.
$$

该转换逐 Fourier 系数应用，保留 $A,A_s,A_{ss},M_c,(M_s)_c$。全角混合两阶可直接由频率乘法得到：$\partial_\theta e^{im\theta}=im e^{im\theta}$，cosine 则转为 sine，因此这里确实包含完整二维两阶数据，而非仅一个径向曲线。

一些便于后续比较的严格数据是：

| 当前实际迹的量 | 严格范围或上界 |
|---|---:|
| $F_{R,z}$ 零模 | $[-.0800598106904641,-.08005981069011027]$ |
| $F_{RR,z}$ 零模 | $[1.8639264842595287,1.8639264842842347]$ |
| 水平扰动相对真背景的 $R$ 阶 $0/1/2$ Fourier $\ell^1$ | $(4.749319879\cdot10^{-6},.000306985471,.010637547355)$ |
| 高度非零模的 $R$ 阶 $0/1/2$ Fourier $\ell^1$ | $(.000167074467,.003699305603,.045419232983)$ |

真上侧背景在切口的两条竖向导数是 $-w_c$、$-w_{R,c}$，与本表的完整迹并非相等。因此后续接缝必须保留 mean 及其导数的真实债，不能只匹配非零 $H$ 模式。

## 6. 供后继直接共用的接口

新源 [export_m24_true_bridge_cut_r_jets.py](../scripts/resume_m3/export_m24_true_bridge_cut_r_jets.py) 为有 main guard 的独立模块。纯函数 `exact_endpoint_jets` 返回 $qY$ 的精确有理末端三行，`exact_fourier_field_jets` 给其 Cartesian Fourier 形式，`assemble_R_trace` 按上述正确目标链式公式组装完整迹。

本次 scratch NPZ 的字段为：

| 字段 | 形状/定义 |
|---|---|
| `planar_modes` | 49 个有符号频率，水平复 Fourier 的实系数 |
| `height_modes` | $[0,3,\ldots,72]$，竖向 cosine 系数 |
| `planar_R_jets` | $(3,2,49)$：$R$ 阶 $0/1/2$、lower/upper、频率 |
| `height_R_jets` | $(3,2,25)$，同上；位置零模仍是 $Z_c$ 的包围 |
| `actual_a_jets`, `target_a_jets` | 分开保存各自 $s$ 阶 $0/1/2$，不能互换 |
| `mean_0_1` | $M_c,(M_s)_c$ 的区间 |
| `qY_s_jets` | $(3,2,73)$，已经乘 $q$ |
| `exact_endpoint_data_json` | 219 个 $qY$ 精确有理数及其 Fourier 变换 |
| `bindings_json` | 当前物理图、mean、目标和符号合同 |

未来两侧要引用**同一组可计算实数表达式**。区间中点或各自独立舍入的参数不自动共享同一个两阶结点。尤其 $Z_c$ 在桥/背景放置式中是同一符号；例如定义 $z_b=Z_c+\mu_c$ 后，计算位置扰动零模应先代数消去 $Z_c$，不能把两个独立宽区间相减。

## 7. 实际执行与复现

本次实际 exit 0，约 6.224 秒。NPZ SHA-256：

`9f91cad1aea020ddbd852e7c6133434612c324d0fbf6597f6f7c668b5b98ce8a`。

完整证书 JSON SHA-256：

`5e737935ac071e759e1d6cf0b2589026ca8564f1b82f283cd769ea5bd676dc6d`。

源与全部输入绑定见
[2026-11-20-m24-true-cut-trace-execution.json](2026-11-20-m24-true-cut-trace-execution.json)。完整调用为：

~~~bash
python "$TOPIC/scripts/resume_m3/export_m24_true_bridge_cut_r_jets.py" \
  --source-run "$M3WORK/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$M3WORK/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --reference-seam "$WORK/m24-bridge-tail-reference-seam-certificate.json" \
  --bridge-jet-certificate "$N4WORK/short-bridge-m24-gl64-extended-gap.json" \
  --height-contract "$WORK/m24-cut-height-contract-certificate.json" \
  --mean-cache "$WORK/newg-m24-r53-core1168-intervals.npz" \
  --mean-kernel "$TOPIC/scripts/resume_m3/certify_r59_fixed_mean_ranges.py" \
  --interval-kernel "$TOPIC/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py" \
  --out-npz "$WORK/m24-true-bridge-cut-r-jets.npz" \
  --out "$WORK/m24-true-bridge-cut-r-jets-certificate.json"
~~~

没有新 BVP、tail shooting、核心评价或背景重积分；没有修改原 physical、R60 图、目标度量或正在进行的 true DN 求解。可再生 NPZ 与完整证书只留 scratch。新的 actual full H 前缀若改变物理文件，必须对那个新输入重绑定，不能沿用这里的旧 SHA。
