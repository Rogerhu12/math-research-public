# R189：全 $p$ primal Robert 生成元与同一支撑上的精确局部配对

**状态：已证明。**

[R163](R163-all-prime-primitive-adjoint-robert-generator.md) 的原始 Robert 单位生成的是 $W(1)$ 的对偶线。二阶提升还涉及 $W$ 本身，二者的 Kummer 角色不同，辅助理想也不能直接照搬。
本文证明：对每个 $p>37$、$p\equiv3\pmod4$，一个范数 $5$ 的固定高斯素理想给出 $W$ 的全局 $p$–full 线的原始生成元；所用函数仅为

$$
\frac{4}{(-1+2i)x^2+1}.
$$

原来辅助整数 $11$ 的相应 primal 投影反而模 $p$ 为零。
对 R171 的同一个 $776$ 位素数，本文完整重算 $1848$ 个新值，得到这个规范生成元的 $q$ 有限坐标为 $10$，以及它在 $43$ 处对 R185 的 Artin–Hasse 基的配对 $(6,10)$。
这些是同一全局问题的实际 primal 数据；它们尚不是二阶阻碍 $\Omega_2$。

## 1. 表示、准确局部条件及一维全局空间

置

$$
A:y^2=x^3-x,\quad K=\mathbb Q(i),\quad
T=K(A[p])=K((1+i)^3p),\quad
C=\operatorname{Gal}(T/K)=\mathbb F_{p^2}^{\times}.
\tag{189.1}
$$

选实的 $0\ne P\in A[p]$，以 $(P,iP)$ 为基；复共轭记为 $\tau$。
记

$$
W=\{D_z:v\mapsto z\bar v\},\qquad
\operatorname{ad}^0A[p]=\mathbb F_p(\chi_{-4})[i]\oplus W.
$$

$C$ 和 $\tau$ 在 $W$ 上的作用是

$$
a:D_z\mapsto D_{a^{1-p}z},\qquad
\tau:D_z\mapsto D_{\bar z}.
\tag{189.2}
$$

Kummer 实现 $H^1(\mathbb Q,W)$ 所需的系数模为

$$
U=W(-1),\qquad
 a:z\mapsto a^{-2p}z,\qquad \tau:z\mapsto-\bar z.
\tag{189.3}
$$

这里用了 $\det(a)=a^{p+1}$，所以
$a^{1-p}a^{-(p+1)}=a^{-2p}$；复共轭在圆分扭曲上的符号为 $-1$。
扩系数后，$U$ 的两个 Cartan 特征为 $a^{-2p},a^{-2}$，不同且被 $\tau$ 交换。
因此 $U$ 在完整 $G=\operatorname{Gal}(T/\mathbb Q)$ 上绝对不可约，
$\operatorname{End}_G(U)=\mathbb F_p$。

定义

$$
\mathcal P_p=
\{c\in H^1(\mathbb Q,W):
 c\text{ 在所有 }\ell\ne2,p\text{ 不分歧}\}.
\tag{189.4}
$$

$p$ 处没有另加 flat 条件；$2$ 处整个 $H^1$ 已为零。
这不是 R161 的严格 $p$ 局部条件。

### 命题 189.1

$$
\dim_{\mathbb F_p}\mathcal P_p=1,
\qquad
\mathcal P_p\xrightarrow{\ \operatorname{loc}_p\ }
H^1(\mathbb Q_p,W)/L_{\rm fl}
\text{ 为同构。}
\tag{189.5}
$$

特别地，任何非零 $c\in\mathcal P_p$ 的 $p$ 定位都不属于 flat 切线 $L_{\rm fl}$。

**证明。** 先明确所用的局部条件及维数。
在 $p$，$A$ 好超奇异，模 $p$ 惯性给完整非分裂 Cartan。
$W$ 及 $W(1)$ 没有局部不变量；局部 Euler 公式给

$$
h^1(\mathbb Q_p,W)=h^1(\mathbb Q_p,W(1))=2.
$$

