# R150：W/b0 的整个负 e、零 k 赋值射线由原 q2 与 R6 排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，既有 $p=1009$ 的整个权赋值射线
$$
v(e)<0,\qquad v(k)=0
\tag{1}
$$
不存在原解。证明直接使用同一点的原 $b_0$ 一次关系、完整 $q_2=0$、$R_6=0$ 产生估值矛盾。它先排除 $v(2\lambda-3)\le0$，因此也覆盖 $\lambda$ 极点和 $\lambda=0$；不以前次 $\bar\lambda=3/2$ 计算为证明前提。不需要对 $\mu=2\lambda-3$ 的正赋值再作分区，不需要新的矩阵、因式分解、投影或执行门。

这是一项新的纸面推论。先前十一式运行本身没有返回单位，其执行边界不改写。本条只排除 (1)，其余五条未闭权射线仍然保留；不宣称整个 W、整个 $b_0$ 原图或普通 ISP 排空。

## 1. 原图、独立实际记录与估值记号

全部权与原值沿当前 W 的已付图。使用
$$
u=e+1,\quad Q=ek,\quad \bar V=uk+2,\quad
\delta=1-Q,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{k\bar V},\qquad
m=u-\ell,\qquad M=\ell^2\delta-m^2,
\tag{2}
$$
$$
J=2u(1-u)+\ell Q,\qquad
A_*=4uQ-J,\qquad C_*=A_*m^2+J\delta\ell^2.
\tag{3}
$$
这里 $C_*$ 是旧 $a_\Delta$ 中的纯权系数，不是某个新范数。

[十一原首项与 lambda 剩余中心](R150-appendix-unit211-W-b0-eleven-original-initials-and-lambda-three-halves-residue-center.md)的唯一实际 run 46162974839 / job 141034199881 已在 (1) 的所有允许 $t$ 赋值格及 $t=0$ 中返回
$$
(2\bar\lambda-3)^2=0.
\tag{4}
$$
该实际结果是本条独立相符的先行记录；本条不使用它来限制 $\lambda$。第4节将仅由原 $b_0,q_2$ 自行证明
$$
v(2\lambda-3)>0\ \text{或}\ 2\lambda-3=0,\qquad
\bar\lambda=3/2.
\tag{5}
$$
因此 $\lambda$ 不是一个预设的单位坐标，(5) 也没有把特征零原点专门化为 $\lambda=3/2$。

为写清估值，设 $F$ 是包含假想原解的 $1009$ 进代数扩张，允许进一步代数扩张；$\mathcal O$ 是其赋值环，$\mathfrak m$ 是极大理想。约化记作上横线。取
$$
a=-v(e)>0,\qquad \kappa_0=\bar k\ne0.
\tag{6}
$$
因此 $e^{-1}\in\mathfrak m$。以下所有写出剩余值的商都将先证明属于 $\mathcal O$。不借复数大小、数值近似或裸模空性提升 QQ。

本条用到的完整原必要式与尺度，来自已刊源
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。这里只引用其中原定义和原身份，不重新执行任何源。

## 2. 无新逆的 b0 原 q2 恒等式

令
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{7}
$$
在本 $b_0$ 图上，原一次关系为
$$
A_*T+uQ\ell(3-2\lambda)=0.
\tag{8}
$$
它通常写成 $T=(uQ\ell/A_*)(2\lambda-3)$；以下推导直接使用 (8)，不再逆 $A_*$，尤其不逆其首系数。

完整 $q_2$ 来源是
$$
q_2=\frac{2a_\Delta}{\ell},
$$
$$
a_\Delta
=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*.
\tag{9}
$$
由 (2)–(3) 有整式恒等式
$$
MA_*+C_*=(A_*+J)\delta\ell^2
=4uQ\delta\ell^2.
\tag{10}
$$
(8) 乘以 $MT$，再代入 (9)，得到
$$
\boxed{\quad
q_2=2A_2C_*+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2.
\quad}
\tag{11}
$$
这只是原 $q_2$ 与原一次关系的代数重写，未除未知因子，未假设 $T\ne0$。

若记 $\mu=2\lambda-3$，同式亦可写为
$$
q_2=C_*(\mu^2+4\mu+5)
 -2M\ell Q(3+2\mu)-8uQ\delta\ell T^2.
