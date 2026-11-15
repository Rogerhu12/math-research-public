# R271 附录：原连续尾的秩一 Feshbach 下界与抛物窗口内真实三阶负部障碍

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文把既有[原 primitive 真逆八分之十五次下界](R271-appendix-normalized-creation-row-and-original-primitive-fifteen-eighths-lower-bound.md)中的同一个有界分析提升为完整 primitive Gram 的秩一算子下界，再接[原两下降的完整 Schur 恒等式](R239-appendix-two-descents-third-tail-and-paid-jet-anchor.md)。所得结论是原无限连续尾的真实三阶 jet 具有明确的大负二次型，而非仅有很大的绝对真幂逆。

在孔层 $n=q+1\asymp(m+1)^2$，该负部至少为常数乘 $(m+1)^{9/4}$，严格超过 $n\log n\log\log n$ 的量级。因此不能把[同一实际顶部负型恒等式](R271-appendix-same-top-sequential-projection-negative-form-and-complete-return-scalar.md)中尚欠的实际来源估计替换成整个 $\ker D^h$ 上相同量级的统一算子界。本文没有把所构造的负向量识别成实际 $u_Q(w)$ 的孔分量，也没有否定保同一 $w$、完整递推及两侧来源的联合预算。

## 1. 原算子、真逆与结论

固定整数 $m\ge5$，令
$$
D=D_m=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2},
$$
$$
S_t=\sum_{j\ge t}a_j^2,\qquad
W=\sum_{j\ge m}a_j^2n_j,\qquad n_j=E_j^*E_j.
\tag{1.1}
$$
全部级数在算子范数中收敛，且 $0\le W\le S_mI$。记原第 $r$ 孔层为 $\mathcal H_r$，
$$
D_r=D|_{\mathcal H_r},\qquad K_r=\ker D_r,\qquad
E_{j,r}=\ker D^j\cap\mathcal H_r,\qquad
U_{j,r}=E_{j,r}\ominus E_{j-1,r}.
\tag{1.2}
$$
这里 $E_{0,r}=0$，所有正交性均为原物理内积。

每个固定孔层的 $D_r$ 及所需有限真幂满射，因此其 MP 逆有界；本文不使用跨全部孔层的有界 MP。取整数 $q\ge2$，令
$$
k=\left\lfloor q^{3/4}/4\right\rfloor,\qquad
J=m+2q-k,\qquad
\theta=S_J(m+k)^4,\qquad R=e^{2/(m+k+1)}.
\tag{1.3}
$$
以下定量结论只要求
$$
k\ge4(m+1),\qquad m+k+1\ge512.
\tag{1.4}
$$
特别没有另行要求 $q\ge16m^2$。后者是旧稿获得其简洁常数的一组充分条件，本稿直接保全部参数构造。

在 $K_q$ 上定义真实 primitive MP Gram 及真实压缩创建 Gram
$$
\Gamma=(D_{q+1}^{\dagger}|_{K_q})^*
       (D_{q+1}^{\dagger}|_{K_q}),\qquad
H_0=P_{K_q}D_{q+1}D_{q+1}^*|_{K_q}.
\tag{1.5}
$$
这是先取完整层 MP 再压 primitive 的 $\Gamma$。本文从未用 $H_0^{-1}$ 代替 $\Gamma$。

**定理。** 在 (1.4) 下，原两下降常数满足
$$
\boxed{
C_*(q+1)
=\|H_0^{1/2}\Gamma H_0^{1/2}\|
\ge \frac{q^{15/4}}{4(m+1)^3}.
}
\tag{1.6}
$$
令 $n=q+1$，并对 $1\le j\le n$ 定义真正顺次投影
$$
P_{n,j}
=
D_n^\dagger D_{n-1}^\dagger\cdots D_{n-j+1}^\dagger
\,D_{n-j+1}\cdots D_n.
\tag{1.7}
$$
对任意整数 $3\le h\le n$，令
$$
\mathcal A_{h,n}=\sum_{j=1}^{h}P_{n,j}.
\tag{1.8}
$$
则
$$
\boxed{
\sup_{\substack{v\in E_{3,n}\cap K_n^\perp\\\|v\|=1}}
-\operatorname{Re}\langle\mathcal A_{h,n}v,v\rangle
=
\frac{\sqrt{C_*(n)}-3}{2}
\ge
\frac{q^{15/8}}{4(m+1)^{3/2}}-\frac32.
}
\tag{1.9}
$$
若左侧为负，等式仍是相应二次型的上确界；其正部才是该压缩的 Hermitian 负部范数。在本稿的渐近应用中右侧严格为正。

