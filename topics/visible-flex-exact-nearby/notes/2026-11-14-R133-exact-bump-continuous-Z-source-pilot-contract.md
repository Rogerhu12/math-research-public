# 精确 compact bump 系数与连续 $Z$ 完整残差的小范围消费者

本文件定义新的有向包络方法，不提前登记任何数值通过。原候选、完整
193 态响应三次片、已完成均值方程、全部标量 target jets、原残差证书
和原连续 Green 证书均保持字节身份。新的公开 Actions 只重新评价一个
更紧的、数学上同一的已知源多项式；没有新的 target 调用。

## 1. 原始输入与本次范围

完整原候选的 index SHA256 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`；
完整 physical 响应 index 为
`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`。
原 40 个 residual parts 合起来准确覆盖 7721 个共同闭径向格，均与完成的
body/mean native
`a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870`
及修补源 native
`05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4`
的逐 part SHA 匹配。它们仍保留完整均值和全部角输出。

公开 run `43607383671` 已完成的 fixed-$\eta_0$ 诊断 native 为

`a73382575ca2b14afb810c2ed43ae0aec9d59aef563635a19f6785b414111993`。

该 native 中 80 次真实 target 调用给出 8 个原格各自的 1 格与 4 子格
midpoint/whole third jets。新 worker 按原 run 下载完整 artifact，
核对 native、producer、worker、manifest、成功 child 和全部门；
新 producer 只读取其中已经保存的 jets。原真实 artifact process 的
实际 SHA 另行记录，不能把稍后多一个 publication checkpoint 的 repo
process 字节冒充同一 artifact process。

本次仍取已公开选择的 14 个原格

$$
0,\ 597,\ 1280,\ 1283,\ 1284,\ 1289,\ 1519,\ 1521,\ 1522,\
1524,\ 1753,\ 3070,\ 5584,\ 6375 .
\tag{B.1}
$$

选择只复用原诊断的浮点排名与代表半径，不能据此推出全域最大值。
本次新包络共为 14 个原全参数格及已经存在的 40 个 fixed 参数子格。
除最后一步将同一原格子格的平方径向积分相加外，不改变原分片。

所有结果位于仿射参数偏移 $0$，即固定物理 $\eta_0$ 与原物理 $\nu$。
原 whole-$\eta$ jets 是包含该点的严格域；新 fixed jets 原样复用。
没有把 whole-$\eta$ 的范围重新命名为单点计算，也没有重新评价旧
均值 ODE、target、原 trial 或原 cap 矩阵。

## 2. 同一个 bump 的精确系数包络

令原 compact 支集为 $[r_L,r_R]=[1/20,9/50]$，
$W=r_R-r_L$。在真实原片内用
$x=(r-r_c)/h$，$r_c=(l+r)/2$、$h=(r-l)/2$，则

$$
t=t_0+t_1x,\qquad
t_0=\frac{r_c-r_L}{W},\qquad t_1=\frac hW ,
$$

$$
p=t(1-t)
=t_0(1-t_0)+t_1(1-2t_0)x-t_1^2x^2 .
\tag{B.2}
$$

在 `Fraction` 上先准确卷积展开

$$
w=4096p^6,\qquad
w_r=\frac{24576}{W}p^5(1-2t_0-2t_1x).
\tag{B.3}
$$

每个新格逐系数核对 $h^{-1}\partial_x w=w_r$。这是原同一个 bump 的
恒等重写。旧代码先把 $t$ 与 $1-t$ 分别取三角范数，再相乘和乘方，
会把系数抵消丢掉；本版本先在有理数域完成抵消，随后用原
`RadialFourier.scalar` 接收每个有向 Arb 系数球。所有 Arb 和
binary64 coefficient radius 均计入其 uniform remainder。没有只保存
midpoint，也没有把误差写成零。

格完全在支集外时源准确为零；格在支集内时用 (B.2)–(B.3)；
任何跨越原支集接口的格必须拒绝。不得把这条多项式延拓到原
piecewise 定义的支集外。

设 $Q=(u,v)$，$m=\langle v\rangle$，原有向 primitive 为 $\mathcal I$，
则保持原完整参数源

$$
K_\nu=-Kw+Tw_r ,
$$

$$
F_\nu^1=-\beta K_\nu
  \bigl(\mathcal I(v^2)u_\phi+v^2u\bigr)
  +\gamma m(Kw/2+K_\nu)v_\phi ,
$$

$$
F_\nu^2=-\beta K_\nu
  \bigl(\mathcal I(v^2)v_\phi+v^3\bigr)
  -(\gamma mw/2)u_\phi .
\tag{B.4}
$$

径向 bump 是角标量，故原角支撑没有变化。对原 $M32$ 背景和
193 态 trial，完整 $D h$ 支撑至 $j=160$，完整 $F_\nu$ 至 $96$，
完整 $A e_2$ 至 $64$。这些门同时检查 polynomial 和 uniform
remainder 的实际角支撑，而非只检查所存 midpoint 数组。

## 3. $q_*$ 的诊断与完整连续 $Z$ 是两个不同对象

原精确均值 ODE 构成 $q_*=q_{\rm raw}+e_z e_2$。它的非均值
残差仍采用已通过的 Fourier 相关组合

$$
R_{\ne0}-e_0 C_{\ne0},
\qquad
E_R+|e_0|E_C+\epsilon(N_C+E_C),
\quad
\epsilon=\sup|e_z-e_0| ,
\tag{B.5}
$$

其中 $e_0$ 为固定的准确 binary64 dyadic，$C=Ae_2$。
独立的三角范数与 (B.5) 范数可取较小者，但该较小标量不得代替
所存方向 polynomial 自己的 uniform remainder。$e_z'$ 只属于
独立 even mean 行，由原真实 mean ODE 处理；新 source 不把其导数
加进非均值行。

相位线实际使用的方向则是原 full193 trial 的连续修补 $Z$，其完整
native 为

`87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88`，

定义为

`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。

