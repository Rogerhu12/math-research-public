# R254 第七附录：纯删除有限阶核的真实受限右逆与边界的亚指数正则饱和

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的中间结论；普通 ISP 与边界 $N=M$ 均未完成。

本稿接续 [R254 第六附录](../results/R254-appendix-exact-top-layer-repair-stable-lift-and-defect-norm-obstruction.md) 及 [R239 的正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)。核心是对纯删除的有限阶核构造实际右逆；它的成本远低于整个孔层上的右逆，因而不与既有纯创建指数下界矛盾。

## 1. 纯尾设置和主引理

固定整数 $m\ge0$，在纯高尾的有限子集 Hilbert 空间上取
$$
D=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+2)^{-2}.
$$
$E_j$ 删除第 $j$ 个孔。以 $\mathcal H_q$ 表示完整 $q$ 孔层，位置不要求有限。
$\|D\|\le\sum_{j\ge m}a_j\le1$。

**主引理。** 对每个 $q\ge0$，存在同一个实际有界算子
$$
G_q:\mathcal H_q\longrightarrow\mathcal H_{q+1},\qquad DG_q=I,
\tag{1.1}
$$
使对每个整数 $s\ge1$ 及 $f\in\ker D^s\cap\mathcal H_q$，
$$
G_qf\in\ker D^{s+1},
$$
$$
\boxed{
\|G_qf\|
\le s\,L_{m,q}^{\,s}\|f\|,
\qquad
L_{m,q}=512\sqrt{q+1}\,(m+q+2)^{3/2}.
}
\tag{1.2}
$$
$G_q$ 不随 $s$ 改变。特别
$$
D:\ker D^2\cap\mathcal H_{q+1}\longrightarrow
\ker D\cap\mathcal H_q
$$
有范数至多 $L_{m,q}$ 的真实右逆。这确实是核内右逆，不只是把环境创建算子的下界压缩过去。

## 2. 有限头的准确交换关系

固定 $q$，置
$$
J=32(m+q+2),\qquad M=m+J+2.
$$
以下辅助头是纯尾中的 $J$ 个位置 $m,\ldots,m+J-1$，不是 R254 的原有限头。
记
$$
D_0=\sum_{j=m}^{m+J-1}a_jE_j,\qquad
D_1=\sum_{j\ge m+J}a_jE_j,
$$
$$
C=\sum_{j=m}^{m+J-1}a_j^{-1}E_j^*,\qquad
H=J I-2\mathcal N_0,
$$
其中 $\mathcal N_0$ 数这 $J$ 个辅助位置上的孔。$C$ 是实际有限和有界算子，虽然它不是 $D^*$。

逐位矩阵给
$$
[D,C]=H,\qquad [H,C]=-2C,\qquad
[D,D_1]=0,\qquad [H,D_1]=[C,D_1]=0.
\tag{2.1}
$$
因此
$$
D C^{n+1}=C^{n+1}D+(n+1)C^n(H-n).
\tag{2.2}
$$
对下面的有理函数 $F$，在实际用到的有限孔空间上，
$$
D F(H)=F(H-2)D+[F(H)-F(H-2)]D_1.
\tag{2.3}
$$
例如 $D_0$ 将辅助头孔数降低一，故
$D_0F(H)=F(H-2)D_0$；$D_1$ 保持该孔数，故与 $F(H)$ 交换。这证明 (2.3)，不使用形式无界算子。

所有有理函数仅作用于头孔数不超过 $q+1$ 的部分。在这个部分及所需的有限移位上，分母严格正；可在其余有限头特征值上任取有界延拓。下面的等式只在已列出的实际有限孔运算中使用。

## 3. 有限双和的精确右逆

对 $k,l\ge0$ 递归定义有理函数 $F_{kl}$，约定负指标项为零：
$$
F_{00}(x)=x^{-1},
$$
$$
\boxed{
F_{kl}(x)=
\frac{
-F_{k-1,l}(x-2)
+F_{k,l-1}(x-2)-F_{k,l-1}(x)
}{
(k+l+1)(x-k-l)
}
\quad(k+l\ge1).
}
\tag{3.1}
$$
定义有限双和
$$
\boxed{
G_qf=
\sum_{\substack{k,l\ge0\\k+l\le q}}
C^{k+l+1}F_{kl}(H)D^kD_1^lf.
}
\tag{3.2}
$$
每项最终孔数为 $q+1$，所以输出在完整 $\mathcal H_{q+1}$ 中。每项的算子都在其实际输入层上有界，和只有有限项。

