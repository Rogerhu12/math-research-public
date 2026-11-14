# R254 第十附录：相容多次纯尾原像与 p>1/4 实际正则核饱和

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的实际中间结论。

本稿把 [R254 第七附录](../results/R254-appendix-restricted-pure-kernel-right-inverse-and-subexponential-stable-range.md) 的单次有限双和推广为相容的多次原像 $R_t$，使 $DR_t=R_{t-1}$ 准确成立。整个多次原像只支付一次输入核阶。再结合 [R254 第九附录](../results/R254-appendix-common-plateau-pure-power-inverse-and-one-third-stable-range.md) 已支付的 $q=25d^4$ 前半桥与实际正则提升，得到所有 $p>1/4$ 的原实际正则核饱和。未证明一般实际核内稠密性。

## 1. 固定共同辅助头与相容递推

设
$$
D=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+2)^{-2},
$$
且 $\mathcal H_\ell$ 为完整的高尾 $\ell$ 孔层，位置可无限远。固定输入上界 $q$、最大原像阶 $t_{\max}\ge1$，写
$$
Q=q+t_{\max},\qquad J=32(m+Q+2).
$$
辅助头为高尾最前面的 $J$ 个位置。定义
$$
D=D_0+D_1,\qquad
C=\sum_{m\le j<m+J}a_j^{-1}E_j^*,\qquad
H=J-2\mathcal N_{\rm aux}.
$$
$C$ 不是 $D^*$。准确关系为
$$
[D,C]=H,\qquad [H,C]=-2C,\qquad
[D_1,C]=[D_1,H]=[D_1,D]=0,
$$
$$
DC^r=C^rD+rC^{r-1}(H-r+1),
\tag{1.1}
$$
$$
DF(H)=F(H-2)D+[F(H)-F(H-2)]D_1.
\tag{1.2}
$$

置 $F^{(0)}_{00}=1$，$F^{(0)}_{kl}=0$ 当 $(k,l)\ne(0,0)$，负指标项也为零。对 $t\ge1$ 递推定义
$$
\begin{aligned}
&(k+l+t)(x-k-l-t+1)F^{(t)}_{kl}(x)\\
&\quad=F^{(t-1)}_{kl}(x)
-F^{(t)}_{k-1,l}(x-2)
+F^{(t)}_{k,l-1}(x-2)-F^{(t)}_{k,l-1}(x).
\end{aligned}
\tag{1.3}
$$
先按 $t$、再按 $k+l$ 递推，定义没有循环。

在 $\mathcal H_{\le q}$ 上令
$$
R_t f=
\sum_{k+l\le q}
 C^{k+l+t}F^{(t)}_{kl}(H)D^kD_1^l f,
\qquad 0\le t\le t_{\max}.
\tag{1.4}
$$
所有 $R_t$ 使用同一个 $C,H,D_1$。
实际应用中只出现辅助孔数不超过 $Q$ 的有限谱点；下面证明所有分母在需要的源层均严格正。其余谱点可任意作有界延拓，不参与恒等式。

把 (1.1)--(1.2) 代入 (1.4)，收集
$C^{k+l+t-1}D^kD_1^l$ 的系数，得到 (1.3) 左侧与右侧的精确抵消。最外边界 $k+l=q+1$ 的项删除至少 $q+1$ 次孔，在输入上准确为零。因此
$$
\boxed{
R_0=I,\qquad
DR_t=R_{t-1},\qquad
D^tR_t=I
\quad\text{于 }\mathcal H_{\le q}.
}
\tag{1.5}
$$
$R_t$ 严格增加 $t$ 次孔，且
$$
R_t(\ker D^s\cap\mathcal H_{\le q})
\subseteq\ker D^{s+t}.
\tag{1.6}
$$
没有要求 $R_t$ 等于旧单次右逆在变动辅助头下的 $t$ 次复合。

## 2. 正分母展开与多次系数预算

