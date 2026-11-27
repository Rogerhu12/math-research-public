# R1140：原双角色的低权 Manin 来源归约

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**结论与范围。** 对原 forced 角色的指定一对 $j=1,k=2$，本文直接在模 $p$ 的真实 Manin 模块中证明：全部 rank-one 来源为零，全部 rank-two 来源等于一个保留的权六端点来源乘 $16\delta^2/21$。该端点在原曲线上的类是紧致的，通常 Hecke 的实际特征值为 $\ell^{-2}+\ell^3$。本文不以“Eisenstein”名称或 level-one 权六无 cusp forms 为理由消掉这个类，也不将一个虚设的零号来源称为原 cuspidal 函数 $F_0$。

在 R1139 的明确混合 Bernoulli 门内，原裸 cup 因而准确归约为这个单一紧致来源的值。本文没有证明该剩余值为零，也没有完成四阶覆盖或一般 $p$ 的排点。

## 1. 原标记与所要归约的两个完整循环

沿 [R1136](R1136-original-forced-compact-Manin-sources.md) 的原规范，固定
$$
p>37,\qquad m=(p-1)/2,\qquad
\chi_1=\omega^{p-3},\quad \chi_2=\omega^{p-5},\quad
\theta=\chi_1\chi_2=\omega^{p-7}.
\tag{1140.1}
$$
这两条是实际 forced 角色，不需要额外的 Bernoulli-good 假设才能定义其原函数与循环。

在原 symplectic 标记上写
$$
N(x,y)=x^2-\delta y^2,\qquad
\delta\in\mathbb F_p^\times\setminus\mathbb F_p^{\times2},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad q=N\circ J.
\tag{1140.2}
$$
不把 $J$ 当作 $N$ 的等距变换。R1136 (F8)–(F10) 已支付实际 torsion labels 为 $J$ 乘 Manin columns，以及路径与两槽交换的两个负号。

对 $\det(v,w)=1$，令 $e(v,w)$ 为 fixed-Weil full-level 上的原 Manin 类；它只按 $(v,w)\sim(-v,-w)$ 识别。R1136 的两个完整来源是
$$
C_{12}^{(2)}
 =\frac1{2m^2}\sum_{\det(v,w)=1}
       q(v)^2q(w)^4e(v,w),
\qquad
C_{12}^{(1)}
 =\frac12\sum_{c,d\in\mathbb F_p^\times}
       c^4d^8[c:d].
\tag{1140.3}
$$
后一式采用原 $\Gamma_1(p)$ bottom-row convention。本文始终保留第一式的全部 determinant-one 点对，以及第二式的全部依赖点对。

定义新的端点来源
$$
C_{\mathrm{Eis}}
 =\frac1{2m^2}\sum_{\det(v,w)=1}q(w)^2e(v,w).
\tag{1140.4}
$$
这只是一个 Manin 循环的定义，不对应一个新造的原 $F_0$。

令
$$
H' =J^{-1}\bigl((N_{\rm ns}\cap\mathrm{SL}_2(\mathbb F_p))/\{\pm1\}\bigr)J.
$$
由于 $q(hv)=\pm q(v)$，(1140.3) 的 rank-two 类与 (1140.4) 均为 $H'$-不变。按 R1136 (F16) 以 $J_*$ 与 degree-$p+1$ transfer 下降，所得原 $X=X_{\rm ns}^+(p)$ 紧致类分别记为 $c_{12}^{(2)}$、$c_{\mathrm{Eis}}$。所有规范都除以同一个 $p+1$，所以不改变本文各比例。

(1140.4) 确实紧致：固定 $v$ 时，$w=w_0+tv$ 给 $q(w)^2$ 的次数至多四，求和为零；固定 $w$ 时，另一端的常权求和为 $p=0$。两端边界分别消去。这里不借跨 Weil 分量的总和来支付单个分量的边界。

## 2. 模 $p$ 的三个低权 Manin 商

令 $V_d=\mathbb F_p[X,Y]_d$，只取 $d=4,8,12$，并置
$$
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
U=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad
\mathcal M_d=
 V_d\big/\bigl((1+S)V_d+(1+U+U^2)V_d\bigr).
\tag{1140.5}
$$
这里矩阵在多项式上的作用是 $P(Z)\mapsto P(gZ)$；所有次数均偶，故 $S^2$ 作用为一。因 $2,3$ 在 $\mathbb F_p$ 中可逆，两个关系像分别为 $V_d^S$ 和 $V_d^U$。

在代数闭包中计算特征值，得到
$$
\begin{array}{c|ccc}
d&4&8&12\\ \hline
\dim V_d^S&3&5&7\\
\dim V_d^U&1&3&5 .
\end{array}
\tag{1140.6}
$$
二者的交是 $\mathrm{SL}_2(\mathbb F_p)$-不变子空间。该交为零：平移不变的次数 $d<p$ 齐次多项式必为 $cY^d$，再施以 $S$ 就迫 $c=0$。所以三个 $\mathcal M_d$ 都恰为一维。

更准确地，
$$
\lambda_d(P)=P(1,0)-P(0,1)
\tag{1140.7}
$$
在 $1+S$ 上为零；在 $1+U+U^2$ 上，三个端点差沿 $(1,0),(0,1),(1,1)$ 的轨道消去。且 $\lambda_d(X^d)=1$。因此它给
$$
\mathcal M_d\xrightarrow{\sim}\mathbb F_p.
\tag{1140.8}
$$
特别，所有内部单项式 $X^aY^{d-a}$、$0<a<d$ 的类为零。

这是模 $p$ 关系的直接计算。没有先取特征零 cuspidal dimension 再忽略可能的模 $p$ 边界类。

## 3. 系数对偶与实际 full-level 循环

使用以下 apolar 配对：
$$
\langle X^iY^{d-i},X^jY^{d-j}\rangle_d
 =
 \begin{cases}
 (-1)^i\binom di^{-1},&i+j=d,\\
 0,&i+j\ne d.
 \end{cases}
\tag{1140.9}
$$
因 $d<p$，此配对非退化；它满足
$$
\langle Q\circ M,P\circ M\rangle_d
  =(\det M)^d\langle Q,P\rangle_d.
\tag{1140.10}
$$
故 $\mathrm{SL}_2$ 自对偶在延至 $\mathrm{GL}_2$ 时的行列式因子被明确保留。

定义 full-level 系数映射
$$
\Phi_d(P)
 =\frac12\sum_{g\in\mathrm{SL}_2(\mathbb F_p)}
   \bigl\langle q(g(X,Y))^{d/2},P\bigr\rangle_d\, e_g.