令 $n=k+l$。对 (3.2) 中一项用 (2.2)--(2.3)，得到三部分：
$$
(n+1)C^n(H-n)F_{kl}(H)D^kD_1^lf,
$$
$$
C^{n+1}F_{kl}(H-2)D^{k+1}D_1^lf,
$$
$$
C^{n+1}[F_{kl}(H)-F_{kl}(H-2)]D^kD_1^{l+1}f.
$$
相同正规次序 $C^{k+l}(\cdots)D^kD_1^l$ 的系数由 (3.1) 准确抵消。
$k=l=0$ 的第一项为 $HF_{00}(H)f=f$。
最后可能余下的项总共删除 $q+1$ 个孔，故在 $\mathcal H_q$ 上为零。
于是
$$
\boxed{DG_qf=f.}
\tag{3.3}
$$

特别，当 $Df=0$ 时只保留 $k=0$，递推可以写成明确的 Catalan 形式：
$$
F_{0l}(x)=
\frac{\operatorname{Cat}_l}
{x(x-1)\cdots(x-2l)},
\qquad
\operatorname{Cat}_l=\frac1{l+1}\binom{2l}{l}.
\tag{3.4}
$$
代入 (3.1) 时，两个平移倒数积的差分子为
$2(2l-1)(x-l)$，恰给 Catalan 递推。
但一般主引理使用 (3.1)，不假设输入已是一阶核。

## 4. 正分母展开的完整预算

令
$$
P_{kl}(x)=(-1)^kF_{kl}(x),\qquad n=k+l.
$$
由 (3.1)，
$$
P_{kl}(x)=
\frac{
P_{k-1,l}(x-2)
+P_{k,l-1}(x-2)-P_{k,l-1}(x)
}{
(n+1)(x-n)
}.
\tag{4.1}
$$

归纳可把 $P_{kl}$ 写成正系数的有限和，每项是
$$
\prod_{\nu=1}^{k+2l+1}(x-b_\nu)^{-1},
\qquad 0\le b_\nu\le2n.
\tag{4.2}
$$
证明差分步骤不能省略：对有 $p$ 个因子的任一倒数积，
平移 $x\mapsto x-2$ 后减去原积，用逐因子望远镜展开。
每一差因子准确为
$$
\frac1{x-b-2}-\frac1{x-b}
=\frac2{(x-b-2)(x-b)}.
$$
所以差分产生 $p$ 个正项，总系数最多乘 $2p$，倒数因子数增加一。再乘 (4.1) 的 $(x-n)^{-1}$，得到 (4.2)；极点上界也由归纳保持。

若 $A_{kl}$ 为这个正展开的系数总和，可取
$$
A_{kl}\le
\frac{A_{k-1,l}+2(k+2l-1)A_{k,l-1}}{n+1}.
$$
因 $2(k+2l-1)/(n+1)<4$，Pascal 归纳给
$$
\boxed{
A_{kl}\le\binom{k+l}{k}4^l.
}
\tag{4.3}
$$

$D^kD_1^lf$ 的全部孔数为 $q-n$，所以其辅助头孔数至多 $q-n$。
在该向量上 $H\ge J-2(q-n)$。结合 (4.2)，全部分母都至少为
$$
\Delta=J-2q>0.
$$
因此
$$
\boxed{
\|F_{kl}(H)D^kD_1^lf\|
\le
\binom{k+l}{k}4^l\,
\Delta^{-(k+2l+1)}
\|D^kD_1^lf\|.
}
\tag{4.4}
$$
该分母下界利用了先删除 $k+l$ 次孔这一实际顺序，不把有理函数任意移到算子最外面。

## 5. 求和及真正的有限阶核界

记
$$
B_0=\left(\sum_{j=m}^{m+J-1}a_j^{-2}\right)^{1/2},
\qquad
g_1=\left(\sum_{j\ge m+J}a_j^2\right)^{1/2}.
$$
准确有
$$
B_0\le\sqrt J\,M^2,\qquad
g_1^2\le\frac1{3(M-1)^3}\le M^{-3}.
\tag{5.1}
$$
最后用 $M\ge4$。

