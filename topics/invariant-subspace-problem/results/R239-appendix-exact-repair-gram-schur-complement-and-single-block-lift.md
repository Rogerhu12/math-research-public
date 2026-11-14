# R239 附录：原最小修复的链 Gram、Schur 补与逐头单块残量

日期：2026-11-13。作者：Astra-ISP-0c017065 / boundary_resume。
状态：主会话已全文核验下述实际恒等式及能量界；无权 $N=M$ 未完成。

本稿接[全整数原线性窗口](R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)，不重计已证的 $4/3$ 权阶与 $K_*$ 常数。完整证明见[单块残量稿](../notes/2026-11-13-linear-head-single-block-residual-and-commutator-trace-obstruction-boundary-resume.md)及[链 Gram 稿](../notes/2026-11-13-minimal-repair-chain-gram-schur-complement-and-local-band-energy-boundary-resume.md)。

## 1. 原最小修复恰是一个压缩正 Gram 的逆

固定原物理头 $m\ge5$、$d=2^m$ 和合法 $q$，令
$A=A_m$、$D=D_m$、$L=A+D$。$A^d=0$，$D$ 降低一个尾孔，二者交换。所有层保持完整尾位置，不限制最大物理位。

在
$$
\mathscr C=\bigoplus_{t=1}^d\mathcal H_{q+t}^{(m)}
$$
定义
$$
Sc=(Ac_1+Dc_2,\ldots,Ac_{d-1}+Dc_d,Ac_d),
\quad\mathscr K=\ker S,
\quad Fc=Dc_1\quad(c\in\mathscr K).
\tag{1.1}
$$
此处没有附加 $D^dc=0$。

R254J 的同一相容族 $DR_t=R_{t-1}$ 给整个 $\mathcal H_q^{(m)}$ 上的有界右逆
$$
\mathcal Rr=\sum_{j=0}^{d-1}(-A)^jR_{j+1}r,\qquad
F\mathcal R=I.
$$
例如
$$
\|\mathcal R\|\le
\Gamma_{m,q}=d\,6^{d-1}(2R)^{q+d},\qquad
R=512\sqrt{q+d+1}(m+q+d+2)^{3/2}.
\tag{1.2}
$$
固定 $m,q$ 时有限；不要求对全部 $q$ 一致。

令 $D_0^*y=(D^*y,0,\ldots,0)$。准确正 Gram 为
$$
\boxed{\mathsf G_{m,q}=FF^*=D_0P_{\mathscr K}D_0^*,
\qquad \mathsf G_{m,q}\ge\Gamma_{m,q}^{-2}I.}
\tag{1.3}
$$

现在取实际 $w\in M=\ker T$ 的低方程正交投影 $v=v_{m,q}$，
$r=Lv=A v_q$。前稿的单层身份给
$$
D^kr=(-1)^kA^{k+1}v_{q-k}\qquad(0\le k<d).
\tag{1.4}
$$
对任意 $c\in\mathscr K$、$Fc=r$，逐层准确有
$$
D^dc_t=(-A)^{t-1}D^{d-t}r
=(-1)^{d-1}A^dv_{q-d+t}=0.
\tag{1.5}
$$
所以仅对这个实际残量，原附加纯核约束自动成立，修复集就是 $\{c\in\mathscr K:Fc=r\}$。
不得把 (1.5) 扩到任意 $r\in\mathcal H_q$。

因此原 Hilbert 最小修复量准确为
$$
\boxed{
c^{\min}=F^*\mathsf G_{m,q}^{-1}r,\qquad
\lambda_{m,q}(w)^2=\langle\mathsf G_{m,q}^{-1}r,r\rangle .
}
\tag{1.6}
$$
这提供了真正需要估计的压缩算子。

## 2. 分母是完整伴随链能量

由 $(\ker S)^\perp=\overline{\operatorname{Ran}S^*}$，
$$
\boxed{
\mathcal E(y)=\langle\mathsf G_{m,q}y,y\rangle
=\inf_{z_1,\ldots,z_d}
\left[
\|D^*y-A^*z_1\|^2+
\sum_{t=2}^d\|D^*z_{t-1}+A^*z_t\|^2
\right].
}
\tag{2.1}
$$
$z_t\in\mathcal H_{q+t}^{(m)}$。只取 inf，不假设 $\operatorname{Ran}S^*$ 闭或最小值由某个 $z$ 达到。
由 (1.3)，每个固定 $m,q$ 的分母严格正，且
$$
\lambda^2=\sup_{y\ne0}\frac{|\langle r,y\rangle|^2}{\mathcal E(y)}.
\tag{2.2}
$$
环境创建范数只给 $\mathcal E(y)\le\|D^*y\|^2$；
环境 $D^*$ 的下界并不下传这个 inf。

残量属于闭子空间 $\mathscr V=\operatorname{Ran}(A\otimes I)$。
相对于 $\mathscr V\oplus\ker(A^*\otimes I)$，写
$\mathsf G=(G_{ij})_{1\le i,j\le2}$。真正消去正交方向后，
$$
\boxed{
\lambda^2=
\left\langle
(G_{11}-G_{12}G_{22}^{-1}G_{21})^{-1}r,r
\right\rangle.
}
\tag{2.3}
$$
不是 $G_{11}^{-1}$。
例如正矩阵
$\left(\begin{smallmatrix}1&\sqrt{1-\epsilon}\\
\sqrt{1-\epsilon}&1\end{smallmatrix}\right)$
的可见块为1、Schur补却为 $\epsilon$；该例只校准投影推理，不声称实际模型实现这个坏矩阵。

## 3. 全整数窄带保留的两侧能量

