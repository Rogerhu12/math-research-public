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