固定圆分行列式的 flat 变形环为 $\mathbb Z_p[[t]]$，其一维切线在 $W$ 中；故 $\dim L_{\rm fl}=1$。
在 $2$，保留的是 $A$ 的同一个完整 $Q_8$ 惯性核与最小局部型。
$W$ 的惯性作用是两个非平凡的 $Q_8/\{\pm1\}$ 特征，所以 $W^{I_2}=0$。
圆分角色在 $2$ 的惯性上平凡，故 $W(1)^{I_2}=U^{I_2}=0$。
局部对偶及 Euler 公式因此给

$$
H^1(\mathbb Q_2,W)=H^1(\mathbb Q_2,W(1))=0.
\tag{189.6}
$$

R161 的最小条件 $\mathcal F$ 在 $p$ 取 $L_{\rm fl}$，在 $2$ 取上述零群，其他有限处取不分歧条件。
其最小 $R=T=\mathbb Z_p$ 输入使用层 $32$ 唯一的权 $2$ 形式、固定行列式及这个准确的 $2$ 处条件。
残余表示及其在 $G_{\mathbb Q(\sqrt{-p})}$ 上的限制都绝对不可约：后一个二次域在 $2$ 不分歧，所以仍含忠实的二维 $Q_8$ 惯性表示。
由该最小环的零切空间，

$$
H^1_{\mathcal F}(\mathbb Q,W)=0.
$$

同时，$h^0(\mathbb R,W)=1$，全局 $H^0$ 两侧为零。
Greenberg–Wiles 维数差中，$p$ 处贡献 $1$、实处贡献 $-1$，其余贡献为零，遂有

$$
H^1_{\mathcal F^\perp}(\mathbb Q,W(1))=0.
$$

现在只把 $p$ 条件由 $L_{\rm fl}$ 放宽到整个二维 $H^1$。
Poitou–Tate 比较的相关部分为

$$
0\longrightarrow H^1_{\mathcal F}(\mathbb Q,W)
\longrightarrow \mathcal P_p
\longrightarrow H^1(\mathbb Q_p,W)/L_{\rm fl}
\longrightarrow H^1_{\mathcal F^\perp}(\mathbb Q,W(1))^\vee.
$$

两端为零，得到 (189.5)。这从准确的 full/flat 维数推出一维空间，而非把对偶线的结论直接换名字。证毕。

## 2. 全局单位覆盖与正确的类群特征

以 $\widetilde U$ 表示 (189.3) 的 Teichmüller $\mathbb Z_p$ 提升；其 Cartan 特征取值于 $\mathbb Z_p[i]$，复共轭仍为 $-\bar{\phantom x}$。
$T$ 全虚，复无限位置的置换表示是
$\operatorname{Ind}_{\langle\tau\rangle}^G\mathbf1$。
Dirichlet 定理给自由单位部分的表示

$$
\operatorname{Ind}_{\langle\tau\rangle}^G\mathbf1-\mathbf1.
$$

$U^\tau$ 一维，$U$ 无平凡分量且绝对不可约，故单位的 $U^\vee$ 重数准确为一。
$p\nmid|G|=2(p^2-1)$，整幂等元及模 $p$ 分解保持此重数。
$\mu_T/p$ 的可能非零部分是圆分特征 $a^{p+1}$，与 $a^{2p},a^2$ 均不同，因此它不贡献这个分量。
由此

$$
\dim\left((\mathcal O_T^\times/\mathcal O_T^{\times p})
\otimes U\right)^G=1.
\tag{189.7}
$$

取 $S_T$ 为 $T$ 中所有位于 $2,p$ 上的素点。
这些素点的置换模不含 $U^\vee$：在 $p$，惯性包含完整 $C$，而 $U^C=0$；在 $2$，由 (189.6) 前的惯性计算，$U^{I_2}=0$。
所以允许 $S_T$ 处的单位赋值不会增加 (189.7) 的分量。

Kummer 正合列和 $p\nmid|G|$ 给