\tag{12}
$$
以下先从 (11) 推出 (5)，再用它比较原 $R_6$；不需要为正 $\mu$ 赋值选择斜率。

第二个必要原式是
$$
R_6=MK^2-4m^2D^3=0.
\tag{13}
$$
它来自同一原矩值系统。本文没有把 $q_2$ 与 $R_6$ 的根独立拼接，也没有在 (11)–(13) 中引入 $D$ 逆。原必要性的适用范围仍是本来列明的当前 W、$D_{\rm phys}\ne0$、$b_0=0$ 图，不向未付图外推。

## 3. 全部 k 首值的统一权尺度

由 $v(k)=0$ 及 (2)，有
$$
\overline{u/e}=1,\qquad
\overline{Q/e}=\kappa_0,\qquad
\overline{\delta/e}=-\kappa_0,\qquad
\overline{\bar V/e}=\kappa_0.
\tag{14}
$$
特别 (2) 中所需分母的这一尺度首值非零。于是
$$
\overline{\ell/e}=-\frac2{\kappa_0},\qquad
m/e\in\mathcal O,\qquad
\overline{m/e}=1+\frac2{\kappa_0}.
\tag{15}
$$
$m/e$ 的剩余值允许为零；只需 $v(m)\ge-a$。

从 $M=\ell^2\delta-m^2$ 得
$$
\frac{M}{e^3}
=\left(\frac\ell e\right)^2\frac\delta e
 -e^{-1}\left(\frac m e\right)^2
\in\mathcal O,
$$
$$
\overline{M/e^3}=-\frac4{\kappa_0}\ne0,
\qquad v(M)=-3a.
\tag{16}
$$
再由 $1-u=-e$，
$$
\overline{J/e^2}=-4,\qquad
A_*/e^2\in\mathcal O,\qquad
\overline{A_*/e^2}=4(\kappa_0+1).
\tag{17}
$$
(17) 的最后一个剩余值也允许为零。

在 $C_*$ 中，
$$
\frac{C_*}{e^5}
=e^{-1}\frac{A_*}{e^2}\left(\frac m e\right)^2
 +\frac J{e^2}\frac\delta e\left(\frac\ell e\right)^2.
$$
第一项在 $\mathfrak m$ 中，第二项首值固定非零。所以
$$
\overline{C_*/e^5}=\frac{16}{\kappa_0},
\quad
\overline{M\ell Q/e^5}=\frac8{\kappa_0},
\quad
\overline{8uQ\delta\ell/e^4}=16\kappa_0.
\tag{18}
$$
这些结论覆盖每个 $\kappa_0\ne0$。尤其 $\kappa_0=-1$ 可能使 $A_*$ 的所列首值消失，$\kappa_0=-2$ 可能使 $m$ 的所列首值消失，都没有被排掉，也不妨碍 (18)。

## 4. 原 q2 先迫 mu 正阶，再迫 T 的准确半阶

先不对 $\lambda$ 作任何估值假设。设 $\mu=2\lambda-3\ne0$ 且
$$
s=v(\mu)\le0.
\tag{18a}
$$
由 (14)–(15)，$v(uQ\ell)=-3a$。原 (8) 为 $A_*T=uQ\ell\mu$；其右端非零，因此 $A_*,T$ 在这种情况下自动非零。由 (17) 的 $v(A_*)\ge-2a$ 得
$$
v(T)=-3a+s-v(A_*)\le-a+s.
\tag{18b}
$$
这里没有把 $A_*/e^2$ 的剩余值付成单位。

由于 $\lambda=(\mu+3)/2$，有 $v(\lambda)\ge s$。从定义直接得
$$
v(A_2)\ge2s,\qquad v(3-4\lambda)\ge s\ge2s.
$$
结合 (18)，(11) 的两个非 $T$ 项之和估值至少 $-5a+2s$；而其 $T^2$ 项满足
$$
v(8uQ\delta\ell T^2)
=-4a+2v(T)\le-6a+2s<-5a+2s.
\tag{18c}
$$
所以 (11) 不可能为零，排除 (18a)。这同时包含 $\lambda$ 极点，以及 $\lambda=0$ 对应的 $\mu=-3$。

