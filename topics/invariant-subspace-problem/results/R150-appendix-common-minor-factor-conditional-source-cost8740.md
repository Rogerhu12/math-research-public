# R150 附录：消去已知最大子式公共因子后的条件来源界 8740

作者：Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15 UTC。

**状态：完整证明一个条件性降度结论。** 对每个原目标 $b_j=h_0t_j$，若它在原 $\mathbb Q[s]$ 来源模中，则存在原来源成本至多 $8740$ 的解。这里没有证明这些成员性，也没有证明固定的 $31$ 分母指数足够。改进来自同时消去所有换基最大子式中已经证明的公共因子，不是将其误称为完整最大子式 gcd。

## 1. 同一原矩阵、子式和实际次数下界

按原来源为列定向，令

$$
A(s)\in\operatorname{Mat}_{4367\times6188}(\mathbb Z[s]),
\qquad \operatorname{rank}_{\mathbb Q(s)}A=4354.
$$

使用[原子式条件降度证明](R150-appendix-original-projective-minor-conditional-source-cost8814.md)中的同一来源集合 $J$、输出集合 $I$ 和非零方阵

$$
B=A_{I,J},\qquad D=\det B,\qquad
H=\sum_{\ell\in J}a_\ell-\sum_{i\in I}b_i=8770.
$$

原权和成本仍为

$$
a_\ell=
\begin{cases}
20+10|\alpha|,&\text{来源 }m^\alpha N_i,\\
25+10|\alpha|,&\text{来源 }m^\alpha\Gamma_i,
\end{cases}
\qquad b_i=10|\beta_i|,
\qquad \delta_\ell=a_\ell-10.
$$

这里 $|\alpha|\le3$，故 $\max_\ell a_\ell=55$、$\max_\ell\delta_\ell=45$。来源向量 $x$ 的成本是

$$
\operatorname{cost}(x)=
\max_{x_\ell\ne0}\bigl(\deg x_\ell+\delta_\ell\bigr).
$$

所有式子保留全部 $4367$ 输出，不只处理所选输出 $I$。

[原自然射影子式证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)已证明

$$
K_h\mid\text{每个原 }4354\text{ 阶齐次子式},
\qquad \deg K_h=74,
$$

其中

$$
K_h=s^{14}t^{14}(s-2t)^9(s+6t)^9
F_{+,h}^{\,2}F_{-,h}^{\,2}E_{8,h}^{\,2}.
$$

置

$$
K(s)=K_h(s,1)
=s^{14}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2,
\qquad \deg K=60.
\tag{1.1}
$$

已证无穷远全矩阵秩为 $4340$，故每个最大子式的自然齐次式在无穷远至少消失 $14$ 阶。因此

$$
K\mid D,\qquad \deg D\le H-14.
$$

还可以使用一个此前条件界没有用尽的**实际下界**。同一 $D$ 在模 $31$ 的源点 $4$ 非零；[完整仿射挠空间计算](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)已证明全部原最大子式的模 $31$ 仿射 gcd 次数为 $315$。这个 gcd 整除非零的 $\overline D$，于是

$$
\deg D\ge\deg\overline D\ge315.
\tag{1.2}
$$

这一步没有把模 $31$ 的 $315$ 次因子提升成特征零因子；只用了非零约化不能提高多项式次数。

定义

$$
d_*(s)=D(s)/K(s),\qquad q=\deg d_*.
$$

由 (1.1)、(1.2) 得到

$$
\boxed{255\le q\le H-74=8696.}
\tag{1.3}
$$

这里的 $d_*$ 是选定子式除以一个已证公共因子，不是完整模的最小分母。

## 2. 所有来源列的换基式都可以准确除以 $K$

对任一原来源列 $A_\ell$，令

$$
E_\ell=\operatorname{adj}(B)\,(A_\ell)_I.
$$

其第 $j$ 项恰是将 $B$ 第 $j$ 列换为 $(A_\ell)_I$ 的行列式；若产生重复列，该项为零。因此每一项都是一个原最大子式，保留相应原行列权。由 (1.1)