它满足每个原三次片内 $Z-q_{\rm raw}$ 对径向准确为常量，
并在全部 6143 接口连续，保留全部 193 态和 even mean。
原 native 的
`direction_repair_full_interval_joint_derivative_norms["1/64"][j]`
对 $j=0,1$ 给完整区间 $[0,25/8]$ 的角 $j$ 阶 pair Wiener
修补费 $E_0,E_1$；此处降为 $A_0$ 界。该字段不能被误称为径向
联合导数，也不依赖只覆盖负区的原完整 $Z$ 本身范数字段。

新 $Z$ 残差从

$$
R_{\rm raw}=D_{Q_{\rm raw}}q_{\rm raw}-F_{\nu,Q_{\rm raw}}
\tag{B.6}
$$

的完整两行开始，第二行不删除 mean。新 native 同时保存
$P_{\le96}R_{\rm raw}$ 的全部 193 个径向 Fourier amplitude，
它自己的两 component uniform errors，及下述独立全 pair 费用。

## 4. 原 full operator 对方向修补的严格费用

写 $D_Q=\partial_r-A_Q$，$K_*=\max(1,|K|)$，令 $Q_0,Q_1$
为已完成 repair native 中原背景的全 pair $A_0$ 与一阶角导数上界。
在四倍角频下 $\|\mathcal I\|\le1/4$，$\|J_K\|\le K_*$，
$|m|\le Q_0$，因此全 operator 满足

$$
\|A_Q h\|_{A_0}
\le a_1\|h_\phi\|_{A_0}+a_0\|h\|_{A_0},
$$

$$
a_1=|\gamma|K_*Q_0+\frac{|\beta|K_*Q_0^2}{4},
$$

$$
a_0=|\beta|(1+3K_*Q_0^2)
 +\frac{|\beta|K_*Q_0Q_1}{2}+|\gamma|K_*Q_1 .
