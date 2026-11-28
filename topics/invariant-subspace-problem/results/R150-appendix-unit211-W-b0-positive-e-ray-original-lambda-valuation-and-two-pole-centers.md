# R150：W/b0 正 e、零 k 射线的原 lambda 估值限制与极点中心

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，取 $1009$ 上方的赋值。设
$$
v(e)>0,\qquad v(k)=0,\qquad \zeta=\bar k\ne0.
\tag{1}
$$
则同一点的原必要式给出
$$
\boxed{\quad
\zeta\ne-2\quad\Longrightarrow\quad
\lambda\ne0,\quad v(\lambda)\le0.
\quad}
\tag{2}
$$
进一步，
$$
\boxed{\quad
\zeta\ne-2,\quad v(\lambda)<0
\quad\Longrightarrow\quad \zeta=4.
\quad}
\tag{3}
$$
因此本射线上，零或正估值的 $\lambda$ 只可能位于 $\bar k=-2$ 中心；所有 $\lambda$ 极点只可能位于 $\bar k\in\{-2,4\}$。本文没有排除这些中心，也没有排除其余 $\bar k$ 上的单位 $\lambda$。

证明是新的原有理式估值推导，没有重新执行六射线初始理想或任何已冻结目标。尤其 (2) 包含 $M$ 首值为零的 $\zeta=-4$；没有把 $M$ 的首值或新的几何头当作单位。

## 1. 范围、赋值和原必要身份

当前原点的代数性与选择 $1009$ 上方赋值的依据，见[全权 Artin 必要模型](R150-appendix-unit211-W-entire-b0-23088-normalized-Artin-length.md)及[六射线原最低项记录](R150-appendix-unit211-W-b0-original-initial-ideals-and-two-lambda-valuation-restrictions.md)。允许在包含全部坐标的赋值域内作代数扩张。记赋值环为 $\mathcal O$，极大理想为 $\mathfrak m$，剩余域包含在 $\overline{\mathbb F}_{1009}$。所有写出上横线的量先证明属于 $\mathcal O$。

沿当前 W 原定义，
$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad V_b=uk+2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{kV_b},\quad
m=u-\ell,\quad M=\ell^2\delta-m^2,
\tag{4}
$$
$$
J=2u(1-u)+\ell Q,\quad
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2.
\tag{5}
$$
这里 $V_b$ 只是纯权分母，不是物理向量。

设
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{6}
$$
同一点的原 $b_0$ 一次条件是
$$
A_*T=uQ\ell(2\lambda-3).
\tag{7}
$$
完整 $q_2$ 在 (7) 下的准确重写为
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0.
\tag{8}
$$
这来自
$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*,
\quad q_2=2a_\Delta/\ell,
$$
以及整恒等式 $MA_*+C_*=4uQ\delta\ell^2$；只代入 (7)，不倒任何新头。

