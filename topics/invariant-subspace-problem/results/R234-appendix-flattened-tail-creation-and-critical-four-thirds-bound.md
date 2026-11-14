# R234第三附录：截平纯尾权与临界4/3次右逆成本

日期：2026-11-13（UTC+8）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：以下全部结论已证明，主问题未完成。

这里的临界次数权是 $e^{c(q+1)^{4/3}}$。本文证明一个明确的大常数 $c$ 可用，**没有证明所有任意小的临界 $c>0$ 可用**。

本文替换 [R234](R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) 的纯尾逐层右逆，故不是对原右逆的单纯重新估计。新纯尾右逆一般不保持有限位置支撑；本文逐处说明这不妨碍真实误差、有限测试及核差归属。

## 1. 截平权与整个纯孔层上的创建下界

固定尾起点 $m\ge1$、孔次数 $s\ge0$。令
$$
D_{\ge m}=\sum_{j\ge m}(j+1)^{-2}E_j,
\qquad C_a=D_{\ge m}^*|_{H_{\ge m,s}}.
$$
取整数
$$
J=2m+4s+4,
\qquad b_j=\min\{(j+1)^{-2},J^{-2}\}\quad(j\ge m),
$$
并记 $C_b=(\sum_{j\ge m}b_jE_j)^*|_{H_{\ge m,s}}$。
这些是整个允许无限位置的 Hilbert 孔层上的有界算子。

真实纯矩阵 CCR 给
$$
C_b^*C_b-C_bC_b^*
=\sum_{j\ge m}b_j^2(I-2E_j^*E_j).
$$
此处第二项按其自然相邻次数理解。在第 $s$ 层，孔占据总数恰为 $s$，所以
$$
C_b^*C_b\ge
\left(\sum_{j\ge m}b_j^2-2s\max_jb_j^2\right)I.
$$
前 $J-m$ 个权都为 $J^{-2}$，故
$$
\sum_{j\ge m}b_j^2-2s\max_jb_j^2
\ge(J-m-2s)J^{-4}
=(m+2s+4)J^{-4}\ge\frac1{2J^3}.
\tag{1.1}
$$
这也付清 $m\gg s$ 的情形；并未把仅有 $s+1$ 项的平顶当作 $J^{-3}$ 的尾平方和。
因此存在左逆
$$
L_b=(C_b^*C_b)^{-1}C_b^*,\qquad
L_bC_b=I,\qquad \|L_b\|\le\sqrt2\,J^{3/2}.
\tag{1.2}
$$

令 $\rho_j=(j+1)^{-2}/b_j\ge1$。它只在有限多个位置不等于 $1$。在每个孔层定义正对角乘子
$$
S_t e_F=\left(\prod_{j\in F}\rho_j\right)e_F,
\qquad |F|=t.
$$
直接比较每一次创建的系数，有准确恒等式
$$
C_aS_s=S_{s+1}C_b.
\tag{1.3}
$$
同时 $\|S_{s+1}^{-1}\|\le1$。
若 $s\ge1$，最大的 $s$ 位乘积在最小的 $s$ 个位置取得，因此
$$
\|S_s\|\le
\left(\frac{J^s}{\prod_{r=1}^s(m+r)}\right)^2.
$$
由对数的积分下界，
$$
\prod_{r=1}^s(m+r)\ge\left(\frac{m+s}{e}\right)^s.
$$
因 $J\le8(m+s)$，
$$
\boxed{\|S_s\|\le(8e)^{2s}\le512^s.}
\tag{1.4}
$$
$s=0$ 时同式由 $S_0=I$ 成立。

现在取
$$
L_a=S_sL_bS_{s+1}^{-1}.
$$
(1.3) 给 $L_aC_a=I$。特别，范数只付一个 $S_s$，不会多付 $S_{s+1}$。取伴随，得到新右逆
$$
\widehat Q_{m,s}=L_a^*:
H_{\ge m,s}\longrightarrow H_{\ge m,s+1},
\qquad D_{\ge m}\widehat Q_{m,s}=I,
$$
以及
$$
\boxed{
\|\widehat Q_{m,s}\|
\le\sqrt2\,J^{3/2}512^s
\le12\,512^s(m+s+1)^{3/2}.
}
\tag{1.5}
$$
所以旧的 $\exp(O(s\log(m+s)))$ 预算可以换成 $\exp(O(s)+O(\log(m+s)))$。

$L_b$ 中的正算子逆通常作用于无限多个位置。本文**不主张** $\widehat Q_{m,s}$ 保持有限位置支撑；它严格保持的是输出次数恰好增加一。

最后，(1.5) 不超过 R234 的旧统一预算：
$$
12\,512^s(m+s+1)^{3/2}
\le[10000(m+s+1)^2]^{s+1}.
\tag{1.6}
$$
这将允许把原本依赖全空间范数与次数的真实 carry 估计逐项重新套用。