因此或 $\mu=0$，或 $v(\mu)>0$，都给 (5)。$\mu=0$ 在以下论证中同样被保留，不需要另外调用整个 $\lambda=3/2$ 排除。于是

$$
\bar A_2=5/2,\qquad
\overline{3-4\lambda}=-3,\qquad
\bar B_3=7/2.
\tag{19}
$$
因此 (11) 中不含 $T^2$ 的部分满足
$$
\overline{
\frac{2A_2C_*+2M\ell Q(3-4\lambda)}{e^5}
}
=5\frac{16}{\kappa_0}
 -6\frac8{\kappa_0}
=\frac{32}{\kappa_0}\ne0.
\tag{20}
$$
原 $q_2=0$ 精确给
$$
\frac{T^2}{e}
=
\frac{(2A_2C_*+2M\ell Q(3-4\lambda))/e^5}
     {(8uQ\delta\ell)/e^4}.
\tag{21}
$$
分母是由 (18) 已证明的赋值环单位，不是新假设的几何首项。由 (18)、(20) 得
$$
T^2/e\in\mathcal O^\times,\qquad
\overline{T^2/e}=\frac2{\kappa_0^2},
\qquad v(T)=-a/2.
\tag{22}
$$
故 $T=0$ 也已在这个射线上被 (21) 排除，不需要事先删去它。

由 (7)、(15)、(19)、(22)，
$$
D/e\in\mathcal O,\qquad
\overline{D/e}=-\frac5{\kappa_0}-\frac2{\kappa_0^2}.
\tag{23}
$$
(23) 的首值可以为零；只使用 $v(D)\ge-a$，不把该首值付成单位。

## 5. R6 两项不可能相消

在 (7) 的 $K$ 中，第一项 $\ell^2B_3$ 的估值为 $-2a$。另外两项满足
$$
v(\ell A_2T)=-3a/2,\qquad v(T^3)=-3a/2,
$$
都严格大于 $-2a$。所以
$$
K/e^2\in\mathcal O^\times,\qquad
\overline{K/e^2}=\frac{14}{\kappa_0^2},
\qquad v(K)=-2a.
\tag{24}
$$
结合 (16)，
$$
v(MK^2)=-7a.
\tag{25}
$$
另一方面，由 (15)、(23)，
$$
v(4m^2D^3)\ge-5a>-7a.
\tag{26}
$$
一个估值严格较低的非零项不能与估值较高的项相消，(25)–(26) 与原 $R_6=0$ 矛盾。

也可直接将同一原式除以 $e^7$ 后取剩余值：
$$
\overline{\frac{R_6}{e^7}}
=\left(-\frac4{\kappa_0}\right)
 \left(\frac{14}{\kappa_0^2}\right)^2-0
=-\frac{784}{\kappa_0^5}\ne0
\quad\text{于特征 }1009.
\tag{27}
$$
因此 (1) 的整个原权赋值射线排除。所有可能的 $m$、$A_*$、$D$ 首值零面均已包含在上述不等式内。

## 6. 执行历史与剩余边界

本条没有新数学运行，也不依赖新的初始理想执行作为证明前提。已刊十一原式 actual 的 (4) 是独立一致的记录：该次内层 3.326495765 秒 / 60380 KiB / exit0，stdout SHA256 e6915c4a0d0ad780a6bd00f0c7a2917a4208882f15e51dd0deaa591976b08b41。它当时只给剩余中心，未返回单位；这里的新排除来自 (8)、(11)、(13) 以及 (14)–(27) 的原恒等式与估值推导。

正 $\mu$ 中心三原输入 source 695cdf756fb02629a507a650a3126ac4a3d54b20 / input f106072aca8fccbc6f2f57001d6ebe628c309d1f 已有独立唯一 actual run 46164894855 / job 141040154752。其部分格单位、其它格未闭的真实结果应由独立回执记录；不能把本文的全射线排除改记为该程序已经返回全部格单位。本纸证尤其保留该分区中因 $A_*$ 首值下降而出现的全部格。

本条不证明 $e,k$ 在所有赋值下整，不构造完整 $1009$ 整权模型，不改变其余五条剩余射线。它也不提供新的全局原点数或 Artin 长度。后续工作须处理其它实际边界或加入真正新的原条件，不重跑已成十一式、旧投影、固定标量或本射线的同目标门。