$$
\begin{aligned}
0&\longrightarrow
 \left(\mathcal O_{T,S_T}^\times/\mathcal O_{T,S_T}^{\times p}
       \otimes U\right)^G
\longrightarrow\mathcal P_p\\
&\longrightarrow
 \left(\operatorname{Cl}(\mathcal O_{T,S_T})[p]\otimes U\right)^G
\longrightarrow0.
\end{aligned}
\tag{189.8}
$$

这里用 inflation–restriction 把 $T$ 上的 Kummer 类下降到 $\mathbb Q$；有限商 $G$ 的一、二次上同调均为零。
前两项都一维，故第三项为零。
删除 $S_T$ 素理想所得的类群商，其核由上述置换模生成；该模没有所需整特征分量。
因此通常类群与 $S_T$ 类群在这个 $p$ 分量上相同。
Nakayama 引理遂给

$$
(\operatorname{Cl}(T)\otimes\mathbb Z_p[i])^{\widetilde\chi}
=(\operatorname{Cl}(T)\otimes\mathbb Z_p[i])^{\widetilde\chi^p}=0,
\qquad \chi(a)=a^{2p},\quad\chi^p(a)=a^2.
\tag{189.9}
$$

注意这里消失的是 **$U^\vee$ 的类群型**，不是 $U$ 本身；(189.8) 中张量 $U$ 后取不变量决定了这个方向。
同一论证还证明

$$
\boxed{\mathcal P_p=
\left((\mathcal O_T^\times/\mathcal O_T^{\times p})\otimes U\right)^G.}
\tag{189.10}
$$

## 3. 忠实域、精确导子及有限 Gras 等式

令 $\varpi_2=1+i$。由 $\gcd(2p,p^2-1)=2$，$\chi$ 在 $C$ 上的核恰为 $\{\pm1\}$；其忠实域为

$$
H=T^{\{\pm1\}}=K(\varpi_2^2p),\qquad
[H:K]=(p^2-1)/2.
\tag{189.11}
$$

导子可直接核对。模 $\varpi_2^3p$ 的 CRT primary 标签把局部单位根 $\zeta\in\mu_4$ 变成 $\zeta^{-1}$，于是 $\chi$ 在 $2$ 处取值

$$
\zeta^{-2p}=\zeta^2.
$$

它杀 $-1$ 而不杀 $i$，因此二进导子准确为 $\varpi_2^2$。
$p$ 处为非平凡 tame 角色，导子指数准确为一。
所以忠实角色的导子就是 $\varpi_2^2p$，没有额外的 $\varpi_2$，也没有更高 $p$ 次幂。

范数与扩张的复合乘 $[T:H]=2$，是 $p$ 单位；(189.9) 因而也给 $H$ 的两个相应类群分量为零。
Rubin 的有限 Gras 定理用于此 $H/K$：基域 $K$ 的 Hilbert 类域是 $K$，其单位根数为四，且
$p\nmid4[H:K]$；$\chi\oplus\chi^p$ 是非平凡不可约 $\mathbb Z_p$ 型。
该定理不要求 $p$ 在 $K$ 分裂。
结论为

$$
(\mathcal O_H^\times\otimes\mathbb Z_p[i])^{\widetilde\chi}
=(\mathcal C_H\otimes\mathbb Z_p[i])^{\widetilde\chi}
\simeq\mathbb Z_p[i],
\tag{189.12}
$$

其中 $\mathcal C_H$ 为椭圆单位群。
先对不可约 $\mathbb Z_p$ 型用指数等式，再扩系数分成两个特征即可；无需假定两部分长度相等。

令 $u_{\mathfrak a}$ 为导子 $\varpi_2^2p$ 的基本 Robert 单位。
该导子含两个不同素理想，故它们是真正全局单位。
因为 $\chi$ 在 $H/K$ 忠实，来自较小交域的生成元投影为零；其余模数都包含角色导子，可用 Robert 范数关系逐素理想降到该导子。
已有素因子提高指数的范数没有新增 Euler 项；新增素因子的范数只乘群环 Euler 项，不作除法。
因此这些 $e_{\widetilde\chi}u_{\mathfrak a}$ 生成 (189.12)。

