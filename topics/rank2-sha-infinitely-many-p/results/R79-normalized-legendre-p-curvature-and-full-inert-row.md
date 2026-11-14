# R79：标准规范的 Legendre p 曲率与惰性完整行

日期：2026-11-12。状态：矩阵常数、Cartier 原函数及全形式盘结论均已证明。
完整证明见[固定规范的 p 曲率](../notes/2026-11-12-legendre-p-curvature-with-fixed-normalization.md)。

令 $s=1-4t^2$、$A=\begin{pmatrix}0&1\\1/s&8t/s\end{pmatrix}$，
$P_0=I,P_{j+1}=P_j'+P_jA$。取标准 Legendre 多项式
$H=P_{(p-1)/2}(2t)$，规范为 $H(1/2)=1$。

## 1. 不含未定单位的实际矩阵

对所有奇素数，准确有

$$
P_p=s^{1-p}
\begin{pmatrix}HH'&-H^2\\H'^2&-HH'\end{pmatrix}.
$$

它是 $Y^{(p)}=P_pY$ 的矩阵；连接 $\partial_t-A$ 的 p 曲率为其负值。
矩阵秩一、平方为零，像与核均为 $(H,H')$ 张成的线。
证明结合递推的次数界、水平性及 cusp $t=1/2$ 的准确留数，规范常数恰为一。

特别

$$
\operatorname{Cartier}\!\left(\frac{dt}{sH^2}\right)=\frac{dt}s.
$$

存在唯一规范有理函数 $R_p$ 满足

$$
R_p'=\frac1{sH^2}-\frac{t^{p-1}}{s^p},
$$

其 Hasse 零点处至多简单极、两 cusp 处极阶至多 $p-1$，且无穷远取零。
惰性时它为奇函数，在零点有 $R_p=-h^{-2}t^{-1}+O(t)$，$h=H'(0)$。

## 2. 实际惰性 Frobenius 的整个模 p 形式盘

R68 的实际中心常数满足 $b/a\equiv-h^2\pmod p$。
底行水平性先给 $V=(H/h)v(t^p)$、$v(0)=1$；
把准确 Wronskian 与上述 Cartier 恒等式结合，唯一确定 $v=s^{-1}$。
因此

$$
\boxed{\quad V\equiv\frac{H}{h s^p}\pmod p\quad}
$$

在整个 $\mathbb F_p[[t]]$ 成立，不是只在低阶截断成立。
同时

$$
\zeta=\frac UV=-h^2s^pR_p+c(t)^p,
\qquad c\in t\mathbb F_p[[t]]\text{ 为奇函数}.
$$

令 $Z_p=-h^2s^pR_p$、$c_1=[t]c$，则 R78 的实际投影为

$$
\mathcal P_p(f)\equiv
\frac12[t^{p-1}]f'Z_p^2+(c_1+h^2)f_1\pmod p.
$$

对实际 $f=M_eV$，$f$ 始于五次，故这一 $c_1$ 项消失；
它不是新的中央非零判据。目标 $C_{p+1}/p$ 仍需保留模 $p^2$ 信息。

**剩余任务：** 把完整的模平方 Kummer/GM 比较与实际全局单位关系连接，
不能从非零 p 曲率或非零 Hasse 多项式推目标中央导数非零。