另一个完整原必要式为
$$
R_6=MK^2-4m^2D^3=0.
\tag{9}
$$
(4)–(9) 的原来源是已刊[完整 b0/N5 原定义源码](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。本文只用其原定义和必要身份，不执行旧尾段，也不使用完整 N5 作为本结论的前提。

## 2. k 剩余值不为负二时的准确权剩余值

暂设 $\zeta\ne-2$。由 (1)，$u,\delta,k,V_b$ 都是赋值环单位，且
$$
\bar u=\bar\delta=1,\quad
\bar V_b=\zeta+2.
$$
置
$$
L=\frac{\zeta+2}{\zeta}.
\tag{10}
$$
则
$$
\bar\ell=L\ne0,\qquad
\bar m=1-L=-\frac2\zeta\ne0,\qquad
\bar M=2L-1.
\tag{11}
$$
这里 $L-1=2/\zeta\ne0$。最后一个剩余值允许为零；当 $\zeta=-4$ 时确实为零。以下从不倒它。

由 $1-u=-e$ 与 $Q=ek$，
$$
\frac JQ=-\frac{2u}{k}+\ell,\qquad
\overline{J/Q}=1,\qquad
\overline{A_*/Q}=3.
\tag{12}
$$
因此 $A_*/Q$ 是已经从原式证明的赋值环单位，(7) 精确给
$$
T=\kappa(2\lambda-3),\qquad
\kappa=\frac{u\ell}{A_*/Q}\in\mathcal O^\times,
\qquad \bar\kappa=L/3.
\tag{13}
$$
这没有预先付 $A_*$ 的首项；它的单位性来自 (12)。

记
$$
G=3(1-L)^2+L^2=4L^2-6L+3.
\tag{14}
$$
(5)、(11)、(12) 给
$$
C_*/Q\in\mathcal O,\qquad
\overline{C_*/Q}=G,\qquad
\overline{M\ell}=(2L-1)L.
\tag{15}
$$
$G$ 也允许为零。全部后续取剩余值只使用这些整性，不倒 $G$。

## 3. 排除 lambda 为零或正估值

设 $\lambda=0$ 或 $v(\lambda)>0$。此时 $\lambda\in\mathfrak m$，从 (6)、(13) 得
$$
\bar A_2=1,\quad \bar B_3=-1,\quad \bar T=-L.
\tag{16}
$$
因此 $q_2/(2Q)$ 的每个项都在 $\mathcal O$。由 (8) 取剩余值得
$$
\begin{aligned}
0
&=G+3(2L-1)L-4L^3\\
&=-4L^3+10L^2-9L+3\\
&=-(L-1)G.
\end{aligned}
\tag{17}
$$
$L-1\ne0$，所以
$$
G=0.
\tag{18}
$$

另一方面，(6)、(11)、(16) 给
$$
\bar D=L(1-L),\qquad
\bar K=2L^2(1-L).
\tag{19}
$$
这两个量均非零，因为 $L\ne0,1$。将同一个原点代入 (9) 的剩余式，
$$
0=4(1-L)^2L^3\bigl((2L-1)L-(1-L)^3\bigr).
\tag{20}
$$
故
$$
P=L^3-L^2+2L-1=0.
\tag{21}
$$
准确的多项式短除恒等式为
$$
P=\frac{2L+1}{8}G+\frac{16L-11}{8}.
\tag{22}
$$
(18)、(21) 因而迫 $L=11/16$，但
$$
G(11/16)=49/64\ne0
\quad\text{于特征 }1009.
\tag{23}
$$
矛盾，得到 (2)。此论证也覆盖 $\bar M=0$，没有对 $R_6$ 除 $M$ 或 $D$。

## 4. 原 q2 把 lambda 极点收至 k 剩余值 4

仍设 $\zeta\ne-2$，现在假设 $v(\lambda)<0$。从 (13)，
$$
T/\lambda\in\mathcal O^\times,\qquad
\overline{T/\lambda}=2L/3.
\tag{24}
$$
同时
$$
\overline{A_2/\lambda^2}=2,\qquad
(3-4\lambda)/\lambda^2\in\mathfrak m.
\tag{25}
$$
因而 (8) 除以 $Q\lambda^2$ 后全部项在 $\mathcal O$，取剩余值得
$$
\begin{aligned}
0
&=4G-\frac{32L^3}{9}\\
&=\frac49(3-2L)^3.
\end{aligned}
\tag{26}
$$
剩余域是域，$2,3$ 均非零，故 $L=3/2$。结合 (10)，这恰等价于
$$
\zeta=4.
\tag{27}
$$
(26) 是同一完整原 $q_2$ 的必要剩余式；没有把三次幂改成原特征零等式，也没有因为一个首值为零就宣布整个极点中心有解或已排除。

## 5. 准确新范围与未闭输入

旧六射线源码 83e0779c74d39affde14d8b42681454ccacf324a 的实际记录，在 $(1,0)$ 的 $v(\lambda)<0,>0,=0$ 以及 $\lambda=0$ 格均保留必要公因式。本条不改变那次实际输出。新的 (2)–(3) 来自 (7)–(9) 在 $\bar k\ne-2$ 上的原有理式及可证单位尺度；没有重跑该初始理想、增预算、换素数或换算法续旧目标。

以下情形仍开：

- $\bar k=-2$ 的整个更深中心，含所有 $\lambda$ 估值与可能的 $\lambda=0$；
- $\bar k=4$ 的 $\lambda$ 极点中心；
- $\bar k\ne-2$、$v(\lambda)=0$ 的同点完整均值和值条件，含 $\bar M=0$ 的中心；
- 其它尚未关闭的权射线、$v(e)=v(k)=0$ 内部和所有已付纯权分母的 DVR 边界。

本条没有证明正 $e$ 射线整体为空，没有使所有权在 $1009$ 上整，也没有给完整有限 DVR 原模型或新的全局长度。整个 W 和普通 Hilbert ISP 继续未完成。