Stark–Robert 交叉关系在无挠单位特征模中为

$$
(N\mathfrak b-\widetilde\chi(\sigma_{\mathfrak b}))
 e_{\widetilde\chi}u_{\mathfrak a}
=
(N\mathfrak a-\widetilde\chi(\sigma_{\mathfrak a}))
 e_{\widetilde\chi}u_{\mathfrak b}.
\tag{189.13}
$$

若从含单位根阶数的 Stark 幂关系出发，先在此无挠整模内消去同一个非零整数，再模 $p$；不能先模 $p$ 后除掉该整数。
单位根在当前特征中没有贡献。

取

$$
\beta=-1+2i,\qquad\mathfrak b=(\beta),\qquad N\mathfrak b=5.
$$

$\beta$ 为 $A$ 的 primary 元，算术 Artin 在 $A[p]$ 上作用为 $[\beta]$。
因 $p\equiv3\pmod4$，有

$$
e_\beta:=5-\chi(\beta)
=5-\beta^{2p}
=5-\bar\beta^2=8-4i\in\mathbb F_{p^2}^{\times},
\qquad N(e_\beta)=80.
\tag{189.14}
$$

所以整 Euler 因子 $5-\widetilde\chi(\sigma_{\mathfrak b})$ 对每个本题 $p$ 都是单位。
(189.12)–(189.13) 因而证明，单个 $e_{\widetilde\chi}u_{\mathfrak b}$ 是整个单位特征模的基。

从模数 $\varpi_2^3p$ 范数到 $\varpi_2^2p$ 只是已有素因子降一次指数。
两个模数的基域单位中，同余于一的都只有 $1$；Robert 公式因此没有单位阶数的比例，也没有 $1-\sigma_{\varpi_2}^{-1}$。
范数和扩张的复合为 $2$，故同一个原始 Robert 值在 $T$ 中的投影仍是基。

## 4. 一个次数二的实际函数，以及整数 $11$ 的零投影

取

$$
P_2=(i,1-i),\qquad Q=P_2+P.
$$

$P_2$ 的 $\mathcal O_K$ 零化子为 $\varpi_2^3$；$Q$ 是原始模 $\varpi_2^3p$ 点。
在 $A$ 上，非零 $[\beta]$ 核点满足 $[2]R=[-i]R$。
设 $R=(x,y)$、$X=x^2$。倍点公式给

$$
x([2]R)=\frac{(X+1)^2}{4x(X-1)},\qquad
\frac{y([2]R)}y=\frac{2X}{X-1}
\quad\text{当 }x([2]R)=-x.
$$

第二式等于 $-i$，准确给出

$$
x^2=\frac{1+2i}{5}=-\frac1\beta.
\tag{189.15}
$$

反向代回倍点式即可验证，两个 $x$ 值及其两种 $y$ 符号恰是四个非零核点。
因此相应 Robert 函数的分母为 $\beta x^2+1$。
对微分 $dx/(2y)$，$\Delta_A=64$。Scholl §1.2、Remark (v) 的一般有限子群规范使用 $\Delta(A)^5/[\beta]^*\Delta(A)$；因 $[\beta]^*\omega=\beta\omega$，其 Robert 规范常数满足

$$
\delta^{12}=\frac{\Delta_A^{5-1}}{\beta^{12}}
=\left(\frac4\beta\right)^{12}.
$$

所以在十二次单位根之外，原始 Robert 值就是

$$
v_\beta=\frac4{\beta x(Q)^2+1}\in T^\times.
\tag{189.16}
$$

这个单位根不影响模 $p$ Kummer 类。
(189.14) 的原始性遂适用于这个明确小函数。

相反，对原辅助理想 $(11)$，其 primary Artin 标签为 $-11$，于是

