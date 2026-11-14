# R288 附录：出生一完整精度的显式系数展开与 S2 共同源合同

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下恒等式已证明；一般 S2 正性仍未证明。** 前半部分在任意有限独立正权的一孔物理层直接完成完整 Schur 补；后半部分只作同一个实际下出生源的可逆合同，不以不同高度的不同源替换原比较。它为当前两普通组加一异常位出生二的 S2 提供较小的精确生成式，没有重新启动大规模符号展开。

## 0. 与既有完整 Schur 结果的关系

[R239 倒数权对偶 §7](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)、[R271 首边 §2](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)及[原连续尾全高度稿 §2](R271-appendix-original-birth-one-all-height-polynomial-first-return-anchor.md)已给完整一孔矩阵、Schur/协方差和正边网络。下文 (1.1)、(2.1) 与 Schur 原理仅作这些旧身份的入口，不能重新计为全高度精度存在定理。新增计算扩展是生成函数 (1.2)、统一系数式 (1.3)/(2.2)、保留正秩一项的 C3，以及 §§3–4 同一源下的 S2 恒等式。C1/C2 亦已在 R271/R288 中使用。

## 1. 完整一孔 Gram 的一般系数公式

取 $M\ge2$ 个正权，记
$$
d=\sum_{i=1}^M b_iE_i,\quad z_i=b_i^2,\quad
b=(b_i)_i,\quad S=e_1(z),\quad T=\operatorname{diag}(z_i),
$$
$$
K=b^\perp,\qquad P=I-bb^*/S,\qquad e_j=e_j(z_1,\ldots,z_M),\quad e_0=1.
$$
完整一孔物理矩阵为
$$
F_n=\frac{d^n(d^*)^n}{(n!)^2}\bigg|_{\mathcal H_1}.
$$
从实际输入子集直接读出
$$
(F_n)_{ii}=e_n(z_{\widehat i}),\qquad
(F_n)_{ij}=b_ib_j e_{n-1}(z_{\widehat i\widehat j})\quad(i\ne j).
\tag{1.1}
$$
$n=0$ 时第二式按零读，所以 $F_0=I$。令 $E(t)=\prod_i(1+z_it)$、$v_i(t)=b_i/(1+z_it)$，则作为形式幂级数矩阵，
$$
\boxed{\sum_{n\ge0}F_nt^n
=E(t)\left[\operatorname{diag}\big((1+z_it)^{-2}\big)
+t\,v(t)v(t)^T\right].}
\tag{1.2}
$$
这里 $T$ 是实正对角矩阵，$t$ 只是形式变量；取出的每个矩阵系数仍是实际 Hermitian 矩阵。对角上两项恰合为 $E(t)/(1+z_it)$，非对角上分母直接整除 $E(t)$，故整个右式实际上是次数 $M-1$ 的矩阵多项式。

写
$$
D_n(T)=\sum_{r=0}^n(-1)^r(r+1)e_{n-r}T^r.
$$
逐系数提取 (1.2)，得到完整层身份
$$
\boxed{F_n=D_n(T)
+\sum_{\substack{r,s\ge0\\r+s\le n-1}}
(-1)^{r+s}e_{n-1-r-s}T^r b b^* T^s.}
\tag{1.3}
$$
$n=0$ 时和为空。式子先在完整 $\mathcal H_1$ 成立，尚未作 primitive 压缩。

## 2. 先完整逆后压缩的准确精度

对 $0\le n\le M-2$，$F_n>0$。确切地，$A_n=d^n/n!$ 的伴随若消去 $x$，则每个 $(n+1)$ 元子集上的 $\sum x_i/b_i$ 为零。比较只差一个指标的两个子集，迫全部 $x_i/b_i$ 相同，再由一个子集和迫它们为零。$n=0$ 直接是单位矩阵。

因此真实 primitive Gram 和精度是
$$
\Gamma_n=P F_n^{-1}|_K,\qquad C_n=\Gamma_n^{-1}.
$$
另在比旧合法最高高度多一阶的 $n=M-1$ 硬端，仅按 R275 一位递推的约定置 $C_n=0$；此时不构造不存在的 $F_n^{-1}$ 或 $\Gamma_n$，也不把它增列为一个旧合法 MP 高度。

实际子集计数还给
$$
F_nb=(n+1)\bigl(b_i e_n(z_{\widehat i})\bigr)_i,
\qquad b^*F_nb=(n+1)^2e_{n+1}.
\tag{2.1}
$$
定义
$$
r_a=PT^ab\quad(a\ge1),\qquad
\eta_n=\sum_{a=1}^n(-1)^ae_{n-a}r_a.
$$
则 $PF_nb=(n+1)\eta_n$。在同一个正交分解
$\mathcal H_1=K\oplus\mathbb Cb$ 中，先作完整 Schur 补，准确得到
$$
\boxed{\begin{aligned}
C_n={}&P D_n(T)|_K
+\sum_{\substack{a,c\ge1\\a+c\le n-1}}
(-1)^{a+c}e_{n-1-a-c}\,r_ar_c^*\\
&-\frac{\eta_n\eta_n^*}{e_{n+1}}.
\end{aligned}}
\tag{2.2}
$$
这不是将 $PF_nP$ 当作完整逆的逆。最后的 Schur 项正是该差别。

