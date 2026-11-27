# R150：W 的 lambda=3/2 整支原值比率、首一 e 二次与同 e 一次返回

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。AI-assisted GPT-6 Astra Pro。

**状态：完整原值接口与精确必要参数曲线已证明。** 本页只处理当前原 Delta0/W0 图的 lambda=3/2 整纤维。原 Delta、第二矩、第三矩在一个全纤维合法的值比率中转为 e 首一二次和同 e 一次式；没有选根，没有丢弃后一个一次式的首项零支。原 Gram、个别 N/P 及其他物理非零条件仍须返回，本页不宣称该纤维为空。

## 1. 原作用域及唯一的值比率

沿用[完整原值十行定理](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-native-full-value-four-generator-system.md)的当前物理域，而非一般碰撞 hU=kU 图。仍令

$$u=e+1,\quad Q=ek,\quad V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV},\quad
d=1-Q,\quad m=u-\ell,$$

$$J=2u(1-u)+\ell Q,\qquad
s=(\ell\zeta-T)/u,\quad v_0=(T+ms)/\ell.$$

原值仍是同一点的

$$h_U=1+v_0-rs,\quad k_U=1+v_0+rs,\quad r^2=d.$$

原物理 s 非零与原值 Sval=2v0+3-2 lambda 非零在该图已经保留。在 lambda=3/2 时，Sval=2v0，故 v0 也非零。于是整支都可合法定义

$$z=s/v_0\ne0,\qquad s=zv_0,\qquad T=v_0(\ell-mz).\tag{1}$$

这里 z 是新的比率，绝不与旧 U 值变量或权参数混同。没有假设中心化 Gram 坐标 T-2 lambda 非零。

记

$$A_z=4uQ-J+Jdz^2,$$

$$P_2(z)=\ell-2mz+\ell dz^2,\qquad
P_3(z)=\ell-3mz+3\ell dz^2-mdz^3.$$

原第二、第三矩的目标在该 lambda 下分别为 5/2、7/2。因此原矩及原 Delta 准确变成

$$v_0^2P_2=5/2,\quad v_0^3P_3=7/2,\quad
v_0^2A_z=3Q.\tag{2}$$

最后一式由完整原 Delta/Phi 得到；Phi、Q 已付。于是 (2) 本身支付 Az 与 P3 的非零，不是根据它们在某个参数函数域一般非零而倒置。

## 2. e 首一二次的全系数

由 (2) 同一个 v0² 消去，得

$$6QP_2-5A_z=0.\tag{3}$$

为写出完整低次式，令

$$L_h=(k+2)^2-2ek,\quad
m_h=(k+2)(ek-2),\quad
J_h=k+2-4e.$$

则

$$\ell=\frac{uL_h}{kV},\quad
m=\frac{um_h}{kV},\quad
J=\frac{uQJ_h}{V}.$$

将 (3) 除以已付 u e/V 后，准确得到

$$
\begin{aligned}
R(e,k,z)={}&(1-ek)\{k^2+(8e+14)k+24\}z^2\\
&-12(k+2)(ek-2)z\\
&-(20e+9)k^2-(32e+6)k+24=0.
\end{aligned}\tag{4}
$$

z 的系数采用 m=u-ell、z=s/v0 的同一符号；不能将它误写成同号的 2-ek。

置

$$a=-8k^2z^2,$$

$$B=(k^2+14k+16)z^2+12(k+2)z+20k+32,$$

$$C=(k+2)\{(k+12)z^2+24z-3(3k-4)\}.$$

(4) 的全部 e 系数准确是

$$R=ae^2-kBe+C.\tag{5}$$

k 与 z 在此整支均非零，故 a 是原点单位；可定义实际首一式 R/a，而不用倒置任何未付权曲线。这个首一二次不要求判别式非零，不要求 e 的两个根不同。

## 3. 保持同一 v0 的三阶矩

定义完整小多项式

$$U=4V-J_h+J_hdz^2,$$

$$P_{3,h}=L_h(1+3dz^2)-m_hz(3+dz^2).$$

有

$$A_z=\frac{uQ}{V}U,\qquad
P_3=\frac{u}{kV}P_{3,h}.$$

由后两个原式 (2)，同一个 v0 被唯一恢复为

$$v_0=\frac{7A_z}{6QP_3}.\tag{6}$$

把 (6) 代回 v0²Az=3Q，得到

$$49A_z^3-108Q^3P_3^2=0.$$