令
$$
P^{(t)}_{kl}=(-1)^kF^{(t)}_{kl}.
$$
它是非负系数乘以倒数线性因子乘积的有限和。每个乘积恰有
$$
k+2l+t
\tag{2.1}
$$
个因子，全部极点是位于
$$
0\le b\le 2(k+l)+t-1
\tag{2.2}
$$
的整数。

证明同时按 (1.3) 归纳。$t-1$ 项或 $k-1$ 项经除以一个线性因子，都使因子数增加一。$l-1$ 项使用
$P(x-2)-P(x)$：对一个含 $v$ 个倒数因子的乘积，逐因子望远镜展开该差，每项新增一个因子，系数总量为 $2v$，全部系数非负。再除以递推分母又新增一个因子。最大极点也由 (1.3) 直接给 (2.2)。

令 $A^{(t)}_{kl}$ 为这种展开的系数总和。递推给
$$
A^{(t)}_{kl}
\le
\frac{
A^{(t-1)}_{kl}
+A^{(t)}_{k-1,l}
+2(k+2l+t-2)A^{(t)}_{k,l-1}
}{k+l+t}.
$$
因为 $t\ge1$，可进一步估计为
$$
A^{(t)}_{kl}
\le A^{(t-1)}_{kl}+A^{(t)}_{k-1,l}
+4A^{(t)}_{k,l-1}.
$$
从 $A^{(1)}_{00}=1$ 开始，三方向的 Pascal 递推于是给
$$
\boxed{
A^{(t)}_{kl}
\le
\frac{(k+l+t-1)!}{k!\,l!\,(t-1)!}\,4^l.
}
\tag{2.3}
$$
$t=1$ 正好回到第七附录所用的二项系数预算；此处新增的 $t-1$ 方向是多次原像的关键。

## 3. 完整孔层上的受限范数

记
$$
M_*=m+J+2,\qquad
B_0=\|(a_j^{-1})_{m\le j<m+J}\|_2,
\qquad g_1=\|(a_j)_{j\ge m+J}\|_2.
$$
有
$$
B_0\le\sqrt J\,M_*^2,\qquad
g_1\le M_*^{-3/2}.
\tag{3.1}
$$
若 $n=k+l$，在 $D^kD_1^lf$ 之后总孔数至多为 $q-n$，所以
$$
H\ge J-2(q-n).
$$
结合最大极点 (2.2)，每个实际分母都至少为
$$
J-2q-t+1\ge\Delta:=J-2Q>0.
\tag{3.2}
$$

完整孔层的创建、删除估计为
$$
\|C|_{\mathcal H_\ell}\|\le\sqrt{\ell+1}B_0,\qquad
\|D_1|_{\mathcal H_\ell}\|\le\sqrt\ell\,g_1,
\qquad \|D\|\le1.
$$
令
$$
L_0=\frac{\sqrt{Q+1}B_0}{\Delta},\qquad
V=\frac{4\sqrt{Q(Q+1)}B_0g_1}{\Delta^2}.
$$
因为 $J=32(m+Q+2)$，有
$\Delta\ge15J/16$、$M_*\le33J/32$，从而
$$
V\le\frac{32}{225}\sqrt{\frac{33}{32}}<\frac14,
$$
$$
\frac{L_0}{1-V}
\le L:=512\sqrt{Q+1}(m+Q+2)^{3/2}.
\tag{3.3}
$$

若 $f\in\ker D^s\cap\mathcal H_{\le q}$，则 (1.4) 中 $k\ge s$ 的项准确消失。对其余项，(2.1)--(2.3) 与 (3.2) 给
$$
\begin{aligned}
\|R_tf\|
&\le
\sum_{k=0}^{s-1}\sum_{l\ge0}
\frac{(k+l+t-1)!}{k!\,l!\,(t-1)!}
 L_0^{k+t}V^l\|f\|\\
