# R236 附录：原正交像投影的交换子范数距离与真实 dyadic 共轭成本

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；主会话全文复核，central_review 独立复核真实柱、逆域及矩阵范数；AI-assisted，GPT-6 Astra Pro。

**状态：以下定量界完整证明。** 在原 Haar 表示中，有限纯 creation 和的高次像投影可以强趋于恒等，但当提升阶数占块宽的固定比例时，它与实际交换子代数 $A'$ 保持一个明确的正范数距离。通过实际 $A^{2^\ell}$ 将这个投影移入配对，虽对每个固定有限块确实有界，其范数却含不可忽略的实际进位权比。结论同时适用于任意非零复权，以及把固定多位集合视为一个 creation 块的平衡方案。

本文只限制两个具体接口：对原正交像投影的算子范数提升，以及以 $A^{-2^\ell}P A^{2^\ell}$ 实现的实际左侧移入。它不排除其他配对、其他非正交测试或所有可能的伪逆方法，不将纯有限块算子当成 $A'$ 元素。

## 1. 原物理柱与准确的 dyadic 权

沿用实际 Haar 空间
$$
H=L^2(\mathbb Z_2)
=\bigotimes_{j\ge0}(\mathbb C^2,\Omega_+),
\qquad
\Omega_+=(e_0+e_1)/\sqrt2.
$$
原实际关系为
$$
A^{2^\ell}=d_\ell I_{<\ell}\otimes N_\ell,\qquad d_\ell>0,
$$
$$
N_j=E_j+\eta_j E_j^*N_{j+1},\qquad
E_j=|1\rangle\langle0|,\qquad
0<\eta_j\le e^{-770\,16^j}<1.
\tag{1.1}
$$
这些是 [R253 的实际尾分解](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)
及原真实局部递推；不使用边界表示运输未知交换子。

对 $M\ge1$ 和 $0\le b<2^M$，记归一化柱
$$
e_b^{[M]}=2^{M/2}\mathbf1_{\{y\bmod2^M=b\}}.
$$
它等于前 $M$ 位的物理基向量与尾真空的张量积。

若 $b$ 被 $2^\ell$ 整除且 $b>0$，令
$j=v_2(b)<M$。反复使用 (1.1)，有准确等式
$$
\boxed{
A^{2^\ell}e_{b-2^\ell}^{[M]}
=w_{\ell,j}e_b^{[M]},
\qquad
(A^{2^\ell})^*e_b^{[M]}
=w_{\ell,j}e_{b-2^\ell}^{[M]},
}
\tag{1.2}
$$
$$
w_{\ell,j}=d_\ell\prod_{s=\ell}^{j-1}\eta_s,
\qquad \text{空积为 }1.
\tag{1.3}
$$
确实，输入的第 $\ell,\ldots,j-1$ 位都是 $1$，
递推在这些位使用 carry 项；第 $j$ 位为 $0$，
在那里使用 $E_j$ 并停止。伴随方向从输出的第一个 $1$ 反向停止。
因此两式的尾因子都准确保持，未留下未估计的尾项。

特别，对 $j\ge m\ge\ell$，
$$
\frac{w_{\ell,j}}{w_{\ell,m}}
=\prod_{s=m}^{j-1}\eta_s.
\tag{1.4}
$$
下文只使用这个准确比值，不需要重命名原权序列。

## 2. 有限 creation 块和的像投影

取两两不交的非空有限位集
$$
B_1,\ldots,B_N,\qquad
s_\nu=\min B_\nu,\qquad
s_1<s_2<\cdots<s_N,\qquad m=s_1.
$$
所有这些位都小于某个 $M$。置
$$
L=\sum_{\nu=1}^N c_\nu E_{B_\nu},
\qquad
E_{B_\nu}=\prod_{j\in B_\nu}E_j,
\qquad
c_\nu\ne0,
$$
$$
1\le r<N,\qquad
P=\operatorname{Proj}\operatorname{Ran}L^r.
\tag{2.1}
$$
$L$ 是一个已知有限物理矩阵的恒等尾扩张，故其像闭，
$P$ 是原 $H$ 上的正交投影，$\|P\|=1$。
$L$ 与 $P$ 都只在本文作为纯有限块矩阵使用。

