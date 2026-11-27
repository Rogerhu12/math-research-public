# R150 附录：全 W 原 NS/PS 固定六行的完整权曲线

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 定理与准确范围

在已刊一般 LS、$\Delta=0$、$W=0$ 的原物理余图中，取
$$
u=e+1,\qquad Q=ek,\qquad V=uk+2,\qquad
\ell=\frac{u((k+2)^2-2ek)}{kV}.
$$
沿用该图既有的权单位、同一原 Gram 及完整原值条件，不将任何结论扩大到另行处理的 $D_{\rm phys}=0$ 碰撞图。

**定理。** 下文固定原矩阵定义一个非零多项式
$$
P(e,k)\in\mathbb Q[e,k],\qquad
\deg_eP=97,\quad\deg_kP=123,\quad\deg_{\rm total}P=164, \tag{1}
$$
有 8472 个非零项。当前整个 W 图的每个原点都满足
$$
P(e,k)=0. \tag{2}
$$
本次完整返回适用于所有已允许权点，特别包含前一个规范三次头 $H_{265}=0$ 的整条曲线，没有将它作为新分母。

式 (2) 只是完整必要曲线。没有证明 $P$ 不可约、平方自由或其整个零集无原点，也没有据此宣称权点有限或普通 ISP 完成。系数只由本稿固定原定义与冻结源定位，不保存可重算大系数缓存。

## 2. 原六式、旧六规则与如今已付的三个头因子

记同一原 Gram 导出的六式为
$$
\mathcal E=(E_1,E_{B,e},E_{B,o},N_1,N_S,P_S). \tag{3}
$$
前四式总几何次数至多二，后两式至多三。$E_0,N_0,P_1$ 的原恢复、同一点的加权 N/P 来源、原 $H_A,H_B$ 迹身份，都沿用已刊完整构造。新源重新构造所需前缀，并核其原身份；并未把这些必要式反向称为全部个别 N/P 条件的充分系统。

旧 C9 六规则的原坐标为 $x,y,t$，其中
$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$
$$
\lambda=\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P_{02}},
$$
$$
T=\frac{[\lambda P_{02}-(1-u)T_0]T_0-P_ff-\Phi bcQt}{QP_{02}}-\ell. \tag{4}
$$
这里
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,
$$
$$
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),\quad
M=\ell V_2-u^2=4bc(1-Q).
$$
上述分母均为当前已付权单位。

旧四原二次头按 $x^2,xy,xt,y^2,yt,t^2$ 排列，选列 $[0,1,2,5]$，用真正余子式逆得到首一 $x^2,xy,xt,t^2$ 四条原规则。取固定两个原 overlap 的行 $[0,2]$，再得到首一 $y^3,y^2t$ 两条规则。旧源当时明确保留
$$
(k+2)J_{19}C_9\ne0 \tag{5}
$$
的图。现在以下三个**独立完整原定理**已支付它们：

