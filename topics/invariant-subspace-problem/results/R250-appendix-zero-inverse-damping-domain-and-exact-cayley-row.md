# R250附录：正常核图的逆阻尼域为零及真实 Cayley 外部行成本

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d、normal_states。状态：已证明，中间结论。

本文接续 [R250](R250-sparse-common-graph-regularization-and-bounded-normal-moment-intertwiners.md) 及[近投影附录](R250-appendix-normal-moments-near-coordinate-projections-and-kernel-graphs.md)。两个实际慢符号都满足下述一般闭图约束；第二部分的精确单个位行与正常第一矩成本专用于 $S_Y$。这些结论仍以非零正正常湮灭者存在为条件，并未构造这样的湮灭者。

## I. 两个实际模型共有的逆阻尼域障碍

### I.1 设定与结论

在原 Haar 空间取 $S=S_N$ 或 $S_Y$，其中
$$
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jY_j,\qquad a_j=(j+1)^{-2}.
$$
原 $S$ 已证单射。令 $D$ 是 R250 的正 Walsh 对角阻尼，$D\chi_F=\delta_F\chi_F$，且无限集 $I$ 上 $\delta_i=1$；在其余位 $\delta_j=c(j+2)^{-\sigma}$，$0<c\le1$、$1/2<\sigma<1$。因此 $D$ 有界、正、单射且有稠密像。真实有界变形满足
$$
DS=S^+D.
\tag{D.1}
$$

记 $\mathcal H_I=\overline{\operatorname{span}}\{\chi_F:F\subset I,\ F\text{有限}\}$，$P=P_I$、$P_\perp=I_H-P$、$D_\perp=D|_{\mathcal H_I^\perp}$。这里 $I_H$ 是恒等算子，以免与指标集 $I$ 混淆。$DP=PD=P$。

若 $\phi$ 是非零正正常泛函且 $\phi(S\mathcal A)=0$，近投影附录可以选择上述 $I,D$，使
$$
\mathcal G(L)=\{u+Lu:u\in\mathcal H_I\}\subset\ker S^+,
\qquad L\in B(\mathcal H_I,\mathcal H_I^\perp),
\tag{D.2}
$$
且 $\|L\|$ 任意小。每次选择中的 $I,D,S^+$ 允许随所需小量改变。该构造还可要求 $I$ 避开任意预先指定的有限前缀：递归每一步仅增加有限个高位极限条件，不影响既有证明。

**定理。** 对上述任一实际核图，都有
$$
\operatorname{Dom}(D_\perp^{-1}L)=\{0\},\qquad
\operatorname{Ran}L\cap\operatorname{Ran}D_\perp=\{0\}.
\tag{D.3}
$$
把 $I$ 选得避开足够长的有限前缀后，$L$ 还有严格正下界，因而有闭像且不紧。并且稠密定义算子
$$
\mathcal T=L^*D_\perp^{-1}:
\operatorname{Ran}D_\perp\subset\mathcal H_I^\perp\longrightarrow\mathcal H_I
\tag{D.4}
$$
满足
$$
\operatorname{Dom}\mathcal T^*=\{0\},\qquad
\overline{\operatorname{Graph}\mathcal T}
=\mathcal H_I^\perp\oplus\mathcal H_I.
\tag{D.5}
$$
这里 $L^*$ 是通常 Hilbert 伴随，不是 $C$ 转置。甚至把 (D.4) 的定义域限制到有限 Walsh 多项式，图闭包仍是 (D.5) 的整个直和。

### I.2 逆阻尼域准确为零

首先，由 (D.1) 和两个单射算子 $D,S$，
$$
\ker S^+\cap\operatorname{Ran}D=\{0\}.
\tag{D.6}
$$
事实上，若 $x=Dy$ 且 $S^+x=0$，则 $DSy=0$，故 $Sy=0$、$y=0$、$x=0$。

