# R239 附录：顺次 jet 次数算子的真正投影费用与二步 Schur 精确常数

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：本文的短核次数算子递推、同一裸源度量运输、一般充分条件及 $K=3$ / 裸费 $K=2$ 精确常数均已证明。没有假定短核角度一致，未得原全窗口的一般上界。

本文接[单 dyadic 块导数交织与准确 jet 锚](R239-appendix-single-dyadic-block-derivative-intertwiner-and-exact-jet-anchor.md)中的
$$
\mathfrak N_{K,q}h=\sum_{t=0}^{K-1}(t+1)Q_tP_0D^th.
$$
它明确保留原连续尾、顺次单步 MP 与真幂 MP 的区别；低占据 Fock 旗及有限池对称结果均未被外推到原高孔窗口。

## 1. 固定真实孔层与三个不同的逆

固定原 $D=D_m$。记
$$
D_p=D|_{\mathcal H_p}:\mathcal H_p\to\mathcal H_{p-1},
\quad K_p=\ker D_p,\quad
E_{k,p}=\ker D^k\cap\mathcal H_p.
$$
以下孔层和核阶均为有限数；在原应用中 $q\ge4d$、$1\le K\le d-1$，故没有底层越界。原固定层满射结论保证每个 $D_p^\dagger$ 有界。

对 $1\le s<K$，从 $E_{K-s,q-s}$ 到 $E_{K,q}$ 区别：
$$
\widehat Q_{s,q}
=D_q^\dagger D_{q-1}^\dagger\cdots D_{q-s+1}^\dagger
\quad\text{（顺次单步 MP）},
$$
$$
R_{s,q}
=(D_{q-s+1}\cdots D_q)^\dagger
\quad\text{（真幂 MP）}.
\tag{1.1}
$$
乘积算子在右侧先作用。两者都右逆 $D^s$；一般不相同。
在 primitive 输入 $K_{q-s}$ 上，$\widehat Q_{s,q}$ 就是既有 $Q_s$。

真正最小原像 $R_{s,q}f$ 仍在 $E_{K,q}$：因为
$D^K R_{s,q}f=D^{K-s}f=0$。所以真幂最小化在完整层或限制在 $E_{K,q}$ 内所得最小值相同。

## 2. Taylor 尾投影是有界斜投影

原精确 Taylor 身份为
$$
h=\sum_{t=0}^{K-1}Q_tP_0D^th\qquad(h\in E_{K,q}).
\tag{2.1}
$$
这里不同 $Q_tK_{q-t}$ 的像通常不正交。定义
$$
\boxed{\Pi_{s,K,q}:=\widehat Q_{s,q}D^s|_{E_{K,q}}
=\sum_{t=s}^{K-1}Q_tP_0D^t,\qquad
\Pi_{0,K,q}=I.}
\tag{2.2}
$$
第二式因为顺次 MP 的复合准确接回同一 $Q_t$。因此
$$
\Pi_s^2=\Pi_s,\qquad
\ker\Pi_s=E_{s,q},\qquad
\operatorname{Ran}\Pi_s=\widehat Q_{s,q}E_{K-s,q-s},
$$
$$
\Pi_s\Pi_t=\Pi_{\max(s,t)}.
\tag{2.3}
$$
这些是嵌套斜投影，只有
$$
\Pi_1=D_q^\dagger D_q|_{E_{K,q}}=I-P_0
\tag{2.4}
$$
已由单步 MP 性质自动成为物理正交投影。

次数算子因而准确为
$$
\boxed{\mathfrak N_{K,q}=\sum_{s=0}^{K-1}\Pi_{s,K,q}.}
\tag{2.5}
$$
它不是原孔数算子；每项都作用在同一个第 $q$ 孔层。

## 3. 每个斜投影的最佳范数正是顺次／真幂费用比