## 2. 新的有限头模型右逆及完整实际误差

保持 R234 的头选择
$$
m(q)=10+\lceil\log_2(q+1)\rceil,
\qquad d(q)=2^{m(q)},
\qquad1024(q+1)\le d(q)<2048(q+1).
$$
将 (1.5) 的右逆按尾次数拼成 $\widehat{\mathcal Q}_m$。在有限头张量上恒等作用，故与 $T_m$ 交换。定义新算子
$$
\widehat R_q
=\left.\sum_{k=0}^{d(q)-1}(-T_m)^k
\widehat{\mathcal Q}_m^{k+1}\right|_{H_q}.
\tag{2.1}
$$
每项在所需的有限孔次数层之间有界。望远镜消去和 $T_m^d=0$ 给
$$
T^{[m]}\widehat R_q=I|_{H_q}.
\tag{2.2}
$$
输出次数不超过
$$
r_q=q+m+d,
\qquad r_q+1\le4096(q+1).
\tag{2.3}
$$
这不依赖输出的最大位置是否有限。

由 (1.6)，R234 的旧预算 $M_q$ 仍是 $\|\widehat R_q\|$ 的上界，故
$$
\log\|\widehat R_q\|\le\log M_q\le d(q)^3.
\tag{2.4}
$$
真实误差仍为
$$
T\widehat R_q-I=\sum_{L\ge m}K_L\widehat R_q,
\qquad \|K_L\|\le52e^{-770\,16^{L-1}}.
$$
$K_L$ 只作用在前 $L+1$ 位，故第 $L=m+t$ 项的次数不超过 $r_q+m+t+1$。由 (2.3)、(2.4)，在原三次权空间中，
$$
\|K_{m+t}\widehat R_qv\|_{X_{1,3}}
\le52M_qe^{-770\,16^{m+t-1}}
\sqrt{r_q+m+t+2}\,e^{(r_q+m+t+2)^3}\|v\|.
$$
这里 $r_q+m+t+2\le3d+t$，且
$$
770\,16^{m+t-1}=48.125d^4\,16^t.
$$
完全按原数值估计，正指数不超过 $d^3+2(3d+t)^3\le55d^3\,16^t$。因 $d\ge1024$，得到
$$
\boxed{
\|(T\widehat R_q-I)v\|_{X_{1,3}}
\le2e^{-40d(q)^4}\|v\|.
}
\tag{2.5}
$$
这样重新验证了全部次数误差；没有以无权小范数替代次数正则化，也没有使用旧右逆的有限位置性质。

## 3. 新右逆的临界成本：$\exp(O(q^{4/3}))$

沿用已证真实四次头幂：
$$
\|T_m^k\|\le6^k,
\qquad
\|T_m^k\|\le6^ke^{-\gamma k^4}\quad(k\ge2m),
\qquad \gamma=770/16^4>1/100.
\tag{3.1}
$$
这里 $m\ge10$，所以已满足四次界原本的 $k\ge16$ 条件。

置 $x=q+1\ge1$。由 (1.5)，对于每个 $0\le k<d$，
$$
\begin{aligned}
\log\|\widehat{\mathcal Q}_m^{k+1}|_{H_{\le q}\ {\rm tail}}\|
&\le(k+1)\{\log12+(q+k)\log512
+\tfrac32\log(m+q+k+1)\}\\
&\le10(k+1)(x+k+m).
\end{aligned}
\tag{3.2}
$$
第二行只用 $\log12<3$、$\log512<7$ 和 $\log y\le y$。加上 $k\log6$ 后，可统一用
$12(k+1)(x+k+m)$。

### 3.1 低幂 $k<2m$

由 $m\le11+2\log x\le24x^{1/3}$，有
$$
k+1\le2m\le48x^{1/3},\qquad
x+k+m\le x+3m\le73x.
$$
故低幂每项的对数范数不超过
$$
42048x^{4/3}.
\tag{3.3}
$$

### 3.2 高幂 $k\ge2m$

此时 $m\le k/2$，所以由 (3.1)、(3.2)，对数范数不超过
$$
12x+12xk+36k^2-\gamma k^4.
$$
准确的两次实变量优化给
$$
36k^2-\frac\gamma2k^4\le\frac{648}{\gamma}<64800,
$$
$$
12xk-\frac\gamma2k^4
\le\frac{3\,12^{4/3}}{4^{4/3}(\gamma/2)^{1/3}}x^{4/3}
<100x^{4/3}.
$$
所以高幂每项的对数范数不超过 $64912x^{4/3}$。
最后的项数只再付
$$
\log d=m\log2<17x^{4/3}.
$$
因此，一个方便的完全统一常数为
$$
\boxed{
\|\widehat R_q\|\le e^{K(q+1)^{4/3}},
\qquad K=100000.
}
\tag{3.4}
$$
本估计直接保留了 $qk+k^2$ 再与四次衰减优化，没有先用 $k<d$ 把常数放大成 $d$ 的幂。