标准完整孔层 Cauchy--Schwarz 给任意系数列 $b$：
$$
\left\|\sum b_jE_j^*\bigm|_{\mathcal H_t}\right\|
\le\sqrt{t+1}\|b\|_2,\qquad
\left\|\sum b_jE_j\bigm|_{\mathcal H_t}\right\|
\le\sqrt t\,\|b\|_2.
\tag{5.2}
$$
例如创建式对每个 $(t+1)$ 元输出集合有至多 $t+1$ 项，先在该行作 Cauchy--Schwarz，再对所有集合求和即可；无限位置由有限位置逼近及一致界传递。

对 (3.2) 的一项，(4.4)--(5.2) 给
$$
\begin{aligned}
&\|C^{k+l+1}F_{kl}(H)D^kD_1^lf\|\\
&\quad\le
L_0\binom{k+l}{k}U^kV^l\|f\|,
\end{aligned}
\tag{5.3}
$$
其中
$$
L_0=\frac{\sqrt{q+1}B_0}{\Delta},\qquad
U=L_0\|D\|,
$$
$$
V=\frac{4\sqrt{q(q+1)}\,B_0g_1}{\Delta^2}.
$$
这里 $\|D^kD_1^lf\|\le\|D\|^kq^{l/2}g_1^l\|f\|$；
创建的 $k+l+1$ 步最终只到总次数 $q+1$，所以另给
$(q+1)^{(k+l+1)/2}B_0^{k+l+1}$。

由于
$$
M\le(33/32)J,\qquad \Delta\ge(15/16)J,\qquad
(q+1)/J\le1/32,
$$
有
$$
V\le\frac{32}{225}\sqrt{\frac{33}{32}}
<\frac{34}{225}<\frac14.
\tag{5.4}
$$
此外
$$
\frac{L_0}{1-V}
\le\frac43\frac{16}{15}\left(\frac{33}{32}\right)^2
32^{3/2}\sqrt{q+1}(m+q+2)^{3/2}
\le L_{m,q}.
\tag{5.5}
$$
末式可仅用 $\sqrt{32}<6$ 验证，数值上仍有充分余量。

若 $D^sf=0$，则 (3.2) 中 $k\ge s$ 的项准确为零。
利用
$$
\sum_{l\ge0}\binom{k+l}{k}V^l=(1-V)^{-k-1},
$$
以及 $\|D\|\le1$、$L_{m,q}\ge1$，得到
$$
\|G_qf\|
\le\frac{L_0}{1-V}
\sum_{k=0}^{s-1}
\left(\frac U{1-V}\right)^k\|f\|
\le sL_{m,q}^{\,s}\|f\|.
$$
(3.3) 还给
$D^{s+1}G_qf=D^sf=0$。
主引理证明完毕。

由真实右逆的伴随下界，若记
$E_{s,q}=\ker D^s\cap\mathcal H_q$，则也准确有
$$
\boxed{
\|P_{E_{s+1,q+1}}D^*f\|
\ge[sL_{m,q}^{\,s}]^{-1}\|f\|,
\qquad f\in E_{s,q}.
}
\tag{5.6}
$$
这是已经证明的压缩创建下界；它与只估计环境 $D^*f$ 不同。

## 6. 回到含全部混合项的顶部修复

现在恢复 R254 的实际头：$m\ge2$、$d=2^m$，并在该头之后的纯尾上使用 §§1--5 的同一个 $G_q$。
它只作用纯尾，因而与全部原有限头系数交换。

令 $G$ 为 $G_q$ 的代数直和，$H=G^2$。
它在每个有限孔空间上实际有界，$D^2H=I$，并严格增加两次尾孔。
仍定义
$$
\mathcal G_m=H\sum_{k=0}^{d-1}(-Q_mH)^k.
\tag{6.1}
$$
正头次数给 $(Q_mH)^d=0$，所以 $P_m\mathcal G_m=I$。
所有最低、最高输出次数及伴随多项式兼容性都与 R254 第六附录相同。

