# R249附录：移动有限头真实能量通量与缺陷次数尾率

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d。状态：已证明，中间结论。

本文处理负整数边界的两个实际慢算子 $T=T_N,T_Y$，记 $M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$。这里的 $W$ 不是幂权积 $W_n$。全文保留真实 carry，不把逐层 Hilbert 的形式原像当作全空间向量。

组合 [R247](R247-shifted-degree-energy-flux-and-square-root-criterion.md) 的移位通量、[R239指数附录](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) 的层界和 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的平衡有限头相似，得到以下结论。令 $\mathsf P_{>q}$ 为原物理孔次数尾投影，$c_*=2+2\log(3/2)$。对每个非零 $w\in W$，$\tau_q=\|\mathsf P_{>q}w\|$ 满足
$$
\boxed{\liminf_{q\to\infty}\frac{-\log\tau_q}{q}\le\frac{c_*}{26},
\qquad
\limsup_{q\to\infty}\frac{-\log\tau_q}{q}\le\frac{8c_*}{13}.}
\tag{0.1}
$$
两个上界分别约为 $0.10811$、$1.72980$。这是非零缺陷的必要慢尾条件，不是上方尾衰减估计，也不决定 $W=0$。

## 1. 实际分解与规范形式原像

固定 $m\ge3$、$d=2^m$。在 $\mathcal F_m\otimes\mathcal H_{\ge m}$ 中，
$$
T^{[m]}=T_m\otimes I+I\otimes D_{\ge m},
\quad D_{\ge m}=\sum_{j\ge m}(j+1)^{-2}E_j,
$$
$$
T=T^{[m]}+\sum_{L\ge m}K_L,\qquad
K_L=T^{[L+1]}-T^{[L]}.
\tag{1.1}
$$
$K_L$ 只作用前 $L+1$ 位。R234的证明在代入粗指数之前已给
$$
\|T-T^{[m]}\|\le26\eta_{m-1},\qquad
\|K_L\|\le52\eta_{L-1}=:\delta_L.
\tag{1.2}
$$
确实，低头差分别由 $\alpha_m/\alpha_i\le\eta_{m-1}$ 和该量的9倍控制，高尾真／纯差分别由 $\eta_i$、$4\eta_i$ 控制；用 $\sum_i(i+1)^{-2}<2$ 得第一式，相邻两截断的三角不等式给第二式。这里没有把粗界反向加强。

准确的本题权给
$$
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j,
$$
$$
-\log\eta_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
\tag{1.3}
$$
固定任意 $c>c_*$。R238/R239给每个 $w\in N^\perp$ 的规范形式原像 $h$，每个完整物理孔层 $h_q\in\mathcal H_q$，且
$$
T^*h=w\quad\text{逐层成立},\qquad
\|h_q\|\le H e^{c(q+1)},\quad H=C_c\|w\|.
\tag{1.4}
$$
固定输出次数上的全部进位项绝对可和。因此这不是仅在有限位坐标上形式相等；下文只使用有限层 Hilbert 截断和另行支付的绝对和。

## 2. 头链分级及两个不同的变换

R249给可逆 $S_m$ 和非零 $\gamma_m$，满足
$$
T_m=S_m(\gamma_mJ_d)S_m^{-1},\quad
\kappa_m=\|S_m\|\,\|S_m^{-1}\|,
$$
$$
\log\kappa_m\le\left(\frac{35}{6}+o(1)\right)d^4.
\tag{2.1}
$$
其中 $J_de_i=e_{i-1}$。把 $S_m$ 张量恒等延拓，仍用同一记号。定义
$$
y=S_m^{-1}w,\quad k=S_m^*h,\quad G=S_m^*S_m,
$$
$$
L_0=\gamma_mJ_d\otimes I+I\otimes D_{\ge m},\quad
E_L=S_m^{-1}K_LS_m,\quad E=\sum_{L\ge m}E_L.
\tag{2.2}
$$
若 $w\in W$，准确有
$$
(L_0+E)y=0,\qquad (L_0^*+E^*)k=Gy.
\tag{2.3}
$$
原像使用 $S_m^*$、核向量使用 $S_m^{-1}$；不能混用。