在 $E_{K-s,q-s}$ 上记真实 Gram
$$
T_{s,K,q}=\widehat Q_{s,q}^*\widehat Q_{s,q},\qquad
\Gamma_{s,K,q}=R_{s,q}^*R_{s,q}.
$$
令
$$
\boxed{
C_{s,K,q}
=\|\Gamma_{s,K,q}^{-1/2}T_{s,K,q}
\Gamma_{s,K,q}^{-1/2}\|\ge1.}
\tag{3.1}
$$
所有逆均在上述完整短核源空间中读取。则
$$
\boxed{\|\Pi_{s,K,q}\|^2=C_{s,K,q}.}
\tag{3.2}
$$
证明：对 $f=D^sh$，$\Pi_sh=\widehat Q_sf$，而该同源所有 $h$ 的最小物理范数恰为 $\|R_sf\|$。于是比值
$\|\Pi_sh\|^2/\|h\|^2$ 的上确界就是
$\|\widehat Q_sf\|^2/\|R_sf\|^2$；下界由取 $h=R_sf$ 达到上确界意义上的反向。整个证明未交换压缩与取逆。

因此
$$
\boxed{
\|\mathfrak N_{K,q}\|
\le1+\sum_{s=1}^{K-1}\sqrt{C_{s,K,q}}.}
\tag{3.3}
$$
这里 $C_{1,K,q}=1$。对于中间 $1<s<K-1$，(3.1) 的源是整个 $E_{K-s,q-s}$，不只 primitive；只有 $s=K-1$ 的源恰为 $K_{q-K+1}$。所以仅有单个 primitive 最高阶比较不能直接替代 (3.3) 的全部输入。

作为完全明确的充分条件，如果同一原窗口内有实际
$$
T_{s,K,q}\preceq M_{s,K,q}\Gamma_{s,K,q},
$$
则 (3.3) 可将 $C_s$ 换成 $M_s$。这是对原 short-kernel 输出费用的条件，不是把普通相邻 primitive Gram 不等式自动宣称为它。

## 4. 次数递推及同一个首头裸费用

Taylor 公式逐项给
$$
D_q\mathfrak N_{K,q}
=(\mathfrak N_{K-1,q-1}+I)D_q,\qquad
P_0\mathfrak N_{K,q}=P_0.
\tag{4.1}
$$
真正正交分解
$$
E_{K,q}=K_q\oplus D_q^\dagger E_{K-1,q-1}
$$
因此使次数算子准确成为
$$
\boxed{
\mathfrak N_{K,q}
=I_{K_q}\oplus
D_q^\dagger(\mathfrak N_{K-1,q-1}+I)D_q.}
\tag{4.2}
$$
第二块的源内积由 $(D_q^\dagger)^*D_q^\dagger$ 诱导，不能删除。

对首源头 $e_0h$，$h\in E_{K,q}$，原裸和完整右最小费用均为
$$
\alpha_q(e_0h)=\lambda_q(e_0h)=\|D_{q+1}^\dagger h\|.
\tag{4.3}
$$
记这个真正源度量为
$$
W_{K,q}=(D_{q+1}^\dagger|_{E_{K,q}})^*
(D_{q+1}^\dagger|_{E_{K,q}}).
$$
顺次性给准确交织
$$
\boxed{
(\mathfrak N_{K+1,q+1}-I)D_{q+1}^\dagger
=D_{q+1}^\dagger\mathfrak N_{K,q}.}
\tag{4.4}
$$
又 $\mathfrak N_{K+1}-I$ 在 $K_{q+1}$ 上为零、并保持其真实正交补
$D_{q+1}^\dagger E_{K,q}$。故
$$
\boxed{
\|\mathfrak N_{K,q}\|_{W_{K,q}}
=\|\mathfrak N_{K+1,q+1}-I\|_{E_{K+1,q+1}}.}
\tag{4.5}
$$
于是对同一个 $h$，
$$
\boxed{
\alpha_q(e_0\mathfrak N_{K,q}h)
\le\left(\sum_{s=1}^{K}\sqrt{C_{s,K+1,q+1}}\right)
\alpha_q(e_0h).}
\tag{4.6}
$$
完整右普通费用 $\lambda_q$ 有相同结论，因为两个首头源的 (4.3) 均成立。这里没有将 (4.6) 外推到 $\lambda_{\rm flat}$：后者还包含真正左逆 $J_q^{-1}$。

