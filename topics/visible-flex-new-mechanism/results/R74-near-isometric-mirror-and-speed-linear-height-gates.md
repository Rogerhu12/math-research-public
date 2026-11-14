# R74：近等距误差下的镜像法弦与中心速度线性高度门

状态：**已证明**。本结果给当前固定切向场高度空间的额外必要线性约束；它不提供完整 reach、嵌入或等距连接的存在性。当前实际初态的误差仍大于 1，不能把下面小误差假设当成已通过。

## 1. 约定

在一个正则环带上取目标度量

$$
g=ds^2+a(s)^2d\theta^2,\qquad a>0,
$$

并使用 R57/R60 的准确连续重构

$$
X(s,\theta)=a(s)\Pi T(s,\theta)+z(s)e_z,
\qquad |T|=1,\quad \langle T\rangle_\theta=0.
$$

$\Pi$ 是零角均值的周期原函数，因此 $X_\theta=aT$。记

$$
U=X_s,\quad b=z_s,\quad E=|U|^2,\quad q=U\cdot T,
\qquad W=U\times T.
$$

这里 $W_z$ 是**未归一化**法向的第三分量，不是单位法向分量。以目标正交基 $\partial_s,a^{-1}\partial_\theta$ 表示，诱导度量与误差分别为

$$
G_X=\begin{pmatrix}E&q\\q&1\end{pmatrix},\qquad
S=G_X-I=\begin{pmatrix}E-1&q\\q&0\end{pmatrix}.
$$

假设在所论的整个环带上

$$
\|S\|_{\rm op}\le\varepsilon<1.
\tag{1}
$$

这就是 R57 的最大相对算子度量误差条件；有限采样的观测不自动给全域 (1)。

## 2. 法向模长的较强双边界

由 $S_{22}=0$ 和极值原理，$S$ 的两个特征值满足

$$
-\varepsilon\le\lambda_-\le0\le\lambda_+\le\varepsilon.
$$

因此

$$
1-\varepsilon
\le(1+\lambda_-)(1+\lambda_+)
=\det G_X=E-q^2=|W|^2
\le1+\varepsilon.
\tag{2}
$$

两个极值分别由矩形区间上的单调性取得：下端取 $\lambda_-=-\varepsilon,\lambda_+=0$，上端取 $\lambda_-=0,\lambda_+=\varepsilon$。故

$$
\sqrt{1-\varepsilon}\le|W|\le\sqrt{1+\varepsilon}.
\tag{3}
$$

这里使用了角向度量恰为 1 的结构；没有套用一般二维扰动中较弱的 $(1\pm\varepsilon)^2$ 行列式界。特别，(1) 已保证这个 chart 是浸入。

## 3. 镜像点对给出的线性高度下界

假设完整曲面包含上侧点 $p=X(s,\theta)$ 及其平面镜像 $\bar p=(X_x,X_y,-X_z)$，两者来自不同材料点，且所选侧号 $\sigma=\pm1$ 满足 $\sigma X_z>0$。完整曲面若是 $C^2$ 嵌入并有 reach 至少为 $\tau>0$，R30/R66 所用的法弦必要不等式给

$$
\frac{|p-\bar p|^2}{2|(p-\bar p)\cdot n(p)|}\ge\tau,
\qquad n(p)=\frac{W}{|W|}.
$$

当 $W_z\ne0$ 时，这个比值准确为

$$
\rho_{\rm mirror}(s,\theta)
=\frac{|X_z|\,|W|}{|W_z|}.
\tag{4}
$$

镜像侧的法向给相同数值。结合 (3)，得到以下**必要**条件：

$$
\boxed{\quad
\sigma X_z(s,\theta)
\ge \frac{\tau |W_z(s,\theta)|}{\sqrt{1+\varepsilon}}.
\quad}
\tag{5}
$$

若 $W_z=0$，该点对法弦分母为零，(5) 退化为已选侧的非负高度条件，不能据此断言没有其它点对阻断。若两个不同材料点恰有 $X_z=0$，它们同像，嵌入本身已失败；(5) 不能代替这个区分。

反过来，在 (1) 成立且这对点确实不同的前提下，较强的线性下界

$$
\sigma X_z(s,\theta)
\ge \frac{\tau |W_z(s,\theta)|}{\sqrt{1-\varepsilon}}
\tag{6}
$$