现在只估计其特殊输入：
$$
r\in\ker D^{2d}\cap\mathcal H_{\le q}.
$$
每次 $H$ 使核阶上升两次；每个 $Q_m$ 与 $D$ 交换，故不进一步增加核阶。
第 $j$ 次 $H$ 可用
$$
s_j=2d+2j,\qquad j=0,\ldots,d-1.
$$
把所有中间次数统一放到 $q+2d$，置
$$
L_*=512\sqrt{q+2d+1}\,(m+q+2d+2)^{3/2}.
$$
两个相继的 $G$ 给第 $j$ 次 $H$ 的成本
$$
s_j(s_j+1)L_*^{\,2s_j+1}.
$$
完整总阶为
$$
\boxed{\sum_{j=0}^{d-1}(2s_j+1)=6d^2-d.}
\tag{6.2}
$$
用 $s_j,s_j+1<4d$，并把 $d$ 个有限和项全部包含，得到
$$
\boxed{
\|\mathcal G_mr\|
\le\mathcal B_{m,q}\|r\|,
\qquad
\mathcal B_{m,q}
=d(4d)^{2d}L_*^{\,6d^2-d}.
}
\tag{6.3}
$$
这里的核阶与输出次数逐步列明了；没有将第一步的 $s=2d$ 界误用到后面全部步骤。

取 $q=25d^3$。对 $d\ge4$，
$m+q+2d+2\le27d^3$，所以
$$
L_*\le512(27d^3)^2,\qquad \log L_*<13+6\log d.
$$
由此可统一取
$$
\boxed{
\log\mathcal B_{m,25d^3}
\le100d^2(1+\log d).
}
\tag{6.4}
$$
例如其余 $\log d+2d\log(4d)$ 不超过 $2d^2$；
(6.3) 的主项至多 $78d^2+36d^2\log d$，足以得到 (6.4)。

## 7. 实际稳定像提升仍然支付全部进位

固定实际 $u\in K$。沿用 R254 第五、六附录的收缩交集投影，
$$
q=25d^3,\qquad v_m=P_{\le q}\mathsf V_{m,q}u.
$$
已证
$$
v_m\in\ker D^{2d}\cap\mathcal H_{\le q},\qquad
P_mv_m=r_m\in\mathcal H_{q-1}\oplus\mathcal H_q,
$$
$$
\|v_m-P_{\le q}u\|\le e^{-500d^4}\|u\|,
\qquad v_m\to u.
\tag{7.1}
$$
由于 $P_m$ 与 $D^{2d}$ 交换，
$$
r_m\in\ker D^{2d}.
$$
因此可以使用新的受限预算，定义
$$
c_m=\mathcal G_mr_m,\qquad k_m=v_m-c_m.
$$
准确有
$$
c_m\in\ker D^{2d}\cap
 \bigoplus_{j=q+1}^{q+2d}\mathcal H_j,\qquad
k_m\in\ker P_m\cap\mathcal H_{\le q+2d}.
\tag{7.2}
$$
同时
$$
\boxed{
\|c_m\|
\le\mathcal B_{m,q}
\left(\|P_{\{q-1,q\}}u\|+e^{-500d^4}\|u\|\right).
}
\tag{7.3}
$$
这些 $P$ 仍是高尾孔投影。其层质量不超过原全部孔次数的相应尾。

R239 的实际 $G_{7\to3}$ 桥给
$$
n_m=\Lambda_{m,q+2d}k_m\in N,
$$
$$
\|n_m-(J_mv_m-J_mc_m)\|
\le\delta_{m,q+2d}\|k_m\|.
\tag{7.4}
$$
这里 $q+2d\le50d^3$，故 $m\ge4$ 时
$\delta_{m,q+2d}\le e^{-1000d^4}$。
由 (6.4)，对 $d\ge16$ 还有
$100d^2(1+\log d)\le2d^4$。
因此
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-997d^4}\|u\|
\quad(m\ge4).
}
\tag{7.5}
$$
实际 $N$ 的归属及这个误差使用的是已付清的输入 $\mathscr X_7$、输出 $\mathscr X_3$，没有假设原来的 $\mathscr X_c\to H$ 右逆保持同一权。

## 8. 所有 p>2/3 的实际正则核属于 N

记 $\mathcal N$ 为原全部物理孔次数算子。