给头链坐标 $i$ 赋次数 $i$，再加尾孔数，记新链次数投影为 $P_r$。$L_0$ 严格降一次，$L_0^*$ 严格升一次。每个 $P_rk$ 是 Hilbert 向量：固定尾次数 $q$ 只涉及原总孔数 $q,\ldots,q+m$，固定链次数 $r$ 只涉及至多 $d$ 个尾层。由(1.4)，
$$
\boxed{\|P_rk\|\le H\|S_m\|\sqrt{d(m+1)}\,e^{c(r+m+1)}.}
\tag{2.4}
$$
为看清该范数界，先对固定尾次数 $q$ 把原头的不同孔数正交相加，得到范数至多 $\sqrt{m+1}H e^{c(q+m+1)}$；施加 $S_m^*$ 后，再对新链次数中至多 $d$ 个尾层正交相加即可。不要求有限最大位支撑。

$E_L$ 只改变头链位置与其后的 $L-m+1$ 个物理位，所以链次数带宽不超过
$$
b_{m,L}=d+L-m,\qquad \|E_L\|\le\kappa_m\delta_L.
\tag{2.5}
$$
固定输出 $\le n$ 时只需 $k$ 的 $\le n+b_{m,L}$ 层。由(1.3)、(2.4)，这些有限层范数乘 $\delta_L$ 后在 $L$ 上绝对可和，故(2.3)在新分级中仍有完整层意义。

## 3. 实际移位通量

令 $k_{<n}=P_{<n}k$。它是真正 Hilbert 向量，且
$$
\langle(L_0^*+E^*)k_{<n},y\rangle=0,
\qquad P_{\le n}L_0^*k=L_0^*k_{<n}.
$$
第二式来自严格的一次分级。由(2.3)相减得到
$$
\begin{aligned}
\langle P_{\le n}Gy,y\rangle
={}&\sum_{L\ge m}
\langle P_{\le n}E_L^*k_{\ge n},y_{\le n}\rangle\\
&-\sum_{L\ge m}
\langle P_{>n}E_L^*k_{<n},y_{>n}\rangle.
\end{aligned}
\tag{3.1}
$$
第一行的 $E_L^*k_{\ge n}$ 仅表示有限窗 $k_{[n,n+b_{m,L}]}$，不是对整个形式尾直接施算子。上一节保证两行绝对收敛。

令 $I_{n,m,L}=[\max(0,n-b_{m,L}),n+b_{m,L}]$。带宽性质把右边绝对值控制为
$$
2\sum_{L\ge m}\|E_L\|\,
\|k_{I_{n,m,L}}\|\,\|y_{I_{n,m,L}}\|.
$$
再用(2.4)、$\|y\|\le\|S_m^{-1}\|\|w\|$，得到
$$
\begin{aligned}
|\langle P_{\le n}Gy,y\rangle|
\le{}&2H\|w\|\kappa_m^2\sqrt{d(m+1)}
e^{c(n+m+1)}\Theta_m(c),\\
\Theta_m(c):={}&
\sum_{L\ge m}\delta_L\sqrt{2b_{m,L}+1}\,e^{c b_{m,L}}.
\end{aligned}
\tag{3.2}
$$
一个条件数来自变形carry，另一个来自 $k$、$y$ 的相反变换，因此必须支付平方。

## 4. 原正能量与移动尾项

全能量为 $\langle Gy,y\rangle=\|w\|^2$，但 $P_{\le n}$ 一般不与 $G$ 交换，(3.1)左侧未必非负。对 $n\ge d-1$，令
$$
Q=\mathbf1_{\{\text{尾孔数}>n-d+1\}}.
$$
其余尾层已包含全部头链坐标，所以 $(I-P_{\le n})=(I-P_{\le n})Q$。$Q$ 与 $S_m,G,P_{\le n}$ 都交换，于是
$$
\begin{aligned}
|\langle(I-P_{\le n})Gy,y\rangle|
&\le\|GQy\|\,\|Qy\|\\
&=\|S_m^*Qw\|\,\|S_m^{-1}Qw\|\\
&\le\kappa_m\|Qw\|^2
\le\kappa_m\tau_{n-d+1}^2.
\end{aligned}
\tag{4.1}
$$
最后一步使用原物理总孔数至少为尾孔数。故原 Hilbert 范数中有
$$
\boxed{\|w\|^2\le
\kappa_m\tau_{n-d+1}^2+
2H\|w\|\kappa_m^2\sqrt{d(m+1)}
e^{c(n+m+1)}\Theta_m(c).}
\tag{4.2}
$$
这个估计保留了移动斜投影的代价，没有因 $w\in H$ 而免费消去第一项。