&=
\sum_{k=0}^{s-1}
\binom{k+t-1}{k}
 \left(\frac{L_0}{1-V}\right)^{k+t}\|f\|.
\end{aligned}
\tag{3.4}
$$
第一行中的 $V$ 已包含系数 (2.3) 的 $4$；原有限和只被正项无穷和放大。这里在整层上使用算子范数，未用逐基向量界代替整层界。

因 $L\ge1$，再用二项系数求和，
$$
\boxed{
\|R_tf\|
\le\binom{s+t-1}{s-1}L^{s+t-1}\|f\|
\le(2L)^{s+t-1}\|f\|.
}
\tag{3.5}
$$
不同输入孔层的输出仍互相正交，故同一界适用于完整的 $\mathcal H_{\le q}$。
多次原像的指数是 $s+t-1$，不是 $s\,t$。

## 4. 相容原像给准确混合右逆

仍取 $d=2^m$，两种真实混合平方符号均为
$$
P_m=D^2+Q_m,\qquad
[D,Q_m]=0,\quad Q_m^d=0,\quad\|Q_m\|<1/2.
$$
$Q_m$ 的高尾孔降低量为 $0,1,2$，且具有严格正的有限头次数。

在第 1 节取 $t_{\max}=2d$，定义新的实际有限孔右逆
$$
\boxed{
\widetilde{\mathcal G}_{m,q}
=\sum_{k=0}^{d-1}(-1)^kQ_m^kR_{2k+2}.
}
\tag{4.1}
$$
所有 $R_t$ 只作用高尾，与原前 $m$ 位张量恒等。由 (1.5)，
$$
\begin{aligned}
P_m\widetilde{\mathcal G}_{m,q}
&=\sum_{k<d}(-1)^k Q_m^kR_{2k}
+\sum_{k<d}(-1)^k Q_m^{k+1}R_{2k+2}\\
&=I.
\end{aligned}
\tag{4.2}
$$
这里仅使用 $D^2$ 与 $Q_m$ 交换及 $D^2R_t=R_{t-2}$，没有交换 $Q_m$ 与 $R_t$。

第 $k$ 项先增加 $2k+2$ 次孔，再由 $Q_m^k$ 降低至多 $2k$ 次孔。因此此右逆最低增加 $2$ 次、最高增加 $2d$ 次孔。对
$f\in\ker D^{2d}\cap\mathcal H_{\le q}$，(3.5) 给
$$
\|\widetilde{\mathcal G}_{m,q}f\|
\le\sum_{k<d}2^{-k}(2L)^{2d+2k+1}\|f\|.
$$
故
$$
\boxed{
\|\widetilde{\mathcal G}_{m,q}f\|
\le\mathcal C_{m,q}\|f\|,
\qquad
\mathcal C_{m,q}:=d(2L)^{4d-1}.
}
\tag{4.3}
$$
这一改进不再需要把第八附录的四次头衰减放进有限和；单靠相容多次原像已经把输入核阶成本降到线性。

## 5. 特殊实际残量、准确核归属和正则提升

采用第九附录已构造的
$$
q=25d^4,\qquad
v_m=P_{\le q}\mathsf V_{m,q}u,\qquad u\in K.
$$
该构造只依赖交集空间，故不因本稿改换右逆而改变。已证
$$
v_m\in\ker D^{2d}\cap\mathcal H_{\le q},\quad
P_{\le q-2}P_mv_m=0,\quad \|v_m\|\le\|u\|,
$$
$$
\|P_{\le q}u-v_m\|\le e^{-1000d^4}\|u\|,
\qquad v_m\to u.
\tag{5.1}
$$
取
$$
r_m=P_mv_m,\qquad
c_m=\widetilde{\mathcal G}_{m,q}r_m,\qquad
k_m=v_m-c_m.
$$
则
$$
r_m\in\ker D^{2d}\cap(\mathcal H_{q-1}\oplus\mathcal H_q),
$$
$$
\|r_m\|\le\tau_{q-2}(u)+e^{-1000d^4}\|u\|.
\tag{5.2}
$$
所以 (4.3) 确实用在有严格有限纯核阶的输入上。