对于 $u\in\mathcal H_I$，因为 $D|_{\mathcal H_I}=I_H$ 且 $D$ 保持正交分解，
$$
u+Lu\in\operatorname{Ran}D
\quad\Longleftrightarrow\quad
Lu\in\operatorname{Ran}D_\perp.
$$
结合 (D.2)、(D.6)，后者只能在 $u=0$ 时成立。这同时证明 (D.3) 的第一式和 $L$ 的单射性；于是第二式也成立。这里没有把 $D^{-1}$ 应用到未属于其定义域的非零核向量。

### I.3 真实高位压缩使图有严格正下界

令 $\sigma_0=\langle S1,1\rangle$、$a_\Sigma=\sum_ja_j$。对 $S_Y$，$V_j1=\chi_j$，故
$$
\sigma_0=\frac{a_\Sigma}{2}>0.
$$
对 $S_N$，实际 $N_j$ 保函数非负锥，且其真实局部式
$N_j=E_j+\eta_jE_j^*N_{j+1}$ 给
$\langle N_j1,1\rangle\ge\langle E_j1,1\rangle=1/2$。
因此同样有 $\sigma_0\ge a_\Sigma/2>0$。这里采用原 Haar 表示的正函数锥，与正常密度的 Hilbert 正性不是同一假设。

原 $S$ 属于 UHF 局部算子的范数闭包。选一个只作用于前 $r$ 位的局部算子 $S_r$，使
$$
\|S-S_r\|<\sigma_0/4.
$$
若 $I\cap[0,r)=\varnothing$，$\mathcal H_I$ 在前 $r$ 位只有常数参考向量，故
$$
PS_rP=\langle S_r1,1\rangle P.
$$
另一方面，对 $u\in\mathcal H_I$，(D.1) 给
$PS^+u=PDSu=PSu$。于是
$$
S_{11}:=PS^+|_{\mathcal H_I}=PS|_{\mathcal H_I},
\qquad
\|S_{11}-\sigma_0 I_{\mathcal H_I}\|<\sigma_0/2.
\tag{D.7}
$$
故 $S_{11}$ 可逆且 $\|S_{11}u\|\ge(\sigma_0/2)\|u\|$。

设 $S_{12}=PS^+|_{\mathcal H_I^\perp}$。对核图取第一分量，得到
$$
S_{11}+S_{12}L=0.
\tag{D.8}
$$
$S_{12}$ 必非零，且
$$
\boxed{\|Lu\|\ge\frac{\sigma_0}{2\|S_{12}\|}\|u\|.}
\tag{D.9}
$$
因此 $L$ 的像闭。由于 $I$ 无限，$\mathcal H_I$ 无限维；有正下界的 $L$ 不可能紧。顺带，
$$
S_{12}(-LS_{11}^{-1})=I_{\mathcal H_I},
\tag{D.10}
$$
所以这个实际外部行还是满射，并有明确有界右逆。估计 (D.9) 只对固定构造中的 $S^+$ 使用，未赋予全体变形统一范数。

### I.4 伴随域与整个直和的图闭包

$E=D_\perp^{-1}$ 是定义在 $\operatorname{Ran}D_\perp$ 上的正自伴算子：在外部 Walsh 基上，其谱值为 $\delta_F^{-1}$，自然定义域为
$$
\operatorname{Dom}E
=\left\{x:\sum_{F\not\subset I}\delta_F^{-2}|x_F|^2<\infty\right\}.
$$
该域稠密，有限 Walsh 多项式为 $E$ 的图核心。

因 $L$ 有界，通常伴随的定义直接给
$$
(L^*E)^*=EL,\qquad
\operatorname{Dom}(L^*E)^*
=\{u\in\mathcal H_I:Lu\in\operatorname{Dom}E\}.
\tag{D.11}
$$
也可直接验证：$x\mapsto\langle Ex,Lu\rangle$ 在 $\operatorname{Dom}E$ 上对 $\|x\|$ 有界，当且仅当 $Lu\in\operatorname{Dom}E^*=\operatorname{Dom}E$。由 (D.3)，(D.11) 的域只有零。