$$
121-\chi(-11)=121-(-11)^{2p}=0\pmod p.
$$

将 $\mathfrak a=(11)$ 和 $\mathfrak b=(\beta)$ 代入 (189.13)，因后者 Euler 因子是单位，得到

$$
\boxed{e_\chi[v_{11}]=0\text{ 于 }T^\times/T^{\times p}.}
\tag{189.17}
$$

这里 $v_{11}=64^{10}/\psi_{11}(P_2+P)$ 仍是 R163 的同一个原始值，只是现在投影到 $\chi=a^{2p}$。
(189.17) 与 R163 在 $a^{p-1}$ 分量上的非零生成性没有冲突。

## 5. 完整复共轭下降与全 $p$ primal 生成元

在 (189.3) 的 Kummer 张量模型中定义

$$
\xi_\beta=
\frac1{p^2-1}\sum_{a\in\mathbb F_{p^2}^{\times}}
 a^{-2p}[\sigma_a v_\beta].
\tag{189.18}
$$

这是 Cartan 不变张量；方括号表示乘法群的模 $p$ 加法记号。
对 $\bar\beta$ 同样定义 $\xi_{\bar\beta}$。
(189.13) 给

$$
e_{\bar\beta}\xi_\beta=e_\beta\xi_{\bar\beta},
\qquad e_{\bar\beta}=\overline{e_\beta}.
\tag{189.19}
$$

需要同时计算单位及系数上的复共轭。
由 $\tau P=P$、$\tau P_2=iP_2$，并且 (189.16) 的函数在 $[i]$ 下不变，

$$
\tau(\sigma_a v_\beta)=\sigma_{-i\bar a}v_{\bar\beta}.
$$

另一方面，$U$ 的复共轭为 $-\bar{\phantom x}$。
故

$$
\begin{aligned}
\tau\xi_\beta
&=-\frac1{p^2-1}\sum_a a^{-2}
       [\sigma_{-i\bar a}v_{\bar\beta}]\\
&=\frac1{p^2-1}\sum_b b^{-2p}[\sigma_bv_{\bar\beta}]
 =\xi_{\bar\beta}.
\end{aligned}
\tag{189.20}
$$

换元为 $b=-i\bar a$，此时 $a^{-2}=-b^{-2p}$；这正是抵消系数上那个负号的第二个负号。
不能只对函数系数取共轭来代替 (189.20)。

于是 (189.19)–(189.20) 给

$$
\tau(\xi_\beta/e_\beta)=\xi_\beta/e_\beta.
$$

限制映射对次数二的下降没有核。定义 $c_p^{\rm Rob}$ 为这个张量的唯一有理下降，则

$$
\boxed{\mathcal P_p=\mathbb F_p c_p^{\rm Rob},\qquad
\operatorname{res}_{T/\mathbb Q}c_p^{\rm Rob}=e_\beta^{-1}\xi_\beta.}
\tag{189.21}
$$

由 §3 的整原始性，该类非零；由 (189.5)，其 $p$ 定位不是 flat 类。
此处既没有在最后任意重缩放生成元，也没有为下降额外乘 $i$：与 R163 的不同复共轭符号已经完整写在 (189.20) 中。

## 6. 原来 $776$ 位素数上的实际值

现在取 $p=43$，并完全沿用 R171 的 $q$、全局标记、正 Frobenius 特征线上的 $P_q$ 和
$\zeta_q=e_{43}(P_q,iP_q)$。
因此这是同一个全局 $P$ 在已经固定的素点处的实现。
$q\equiv-1\pmod{4p}$，$A[p]$ 在 $\mathbb F_{q^2}$ 上全有理。

记

$$
\ell_a=
\log_{\zeta_q}\left(
 \bigl(\beta x(P_2+[a]P_q)^2+1\bigr)^{(q^2-1)/p}
\right),\qquad
S_\beta=\sum_a a^{-2p}\ell_a.
\tag{189.22}
$$