对任意另一个原实际源 $r$，(4.3) 与首头同源右约化给
$$
|\langle e_0\mathfrak N_{K,q}h,PJ_q^{-1}r\rangle|
\le \alpha_q(e_0\mathfrak N_{K,q}h)\,
\|G_q^{1/2}PJ_q^{-1}r\|.
\tag{4.7}
$$
将 (4.6) 代入，只出现原同一个 $h$ 的 $\alpha$ 和原同一个 $r$ 的平坦对偶分量；没有重算或更换平坦源。

## 5. 普通 K=2 与裸费 K=2 必须区分

因为 $\Pi_1=I-P_0$ 物理正交，
$$
\boxed{\mathfrak N_{2,q}=P_0+2(I-P_0),\qquad
\|\mathfrak N_{2,q}\|=2.}
\tag{5.1}
$$
但是 $W_{2,q}$ 一般不约化这个 primitive 分裂。因此 (5.1) 并不证明
$\alpha(e_0\mathfrak N_{2,q}h)\le2\alpha(e_0h)$。其最佳常数由下一孔层的真正二步 Schur 费用确定，下面给精确式。

## 6. 真二步 MP 是顺次二步的原完整 Schur 补

固定输出孔层 $p\ge3$。定义
$$
A=D_p^\dagger|_{K_{p-1}},\qquad
B=D_{p-1}^\dagger|_{K_{p-2}},\qquad
R=D_p^\dagger B,
$$
以及
$$
T=R^*R,\qquad
\Gamma_2=
\left((D_{p-1}D_p)^\dagger|_{K_{p-2}}\right)^*
\left((D_{p-1}D_p)^\dagger|_{K_{p-2}}\right).
$$
$R$ 是顺次二步，$\Gamma_2$ 是真幂二步的实际 primitive 源 Gram。

有物理正交直和
$$
E_{2,p}=K_p\oplus A K_{p-1}.
$$
$R$ 的像与 $K_p$ 正交。因此从 $R$ 中投掉整个 $\ker D^2$，只需投掉 $AK_{p-1}$，得到真正二步最小原像。准确有
$$
\boxed{
\Gamma_2
=T-R^*A(A^*A)^{-1}A^*R.}
\tag{6.1}
$$
所有像均闭，逆和投影均在原完整 Hilbert 空间中定义。

令最佳顺次／真幂比例为
$$
\boxed{C_*(p)=\|\Gamma_2^{-1/2}T\Gamma_2^{-1/2}\|\ge1.}
\tag{6.2}
$$

## 7. 跨 primitive 两块的准确角度

在输入 $E_{2,p-1}=K_{p-1}\oplus B K_{p-2}$ 上，令
$$
\mathsf K=(D_p^\dagger|_{E_{2,p-1}})^*
(D_p^\dagger|_{E_{2,p-1}}),
$$
并按这个原物理正交分解写为 $(\mathsf K_{ij})$。定义
$$
\rho=\|\mathsf K_{00}^{-1/2}\mathsf K_{01}
\mathsf K_{11}^{-1/2}\|<1.
\tag{7.1}
$$
严格小于一来自固定参数下 $\mathsf K$ 的有界严格正性；尚无参数一致的间隙。

用 $B(B^*B)^{-1/2}$ 将第二源块等距识别到 $K_{p-2}$，便有
$$
\mathsf K_{00}=A^*A,\quad
\mathsf K_{01}=A^*R(B^*B)^{-1/2},
$$
$$
\mathsf K_{11}=(B^*B)^{-1/2}T(B^*B)^{-1/2}.
$$
对正的源归一化作合同或使用其极分解，结合 (6.1) 得
$$
\boxed{
\rho^2=
\|T^{-1/2}(T-\Gamma_2)T^{-1/2}\|,\qquad
1-\rho^2=C_*(p)^{-1}.}
\tag{7.2}
$$
因此这里的角度恰是顺次二步被完整真幂最小化消去的比例；不是另一个人为的尾空间角度。

## 8. 一个两块正度量的精确范数计算