由 (4.2) 和输出带宽，
$$
k_m\in\ker P_m\cap\mathcal H_{\le q+2d},\qquad
c_m\in\mathcal H_{[q+1,q+2d]}.
$$
实际伴随多项式仍满足
$\mathcal A_mP_m=D^{2d}$，故
$$
D^{2d}c_m=\mathcal A_mr_m=D^{2d}v_m=0.
\tag{5.3}
$$
这补全准确的纯核归属，没有要求新右逆一般性地保持 $\ker D^{2d}$。

在 $q=25d^4$ 下，第九附录的计算给 $\log L<13+8\log d$，所以
$$
\boxed{
\log\mathcal C_{m,25d^4}
\le64d(1+\log d).
}
\tag{5.4}
$$
对 $m\ge4$，右侧不超过 $d^4$。

实际 $X_7\to X_3$ 桥作用于 $k_m$，得到
$$
n_m=\Lambda_{m,q+2d}k_m\in N.
$$
第九附录已从原公式重新支付
$\delta_{m,q+2d}\le e^{-900d^4}$。
因为
$\|k_m\|\le2e^{d^4}\|u\|$，仍有
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-898d^4}\|u\|.
}
\tag{5.5}
$$
实际域、carry 和全输出次数均被这个同尺度估计覆盖。

## 6. p>1/4 的实际正则核和真缺陷尾率

**定理。** 对两个原实际慢边界核 $M=\ker T$、$N=\overline{BM}$，任意 $p>1/4$ 和 $c>0$ 都有
$$
\boxed{
M\cap\operatorname{Dom}e^{c(1+\mathcal N)^p}\subseteq N.
}
\tag{6.1}
$$

证明：若 $w=Ju$ 属于左侧，第一位分量提取和总孔数控制给
$\tau_Q(u)\le C_we^{-c(1+Q)^p}$。
因 $q=25d^4$ 且
$$
d(1+\log d)=o(d^{4p}),
$$
(5.2)--(5.4) 给 $\|c_m\|\to0$。
结合 $v_m\to u$、$J_m\to J$ 和 (5.5)，$n_m\to w$ 强收敛，故 $w\in N$。证毕。

另一方面，若 $0\ne w=Ju\in M\ominus N$，同一准确提升及高尾支撑给
$$
\langle J_mc_m,w\rangle\to\|w\|^2,\qquad
\|c_m\|\tau_{q-1}(w)\ge\frac25\|w\|^2
$$
对充分大的 $m$ 成立。由 (5.2)--(5.4)，小误差可吸收，因而
$$
\mathcal C_{m,q}\tau_{q-2}(w)^2
\ge\frac15\|w\|^2.
$$
所以
$$
\log\frac{\|w\|}{\tau_{25d^4-2}(w)}
\le32d(1+\log d)+\tfrac12\log5.
$$
相邻 $q$ 网格比为 $16$，尾范数单调性给全序列结论
$$
\boxed{
-\log\frac{\tau_Q(w)}{\|w\|}
=O\!\left(Q^{1/4}\log(Q+2)\right).
}
\tag{6.2}
$$
这是缺陷存在时必须满足的慢尾条件，并不排除任意慢的 Hilbert 尾。

## 7. 未证明的结论

本稿没有把 (6.1) 的正则核子集当作 $M$ 内稠密子集，也没有把 Haar 表示的逆范围或正常性运输到边界。临界 $p=1/4$ 对任意正 $c$ 亦未宣称成立。

相容 $R_t$ 给出的有限孔原像和实际稳定像提升都是已支付的对象；一般核向量是否使特殊 $c_m$ 有界、或者是否存在另一种无权的核内逼近，仍然开放。$N=M$ 与普通 ISP 尚未完成。