足以使**这些镜像同参数点对**的 (4) 不小于 $\tau$。当 $\varepsilon=0$ 时，(5) 与 (6) 相同，且准确等价于这些点对的法弦条件。任一版本都没有涵盖其它材料点对、近对角曲率或别的接缝，因此绝不是完整 reach 的充分证书。

## 4. 在固定切向场空间内确为线性行

固定完整 $T,a$ 和不可变 $b_0$，令高度参数为 $c_j$：

$$
b=b_0+\sum_jc_jC_j(s),\qquad
z=z_{\rm base}+\sum_jc_j I_j(s),\qquad I_j'=C_j.
$$

因为

$$
U=U_*+be_z,\qquad
U_*=a'\Pi T+a\Pi T_s,
$$

有

$$
W_z=(U_*\times T)_z+(be_z\times T)_z
=(U_*\times T)_z.
\tag{7}
$$

所以 $W_z$ 完全不随高度系数变化。将 (7) 代入 (5)，每个材料点给高度系数的一条真实线性不等式。

具体在有限采样 $s_i,\theta_k$ 上，按当前高度多面体的记号写

$$
\sigma X_z(s_i,\theta_k;c)=\zeta_{ik}+(Ac)_i,
\qquad A_{ij}=\sigma I_j(s_i).
$$

一行所有角点的必要约束准确压缩为

$$
(Ac)_i\ge
\max_k\left\{
\frac{\tau |W_z(s_i,\theta_k)|}{\sqrt{1+\varepsilon}}
-\zeta_{ik}\right\}.
\tag{8}
$$

原球上/下界、共同帽高行与系数盒继续保留，交集仍为凸多面体。其浮点实现或有限样本可行性本身不构成全域认证。若以后改变 $u,v$，$T,U_*$ 及右侧都要重算，不能复用原固定切向场的行。

## 5. 中心速度也有必要线性行

零角均值给 $\langle U_*\rangle_\theta=0$，所以

$$
\langle U\rangle_\theta=be_z.
$$

由 (1) 的 $E\le1+\varepsilon$ 与三角不等式，

$$
|b|=|\langle U\rangle_\theta|
\le\langle|U|\rangle_\theta\le\sqrt{1+\varepsilon}.
$$

故每个 $s$ 另有两条必要线性行

$$
-\sqrt{1+\varepsilon}-b_0(s)
\le\sum_jc_jC_j(s)
\le\sqrt{1+\varepsilon}-b_0(s).
\tag{9}
$$

精确等距时为 $|b|\le1$。与单纯约束 $|c_j|\le1$ 不同，(9) 直接约束真实中心速度。

还可沿用 R59 的更强固定切向场必要上界：若 $S_*(s)=\langle|U_*|^2\rangle_\theta$，则

$$
S_*+b^2=\langle E\rangle_\theta\le1+\varepsilon.
\tag{10}
$$

若 $S_*>1+\varepsilon$，该固定切向场不能仅靠高度满足 (1)。否则 (9) 的上界可缩成 $\sqrt{1+\varepsilon-S_*}$。这仍不是全角度量充分条件，尤其没有消去 $q$。

## 6. 当前任务中的范围

选 $\varepsilon=10^{-6}$ 可以把本题目标误差作为明确的条件设计门；(5)/(9) 是“未来同时满足该误差和所选 reach 的当前固定切向场必须满足什么”，不是声称当前误差约 1.34 的初态已经接近等距。

当前已部署的九高度 LP/QP 保持其原先 $z\ge0$ 与球/帽高筛，不因本证明暗改同一次目标。若实际输出只达到近零高度接触或速度超界，可以另立新约束身份加入 (8)/(9)，记录是否有共同可行点；若固定 $T$ 的 (10) 失败，则必须调整切向场，而不是无止境抬高。所有这些都仍要接完整非线性度量、全曲面及全时验证。

来源：[R57 直接度量与重构](R57-direct-reconstructed-metric-and-auxiliary-frame-space.md)、[R59 中心速度必要门](R59-scalar-center-speed-elimination-and-metric-lower-bounds.md)、[R60 独立中心速度](R60-independent-center-speed-fixed-ports-and-position-two-jets.md)、[R66 法弦高度必要门](R66-core-flat-cap-two-normal-reach-height-gate.md)。