稠密定义算子的一般图正交公式现在给
$$
(\operatorname{Graph}\mathcal T)^\perp
=\{(-\mathcal T^*u,u):u\in\operatorname{Dom}\mathcal T^*\}
=\{0\}.
$$
于是得到 (D.5)。若 $x\in\operatorname{Dom}E$，有限 Walsh 截断 $x_n$ 满足 $x_n\to x$、$Ex_n\to Ex$，从而 $L^*Ex_n\to L^*Ex$。所以有限 Walsh 限制具有同一图闭包。

特别，对每个 $u\in\mathcal H_I$，存在有限外部 Walsh 多项式 $x_n$ 使
$$
x_n\to0,\qquad L^*D_\perp^{-1}x_n\to u.
\tag{D.12}
$$
这准确说明了撤阻尼时的全多值图障碍；它不是原表示上一个已定义的有界交换正则器，也不能把非零核图回传成原 $S$ 的核。

## II. 真实 Cayley 模型的精确行与定量成本

以下只取 $S=S_Y$。保留全部真实 carry，不把纯局部公式当作完整算子。

### II.1 设定和准确局部式

记
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_ja_j,\qquad
S=S_Y=\sum_ja_jY_j
=\frac{a_\Sigma}{2}I-\frac12\sum_ja_jV_j.
$$
固定 $1/2<\sigma<1$、$0<c\le1$、无限稀疏集 $I$，令
$$
\beta_j=(j+2)^{-\sigma},\qquad
\delta_j=1\ (j\in I),\qquad
\delta_j=c\beta_j\ (j\notin I).
$$
$D\chi_F=\delta_F\chi_F$，$S^+=DSD^{-1}$ 为 R248/R250 的有界实际变形。
设 $P=P_I$ 投影到 $H_I$，$Q=I-P$。

R237 的真实 Walsh 局部矩阵为
$$
V_j=\begin{pmatrix}0&-I\\I&2s_j\end{pmatrix},\qquad
s_j=(I+\eta_jN_{j+1})(I-\eta_jN_{j+1})^{-1}.
$$
相似后准确得到
$$
\boxed{
V_j^+=
\begin{pmatrix}
0&-\delta_j^{-1}I\\
\delta_j I&2s_j^+
\end{pmatrix}.
}
\tag{Y.1.1}
$$
$s_j^+$ 只作用在第 $j$ 位之后。它由真实局部相似定义，亦等于
$(I+\eta_jN_{j+1}^+)(I-\eta_jN_{j+1}^+)^{-1}$。
逆存在来自实际 $N_{j+1}^+$ 拟幂零；不要求所有低位都满足
$\eta_j\|N_{j+1}^+\|<1$。

### II.2 外部位的行没有 carry

对 $j\notin I$，定义 $R_j:H_I^\perp\to H_I$：
$$
R_j\chi_F=
\begin{cases}
\chi_{F\setminus\{j\}},&F\cap I^c=\{j\},\\
0,&\text{其余情形}.
\end{cases}
$$
则
$$
R_jR_k^*=\mathbf1_{\{j=k\}}I_{H_I}.
\tag{Y.2.1}
$$
因为输出属于 $H_I$ 必须在外部位 $j$ 为0，$P$ 只取 (Y.1.1) 的第一行。
第一行的 $00$ 块准确为零，$01$ 块准确为
$-\delta_j^{-1}I$，并不含 $s_j^+$。因此
$$
\boxed{
PV_j^+P=0,\qquad PV_j^+Q=-\delta_j^{-1}R_j
\qquad(j\notin I).
}
\tag{Y.2.2}
$$
这同时说明：若输入有两个以上外部 Walsh 位，或者唯一外部位不等于 $j$，
这一行完全为零。全部真实 carry 都在另一行，不能进入 (Y.2.2)。

### II.3 内部位的 carry 可由稀疏选择统一控制

令 $D_j^0=I-2E_j$ 为纯局部 Cayley 因子。对于 $j\in I$，
它保持 $H_I$ 与 $H_I^\perp$，故
$$
P D_j^0Q=0.
$$