在原物理正交两块上，令 $P_0,P_1$ 是两投影，$0<a<b$。
对于正度量 $\mathsf K$ 和 (7.1) 的 $\rho$，
$$
\|aP_0+bP_1\|_{\mathsf K}^2
$$
是满足
$$
\lambda\mathsf K-(aP_0+bP_1)\mathsf K(aP_0+bP_1)\succeq0
$$
的最小 $\lambda$。分别以 $\mathsf K_{00}^{-1/2}$、
$\mathsf K_{11}^{-1/2}$ 合同，二对角块化为
$(\lambda-a^2)I,(\lambda-b^2)I$，非对角块为
$(\lambda-ab)\mathsf C$，$\|\mathsf C\|=\rho$。
所以对 $\lambda\ge b^2$，严格正块 Schur 计算或其极限给准确条件
$$
(\lambda-a^2)(\lambda-b^2)\ge
\rho^2(\lambda-ab)^2.
\tag{8.1}
$$
这里只用交叉算子的范数，不要求有最大奇异向量。

令 $C=(1-\rho^2)^{-1}$，解这个二次式的较大根，得到
$$
\boxed{
\|aP_0+bP_1\|_{\mathsf K}^2
=ab+\frac C2(b-a)^2+
\frac C2(b-a)\sqrt{(b-a)^2+\frac{4ab}{C}}.}
\tag{8.2}
$$

## 9. 普通 N3 与原裸费 N2 的精确常数

由 (4.2)，$\mathfrak N_{3,p}$ 的非primitive 块是在度量
$\mathsf K$ 中的 $2P_0+3P_1$。另一个 primitive 直和块为单位，
而 (8.2) 的值至少九，故
$$
\boxed{
\|\mathfrak N_{3,p}\|^2
=6+\frac{C_*(p)}2
 \left(1+\sqrt{1+\frac{24}{C_*(p)}}\right)
\le C_*(p)+12.}
\tag{9.1}
$$
等价地，以 $\rho$ 表示是
$$
\frac{13-12\rho^2+\sqrt{25-24\rho^2}}
     {2(1-\rho^2)}.
$$
因此普通次数算子 $N_3$ 的一致有界性与 (6.2) 的顺次／真幂二步比较完全等价，且常数准确可换。

对原 $E_{2,q}$ 首头源裸度量 $W_{2,q}$，同一个计算取
$p=q+1,a=1,b=2$，或直接用 (4.5)，得到
$$
\boxed{
\|\mathfrak N_{2,q}\|_{W_{2,q}}^2
=2+\frac{C_*(q+1)}2
 \left(1+\sqrt{1+\frac8{C_*(q+1)}}\right)
\le C_*(q+1)+4.}
\tag{9.2}
$$
这正是同一个 $h$ 上
$$
\alpha_q(e_0\mathfrak N_{2,q}h)^2
\le\|\mathfrak N_{2,q}\|_{W_{2,q}}^2
\,\alpha_q(e_0h)^2
$$
的最佳常数。若 $C_*=1$，(9.1)、(9.2) 分别为 $9$、$4$；
若 $C_*$ 增大，它们都按 $C_*$ 的一阶增长，没有隐藏一个免费的 primitive 正交性。

若另已证明某个上界 $T\preceq C\Gamma_2$，可直接以这个 $C$
替换上述 $C_*$：右侧函数随 $C\ge1$ 增加。这给应用时的明确充分输入。

## 10. 剩余输入及不能作的替换

(3.3)、(4.6)、(9.1)--(9.2) 已把单高块 jet 锚的普通范数与原同源裸费，分别转成完整、可核验的顺次／真幂 MP Gram 比较。对于一般 $K$，必须保留 (3.1) 的整个短核源；对于第一个非正交点，(6.1) 已将未付项准确压为一个真实二步 Schur 补。

目前没有证明这些 $C_{s,K,q}$ 或 $C_*(q)$ 在原连续尾、$q\ge4d$ 的全合法窗口具有目标大小。已有相邻 primitive Gram 不等式若要用于这里，必须先证明它控制的正是 (6.1) 或 (3.1)，不能只因都出现“二步”“primitive”或“Gram”就互换；顺次 MP 与真幂 MP 的差正是本稿保留的费用。

这些界也没有自动运输 $\lambda_{\rm flat}$、删除非齐次物理低锚，或把原 $M$ 图变成物理 dyadic 块。无权 $N=M$ 与普通复 Hilbert ISP 继续开放。