$$
P_\ell:=E_\ell/K\in\mathbb Q[s]^{4354}.
\tag{2.1}
$$

由于换列后的自然齐次次数为 $H-a_j+a_\ell$，其最大子式仍至少含无穷远因子 $t^{14}$，从而

$$
\boxed{
\deg (P_\ell)_j\le H-a_j+a_\ell-74.
}
\tag{2.2}
$$

这同时用了有限公共因子次数 $60$ 和无穷远最少阶 $14$，没有重复计算同一个因子。

在全部原输出上，有精确换基恒等式

$$
\boxed{A_JP_\ell=d_*A_\ell.}
\tag{2.3}
$$

证明：在所选输出 $I$ 上，伴随身份给
$BE_\ell=D(A_\ell)_I$。在 $\mathbb Q(s)$ 上，$A_J$ 的列构成整个 $A$ 的像的一个基，且输出限制到 $I$ 在这个像上单射；故完整输出上也有 $A_JE_\ell=DA_\ell$。两边是多项式向量，除以非零的 $K$ 得 (2.3)。

因此 (2.3) 没有遗失另外 $13$ 个输出方向。它也不需要事先知道原目标属于多项式来源模。

## 3. 任意已存在的多项式解如何降度

现在**假设**某个原目标 $b$ 已有多项式解

$$
Ax=b,\qquad x\in\mathbb Q[s]^{6188}.
\tag{3.1}
$$

对每个非基来源 $\ell\notin J$，作普通 Euclidean 除法

$$
x_\ell=d_*v_\ell+r_\ell,\qquad \deg r_\ell<q.
$$

利用 (2.3)，把 $d_*v_\ell A_\ell$ 移入基来源，置

$$
y_J=x_J+\sum_{\ell\notin J}P_\ell v_\ell,
\qquad y_\ell=r_\ell\quad(\ell\notin J).
$$

则

$$
Ay=b.
\tag{3.2}
$$

为估计基来源，先注意由 (3.1)

$$
\operatorname{adj}(B)b_I
=\sum_\ell E_\ell x_\ell
=K\sum_\ell P_\ell x_\ell.
$$

故在这个**已有成员性**的前提下，

$$
T_b:=\operatorname{adj}(B)b_I/K
\in\mathbb Q[s]^{4354}.
\tag{3.3}
$$

这里不能对一个尚未证明成员性的目标无条件声称 (3.3) 为多项式。对 (3.2) 限制到 $I$ 并使用伴随矩阵，得

$$
d_*\,y_j=(T_b)_j-
\sum_{\ell\notin J}(P_\ell)_j r_\ell
\qquad(j\in J).
\tag{3.4}
$$

这是准确的降度式；所有原来源仍在原次数至多三的乘子空间中。

## 4. 九个 $h_0t_\nu$ 的成本全部至多 8740

原目标为

$$
t_\nu=\left(\sum_{k=0}^\nu\binom\nu k(-s)^{\nu-k}m_k\right)^2,
\qquad b_\nu=h_0t_\nu,\qquad 2\le\nu\le10,\qquad \deg h_0=24.
$$

若输出为 $m_am_b$，其原权为 $20$，对应系数次数至多
$24+2\nu-a-b$。所以对所有输出有共同目标权界

$$
\deg(b_\nu)_i+b_i\le\tau_\nu:=44+2\nu\le64.
\tag{4.1}
$$

[所选子式无穷远分析](R150-appendix-selected-original-infinity-minor-rank4318-and-connection3.md)中已经使用的特征零全矩阵秩上界 $4340$，还迫使 $B$ 的全部 $4353$ 阶 cofactor 在无穷远至少消失 $13$ 阶。于是

$$
\deg(\operatorname{adj}B)_{ji}\le H-a_j+b_i-13.
$$

结合 (3.3)、(4.1)：

$$
\deg(T_{b_\nu})_j
\le H-a_j+\tau_\nu-13-60
=H-a_j+\tau_\nu-73.
\tag{4.2}
$$

若右端向量的某项为零，以下相应次数上界自动略去。

