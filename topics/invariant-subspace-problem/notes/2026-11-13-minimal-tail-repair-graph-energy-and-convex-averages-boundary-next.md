# 互不相交高尾修复的正能量与最小图范数判据

日期：2026-11-13（UTC）。作者：boundary_next；AI-assisted，GPT-6 Astra Pro。状态：已证明的实际缺陷必要条件及稳定像充分条件；$N=M$ 仍未证明。

本稿接续[一次共同截平四次窗口](../results/R239-appendix-quartic-hole-window-by-common-flattening-and-exact-repair.md)，并使用 R254 第六附录与 R239 的真实稳定像提升。此前已知：一个有界高尾修复子列足以把实际核向量送入 $N$。下面利用不同物理截断产生的修复落在互不相交的**原全部孔次数窗口**，把条件放宽为一个倒数能量级数发散条件；非零真缺陷则迫相反的可和性，并有明确尾预算。

证明只用实际 Hilbert 正交性及已支付的提升误差，不使用环境头相似范数作为正能量，也不运输未知限制像。

## 1. 已付输入和固定序列

对两个实际边界 $T=T_N,T_Y$，记
$$
M=\ker T,\qquad N=\overline{BM},\qquad D_{\rm def}=M\ominus N.
$$
为避免与纯尾删除 $D_m$ 混淆，本稿把缺陷记为 $D_{\rm def}$。

在删除原首位后的平方核 $K=\ker P$ 上，实际图为
$$
w=Ju=(u,-Hu),\qquad u\in K,
$$
其中 $Y$ 型使用已经核验的多项式同核图。对前 $m$ 个尾位的真实混合模型，令
$$
d_m=2^m,\qquad q_m=100d_m^4,\qquad m\ge4,
$$
$$
P_m=D_m^2+Q_m,\qquad
D_m=\sum_{j\ge m}(j+2)^{-2}E_j.
$$
首位图 $J_mx=(x,-H_mx)$ 满足
$$
\|x\|\le\|J_mx\|\le\tfrac54\|x\|,\qquad
\|J_m-J\|\le27\eta_m,
$$
$$
-\log\eta_m=1400d_m^4-630d_m^3+300d_m.
\tag{1.1}
$$
$H_m$ 在高尾孔次数上只下降零次或一次。

$P_\ell^{(m)}$ 表示高尾恰有 $\ell$ 孔的正交投影，包含有限头恒等。令 $v_m$ 是 $u$ 到真实闭空间
$$
\mathcal W_m
=\ker D_m^{2d_m}
\cap\mathcal H_{\le q_m}^{(m)}
\cap\ker(P_{\le q_m-2}^{(m)}P_m)
\tag{1.2}
$$
的正交投影。一次共同截平稿给
$$
\|v_m-P_{\le q_m}^{(m)}u\|
\le e^{-800d_m^4}\|u\|,\qquad
\|v_m\|\le\|u\|.
\tag{1.3}
$$
因此 $v_m\to u$。残量
$$
r_m=P_mv_m
$$
只在高尾孔层 $q_m-1,q_m$，且
$$
\|r_m\|
\le\|P_{\{q_m-1,q_m\}}^{(m)}u\|
+e^{-800d_m^4}\|u\|\longrightarrow0.
\tag{1.4}
$$

同一稿已构造一个实际高尾修复 $c_m^{(0)}$，满足
$$
P_mc_m^{(0)}=r_m,\qquad
c_m^{(0)}\in\ker D_m^{2d_m}
\cap\mathcal H_{[q_m+1,q_m+2d_m]}^{(m)},
$$
$$
\|c_m^{(0)}\|\le e^{351d_m^4}\|u\|.
\tag{1.5}
$$
这里的存在性和完整范数上界均已证明，不再列作开放项。

对孔次数上界 $L_m=q_m+2d_m$，真实 R239 提升有
$$
\Lambda_{m,L_m}:
\ker P_m\cap\mathcal H_{\le L_m}^{(m)}
\longrightarrow N,
$$
$$
\|\Lambda_{m,L_m}k-J_mk\|
\le\delta_m\|k\|,\qquad
\delta_m\le e^{-403d_m^4}.
\tag{1.6}
$$
这一数值已经付清原实际 $N/Y$ 全部进位和两权右逆的输出域。

## 2. 取真正最小的高尾图能量

定义闭线性空间
$$
\mathcal Y_m
=\ker D_m^{2d_m}
\cap\mathcal H_{[q_m+1,q_m+2d_m]}^{(m)}
$$
和非空闭仿射集
$$
\mathcal C_m(u)=\{c\in\mathcal Y_m:P_mc=r_m\}.
\tag{2.1}
$$
它非空由 (1.5) 保证。闭性来自纯高阶核、正交孔支撑和有界算子方程的闭性；不需要假设一般算子值域闭。

