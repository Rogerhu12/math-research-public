# R781 原尖点切向下降、无 κ 逆幂的 Laurent 递推与二十坐标关系

日期：2026-11-14。状态：**证明完成；后述准确数值阶段尚未预称执行成功。**

固定 R759/R764 的原第 4 号映射 $f_0$、次数 $1206$、原目标
$C/L:y^2=x^3+b$，以及 R774 实际 $e=1$。本篇把同一原参考 cusp 的准确算术降到 $M^+=L(\xi+\xi^{-1})$，并给出不需要反演 $\kappa$ 的 142 阶 Laurent 构造。最终仍验证同一个原 $L$-函数；原 $b$、$h$、$c_0$、$c_1$ 及 Fourier 相位均保持。

## 1. 原行列式负一元与准确切向相位

沿用 R772/R778 的原算术群
$$
G_{82}=C_3\times N_{\mathsf T_\zeta}
\subset\operatorname{GL}_2(\mathbf Z/82\mathbf Z),
\qquad
K=\mathbf Q(s),\quad L=K(b),\quad M=L(\xi),
$$
$$
s^2=-3,\quad \xi=e^{2\pi i/41},\quad
u=q_Y=e^{2\pi i\tau/82},\quad \xi_{82}=-\xi^{21}.
\tag{781.1}
$$
考虑实际矩阵
$$
g=\begin{pmatrix}-1&40\\0&1\end{pmatrix}\pmod{82}.
\tag{781.2}
$$
其 mod 2 分量是恒等，mod 41 分量是原反射
$J=\left(\begin{smallmatrix}-1&-1\\0&1\end{smallmatrix}\right)$，故 $g\in G_{82}$。
在原右作用约定中，
$$
g=-\operatorname{diag}(1,-1)\,T^{-40}.
\tag{781.3}
$$
右侧作为整数矩阵就给出 (781.2)，不是只按行列式猜测的分解。

若 $f=\sum_n a_nu^n$ 是原 $Y$ 上的 $K$-定义偶权形式，或者 $L$-定义的原模函数，$-I$ 在该偶权作用下平凡，$\operatorname{diag}(1,-1)$ 对常数施加
$\sigma_{-1}:\xi\mapsto\xi^{-1}$、固定 $L$。由 R772 的半线性右作用及 $f*g=f$，
$$
\sigma_{-1}(f)|T^{-40}=f.
$$
而 $u(\tau-40)=\xi^{-20}u(\tau)$，因此逐项得到
$$
\boxed{\sigma_{-1}(a_n)=\xi^{20n}a_n.}
\tag{781.4}
$$
对模函数的负 Laurent 指数，同一式仍成立。这里没有把一般复共轭作用在 $s$ 或 $b$ 上；$\sigma_{-1}$ 是 $M/L$ 中固定这些原量的指定 involution。

现在作明确的局部切向换参
$$
v=\xi^{-10}u,\qquad u=\xi^{10}v.
\tag{781.5}
$$
新系数为 $a_n^+=a_n\xi^{10n}$。由 (781.4)，
$$
\sigma_{-1}(a_n^+)
=\xi^{20n}a_n\xi^{-10n}=a_n^+.
$$
所以
$$
\boxed{a_n^+\in M^+:=L(\xi+\xi^{-1}),\qquad
[M^+:L]=20,\quad[M^+:\mathbf Q]=280.}
\tag{781.6}
$$
逆运输恰为 $a_n=a_n^+\xi^{-10n}$。换参是显式非零常数倍，保留零阶、极点阶及
$$
\mathscr D=\frac1{82}u\frac d{du}
=\frac1{82}v\frac d{dv}.
\tag{781.7}
$$

这不声称 $L$ 本身可再减半，也不改变 R777 已使用的原四十坐标。它只是为本篇后继准确算术使用一个已证明的二十坐标字段。原 $K$ 扭曲与标准模型的识别仍是 R772 的
$E_6/\eta_{\rm Ded}^{12}=24s(2t-1)$，所以 (781.4) 的算术群确作用在原曲线上。

## 2. 从原四十坐标到二十坐标的整数转换