## 4. 一个明确的大常数临界权上的真实有界右逆

记
$$
\beta=4/3,\qquad C=200000,
$$
$$
X_{C,\beta}=
\left\{f:\sum_{q\ge0}e^{C(q+1)^\beta}\|\mathsf P_qf\|<\infty\right\}.
$$
由 (3.4)，$\widehat R=\sum_q\widehat R_q\mathsf P_q$ 有界
$X_{C,\beta}\to H_-$。

还必须在此较大临界权中重付实际误差，而不能仅声称它小于原三次权。对 $d\ge1024$，
$$
C\le d^{8/3},\qquad
(3d+t)^{4/3}\le(3d)^{4/3}16^t.
$$
于是
$$
C(3d+t)^{4/3}\le5d^4\,16^t.
$$
(2.4) 的 $d^3$，以及 $\log52+\tfrac12\log(3d+t)$，合计至多 $2d^3\,16^t$。
因此每个真实误差项的对数范数不超过
$$
-48.125d^4\,16^t+5d^4\,16^t+2d^3\,16^t
\le-40d^4\,16^t.
$$
所以
$$
\|(T\widehat R_q-I)v\|_{X_{C,\beta}}
\le2e^{-40d(q)^4}\|v\|.
\tag{4.1}
$$
定义 $\widehat E=T\widehat R-I$，按逐次数和理解。由 (4.1)，
$$
\|\widehat E\|_{X_{C,\beta}\to X_{C,\beta}}<1/4.
$$
于是
$$
\boxed{
\widehat G=\widehat R(I+\widehat E)^{-1}:
X_{C,\beta}\to H_-,\qquad T\widehat G=I.
}
\tag{4.2}
$$
这是实际 Hilbert 向量的右逆。

## 5. 新右逆的有限输入核差，及真正缺陷的临界形式原像界

设
$$
M=\ker T,\qquad N=\overline{BM},\qquad w\in W=M\ominus N.
$$
已有形式三角原像 $T^*h=w$，并且对有限位置测试 $v$，
$$
\langle h,v\rangle=\langle w,J_Tv\rangle,
\qquad TJ_Tv=v,
$$
其中 $J_Tv$ 是有限位置解。内积按仓库约定对第一变量线性。

新 $\widehat Q$ 不保有限位置，故不能把它造成的核差直接认作旧标准构造。以下用已经证明的三次正则核饱和付清这一步。

由 (2.5)，$\widehat E$ 实际延拓成有界正则化映射
$$
\widehat E:H_-\longrightarrow X_{1,3}.
\tag{5.1}
$$
确实，若 $\delta_q=2e^{-40d(q)^4}$，则
$$
\|\widehat E f\|_{X_{1,3}}
\le\sum_q\delta_q\|\mathsf P_qf\|
\le\left(\sum_q\delta_q^2\right)^{1/2}\|f\|.
$$
这与 (4.1) 的定义在公共域上一致。

对有限位置 $v$，令 $y=(I+\widehat E)^{-1}v\in X_{C,\beta}\subset H_-$。
由 $y=v-\widehat Ey$ 和 (5.1)，得到 $y\in X_{1,3}$。
另一方面，(2.3)、(3.4) 给
$$
\widehat R:X_{1,3}\longrightarrow X_{\gamma_0,3}
\quad\hbox{有界},\qquad
\gamma_0=(4\cdot4096^3)^{-1}.
\tag{5.2}
$$
证明只需逐层使用
$$
\|\widehat R_qv\|_{X_{\gamma_0,3}}
\le\sqrt{r_q+1}\,
\exp\!\left(\tfrac14(q+1)^3+K(q+1)^{4/3}\right)\|v\|,
$$
其与输入权 $e^{(q+1)^3}$ 的比值有有限上界。
所以 $\widehat Gv\in X_{\gamma_0,3}$。两种 $\widehat R y$ 的求和都在 $H_-$ 中收敛，故确为同一个向量。

于是
$$
\widehat Gv-J_Tv\in M\cap X_{\gamma_0,3}\subset N,
\tag{5.3}
$$
最后一步正是已经证明的 [R234第一附录](R234-appendix-fixed-hole-primitives-and-cubic-regular-saturation.md) 三次正则核饱和；没有对临界权作循环使用。
因此有限测试配对成为
$$
\langle h,v\rangle=\langle w,\widehat Gv\rangle.
$$
固定孔层中的有限位置向量稠密，故它给实际 Hilbert 伴随表达
$$
\boxed{
 h_q=(\widehat G|_{H_q})^*w,\qquad
 \|h_q\|\le\|\widehat G\|e^{C(q+1)^{4/3}}\|w\|.
}
\tag{5.4}
$$
这把此前每个 $p>4/3$ 的估计收紧到**一个固定大常数的临界 $p=4/3$**。它仍不推出 $\sum_q\|h_q\|^2<\infty$。

