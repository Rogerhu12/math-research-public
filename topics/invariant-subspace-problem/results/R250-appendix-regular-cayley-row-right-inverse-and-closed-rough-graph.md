# R250附录：真实外部行的全阶正则右逆与粗糙图的闭像分解

日期：2026-11-13（UTC+8）。作者：normal_states；固定第 0、1 外部位的精确简化由 Astra-ISP-1cf 提出并经独立核查。状态：已证明的中间结构；未排除正常湮灭者。本稿专门处理 $S=S_Y$，接 [R250](R250-sparse-common-graph-regularization-and-bounded-normal-moment-intertwiners.md) 与[逆阻尼域附录](R250-appendix-zero-inverse-damping-domain-and-exact-cayley-row.md)。

## 1. 设定与准确局部性

取
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_{j\ge0}a_j,\qquad
S=S_Y=\frac{a_\Sigma}{2}I-\frac12\sum_{j\ge0}a_jV_j.
$$
固定 $1/2<\sigma<1$、$0<c\le1$，记 $\beta_j=(j+2)^{-\sigma}$。
取 R250 共同稀疏递归中的无限集 $I$，并要求
$$
\min I\ge2.
\tag{1.1}
$$
令 $\delta_i=1$ 于 $I$，其余为 $\delta_j=c\beta_j$，以及
$$
D\chi_F=\delta_F\chi_F,\qquad
\delta_F=\prod_{j\in F}\delta_j.
$$
$D$ 为有界、正、单射、稠密像的 Walsh 对角收缩。
R248/R250 给出有界的真实算子 $S^+=DSD^{-1}$ 和恒等式
$$
DS=S^+D.
\tag{1.2}
$$
相似记号在有限 Walsh 核上定义，再由有界延拓理解。