每个 $B_\nu$ 中，由全零和全一物理向量张成的二维空间称为活动空间。
$E_{B_\nu}$ 与其伴随都保持该空间，且在正交补上为零。
故全部块同时活动的张量空间约化 $L$ 和 $P$。
在这个空间中，$L$ 就是 $N$ 个二阶 creation 的加权和。

若 $F\subseteq\{1,\ldots,N\}$，令 $e_F$ 为：
$F$ 中的块全为 $1$，其他块全为 $0$，所有选中块外的前 $M$ 位也为 $0$，
尾因子为真空。于是这些向量正交单位。
记
$$
c_F=\prod_{\nu\in F}c_\nu,\qquad
Z_r=\sum_{|F|=r}|c_F|^2>0,\qquad
u=Z_r^{-1/2}\sum_{|F|=r}c_F e_F.
\tag{2.2}
$$

$L^r$ 将活动占据数提高 $r$。活动 $r$ 层的像只来自活动零层，
且
$$
L^r e_\varnothing=r!\sum_{|F|=r}c_F e_F.
$$
所以 $P$ 在活动 $r$ 层上准确等于
$$
\boxed{P_r=u\otimes u.}
\tag{2.3}
$$

令
$$
\mathscr H_+=\operatorname{span}\{e_F:|F|=r,\ 1\in F\},
\qquad
\mathscr H_-=\operatorname{span}\{e_G:|G|=r,\ 1\notin G\},
$$
并记其正交投影为 $Q_+,Q_-$。定义
$$
p=\sum_{\substack{|F|=r\\1\in F}}\frac{|c_F|^2}{Z_r}\in(0,1).
\tag{2.4}
$$
由 (2.3)，
$$
\boxed{
\|Q_-P Q_+\|=\sqrt{p(1-p)}.
}
\tag{2.5}
$$

## 3. 一个被原投影准确杀掉的实际退步输入

固定 $0\le\ell\le m$。对 $|F|=r$，设
$$
b_F=\sum_{\nu\in F}\sum_{j\in B_\nu}2^j,
\qquad
z_F=e_{b_F-2^\ell}^{[M]}.
\tag{3.1}
$$
因 $b_F\ge2^m\ge2^\ell$，这个柱合法。所有 $z_F$ 仍正交单位。
令 $J_+$、$J_-$ 分别把相应的 $e_F,e_G$ 送到 $z_F,z_G$；
它们是从 $\mathscr H_\pm$ 到原 $H$ 的等距映射。

对 $F$ 含第一个块，$b_F$ 的最低非零位恰为 $m$。
减去 $2^\ell$ 后，位 $m$ 从 $1$ 变成 $0$，
位 $\ell,\ldots,m-1$ 变成 $1$；后面这些位全部在选中块之外。
其他 $r-1$ 个占据块保持全一。

如果 $B_1=\{m\}$，这给活动占据数 $r-1$。
如果 $B_1$ 含多个位，第一个块变成部分占据的非活动向量，
它被 $E_{B_1}$ 及其伴随同时杀掉；在该约化扇区中，其余活动块仍只有 $r-1$ 个全一。
两种情形都与 $\operatorname{Ran}L^r$ 正交。因此
$$
\boxed{P J_+=0.}
\tag{3.2}
$$

又由 (1.2)，
$$
A^{2^\ell}J_+=w_{\ell,m}I_{\mathscr H_+},
\qquad
(A^{2^\ell})^*e_G
=w_{\ell,j(G)}J_-e_G,
\quad
j(G)=\min_{\nu\in G}s_\nu\ge s_2.
\tag{3.3}
$$
所有这些等式都在原有限柱上准确成立。

## 4. 与完整实际交换子代数的范数距离

置
$$
\kappa=\prod_{s=m}^{s_2-1}\eta_s\le\eta_m<1.
\tag{4.1}
$$

