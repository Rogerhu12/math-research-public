# R271 工作补充：真实尾理想、缺陷伴随压缩及最小原像的配对域

日期：2026-11-13 UTC。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d；根回读 R202、R205 的实际生成元与 R234 (2.2)，独立复核压缩和配对。状态：以下是原两个边界中可直接使用的算子范数结论；没有证明低核 / Schur 原像接近 $M$，不推出无权 $N=M$。

## 1. 两种边界共用的实际生成元

使用 [R202 §1–2](../results/R202-slow-boundary-finite-hole-degree-rigidity.md)、[R205 §1](../results/R205-cayley-boundary-degree-two-tail-sum-rigidity.md) 和 [R234 §2](../results/R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) 的同一个负整数边界模型：
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}.
$$
写
$$
W_n=\prod_{\nu=1}^{n}\alpha_{v_2(\nu)},\quad
d_j=W_{2^j}>0,\quad
N_j=d_j^{-1}B^{2^j},\quad
Y_j=N_j(I+N_j)^{-1}.
\tag{1.1}
$$
为免与头维数混淆，本节的 $d_j$ 只指归一化常数，后面头维数另记 $d=2^m$。两种慢算子分别为
$$
T_N=\sum_{j\ge0}b_jN_j,\qquad
T_Y=\sum_{j\ge0}b_jY_j,\qquad b_j=(j+1)^{-2}.
$$
以上级数按算子范数收敛，且两个 $T$ 都与 $B$ 交换。固定其中任一种，并令
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
于是 $B^kM\subset M$，并且对每个 $j$，
$$
N_jM=d_j^{-1}B(B^{2^j-1}M)\subset BM\subset N.
\tag{1.2}
$$
这同时适用于 $T_N$ 和 $T_Y$。此处使用的 $N_j$ 始终是实际 $B$ 的归一化幂；即使正在研究 $T_Y$，也无需把辅助尾换成 $Y_j$。

## 2. 任意可和尾列的真实理想作用

令 $c=(c_j)_{j\ge m}\in\ell^1$，定义
$$
X_m(c)=\sum_{j\ge m}c_jN_j,\qquad
D_m(c)=\sum_{j\ge m}c_jE_j .
$$
由 $\|N_j\|=\|E_j\|=1$，两和按范数绝对收敛。由 (1.2) 和 $N$ 闭，
$$
\boxed{X_m(c)M\subset N.}
\tag{2.1}
$$
R234 (2.2) 的真实 carry 界为
$$
\|N_j-E_j\|\le\eta_j,\qquad
\eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j}.
$$
所以有可求和、保留实际系数的误差
$$
\boxed{
\|X_m(c)-D_m(c)\|
\le\varepsilon_m(c):=\sum_{j\ge m}|c_j|\eta_j.
}
\tag{2.2}
$$
若 $P_M,P_W$ 是原 Hilbert 正交投影，则 (2.1) 准确给
$$
P_WX_m(c)P_M=0,\qquad P_MX_m(c)^*P_W=0.
$$
故
$$
\boxed{
\|P_WD_m(c)P_M\|
=\|P_MD_m(c)^*P_W\|
\le\varepsilon_m(c).
}
\tag{2.3}
$$
这里无需、也没有声称 $P_M$ 与任何尾删除、孔层投影或右逆交换。

特别，取 $c_j=b_j^3$，
$$
D_{3,m}=\sum_{j\ge m}b_j^3E_j,\qquad
X_{3,m}=\sum_{j\ge m}b_j^3N_j,\qquad
s_{3,m}=\sum_{j\ge m}(j+1)^{-6}.
$$
对 $m\ge1$，
$$
s_{3,m}\le\int_m^\infty x^{-6}\,dx=\frac1{5m^5},
$$
以及
$$
\boxed{
\|D_{3,m}\|,\|X_{3,m}\|\le s_{3,m},\qquad
\varepsilon_{3,m}:=\|X_{3,m}-D_{3,m}\|
\le s_{3,m}e^{-770\,16^m}.
}
\tag{2.4}
$$
因此，对每个真实 $w\in W$，
$$
\boxed{
\|P_MD_{3,m}^*w\|
\le s_{3,m}e^{-770d^4}\|w\|,\qquad d=2^m.
}
\tag{2.5}
$$
这使用纯尾 $D_{3,m}$ 本身，没有留下有限头 $A_{3,m}$。它是一条真实伴随压缩估计，而不是 $D_{3,m}^*w$ 的环境范数估计。