R171 的真实局部展开给
$$
V_j=D_j^0+\sum_{r\ge j+1}B_{j,r},\qquad
\operatorname{supp}B_{j,r}\subset[j,r],\qquad
\|B_{j,r}\|\le18\,\frac{\alpha_r}{\alpha_j}.
$$
这里只对 $r>j$ 使用
$$
\frac{\alpha_r}{\alpha_j}\le e^{-770\,16^{r-1}}.
$$
长度 $r-j+1$ 的有限局部相似条件数至多
$$
\prod_{\ell=j}^r\delta_\ell^{-1}
\le c^{-(r-j+1)}(r+2)^{\sigma(r-j+1)}.
$$
因此对 $j\in I$，
$$
\boxed{
\|V_j^+-D_j^0\|\le e_j(c),
}
$$
$$
e_j(c)=18\sum_{r\ge j+1}
c^{-(r-j+1)}(r+2)^{\sigma(r-j+1)}
e^{-770\,16^{r-1}}.
\tag{Y.3.1}
$$
固定任意 $c>0$ 后，$e_j(c)\to0$。
严格地，用 $r-j+1\le r+1$、$\sigma<1$ 可将其统一上界取为
$$
18\sum_{r\ge j+1}
\bigl(c^{-1}(r+2)\bigr)^{r+1}e^{-770\,16^{r-1}},
$$
这是一个绝对收敛正项级数的尾。

R250 递归选择高位时，可以同时加入
$$
\sum_{j\in I}a_j<\theta,\qquad
\frac12\sum_{j\in I}a_je_j(c)<\epsilon
\tag{Y.3.2}
$$
这两个条件：每一步只需把新位取得更高，并按可和预算分配。
不影响此前有限多个紧行和有限矩阵极限条件。
必须先固定 $c$；没有声称 $e_j(c)$ 对 $c\downarrow0$ 统一。

### II.4 两个块的准确公式

记
$$
S_{11}=PS^+|_{H_I},\qquad
S_{12}=PS^+|_{H_I^\perp}.
$$
因为 $DP=P$、$PD=P$，在内部位上
$PV_j^+P=PV_jP$。结合 (Y.2.2)，得到
$$
\boxed{
S_{11}=\frac{a_\Sigma}{2}I_{H_I}
-\frac12\sum_{i\in I}a_iPV_iP.
}
\tag{Y.4.1}
$$
原 $\|V_i\|\le6$ 给
$$
\left\|S_{11}-\frac{a_\Sigma}{2}I\right\|
\le3a_I,\qquad a_I=\sum_{i\in I}a_i.
\tag{Y.4.2}
$$
若 $a_I<a_\Sigma/6$，则 $S_{11}$ 可逆且
$$
\|S_{11}u\|\ge(a_\Sigma/2-3a_I)\|u\|.
\tag{Y.4.3}
$$

外部行则为
$$
\boxed{
S_{12}=
\frac12\sum_{j\notin I}\frac{a_j}{\delta_j}R_j+\mathcal E_I,
\qquad
\mathcal E_I=-\frac12\sum_{i\in I}a_iPV_i^+Q.
}
\tag{Y.4.4}
$$
由本部分第3节，
$$
\|\mathcal E_I\|\le\frac12\sum_{i\in I}a_ie_i(c).
\tag{Y.4.5}
$$
这只有无阻尼内部位的 carry 误差。

设
$$
B_I=\left(\sum_{j\notin I}\frac{a_j^2}{\beta_j^2}\right)^{1/2}<\infty.
$$
由 (Y.2.1)，主行算子的范数准确为
$$
\boxed{
\left\|\frac12\sum_{j\notin I}\frac{a_j}{\delta_j}R_j\right\|
=\frac{B_I}{2c}.
}
\tag{Y.4.6}
$$
其算子范数收敛也由同一个 $\ell^2$ 行关系保证。
故
$$
\|S_{12}\|\le\frac{B_I}{2c}+\|\mathcal E_I\|.
\tag{Y.4.7}
$$
这里精确控制的是这个行块，不是整个 $S^+$ 的范数。
低位的长 carry 在整个算子中仍可支付多于 $c^{-1}$ 的成本，
但它们被 (Y.2.2) 的行结构准确删除。