**定理 4.1。** 对任意 $R\in A'$，
$$
\boxed{
\|R-P\|\ge
\frac{\sqrt{p(1-p)}}{1+\kappa}.
}
\tag{4.2}
$$
这个下界不限制 $\|R\|$，也不要求 $R$ 属于 UHF 或多项式代数。

**证明。** 记 $\delta=\|R-P\|$。
由实际交换性 $RA^{2^\ell}=A^{2^\ell}R$ 及 (3.3)，逐矩阵元有
$$
\langle Re_F,e_G\rangle
=\frac{w_{\ell,j(G)}}{w_{\ell,m}}
 \langle Rz_F,z_G\rangle.
\tag{4.3}
$$
右侧权比在 $(0,\kappa]$。
因此作为有限块算子，
$$
Q_-R Q_+=D_\kappa J_-^*R J_+,
\qquad \|D_\kappa\|\le\kappa.
$$
由 (3.2)，
$$
\|J_-^*R J_+\|
=\|J_-^*(R-P)J_+\|\le\delta.
$$
所以
$$
\|Q_-R Q_+\|\le\kappa\delta.
$$
结合 (2.5) 与三角不等式，
$$
\sqrt{p(1-p)}
\le\|Q_-(P-R)Q_+\|+\|Q_-R Q_+\|
\le(1+\kappa)\delta.
$$
证毕。