\tag{B.7}
$$

这里完整 principal、反应、nonlocal primitive 和独立 mean rank
均已计入。原修补 native 的 background Bernstein 范数完整覆盖原格，
故也覆盖每个已保存子格。由于片内方向 offset 为径向常量，

$$
D_Q Z-D_Qq_{\rm raw}=-A_Q(Z-q_{\rm raw}),
\qquad
\|D_Q Z-D_Qq_{\rm raw}\|_{A_0}
\le a_0E_0+a_1E_1 .
\tag{B.8}
$$

## 5. 真连续背景费用仍单独保留

令 $\bar Q$ 为同一已经定义的精确连续 $M32$ 背景。
已完成修补源 native `05e049...` 的原构造明确以
“raw cubic Bernstein norm $+|e_z|$”定义其
`complete_mean_corrected_response_pair_A0`，故它也上界 raw trial；
这不是从抽象 $\|q_*\|$ 反推 $\|q_{\rm raw}\|$。
该 native 保存完整 first/zero order 差系数 $M_1,M_0$ 和已知费用
$E_{\rm repair}$。从该构造可继续得到

$$
\|(A_{\bar Q}-A_Q)Z
 +(F_{\nu,\bar Q}-F_{\nu,Q})\|_{A_0}
\le E_{\rm repair}+M_0E_0+M_1E_1 .
\tag{B.9}
$$

因此本次付清的每格新增费用为

$$
E_Z=a_0E_0+a_1E_1+E_{\rm repair}+M_0E_0+M_1E_1 .
\tag{B.10}
$$

它是完整两行、包括真实 mean 的已知源费用。全 low、全已知 high
和完整至 $160$ 输出的普通 $L^2$ 界各自由对应 raw residual
范数加 $E_Z$ 得到；径向积分范数另加 $\sqrt{r-l}\,E_Z$。
高块 $97\le j\le160$ 可直接从 $Dq_{\rm raw}$ 取出，因为
$F_\nu$ 在该块连误差一起准确为零。高块的 $E_Z$ 仍完整加入。

本合同没有将已知 source 修补当成对未知 $h$ 的全 operator
转授证明。连续 Green 消费者仍须绑定同一已认证 operator 或已付
operator 域；未付未知 high 输入与 low/high feedback 仍需保留。

## 6. 证据、失败与后续消费范围

原已完成 fixed jets 的原行/子格 SHA、全部旧 40 part SHA、完整
原 cubic shape、全参数 mean enclosure、新 bump exact coefficients、
新 full-$Z$ 与 $q_*$ 两套源范围均保存。新 worker 在数学 child
失败时也打印/保存原 failure、已完成行与 gates，不把失败留成仅
外层 `returned 1`。实际压缩 native 若超过 5 MB，沿已审
`ReviewedRules.snapshot` 原字节分片，完整原件保存在 Actions artifact。

本次 14 格只诊断更紧 source 方法，不能登记为 7721 格全覆盖，
也不能登记为真正 $q_\nu$、完整无限维 inverse、Schur 或非线性解。
后续全 cover 可逐格选择旧有效界或新有效界；若使用现有 continuous
Green ports，可先把已完成 4 子格的最大严格 sup 放回原格，避免
无谓重建完整 projector/Riccati partition。任何零源“待改善部分”
实验只能作为任务选择诊断，不能作为已完成 response 上界。

若最终直接消费连续 $Z$，cut/waist 必须使用同一 $Z$ 的真正完整迹；
不能沿用 $q_*$ 的边界负荷而不付两者的差。$Z$ 的旧 trial jumps
至多作为额外正上界保留，不能宣称为连续 $Z$ 的实际 jump 等式。
同背景相位响应门只要求完整负区普通 pair $L^2$，可用已证固定安全端
$2383968743003/10^{13}$；完整 cap/BVP 与高反馈仍须解出。