在硬顶 $n=M-1$，整个 $F_n$ 只有一个输入列，秩一，而 (2.1) 的标量块仍严格正；消去它后的 Schur 补准确为零。所以 (2.2) 亦与 $C_n=0$ 的真实硬端一致，没有对奇异完整层取逆。

### 2.1 前三阶的显式式子

令 $r=r_1$、$t=r_2$、$u=r_3$。则
$$
\boxed{C_1=P(SI-2T)|_K-\frac{rr^*}{e_2},}
$$
$$
\boxed{C_2=P(e_2I-2ST+3T^2)|_K
-\frac{(t-Sr)(t-Sr)^*}{e_3},}
$$
$$
\boxed{\begin{aligned}
C_3={}&P(e_3I-2e_2T+3ST^2-4T^3)|_K+rr^*\\
&-\frac{(-e_2r+St-u)(-e_2r+St-u)^*}{e_4}.
\end{aligned}}
\tag{2.3}
$$
每式只在相应合法高度或所述真实硬顶使用；特别第三式要求 $M\ge4$，$M=4$ 时它准确给零，$M\ge5$ 时给严格正的实际精度。第三式中的正项 $rr^*$ 是完整 $PF_3P$ 的一部分，不能随最后的 rank-one Schur 项丢掉。

## 3. 两普通组加一异常位的共同下出生坐标

回到 $q$ 个平方权 $z$、$L$ 个平方权一和一个平方权 $w$ 的实际模型，$q,L\ge2$。取此前的下出生一聚合源 $E_1=(x-t,y-t)$。记其源 Gram 为 $N=\Lambda_0$，则
$$
\boxed{N=\begin{pmatrix}
\dfrac1L+\dfrac1{qz}&\dfrac1L\\
\dfrac1L&\dfrac1L+\dfrac1w
\end{pmatrix}.}
\tag{3.1}
$$
对标量多项式 $f$，完整对角物理压缩为
$$
\mathcal B(f)=\begin{pmatrix}
f(1)/L+f(z)/(qz)&f(1)/L\\
f(1)/L&f(1)/L+f(w)/w
\end{pmatrix}.
\tag{3.2}
$$
源对 $T^ab$ 的真实配对行恰为
$$
k_a=(z^a-1,\ w^a-1),
$$
因为聚合坐标已保留每组全部物理重数。

令 $P_j=E_{1,\rm phys}^*C_jE_{1,\rm phys}$。非正交源的准确关系是
$$
\boxed{P_j=N\Lambda_j^{-1}N,
\qquad \Lambda_j=NP_j^{-1}N.}
\tag{3.3}
$$
将 (2.3) 逐项压缩，得到
$$
P_1=\mathcal B(S-2X)-k_1^*k_1/e_2,
$$
$$
P_2=\mathcal B(e_2-2SX+3X^2)
-(k_2-Sk_1)^*(k_2-Sk_1)/e_3,
$$
$$
\boxed{P_3=\mathcal B(e_3-2e_2X+3SX^2-4X^3)+k_1^*k_1
-(-e_2k_1+Sk_2-k_3)^*(-e_2k_1+Sk_2-k_3)/e_4.}
\tag{3.4}
$$
这里 $S=qz+L+w$，$e_j=e_j(z^{[q]},1^{[L]},w)$。只用至多四阶的真实计数多项式；不再需要先求三维完整逆、压缩、然后又求二维逆来生成这些精度。

## 4. S2 及两个强列式的共同可逆合同

以下所有式子仍在同一实际旧模型中。沿用上出生二源度量 $U=H_0$、上物理交换子压缩 $h=\widehat H$ 和真实桥
$$
K=\begin{pmatrix}2(z-1)&w-1\\0&z-1\end{pmatrix}.
$$
令
$$
B_0=NK,\qquad
C=h-B_0^*P_2^{-1}B_0=UH_1^{-1}U>0,
$$
$$
M_0=B_0U^{-1}B_0^*,\qquad
E=P_2-B_0h^{-1}B_0^*,
$$
$$
D=P_2N^{-1}P_2-P_2P_1^{-1}P_2P_1^{-1}P_2.
\tag{4.1}
$$
因为 $C>0$、$P_2>0$，块矩阵
$\begin{psmallmatrix}h&B_0^*\\B_0&P_2\end{psmallmatrix}$ 严格正，所以 $h>0$、$E>0$。本节没有先验假定整个物理交换子正；这里只使用它在真实 primitive 源中的上述完整 Schur 身份。