令 $H_I$ 为只使用 $I$ 中 Walsh 位的闭子空间，$P=P_I$ 为其正交投影，$Q=I-P$。写
$$
S^+=
\begin{pmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{pmatrix}
\quad\text{相对于 }H_I\oplus H_I^\perp,
\qquad D_{\rm out}=D|_{H_I^\perp}.
\tag{1.3}
$$
对每个外部位 $j\notin I$，令 $R_j:H_I^\perp\to H_I$ 删除唯一外部位 $j$：
$$
R_j\chi_F=
\begin{cases}
\chi_{F\setminus\{j\}},&F\cap I^c=\{j\},\\
0,&\text{其余情形}.
\end{cases}
\qquad
R_jR_k^*=\mathbf1_{\{j=k\}}I_{H_I}.
\tag{1.4}
$$

真实 Cayley 因子的 Walsh 局部矩阵准确为
$$
V_j^+=
\begin{pmatrix}
0&-\delta_j^{-1}I\\
\delta_jI&2s_j^+
\end{pmatrix},\qquad
s_j^+=(I+\eta_jN_{j+1}^+)(I-\eta_jN_{j+1}^+)^{-1}.
\tag{1.5}
$$
这里两行两列按第 $j$ 位的 $1,\chi_j$ 排列，$s_j^+$ 只作用于严格高于 $j$ 的位。
因此 $V_j^+$ 固定所有低于 $j$ 的 Walsh 位。
特别，输入第 $j$ 位为空时，输出准确为创建该位并乘 $\delta_j$，不触发任何 carry；
删除第 $j$ 位的矩阵元也准确为 $-\delta_j^{-1}I$。
这些是实际算子式，不是纯模型近似。

## 2. 固定外部位 0 给出全阶正则右逆

由 (1.1)，位 0 在外部。对 $u\in H_I$，考察 $R_0^*u=\chi_0u$。
当 $j\ge1$ 时，$V_j^+$ 保留位 0，所以
$$
PV_j^+R_0^*=0\qquad(j\ge1).
$$
当 $j=0$ 时，(1.5) 给
$$
V_0^+R_0^*u=-\delta_0^{-1}u+2\chi_0s_0^+u.
$$
第二项仍有外部位 0，因而被 $P$ 杀掉。恒等项同样被 $P$ 杀掉，故
$$
\boxed{S_{12}R_0^*=\frac{a_0}{2\delta_0}I_{H_I}.}
\tag{2.1}
$$
于是
$$
\boxed{
Z=\frac{2\delta_0}{a_0}R_0^*,\qquad
S_{12}Z=I_{H_I},\qquad
\|Z\|=\frac{2\delta_0}{a_0}.
}
\tag{2.2}
$$
这是整个真实行 $S_{12}$ 的右逆，不需要小误差 Neumann 修正，也不需要额外限制 $\sigma<3/4$。

$Z$ 的像只含固定外部位 0，内部位的阻尼全部为 1。
因此对每个固定实数 $r>0$，
$$
\boxed{
ZH_I\subset\operatorname{Dom}D_{\rm out}^{-r},\qquad
D_{\rm out}^{-r}Z
=\frac{2\delta_0^{1-r}}{a_0}R_0^*
\in B(H_I,H_I^\perp).
}
\tag{2.3}
$$
特别
$$
D_{\rm out}^{-1}Z=\frac2{a_0}R_0^*.
\tag{2.4}
$$
域陈述可由任意有限 Walsh 部分和直接取极限，或由 $D_{\rm out}^{-r}$ 的闭性得到。

## 3. 核图分解与剩余图的零反阻尼域

设 $L:H_I\to H_I^\perp$ 有界，且
$$
u+Lu\in\ker S^+\qquad(u\in H_I).
\tag{3.1}
$$
R250 的假想正常正湮灭者会产生这样的图；本节只用 (3.1)。
其两个块方程为
$$
S_{11}+S_{12}L=0,\qquad S_{21}+S_{22}L=0.
\tag{3.2}
$$
定义
$$
\boxed{
L_{\rm reg}=-ZS_{11},\qquad
L_{\rm rough}=(I-ZS_{12})L=L+ZS_{11}.
}
\tag{3.3}
$$
于是
$$
L=L_{\rm reg}+L_{\rm rough},\qquad
S_{12}L_{\rm rough}=0.
\tag{3.4}
$$
由 (2.3)，对所有固定 $r>0$，
$$
L_{\rm reg}H_I\subset\operatorname{Dom}D_{\rm out}^{-r},\qquad
D_{\rm out}^{-r}L_{\rm reg}
=-\frac{2\delta_0^{1-r}}{a_0}R_0^*S_{11}
\in B(H_I,H_I^\perp).
\tag{3.5}
$$
所以正则补偿完全位于固定外部位 0，任何固定阶的反阻尼都可支付。

原 $S_Y$ 已证全空间单射。若 $Lu\in\operatorname{Ran}D_{\rm out}$，则 $u+Lu=Dv$ 对某个 $v\in H$ 成立。
由 (1.2)、(3.1)，$DSv=S^+Dv=0$。
$D$ 与 $S$ 都单射，故 $v=0$，再投影到 $H_I$ 得 $u=0$。
因此
$$
\operatorname{Dom}(D_{\rm out}^{-1}L)=\{0\}.
\tag{3.6}
$$
减去全域正则的 (3.5)，得到
$$
\boxed{
\operatorname{Dom}(D_{\rm out}^{-1}L_{\rm rough})=\{0\}.
}
\tag{3.7}
$$
等价地，$\operatorname{Ran}L_{\rm rough}\cap\operatorname{Ran}D_{\rm out}=\{0\}$，且 $L_{\rm rough}$ 单射。
对 $r\ge1$ 同样有 $\operatorname{Dom}(D_{\rm out}^{-r}L_{\rm rough})=\{0\}$。
不由此断言 $0<r<1$ 时的相应结论。

## 4. 固定外部位 1 强迫剩余图有下界

位 1 也在外部。先计算从 $H_I$ 到“唯一外部位 1”这一行。
对 $u\in H_I$，$V_1^+u=\delta_1\chi_1u$。
$V_0^+u=\delta_0\chi_0u$，被 $R_1$ 杀掉。
对 $j\ge2$，$V_j^+$ 保留位 1 为空，也被 $R_1$ 杀掉。
恒等项没有外部位。因此
$$
\boxed{R_1S_{21}=-\frac{a_1\delta_1}{2}I_{H_I}.}
\tag{4.1}
$$

其次，从输入 $R_0^*u=\chi_0u$ 出发，所有 $V_j^+$、$j\ge1$ 都保留位 0，故无法输出唯一外部位 1。
$V_0^+$ 删除位 0 的那一项是 $-\delta_0^{-1}u\in H_I$，先被 $Q$ 杀掉；
另一项 $2\chi_0s_0^+u$ 保留位 0，仍被 $R_1$ 杀掉。
所以准确有
$$
\boxed{R_1S_{22}R_0^*=0.}
\tag{4.2}
$$
此处即使 $s_0^+$ 在高位产生任意真实 carry，位 0 仍留在该项中，故结论不受影响。

令
$$
F=S_{21}-S_{22}ZS_{11}:H_I\longrightarrow H_I^\perp.
\tag{4.3}
$$
结合 (2.2)、(4.1)、(4.2)，
$$
\boxed{R_1F=-\frac{a_1\delta_1}{2}I_{H_I},\qquad
\|Fu\|\ge\frac{a_1\delta_1}{2}\|u\|.}
\tag{4.4}
$$
另一方面，(3.2)、(3.3) 给
$$
S_{22}L_{\rm rough}=-F.
\tag{4.5}
$$
于是
$$
\boxed{
\|L_{\rm rough}u\|
\ge\frac{a_1\delta_1}{2\max(1,\|S_{22}\|)}\|u\|
=\frac{c\,3^{-\sigma}}{8\max(1,\|S_{22}\|)}\|u\|.
}
\tag{4.6}
$$
所以 $L_{\rm rough}$ 有闭像、无限秩且非紧；其每个非零像向量都不属于 $\operatorname{Ran}D_{\rm out}$。
下界直接来自两个固定外部位的真实通道，不使用 UHF 逼近或抽象正数 $\|D_cSg_0\|$。
除 $I\cap\{0,1\}=\varnothing$ 外，本节不需再把 $I$ 向高处调整。

## 5. 可选：分散于所有单外部位的另一种右逆

这一节保留早先的加权最小范数构造；它不用于第 2–4 节的主结论。
额外假设 $1/2<\sigma<3/4$，置
$$
B_I^2=\sum_{j\notin I}\frac{a_j^2}{\beta_j^2},\qquad
C_I^2=\sum_{j\notin I}\frac{a_j^2}{\beta_j^4}<\infty.
$$
R250B 给
$$
S_{12}=A_c+\mathcal E_I,\qquad
A_c=\frac1{2c}\sum_{j\notin I}\frac{a_j}{\beta_j}R_j,
\qquad
\|\mathcal E_I\|\le\frac12\sum_{i\in I}a_i e_i(c),
$$
其中固定 $c$ 时 $e_i(c)\to0$。
令
$$
Z_0=\frac{2c}{B_I^2}\sum_{j\notin I}\frac{a_j}{\beta_j}R_j^*.
$$
由 (1.4)，
$$
A_cZ_0=I,\qquad \|Z_0\|=\frac{2c}{B_I},\qquad
D_{\rm out}^{-1}Z_0
=\frac2{B_I^2}\sum_{j\notin I}\frac{a_j}{\beta_j^2}R_j^*,
\qquad
\|D_{\rm out}^{-1}Z_0\|=\frac{2C_I}{B_I^2}.
$$
两级数均由正交行关系按算子范数收敛；逆阻尼域结论再用闭性。
若把 $I$ 取得足够高，使 $\|\mathcal E_I Z_0\|\le1/2$，则
$$
Z_{\rm av}=Z_0(I+\mathcal E_I Z_0)^{-1}
$$
也是实际右逆，满足
$$
S_{12}Z_{\rm av}=I,\qquad
\|Z_{\rm av}\|\le\frac{4c}{B_I},\qquad
\|D_{\rm out}^{-1}Z_{\rm av}\|\le\frac{4C_I}{B_I^2}.
$$
其像只有一个外部位，但可分散在所有外部位置。
固定位置右逆 (2.2) 的优势是没有 $\sigma<3/4$ 限制，并有全部固定阶的逆阻尼域。

## 6. 当前剩余缺口

假想正常正湮灭者所产生的核图，必须分成一个真实行的全阶反阻尼正则补偿，以及一个落在 $\ker S_{12}$、有下界、闭像、非紧且一阶反阻尼域为零的剩余图。
本稿没有证明后者不能存在。
常数 (4.6) 依赖 $c$，且 $\|S_{22}\|$ 可以随 $c$ 增长，因此不与 R250 的任意小图范数矛盾。
图的这个分解也不自动给 $A^+$ 不变性或交换关系。

后续仍须利用更高正常矩及正性排除剩余图，或为原见证构造 R244 所需且 $\phi(R)\ne0$ 的有界交换配对正则器。
普通 ISP 与完整的正常湮灭者排除均未在这里完成。