仍取
$$
m(q)=\max\left(5,\left\lceil
\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right),
\quad d_q=2^{m(q)},\quad\ell_q=d_q+m(q),\quad q\ge128.
$$
前稿修复指数记为 $F_q$，
$F_q=(K_*+o(1))(\log q)^{4/3}$、
$K_*=3(16/770)^{1/3}$。

保留原输入的真实窄带
$$
\beta_q=\|\mathbf1_{[q-d_q+1,q+m(q)]}(\mathcal N)w\|,
$$
相容原像估计给
$$
\lambda_q\le e^{F_q}(\beta_q+e^{-74d_q^4}\|w\|).
\tag{3.1}
$$
这些窗口的全部整数覆盖满足
$$
\sum_{\{q:\ p\in[q-d_q+1,q+m(q)]\}}\ell_q^{-1}\le4.
$$
此外 $q\ge Q$ 时窗口下端至少为 $Q-2d_Q+1$。
分组支付低投影误差后得到
$$
\boxed{
\sum_{q\ge Q}\frac{e^{-2F_q}\lambda_q^2}{\ell_q}
\le8\tau_{Q-2d_Q}(w)^2+
4e^{-147d_Q^4}\|w\|^2.
}
\tag{3.2}
$$
这里 $\tau_s=\|\mathbf1_{\{\mathcal N>s\}}w\|$。
与仅使用整个尾的逐 $q$ 上界相比，(3.2) 保留了可求和的局部能量。

若 $0\ne w\in M\ominus N$，前稿同时给
$$
\sum_{q\ge Q}\frac1{\ell_q\lambda_q^2}
\le8\tau_Q(w)^2/\|w\|^4.
$$
两侧有限和用 Cauchy–Schwarz 后取极限，
$$
\boxed{
\tau_Q(w)^2
\left[\tau_{Q-2d_Q}(w)^2+
\tfrac12e^{-147d_Q^4}\|w\|^2\right]
\ge\frac{\|w\|^4}{64}
\left(\sum_{q\ge Q}\frac{e^{-F_q}}{\ell_q}\right)^2.
}
\tag{3.3}
$$
这些界仍允许慢 Hilbert 尾，尚未强制
$\sum_q[\ell_q(1+\lambda_q^2)]^{-1}$ 发散。

## 4. 逐头 carry 只落在一个真实块

固定旧头 $p$、$d=2^p$，按新最高位分块。
记旧头 $A_p$、$b_p=(p+1)^{-2}$，则两型都准确有
$$
A_{p+1}=
\begin{pmatrix}A_p&b_pI+K_p\\0&A_p\end{pmatrix},
\qquad
H_p=A_p+b_pE_p=
\begin{pmatrix}A_p&b_pI\\0&A_p\end{pmatrix}.
\tag{4.1}
$$
其中
$$
C_{j,p}=\left(\prod_{\nu=j}^{p-1}\eta_\nu\right)
E_j^*\cdots E_{p-1}^*,\quad
K_p=\sum_{j<p}b_jC_{j,p}\quad(N),
$$
$$
K_p=\sum_{j<p}b_j(I+N_j^{[p]})^{-1}
C_{j,p}(I+N_j^{[p]})^{-1}\quad(Y).
$$
保留左右乘序，不假设 $C_{j,p}$ 与有限头逆交换。

若 $k=(k_0,k_1)\in\ker(D_{p+1}+H_p)$，底块满足
$(D_{p+1}+A_p)k_1=0$，所以新残量为 $(K_pk_1,0)$，
$$
D_{p+1}^s(K_pk_1,0)=(K_p(-A_p)^sk_1,0),
\quad D_{p+1}^dr=0.
$$
只需旧 $d$ 阶纯核，不需要先前有效粗界中的 $d+1$ 阶。
全部混合词准确缩成
$$
A_{p+1}^j(A_{p+1}-H_p)H_p^s
=\begin{pmatrix}0&A_p^jK_pA_p^s\\0&0\end{pmatrix}.
\tag{4.2}
$$
因此校正可以保持底块：
$$
c=(c_0,0),\qquad
c_0=\sum_{j<d}(-A_p)^jR_{j+1}K_pk_1,\qquad
(D_{p+1}+A_{p+1})(k-c)=0.
$$
对有限孔输入最多增加 $d$ 次尾孔；不提供全 $H$ 的有界右逆。

## 5. 两条不能直接采用的简化

若能解 $[A_p,Z_p]=K_p$，则 $Z_pk_1$ 会给不增加孔数的校正。
必要条件是 $\operatorname{Tr}(A_p^rK_p)=0$。
但最小两位 $p=1$ 时，两型分别有
$$
A_1=b_0E_0,\quad K_1=b_0\eta_0E_0^*\quad(N),
$$
$$
K_1=b_0\eta_0(E_0^*-I+E_0)\quad(Y),
$$
并且都满足
$$
\operatorname{Tr}(A_1K_1)=b_0^2\eta_0\ne0.
$$
故这条纯有限头交换子校正不存在；不能因此断言所有无权校正失败。

R254J 的实际递推还精确给
$$
F^{(t)}_{s,0}(x)=
\frac{(-1)^s\binom{s+t-1}{s}}{(s+t)!}
\prod_{\nu=s}^{2s+t-1}(x-\nu)^{-1}.
$$
取 $t=j+1$，同总阶 $n=j+s+1$ 的大小为 $1/(j!s!n)$，
还带不同源层移位分母和外侧 $(-1)^j$。
因此不能直接用未加权
$\sum_jA^j(A-H)H^{n-1-j}=A^n-H^n$
合并真实相容原像。
这仍允许研究合法重组和更好的最小范数估计。

接下来需要控制 (2.1) 的完整链能量或 (2.3) 的实际 Schur 补，
并利用残量 (1.4) 的特殊结构。当前恒等式、投影校准和两侧能量均未完成无权核内饱和。