## 6. 临界正则核饱和与真实缺陷的次数尾

令 $X_{C,\beta}^+$ 的权为 $e^{C(q+2)^\beta}$。
真实恒等式 $N_iE_i^*=I-E_i^*E_i$ 使
$$
N_i\widehat GE_i^*:X_{C,\beta}^+\to H_-
$$
一致有界，范数至多 $\|\widehat G\|$。
其弱算子聚点 $\widehat C$ 满足
$$
T\widehat C=I,
\qquad
\widehat Cv-J_Tv\in N\quad\hbox{对有限位置 }v.
\tag{6.1}
$$
这里第二式直接来自：充分高 $i$ 时，$N_iE_i^*v=v$，并且
$N_i\widehat GE_i^*v$ 与 $J_Tv$ 均属于 $\operatorname{Ran}B$；它们的差在
$M\cap\operatorname{Ran}B\subset N$。弱极限保持闭子空间 $N$。
故有限位置 $x$ 满足 $x-\widehat CTx\in N$。

对每个 $a>C$，真实局部 carry 分解给
$$
T:X_{a,\beta}\to X_{C,\beta}^+
\quad\hbox{有界}.
\tag{6.2}
$$
具体地，$K_L$ 最多改 $L+1$ 孔，且对固定 $a>C$，
$$
\sup_q\sqrt{q+L+2}\,
 e^{C(q+L+3)^\beta-a(q+1)^\beta}
\le A e^{A'(L+2)^\beta}.
$$
这由 $C<C'<a$ 吸收平方根，再把凸增长分成 $q$ 与 $L$ 两段得到；真实
$e^{-77016^{L-1}}$ 支付全部 $L$ 和。
有限位置逼近及 (6.1)、(6.2) 因而给
$$
\boxed{M\cap X_{a,4/3}\subset N\quad\text{对每个 }a>C.}
\tag{6.3}
$$
没有证明它对全部任意小 $a>0$ 成立，也没有证明这些正则核向量在 $M$ 中稠密。

最后设 $\|w\|=1$，令
$$
u_q=\mathsf P_{\le q}w,\qquad
\tau_q=\|\mathsf P_{>q}w\|,\qquad q\ge1.
$$
固定有限次数中的有限位置逼近，可用 (6.2) 支付 $T$ 的连续性，所以
$u_q-\widehat CTu_q\in N$。因此
$$
\|u_q\|^2\le\|\widehat C\|\,\|Tu_q\|_{X_{C,\beta}^+}.
$$
输出次数不超过 $2q$ 的部分，由 $Tw=0$ 有界为
$$
6\sqrt{2q+1}\,e^{C(2q+2)^\beta}\tau_q.
$$
输出次数大于 $2q$ 时，纯删除 $D$ 无贡献，而局部 $K_L$ 必须有 $L\ge q$。因此高输出余量至多
$$
\Delta_q=52\sum_{L\ge q}\sqrt{q+L+2}\,
 e^{-77016^{L-1}+C(q+L+3)^\beta}\longrightarrow0.
$$
因 $q\le L$，指数中的正项只为 $O(L^{4/3})$，故此极限严格成立。
当 $q$ 足够大，$\|u_q\|^2\ge1/2$ 且
$\|\widehat G\|\Delta_q\le1/4$，得到
$$
\boxed{
\tau_q\ge
\frac{e^{-C(2q+2)^{4/3}}}
{24\|\widehat G\|\sqrt{2q+1}}.
}
\tag{6.4}
$$
特别，任何非零真实缺陷都满足
$$
\boxed{-\log\tau_q=O(q^{4/3}).}
\tag{6.5}
$$
这个结论仍允许大量平方可和的慢尾；不排除 $W$。

## 7. 准确结论与尚缺的能量步骤

本文实际得到：纯尾右逆的次数成本从 $\exp(O(q\log q))$ 降到 $\exp(O(q))$；重新构造的真实逐层右逆成本从 $\exp(O((q\log q)^{4/3}))$ 降到 $\exp(O(q^{4/3}))$；一个大常数临界权上的实际右逆、其有限测试核差、形式原像整层 Hilbert 表达，以及临界正则核饱和和缺陷次数尾下界均已证明。

新左逆不是有限位置算子，此点未被隐藏或借用。原三次饱和仅在第 5 节用来合法识别新右逆的有限测试配对。

仍未证明全部次数的无权平方和，也未获得跨次数能量通量为零。$N=M$ 与本题原 Hilbert 不变子空间目标均未完成。