$\sum_a a^{-2p}=0$，故 (189.16) 中常数 $4$ 被投影杀掉。
函数的倒数给一个负号；平均因子 $1/(p^2-1)=-1\pmod p$ 再给一个负号。
由 $\mathbb Q_q$ 限制到未分歧二次域时，不分歧 $W$ 类在正特征线上的值乘二。
因此在 R168 的 primal 有限坐标 $aF$ 中，准确值为

$$
\boxed{a_q(c_p^{\rm Rob})=\frac{S_\beta}{2e_\beta}\in\mathbb F_p.}
\tag{189.23}
$$

其确实为实数也可由 (189.19)–(189.20) 直接验证。

标准库程序逐个计算了全部 $1848$ 个非零 $a$，所得数据为

| 量 | $\mathbb F_{43}[i]$ 中的值 |
|---|---:|
| $e_\beta$ | $8+39i$ |
| $e_{\bar\beta}$ | $8+4i$ |
| $S_\beta$ | $31+6i$ |
| $S_{\bar\beta}$ | $31+37i$ |
| $S_\beta/e_\beta=S_{\bar\beta}/e_{\bar\beta}$ | $20$ |
| $a_q(c_{43}^{\rm Rob})$ | $10$ |

复共轭辅助值还在取剩余符号之前逐点核对：

$$
\psi_{\bar\beta}(P_2+[a]P_q)
=\psi_\beta(P_2+[-i\bar a]P_q)^q.
$$

所以其离散对数为 $-\ell_{-i\bar a}$，而不是未经证明地只对最终总和取共轭。
两种计算权重 $a^{-2p}$ 与 $\bar a^{-2}$ 也逐项一致。
以字节三元组 $(\Re a,\Im a,\ell_a)$、按两个坐标递增的顺序拼接，完整日志的 SHA256 为

```text
dcbd26dd533afa5a983b61875a96cc7a5d2add021ff6589b6796f7dfc725894c
```

## 7. $p$ 处 AH 对偶坐标不再有未知比例

仅在本节，仍取 $p=43$。
用 R185 的同一个规范参数 $\pi$、轨道和算子 $\mathcal B$ 及基

$$
b_1=\mathcal B(E_{43}(\pi)),\qquad
b_{45}=\mathcal B(E_{43}(\pi^{45})).
$$

R185 的真实全局类在此基中为

$$
\operatorname{loc}_p d_p^{\rm Rob}=24b_1+20b_{45},\qquad
\operatorname{loc}_p d_q=20b_1+29b_{45}.
\tag{189.24}
$$

依此顺序，坐标矩阵行列式为 $38$；交换两行则为 $5$。
记局部 Tate 配对

$$
A_1=\langle c_p^{\rm Rob},b_1\rangle_p,\qquad
A_{45}=\langle c_p^{\rm Rob},b_{45}\rangle_p.
$$

$c_p^{\rm Rob}$ 和 $d_p^{\rm Rob}$ 在 $2,p$ 外不分歧；$2$ 处上同调为零。
全局互反给

$$24A_1+20A_{45}=0.$$

对 $d_q$，其他素数仍没有贡献。
$q$ 处 primal 类不分歧、有限坐标为 $10$；$d_q$ 的奇异坐标为 $1$。
R168 的精确杯积是 $2(ad-bc)$，故 $q$ 处贡献为 $20$。
于是

$$
20A_1+29A_{45}=-20\pmod{43}.
$$

两式有唯一解

$$
\boxed{(A_1,A_{45})=(6,10).}
\tag{189.25}
$$

这是按 (189.18)–(189.21) 的实际原始生成元和 R185 的实际 AH 基得到的完整泛函；没有再留任意非零比例。
特别地，$A_{45}=10\ne0$ 与命题 189.1 的“不属于 flat 线”相符，因为 R185 已证 $L_{\rm fl}^{\perp}=\mathbb F_{43}b_{45}$。

## 8. 二阶计算的准确接口与范围