### II.5 任一核图的下界

假设 $L:H_I\to H_I^\perp$ 有界，且
$$
u+Lu\in\ker S^+\qquad(u\in H_I).
$$
取 $P$ 分量给真实图方程
$$
S_{11}+S_{12}L=0.
\tag{Y.5.1}
$$
由 (Y.4.3)、(Y.4.7)，
$$
\boxed{
\|Lu\|\ge
\frac{a_\Sigma/2-3a_I}
{B_I/(2c)+\|\mathcal E_I\|}\,\|u\|.
}
\tag{Y.5.2}
$$
所以只要 $a_I<a_\Sigma/6$，$L$ 单射、具有闭像且非紧。
这与 R250 的任意小图范数相容：小参数 $c$ 同时出现在 (Y.5.2) 的下界中。

此外，$D$ 在 $H_I$ 上为恒等，并保持 $H_I^\perp$。
若某个非零 $u$ 有 $Lu\in\operatorname{Ran}(D|_{H_I^\perp})$，
则 $u+Lu\in\operatorname{Ran}D\cap\ker S^+$。
由 $DS=S^+D$、$D$ 单射和原 $S$ 单射，这个交只有零，
与投影到 $H_I$ 得到 $u\ne0$ 矛盾。因此
$$
\operatorname{Ran}L\cap\operatorname{Ran}(D|_{H_I^\perp})=\{0\}.
\tag{Y.5.3}
$$
这与第一部分的通用逆阻尼域结论一致。

### II.6 单独的正常第一矩成本

对正正常 $\phi$，令 $\lambda=\phi(I)>0$、
$m_j=\phi(V_j)$。
若 $\phi(S_Y\mathcal A)=0$，取测试 $I$ 即有准确恒等式
$$
\sum_ja_jm_j=a_\Sigma\lambda.
\tag{Y.6.1}
$$
这是原实际 Cayley 符号的等式，完全没有 carry 误差。

因为 $\|\phi\|=\lambda$、$\|V_j\|\le6$，
$$
\left|\sum_{j\notin I}a_jm_j\right|
\ge\lambda(a_\Sigma-6a_I).
$$
加权 Cauchy–Schwarz 给
$$
\boxed{
\left(\sum_{j\notin I}\beta_j^2|m_j|^2\right)^{1/2}
\ge\lambda\,\frac{a_\Sigma-6a_I}{B_I}.
}
\tag{Y.6.2}
$$
R250 的第一列在外部单个位上的系数为
$-c\beta_jm_j$。故
$$
\boxed{
\|H_{\phi,\delta}-\lambda P_I\|
\ge c\lambda\,\frac{a_\Sigma-6a_I}{B_I}.
}
\tag{Y.6.3}
$$
若右边的分子为正，这显示对于真正的湮灭者，
近投影误差不能在固定这些权的同时免费提升为 $o(c)$。
它没有与已证明的 $O(c)$ 上界发生矛盾，也没有排除所有正常湮灭者。


## III. 保留的开放量词

同一 R250 递归可以同时支付第一部分的有限前缀回避、第二部分的内部系数质量和真实 carry 误差，以及全部正常矩与紧合成条件。故上述结论适用于同一个实际适配变形。

一方面，核图可以任意小；另一方面，固定该变形后，图算子有严格正下界，其每个非零像都在逆阻尼域之外。Cayley 的外部行和第一矩进一步给与 $c$ 同阶的必要成本。两者相容，不能仅由任意小图或近投影推出湮灭者矛盾。还须使用更强的正常矩结构，或完成 R244 的指定输入配对正则器；一般正正常湮灭者和普通 ISP 均未决定。