令
$$
t_\xi=\xi+\xi^{-1},\qquad
S_0(T)=2,\quad S_1(T)=T,\quad
S_{r+1}(T)=TS_r(T)-S_{r-1}(T).
$$
则 $S_r(t_\xi)=\xi^r+\xi^{-r}$，且
$$
g_{41}(T):=1+\sum_{r=1}^{20}S_r(T)
\tag{781.8}
$$
是 $t_\xi$ 的 monic 二十次最小多项式：它由 $\Phi_{41}(\xi)=0$ 得到，次数与
$[\mathbf Q(\xi+\xi^{-1}):\mathbf Q]=20$ 相同。

先按 (781.5) 将一项原系数乘 $\xi^{10n}$，并用 $\Phi_{41}$ 约化为
$\sum_{r=0}^{39}c_r\xi^r$。添 $c_{40}=0$。其被 $\sigma_{-1}$ 固定，当且仅当
$$
c_r=c_{41-r}\qquad(1\le r\le20).
\tag{781.9}
$$
证明是：两循环表示之差的常数项为零；若差在 $\xi$ 处为零，它作为至多四十次多项式只能是 $\Phi_{41}$ 的常数倍，常数项又迫该倍数为零。

因此可准确转换为
$$
c_0+\sum_{r=1}^{20}c_rS_r(t_\xi)
\pmod{g_{41}(t_\xi)},
\tag{781.10}
$$
再约化至次数小于 20。整个转换是整数线性变换，不含隐藏的 $1/2$。

对于 R774 的十四个有理坐标行，可先对其 primitive 整数行执行这个变换，仍保留原行尺度 $\rho_i$。如果某尺度为零，其原整数行也为零；不会产生例外的除法。实际执行必须逐项核 (781.9)，以验证相位运输和字段投影。

## 3. 原 y 的首系数与唯一形式解

在新参数中写
$$
\mathcal H(v)=H^3=\sum_{j\ge1}\kappa_jv^j,\qquad
\kappa:=\kappa_1\ne0,\qquad
A_0(v)=\frac{\mathcal H(v)}{\kappa v}.
\tag{781.11}
$$
R774 的实际 $e=1$ 保证 $\kappa\ne0$。若原 $u$ 参数中的首系数为 $\kappa_u$，则
$\kappa=\xi^{10}\kappa_u$。

原 $f_0(P)=O$ 的 $y$ 有一阶 $v$ 极点。由 R772 的准确方程
$$
(\mathscr Dy)^3=27(y^2-b)^2\mathcal H
\tag{781.12}
$$
比较最低阶，得到
$$
C=-\frac1{246^3\kappa},\qquad
y=Cv^{-1}Z(v),\qquad Z(0)=1.
\tag{781.13}
$$
其中 $246^3=27\cdot82^3$。原 $u$ 首系数 $C_u$ 与它满足
$C=\xi^{-10}C_u$，与 (781.5) 对负指数的运输相同。