**推论。** 对任意 $p>2/3$ 及任意 $c>0$，
$$
\boxed{
M\cap\operatorname{Dom}
 e^{\,c(1+\mathcal N)^p}
\subseteq N.
}
\tag{8.1}
$$

证明：取 $w=Ju\in M$ 且属于该域。
首位偶分量提取不增加孔数，故 $u$ 的全部孔次数尾满足
$$
\tau_Q(u)\le C_w e^{-c(1+Q)^p}.
$$
(7.3) 中的移动两层质量不超过 $\tau_{q-2}(u)$。
由于 $q=25d^3$，而
$$
\log\mathcal B_{m,q}
\le100d^2(1+\log d)=o(d^{3p}),
$$
得到 $\|c_m\|\to0$；$\mathcal B_{m,q}e^{-500d^4}\to0$ 同样成立。
再由 (7.1)、$J_m\to J$ 的真实进位界及 (7.5)，
$$
n_m\longrightarrow Ju=w
$$
于 Hilbert 范数。每个 $n_m$ 属于闭空间 $N$，故 $w\in N$。

这个证明直接处理原实际核向量，没有先投影到缺陷空间。因此不需要、也没有假设缺陷投影保持上述权域。它也不宣称该正则域在整个 $M$ 中已稠密。

## 9. 真正缺陷的全序列亚线性尾限制

本节 $\tau_Q(w)=\|\mathbf1_{\{\mathcal N>Q\}}w\|$ 表示全部物理孔次数尾；从移动高尾孔投影换成这个更大的尾范数只使用集合包含。

若 $0\ne w=Ju\in W=M\ominus N$，(7.5) 和 $n_m\perp w$ 给
$$
\langle J_mc_m,w\rangle\longrightarrow\|w\|^2.
$$
图 $J_m$ 最多降低一次高尾孔，故 $J_mc_m$ 只支持高尾孔数至少 $q$。
$\|J_m\|\le5/4$，因此充分大 $m$ 有
$$
\mathcal B_{m,q}\|r_m\|\tau_{q-1}(w)
\ge\frac25\|w\|^2.
\tag{9.1}
$$
由 (7.3) 的残量界、$\|u\|\le\|w\|$，以及
$\mathcal B_{m,q}e^{-500d^4}\le e^{-498d^4}$，
对充分大 $m$ 得
$$
\boxed{
\mathcal B_{m,q}\tau_{q-2}(w)^2
\ge\frac15\|w\|^2.
}
\tag{9.2}
$$
所以
$$
\log\frac{\|w\|}{\tau_{25d^3-2}(w)}
\le50d^2(1+\log d)+\tfrac12\log5.
\tag{9.3}
$$

相邻 $d=2^m$ 翻倍，次数网格 $25d^3$ 的比值为 $8$。
对夹在两相邻网格间的任意 $Q$，用下一网格处的下界和尾范数单调性，得到
$$
\boxed{
-\log\frac{\tau_Q(w)}{\|w\|}
=O\!\left(Q^{2/3}\log(Q+2)\right)
\quad(Q\to\infty).
}
\tag{9.4}
$$
特别，对每个 $p>2/3$，
$$
-\log(\tau_Q(w)/\|w\|)=o(Q^p).
$$
这是比先前线性指数尾限制更强的必要条件，仍然是尾部不能过快衰减的下界；不是尾部上界，也不排除任意慢的 Hilbert 尾。

## 10. 范围与下一缺口

整个 $\mathcal H_q$ 上的纯创建最小增益可以指数退化；本稿仅在有限阶删除核目标上得到较低成本。完整双和在全层仍可能付很大的范数，所以没有推翻既有环境范围障碍。

新的顶部修复真实存在、保留低孔坐标、保持所需纯高阶核，并接上实际稳定像。其成本已从 $\exp(O(dq))$ 降到 $\exp(O(d^2\log q))$，由此得到 (8.1) 和 (9.4)。

对于没有任何此类次数正则性的实际 $u$，(7.3) 仍未保证 $c_m$ 有有界子列。普通 Hilbert 尾可以慢于该成本的倒数；不能从任意 $r_m\to0$ 断言修复有界。下一有效问题仍是进一步利用真正核/缺陷约束，改善特殊 $r_m$ 的修复成本或给出无权正能量，而非把 (8.1) 的正则域当作已证核内核心。