对旧下出生源作同一个可逆变换
$$
\boxed{W=\Lambda_2^{-1}N=N^{-1}P_2.}
\tag{4.2}
$$
它用于整个 S2 缺陷，不分别更换各高度的源。原式中的低出生余量满足
$$
W^*(\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1)W=D.
$$
原两列 $Y=U^{-1}K^*\Lambda_2$、$Z=K^*\Lambda_2\Lambda_3^{-1}\Lambda_2$ 则准确变为
$$
YW=U^{-1}B_0^*,\qquad ZW=B_0^*P_2^{-1}P_3.
\tag{4.3}
$$
所以两个更强列缺陷经过同一个合同后分别为
$$
\boxed{D_{\rm left}
=D-B_0U^{-1}hU^{-1}B_0^*+M_0P_2^{-1}M_0,}
\tag{4.4}
$$
$$
\boxed{D_{\rm right}=D+P_3P_2^{-1}P_3-P_3E^{-1}P_3.}
\tag{4.5}
$$
(4.5) 只用了准确的块逆／Woodbury 身份
$$
P_2^{-1}B_0C^{-1}B_0^*P_2^{-1}=E^{-1}-P_2^{-1}.
$$
全部逆都已付严格正性，次序未改变。

完整 S2 缺陷经过同一合同，进一步准确为
$$
\boxed{\begin{aligned}
D_{\rm S2}={}&D-\frac14\Big[
B_0U^{-1}hU^{-1}B_0^*+P_3E^{-1}P_3\\
&\hspace{23mm}-(M_0-P_3)P_2^{-1}(M_0-P_3)\Big].
\end{aligned}}
\tag{4.6}
$$
证明是将 $\tfrac14(CYW+ZW)^*C^{-1}(CYW+ZW)$ 完整展开，再把含 $P_2^{-1}$ 的三个交叉项合成显示的平方。这里没有删掉坏符号项。

### 4.1 右列交换 Schur 的较小下出生余量

还可使用同一个真实下出生源上的另一可逆变换
$$
T_0=N^{-1}P_1,
\qquad J=P_1N^{-1}P_1-P_2.
$$
准确有
$$
T_0^*D_{\rm low}T_0=J,
\qquad ZT_0=B_0^*P_2^{-1}P_3P_2^{-1}P_1.
\tag{4.7}
$$
旧下出生的普通严格首边已经由实际两组加一异常位定理支付，所以 $D_{\rm low}>0$，进而 $J>0$。记
$$
V_0=P_1P_2^{-1}P_3P_2^{-1}B_0.
$$
对真块矩阵 $\begin{psmallmatrix}C&Z\\Z^*&D_{\rm low}\end{psmallmatrix}$ 作 $\operatorname{diag}(I,T_0)$ 合同，并交换 Schur 补的顺序，得到准确等价
$$
\boxed{D_{\rm low}-Z^*C^{-1}Z\succeq0
\quad\Longleftrightarrow\quad
C-V_0^*J^{-1}V_0\succeq0.}
\tag{4.8}
$$
严格正性也等价。这里右端不请求 $C^{-1}$，下出生逆只作用于显式 $J$；上、下源及次序仍原样保留。它只是一个与原右列等价的新计算入口，尚未证明右端正性。

## 5. 当前用途与未付目标

(3.4)、(4.4)–(4.6) 是另一个准确生成方式；(4.4)、(4.5) 若都正，范数凸性仍给原 S2，(4.6) 若正则直接给原 S2。这里不把“式子更短”当成符号结论。

原已证短侧和出生二 S1 的脚本、证书均保持冻结。本节新生成器只在小型有理模型核对这些共同源身份；没有重复启动原主参数区的大展开，也没有改变已交本库 Actions 请求的代码路径。

## 6. 计算入口与一次有界剖面的准确状态

新[精度生成器](../notes/2026-11-14-two-group-singleton-s2-precision-congruence-789f-next.py)的有理身份检查只核对式子一致，不构成参数区正性证书。[交换Schur剖面](../notes/2026-11-14-s2-right-swapped-bounded-profile-789f-next.json)在45秒/768MiB/禁core限制下超时，只有完整P0–P3输入，未得任何主子式。

另[直接首Gram入口](../notes/2026-11-14-s2-right-complete-first-gram-entry-789f-next.md)用C_form⁻¹=U⁻¹H1U⁻¹避免重求混合二维逆；[其单次剖面](../notes/2026-11-14-s2-right-complete-first-gram-profile-789f-next.json)在0.223秒完成真实输入、23.776秒形成右费用，在同一45秒限制下于费用相减/约分阶段超时，仍无主子式或最终通过事件。两个回执及原始JSONL均保存，未重复本地大展开；原正在运行的Actions输入保持不变。

[旧正边恢复与方法边界](../notes/2026-11-14-birth-one-precision-covariance-and-positive-edge-form-789f-next.md)另保Catalan系数展开与(6,6,1,1)单边标量比较失败例；不把它当作相邻矩阵反例。