将 (781.13) 代入 (781.12)，精确得到
$$
(Z-vZ')^3=A_0(v)(Z^2-cv^2)^2,\qquad
c=246^6b\kappa^2.
\tag{781.14}
$$
暂将 $Z_n$ 置零时，设左减右的第 $n$ 阶系数为 $E_n$。真正未知 $Z_n$ 的系数为
$3(1-n)-4=-(3n+1)$，因此 $Z_n=E_n/(3n+1)$。这逐阶唯一确定同一原 $y$，不另选立方根或 CM 符号。

## 4. 避免 κ 反演和全部代数逆幂

为了实际生成关系矩阵，无需先算 (781.13) 中的 $\kappa^{-1}$。再作纯形式缩放
$$
v=\kappa w,\qquad R(w)=Z(\kappa w).
$$
$\kappa$ 是系数域中的固定非零常数，所以 $v\,d/dv=w\,d/dw$。置
$$
\widetilde A_0=1,\qquad
\widetilde A_n=\kappa_{n+1}\kappa^{\,n-1}\ (n\ge1),\qquad
c_*=246^6b\kappa^4.
\tag{781.15}
$$
则
$$
\boxed{
(R-wR')^3=\widetilde A(w)(R^2-c_*w^2)^2,\qquad R_0=1.
}
\tag{781.16}
$$
所有输入只含原 $\kappa_j$、$b$ 的非负幂。若 $E_n^*$ 是暂取 $R_n=0$ 时的左减右残差，
$$
\boxed{R_n=\frac{E_n^*}{3n+1}\qquad(1\le n\le142).}
\tag{781.17}
$$
全过程只需同一 $M^+$ 中的乘法、加法，以及除以明确的非零有理整数。它不需要代数 $\kappa$ 的逆元，也不保存逐阶增长的 $\kappa^{-n}$。

令
$$
W=R-wR',\qquad U=R^2-c_*w^2.
$$
通过逐阶保留 $R^2,W^2,U^2$，计算 (781.16) 的新系数只需已有系数的卷积。每一阶用线性于 $n$ 的域运算，全部至 142 阶为二次数量的域运算；无须每次重做此前完成的整个幂级数乘法。每个完成阶与这些卷积状态一起保存，续算直接恢复。

## 5. 清除代数分母后的原 143 条关系

由 (781.13) 和 $Z(v)=R(v/\kappa)$，
$$
[v^n]y=-\frac{R_{n+1}}{246^3\kappa^{n+2}}
\qquad(n\ge-1).
\tag{781.18}
$$
现在令 $A(v)=\sum_{n\ge0}A_nv^n$、$B(v)=\sum_{n\ge0}B_nv^n$ 为 R778 的两个原 numerator 基组合，未知基坐标在 $L$ 中。对每个 $-1\le n\le141$，乘以非零的 $246^3\kappa^{n+2}$，得到准确等价式
$$
\boxed{
246^3\kappa^{n+2}A_n+
\sum_{j=0}^{n+1}\kappa^jR_{n-j+1}B_j=0,
}
\tag{781.19}
$$
其中 $A_{-1}=0$。特别是 $n=-1$ 恰给 $B_0=0$，没有引入额外根或丢掉原 cusp 极点。

所有系数都在 $M^+$，按
$1,t_\xi,\ldots,t_\xi^{19}$ 展开后，至多得到
$$
143\cdot20=2860
$$
个 $L$-线性行，未知数量仍是 $2\cdot1514=3028$。由 R778，完整矩阵的实际全球核维数为 308、秩为 2720；本篇并未把理论秩冒作一个已经执行的数值结果。

若一个非零候选 $(A,B)$ 以特征零准确通过全部 (781.19) 的二十坐标，它就通过原 R778 的全部 143 个 Laurent 条件。因为两次换参都是明确非零常数缩放，且逐行乘数非零，R778 立即证明 $A/B$ 是同一个原 $y$。无需另外求完整 308 维核才能认证这个候选。

原 $u$ 坐标可以通过 (781.5) 准确运回。使用原 $h$ 的
$x=3(y^2-b)h/dy$ 仍固定原目标微分方向；本篇没有从立方单独选择 $x$ 的三个 CM 分支。

## 6. 同一原字段中的准确整数乘法

为使每次域约化不引入原 $b$ 多项式的有理分母，设其原 monic 七次多项式为
$$
f_b(X)=X^7+\sum_{i=0}^6a_iX^i.
$$
R774 已证各 $a_i$ 的分母只含 2、3。根据每个既有准确 $a_i$ 的最简分母，取
$$
A_\lambda=\max_i\left\lceil\frac{v_2(\operatorname{den}a_i)}{7-i}\right\rceil,\qquad
B_\lambda=\max_i\left\lceil\frac{v_3(\operatorname{den}a_i)}{7-i}\right\rceil,
$$
$$
\lambda=2^{A_\lambda}3^{B_\lambda},\qquad B=\lambda b.
\tag{781.20}
$$
这些指数须由实际原数据计算并保存，不预填数值。于是
$$
f_B(X)=\lambda^7 f_b(X/\lambda)\in\mathbf Z[X]
\tag{781.21}
$$
是 monic 七次不可约多项式。本篇只更换同一字段的算术基，目标系数始终是 $b=B/\lambda$，没有更换原扭曲模型。

使用准确有理基
$$
B^i s^j t_\xi^r,\qquad
0\le i<7,\quad0\le j<2,\quad0\le r<20.
\tag{781.22}
$$
对两个整数系数向量，打包指数为
$$
r+39i+507j,\qquad507=39\cdot13.
\tag{781.23}
$$
乘积满足 $r\le38,i\le12,j\le2$，故这种普通整数多项式乘法没有内部进位歧义。随后准确按
$$
s^2=-3,\qquad f_B(B)=0,\qquad g_{41}(t_\xi)=0
\tag{781.24}
$$
约化。三个关系都是不同变量上的 monic 整数关系，所以得到唯一的 280 个有理基坐标。

每个域元素可存为一个 primitive 整数向量乘一个有理数 $\rho$。乘法只先乘整数向量，约化后提出 content 并吸收到 $\rho$。加法先取两个 $\rho$ 的有理 gcd，再按整数比例合并向量、提出 content。这样巨大共同的 2、3 幂可以保存在一个有理尺度中，而不在 280 个坐标中重复展开。

这种表示是准确的，无需先执行 280 阶 $\kappa$ 反演。逐阶记录实际向量 bit 长度与尺度大小，以真实产物判断内存和后续算法，不预称其高度小。

## 7. 完整普通分母界

本节给出有限截断的确定分母控制，不要求程序为了使用它而膨胀每一个坐标。

令 $\mathcal O=\mathbf Z[B,s,t_\xi]$，并取一个正整数 $D$，使全部实际
$\kappa_1,\ldots,\kappa_{143}$ 都在 $D^{-1}\mathcal O$ 中。它可以直接取准确输入各尺度分母的最小公倍数；无需对 $\kappa$ 的代数范数作因式分解。置
$$
S=D^2\lambda,\qquad
\Delta_0=1,\qquad
\Delta_n=\prod_{j=1}^n(3j+1)^{\lfloor n/j\rfloor}.
\tag{781.25}
$$
由 (781.15)，$\widetilde A_n\in S^{-n}\mathcal O$，
$c_*\in S^{-2}\mathcal O$。按权
$\operatorname{wt}\widetilde A_j=j,\operatorname{wt}c_*=2,\operatorname{wt}R_i=i$
归纳，(781.16) 的第 $n$ 阶残差齐次权为 $n$。

对其中任何已知 $R_i$ 的乘积，所有 $i<n$ 且指标总和不超过 $n$。对每个 $j<n$，
$\sum_i\lfloor i/j\rfloor\le\lfloor n/j\rfloor$；而 $j=n$ 尚未出现。故其全部整数分母的乘积整除
$\Delta_n/(3n+1)$。再使用 (781.17)，得到
$$
\boxed{R_n\in(S^n\Delta_n)^{-1}\mathcal O
\qquad(0\le n\le142).}
\tag{781.26}
$$
特别地，所有除法都是有限的普通整数分母，不含未控制的代数 $\kappa$ 逆幂。

若使用 R777 的统一整数权十二基，则 (781.19) 的第 $n=m-1$ 行中，每个矩阵条目乘
$$
D\,S^m\Delta_m
\tag{781.27}
$$
后属于 $\mathcal O$。第一项用 $\kappa^{m+1}\in D^{-(m+1)}\mathcal O$，
其余项用 $D\mid S$、$\Delta_{m-j}\mid\Delta_m$ 即得。
这给出完整有限的有理清分母证书。实际实现仍优先按 content 约分保存，避免主动制造远大于真实所需的公分母。

## 8. 实施范围与后续真实证书

R777 已部署的基与权六坐标阶段保持原四十坐标，不因本篇重算。后继 R781 算术阶段只读取真正完成的 R777 基和原 R774 系数，执行 (781.5)、(781.10)、(781.15)–(781.19) 的新准确运算。每个 $R_n$ 和完整卷积状态应绑定输入、原字段、相位、前项 SHA，并逐阶保存。

辅助素数可以用来寻找主元或候选，但若 $\kappa$ 在某个约化分量为零，不能把清行后的秩下降冒作特征零现象。最终候选必须在同一准确字段中代回全部 143 条、二十坐标的 (781.19)，再由 R778 认证原函数。

本篇完成了真实切向减半与无代数逆幂的完整构造证明。它尚未给出一个已经执行返回的 $A/B$、$\beta$ 或高度数值；这些继续由公开 Actions 的实际产物决定。

## 依据

- [R772](R772-original-RR-descent-and-exact-function-recovery-certificates.md)：原 $G_{82}$、半线性右作用、字段与 $H^3$ 规范。
- [R774](R774-certified-original-Hodge-cube-and-cusp-order.md)：实际 $e=1$、原 $\kappa_j$ 前缀及 $b$ 的原分母。
- [R778](R778-original-cusp-orbit-and-short-exact-recovery.md)：原二十 cusp 的 Galois 轨道及全部 143 项完整函数证书。
- [R777 方法](../notes/R777-exact-short-K-basis-and-Hodge-coordinates-method.md)：同一原 $K$ 基、准确整数尺度和权六坐标接口。
- D. Zywina, *Explicit open images for elliptic curves over Q*, [原稿](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)，Corollary 4.10：本篇所用的半线性行列式右作用。