在 $\mathcal Y_m$ 上使用实际正图内积
$$
\langle c,h\rangle_{G_m}
=\langle J_mc,J_mh\rangle
=\langle c,h\rangle+\langle H_mc,H_mh\rangle.
$$
由 (1.1)，这个内积与原内积等价，
$$
\|c\|^2\le\|c\|_{G_m}^2\le\tfrac{25}{16}\|c\|^2.
\tag{2.2}
$$
故非空闭仿射集 $\mathcal C_m(u)$ 有唯一 $G_m$ 范数最小元，记为 $c_m$。令
$$
b_m=J_mc_m,\qquad \gamma_m=\|b_m\|.
\tag{2.3}
$$
这是本稿所用的具体最小图能量，不是未经证明的环境压缩范数。

由最佳逼近及候选 (1.5)，
$$
\boxed{
\|c_m\|\le\gamma_m
\le\tfrac54e^{351d_m^4}\|u\|.
}
\tag{2.4}
$$
特别，换成最小图能量修复不会破坏已经支付的进位预算。

置
$$
k_m=v_m-c_m.
$$
准确有
$$
k_m\in\ker P_m\cap\mathcal H_{\le q_m+2d_m}^{(m)},
\qquad
P_{\le q_m}^{(m)}k_m=v_m.
\tag{2.5}
$$
并且 $v_m,c_m$ 支撑正交，所以
$$
\|k_m\|^2=\|v_m\|^2+\|c_m\|^2.
$$
由 (2.4)，可安全使用
$$
\|k_m\|\le\tfrac94e^{351d_m^4}\|u\|.
\tag{2.6}
$$

令
$$
n_m=\Lambda_{m,q_m+2d_m}k_m\in N.
$$
结合 (1.6)、(2.6)，
$$
\boxed{
\|n_m-(J_mv_m-b_m)\|
\le e^{-50d_m^4}\|u\|.
}
\tag{2.7}
$$
常数 $9/4$ 已被 $e^{2d_m^4}$ 的余量吸收。

## 3. 修复在原全部孔次数上的支撑确实互不相交

本节改用 $\mathsf P_\ell$ 表示**原全部物理位**的孔次数投影，包括原首位和有限头。不能把不同 $m$ 的高尾孔层直接当成共同正交分级。

$c_m$ 的高尾孔数在 $[q_m+1,q_m+2d_m]$，前 $m$ 个尾位至多贡献 $m$ 个孔。$J_m$ 的第二分量再加入原首位一个孔，而 $H_m$ 最多删除一个高尾孔。因此保守而准确的总支撑为
$$
\boxed{
b_m=\mathsf P_{I_m}b_m,\qquad
I_m=[q_m,q_m+2d_m+m+1]\cap\mathbb Z.
}
\tag{3.1}
$$
这里不要求 $H_m$ 在有限头孔数上单调；只使用该头总共 $m$ 位。

由于
$$
q_{m+1}=16q_m,\qquad
q_m+2d_m+m+1<16q_m,
$$
各 $I_m$ 两两不交。于是
$$
\boxed{\langle b_m,b_\ell\rangle=0\quad(m\ne\ell).}
\tag{3.2}
$$
这是真实原 Hilbert 空间中的正交性，不带任何头相似条件数。

由 (1.1)、(1.3)、(2.7)，可写
$$
n_m=w-b_m+\varepsilon_m,\qquad w=Ju,
\tag{3.3}
$$
其中
$$
\|\varepsilon_m\|
\le\tfrac54\|v_m-u\|
+(27\eta_m+e^{-50d_m^4})\|u\|
\longrightarrow0.
\tag{3.4}
$$
若 $\tau_q(u)$ 表示删除原首位后按全部孔数的尾，则对每个 $M\ge4$ 还有统一尾起点界
$$
\boxed{
\sup_{m\ge M}\|\varepsilon_m\|
\le
\tfrac54\tau_{q_M}(u)
+3e^{-50d_M^4}\|u\|
=:\epsilon_M(u)\longrightarrow0.
}
\tag{3.5}
$$
这是先固定起点再作平均所需的一致界。

## 4. 正凸平均：倒数能量级数发散即足够

对固定 $u\in K$，定义非负权
$$
a_m=\frac1{1+\gamma_m^2},\qquad
A_{M,K}=\sum_{m=M}^K a_m.
$$
只要 $K\ge M$，就有 $A_{M,K}>0$，可以取实际稳定像的正凸平均
$$
\bar n_{M,K}
=\frac1{A_{M,K}}\sum_{m=M}^K a_m n_m\in N.
\tag{4.1}
$$
由 (3.2)，
$$
\left\|\frac1{A_{M,K}}
\sum_{m=M}^K a_m b_m\right\|^2
=\frac{\sum_{m=M}^K a_m^2\gamma_m^2}{A_{M,K}^2}
\le\frac1{A_{M,K}},
$$
因为 $a_m^2\gamma_m^2\le a_m$。
由正权归一化和 (3.5)，
$$
\left\|\frac1{A_{M,K}}
\sum_{m=M}^K a_m\varepsilon_m\right\|
\le\epsilon_M(u).
$$
因此得到可直接审查的逼近误差：
$$
\boxed{
\|\bar n_{M,K}-Ju\|
\le\epsilon_M(u)+A_{M,K}^{-1/2}.
}
\tag{4.2}
$$