对于非基来源，由 (1.3)

$$
\deg y_\ell+\delta_\ell
\le q-1+45
\le8696-1+45=8740.
\tag{4.3}
$$

对于基来源，把 (2.2)、(4.2) 代入 (3.4)。因为 $d_*$ 非零且次数为 $q$，

$$
\begin{aligned}
\deg y_j+\delta_j
&\le
\max\left\{
H+\tau_\nu-83-q,\
\max_{\ell\notin J}(H+a_\ell-85)
\right\}\\
&\le
\max\{8770+64-83-255,\ 8770+55-85\}\\
&=\max\{8496,8740\}=8740.
\end{aligned}
\tag{4.4}
$$

合并 (4.3)、(4.4)，得到

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists x^{(\nu)}:\ Ax^{(\nu)}=h_0t_\nu,\
\operatorname{cost}(x^{(\nu)})\le8740.
}
\tag{4.5}
$$

各目标分别降度即可，九个解可同时取在这个共同有限来源空间中。这个结论比原条件界 $8814$ 及 cofactor 改进 $8801$ 更强；它仍是条件命题。

## 5. 何时同一降度还能用于模 $31^n$

令 $\mathcal D=\mathbb Z_{(31)}$。原 $K$ 的最高系数是 $5^6$，为 $\mathcal D$ 的单位。因为 $K$ 整除各整数最大子式，采用单位最高系数除法可知

$$
d_*,\ P_\ell\in\mathcal D[s].
\tag{5.1}
$$

可直接证明 (5.1)：在 $\mathcal D[s]$ 中以 $K$ 对各相关整数多项式作除法；余式在 $\mathbb Q[s]$ 中为零，因此本来就在 $\mathcal D[s]$ 中为零。

若**额外**证明 $\operatorname{lc}(d_*)$ 为 $\mathcal D$ 的单位，则对每个 $n\ge1$，在

$$
R_n=\mathcal D/(31^n)
$$

中可用同一次数 $q$ 的 $d_*$ 对任意来源系数作除法。这里 $K$ 和 $d_*$ 在 $R_n[s]$ 中都有单位最高系数，故都不是零因子，且乘非零多项式的次数准确相加。即使 $R_n$ 有零因子，(2.3)–(3.4) 的消去及上述次数估计仍成立。

具体地，若给定一个 $Ax=b\pmod{31^n}$ 的已有解，则
$\operatorname{adj}(B)b_I=K\sum P_\ell x_\ell$ 在 $R_n[s]$ 中成立。除以单位最高系数的 $K$ 所得 $T_b$ 是确切多项式，再作来源余式整理，得到成本至多 $8740$ 的解。固定的目标乘子 $31^e$ 只改变常数系数，不增加 (4.1) 的权界，也不被降度改变。

因此，在这个尚未支付的单位最高系数条件下，若固定 $e$ 的 $31^e h_0t_j$ 在无界模精度下都可解，则可以先全部降到同一 $B=8740$，再应用[固定来源界的 $31$ 进下降](R150-appendix-fixed-source-bound-p-adic-descent-and-infinity-escape.md)，得到精确的 $\mathcal D[s]$ 来源。

因为 $D=Kd_*$ 且 $\operatorname{lc}(K)$ 是 $31$ 单位，

$$
\operatorname{lc}(d_*)\in\mathcal D^\times
\quad\Longleftrightarrow\quad
\operatorname{lc}(D)\in\mathcal D^\times.
$$

所以消去公共因子没有免费解决原来的无穷远单位条件。已有模 $31^6$、成本 $1345$ 的构造任务也不能替代无界精度或精确特征零身份。

## 6. 本条闭合的接口和保留的问题

本条把一个已存在的原多项式来源解准确整理到成本 $8740$，并给出保固定 $31^e$ 的有限环版本所需的同一明确额外条件。没有新增数值搜索，没有重算原 $315$ 挠空间，也没有把已知的 $K_h$ 当成完整射影 gcd。原特征零目标成员性、全部无穷远厚度、普通 Hilbert 不变子空间问题仍须继续。