\tag{1140.11}
$$
$g$ 与 $-g$ 的两项相同，$1/2$ 只除 simultaneous-sign 双计。对右乘 $h\in\mathrm{SL}_2(\mathbb F_p)$ 重指标，有
$$
R_h\Phi_d(P)=\Phi_d(P\circ h).
\tag{1140.12}
$$
因此 (1140.11) 把 (1140.5) 的两组关系送到实际 full-level Manin 关系；它不是只在一个抽象多项式商中进行计算。

系数泛函的准确对偶为
$$
[X^aY^{d-a}]Q
 =\bigl\langle Q,(-1)^a\binom da X^{d-a}Y^a\bigr\rangle_d.
\tag{1140.13}
$$
于是 Sym$^{12}$ 的 $[X^4Y^8]$ 对应 $495X^8Y^4$，Sym$^8$ 的 $[X^2Y^6]$ 对应 $28X^6Y^2$；两者都是 (1140.8) 中的内部项。Sym$^4$ 的 $[Y^4]$ 则对应 $X^4$，是保留的端点。

这里的 $q=N\circ J$ 与整个 $H'$ 同时运输。对 $d=4,8,12$，$d/2$ 为偶，所以 (1140.11) 在 $H'$ 下不变。此后可用同一 prime-to-$p$ transfer 下降。

## 4. 完整 polar 恒等式与 $16\delta^2/21$

设
$$
A=q(v),\quad B=q(w),\quad
C=\frac{q(v+w)-q(v)-q(w)}2,\quad D=\det(v,w).
$$
由 (1140.2) 的原二次型，
$$
C^2=AB+\delta D^2,\qquad
q(Xv+Yw)=AX^2+2CXY+BY^2.
\tag{1140.14}
$$
直接展开两个完整系数：
$$
\begin{aligned}
K_0
 &:=[X^4Y^8]q(Xv+Yw)^6\\
 &=15A^2B^4+240AC^2B^3+240C^4B^2\\
 &=495A^2B^4+720\delta D^2AB^3+240\delta^2D^4B^2,\\[2mm]
K_2
 &:=[X^2Y^6]q(Xv+Yw)^4\\
 &=4AB^3+24C^2B^2
  =28AB^3+24\delta D^2B^2 .
\end{aligned}
\tag{1140.15}
$$
因而有精确重建式
$$
\boxed{\quad
 A^2B^4
 =\frac{K_0}{495}
  -\frac{4\delta}{77}D^2K_2
  +\frac{16\delta^2}{21}D^4B^2 .
 \quad}
\tag{1140.16}
$$
全部分母仅涉及 $3,5,7,11$，对 $p>37$ 均为单位。这条恒等式包含实际 inverse Clebsch 系数；不能把单独 normalized transvectant 的系数直接当作 (1140.16) 的末项。

在 determinant-one 上 $D=1$。由 (1140.11)–(1140.13)，前两项的完整加权 Manin 和严格为零。因此
$$
\boxed{\qquad
 C_{12}^{(2)}=\frac{16\delta^2}{21}C_{\mathrm{Eis}},
 \qquad
 c_{12}^{(2)}=\frac{16\delta^2}{21}c_{\mathrm{Eis}} .
 \qquad}
\tag{1140.17}
$$
先得到的是相对同调等式；两边已逐端点证明紧致，而紧致同调到相对同调单射，所以它也是原紧致同调等式。

## 5. 全部 rank-one 来源准确为零

为了同时保留 bottom-row convention 和系数对偶，定义
$$
\mathcal E_d(P)
 =\frac12\sum_{x=(c,d)\ne(0,0)}
      P(J^{-1}x^T)[c:d].
\tag{1140.18}
$$
这里不把公式中的第二坐标与次数下标混为一物。由
$h^{-T}=JhJ^{-1}$，右重指标 $x\mapsto xh$ 给
$$
R_h\mathcal E_d(P)=\mathcal E_d(P\circ h).
\tag{1140.19}
$$
故此映射同样杀 (1140.5) 的关系。

$J^{-1}(c,d)^T=(d,-c)^T$，所以
$$
C_{12}^{(1)}=\mathcal E_{12}(X^8Y^4)=0.
\tag{1140.20}
$$
由于该单项式在两条坐标轴上都为零，(1140.18) 中加入的 $c=0$ 或 $d=0$ 项确实没有贡献。没有删除依赖点对，也没有利用 full-level 到 $\Gamma_1(p)$ 的 degree-$p$ pullback 反除。这是原 $\Gamma_1(p)$ 紧致类自身为零。

## 6. 原 Cartan Hecke 的完整行列式尺度

本节只对素数 $\ell\ne p$ 陈述通常 $T_\ell$。使用 Merel 的完整 universal Manin 元
$\sum_M u_M[M]$，其中 $\det M=\ell$，满足其条件 $(C_\ell)$。标准 level-one 权 $d+2$ 算子在 (1140.5) 上为
$$
T_\ell^{[d+2]}P
 =\sum_M u_M\,P(M(X,Y)).
\tag{1140.21}
$$
这里不能以一个未经 Manin 分解的裸 double-coset 多项式和替代全部 $u_M$。

### 6.1 原群上的 reset 与 adjugate

令 $\Gamma=\Gamma_{H'}$。选原 Cartan 元 $b_\ell$、$N(b_\ell)=\ell$，并令
$b'_\ell=J^{-1}b_\ell J$，故 $q(b'_\ell v)=\ell q(v)$。
取
$$
\Delta_\ell
 =\{A\in M_2(\mathbb Z):\det A=\ell,\
                 A\bmod p\in H'b'_\ell\}.
\tag{1140.22}
$$
R1136 §11.2–11.3 的 CRT 与实际 degree-$\ell$ isogeny 已将此 double coset 识别为原通常 Hecke，且其物理 level 作用是 $\ell A^{-T}=JAJ^{-1}$。