其完整已付因子清除后为

$$H(e,k,z)=49u k^2U^3-108V P_{3,h}^2=0,\tag{7}$$

因为

$$49A_z^3-108Q^3P_3^2
=\frac{u^2Q^3}{k^2V^3}H.$$

反过来，若在当前权域 k z Az P3 非零、R=H=0，按 (6) 恢复同一 v0，再按 (1) 恢复 s、T，则逐式有

$$v_0^2=3Q/A_z,\qquad v_0^2P_2=5/2,\qquad
v_0^3P_3=7/2.$$

所以这正是三个原值条件的同点恢复；未在平方消元后任意选择 v0 的正负。Az=P3=0 的公共零集不被当作合法恢复图，它由原 (2) 与 Q 非零直接排除。

(6) 不表示其余原 Gram 或个别 N/P 已成立。恢复的 T 必须仍与同一 Gram 的原 T 相等；zeta、hU、kU 及其他原物理不等式也继续保留。

## 4. 六步原伪除与完整同 e 一次式

H 对 e 次数为七，R 的 e 次数为二。以下固定的多项式伪除法给出完全明确、可再生的 G0、G1，而无另选因子。

从 rem=H、quot=0、scale=1 开始。每一步令 j=deg_e rem、c=[e^j]rem，执行

$$
\begin{aligned}
rem&\leftarrow a\,rem-ce^{j-2}R,\\
quot&\leftarrow a\,quot+ce^{j-2},\\
scale&\leftarrow a\,scale.
\end{aligned}
$$

实际准确六步后，整式身份为

$$a^6H=Q_{\rm div}R+1728k^{10}z^6\{G_0(k,z)+eG_1(k,z)\}.\tag{8}$$

源码把两边全部多项式乘回，逐个整系数检查相等。仅剥除显示的非零整数及 k,z 的幂；未剥掉其他内容因子。

G0 为 138 项、双次数 (k,z)=(12,12)，G1 为 127 项、双次数 (13,12)。因此在当前整支，

$$R=H=0\quad\Longleftrightarrow\quad
R=0,\quad G_0+eG_1=0.\tag{9}$$

这个等价只用 a 与 1728k^10z^6 的真单位。在 G1 非零图可写 e=-G0/G1；本文没有倒置 G1。其完整零支为 G1=G0=0，并继续连同原 R、物理域和所有原行保留。

## 5. 真正的一元 e 消元组合

定义参数必要式

$$N(k,z)=aG_0^2+kB G_0G_1+CG_1^2.\tag{10}$$

源实际乘回完整身份

$$
G_1^2R-N
=(G_0+eG_1)\{aeG_1-aG_0-kBG_1\}.\tag{11}
$$

所以 (10)=0 是所有原点都满足的必要条件，包含 G0=G1=0 的退化支，不要求 G1 为单位。它有 349 项，双次数 (22,24)。

这里没有从两个多变量多项式的 gcd 为一推出判空，也没有把 N 当作可逆范数。N=0 单独不等价于完整原值条件；后续仍须同点返回 R、G0+eG1 与 (6)，并完成原 Gram、个别 N/P。

## 6. 已执行精确证书

自含源：

notes/2026-11-27-unit211-W-lambda-three-halves-same-value-ratio-e-quadratic-8542.js

源 7682 字节，SHA256：

11e9cdc8af1ae94d3189e56b4b9981ed7e3c5ae76196bf02cfc8e015e100974d

源码实际使用三变量整系数 BigInt 多项式，完整核验 (4) 的符号、(5) 的全部系数、(8) 的整个伪除身份以及 (11) 的全部组合。没有数值样本，没有模素数特化。实际 V8 耗时 233 毫秒；无外部进程，POSIX exit 与 RSS 不适用。

原 R 的系数摘要为 855718d100f29e7c3ef590dbc91f5c1e9858cf8a30912ed43694dcab55019264；原 H 为 7965990ed9cd425dd75ed2bdc4ce7c53d2d37fd1f3176bbfbf26e55f8b583e0e。

全部整式身份的规范再生数据 26987 字节，SHA256 cc1c1cfa071d08f02dc0e683da55a6de60b0bc212c57f97b7b420486e1ee9179。只保自含源、次数与摘要小回执，不保存可重算矩阵或大系数缓存。

本页给出 lambda=3/2 整纤维的新原值接口，不声称该纤维、W、R150 或普通 ISP 已完成。
