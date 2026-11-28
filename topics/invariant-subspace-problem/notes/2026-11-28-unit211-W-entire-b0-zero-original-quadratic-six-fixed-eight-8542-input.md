# 新输入：W 整 b0 零支的原 lambda 二次、六次与固定八阶权覆盖

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**尚未执行。** 自含零依赖；唯一首次预算 $180$ 秒、$4$ GiB。
源 basename：
2026-11-28-unit211-W-entire-b0-zero-original-quadratic-six-fixed-eight-8542.py。
源 $9617$ 字节，SHA256
a11fa3741692def8a90a04324378be92531c6e55569da596c59321e8b4116677。

## 1. 原域和本次只研究的整支

仍是当前 W、原 singleton 两值互异、物理 $D\ne0$ 的图。
沿已刊原权参数
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},
$$
$$
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2=\ell^2\delta-m^2=4bc\delta,
$$
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2 .
$$
当前 $u,Q,\ell,m,M,\delta$ 都已付。
$A_*$ 尚未在一般 W 图上支付，本篇也不这样做。

只接上一原四次来源中的整零支
$$
b_0=2m\{A_*T+uQ\ell(3-2\lambda)\}=0.                  \tag{1}
$$
这里不是任意选开的几何图；下面先完整处理 (1) 中
$A_*=0$ 的可能性。

## 2. Astar 零面和唯一 T 恢复

若 (1) 同时有 $A_*=0$，则原已付 $muQ\ell$ 迫
$3-2\lambda=0$。
[整个 W 的 lambda=3/2 原支](../results/R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)
已经独立关闭，包括所有原首项零面。
因此 $A_*$ 在整个当前 (1) 支上非零，且只在这个支内可用
$$
\kappa=\frac{uQ\ell}{A_*},\qquad
T=-\kappa(3-2\lambda).                                 \tag{2}
$$
没有把 $A_*$ 支付到 $b_0\ne0$ 的补图。
本次源不再执行旧 lambda=3/2 门。

## 3. 两条真正原必要式

沿
[两个原四次必要式](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)
和
[原完整 N4(V) 低 D 压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，
定义
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,
$$
$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ\ell(3-2\lambda)T+DC_*,\\
b_\Delta={}&Mb_0,\qquad
C_4=2mD\,a_\Delta+K b_\Delta,\\
R_6={}&MK^2-4m^2D^3.
\end{aligned}                                         \tag{3}
$$
$C_4,R_6$ 都是同一点完整原值系统的必要式。

在 (1) 中，$C_4=2mD\,a_\Delta$。
只有此处使用原物理 $mD\ne0$，得到 $a_\Delta=0$。
不从任何模 $D$ 幂零结论提升 QQ，也不向 $D=0$ 值碰撞图外推。

用 (2)，令 $n=2\lambda-1$，直接有
$$
MA_*+C_*=4uQ\delta\ell^2,\qquad T=\kappa(n-2).
$$
从而得到真正低次二次
$$
q_2=\frac{2a_\Delta}{\ell}
=2M\ell Q(1-2n)+C_*(n^2+1)
 -8uQ\delta\ell\kappa^2(n-2)^2.                         \tag{4}
$$
源将完整返回 (1)–(4) 的每个相关乘积。
$R_6$ 在同一 $T$ 代入后对 $\lambda$ 次数至多六。
本次保留
$$
q_2(\lambda)=R_6(\lambda)=0                            \tag{5}
$$
的全部原物理必要性，没有把它们宣称为充分系统。
其他原 Gram、均值、N/P 和完整值条件都继续保留。

## 4. 纯权清分母和固定八阶

两式分母仅来自已付纯权单位与本支已经支付的 $A_*$。
源逐项检查其分母支持。
分别从两个完整分子只剥已付纯权内容并乘回，
得实际多项式 $\widehat q_2,\widehat R_6$；
不剥未知 $\lambda$ 首项或几何因子。

按 $1,\lambda,\ldots,\lambda^7$ 排列列：
前六行取 $\lambda^j\widehat q_2$、$0\le j<6$，
后两行取 $\lambda^j\widehat R_6$、$0\le j<2$。
每行实际重建原输入倍数，定义
$$
S_8(e,k),\qquad H(e,k)=\det S_8(e,k).                   \tag{6}
$$
固定次数界始终是 $2,6$，不是专门化之后挑选的首项。
若某点有共同有限 $\lambda_0$，那么
$$
S_8(e,k)(1,\lambda_0,\ldots,\lambda_0^7)^t=0.            \tag{7}
$$
所以 (6) 在每个当前原点为零，
即使二次或六次的一个、两个首项同为零，(7) 仍成立。

所有 Bareiss 商必须整除并逐个乘回。
临时主元只用于建立 $\mathbb Q[e,k]$ 中的固定多项式身份；
其零面不因此删除。若 (6) 实际恒零，源明确不给新权覆盖。

若非零，再只剥已付权支持，并实际核完整乘回，
最后 QQ 因式分解并保每个未付因子及其重数。
这仅给整个 (1) 的必要权曲线；除非实际剩余为常数单位，
不宣称整支排空，不以多元 gcd 为一或数值采样作替代。

## 5. 准确的已付支持

基础列表沿已经发表的完整 alpha/chi 原图使用：
$e,k,u,\delta,\overline V,k+4,P_{02},M,k+1,H_{\rm old}$，
以及整个等权、$\ell=0$、J19、C9 支排除所付支持。
其中
$$
H_{\rm old}=4ek-k^2-4k-8.
$$
源码完整写出 J19、C9 与所有原权有理式，不调用旧 native 门。

另加两个有明确原出处的支持：

1. 仅本 (1) 支上的 $A_*$，由第 2 节付清；
2. 全当前 W 的 $2\ell-1$，引用
   [整个 Lhalf 原排除](../results/R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)。
   该整支最终实际是 run46104932037/job140855440829，
   $23.034741738$ 秒、$158328$ KiB、退出零；
   不是仅给 F101 有限覆盖的较早结论。

源码的每个 gcd 层只作为实际除法记录，
不会将复合支持的“层数”当成该整个多项式的幂次。
所有没有被这张已付表覆盖的权因子均留在新曲线中。
特别 $A_*$ 的整零面已经按原 (1) 支支付，
而其他原未付头零绝不隐去。

## 6. 唯一首次与来源隔离

本源自含，只从 (2)–(5) 新建这一个固定八阶矩阵。
不再生 native 六规则、122 秒四次两列、
旧 qT4/Vlow、旧十二乘法动作、旧 lambda 模块或任何冻结结式。
已成原定理只作数学来源，不作为新的复算门。

首次上限 $180$ 秒 / $4$ GiB，单个绝对定时器，无嵌套重置。
按实际完成的阶段返回次数、项数、字节数、SHA、
精确除法数和运行回执；不输出大系数、矩阵、encoded payload 或分片。
若资源界先到，只保最后真正完成的阶段及全部尚未返回的范围。
