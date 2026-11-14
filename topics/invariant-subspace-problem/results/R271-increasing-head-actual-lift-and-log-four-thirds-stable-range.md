# R271：逐头升级的真实稳定像提升与 4/3 次对数权饱和

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的实际中间结论。

本稿使用相容受限右逆，逐次把混合头从 $m$ 升为 $m+1$，每次由准确的新模型核方程重置纯核阶。它闭合无限校正，不在固定辅助头上无证使用全空间 Neumann 逆。由此替换旧 $X_7\to X_3$ 桥中随 $q$ 的 $e^{7q}$ 成本，并把前稿的大孔窗口真正提升到 $N$。

这里的新权是 $\exp(c[\log(2+\mathcal N)]^{4/3})$。全部正伸缩指数核的饱和此前已经证明，不重复登记；一般核内稠密性与 $N=M$ 仍未完成。

## 1. 逐头升级时准确的核阶运输

记
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+2)^{-2},
\qquad d=2^m.
$$
混合平方符号为
$$
P_m=D_m^2+Q_m,\quad [D_m,Q_m]=0,\quad
Q_m^d=0,\quad \|Q_m\|<1/2.
$$
实际伴随多项式给
$$
k\in\ker P_m\quad\Longrightarrow\quad D_m^{2d}k=0.
\tag{1.1}
$$
这里 $b_j$ 始终使用同一个原图尾物理位号，升级头时不把系数重新编号。$E_m$ 指第 $m$ 个图尾位的纯删除。提升一位时
$$
D_{m+1}=D_m-b_mE_m,\qquad E_m^2=0,\qquad [D_m,E_m]=0.
$$
有限二项式因而准确给
$$
D_{m+1}^{2d+1}
=D_m^{2d+1}-(2d+1)b_mE_mD_m^{2d}.
$$
所以
$$
\boxed{
k\in\ker P_m\quad\Longrightarrow\quad
k\in\ker D_{m+1}^{2d+1}.
}
\tag{1.2}
$$

若 $k$ 的旧高尾孔数至多为 $Q$，把第 $m$ 位归入新头不会增加剩余高尾孔数。新符号 $P_{m+1}$ 只降低新高尾孔数。因此
$$
r=P_{m+1}k=(P_{m+1}-P_m)k
\in\ker D_{m+1}^{2d+1}\cap\mathcal H_{\le Q}^{(m+1)}.
\tag{1.3}
$$
这里用的是 $P_{m+1}$ 与 $D_{m+1}$ 的实际交换性。

两次原实际误差界给
$$
\boxed{
\|P_{m+1}-P_m\|
\le36(\eta_m+\eta_{m+1})\le72\eta_m.
}
\tag{1.4}
$$
原物理位号保持不变，且 $\eta_m\le e^{-770d^4}$。

## 2. 每一步使用已证受限右逆