## 3. 把 $P_M$ 留在配对的另一侧

对任意 $u\in\mathcal H_-$ 和 $w\in W$，正交分解给准确等式
$$
\langle w,D_{3,m}u\rangle
=\langle P_MD_{3,m}^*w,P_Mu\rangle
+\langle (I-P_M)D_{3,m}^*w,(I-P_M)u\rangle,
\tag{3.1}
$$
按仓库内积约定也可同时取共轭。因而
$$
\boxed{
|\langle w,D_{3,m}u\rangle|
\le
\varepsilon_{3,m}\|w\|\,\|P_Mu\|
+s_{3,m}\|w\|\,\operatorname{dist}(u,M).
}
\tag{3.2}
$$
这里右侧第二项是明确的横向缺口。第一项已由真实理想付清，不能因第一项很小就删掉第二项。

现在固定纯尾孔层 $p$，并在前 $m$ 个物理位上张量恒等。记
$$
K_p=\mathbb C^{2^m}\otimes
(\ker D_m\cap\mathcal H_p^{(m)}).
$$
[全尾固定层双行闭像证明](../results/R271-appendix-full-tail-two-row-fixed-layer-range-and-contractive-known-images.md)给有界最小右逆
$$
R_{m,p}^{(3),\min}:K_p\longrightarrow K_{p+1},
\qquad
D_{3,m}R_{m,p}^{(3),\min}=I.
$$
将 $u=R_{m,p}^{(3),\min}h$ 代入 (3.1)–(3.2)，得到合法的真实配对
$$
\boxed{
|\langle w,h\rangle|
\le
\varepsilon_{3,m}\|w\|\,\|R_{m,p}^{(3),\min}h\|
+s_{3,m}\|w\|\,
\operatorname{dist}(R_{m,p}^{(3),\min}h,M).
}
\tag{3.3}
$$
不需要写 $P_MR=RP_M$，也没有将 $P_Mh$ 送入一个未说明的固定层域。

若源已知为 $h=D_{3,m}f$，其中 $f\in K_{p+1}$，则
$$
R_{m,p}^{(3),\min}h
=P_{K_{p+1}\ominus(K_{p+1}\cap\ker D_{3,m})}f,
\qquad
\|R_{m,p}^{(3),\min}h\|\le\|f\|.
\tag{3.4}
$$
所以 (3.3) 的第一项可以只付已知 $f$ 的范数。第二项仍是 (3.4) 中准确正交投影的像到 $M$ 的距离，不能把它换成 $\operatorname{dist}(f,M)$。

另一方面，可不经过最小原像，直接将任何一个已知 $f$ 代入 (3.2)：
$$
|\langle w,h\rangle|
\le
\varepsilon_{3,m}\|w\|\,\|f\|
+s_{3,m}\|w\|\,\operatorname{dist}(f,M).
\tag{3.5}
$$
因此在真实配对中，应按已有证据选择范数较小的最小原像，或选择更接近 $M$ 的其他原像；二者没有自动等价。一个完全准确的待估量是
$$
\inf_{\substack{f\in K_{p+1}\\D_{3,m}f=h}}
\left(
\varepsilon_{3,m}\|f\|
+s_{3,m}\operatorname{dist}(f,M)
\right).
\tag{3.6}
$$

## 4. 对当前低核通量的范围

原 R271 出生层第二下降块含 $D_{3,m}D_m^{h-3}f$，其最末源确在 $\ker D_m$。全尾固定层右逆因而可用 (3.4)；(2.5) 另外付清了纯尾到真实理想的替换。

尚未证明的是：这些已知像经过 $J_{h,p}$、真实低核投影和两个 Schur 逆之后，存在原像使 (3.6) 在原通量预算内足够小。它们一般不保持 $M$，原像存在及 (3.4) 的收缩都不支付横向距离。以上公式把该缺口留在配对另一侧，不添加任何投影交换假设。无权 $N=M$ 与普通 ISP 继续开放。