本条完成了三件此前没有的事：全 $p$ 的 primal 原始单位、同一 $q$ 的非零有限值，以及它在同一 $p$ 局部 Kummer 基上的完整配对。
它也说明，直接从 R171 的 $\psi_{11}$ 模 $p$ 日志寻找这个 primal 类会得到零。

对一个已经求出的普通模 $p^3$ 全局提升，假设其 $\eta$ 分量已另行处理，记 $p$ 处剩余的 $W$ 差类为 $z$。
将这个 $W$ 分量调入 flat 直线时，$c_p^{\rm Rob}$ 的非零值 $A_{45}=10$ 给出确切的全局类校正：

$$
z\longmapsto z-
\frac{\langle z,b_{45}\rangle_p}{10}\operatorname{loc}_p c_p^{\rm Rob}.
\tag{189.26}
$$

它不改变对 $d_p^{\rm Rob}$ 的配对，因为 (189.25) 与 (189.24) 的第一行正交。
同时，加入 $c_p^{\rm Rob}$ 会改变 $q$ 的有限坐标；(189.26) 不是保持所有 Tate 条件的完整调整，仍须与 R180 的其他局部方程联立。
因此此校正也不消除固定晶体型的问题；R176 的 $\Omega_2$ 仍需实际计算二阶全局上链及其 $p$ 定位。
也不能从 (189.25) 自动得到 R180 晶体迹切线 $f$ 的单独比例
$k=\langle f,d_p^{\rm Rob}\rangle_p$。

R171 的同一个 $q$ 已被 Gaussian $5$ 整数迹条件排除为实际椭圆曲线支撑；本条没有构造新的实际椭圆曲线，也没有声称所有 $q$ 上的 (189.23) 都非零。
主目标所需的变化支撑及完整非线性条件仍然保留。

复算入口：

```bash
python3 verify_r189_primal_robert_generator.py --check
```

程序复用 R171 的 ECPP/Pratt 素性证书和原标记，重新验证配对及全部新函数值；它不调用类群程序或大次数域构造。

## 参考来源

- A. J. Scholl, *An introduction to Kato's Euler systems*, LMS Lecture Note Series **254** (1998), 379–460，§1.2，Theorem 1.2.1 后的 Remark (v)，印刷 p.385；[作者全文](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf)。这里使用任意阶与六互素的有限子群的 Robert 规范及 $\Delta(A)^{\#P}/\varphi^*\Delta(A/P)$，而不是把非整数辅助元直接冒称整数乘法除法多项式。
- K. Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*, Inventiones Mathematicae **103** (1991), 25–68，Theorem 3.3，印刷 p.35；[DOI](https://doi.org/10.1007/BF01239508)、[原刊档案](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0103)。使用的是有限非平凡字符的 Gras 指数等式；单位根条件针对基 Hilbert 类域。
- H. Oukhaba and S. Viguié, *On the Gras Conjecture for Imaginary Quadratic Fields*, Canadian Mathematical Bulletin **56** (2013), 148–160；[原刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)。引言 p.148 明确 Rubin 定理条件；§4 p.155 的 Robert/Stark 关系、两种范数分支与 Remark 4.3 提供 (189.12)–(189.13) 及同素数升指数接口。
- [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md) §§1–3：准确的最小局部条件、Conrad flat 环与 Poitou–Tate 维数。其 Conrad/Fontaine–Laffaille/最小 $R=T$ 原始来源全部沿用，本文 §1 重新给出放宽 $p$ 后的维数推导。
- [R163](R163-all-prime-primitive-adjoint-robert-generator.md) §§3–5：primary CRT 标签、有限 Gras 的整特征操作及 Robert 范数生成元。本文的字符是 $a^{2p}$，忠实域和 Euler 因子已独立重算。
- [R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)、[R171](R171-principal-norm-selflocal-tate-slope.md)、[R185](R185-p-local-robert-and-principal-unit-coordinates.md)：分别提供准确杯积、同一个全局标记和原始素数证书、同基的两条真实 $p$ 定位。R176/R180 的二阶阻碍没有被这些一阶配对替代。