## 2. 保全部中间位的分析行

本节复写旧八分之十五次稿中所需的原空间构造，以钉住算子下界的共同源。

把原尾分成：

- 最初 $k$ 个实际位 $[m,m+k)$；
- 中间 $q-k$ 个相邻暗对，覆盖 $[m+k,J)$；
- 完整无限远尾 $[J,\infty)$。

对中间一对实际权 $\alpha,\beta>0$，置
$$
h_{\alpha,\beta}
=\frac{\beta|10\rangle-\alpha|01\rangle}
{\sqrt{\alpha^2+\beta^2}},\qquad
g_{\alpha,\beta}
=\frac{\alpha|10\rangle-\beta|01\rangle}
{\sqrt{\alpha^2+\beta^2}},\qquad
\rho_{\alpha,\beta}=\frac{2\alpha\beta}{\alpha^2+\beta^2}.
\tag{2.1}
$$
该对的删除消去 $h_{\alpha,\beta}$；该对的创建消去 $g_{\alpha,\beta}$。因此行
$\langle g_{\alpha,\beta}/\rho_{\alpha,\beta},\cdot\rangle$ 与删除精确交织到零，且在 $h_{\alpha,\beta}$ 上取值一。

记
$$
h_{\rm gap}=\bigotimes h_{\alpha,\beta},\qquad
g_{\rm gap}^{\sharp}=\bigotimes(g_{\alpha,\beta}/\rho_{\alpha,\beta}).
$$
从实际相邻权的
$$
\rho_{\alpha,\beta}^{-1}
=\cosh\!\left(2\log(1+1/(j+1))\right)
$$
及 $\log\cosh u\le u^2/2$，得到
$$
\|g_{\rm gap}^{\sharp}\|\le R=e^{2/(m+k+1)}.
\tag{2.2}
$$
这是有界斜分析的真实成本，不是把这些位置删去。

在远尾令 $e_r$ 为平方权的初等对称和，并置
$$
u_r=e_r^{-1/2}\sum_{\substack{I\subseteq[J,\infty)\\|I|=r}}
a_I|I\rangle,\qquad a_I=\prod_{i\in I}a_i,\qquad u_0=\Omega.
$$
这些单位向量满足
$$
D_J^*u_{r-1}=c_ru_r,\qquad
c_r=r\sqrt{e_r/e_{r-1}},\qquad
\langle u_{r-1},D_J(\cdot)\rangle
=c_r\langle u_r,\cdot\rangle.
\tag{2.3}
$$
最后一个等式作用于整个真实孔层。并且
$$
(r+1)e_{r+1}\le S_Je_r,\qquad
\|D_J^su_k\|^2\le\frac{k!}{(k-s)!}S_J^s
\quad(0\le s\le k).
\tag{2.4}
$$

保最初 $k$ 位不动，先施加中间行 $g_{\rm gap}^{\sharp}$，再在远尾使用各层单位行 $u_r$。这样在原第 $q+t$ 层得到算子 $\mathcal T_t$，其值域是“原 $k$ 强位加一个标量模”的总次数 $k+t$ 层。若标量模删除为 $C\mathbf e_r=c_r\mathbf e_{r-1}$，模型删除为
$$
\mathcal L=D_{\rm hd}+C,
$$
则
$$
\|\mathcal T_t\|\le R,\qquad
\mathcal T_{t-1}D=\mathcal L\mathcal T_t.
\tag{2.5}
$$
所有中间位与无限尾均在这个有界全层分析中保留。

## 3. 真 primitive 的秩一 Feshbach 下界