在新头 $m'=m+1$、$d'=2d$ 上，用 [R254 第十附录](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md) 的
$$
\widetilde{\mathcal G}_{m',Q}
=\sum_{\ell<d'}(-Q_{m'})^\ell R_{2\ell+2}.
$$
它是真实 $P_{m'}$ 右逆，输出孔数最多增加 $2d'$。输入 (1.3) 的核阶为 $2d+1\le2d'$，所以原受限界确实适用：
$$
\|\widetilde{\mathcal G}_{m',Q}r\|
\le d'(2L')^{4d'-1}\|r\|,
$$
$$
L'=512\sqrt{Q+2d'+1}
 (m'+Q+2d'+2)^{3/2}.
\tag{2.1}
$$
置
$$
k'=k-\widetilde{\mathcal G}_{m',Q}r.
$$
则
$$
P_{m'}k'=0.
\tag{2.2}
$$
此后再由新头的准确伴随多项式重置
$D_{m'}^{2d'}k'=0$。不把前一步粗略增加的核阶无限累积。

## 3. 所有迭代的统一预算

固定初始 $m_0\ge4$，$d_0=2^{m_0}$，并设
$$
k_0\in\ker P_{m_0}\cap\mathcal H_{\le Q_0}^{(m_0)},
\qquad
1\le Q_0\le e^{d_0^3/3}.
\tag{3.1}
$$
递归取
$$
m_n=m_0+n,\qquad d_n=2^nd_0,\qquad
Q_n=Q_0+4d_n-4d_0,
$$
并按第 2 节从 $k_n$ 构造 $k_{n+1}$。归纳保证
$$
k_n\in\ker P_{m_n}\cap\mathcal H_{\le Q_n}^{(m_n)}.
\tag{3.2}
$$
因为每一步最多增加 $2d_{n+1}=4d_n$ 次新高尾孔，$Q_{n+1}=Q_n+4d_n$ 正好覆盖输出。

写 $z=d_n\ge16$。第 $n$ 步的新辅助常数满足
$$
L'_n\le512(Q_0+10z)^2.
$$
由 (3.1)，
$$
\log(2L'_n)
\le\tfrac23d_0^3+12+2\log z.
$$
所以 (2.1) 的全部对数成本不超过
$$
\begin{aligned}
\log(2z)+8z\log(2L'_n)
&\le \tfrac{16}{3}z d_0^3
 +96z+16z\log z+\log(2z)\\
&\le7z^4.
\end{aligned}
\tag{3.3}
$$
末一步只用 $d_0\le z$、$z\ge16$；其余低阶项远小于 $z^4$。

结合 (1.4) 和真实 $\eta_{m_n}\le e^{-770z^4}$，
$$
\boxed{
\|k_{n+1}-k_n\|
\le e^{-750d_n^4}\|k_n\|.
}
\tag{3.4}
$$
令 $\varepsilon_n=e^{-750d_n^4}$。这些误差的和小于
$2e^{-750d_0^4}$，因此
$$
\|k_n\|\le
\prod_{j<n}(1+\varepsilon_j)\|k_0\|
\le2\|k_0\|.
$$
实际 Hilbert 级数遂收敛到 $k_\infty$，并有
$$
\boxed{
\|k_\infty-k_0\|
\le4e^{-750d_0^4}\|k_0\|
\le e^{-749d_0^4}\|k_0\|.
}
\tag{3.5}
$$
由于 $P_{m_n}\to P$ 为普通算子范数收敛，(3.2) 和 $k_n\to k_\infty$ 给
$$
Pk_\infty=0.
\tag{3.6}
$$
这是全部无限迭代的结论，不是只做第一步残差修复。

## 4. 极限具有真实次数正则性，因而属于 N

每步差 $k_{n+1}-k_n$ 的原图尾总孔数不超过
$$
m_{n+1}+Q_{n+1}\le Q_0+10d_n.
$$
由 (3.4)，对每个固定 $c>0$，
$$
\sum_{n\ge0}
\|e^{c\mathcal N_{\rm tail}}(k_{n+1}-k_n)\|
\le
2\|k_0\|
\sum_{n\ge0}
e^{c(Q_0+10d_n)-750d_n^4}
<\infty.
\tag{4.1}
$$
初值 $k_0$ 只有有限孔，因此
$$
k_\infty\in\operatorname{Dom}e^{c\mathcal N_{\rm tail}}
\quad\text{对每个固定 }c>0.
\tag{4.2}
$$
$Q_0$ 可以很大，但在这条收敛级数中是固定常数，不破坏收敛。指数域的算子常数可以依赖这个初始有限 $Q_0$；下面的 Hilbert 小误差仍保持所列统一界。

还要支付原实际图。采用全空间多项式图
$$
Jx=(x,-Hx),
$$
其中 $H=\mathcal A$ 对应 $N$ 型，
$H=(I-\eta C)\mathcal A-\eta C$ 对应 $Y$ 型。
在 $K=\ker P$ 上它与原核图一致。以下完整检查实际图的正则性。

设 $\mathcal H_c=\operatorname{Dom}e^{c\mathcal N_{\rm tail}}$，配加权 Hilbert 范数。若 $K_\ell$ 只作用前 $\ell+1$ 位，则尾部权因子准确消掉，而有限头上
$$
\|e^{c\mathcal N_{\rm tail}}K_\ell
 e^{-c\mathcal N_{\rm tail}}\|
\le e^{c(\ell+1)}\|K_\ell\|.
$$
固定任一有限低头 $h\ge4$，混合截断
$\mathcal A^{[h]}=\mathcal A_h+D_h$
在 $\mathcal H_c$ 上有界：头部分至多付 $e^{ch}\|\mathcal A_h\|$，纯删除部分付 $e^{-c}\|D_h\|$。其余真实相邻壳满足
$\|\Delta\mathcal A_\ell\|\le52\eta_\ell$；快速头的相邻壳满足
$\|\Delta C_\ell\|\le2\eta_\ell$。因此
$$
\|\mathcal A\|_{\mathcal H_c\to\mathcal H_c}
\le e^{ch}\|\mathcal A_h\|+e^{-c}\|D_h\|
 +52\sum_{\ell\ge h}\eta_\ell e^{c(\ell+1)}<\infty,
$$
$$
\|C\|_{\mathcal H_c\to\mathcal H_c}
\le e^{ch}\|C_h\|
 +2\sum_{\ell\ge h}\eta_\ell e^{c(\ell+1)}<\infty.
$$
加权范数中的和与原 Hilbert 范数中的真实算子相同，因为前者收敛蕴含后者收敛，且有限孔向量是共同稠密域。两个有限乘积构成的 $H$ 也保持 $\mathcal H_c$；加入原第 $0$ 位最多再付 $e^c$。


所以
$$
Jk_\infty\in M\cap\operatorname{Dom}e^{c\mathcal N}
\quad(c>0).
$$
例如取 $c=4$，Cauchy--Schwarz 给它属于旧的加权层 $\ell^1$ 空间 $X_3$。使用 [R239 已证实际指数权结论](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) $M\cap X_3\subseteq N$，得到
$$
Jk_\infty\in N.
\tag{4.3}
$$
本稿不以待证明的新对数权结论证明这一步，故没有循环。

所有步骤线性，Hilbert 估计统一，因此
$$
\Lambda^{\rm inc}_{m_0,Q_0}k_0:=Jk_\infty
$$
是从所述混合模型核到 $N$ 的实际有界线性映射。由
$\|J\|\le5/4$、$\|J-J_{m_0}\|\le27\eta_{m_0}$ 及 (3.5)，
$$
\boxed{
\|\Lambda^{\rm inc}_{m_0,Q_0}k_0-J_{m_0}k_0\|
\le e^{-748d_0^4}\|k_0\|,
\qquad Q_0\le e^{d_0^3/3}.
}
\tag{4.4}
$$
这个界替换了旧桥的 $e^{7Q_0}$ 成本。

## 5. 接回大窗口：全部实际范数均有余量

[R254 第十二附录](R254-appendix-factorial-preimages-carry-jets-and-large-low-output-windows.md) 已证明：对实际 $u\in K$，取
$$
q_m=\left\lfloor e^{d^3/4}\right\rfloor,\qquad d=2^m,
$$
存在低方程正交投影 $v_m$，满足
$$
\|v_m\|\le\|u\|,\quad
\|P_{\le q_m}u-v_m\|\le e^{-700d^4}\|u\|,\quad
v_m\to u,
$$
$$
v_m\in\ker D_m^{2d},\qquad
r_m=P_mv_m\in\mathcal H_{q_m-1}\oplus\mathcal H_{q_m}.
\tag{5.1}
$$

按已证相容右逆取
$c_m=\widetilde{\mathcal G}_{m,q_m}r_m$，
$k_m=v_m-c_m$。准确有
$$
c_m\in\ker D_m^{2d}\cap
\mathcal H_{[q_m+1,q_m+2d]},\qquad
k_m\in\ker P_m\cap\mathcal H_{\le q_m+2d}.
\tag{5.2}
$$
这里 $c_m$ 的核阶由 $P_mk_m=0$ 推出 $D_m^{2d}k_m=0$，再与 $D_m^{2d}v_m=0$ 相减得到；不靠右逆本身保同一核阶。
[R254 第十一附录](R254-appendix-top-residual-derivatives-and-log-square-stable-range.md) 的特殊残量公式仍给
$$
\|c_m\|\le
\tfrac12 Z^2(1+Z)F_m(Z)^2\,\Theta_m,
$$
$$
F_m(Z)=\sum_{j<d}Z^{2j}\|Q_m^j\|,\qquad
Z=1024\sqrt{q_m+2d+1}(m+q_m+2d+2)^{3/2},
$$
$$
\Theta_m\le
\tau_{q_m-2d-1}(u)+e^{-700d^4}\|u\|.
\tag{5.3}
$$
在新窗口，只用粗界就足够：
$$
\log Z\le9+\tfrac12d^3,\qquad
F_m(Z)\le d Z^{2d-2}.
$$
从而对所有 $m\ge4$，
$$
\boxed{
\|c_m\|
\le e^{5d^4}\left[
\tau_{q_m-2d-1}(u)+e^{-700d^4}\|u\|
\right].
}
\tag{5.4}
$$
也可直接用 $\Theta_m\le\|u\|$ 得
$\|c_m\|\le e^{5d^4}\|u\|$。

因为 $Q_0=q_m+2d\le e^{d^3/3}$，第 4 节的新桥可用于整个 $k_m$：
$$
n_m=\Lambda^{\rm inc}_{m,q_m+2d}k_m\in N.
$$
用 $\|k_m\|\le2e^{5d^4}\|u\|$ 支付完整修复范数，得到
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-742d^4}\|u\|.
}
\tag{5.5}
$$
这里既支付了大窗口低方程，也支付了全部无限实际提升。

## 6. 新的 4/3 次对数权定理

**定理。** 对两个原实际慢边界，若
$$
c>5\cdot4^{4/3},
$$
则
$$
\boxed{
M\cap\operatorname{Dom}
\exp\!\left(c[\log(2+\mathcal N)]^{4/3}\right)
\subseteq N.
}
\tag{6.1}
$$
例如固定 $c=64$ 足够。

证明：若 $w=Ju$ 属于左侧，第一位分量和总孔数控制给
$$
\tau_Q(u)\le C_w
 \exp[-c(\log(Q+2))^{4/3}].
$$
而
$$
\log(q_m-2d+1)=d^3/4+o(1).
$$
因此 (5.4) 中的主指数为
$$
\left(5-c\,4^{-4/3}+o(1)\right)d^4\longrightarrow-\infty.
$$
于是 $\|c_m\|\to0$。由 $v_m\to u$、$J_m\to J$ 及 (5.5)，
$n_m\to Ju=w$ 强收敛。$N$ 闭，故 $w\in N$。证毕。

它严格扩大此前平方对数权的已证范围；没有宣称临界系数或所有正 $c$。特别，对任意 $\beta>4/3$ 和任意 $c>0$，相应
$\exp(c[\log(2+\mathcal N)]^\beta)$ 正则核也属于 $N$。

## 7. 真缺陷的全序列必要慢尾

若 $0\ne w=Ju\in M\ominus N$，由 (5.1)、(5.5) 和 $n_m\in N$，
$$
\langle J_mc_m,w\rangle\to\|w\|^2.
$$
准确高尾支撑仍给
$$
\|c_m\|\tau_{q_m-1}(w)\ge\tfrac25\|w\|^2
$$
对充分大的 $m$ 成立。代入 (5.4) 并吸收明确小项，
$$
e^{5d^4}\tau_{q_m-2d-1}(w)^2
\ge\tfrac15\|w\|^2.
$$
故在该网格上
$$
\log\frac{\|w\|}{\tau_{q_m-2d-1}(w)}
\le\tfrac52d^4+\tfrac12\log5.
\tag{7.1}
$$
相邻次数网格现在很疏：
$$
\frac{\log q_{m+1}}{\log q_m}\longrightarrow8.
$$
必须用下一网格的 $d^4$ 付 $16$ 倍，而不能沿用平方对数稿中“对数网格比趋于 $1$”的常数。按尾单调性，得到
$$
\boxed{
\limsup_{Q\to\infty}
\frac{-\log(\tau_Q(w)/\|w\|)}
{[\log(Q+2)]^{4/3}}
\le40\cdot4^{4/3}.
}
\tag{7.2}
$$
特别，
$-\log(\tau_Q(w)/\|w\|)=O((\log(Q+2))^{4/3})$。
这是非零缺陷的必要慢尾条件，仍不排除一般 Hilbert 尾。

## 8. 剩余问题

本稿每次改变头后重新得到准确模型核，再支付新纯核阶，因此无限升级与固定头上的无证 Neumann 迭代不同。极限的真实次数正则性和 $N$ 归属都已证明。

然而 (6.1) 的正则核在整个 $M$ 内是否稠密仍未知；任意阶多项式次数矩也不自动给该固定对数幂权。一般特殊修复的最小能量、无权核内核心与 $N=M$ 仍然开放。普通 Hilbert ISP 未完成。