Merel 的 $\widetilde A=\ell A^{-1}$ 没有造成额外角色：
$\ell(b'_\ell)^{-2}$ 属于 norm-one Cartan，所以
$\widetilde\Delta_\ell=\Delta_\ell$。
在 Merel Theorem 4 中可取
$$
\phi(A)\bmod p=(b'_\ell)^{-1}A.
\tag{1140.23}
$$
其值按 $\Gamma$ 左陪集解释；选择整 $\mathrm{SL}_2$ 提升不影响该值。右乘相容性直接来自 (1140.23)；$A\phi(A)^{-1}$ 约模为 $b'_\ell$，给其第二条件。若两 adjugate 矩阵给同一个 right-$\mathrm{SL}_2(\mathbb Z)$ coset，则它们的商为整 determinant-one 矩阵，且约模在 $H'$，给第三个 injectivity 条件。每个 determinant-$\ell$ 整矩阵可右乘一个 $\mathrm{SL}_2(\mathbb Z)$ 提升使其约模落入 $H'b'_\ell$，所以无额外遗漏项。

因此原 weight-two Manin 边的 Hecke 公式正是
$$
T_\ell e_g=\sum_Mu_M e_{\phi(gM)}.
\tag{1140.24}
$$

### 6.2 对偶配对的因子不能省

令 $\overline\Phi_d$ 为 (1140.11) 的原 $X$ 下降；所有项都带同一 transfer 因子。对 (1140.24) 的每个 $M$，重指标
$$
g=b'_\ell hM^{-1}
$$
后有
$$
\begin{aligned}
\bigl\langle q(gZ)^{d/2},P\bigr\rangle_d
 &=\ell^{d/2}
   \bigl\langle q(hM^{-1}Z)^{d/2},P\bigr\rangle_d\\
 &=\ell^{d/2}\ell^{-d}
   \bigl\langle q(hZ)^{d/2},P(MZ)\bigr\rangle_d .
\end{aligned}
\tag{1140.25}
$$
第一因子来自真实 Cartan norm；第二因子是 (1140.10) 的 $\mathrm{GL}_2$ 对偶因子。故完整公式为
$$
\boxed{\quad
T_\ell\,\overline\Phi_d(P)
 =\ell^{-d/2}\,
   \overline\Phi_d(T_\ell^{[d+2]}P).
\quad}
\tag{1140.26}
$$
这不是只从 $\mathrm{SL}_2$ 自对偶推测一个 Hecke twist。

### 6.3 端点特征值从真实 boundary action 读出

Merel Proposition 11 的边界算子使用
$$
P|A=P(\operatorname{adj}(A)Z),\qquad
T_\ell^\partial(P\{\alpha\})
 =\sum_{\delta\in\mathrm{SL}_2(\mathbb Z)\backslash M_2(\mathbb Z)_\ell}
       P|\delta\{\delta\alpha\}.
\tag{1140.27}
$$
在 level-one 的 $\infty$ boundary coinvariant，$X^d\{\infty\}$ 为生成元，取值是 $X^d$ 的系数。用代表
$$
\delta_\infty=\begin{pmatrix}\ell&0\\0&1\end{pmatrix},
\qquad
\delta_b=\begin{pmatrix}1&b\\0&\ell\end{pmatrix}
\quad(0\le b<\ell),
$$
前项的该系数为 $1$，另 $\ell$ 项各为 $\ell^d$。因此 boundary 算子为 $1+\ell^{d+1}$。Merel 的
$\partial T_\ell=T_\ell^\partial\partial$ 与 (1140.8) 的单位 boundary 识别给
$$
T_\ell^{[d+2]}[X^d]=(1+\ell^{d+1})[X^d]
\quad(d=4,8,12).
\tag{1140.28}
$$
本段是 boundary 上的简单 coset 计算；(1140.21) 仍是完整 universal Manin 算子，二者没有混用。

(1140.4) 等于 $m^{-2}\Phi_4(X^4)$。代入 (1140.26) 得
$$
\boxed{\qquad
T_\ell c_{\mathrm{Eis}}
 =(\ell^{-2}+\ell^3)c_{\mathrm{Eis}}
 \quad(\ell\ne p).
\qquad}
\tag{1140.29}
$$
这是实际 compact Cartan source 中的 $I_3=I_{p-3}$ 系统。它仍可能非零；level-one endpoint 的像在这里紧致，正是 §1 的模 $p$ 端点求和所付的现象。

## 7. 无需混合 Bernoulli 门的两个真实 target 部分

本节先不假设 R1136 (F33)。令
$$
\beta=\frac4{m^2}\{F_{\chi_1},F_{\chi_2}\},\qquad
S_n=\Psi_n(c_{12}^{(2)},C_{12}^{(1)})
    =\frac{16\delta^2}{21}\Psi_n(c_{\mathrm{Eis}},0).
\tag{1140.30}
$$
这里 $n>3$ 为素数、$n\ne p$，$\Psi_n$ 是原**完整 smoothed** map；
它不需要先有 source unit ideal。R1138 给
$$
S_n=V_n\beta,\qquad
V_n=n^4-n^{-4}T_n+n^{-11},
\tag{1140.31}
$$
因为当前 $a=p-7\equiv-6\bmod p-1$。

由 (1140.29) 和原 smoothed Hecke 相容性，全部 $S_n$ 都满足
$T_\ell S_n=(\ell^{-2}+\ell^3)S_n$。
在这一系统上 $V_n$ 的 scalar 是
$$
v_n=n^4-n^{-4}(n^{-2}+n^3)+n^{-11}
   =n^{-11}(n^5-1)(n^{10}-1).
\tag{1140.32}
$$
取 primitive residue class 中的素数 $n_0>3$，则 $p>37$ 保证
$n_0^5,n_0^{10}\ne1$，所以 $v_0=v_{n_0}$ 为单位。定义
$$
\beta_{\mathrm{Eis}}=v_0^{-1}S_{n_0},
\qquad \beta_8=\beta-\beta_{\mathrm{Eis}}.
\tag{1140.33}
$$
SV 原 compatibility 在指定循环上给
$v_0S_n=v_nS_{n_0}$。于是
$$
V_n\beta_8=0\quad\text{对全部辅助素数 }n>3,\ n\ne p.
\tag{1140.34}
$$
等价地，这个部分被
$T_n-(n^8+n^{-7})$ 杀掉。这里准确保留的是原辅助素数族的
$I_8$ common-kernel，不凭空扩大为整个 field $K_2/p$ 的 source 商关系。

因此得到无条件的实际分解
$$
\boxed{\quad
\beta=\beta_{\mathrm{Eis}}+\beta_8,\qquad
T_\ell\beta_{\mathrm{Eis}}=(\ell^{-2}+\ell^3)\beta_{\mathrm{Eis}},
\quad V_n\beta_8=0.
\quad}
\tag{1140.35}
$$
两部分的来源、常数及 target 均已指定。它们不依赖 $n_0$：
另取任何 $v_{n_1}\ne0$ 的辅助素数，compatibility 给
$S_{n_1}/v_{n_1}=S_{n_0}/v_{n_0}$。
且两个系统严格分离，因为同一个 $V_{n_0}$ 在前者上为非零
$v_0$，在后者上为零。不能把 (1140.35) 省成只剩第一项。

原 $\beta$ 有 R1139 §2 的完整曲线 Kummer-cup lift；
这个 lift 的存在不使用其 Bernoulli 假设。因此
$\beta_{\mathrm{Eis}}=v_0^{-1}V_{n_0}\beta$ 与 $\beta_8$
均属于同一实际紧致 target 像。R1139 的 base scalar
$n(n^a-n)(n^a-n^2)$ 对 primitive $n$ 非零，
故 $\beta_8$ 的 common-kernel 不是遗漏的纯 base 常数项。
本节不以此删去剩余的几何 $H^1$ 算术层。

## 8. 在明确混合门中的原裸 cup 读数

对 $j=1,k=2$，R1139 的混合门准确为
$$
8<m,\qquad p\nmid B_{16}B_{p-15}.
\tag{1140.36}
$$
第一条件对 $p>37$ 自动成立；仍明确保留两个 Bernoulli 条件，
不由原 forced 角色存在性代替。
若 (1140.36) 成立，R1139 消去 (1140.34) 的紧致 common-kernel，
所以 $\beta_8=0$。
沿同一 actual unsmoothing map $\Psi$，更准确地有
$$
\begin{aligned}
\frac4{m^2}\{F_{\chi_1},F_{\chi_2}\}
 &=\Psi(c_{12}^{(2)},C_{12}^{(1)})\\
 &=\frac{16\delta^2}{21}\,
       \Psi(c_{\mathrm{Eis}},0).
\end{aligned}
\tag{1140.37}
$$
即
$$
\boxed{\qquad
\{F_{\chi_1},F_{\chi_2}\}
 =\frac{4m^2\delta^2}{21}\,
       \Psi(c_{\mathrm{Eis}},0)
 \quad\text{在原 }K_2(K(X))/p.
\qquad}
\tag{1140.38}
$$
$F_{\chi_i}$ 全程为原 leading-normalized cuspidal 函数类。
右边的 $\Psi$ 含原一次 $e_\theta$、all-vector 系数、
Cartan transfer 和全部 auxiliary smoothing 的实际消去；
本文没有重新规范化这些量。

由 $\Psi$ 的原 Hecke 相容性，(1140.29) 也约束 (1140.38) 的剩余 target 值。
因此指定裸 cup 已归约到一个明确的 compact source Hecke system。
**没有由此得到该值为零。**
R1131 的指定 odd $K$-rational torsion 消去不等于整个
$I_3$ compact block 消失，不能用于删掉此项；
实际原 $\chi_1$ cuspidal 来源正需继续保留。

## 9. 证据、依赖与尚未完成的门

- [R1136](R1136-original-forced-compact-Manin-sources.md)，(F8)–(F26)、§11：原 $J$、正商、两完整循环、一次 determinant transport、物理 Hecke 与 CRT。
- [R1138](R1138-original-integral-bare-cup-smoothing-comparison.md)：实际辅助单位除子与完整 crossed norms 的模 $p$ 裸比较。
- [R1139](R1139-original-compact-target-unsmoothing-and-bare-cup.md)：在 (1140.36) 中的 compact-target unsmoothing，包含全部 cusp、base、geometric 和 Pic/Br 门。
- Loïc Merel，*Universal Fourier expansions of modular forms*，Lecture Notes in Mathematics 1585 (1994), 59–94；[作者全文](https://perso.imj-prg.fr/wp-content/uploads/merel-pub/Essen.pdf)。本文亲读其 §1.1 的 adjugate coefficient action、Proposition 1 的 Manin relations、Proposition 6 的 boundary、§2.1 Theorem 4 与 Proposition 11，以及 introduction Theorem 2 的完整 universal Hecke 元。作者稿的对应印刷页为 4、9、16–18。

上述低权关系与全部常数在本文逐式自证；没有调用数值计算。保留的下一项是原 $\Psi(c_{\mathrm{Eis}},0)$ 的实际值及其与所需高 cochain 的关系。本文不从来源缩小推原 cup 零，不从 cup 归约推全局有理点分类。


## 10. 指定端点的真实 degree-p norm 与 p-isogeny 两槽

本节仍取 $n>3$、$n\ne p$ 为辅助素数，所有 theta 使用 SV §6.3.1
(6.5)–(6.6) 的 trace-fixed 规范。以下只对 degree-$p$ map 取真实 norm，
从不反除 $p$。

### 10.1 不留下未知 base 常数的 theta norm

令 $\pi:E\to E'$ 为 cyclic degree-$p$ isogeny，$C\subset E[n]$。
因为 $(n,p)=1$，$\pi$ 将 $E[n]$ 同构到 $E'[n]$，并将 $C$ 同构到 $\pi C$。
pushforward 原 theta divisor 给
$$
\pi_*\bigl(n^2[O]-[E[n]]\bigr)
 =n^2[O']-[E'[n]],\qquad
\pi_*\bigl(n[C]-[E[n]]\bigr)
 =n[\pi C]-[E'[n]].
\tag{1140.39}
$$
所以 norm 与对应 target theta 至多相差 base 的 $K_1$ 类。
norm 与所有 $[s]_*$ 交换，故此差仍 trace fixed。
对 base 类，$[s]_*$ 是乘 $s^2$；因而差被全部 $s^2-1$ 杀掉。
SV 脚注 19 的 gcd 论证给该 gcd 整除 $24$。
在 $\mathbb Z_{(p)}$ 中 $24$ 可逆，所以差严格为零：
$$
\operatorname{Nm}_{\pi}\theta_{n,E}=\theta_{n,E'},
\qquad
\operatorname{Nm}_{\pi}\theta'_{n,C,E}
 =\theta'_{n,\pi C,E'}.
\tag{1140.40}
$$
也可先限制 $s$ 与 $6np$ 互素；CRT 仍使其 gcd 整除 $24$。
这保留了原规范，不把两个 fiber divisors 相等误写成无常数等式。
若使用实际函数代表，则唯一余差为 prime-to-$p$ torsion，
在所用 $K_1/p$ 中同样为零。

### 10.2 固定 Q 的 p 个实际 first-slot 点

在 $Y_1(p)_K$ 上取原 $(E,Q)$，令
$$
\pi_Q:E\longrightarrow E_Q=E/\langle Q\rangle.
$$
固定 $\zeta=\zeta_p$。对任一 $P$ 满足 $e_p(P,Q)=\zeta$，
$$
Q^\vee=\pi_Q(P)\in\ker\widehat\pi_Q
\tag{1140.41}
$$
与 $P$ 的选择无关，因为全部选择正是 $P+\langle Q\rangle$。
它由 $Q$、$\zeta$ 及 Cartier duality 唯一给出，所以定义在同一
$Y_1(p)_K$ 上。这不是另外选择一个未规范的 dual generator。

定义
$$
\begin{aligned}
\mathcal B_n^{\rm iso}(E,Q)
={}&\{\theta_{n,E_Q}(Q^\vee),\theta_{n,E}(Q)\}\\
&-\sum_{C\subset E[n]\ {\rm cyclic}}
 \operatorname{Cor}_C
 \{\theta'_{n,\pi_QC,E_Q}(Q^\vee),
   \theta'_{n,C,E}(Q)\}.
\end{aligned}
\tag{1140.42}
$$
求和仍按真实 closed subgroup 及其 residue field 作 corestriction。
两个被评值点均有阶 $p$，因而避开全部 $n$-torsion 支撑。

由 projection formula、(1140.40) 及 cyclic-$n$ base change 与
degree-$p$ norm 的交换，
$$
\boxed{\quad
 \sum_{\substack{P\in E[p]\\e_p(P,Q)=\zeta}}
       B_n(P,Q)=\mathcal B_n^{\rm iso}(E,Q).
 \quad}
\tag{1140.43}
$$
左边是原 full-level 至固定 $Q$ 的 degree-$p$ norm；
它没有被除以 cover degree。第二行的整个 cyclic correlation
在这一 norm 下逐项保留。

### 10.3 Fricke 交换的确切号及其限制

令 $W_\zeta(E,Q)=(E_Q,Q^\vee)$。
在第二次 quotient 后以 dual isogeny 识别回 $E$，
新的 dual generator 为 $-Q$。确切地，若 $R$ 满足
$e_p(R,Q^\vee)=\zeta$，则 Weil pairing 相容给
$e_p(P,\widehat\pi_QR)=\zeta^{-1}$，所以
$\widehat\pi_QR=-Q$。
两 theta 都偶，因此
$$
W_\zeta^*\mathcal B_n^{\rm iso}
 =-\mathcal B_n^{\rm iso}.
\tag{1140.44}
$$
这同时交换全部 $C$ 与 $\pi_QC$，没有删除 norm 项。

对 $u,v\in\mathbb F_p^\times$，用
$\mathcal B_n^{u,v}(E,Q)$ 表示 (1140.42) 中
$Q^\vee,Q$ 分别换成 $uQ^\vee,vQ$ 的完整符号。
则更准确的式子是
$$
W_\zeta^*\mathcal B_n^{u,v}=-\mathcal B_n^{v,u}.
\tag{1140.45}
$$
所以带不同双权的和不因 (1140.44) 自动为零。

## 11. 原一次 Galois 投影给出的准确双权 4、8

将 (1140.43) 代入 (1140.4) 的实际 theta 读数。
在原 full-level field 上，
$$
\mathfrak z_{n,X}(c_{\mathrm{Eis}})
 =\frac1{2m^2}\sum_{Q\in E[p]\setminus\{0\}}
       N(Q)^2\mathcal B_n^{\rm iso}(E,Q).
\tag{1140.46}
$$
本式按原 $H$ transfer 的 restriction 理解；
R1136 (F17) 使其与原 $X$ 上的读数完全一致。

在 full-level lift 上，原 $\sigma_d$ 同时把
$\zeta$ 送到 $\zeta^d$、$Q$ 送到 $b_dQ$。
重指标 $Q'=b_dQ$ 给 $N(Q)^2=d^{-2}N(Q')^2$。
而将 $\zeta$ 换成 $\zeta^d$ 把 (1140.41) 的 dual generator 乘 $d$。
故 $e_\theta$、$\theta=\omega^{-6}$ 的权准确为
$$
d^6d^{-2}=d^4.
\tag{1140.47}
$$
不能只改变 Weil root 而漏掉 Cartan 重标的 $d^{-2}$。

每条 $\mathbb F_p$-line $L\subset E[p]$ 选 $Q_L\ne0$。
写 $Q=tQ_L$ 时，quotient 不变而
$Q^\vee=t^{-1}Q_L^\vee$。
置 $u=d/t,\ v=t$，则
$$
d^4t^4=u^4v^8.
\tag{1140.48}
$$
结合 $\Psi_n(c,0)=2(p-1)e_\theta\mathfrak z_{n,X}(c)$，
$1/2$ 与 $p-1$ 都按原定义抵消，得到
$$
\boxed{\quad
\Psi_n(c_{\mathrm{Eis}},0)
 =\frac1{m^2}\,
 \mathcal T\!\left(\mathcal R_n^{4,8}\right),
\quad
\mathcal R_n^{4,8}
 =\sum_{u,v\ne0}u^4v^8\,\mathcal B_n^{u,v}.
\quad}
\tag{1140.49}
$$
这里 $\mathcal T$ 是以下实际 weighted pull–trace：
对 diamond-$t^{-4}$ 的 $Y_1(p)_K$ 类 $D$，
$$
\mathcal T(D)=\frac1{p+1}
 \operatorname{Cor}_{K(Z)/K(X)}
 \sum_{L}N(Q_L)^2\,\pi_L^*D.
\tag{1140.50}
$$
$\pi_L$ 忘到 $(E,Q_L)$；选择 $Q_L\mapsto tQ_L$ 时，
权乘 $t^4$、$D$ 乘 $t^{-4}$，故不依赖生成元。
整个和在原 $H$ 下不变；(1140.50) 只除 prime-to-$p$ 的 $p+1$。

式 (1140.45) 把双权 $(4,8)$ 交换成 $(8,4)$ 并取负。
它没有将 (1140.49) 的指定权变成其自身，因此不能据 Fricke 号将它设零。

## 12. 同一 p-isogeny 来源的两个实际单位与完整算子

### 12.1 单线单位类，不使用 1/p Siegel 代表

在 $Y_1(p)_K$ 上，对 $r=4,8$ 定义
$$
\mathcal L_r f=\sum_{t\ne0}t^r[f(tQ)],
\qquad
\kappa_r(c)=c^2-c^{-r}.
$$
各权先取 augmentation-zero 整数提升，再约模 $p$。
选择 primitive residue class 中的共同辅助素数 $c>3$、
$c\ne n,p$；因为 $p-1>10$，两个 $\kappa_r(c)$ 都非零。
置
$$
\mathcal G_r=\kappa_r(c)^{-1}\mathcal L_r\theta_c.
\tag{1140.51}
$$
两 auxiliary-theta divisor 的比较给
$\kappa_r(d)\mathcal L_r\theta_c
 =\kappa_r(c)\mathcal L_r\theta_d$；
共同 base factor 由 augmentation 消去。
因此 (1140.51) 不依赖 $c$。
它是原 theta 的实际 $K_1/p$ 类，未使用 $1/p$ 的有理 Siegel 单位。
$\mathcal G_r$ 是本节单线类，不应与原全向量 $G_\chi$ 混名。

定义两个真实槽
$$
A=W_\zeta^*\mathcal G_4,\qquad B=\mathcal G_8,\qquad D=\{A,B\}.
\tag{1140.52}
$$
diamond $t$ 对 $A,B$ 分别作用 $t^4,t^{-8}$，所以 $D$ 的
diamond 为 $t^{-4}$，满足 (1140.50) 的确切条件。
对 $K$ 的自然常数作用、保持 $(E,Q)$ 不动时，
$\sigma_d^0A=d^{-4}A$、$\sigma_d^0B=B$。
再加 (1140.50) 的 Cartan 重标 $d^{-2}$，得到
$$
\sigma_d\mathcal T(D)=d^{-6}\mathcal T(D).
\tag{1140.53}
$$
这是原 target 的 $\theta$ 角色；没有漏掉第二个 root/marking 因子。

### 12.2 fixed-Weil quotient 中必要的 n 因子

令 $T_n^Y=\phi_*q^*$ 是 $Y_1(p)_K$ 上固定 $\zeta$ 的通常
degree-$n$ correspondence。在相应 square 中，
$p$-dual generator 的真实运输满足
$$
q(Q^\vee)=n\,Q_{\rm target}^\vee.
\tag{1140.54}
$$
因为 degree-$n$ isogeny 将 Weil pairing 乘为 $\zeta^n$，
而 target generator 仍以 $\zeta$ 规范。
权 $t^4$ 重标给 $n^{-4}$。
因此，R1138 同一 divisor 比较在两槽分别为
$$
\mathcal L_4\theta'_{n,\pi_QC,E_Q}
 =n^{-4}(nA'-A),\qquad
\mathcal L_8\theta'_{n,C,E}
 =nB'-n^{-8}B.
\tag{1140.55}
$$
$A',B'$ 为 fixed-$\zeta$ target 的实际 pullback。
相同 single-slot norm 给
$$
T_n^Y A=(n^5+1)A,\qquad
T_n^Y B=(n+n^{-8})B.
\tag{1140.56}
$$
例如第一式先在 physical generator 上是
$n^{-4}T_n^YA=(n+n^{-4})A$；这一步不能省去 $n^{-4}$。

### 12.3 全部 crossed 项合并，回到同一个原算子

用 (1140.55) 展开 (1140.49) 中完整 correlation，并用
(1140.56) 和 projection formula，得到
$$
\begin{aligned}
\mathcal R_n^{4,8}
={}&\Bigl[
 (n^2-n^{-4})(n^2-n^{-8})
 -n^{-2}T_n^Y\\
&\hspace{6mm}
 +n^{-11}(n^5+1)+n^{-3}(n+n^{-8})
 -(n+1)n^{-12}
 \Bigr]D\\
={}&\boxed{\ (n^4-n^{-2}T_n^Y+n^{-11})D\ } .
\end{aligned}
\tag{1140.57}
$$
这与 R1138 一样是计算两个 crossed 项，未将它们逐个设零。

最后，actual physical quotient 的 root 是 $\zeta^n$。
故 Cartesian pull–trace square 给
$$
\widetilde T_n^X\mathcal T(D)
 =\mathcal T(\sigma_n^0T_n^YD)
 =n^{-4}\mathcal T(T_n^YD).
$$
由 (1140.53)，左侧又是 $n^{-6}T_n^X\mathcal T(D)$。
因此准确的同源 twist 为
$$
\mathcal T(T_n^YD)=n^{-2}T_n^X\mathcal T(D).
\tag{1140.58}
$$
本式是对具体类及其 stable character space 的实际 moduli
pull–trace 证明，不把一个 characteristic-zero twisting matrix
直接约模 $p$。

综合 (1140.49)、(1140.57)、(1140.58)：
$$
\boxed{\quad
\Psi_n(c_{\mathrm{Eis}},0)
 =\frac1{m^2}
 (n^4-n^{-4}T_n^X+n^{-11})\,
        \mathcal T\{W_\zeta^*\mathcal G_4,\mathcal G_8\}.
\quad}
\tag{1140.59}
$$
故 (1140.33) 中无条件定义的端点部分有完全具体的式子
$$
\boxed{\quad
\beta_{\mathrm{Eis}}
 =\frac{16\delta^2}{21m^2v_0}\,
 V_{n_0}\mathcal T
       \{W_\zeta^*\mathcal G_4,\mathcal G_8\}.
\quad}
\tag{1140.60}
$$
这里仍保实际 $V_{n_0}$ 投影，不能从 (1140.59) 直接在整个
field $K_2/p$ 上反除它，也没有先宣布
$\mathcal T\{W_\zeta^*\mathcal G_4,\mathcal G_8\}$ 本身有完整 proper lift。
(1140.60) 的左侧已有 §7 的实际紧致 lift；这正是当前已付范围。

本后继亲读 SV §6.3.1 的 (6.5)–(6.6)、脚注 19
（作者稿印刷第 57–58 页）及 Lemma 6.3.1；
degree-$p$ distribution 由 (1140.39)–(1140.40) 在原函数上直接证明。
global_route 与 o2_high_coefficient 已分别核原 norm、Fricke 号、
两次 Galois/Cartan 重标、$u^4v^8$、fixed-Weil 的 $n^{-4}$，
以及 (1140.57)–(1140.58) 的完整系数。没有数学程序执行。


## 13. 这个未平滑 pull–trace 的全部尖点 tame 实际消去

本节补付 (1140.60) 后保留的 generic-$K$ 紧致性门。
记
$$
\mathfrak b=\mathcal T\{W_\zeta^*\mathcal G_4,\mathcal G_8\}
       \in K_2(K(X))/p.
\tag{1140.61}
$$
结论是 $\mathfrak b$ 确有原 $X_K$ 上的 proper
$H^2(\mu_p^{\otimes2})$ lift。本节不另断言
$\mathcal O_K[1/p]$ 上的算术延拓，也不将它设为零。

### 13.1 同一 Tate 规范及不可遗漏的 p 次根相位

在任一 full-level cusp 选保 Weil pairing 的 Tate basis
$$
E=E_{\tau^p},\qquad e_1=\tau,\quad e_2=\zeta.
$$
使用 R1070 (1070.19)–(1070.20) 的同一 theta product。
在乘法点 $\zeta^t$，其首项除去与 $t$ 无关的共同因子后为
$$
\zeta^{a_c t}
 \frac{(1-\zeta^t)^{c^2}}{1-\zeta^{ct}},
\qquad a_c\in\mathbb Z,
\tag{1140.62}
$$
可能的共同符号也包含在上述共同因子中。
$\mathcal L_4$ 的 augmentation-zero 整数提升杀共同因子；
剩下的 $\mu_p$ 相位由
$\sum_{t\ne0}t^5=0$ 消去。亦可直接选
$t\leftrightarrow -t$ 对称的 augmentation-zero 提升核该相位。
所以在乘法 cusp，
$$
\overline{\mathcal G_4}
 =\epsilon_4:=\sum_{t\ne0}t^4[1-\zeta^t]
       \quad\text{in }K^\times/K^{\times p}.
\tag{1140.63}
$$
这里重指标 $t\mapsto ct$ 给的系数正是
$c^2-c^{-4}=\kappa_4(c)$，由 (1140.51) 除回。
共同 Hodge frame，包括 degree-$p$ quotient 的微分尺度，
也因同一 augmentation 条件消去。
因此 (1140.63) 保留原 $\mu_p$ 相位及原实际常数，而非只比较 divisor。

另外，将 $\mathcal G_8$ 代入非乘法点
$Q_b=\tau\zeta^b$ 时，其 $\tau$-阶与 $b$ 无关。
这是同一 theta product 的直接结论：每个非零 $t$ 的
$q$-指数只依赖 $t/p$；乘以 $\zeta^{bt}$ 不改变该指数。
因为 $c$ 与 $p$ 互素，分母中的 $ct/p$ 不成为整数，
没有额外的 leading cancellation。记此共同阶为 $v_8$，
只需其模 $p$ 值，不需要对 $v_8$ 作 Bernoulli 单位假设。

### 13.2 p+1 条核直线的两种实际贡献

原 $\mathcal T$ 中的 $p+1$ 条直线正是
$$
L_\infty=\langle e_2\rangle,\qquad
L_b=\langle e_1+b e_2\rangle\quad(b\in\mathbb F_p).
$$

对 $L_\infty$，取 $Q=e_2=\zeta$。
实际 quotient 为
$E_{\tau^p}\to E_{\tau^{p^2}}$，dual generator 为 $\tau^p$。
在 target 的非乘法 cusp，局部参数因此是 $\tau^p$。
所以 $A=W_\zeta^*\mathcal G_4$ 的 $\tau$-阶为 $p$ 的倍数，
而 $B=\mathcal G_8$ 是单位；该槽的 tame 在 $K^\times/K^{\times p}$
中为零。这使用实际 ramification factor $p$，未将 degree-$p$ norm
替换成除以 $p$ 的平均。

对 $L_b$，取 $Q_b=\tau\zeta^b$。
quotient 为 $E_{\tau^p}\to E_{\tau\zeta^b}$；
dual generator 是同一个 $\zeta^{-1}$（反向 Weil convention 同时改成
$\zeta$，因权 $4$ 为偶数，结果相同）。
因此 $A$ 是单位、首项为同一个 $\epsilon_4$，
而 $B$ 的阶为同一个 $v_8$。
按 $\partial\{A,B\}=\overline A^{\operatorname{ord}B}$
的原 tame 约定，
$$
\partial_{L_b}D=v_8\,\epsilon_4
\quad\text{对所有 }b\in\mathbb F_p.
\tag{1140.64}
$$
第二槽的 leading coefficient 可以随 $b$ 变化，但因
$\operatorname{ord}A=0$，它不进入 (1140.64)。

### 13.3 原范数平方权逐 cusp 精确杀掉剩余贡献

在所选 Tate basis 中，原 norm 是某个二次型 $Q_N$。
本式没有把重新选的 basis 当成原 norm 的等距变换。
其实际权为
$$
N(e_1+b e_2)^2=Q_N(1,b)^2,
$$
是 $b$ 的次数至多 $4$ 的多项式。
$p>37$ 给 $4<p-1$，包括常数项在内逐幂求和均为零：
$$
\sum_{b\in\mathbb F_p}Q_N(1,b)^2=0
          \quad\text{in }\mathbb F_p.
\tag{1140.65}
$$
因此 (1140.64) 的完整带权和为零；
$L_\infty$ 已由前节的 $p$ 因子消去。
同一证明适用于每个 full cusp。

原 $H$ 与 cusp 的 order-$p$ unipotent inertia 交平凡；
full-level 与原 Cartan cusp 的宽度均为 $p$，
且 $Z\to X_K$ 的次数 $p+1$ 在模 $p$ 可逆。
由 residue/corestriction 相容及 (1140.50)，
上述全部 tame 消去准确下降到 $\mathfrak b$。
非尖点处两单线槽都是 augmentation 后的实际 modular units，
故没有其他 residue。
Merkurjev–Suslin 及曲线 purity 遂给
$$
\boxed{\quad
\mathfrak b\in
\operatorname{im}\bigl(
 \operatorname{Br}(X_K)[p]\otimes\mu_p
 \longrightarrow K_2(K(X))/p
\bigr).
\quad}
\tag{1140.66}
$$
Kummer exact sequence再给原 proper $H^2(\mu_p^{\otimes2})$ lift。
这里用的是原一次 weighted pull–trace，没有添加一个新的 cusp 修正常数。

### 13.4 去掉 V 投影所需的准确条件

由 (1140.59)、$\mathfrak b$ 的紧致性及 §7，
$$
\beta-\frac{16\delta^2}{21m^2}\mathfrak b
\tag{1140.67}
$$
是一个实际紧致的 $I_8$ common-kernel 类。
只有在 (1140.36) 的两个 Bernoulli 单位门下，
R1139 才将它杀掉；于是
$$
\boxed{\quad
 \{F_{\chi_1},F_{\chi_2}\}
 =\frac{4\delta^2}{21}\,
   \mathcal T\{W_\zeta^*\mathcal G_4,\mathcal G_8\}
 \quad\text{in }K_2(K(X))/p.
\quad}
\tag{1140.68}
$$
没有这两个门时，(1140.60) 的投影表达及 (1140.67) 的
compact common-kernel 仍是保留的准确范围。
本节的 Tate leading、$\mu_p$ 相位、两类核直线、
全部 cusp 的多项式求和与 purity 范围均经 o2_high_coefficient
独立纸核；没有数学程序执行。


## 14. 原局部常数及端点的实际复共轭位置

### 14.1 ε₄ 与原圆单位基、v₄ 与 v₈ 的准确关系

沿 R1069 (1069.14)，取同一个奇整数 $a$、原圆单位
$\eta_a=\zeta^{(1-a)/2}(1-\zeta^a)/(1-\zeta)$，以及
$\beta_{\chi_2}=e_{\omega^{-4}}[\eta_a]$。
直接在原 $K^\times/K^{\times p}$ 中有
$$
\epsilon_4=(p-1)e_{\omega^{-4}}[1-\zeta],\qquad
\beta_{\chi_2}=(a^{-4}-1)e_{\omega^{-4}}[1-\zeta].
$$
$\mu_p$ 的 $\omega$ 角色不进入这个偶投影，且
$a^{-4}\ne1$。因此
$$
\boxed{\quad
\epsilon_4=\frac{\beta_{\chi_2}}{1-a^{-4}}.
\quad}
\tag{1140.69}
$$
这里沿用原圆单位及原角色方向，没有另选一个一维空间的基。

为精确读 Tate 阶，可以在 $\mathbb Z_p$ 完成中取
$\omega(t)^r$ 权；其模 $p$ 类仍由 (1140.51) 的实际整数提升定义。
对 $r=4,8$，这些权的和严格为零。
theta product 的 $\tau$-阶为
$$
\frac p2
 \left(c^2B_2(t/p)-B_2(\{ct/p\})\right).
$$
重指标并除以 $\kappa_r(c)$ 的 Teichmüller 提升
$c^2-\omega(c)^{-r}$ 后，
$$
v_r=\frac p2\sum_{t=1}^{p-1}\omega(t)^rB_2(t/p)
    =\frac{B_{2,\omega^r}}2
       \quad\text{in }\mathbb Z_p .
\tag{1140.70}
$$
广义 Kummer 同余给
$B_{2,\omega^r}/2\equiv B_{r+2}/(r+2)\pmod p$。
这也可只用普通 Kummer 核准：偶非平凡 Teich 权使
$\sum\omega(t)^rt=\sum\omega(t)^r=0$，
且 $\omega(t)^r\equiv t^{pr}\pmod{p^2}$。
Faulhaber 给
$p^{-1}\sum_{t=1}^{p-1}t^{pr+2}\equiv B_{pr+2}\pmod p$；
因 $pr+2\equiv2\pmod p$、$pr+2\equiv r+2\pmod{p-1}$，
再用普通 Kummer 即得所写同余。
这两个指数不在分母异常范围，因此
$$
\boxed{\quad
v_4\equiv\frac1{252},\qquad
v_8\equiv\frac1{132}\pmod p .
\quad}
\tag{1140.71}
$$
特别，(1140.64) 每条 $L_b$ 的原读数准确为
$$
\partial_{L_b}D
 =\frac{\beta_{\chi_2}}{132(1-a^{-4})}.
\tag{1140.72}
$$
$p>37$ 使显示分母全部可逆。这个局部 leading/tame 标量
不是 R1141 中剩余全局 cup 的未知倍数；(1140.65)
依旧消去它的完整带权和。

在 (1140.36) 的双 Bernoulli 门内还有一个可直接消费的支撑后果：
R1141 §2 已付原裸 cup 的 $S=\{p\}$ 算术延拓，
(1140.68) 的系数为 $p$-unit，故同一个 $\mathfrak b$
也有 $\mathcal O_K[1/p]$ 上的算术 lift。
这是同一类的等式给出的结论；门外本节不扩大该支撑范围。

### 14.2 真 Betti 复共轭与 Merel 的 ι* 不同号

在原 analytic moduli 中，实际复共轭是
$$
E_\tau\longrightarrow E_{-\bar\tau},\qquad z\longmapsto\bar z.
$$
它将 $(\tau/p,1/p)$ 送到 $(-e'_1,e'_2)$，即原 level 坐标上的
$$
\varepsilon=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$
$\varepsilon$ 保持 $N(x,y)=x^2-\delta y^2$ 并正规化实际
non-split Cartan normalizer，故这给原 $\mathbb Q$-下降的实结构。
在 symplectic-dual source 中，
$J^{-1}\varepsilon J=-\varepsilon$；
整体 $-1$ 不改原商，且 $q=N\circ J$ 同样满足 $q\circ\varepsilon=q$。
这同时支付了 source 群与原 norm 的相容性。

原路径 $e_g=g\{0\to\infty\}$ 的真实作用是
$$
c_*e_g=e_{\varepsilon g\varepsilon^{-1}}.
\tag{1140.73}
$$
例如 $0\to\infty$ 的垂直路径在
$\tau\mapsto-\bar\tau$ 下点态固定，没有另一个反向号。
重指标后第二列为 $\varepsilon w$，所以 (1140.4) 给
$$
c_*C_{\rm Eis}=C_{\rm Eis},\qquad
c_*c_{\rm Eis}=c_{\rm Eis}.
\tag{1140.74}
$$
第二式与原 degree-$p+1$ transfer 相容。

已亲读 Merel §1.6 Proposition 7：
其 $\iota(f)(z)=f(-\bar z)$ 的定义没有并入微分的负号，
相应 modular-symbol involution 为
$-[P\mid\operatorname{adj}\varepsilon,\varepsilon g\varepsilon^{-1}]$。
故在此 weight-two 的真实 Betti 路径上
$c_*=-\iota^*$。本节不把文献中 $\iota^*$ 的正负标签
直接称为原复共轭的正负标签。

### 14.3 在实际 I₃ 格中锁定原 cuspidal 直线，仍不宣非零

现在另加 $p\nmid B_{p-5}$。
R1131 对 $j=1$ 的两个 gate 是 $B_6$ 与 $B_{p-5}$；
前者对 $p>37$ 恒为单位。
该文因此给原 $I_3$ 的实际 away-$p$ Hecke DVR、
自由秩二 Tate 格及准确非分裂方向
$$
0\longrightarrow\mathbb F_p(\omega^{-2})
 \longrightarrow J[\mathfrak m_3]
 \longrightarrow\mathbb F_p(\omega^3)
 \longrightarrow0.
$$
左侧就是原非零 cuspidal 直线。
(1140.29) 的全部实际 Hecke 特征
$\ell^{-2}+\ell^3$ 使 $c_{\rm Eis}$ 的像落在这个真正
$\mathfrak m_3$-socle 中；这里的 order 只用已付 away-$p$ 生成元。

用原 Jacobian 的规范 Betti 比较
$H_1(X(\mathbb C),\mathbb F_p)\simeq J[p](\mathbb C)$；
它把整 cycle 模 $p$ 送到对应周期的 $1/p$ 类，
与实际 Hecke 及复共轭相容。
因 $2$ 可逆，$J[\mathfrak m_3]$ 的 $c=+1$ 空间一维，
且恰是上述偶子线。由 (1140.74)，得到
$$
\boxed{\quad
c_{\rm Eis}=\lambda_E P_{\chi_1}
 \quad\text{for some }\lambda_E\in\mathbb F_p,
\qquad
P_{\chi_1}=
 \left[\frac1p\operatorname{div}(f_{\chi_1})\right].
\quad}
\tag{1140.75}
$$
$f_{\chi_1}$ 是原 $F_{\chi_1}$ 的实际代表，
故此处保留其全部规范因子；没有将该点默认为未经 $m$ 运输的另一生成元。
$\lambda_E$ 可以为零。本节既没有计算 $\lambda_E$，
也没有把它与 (1140.72) 的局部标量或 R1141 的算术 cup 倍数混同。

(1140.69)–(1140.75) 的角色、数值分母、真实复共轭符号及
actual socle 范围均经 o2_high_coefficient 独立纸核；
所有引用的 cusp/Hecke 格均为已发表的原来源，没有数学程序执行。

后续 [R1143](R1143-original-Eisenstein-lattice-and-exact-cuspidal-endpoint.md) 已将 (1140.75) 升级为无条件 $p>37$ 的准确式 $c_{\rm Eis}=-2016\delta^2P_{\chi_1}\ne0$，保同一规范。其 motivic 读数仍未由 source 非零确定。