按强位子集 $I\subseteq[k]$ 定义原向量
$$
F=
\sum_{I\subseteq[k]}
(-1)^{|I|}\frac{(k-|I|)!}{k!}\,
a_I^{-1}|I\rangle\otimes D_J^{|I|}u_k.
\tag{3.1}
$$
逐个强位标签中，强位删除项与远尾删除项准确抵消，所以
$$
(D_{\rm hd}+D_J)F=0.
$$
由不同强位标签正交、(2.4) 及
$e_s((a_i^{-2})_{i\in[k]})\le\binom ks(m+k)^{4s}$，
$$
1\le\|F\|^2
\le\sum_{s=0}^k\frac{\theta^s}{s!}
\le e^\theta.
\tag{3.2}
$$
因此
$$
\widetilde f=F\otimes h_{\rm gap}\in K_q,\qquad
1\le\|\widetilde f\|^2\le e^\theta.
\tag{3.3}
$$
张量位置仍按强位、中间位、远尾读取。

令
$$
h_0=|\varnothing\rangle_{\rm hd}
       \otimes g_{\rm gap}^{\sharp}\otimes u_k,
\qquad
\ell=P_{K_q}h_0.
\tag{3.4}
$$
则 $\|h_0\|\le R$、$\langle h_0,\widetilde f\rangle=1$。从真正交投影得到
$$
\boxed{
\|\ell\|^2\ge e^{-\theta},\qquad
\|h_0-\ell\|^2\le R^2-e^{-\theta}.
}
\tag{3.5}
$$

模型次数 $k$ 的空间以全部强位子集为索引；次数 $k-1$ 缺少全强位占据标签。其删除矩阵的每个非顶标签都有严格正标量对角 $c_{k-|I|}$，故该矩阵满行秩、核恰一维。记唯一空强位坐标为一的核向量为 $\omega$。由 (2.5)，对任意 $f\in K_q$，
$$
\mathcal T_0f=\langle h_0,f\rangle\omega
=\langle\ell,f\rangle\omega.
\tag{3.6}
$$
这里的线性行方向依所用内积约定读取；后文只用其绝对值平方。

模型次数 $k+1$ 到 $k$ 的删除是三角可逆方阵。有限展开
$$
\mathcal L^{-1}
=\sum_{s=0}^{k}(-1)^sC^{-s-1}D_{\rm hd}^s
$$
给准确空强位坐标
$$
(\mathcal L^{-1}\omega)_{\varnothing}
=\frac{k+1}{c_{k+1}}
=\sqrt{\frac{e_k}{e_{k+1}}}.
\tag{3.7}
$$
例如按 $|I|=s$ 汇总时，$\binom ks$、$s!$ 与 $(k-s)!/k!$ 相乘为一，每个 $s$ 都贡献 $1/c_{k+1}$。该式是整个模型方阵的逆，不是受限试探原像。

对任意原 $u$ 满足 $Du=f\in K_q$，(2.5)–(3.7) 迫
$$
R^2\|u\|^2
\ge \frac{e_k}{e_{k+1}}|\langle\ell,f\rangle|^2.
$$
对全部原像取最小，得到共同源上的 Loewner 不等式
$$
\boxed{
\Gamma
\succeq\frac1{R^2}\frac{e_k}{e_{k+1}}\,
|\ell\rangle\langle\ell|
\succeq \frac{k+1}{R^2S_J}\,
|\ell\rangle\langle\ell|.
}
\tag{3.8}
$$
这一步比单个单位源的逆范数下界保留更多信息：同一个 Riesz 向量 $\ell$ 出现在完整 primitive Gram 的秩一算子下界中。

## 4. 该 Riesz 向量具有真实的大创建能量

primitive 上的原交换子给
$$
H_0=S_mI-2P_{K_q}W|_{K_q}\succeq0.
\tag{4.1}
$$
$h_0$ 完全不占最初 $k$ 个强位，因此
$$
\langle Wh_0,h_0\rangle\le R^2S_{m+k}.
$$
令 $e=h_0-\ell$。用 $0\le W\le S_mI$ 和 (3.5)，
$$
\begin{aligned}
\langle W\ell,\ell\rangle
&\le2\langle Wh_0,h_0\rangle+2\langle We,e\rangle\\
&\le2R^2S_{m+k}+2S_m(R^2-e^{-\theta}).
\end{aligned}
\tag{4.2}
$$
从而
$$
\langle H_0\ell,\ell\rangle
\ge
S_m\left[
5e^{-\theta}-4R^2\left(1+\frac{S_{m+k}}{S_m}\right)
\right].
\tag{4.3}
$$