## 5. 全部进位的统一渐近率

写 $\lambda_j=-\log\eta_j$，准确计算给
$$
\lambda_{j+1}-16\lambda_j
=5040\,8^j-4200\,2^j>0.
$$
归纳得 $\eta_{m+t-1}\le\eta_{m-1}^{16^t}$。因此
$$
\Theta_m(c)\le
52\eta_{m-1}e^{cd}\sqrt{2d+1}
\sum_{t\ge0}\sqrt{1+2t}\,
e^{ct-(16^t-1)\lambda_{m-1}}.
$$
对固定 $c$，最后的和在充分大 $m$ 上一致有界：取 $\lambda_{m-1}\ge c+2$，用相应固定超几何可和序列支配即可。由(1.3)，
$$
\boxed{\log\Theta_m(c)\le-\frac{175}{2}d^4+o(d^4).}
\tag{5.1}
$$
所有 $o(d^4)$ 对固定 $c$ 使用，不声称端点常数一致。

## 6. 两个尾率及16倍网格

归一化 $\|w\|=1$。置
$$
a=\frac{35}{6},\quad b=\frac{175}{2},\quad b-2a=\frac{455}{6}.
$$
固定 $0<\ell<(b-2a)/c$，令
$$
n_m=\lfloor\ell d^4\rfloor,\qquad q_m=n_m-d+1.
$$
(4.2)第二项由(2.1)、(5.1)至多为
$$
\exp((2a+c\ell-b+o(1))d^4)\longrightarrow0.
$$
所以
$$
\tau_{q_m}^2\ge(1-o(1))\kappa_m^{-1},\qquad
-\log\tau_{q_m}\le\left(\frac a2+o(1)\right)d^4.
\tag{6.1}
$$
这些尾均非零；若某个更早尾为零，则全部较后尾为零，亦矛盾。

因为 $q_m/d^4\to\ell$，先有
$$
\liminf_{q\to\infty}\frac{-\log\tau_q}{q}
\le\frac{a}{2\ell}.
$$
令 $\ell\uparrow(b-2a)/c$，得到
$$
\liminf_{q\to\infty}\frac{-\log\tau_q}{q}
\le\frac{ac}{2(b-2a)}=\frac c{26}.
\tag{6.2}
$$
子列界不能直接充当全序列界。准确地 $q_{m+1}/q_m\to16$。若 $q_m\le q<q_{m+1}$，由 $\tau_q$ 单调，
$$
\tau_q\ge\tau_{q_{m+1}},\qquad
\frac{-\log\tau_q}{q}
\le\frac{-\log\tau_{q_{m+1}}}{q_m}.
$$
归一化后 $\tau_q\le1$，故上式除分母方向合法。由(6.1)，再令 $\ell$ 趋上端，得
$$
\limsup_{q\to\infty}\frac{-\log\tau_q}{q}
\le\frac{16ac}{2(b-2a)}=\frac{8c}{13}.
\tag{6.3}
$$
(6.2)、(6.3)对每个 $c>c_*$ 成立，让 $c\downarrow c_*$ 即得(0.1)。无需右逆常数在端点一致。原非归一化向量只改变对数中的常数，不影响两种指数率。

## 7. 结论范围

R239已证明固定有限头加纯删除尾的形式分级像属于真实伴随像闭包。本文重新加入全部真实进位，付清其条件数平方代价和正能量的条件数尾项，得到更强的必要慢尾条件。

一般 Hilbert 向量可以具有(0.1)允许的多项式慢尾。尚未证明 $\kappa_m\tau_{n_m-d+1}^2\to0$，也未取得 R247 反能量尾级数发散。因此 $N=M$、其反面以及普通 ISP 均未由本附录决定。

本稿在2026-11-12约21:55 UTC执行环境失联后，依据此前完整草稿与逐式核验重建；根README §8后备仅保存小于100KB的UTF-8完整证明，不将API读取冒称实际git pull。