若所有 $|c_\nu|$ 相等，准确有 $p=r/N$，故
$$
\boxed{
\operatorname{dist}(P,A')
\ge
\frac{\sqrt{(r/N)(1-r/N)}}{1+\kappa}.
}
\tag{4.4}
$$
当 $r/N$ 留在 $(0,1)$ 的一个固定紧子区间时，右侧一致离开零。
把整组块移到任意远的物理位置只会使 $\kappa$ 更小，不会消除这个间隙。

更一般，若
$$
\Lambda=\frac{\max_\nu|c_\nu|}{\min_\nu|c_\nu|}\ge1,
$$
则
$$
p\ge\frac{r}{\Lambda^2N},\qquad
1-p\ge\frac{N-r}{\Lambda^2N},
$$
从而
$$
\operatorname{dist}(P,A')
\ge
\frac{\Lambda^{-2}\sqrt{(r/N)(1-r/N)}}{1+\kappa}.
\tag{4.5}
$$
为核前两式，在其余 $N-1$ 个正权 $b_\nu=|c_\nu|^2$ 上，
$$
\frac{N-r}{r}b_{\min}
\le\frac{e_r(b_{\ne1})}{e_{r-1}(b_{\ne1})}
\le\frac{N-r}{r}b_{\max}.
$$
这是对每个 $(r-1)$ 元集合求剩余 $N-r$ 个权的和，再除以 $r$。
代入准确赔率
$p/(1-p)=b_1 e_{r-1}(b_{\ne1})/e_r(b_{\ne1})$ 即得。
所以固定精度的块产品平衡仍有同一常数级障碍。

## 5. 实际 dyadic 共轭：每个固定块有界，但有巨大下界

定义自然共轭
$$
\mathcal Q_\ell=A^{-2^\ell}P A^{2^\ell}.
\tag{5.1}
$$
这里先验证它确实全域有界，而不是直接使用未付的无界表达式。

$\operatorname{Ran}L^r$ 中每个物理分量至少有一个选中块全一，
所以在位 $\ell,\ldots,M-1$ 中至少有一个 $1$。
在这个有限柱直和上，(1.2) 的同一计算，允许任意前 $\ell$ 位以及任意尾向量，
给实际 $A^{2^\ell}$ 的有界右逆，其范数不超过
$$
w_{\ell,M-1}^{-1}.
$$
故
$$
PH\subseteq\operatorname{Ran}A^{2^\ell},\qquad
A^{-2^\ell}P\in B(H),
$$
$$
\|\mathcal Q_\ell\|
\le
\frac{d_\ell}{w_{\ell,M-1}}
=\left(\prod_{s=\ell}^{M-2}\eta_s\right)^{-1}.
\tag{5.2}
$$
最后用 $\|A^{2^\ell}\|=d_\ell$；只需已知 $\|N_\ell\|\le1$ 时，同一上界也成立。
原 $A$ 单射，故所定义的逆像唯一。

对整数 $1\le L_0\le N-r$，置
$$
p_{L_0}
=\frac{\sum_{\substack{|G|=r\\G\subseteq\{L_0+1,\ldots,N\}}}|c_G|^2}{Z_r}>0,
\qquad
\vartheta_{L_0}=\prod_{s=m}^{s_{L_0+1}-1}\eta_s.
\tag{5.3}
$$

**定理 5.1。**
$$
\boxed{
\|\mathcal Q_\ell\|
\ge
\vartheta_{L_0}^{-1}\sqrt{p\,p_{L_0}},
\qquad 0\le\ell\le m.
}
\tag{5.4}
$$

**证明。** 把输出限制到活动 $r$ 层且只占据最后 $N-L_0$ 个块的空间 $\mathscr H_{L_0}$。
由 (2.3)，
$$
\|Q_{L_0}P Q_+\|=\sqrt{p\,p_{L_0}}.
$$
以 $z_F,z_G$ 为输入输出预像柱，(1.2) 给
$$
\langle\mathcal Q_\ell z_F,z_G\rangle
=\frac{w_{\ell,m}}{w_{\ell,j(G)}}\langle Pe_F,e_G\rangle.
\tag{5.5}
$$
对这些 $G$，$j(G)\ge s_{L_0+1}$，所以每个输出行的正缩放至少为
$\vartheta_{L_0}^{-1}$。
一个正对角矩阵若每个对角元至少 $a>0$，左乘任意矩阵后其范数至少放大 $a$。
于是 (5.4) 成立。证毕。

### 5.1 连续单个位池的显式增长

取
$$
B_\nu=\{m+\nu-1\},\qquad |c_\nu|\text{ 全相等}.
$$
则
$$
p=\frac rN,\qquad
p_{L_0}=\frac{\binom{N-L_0}{r}}{\binom Nr}.
$$
特别选 $L_0=N-r$，得到
$$
\boxed{
\|\mathcal Q_\ell\|
\ge
\left(\prod_{s=m}^{m+N-r-1}\eta_s\right)^{-1}
\sqrt{\frac{r}{N\binom Nr}}.
}
\tag{5.6}
$$
由原权界，
$$
\boxed{
\log\|\mathcal Q_\ell\|
\ge
\frac{770}{15}\bigl(16^{m+N-r}-16^m\bigr)
+\frac12\log(r/N)-\frac12\log\binom Nr.
}
\tag{5.7}
$$
当 $r/N$ 为固定严格小于 $1$ 的正比例时，
这个对数下界远大于 $N$ 的任何固定幂。
所以不能把它并入 $\exp(O(N^a))$ 型范数预算，任意固定 $a>0$ 均不够。

若 $c_\nu$ 非等模，(5.4) 是准确式。
粗略地，
$$
\sqrt{p\,p_{N-r}}\ge
\Lambda^{-2r}\binom Nr^{-1},
$$
因为分子中分别保留一个合法集合即可。
因而仍有
$$
\log\|\mathcal Q_\ell\|
\ge
\frac{770}{15}\bigl(16^{m+N-r}-16^m\bigr)
-2r\log\Lambda-\log\binom Nr.
\tag{5.8}
$$
例如，在 $r/N\le\theta<1$ 的固定比例上界下，
若 $\log\Lambda=O((m+N)^a)$，损失只是多项式量级，
不能抵消 (5.8) 中的 $16^{m+N-r}$ 项。
若 $N-r$ 保持很小，则不能删去此比较中的条件。

### 5.2 固定多位块不会消除这个实际权比

若 $B_\nu$ 为依次排列、每块含 $b\ge1$ 个连续位，
则 $s_\nu=m+b(\nu-1)$。
等模 $c_\nu$ 时，(5.6)--(5.7) 中的 $m+N-r$ 变成
$$
m+b(N-r).
$$
因此将若干位打包、平衡 $\prod_{j\in B_\nu}a_j$，可以改善 creation 权的条件数，
却不消除这里的原 odometer 权比。即使块权完全相等，
(4.4) 的常数距离和这个共轭增长仍存在。

## 6. 小范数扰动的准确范围

若 $\widetilde P\in B(H)$ 满足
$$
\|\widetilde P-P\|\le\delta,
$$
而存在有界 $\widetilde{\mathcal Q}_\ell$ 使
$$
A^{2^\ell}\widetilde{\mathcal Q}_\ell
=\widetilde P A^{2^\ell},
\tag{6.1}
$$
则同一有限矩阵元计算给
$$
\boxed{
\|\widetilde{\mathcal Q}_\ell\|
\ge
\vartheta_{L_0}^{-1}
\bigl(\sqrt{p\,p_{L_0}}-\delta\bigr)_+.
}
\tag{6.2}
$$
证明只需先在 $Q_{L_0}\widetilde P Q_+$ 上减去 $\delta$，
再使用 (5.5) 的正行缩放。
没有假定任意小范数扰动都保持 $PH\subseteq\operatorname{Ran}A^{2^\ell}$；
若 (6.1) 不存在，本接口本身就没有被建立。

尤其，若试图把 $P$ 以小于 (4.2) 的范数误差提升成真正 $A'$ 元，
定理 4.1 已直接排除。极小 carry 可以控制某个已给的有限解析块多项式，
却不会把这个包含 adjoint 的正交投影自动变成解析交换子。

## 7. 与强近恒等及 Bell 端项的关系

[R236 已有高次提升带及像投影定理](R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)
已经证明：单个位等权池中，若 $N\to\infty$、
$r\le\theta N$、固定 $\theta<1/2$，
且整池的最小物理位趋于无穷，则 $P\to I$ 强收敛。
其准确真空式为
$$
\|(I-P)\Omega\|^2
=\mathbb P\{\operatorname{Bin}(N,1/2)<r\}.
\tag{7.1}
$$
本稿不重新登记该强极限；(4.4) 与它完全相容。
强趋于恒等不意味着到 $A'$ 的算子范数距离趋零。

固定 $b$ 位且 $c_\nu=c\ne0$（共同相位）的等权块也可直接计算：每块的活动概率为 $2^{1-b}$，
条件于活动时其全一概率为 $1/2$。
分解为互相正交的活动/非活动扇区，再使用 (7.1) 的有限层计算，得到
$$
\|(I-P)\Omega\|^2
=\mathbb P\{\operatorname{Bin}(N,2^{-b})<r\}.
\tag{7.2}
$$
所以当 $N\to\infty$ 且 $r/N<2^{-b}$ 保持固定余量时，同样可得到强近恒等；
与此同时，(4.4) 的范数距离仍为常数级。
这里的强极限仍须最小物理位趋于无穷，随后由有限柱稠密性扩展。

在 Bell 反射端项中，原正交伪逆写为
$$
V_N=(L^r)^\dagger,\qquad L^rV_N=P.
$$
把某个输入写成 $f=A^{2^\ell}x$，并不免费允许把
$P A^{2^\ell}x$ 改写为一个成本受控的
$A^{2^\ell}\mathcal Q_\ell x$。
本稿说明该具体 $\mathcal Q_\ell$ 对每个固定池虽然真实存在，
但已经满足 (5.4) 的巨大范数下界。
若所用移入还需要 $V_N$ 自身的除法，则必须另付该更强的域与成本，
不能仅靠 $P$ 的有界性或 (7.1) 的强极限。

这些下界没有覆盖不经过 (6.1) 的新双边配对、受限核内相消，
或另一个可直接建立的预处理。它也不把小的普通交换子
$\|[A^{2^\ell},P]\|$ 当成除法后的成本：
(1.2) 中很小的权正是 (5.5) 被逆向放大的来源。

普通 Hilbert ISP、真实正常见证及一般伪逆端项仍未解决。