- [一般等权完整排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，结合
  $$(\ell-u)kV=u(k+2)(2-Q),$$
  允许在当前 W 余图使用 $k+2$。
- [整个 J19 原权曲线排除](R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)，允许使用 $J_{19}$。
- [整个 C9 原权曲线排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)，允许使用 $C_9$。这里没有用 J19 或 D27 偷换 C9 的来源。

除 (5) 外的旧头因子都属于原已付权表。新源直接对**实际**四阶头行列式 $\delta_2$、实际两阶三次头 $\delta_3$ 的分子与分母逐次 gcd 剥除，并把所有除法乘回；三个剩余都为非零常数。它没有把旧源码中的“显式开图”标签当成已经证明的单位。

实际非平凡 gcd 循环记录如下。数字为源码循环次数，不擅自解释为相应整个原多项式的幂：

| 对象 | 实际非平凡支付记录 |
|---|---|
| $\delta_2$ | $e:2,\ k:1,\ u:2,\ Q-1:1,\ V:1,\operatorname{num}(M):2,\ k+2:1,\ J_{19}:1$ |
| $\operatorname{num}(\delta_3)$ | $e:3,\ k:2,\ Q-1:1,\ k+4:1,\ H_{\rm old}:1,\ C_9:1$ |
| $\operatorname{den}(\delta_3)$ | $V:1,\ J_{19}:1$ |

这里 $H_{\rm old}=4ek-k^2-4k-8$，已由其独立完整零支定理支付，**不是**尚未排空的 $H_{265}$。$k+4$ 是当前图中 $\Phi$ 的已付原因子。源码名为 bc 的原子实际是 $\operatorname{num}(M)$，本表按实际输入列出。

因此旧六条规则及其原组合如今在当前整个 W 上有效。全部规则系数、原组合系数、乘法系数的真实分母也逐一按同一已付表返回，未引入新的几何单位或参数单位。

## 3. 真实六值列与完整原乘法

六规则在固定单项式序下严格下降，因而原商可由
$$
v=(1,x,y,t,y^2,yt)^{\mathsf t} \tag{6}
$$
生成。这里只用它们的生成性质；不要求它们自由、线性独立或形成一个不带关系的六维代数。

对 $z=x,y,t$，源码实际给出矩阵 $M_z$ 以及原乘子 $E_{z,i,g}$，逐个核验 18 条完整身份
$$
zv_i=\sum_{j=0}^5(M_z)_{ij}v_j
+\sum_{g=0}^5 E_{z,i,g}\mathcal E_g. \tag{7}
$$
全部矩阵采用**行作用于值列**的方向。式 (7) 的原点含义是 $M_zv=zv$，不能把抽象矩阵的各个交换子元素直接设成零。本次没有执行旧 C9 的交换子或自适应参数 Gaussian 段。

原 $N_S,P_S$ 约化所得两行分别记为 $r_N,r_P$，它们的完整原组合为
$$
r_Av=\sum_g\tau_{A,g}\mathcal E_g,\qquad A=N,P. \tag{8}
$$
式 (8) 并非仅有余式零的断言；六个原乘子及完整多项式等式都已实际乘回。

若 $(r,\tau)$ 满足 (8)，则由 (7)
$$
(rM_z)v=\sum_g\left(z\tau_g-\sum_i r_iE_{z,i,g}\right)\mathcal E_g. \tag{9}
$$
新源对 $z=y,t$ 及 $A=N,P$ 的四条式 (9) 逐一返回。因此固定六原行
$$
r_N,\quad r_P,\quad r_NM_y,\quad r_NM_t,\quad
r_PM_y,\quad r_PM_t \tag{10}
$$
都同时杀死同一个原值列 (6)。它们的来源分别为原 $N_S,P_S,yN_S,tN_S,yP_S,tP_S$ 在同一规则商中的返回。这是新固定原输入，与此前未完成的规范 $\lambda,S$ 六列行列式不同。

## 4. 只用已付单位的多项式化及固定 P 定义

对式 (10) 每行取其六个有理权系数的最小公共多项式分母，再按冻结源码给定的有序已付表剥共有已付因子。设所得多项式行是 $\widehat r_i$，行比例为 $s_i\in A^\times$，则实际返回
$$
\widehat r_i=s_i r_i
$$
的全部六个标量等式，及完整原组合
$$
\widehat r_iv=\sum_g s_i\tau_{i,g}\mathcal E_g. \tag{11}
$$
所有未付公因子都保留。本次六行的 paid content 剥除均只有常数；公共分母是真正已付权乘积。

以式 (10) 的固定行序和式 (6) 的固定列序，定义
$$
\mathcal M(e,k)=
\begin{pmatrix}
\widehat r_N\\
\widehat r_P\\
\widehat r_{yN}\\
\widehat r_{tN}\\
\widehat r_{yP}\\
\widehat r_{tP}
\end{pmatrix},\qquad \mathcal D(e,k)=\det\mathcal M(e,k). \tag{12}
$$
这一定义不含任何选择数值根、参数采样或未付逆。原点上 (11) 给
$$
\mathcal Mv=0,\qquad v_0=1,
$$
故 $\mathcal D=0$。

本次实际完成 (12) 的五步多项式 Bareiss 计算，共 55 个精确整除商积。每个商都在 $\mathbb Q[e,k]$ 内实际乘回，所以即使某个中间主元在某权点为零，最终行列式身份仍在那里成立；没有丢失瞬时主元零纤维。

完整非零 $\mathcal D$ 的双次数为 $(195,268)$、总次数 366，有 34516 项。按冻结源码的有序已付 gcd 规则取
$$
\mathcal D=c\,U\,P,\qquad c\in\mathbb Q^\times,\quad U\in A^\times, \tag{13}
$$
并将 $P$ 的固定字典序最高项系数归一为 1。$P$ 的此归一不宣称它关于 $e$ 或 $k$ 为首一式。式 (13) 的所有实际整除与最终完整乘积均已返回，所得 $P$ 恰为式 (1)。

实际付掉的非平凡 gcd 循环如下：
$$
e:11,\ k:5,\ u:3,\ Q-1:11,\ V:3,\ k+4:7,\
\operatorname{num}(P_{02}):6,\ \operatorname{num}(M):6,\
k+2:15,\ J_{19}:8,\ C_9:7.
$$
同样，这些是准确的逐次 gcd 循环计数；不能把它们重新解释成未经核验的完整因子幂公式。因为 $cU$ 在整个当前图均非零，$\mathcal D=0$ 推出式 (2)，证明定理。

## 5. 精确输入定义、规模及保存方式

(12)–(13)、旧六规则的固定头选择、原六式及冻结源码共同定义唯一 $P$，无需另附 8472 项大系数表。完整定义串的 SHA-256 是：

| 对象 | 规范定义串字节数 | SHA-256 |
|---|---:|---|
| 固定六行矩阵 | 1728830 | e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf |
| 完整 $\mathcal D$ | 3653552 | 0d2deb915985d0a4688add35a1caada7075eebbfe009c232072dd7fb2d81e8f1 |
| 已付归一后的 $P$ | 511382 | fdc5b144942e1baa0223b7aa437e4484f59ab694702e29878c7f848b8e2c52c6 |

这些可再生输出未保存成系数文件、编码块、矩阵缓存或证书 artifact。后续新数学输入须从本稿定义或冻结源所需前缀构造，不将这次完整成功行列式作为额外重复门。

六条多项式行的最大双次数依次为
$$
(29,37),(29,37),(37,49),(41,54),(37,49),(41,54),
$$
项数依次为 4346、4340、7092、8944、7086、8944。全部原乘法、六行原组合及多项式化在 10.527643947 秒前已完成；最终权必要式完整返回时间为 95.831038077 秒。

## 6. 唯一实际执行

源：
`notes/2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py`

- Git blob：`0d890247f59056395abfc41927b9b8f42b3cbafe`。
- SHA-256：`eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d`。
- 唯一依赖：`2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py`，完整 SHA-256 `10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1`。
- 只执行其 `def multiply_matrix` 之前的 15665 字节必要前缀，SHA-256 `c09268d1b0d4b21f565600b8d51fa13e493dd1aeb6628d5b0acceb9d1a6ffd22`；旧交换子、自适应 Gaussian、参数 cofactor 尾段未执行。
- run 46068841943；job 140740627266；源提交 `8b8da559c05cb1fb48d98f6b53daaf8fe0d321a3`。
- 180 秒 / 4 GiB 首次真实门；源内部最终时间 95.831201017 秒，驱动墙钟 95.890604382 秒，最大子进程 RSS 244388 KiB，内层真实退出码 0。
- stdout 9923 字节，SHA-256 `f7ed50f309f0d4c72ef34eb510004c45cd18e4945384c69f36f66e1e99d16ec6`。
- 2026-11-27 21:13:25.322959 UTC 真实 pull 后两 README blob 均未变。

本次得到整个当前 W 的明确必要权曲线；其所有剩余原有限纤维、与其它未付头曲线的交点以及同点个别原值返回继续保留。
