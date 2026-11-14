# R150 附录：高次旋转增生多项式、全部首一非线性剪切与真实核正则化

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。根代理与 kernel_resume_1cf 已独立逐项核查收缩半群矩插值、真实因式右逆、全部高次自然域及 Bell 权。

状态：完整证明。把[固定复直线二次稿](R150-appendix-fixed-complex-line-skeleton-rough-strips-and-all-bounded-companion-parts.md)的全部有界部分排除扩至任意有限次数，再关闭旧非线性剪切的所有最高边碰撞。主行、独立固定复直线骨架及全部复误差均保留。

## 1. 原函数与完整结论

取
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,\qquad
\psi\in\mathbb R.
$$
取 $d^0,d^1$ 满足
$$
d^\nu_j=0\quad(a_j=0),\qquad
\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty,
$$
并取任意复 $e^0,e^1\in\ell^1$、$u_*,v_*,\gamma$。
保持原函数
$$
u=u_*+\sum_j(a_j+d_j^0+e_j^0)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d_j^1+e_j^1)\chi_j.
\tag{1.1}
$$

令 $\Psi\in\mathbb C[x]$ 的次数为 $k\ge2$。
令 $G(x,s)$ 关于 $s$ 首一，$\deg_sG=m\ge1$，
并对每个非零单项式 $x^is^j$ 要求
$$
\boxed{i+(k-1)j\le m(k-1).}
\tag{1.2}
$$
则对每个 $\lambda\in\mathbb C$、整数 $r\ge1$、
任意复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{
[G(u,v-\Psi(u))-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.3}
$$

没有最高边与其平移互素的假设。
旧[非线性剪切稿](R150-appendix-nonlinear-scalar-shears-degenerate-newton-edges-and-point-powers.md)
已经处理该互素条件成立的更一般辅助行；
本文新增的是 (1.1) 范围内全部真实碰撞。
$k=2$ 退回固定复直线二次稿。

## 2. 收缩半群的真实自然幂矩插值

以下先在任意 Hilbert 空间上工作。
设 $X$ 最大增生，$S(t)=e^{-tX}$ 为收缩半群。
固定整数 $k\ge2$。

对 $u\in\operatorname{Dom}X^k$、$h>0$ 及
$\ell=0,\ldots,k-1$，实际半群轨道的 Taylor 积分式给
$$
S(\ell h)u
=\sum_{j=0}^{k-1}\frac{(-\ell h)^j}{j!}X^ju+R_\ell,
\qquad
\|R_\ell\|\le\frac{(\ell h)^k}{k!}\|X^ku\|.
\tag{2.1}
$$
它来自 $S(t)u$ 的前 $k$ 阶强导数；
最后导数为 $(-1)^kS(t)X^ku$，范数由收缩性控制。

反演固定有限 Vandermonde 矩阵，得到常数 $C_k$，使
$$
h^j\|X^ju\|
\le C_k\bigl(\|u\|+h^k\|X^ku\|\bigr)
\quad(1\le j<k).
\tag{2.2}
$$
优化 $h=(\|u\|/\|X^ku\|)^{1/k}$，得到
$$
\boxed{
\|X^ju\|
\le C'_k\|u\|^{1-j/k}\|X^ku\|^{j/k}.
}
\tag{2.3}
$$
若最高作用为零，直接在 (2.2) 令 $h\to\infty$；
若 $u=0$ 则显然。
这些退化情况也已包括。

(2.3) 同时证明每个自然 $X^k$ 闭：
若 $u_n\to u$、$X^ku_n\to v$，则各中间 $X^ju_n$ 都 Cauchy；
逐层用 $X$ 闭性识别全部极限。
其定义域稠密可由一个实际预解的 $k$ 次幂像得到。

若 $J$ 有界并与 $X$ 全部预解交换，
则它保持所有这些自然幂域。
对任意 $c\ge0$、$|\alpha|=1$，
最高单位多项式
$$
Q_\pm=cX\pm\alpha(X^k+JX^{k-1}),
\qquad \operatorname{Dom}Q_\pm=\operatorname{Dom}X^k
$$
满足固定图预算
$$
\boxed{
\|X^ku\|\le C\bigl(\|Q_\pm u\|+\|u\|\bigr).
}
\tag{2.4}
$$
确实，(2.3) 和 Young 不等式把
$\|J\|\|X^{k-1}u\|+c\|Xu\|$
以任意小的 $X^k$ 相对界吸收。
本节常数可依 $k,c,\|J\|$，不依后面的预解参数 $z$。

## 3. 任意高次的旋转增生排除引理

假设 $X$ 在一个非零空间上最大增生、空谱，
其真实预解满足：

- 每个固定实 $B$ 有固定预算
  $$
  M(B)=\sup_{\operatorname{Re}z\le B}\|(X-z)^{-1}\|<\infty;
  \tag{3.1}
  $$
- 对任意 $k'>0$，存在 $\tau_n\to\infty$、
  $r_n=k'\log\tau_n$，使
  $$
  \sup_{\operatorname{Re}z\le r_n}\|(X-z)^{-1}\|
  \le2e^{r_n\tau_n}/r_n.
  \tag{3.2}
  $$

令 $J$ 为任意有界预解交换子，$|\alpha|=1$、$c\ge0$。
若两个准确自然多项式
$$
Q_\pm=cX\pm\alpha(X^k+JX^{k-1}),
\qquad \operatorname{Dom}Q_\pm=\operatorname{Dom}X^k
\tag{3.3}
$$
都最大增生，则矛盾。

### 3.1 一个实际右逆因式，不要求另一因子可逆

置 $R=|z|$、$q_\pm(z)=cz\pm\alpha z^k$，并定义
$$
F_\pm(z)=Q_\pm-q_\pm(z)I\mp\alpha Jz^{k-1}.
$$
在 $\operatorname{Dom}X^k$ 上，准确有
$$
\boxed{F_\pm(z)=(X-z)H_\pm(X,z),}
\tag{3.4}
$$
其中
$$
H_\pm(X,z)
=cI\pm\alpha\sum_{\ell=0}^{k-1}z^\ell X^{k-1-\ell}
\pm\alpha J\sum_{\ell=0}^{k-2}z^\ell X^{k-2-\ell}.
\tag{3.5}
$$
最高次数只有 $k-1$。

固定 $d>\|J\|$。
若
$$
-\operatorname{Re}q_\pm(z)\ge d(R+1)^{k-1},
\tag{3.6}
$$
最大增生预解和有界扰动给
$$
\boxed{
\|F_\pm(z)^{-1}\|
\le\frac1{(d-\|J\|)(R+1)^{k-1}}.
}
\tag{3.7}
$$
对 $g\in H$，令 $u=F_\pm(z)^{-1}g$；
它确实属于 $\operatorname{Dom}X^k$。
由其方程及 (2.4)，
$$
\|u\|\le C(R+1)^{-k+1}\|g\|,\qquad
\|X^ku\|\le C(R+1)\|g\|.
\tag{3.8}
$$
后一式中
$|q_\pm(z)|+\|J\|R^{k-1}=O((R+1)^k)$，
乘上前一界只剩 $O(R+1)$。

将 (3.8) 代入 (2.3)，对所有 $0\le j\le k$ 得
$$
\boxed{
\|X^jF_\pm(z)^{-1}\|
\le C(R+1)^{j-k+1}.
}
\tag{3.9}
$$
因此 (3.5) 的第一组每一项
$z^\ell X^{k-1-\ell}F_\pm^{-1}$
一致有界；第二组还多一个 $(R+1)^{-1}$。
从而
$$
\|H_\pm(X,z)F_\pm(z)^{-1}\|\le C.
\tag{3.10}
$$

还必须识别这个乘积的实际值：
$F_\pm^{-1}H\subseteq\operatorname{Dom}X^k$，
故 (3.5) 使
$H_\pm(X,z)F_\pm^{-1}H\subseteq\operatorname{Dom}X$。
(3.4) 于是给
$$
(X-z)H_\pm(X,z)F_\pm^{-1}=I.
$$
$X-z$ 已有真实唯一逆，所以
$$
\boxed{
(X-z)^{-1}=H_\pm(X,z)F_\pm(z)^{-1}.
}
\tag{3.11}
$$
这不要求 $H_\pm(X,z)$ 自身有界或有逆。
(3.10) 证明预解在 (3.6) 的全部区域统一有界。

### 3.2 有限宽射线带

取任意固定左半面界，例如 $\operatorname{Re}z\le1$，
由 (3.1) 控制。
其余未控制的大点只能满足
$$
\operatorname{Re}z\ge1,\qquad
|\operatorname{Re}(\alpha z^k)|
\le c\operatorname{Re}z+d(R+1)^{k-1}.
\tag{3.12}
$$
写 $\alpha=e^{-i\psi}$。
主部的 $2k$ 条零射线为
$$
\theta_\ell=\frac{\psi+\pi/2+\ell\pi}{k},
\qquad \ell=0,\ldots,2k-1.
\tag{3.13}
$$
(3.12) 先给
$|\cos(k\arg z-\psi)|=O(R^{-1})$，
故未控制大点距这些射线有统一有界距离。

在任一射线附近写
$$
z=e^{i\theta}(t+is),\qquad t\ge0,\quad s=O(1).
$$
因为 $\alpha e^{ik\theta}=\pm i$，当 $t\to\infty$，
$$
|\operatorname{Re}(\alpha z^k)|
=k t^{k-1}|s|+O(t^{k-3})
$$
（$k=2$ 时该式准确且余项为零）。
除以 $k t^{k-1}$，得到：

- $k=2$ 时，未控制带半宽至多
  $$
  (c\cos\theta+d)/2+o(1);
  $$
- $k\ge3$ 时，半宽至多
  $$
  d/k+o(1).
  $$

取每条带的固定半宽 $h_\theta$ 严格大于对应界。
两条长边由 (3.6)、(3.10) 控制；短边紧致。
向左射线的远部落入固定左半面；
竖直带的实部有固定上界，也由固定 $M(B)$ 控制。

### 3.3 好时间障碍与 Liouville

只需处理有限条 $\cos\theta>0$ 的右向半条带。
选同一个足够大的 $k'$，使每条带都可取
$$
\frac{\cos\theta}{k'}<\beta_\theta<\frac{\pi}{2h_\theta}.
$$
令
$$
L_n=\frac{r_n-h_\theta|\sin\theta|-1}{\cos\theta}.
$$
在远端 $t=L_n$，实际 $\operatorname{Re}z\le r_n$，
故 (3.2) 控制对数预解为 $O(\tau_n\log\tau_n)$。

对任一单位向量矩阵元，乘上
$\exp[-\varepsilon\cosh(\beta_\theta(w-t_0))]$。
其远端实部障碍按
$\tau_n^{\beta_\theta k'/\cos\theta}$ 增长，
指数严格大于1。
与固定复直线稿完全相同的有限矩形最大模证明，
先沿远端趋远，再令 $\varepsilon\downarrow0$，
给全部这些半条带统一界。
竖直及左向部分的界已经单独支付。

所以整预解全平面有界。
负实轴上的最大增生界使其趋零，Liouville 迫预解恒零，
与非零空间上的真实逆矛盾。
高次引理证毕；从未要求 $J$ 有限谱。

## 4. 真实高次相伴算子没有任何有界部分

使用 (1.1) 的参考 first：
$$
X_0=X_a,\qquad
Z=X_{a+d^0}+\omega I,\qquad
L=Z^{-1},\qquad Y=e^{i\psi}X_b,
\tag{4.1}
$$
其中 $\omega$ 取[复加权主行稿](R150-appendix-weighted-complex-main-real-controlled-skeleton-and-all-shear-powers.md)
§3 已付的一个共享平移。
$Z$ 空谱且最大增生，$L\in A'$ 拟幂零，
而
$$
cZ\pm e^{-i\psi}Y
$$
对每个充分大实 $c$ 为原完整最大增生 first。

对每个 $k\ge2$，定义
$$
W_k=(Y-Z^k)_{\rm can},\qquad
\mathscr T_k=W_kL^{k-1},
$$
$$
\operatorname{Dom}\mathscr T_k
=\{h:L^{k-1}h\in\operatorname{Dom}W_k\}.
\tag{4.2}
$$
$W_k$ 是 R186 的规范闭多项式，
故 $\mathscr T_k$ 闭，图被全部有界 $A'$ 保持。
在实际共同深域上，
$$
\mathscr T_k=YL^{k-1}-Z.
\tag{4.3}
$$

**定理4.1。** 在任意有限对角放大中，
不存在非零闭、对所有对角 $A'$ 不变的 $\mathcal M$，
使 $\mathcal M\subseteq\operatorname{Dom}\mathscr T_k$，
且 $\mathscr T_k\mathcal M\subseteq\mathcal M$、
$J=\mathscr T_k|_\mathcal M$ 有界。

### 4.1 无限计数支：完整自然 $k$ 次域

若 $\Lambda_a=\infty$，原主锚的真实半群与 Laplace
给 §3 的 (3.1)—(3.2) 全部预算。
这些界限制到 $\mathcal M$ 后保持；
预解/Yosida 逼近使 $Z_\mathcal M$ 最大增生、空谱，
并使各 $(cZ\pm e^{-i\psi}Y)_\mathcal M$ 最大增生。
$J$ 与共同正则器和 $L_\mathcal M$ 交换。

在足够深的共同域中，把 (4.3) 作用于
$Z_\mathcal M^{k-1}f$，得到
$$
Yf=Z_\mathcal M^kf+JZ_\mathcal M^{k-1}f.
\tag{4.4}
$$
给任意 $f\in\operatorname{Dom}Z_\mathcal M^k$，
用同一 R186 正则器在 $Z_\mathcal M^k$ 图中逼近。
$Yf_\varepsilon$ 的右侧收敛，
而 $(cZ\pm e^{-i\psi}Y)f_\varepsilon$ 也收敛。
分别用原 $Y$ 和原两个完整 first 的闭性，
便得到 (4.4) 与实际包含
$$
Q_\pm=cZ_\mathcal M
\pm e^{-i\psi}(Z_\mathcal M^k+JZ_\mathcal M^{k-1})
\subseteq(cZ\pm e^{-i\psi}Y)_\mathcal M
$$
在准确域 $\operatorname{Dom}Z_\mathcal M^k$ 上成立。

对每个复 $\lambda$，
$$
(Q_\pm-\lambda)L_\mathcal M^k
=\pm e^{-i\psi}I
\pm e^{-i\psi}JL_\mathcal M
+cL_\mathcal M^{k-1}-\lambda L_\mathcal M^k.
\tag{4.5}
$$
右侧为非零标量单位加拟幂零项，因而是有界单位。
这里 $L_\mathcal M$ 拟幂零且与有界 $J$ 交换。
其逆乘 $L_\mathcal M^k$ 给 $Q_\pm-\lambda$ 的真实有界逆；
自然多项式也因此闭，准确域没有增加。

取负实 $\lambda$；
左边限制算子满射、右边最大增生部分单射，
所以两者的完整域和算子相等。
现在 §3 的高次引理全部假设成立，排除非零 $\mathcal M$。

### 4.2 有限计数支：同一真实复中心全柱

若 $\Lambda_a<\infty$，
复加权主行稿 §§6—7 给有限集 $F_n$、
$d_n=|F_n|$、真实复中心
$$
\sigma_n=\omega+\sum_{j\in F_n}(a_j+d_j^0),\qquad
|\sigma_n|\to\infty,
$$
以及
$$
g_n=\|(a+d^0)\mathbf1_{F_n^c}\|_2+
\|b\mathbf1_{F_n^c}\|_2,\qquad
\sqrt{d_n}\,g_n/|\sigma_n|\to0.
\tag{4.6}
$$
$Q_{F_n}\to I$ 强，全部真实头绝对系数除以 $|\sigma_n|$ 一致有界。

高次算子的实际深伴随表达式只变为
$$
\mathscr D_k^\dagger=(L^*)^{k-1}Y^*-Z^*.
$$
原归一三项展开仍是：

1. 一致有界标量乘 $(L^*)^{k-1}$，为一致拟幂零族；
2. 真实有限头，其有界交换系数总范数一致；
3. 两个真实混合尾，其全柱 $q$ 次自然幂根
   不超过 $C_k g_n\sqrt q/|\sigma_n|$。

理由逐项与前稿相同：
$k$ 固定，$(L^*)^{k-1}$ 有界、与全部真实伴随词交换；
R251 任意物理头的进位估计及混合尾 Cauchy 极化都不改变。
头系数准确为
$$
\frac{-\overline{(a_j+d_j^0)}I+
e^{-i\psi}b_j(L^*)^{k-1}}{\overline{\sigma_n}}.
$$
有限常数 $C_k$ 可依 $\|L\|^{k-1}$，不影响 (4.6)。

因此有同一列 $p_n/d_n\to\infty$，使
$$
\left\|
\left(\frac{\mathscr D_k^\dagger+\overline{\sigma_n}}
{\overline{\sigma_n}}\right)^{p_n}Q_{F_n}
\right\|^{1/p_n}\to0.
\tag{4.7}
$$
所有迭代输入的真实伴随词域由同一 R251 补集尺度支付。

令 $\Pi$ 为到 $\mathcal M$ 的投影。
在实际共同正则核心上作原 Hilbert 双配对并取极限，得到
$$
\Pi(\mathscr D_k^\dagger+\overline{\sigma_n})^{p_n}Q_{F_n}
=(J^*+\overline{\sigma_n})^{p_n}\Pi Q_{F_n}.
$$
由于
$\|(I+J^*/\overline{\sigma_n})^{-1}\|\to1$，
(4.7) 迫 $\|\Pi Q_{F_n}\|\to0$。
强收敛 $Q_{F_n}\to I$ 给 $\Pi=0$，矛盾。
这里也完全不需要 $J$ 有限谱。
定理4.1得证。

## 5. 任意有界交换系数的自然首一多项式无核

对 $d\ge1$、任意 $B_j\in A'$，在自然域上令
$$
Q(\mathscr T_k)
=\mathscr T_k^d+\sum_{j<d}B_j\mathscr T_k^j,\qquad
\operatorname{Dom}Q=\operatorname{Dom}\mathscr T_k^d.
$$
则
$$
\boxed{\ker Q(\mathscr T_k)=\{0\}.}
\tag{5.1}
$$

完整理由为相伴核图
$$
\Gamma=\{(h,\mathscr T_kh,\ldots,\mathscr T_k^{d-1}h):
h\in\operatorname{Dom}\mathscr T_k^d,\ Q(\mathscr T_k)h=0\}.
$$
若坐标收敛，前 $d-1$ 层由 $\mathscr T_k$ 闭性识别，
最高一层由
$\mathscr T_k^dh=-\sum_{j<d}B_j\mathscr T_k^jh$
和最后一次闭性识别，故 $\Gamma$ 闭。
它被全部对角 $A'$ 保持。

同一等式的右侧还属于 $\operatorname{Dom}\mathscr T_k$，
因为每个 $B_j$ 保域，且 $j<d$。
故原 $h$ 自动进入下一次自然域；
交换性给 $Q(\mathscr T_k)\mathscr T_kh=0$。
所以对角 $\mathscr T_k$ 保持 $\Gamma$，
其作用由有界相伴矩阵给出。
非零核于是违反定理4.1，证明 (5.1)。

这里没有声称整个自然 $Q$ 图闭，
也没有把其域当成一个任意规范闭扩张的域。

## 6. 原完整 Bell 的准确权与有界归一系数

先可将 $\Psi$ 最高系数化为1。
若其最高系数为 $\kappa\ne0$，
取
$$
v'=\kappa^{-1}v,\qquad
\Psi'=\kappa^{-1}\Psi,\qquad
G'(x,s)=\kappa^{-m}G(x,\kappa s),\qquad
\lambda'=\kappa^{-m}\lambda.
$$
$v'$ 仍属于 (1.1)，只改变固定直线的角度、幅度和误差。
原目标向量变为 $G',v',\Psi',\lambda'$ 目标的非零标量
$\kappa^{mr}$ 倍。
以下因此设 $\Psi$ 首一。

固定 $\lambda,r,w$，先对原完整
$$
F(x,y)^r=[G(x,y-\Psi(x))-\lambda]^r
$$
构造其全部混合 Bell 多项式
$\mathcal P_{\lambda,r,w}$。
不删除原 cumulant 或复倾斜。
令 $d=mr$、$D=(k-1)d$。

在 $(x,s=y-\Psi(x))$ 坐标中赋权
$\operatorname{wt}x=1$、$\operatorname{wt}s=k-1$。
原式权至多 $D$，且关于 $s$ 首一、次数 $d$。
Bell 所用两个实际微分对应
$$
\partial_y=\partial_s,\qquad
\left.\partial_x\right|_y
=\left.\partial_x\right|_s-\Psi'(x)\partial_s.
\tag{6.1}
$$
$\partial_s$ 降权 $k-1$；
$\partial_x|_s$ 降权1；
$\Psi'(x)\partial_s$ 不增权，因为 $\deg\Psi'=k-1$。
所以所有混合 Bell 项仍有权至多 $D$。
任意非零导数项都不产生 $s^d$ 系数，故首一性保留。

原倾斜 first 的实际代换为
$$
x_{\rm old}=Z+H,\qquad
y_{\rm old}=Y+RZ+K,
\qquad H,K\in\mathcal A,\ R\in A'
$$
且这些有界系数彼此交换。
这是复加权主行稿 §2、§5 已付的真实域等式。
令 $s_0=Y-Z^k$。
则
$$
s_{\rm old}
=s_0+\bigl[Z^k+RZ+K-\Psi(Z+H)\bigr].
\tag{6.2}
$$
方括号是 $Z$ 的次数至多 $k-1$ 的有界交换系数多项式，
所以再次保持权和关于 $s_0$ 的首一性。

因此在真实共同深域上，原 Bell 算子具有有限表达式
$$
P(Z,Y)
=s_0^d+
\sum_{\substack{j<d\\i+(k-1)j\le D}}
E_{ij}Z^is_0^j,
\qquad E_{ij}\in A'.
\tag{6.3}
$$
原所有系数均已包括；它仍是最初原 Bell 实现的核心表达式。

将 (6.3) 乘有界 $L^D$，并用
$\mathscr T_k=s_0L^{k-1}$ 的深域恒等式，得到实际首一多项式
$$
\boxed{
Q(\mathscr T_k)
=\mathscr T_k^d+
\sum_{j<d}B_j\mathscr T_k^j,\qquad
B_j=\sum_iE_{ij}L^{D-i-(k-1)j}\in A'.
}
\tag{6.4}
$$
全部 $L$ 次数非负正是 (1.2) 的用途。
这里没有形式负幂，也不要求这些 $B_j$ 的有限谱信息。

## 7. 用同一个真实正则器处理规范最大核

最后须把 §5 的自然域结论准确传回原规范 Bell 图。

假设
$$
0\ne f\in\ker\mathcal P_{\lambda,r,w}.
$$
取 R186 对本文全部有限 first 族的同一个
单射有界共同正则器 $\mathcal R\in A'$。
取有限 $N\ge kd+2$，并在原有限族的正则器定义若要求更大固定词深度时相应增大，使
$$
h=\mathcal R^Nf
$$
属于 (6.1)—(6.4) 的全部实际中间混合词域，
并至少属于展开 $\mathscr T_k^j$、$j\le d$ 所需的长度 $kd$ 词域。
如将原 $Z$ 展开为两个 first 加常数，需要相应增加一个固定有限深度；
R186 同一有限族规则支付它。

原规范图与 $\mathcal R$ 交换，所以
$$
\mathcal P_{\lambda,r,w}h=0.
$$
而 $\mathcal R$ 单射保证 $h\ne0$。

对这样的 $h$，每个有界 $L$ 保持全部已付词域。
由规范 $W_k$ 在共同自然核心上的真实作用，逐次归纳得
$$
\mathscr T_k^jh
=(Y-Z^k)^jL^{(k-1)j}h
\quad(0\le j\le d).
\tag{7.1}
$$
每次下一作用的输入域都由同一长度 $kd$ 的真实词预算覆盖。
所以 $h\in\operatorname{Dom}\mathscr T_k^d$，
(6.4) 在这个指定输入上准确给
$$
Q(\mathscr T_k)h
=L^D\mathcal P_{\lambda,r,w}h=0.
$$
这与 (5.1)、$h\ne0$ 矛盾。

因此原规范最大核为零。
完整原 $C$ 自伴性给像稠密，
而 R186 的循环指数图核心给
$$
[\mathcal P_{\lambda,r,w}e^w]_A
=\overline{\operatorname{Ran}\mathcal P_{\lambda,r,w}}=H.
$$
其作用正是未改动的原普通点态向量 (1.3)，证明完成。

本节没有断言
$\operatorname{Dom}\mathcal P_{\lambda,r,w}
=\operatorname{Dom}\mathscr T_k^d$。
使用的是同一真实单射正则器将一个假想核向量送入已付自然域；
这是比直接混同两图更弱且足够的准确步骤。

## 8. 例子与仍未覆盖的范围

取任意 $1/2<\sigma\le1$，
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=i\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j.
$$
例如 $k=3$、$\Psi(x)=x^3$、$G(x,s)=s^2-\beta x^4$，
对全部 $\beta,\lambda\in\mathbb C$、$r\ge1$、复权 $w$，
$$
\boxed{[(v-u^3)^2-\beta u^4-\lambda]^r e^w\text{ 循环。}}
$$
旧最高边平移在 $\beta=9$ 时有真实根碰撞；
本稿包括该值，不用把两个已循环点态因子的乘积直接当作循环。

一般次数 $k$ 与所有 (1.2) 型余项也完全同样。
原主、副行的 weighted 与 $\ell^1$ 误差、全部复常数照 §1 保留。

一般复同阶骨架若模去
$\mathbb C a+\ell^1+\ell^2(a^{-1})$
后不落在固定复直线，仍缺所需两个最大增生 first。
超过 (1.2) 的剪切余项会出现负的归一 $L$ 次数，
不能直接沿用 §6。
指定真正常见证的聚合上界、一般慢主理想和普通 Hilbert ISP 仍未完成。