现在核全部常数。(1.4) 给 $m\le k$、$k\le q/4$，故
$$
J\ge7q/4,\qquad m+k\le2k\le q^{3/4}/2,
$$
$$
\theta\le\frac4{1029}<\frac1{64}.
\tag{4.4}
$$
又由 $m+k+1\ge512$，
$$
R^2\le e^{1/128}\le\frac{128}{127}<\frac{65}{64}.
$$
原尾积分比较及 $k\ge4(m+1)$ 给
$$
\frac{S_{m+k}}{S_m}
\le\left(\frac{m+1}{m+k}\right)^3\le\frac1{64}.
\tag{4.5}
$$
因此 (4.3) 中的括号至少
$$
5\frac{63}{64}
-4\frac{65}{64}\frac{65}{64}
=\frac{3260}{4096}>\frac12,
$$
即
$$
\boxed{\langle H_0\ell,\ell\rangle\ge S_m/2.}
\tag{4.6}
$$
这里只估真实 bounded 占据算子 $W$，没有用可能放大的环境 $D^*$ 范数去乘投影误差。

## 5. 经完整两下降 Schur 强迫真实回返

为核清逆和出生的顺序，置 $n=q+1$，并定义
$$
A_1=D_n|_{U_{2,n}}:U_{2,n}\to K_q,\qquad
B_2=P_{K_q}D_n|_{U_{3,n}}:U_{3,n}\to K_q.
$$
$A_1$ 为有界双射，$A_1^{-1}=D_n^\dagger|_{K_q}$。对 $f\in K_q$，
$$
D^2D^*f=-2D_3f,\qquad
D_3=\sum_{j\ge m}a_j^3E_j,\qquad DD_3=D_3D.
$$
故 $D^*f\in U_{2,n}\oplus U_{3,n}$，没有更高出生遗漏。因此
$$
H_0=A_1A_1^*+B_2B_2^*
=\Gamma^{-1}+B_2B_2^*.
\tag{5.1}
$$
完整顺次二步／真二次幂比例恰为
$$
C_*(n)=1+\|A_1^{-1}B_2\|^2
=\|\Gamma^{1/2}H_0\Gamma^{1/2}\|.
\tag{5.2}
$$

下面不用“$\Gamma$ 大则 $\Gamma^{1/2}$ 可直接作 Loewner 替换”这类错误操作。两个正算子
$\Gamma^{1/2}H_0\Gamma^{1/2}$ 与
$H_0^{1/2}\Gamma H_0^{1/2}$ 分别是同一个有界算子的 $T^*T$ 与 $TT^*$，故范数相同。对后者直接使用 (3.8) 的合同，再用 (4.6)，得
$$
C_*(n)
\ge
\frac{k+1}{R^2S_J}\langle H_0\ell,\ell\rangle
\ge\frac{(k+1)S_m}{2R^2S_J}
\ge\frac{(k+1)J^3}{4(m+1)^3}.
\tag{5.3}
$$
最后用 $k+1>q^{3/4}/4$ 与 $J\ge7q/4$，
$$
C_*(q+1)>
\frac{343}{1024}\frac{q^{15/4}}{(m+1)^3}
\ge\frac{q^{15/4}}{4(m+1)^3}.
$$
这证明 (1.6)。

旧分析 $\mathcal T_t$ 仍然消去相应层的 $\ker D^t$，这个事实没有改变。新结论不是把同一行直接作用在高返回上；它经过其 primitive Riesz 向量、真实创建能量及完整 Schur 身份 (5.1)–(5.2)，从而迫出另一个真实回返块的下界。

## 6. 负二次型的准确位置与全部定义域