若
$$
\sum_{m\ge4}\frac1{1+\gamma_m^2}=\infty,
$$
则对任意固定 $M$，令 $K\to\infty$ 使第二项趋零，再令 $M\to\infty$ 使第一项趋零。因为 $N$ 闭，
$$
\boxed{
\sum_{m\ge4}\frac1{1+\gamma_m(u)^2}=\infty
\quad\Longrightarrow\quad Ju\in N.
}
\tag{4.3}
$$
这比存在有界子列弱。例如，若 $\gamma_m=O(\sqrt m)$，该级数仍发散，即使修复范数没有有界子列。更一般地，
$$
\gamma_m^2
=O\!\left((m+1)\log(m+2)\log\log(m+e^e)\right)
\tag{4.4}
$$
也足够，因为相应倒数级数发散。

这里只断言充分性；没有证明一般实际核向量满足 (4.3) 或 (4.4)。

## 5. 非零真实缺陷的 Bessel 尾能量

现在额外假设
$$
0\ne w=Ju\in D_{\rm def}.
$$
由 $n_m\in N$ 及 (3.3)，
$$
\langle b_m,w\rangle
=\|w\|^2+\langle\varepsilon_m,w\rangle
\longrightarrow\|w\|^2.
\tag{5.1}
$$
内积采用第一变量线性的约定。因而存在 $M_0$，使所有 $m\ge M_0$ 均有
$$
|\langle b_m,w\rangle|\ge\tfrac12\|w\|^2.
\tag{5.2}
$$
特别，这些 $b_m$ 均非零。

由 (3.2)，向量 $b_m/\gamma_m$ 两两正交且范数为 $1$。又所有 $m\ge M$ 的支撑都在原总孔数至少 $q_M$ 的区域。对 $M\ge M_0$，Bessel 不等式给
$$
\sum_{m\ge M}
\frac{|\langle b_m,w\rangle|^2}{\gamma_m^2}
\le
\|\mathsf P_{\ge q_M}w\|^2
=\tau_{q_M-1}(w)^2.
$$
结合 (5.2)，得到
$$
\boxed{
\sum_{m\ge M}\frac1{\gamma_m(u)^2}
\le
\frac{4\,\tau_{q_M-1}(w)^2}{\|w\|^4},
\qquad M\ge M_0.
}
\tag{5.3}
$$
这是移动修复窗口的总正能量预算，强于只断言每一项修复发散。

再由 $\gamma_m\le(5/4)\|c_m\|$，得到原 Hilbert 修复范数的版本：
$$
\boxed{
\sum_{m\ge M}\frac1{\|c_m\|^2}
\le
\frac{25\,\tau_{q_M-1}(w)^2}{4\|w\|^4}.
}
\tag{5.4}
$$
特别，非零真缺陷必须满足
$$
\sum_{m\ge4}\frac1{1+\gamma_m(u)^2}<\infty.
\tag{5.5}
$$
有限个初始项当然不影响该结论。

上述不等式来自实际 $w\perp N$，不能改写成环境右逆的普遍下界，也没有对 $M^\perp$ 的坏向量作缺陷推断。

## 6. 最小范数的含义和剩余工作

$\gamma_m(u)$ 是固定真实低孔向量 $v_m$ 的最小高尾图能量。非空仿射集、范数等价、唯一最小元、准确支撑和其真实 $N$ 提升都已经支付。继续工作可以直接估计这个正变分量，不需要再选择一个任意代数修复后隐藏其范数。

当前仅有很粗的
$$
\gamma_m(u)\le\tfrac54 e^{351d_m^4}\|u\|.
$$
它不能推出 (4.3)。低层残量趋零、所有固定低孔坐标保持、进位修正趋零，同样不能替代这项估计。

若以后能对每个实际核向量证明倒数最小能量级数发散，则 (4.3) 会给 $N=M$。若存在非零真缺陷，其最小能量必须满足更强的 (5.3)—(5.5)。本稿把两种可能性之间的剩余问题放在一个真实的正能量级数上；尚未决定哪种可能性发生。

已使用的完整来源：
- [一次共同截平四次窗口](../results/R239-appendix-quartic-hole-window-by-common-flattening-and-exact-repair.md)；
- [R254 顶部精确修复与稳定像提升](../results/R254-appendix-exact-top-layer-repair-stable-lift-and-defect-norm-obstruction.md)；
- [R239 混合低孔正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)；
- [R239 首位小图与强耦合](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)。