记 $K=A_1^{-1}B_2:U_{3,n}\to U_{2,n}$。在物理正交分解
$U_{2,n}\oplus U_{3,n}\subset E_{3,n}\cap K_n^\perp$ 上，
$$
P_{n,1}=I,\qquad
P_{n,2}=
\begin{pmatrix}0&-K\\0&I\end{pmatrix}.
\tag{6.1}
$$
第二式来自准确顺次／真幂分裂：对 $v\in U_{3,n}$，
$D_n^\dagger D_{n-1}^\dagger D^2v=v-A_1^{-1}B_2v$。
对 $v\in U_{2,n}$，$D^2v=0$。全部 $j\ge3$ 则在整个 $E_{3,n}$ 上为零。因此对每个 $h\ge3$，
$$
\mathcal A_{h,n}|_{U_{2,n}\oplus U_{3,n}}
=
\begin{pmatrix}I&-K\\0&2I\end{pmatrix}.
\tag{6.2}
$$
此处是 $\mathfrak N_{h,n}-I$，不是包含 $P_{n,0}=I$ 的完整次数算子本身。

其 Hermitian 压缩为
$$
\begin{pmatrix}I&-K/2\\-K^*/2&2I\end{pmatrix}.
$$
对 $K$ 的近极值奇异向量取相应两维实系数，或直接求该块的谱下确界，可得
$$
\inf_{\|v\|=1,\ v\in U_{2,n}\oplus U_{3,n}}
\operatorname{Re}\langle\mathcal A_{h,n}v,v\rangle
=\frac{3-\sqrt{1+\|K\|^2}}2.
\tag{6.3}
$$
即使范数不被某个向量取到，任意接近该下确界的单位向量都在上述两个真实正交子空间内。固定孔层的各个 MP 有界，所以它们全部属于 (1.7) 的完整自然定义域；无需任何跨层无界逆的域假设。结合 (5.2) 得 (1.9)。

## 7. 抛物窗口的量词与实际同源问题的剩余范围

固定任意 $\kappa>0$，令 $m\to\infty$、$q=\lfloor\kappa(m+1)^2\rfloor$。则
$$
\frac{k}{m+1}\sim\frac{\kappa^{3/4}}4(m+1)^{1/2}\longrightarrow\infty,
$$
所以 (1.4) 最终成立，不论 $\kappa$ 是否大于旧展示条件中的 16。由 (1.9)，
$$
\sup_{\substack{v\in E_{3,q+1}\cap K_{q+1}^\perp\\\|v\|=1}}
-\operatorname{Re}\langle\mathcal A_{h,q+1}v,v\rangle
\ge c_\kappa(m+1)^{9/4}
\tag{7.1}
$$
对充分大 $m$ 成立，且对所有 $h\ge3$ 一致。因此该量除以
$q\log(q+2)\log\log(q+3)$ 仍趋于无穷。

在实际 cut 区间 $a\le p\le b$，同顶部合并算子是
$$
\mathscr A_n=
\sum_{\substack{1\le j\le h\\a\le n-j\le b}}P_{n,j}.
\tag{7.2}
$$
只有在 $a+h\le n\le b+1$ 的内部层，(7.2) 才恰为完整和 $\mathcal A_{h,n}$。本文仅在这些内部层援用 (7.1)，没有丢掉两端 partial sums；若拟对全部孔向量族作直接和算子估计，可把其他层置零，内部层已足以排除上述统一费用。

对强位并头后的原远尾，只需把本稿尾起点 $m$ 换成该原远尾的实际起点 $x$；连续权、全部无限后尾及原物理内积均相同。因而 $Q\asymp x^2$ 的实际尺度不能免费获得整个 $E_h$ 上的 $O(Q)$、$O(Q\log Q\log\log Q)$ 或固定常数倍 $Q^2/x^2$ 负部上界。

但真实来源还同时满足
$$
Cu_n+Du_{n+1}=0,
$$
全部有限头旗、完整左右来源与
$u_Q=P_{V_Q}w-P_{K_Q}w$ 的同一个 $w$ 条件。本稿的近极值负向量尚未被识别成这个真实族中的孔分量。因此：

- 不能把 (7.1) 当成实际同源负型充分条件的反例；
- 不能据此把原无权 $N=M$ 或普通 ISP 判为不成立；
- 后续若仍使用负型路线，必须保实际递推／来源，或从全短核中明确剥离上述完整 Schur 负方向；仅靠逐层所有 $E_h$ 的统一负部已不足。

新关闭的是原模型中这一具体“全源替代”路线，而不是实际同一 $w$ 的联合预算。
