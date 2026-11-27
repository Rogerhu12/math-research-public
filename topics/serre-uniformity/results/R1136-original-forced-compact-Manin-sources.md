# R1136：原 forced 双权的紧致 Manin 来源与行列式角色

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明的范围。** 本文在模 $p$ 系数上构造两个真实的紧致来源：独立点对的 full-level Manin 循环，以及依赖点对的 $\Gamma_1(p)$ Manin 循环。前者经 symplectic-dual 坐标和 prime-to-$p$ transfer 落在原 $X_{\rm ns}^+(p)$；后者的实际 diamond 角色及其 quadratic 例外保留，不一概称为 $J_0(p)$ old 部分。所读的是 Sharifi–Venkatesh 的完整辅助 $\theta_n$ 符号，包含全部 cyclic-$n$ correlation，不是裸 Siegel cup。

另给物理 Hecke 对原 Weil 常数的准确作用及相应混合角色指标。这里不引用 SV 需要反除 level 的命题来消去新相关项，不宣布一个指定原 cup 为零，不构造完成的四阶覆盖。附节保留已经独立核准的同一标记内 bar-crossed 消去。

## 1. 原角色、原权与两个点对秩

固定 $p>37$，并令
$$
K=\mathbb Q(\zeta_p),\quad
\Delta=\operatorname{Gal}(K/\mathbb Q),\quad
m=(p-1)/2,\quad h=\lfloor p/4\rfloor-1.
\tag{F1}
$$
沿 R1062、R1070 的原规范，取
$$
V=\mathbb F_{p^2},\quad N:V\longrightarrow\mathbb F_p,\qquad
\chi=\omega^{p-1-2j},\quad\psi=\omega^{p-1-2k},
\quad 1\le j,k\le h.
\tag{F2}
$$
固定原 symplectic level 标记 $v\mapsto P_v$；$N$ 是该标记上的原非分裂二次型。取 $\mathbb F_p$ 值权
$$
a(v)=m^{-1}\chi(Nv)^{-1}=m^{-1}N(v)^{2j},\qquad
b(v)=m^{-1}\psi(Nv)^{-1}=m^{-1}N(v)^{2k}
\quad(v\ne0).
\tag{F3}
$$
它们是 R1070 的真实 augmentation-zero 整数权约模 $p$。下文模 $p$ 的符号加法只使用这些约化；需要实际乘法单位时仍选 R1070 的整数提升，不把 Teichmüller 数直接作函数指数。

记
$$
\theta=\chi\psi=\omega^a,\qquad
a=p-1-2(j+k).
\tag{F4}
$$
此处上标 $a$ 与函数 $a(v)$ 依各自位置区分。精确范围为
$$
\begin{cases}
4\le a\le p-5,&p\equiv1\pmod4,\\
6\le a\le p-5,&p\equiv3\pmod4.
\end{cases}
\tag{F5}
$$
因此实际二槽目标不含角色 $a=0$ 或 $a=2$。

完整非零点对按 $\det(v,w)\ne0$ 和 $\det(v,w)=0$ 分开。后一部分始终保留。模 $p$ 中的紧致性是来源循环的性质；它本身不表示其目标符号在尖点无 tame residue。

## 2. 实际辅助符号，及其系数范围

取素数 $n>3$、$n\ne p$。在原 full-level 开曲线的 universal elliptic curve 上，使用 SV §6.3 的两个实际 theta 函数：
$$
\operatorname{div}\theta_n=n^2[O]-[E[n]],\qquad
\operatorname{div}\theta'_{n,C}=n[C]-[E[n]],
\tag{F6}
$$
其中 $C$ 在全部 cyclic order-$n$ 子群中变化。第二个函数定义于加上 $\Gamma_0(n)$ 结构的曲线上。取 SV 的 trace-fixed 规范；其构造在 $\mathbb Z[1/30]$ 系数上成立，故可原样映入 $\mathbb Z_{(p)}$。这里“整 $p$ 系数”不等同于声称曲线在坏素 $p$ 有光滑模型。

对两个处处非零的原 $p$-torsion 标记定义
$$
B_n(P,Q)=
 \{\theta_n(P),\theta_n(Q)\}
 -
 \sum_{C\ {\rm closed}}
 \operatorname{Cor}_{C}
 \{\theta'_{n,C}(P),\theta'_{n,C}(Q)\}.
\tag{F7}
$$
和式按 cyclic-subgroup cover 的真实闭点及 residue fields 取 corestriction；没有除以分裂域次数或 $n+1$。式 (F7) 正是 SV (6.10)–(6.11) 的 pullback。它不同于辅助 $c$-torsion 平移笔记中的 $\Psi_c$。

所有被读的 $p$-torsion 点都避开 $E[n]$。对 full-level 的任一 primitive integral linear combination，模 $p$ 的系数不同时为零，因此仍避开该支撑。这支付了 SV big cocycle 在所需 full-level section、全部 Manin 边及 parabolic 比较中的 regularity。

SV Theorem 6.4.1、Lemma 6.4.4 的证明给出实际 Manin 反对称、三项关系和 parabolic cocycle；其中 $[-1]$ 的偶性已在 $\mathbb Z[1/30]$ 上核定。因而下文读数没有另一个未记录的 $p$ 次单位根相位。完整符号 (F7) 可以读紧致循环；本文没有把 SV 有理 unsmoothed 公式当作模 $p$ 的定义。

## 3. full-level 的 symplectic-dual convention

在 analytic uniformization
$$
E_\tau=\mathbb C/(\mathbb Z\tau+\mathbb Z),\qquad
(\tau/p,1/p)
$$
下，$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ 所给的同构 $z\mapsto z/(c\tau+d)$ 把原 level 坐标按 $\gamma^{-T}$ 运输。置
$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\gamma^{-T}=J\gamma J^{-1}\quad(\det\gamma=1).
\tag{F8}
$$
所以实际 torsion 标记是 $J$ 乘 Manin columns。来源二次型是 $N\circ J$，不是凭空假设 $J$ 保持原 $N$。

令 $e_\gamma=\gamma\{0\longrightarrow\infty\}$。若 $\gamma$ 的有序列为 $v,w$，则
$$
e_{J\gamma J^{-1}}=-J_*e_\gamma,
\qquad
(J\gamma J^{-1})_{\rm columns}=(-Jw,Jv).
\tag{F9}
$$
由于 $\theta_n,\theta'_{n,C}$ 偶，
$$
B_n(P_{-Jw},P_{Jv})=-B_n(P_{Jv},P_{Jw}).
\tag{F10}
$$
(F9) 与 (F10) 的两个负号同时消去。因此 pushed geodesic $J_*e_\gamma$ 的真实读数是正号的 $B_n(P_{Jv},P_{Jw})$。等价地，可在 big cocycle 中使用 section $(P_0,Q_0)J$；在 closed loops 上 conjugation 的两项 coboundary 消去。本文后文统一采用这个 convention。

因 $\det J=1$，此运输不改变 Weil determinant。它只把来源的几何群共轭为 $J^{-1}HJ$，并把 norm 权换成 $N\circ J$；两个改变全程一起保留。

## 4. 每个固定 determinant 的 forced 边界各自为零

设 $d\in\mathbb F_p^\times$。固定 $v\ne0$ 后，
$$
\{w:\det(v,w)=d\}=\{w_0+t v:t\in\mathbb F_p\}.
\tag{F11}
$$
这些 $w$ 全部非零。$N(Jw_0+tJv)^{2k}$ 是 $t$ 的多项式，次数至多 $4k<p-1$，所以
$$
\sum_{\det(v,w)=d} b(Jw)=0.
\tag{F12}
$$
常数项亦给零，因为 $\sum_{t\in\mathbb F_p}1=p=0$。交换两槽同理，由 $4j<p-1$ 得另一边界为零。这是每个 $d$ 的结论，不依赖跨 Weil 分量求和。

特别，在 determinant one 的 full-level Manin 模块中取
$$
C_{\chi,\psi}^{(2)}
 =\frac12\sum_{\det(v,w)=1}
 a(Jv)b(Jw)\, e(v,w).
\tag{F13}
$$
每个矩阵取其 $\mathrm{SL}_2(\mathbb Z)$ 提升；$e(v,w)$ 为相应 Manin 类。该定义不依赖提升。$1/2$ 只消去同时取负 $(v,w)\sim(-v,-w)$ 的双计数。

Manin 边界为第二端与第一端的差，依所选路径方向也可整体反号；(F12) 同时杀两个端点。因此
$$
C_{\chi,\psi}^{(2)}
 \in H_1(X(p),\mathbb F_p)
 \subset H_1(X(p),\{\text{cusps}\};\mathbb F_p).
\tag{F14}
$$
该紧致类可提升到整 $p$ homology：相对边界像是尖点 augmentation-zero 格，故模 $p$ 边界为零时可减去 $p$ 倍相对链。改变提升只改变读数的 $p$ 倍。

对 $j=k$，转置两槽并使用 $(v,w)\mapsto(-w,v)$ 和 Manin 反对称，得到 $C_{\chi,\chi}^{(2)}=0$。这不声称任意不同角色的类也为零。

## 5. 原正规化子正商，而非完整 Cartan 负商

令 $Z=X(p)_K$ 为固定 Weil 分量，且
$$
H=(N_{\rm ns}\cap\mathrm{SL}_2(\mathbb F_p))/\{\pm1\},
\qquad |H|=p+1.
\tag{F15}
$$
原曲线 $X=X_{\rm ns}^+(p)$ 满足 $X_K=Z/H$。在 (F8) 的来源 convention 中使用 $H'=J^{-1}HJ$。

norm-one Cartan 保持 $N$；determinant-one 的正规化子反射为 $\alpha\bar{\phantom z}$、$N\alpha=-1$，把 $N(v)$ 送到 $-N(v)$。$\chi,\psi$ 均偶，因此原两权在整个 $H$ 下不变。(F13) 于是为 $H'$-不变的真实紧致类。这直接给原正规化子正商；没有从另一个完整 Cartan 负块偷换来源。

对有限商 $f:Z\to X_K$，在 $\mathbb Z_{(p)}$ homology 上使用 trace/transfer：
$$
f_*f^!=[p+1],\qquad
f^!f_*=\sum_{g\in H}g_*.
\tag{F16}
$$
这是紧致曲线上的等式，不要求在椭圆点或尖点处处不分歧。由 $p\nmid p+1$，$H$-不变类准确来自 $X_K$；在 (F8) 的共轭坐标中先用 $J_*$ 运输即可。

设 $\mathfrak z_{n,Z}$ 为 (F7) 的紧致 Manin 读数。其对 level 变换的自然性由 SV big construction 给出；在相反的 pullback/pushforward convention 中同时取逆，不改变不变部分。下降读数可直接定义为
$$
\mathfrak z_{n,X}(c)
 =\frac1{p+1}\operatorname{Cor}_{K(Z)/K(X)}
       \mathfrak z_{n,Z}(f^!c).
\tag{F17}
$$
限制回 $K(Z)$ 后恰为被积的 $H$-不变类，因为 restriction–corestriction 给 $\sum_Hg^*$。本式只除 $p+1$；没有除以 level $p$。曲线上的 norm 保持非尖点处的 regularity。

通过已付整 Chen 比较，(F17) 的紧致 source 属于真实 Fricke 正部分中的 Cartan 因子。这里的正号是正规化子/Fricke 的号，不是把复共轭在全部 Jacobian 上称为正号。

## 6. Weil 分量、一次 Galois 投影与 all-vector 的系数二

在原 fixed-Weil full-level field 上定义
$$
S_d=\sum_{\det(v,w)=d}
 a(v)b(w)B_n(P_v,P_w).
\tag{F18}
$$
式 (F13) 的 $1/2$ 与 (F9)–(F10) 给出
$$
S_1=2\,\mathfrak z_{n,X}(c_{\chi,\psi}^{(2)})
\tag{F19}
$$
的限制；$c_{\chi,\psi}^{(2)}$ 是 (F16) 下降后的紧致类。

对 $d\ne0$ 选 Cartan 元 $b_d$，$N(b_d)=d$。它将 determinant-one 实际 ordered bases 送到 determinant-$d$ bases，Weil pairing 从 $\zeta_p$ 送到 $\zeta_p^d$。其作用在 Cartan 商上的常数正是 R1062/R1070 规定的 $\sigma_d$。换 $b_d$ 只乘一个 norm-one 元，已由 (F15) 商掉。

重指标给准确方向
$$
\sigma_d S_1=\theta(d)S_d.
\tag{F20}
$$
这是函数的原 Galois 作用，不是把任意 determinant-$d$ 裸点对冒作同一 fixed-Weil unimodular edge。故完整独立部分满足
$$
\sum_{d\ne0}S_d
 =2\sum_{d\ne0}\theta(d)^{-1}
       \sigma_d\mathfrak z_{n,X}(c_{\chi,\psi}^{(2)})
 =2(p-1)e_\theta
       \mathfrak z_{n,X}(c_{\chi,\psi}^{(2)}).
\tag{F21}
$$
这里 $e_\theta=(p-1)^{-1}\sum_d\theta(d)^{-1}\sigma_d$。只作一次实际角色投影；系数二来自 all-vector 对 simultaneous-$\pm$ Manin 边的双计，不是额外一次 bar norm。

## 7. 全部依赖点对的实际 $\Gamma_1(p)$ 紧致来源

设
$$
\alpha(c)=\chi(c^2)^{-1},\quad
\beta(d)=\psi(d^2)^{-1}\qquad(c,d\in\mathbb F_p^\times).
$$
原角色满足 $\chi^2,\psi^2\ne1$，所以
$$
\sum_{c\ne0}\alpha(c)=\sum_{d\ne0}\beta(d)=0.
\tag{F22}
$$
采用 SV §4.3 的标准 bottom-row Manin convention：
$$
[c:d]=\gamma\{0\to\infty\},\qquad
\gamma=\begin{pmatrix}*&*\\c&d\end{pmatrix}\in
\mathrm{SL}_2(\mathbb Z).
$$
当 $c,d\ne0$ 时，两端尖点的非零 lower residue 分别为 $d,c$，并只按同时 $\pm$ 识别。由 (F22)，
$$
C_{\chi,\psi}^{(1)}
 =\frac12\sum_{c,d\ne0}
       \alpha(c)\beta(d)[c:d]
 \in H_1(X_1(p),\mathbb F_p).
\tag{F23}
$$
这也是逐端点的实际边界抵消。没有把无穷尖点或 bottom coordinate 为零的边偷偷加入。

SV 原 section $(0,P)$ 在该边的读数就是 $B_n(cP,dP)$，故
$$
\mathfrak z_{n,1}(C_{\chi,\psi}^{(1)})(E,P)
 =\frac12\sum_{c,d\ne0}\alpha(c)\beta(d)
                          B_n(cP,dP).
\tag{F24}
$$
diamond $t:P\mapsto tP$ 的重指标给
$$
\mathfrak z_{n,1}(C_{\chi,\psi}^{(1)})(E,tP)
 =\theta(t^2)\,
   \mathfrak z_{n,1}(C_{\chi,\psi}^{(1)})(E,P).
\tag{F25}
$$
其角色准确为 $\theta^2$。若 $p\equiv1\pmod4$ 且 $j+k=(p-1)/4$，则 $a=m$、$\theta=\omega^m$ 为 quadratic，因而 $\theta^2=1$。除此例外外 diamond 非平凡；$p\equiv3\pmod4$ 时 $a$ 偶而 $m$ 奇，故无该例外。两个单独角色 $\chi^2,\psi^2$ 始终非平凡，所以 (F22)–(F26) 在该例外中完全不变。

对每条 $\mathbb F_p$-line $L\subset V$ 选 $v_L\ne0$，置 $P_L=P_{v_L}$，令 $\pi_L$ 为从原 full level 忘到 $(E,P_L)$ 的真实模映射。完整依赖部分准确为
$$
S_{\rm dep}
 =2\sum_L a(v_L)b(v_L)\,
          \pi_L^*\mathfrak z_{n,1}(C_{\chi,\psi}^{(1)}).
\tag{F26}
$$
更换 $P_L\mapsto tP_L$ 时，前因子乘 $\theta(t^2)^{-1}$，后者乘 $\theta(t^2)$，所以 (F26) 不依赖各 line 的生成元。H-不变性与 Cartan 下降仍按 (F17) 的实际 norm 完成。

式 (F26) 只用 pullback，**没有除以** full-level 到 $\Gamma_1(p)$ 的 degree $p$。它没有把此 diamond source 嵌入原 Cartan 的同一个紧致 Hecke 格。欲以 normalized twist $\theta^{-1}$ 将 level-$p$ nebentype $\theta^2$ source 接到 square-level 部分（通常为 principal series；quadratic 例外须另保 ramified Steinberg 支），仍须付该真实整 Hecke 接口与正规化子符号；本文没有据此删除 (F26)。

## 8. 原函数类、物理 Hecke 和准确混合门

### 8.1 第一项确回原函数，但 correlation 保留

在所选 local Hodge frame 上 $\theta_n(P)=\lambda(E)\psi_n(P)^{-1}$；两个函数的 fiber divisor 相同。完整 augmentation-zero 权消去共同 $\lambda(E)$。逐 fixed-det 的模 $p$ 行列和 (F12) 亦消去相应模 $p$ 常数符号。

若 $M_{n,\chi}$ 是 R1070 的 all-vector division product，则
$$
[M_{n,\chi}]=\frac{2\kappa_\chi(n)}m[F_\chi],
\qquad
\kappa_\chi(n)=n^2-\chi(n^2).
\tag{F27}
$$
因此完整双权 (F7) 的第一项准确为
$$
\{M_{n,\chi},M_{n,\psi}\}
 =\frac{4\kappa_\chi(n)\kappa_\psi(n)}{m^2}
       \{F_\chi,F_\psi\}\pmod p.
\tag{F28}
$$
但其第二项是全部 cyclic-$n$ closed corestrictions：
$$
\sum_C\operatorname{Cor}_C
 \left\{\prod_{v\ne0}\theta'_{n,C}(P_v)^{n_{\chi,[Nv]}},
        \prod_{w\ne0}\theta'_{n,C}(P_w)^{n_{\psi,[Nw]}}\right\}.
\tag{F29}
$$
(F21)、(F26) 给的是 (F28) **减去** (F29) 的完整来源，绝不只给 (F28)。

若需要同时 $\kappa_\chi(n),\kappa_\psi(n)$ 为单位，可先选 Fp 乘法群中避开两个 proper subgroup 的一个剩余类，再用 Dirichlet 取该类中的素数 $n>3$。它可能大于 $p$；此时不能再称其 $n$-torsion splitting degree prime-to-$p$。式 (F7)、(F29) 使用真实 corestriction，不除该次数，故无此需要。

### 8.2 物理 Hecke 的 determinant 修正

令 $T_\ell$ 为原 $\mathbb Q$ 曲线 $X$ 上的通常 prime-to-$p$ Hecke correspondence，并在 $X_K$ 上固定常数。令 $\widetilde T_\ell$ 保留 physical isogeny 运输的两个 full-level 标记，尚不把 target Weil root reset；令 $\widetilde{[\ell]}$ 为同时乘两个标记以 $\ell$。

由 Weil pairing 的 isogeny 公式以及原 Cartan 商的定义，
$$
\widetilde T_\ell=\sigma_\ell T_\ell,\qquad
\widetilde{[\ell]}=\sigma_{\ell^2}.
\tag{F30}
$$
具体地，physical quotient 把 $\zeta_p$ 送到 $\zeta_p^\ell$，在 underlying $X$ 上是原 Hecke；scalar $\ell I$ 不改变 necklace，而把 pairing 送到 $\zeta_p^{\ell^2}$。这个说明也固定了 $\sigma_\ell$ 而非其逆。两侧在 motivic pullback/corestriction 上按同一 source–target 次序解释。

故原 SV 平滑多项式的物理版本在 $\theta=\omega^a$ 部分为
$$
\widetilde V_\ell^{(a)}
 =\ell^4-\ell^{a+2}T_\ell+\ell^{2a+1}
 =\ell^{a+2}
   \bigl(\ell^{2-a}+\ell^{a-1}-T_\ell\bigr).
\tag{F31}
$$
保留了整个 $\ell^2 T'_\ell$ 项。其 residual common ideal 是
$$
I_r,\qquad r\equiv2-a\pmod{p-1},
\qquad r=2j+2k+2.
\tag{F32}
$$
本次 forced 二槽范围没有 $I_0$。也不能因为讨论的是“常中心”就预设 $a=0$：常 Lie 二阶中心对应 Kummer/Tate 角色 $a=2$；四阶常中心的总 Kummer 角色为 $a=4$，是另一个尚须构造的高 cochain 接口。

### 8.3 已付的整块排除仅在明确混合范围内

若
$$
r=2(j+k+1)<m,\qquad
p\nmid B_{\,4j+4k+4}\,B_{\,p-3-4j-4k},
\tag{F33}
$$
则 R1132 的实际整块定理使原 $X$ 的紧致 Hecke 格上 $I_r$ 块整个消失。因而 (F31) 的全部 prime-to-$p$ smoothing operators 在该**原紧致格的 Hecke 代数**中生成单位理想：若有共同极大理想，(F31) 会逐素数迫其 residual system 为已消失的 $I_r$。

这不是 R1131 奇 $K$-rational torsion 消失的同义改写。R1131 的高偶块本身通常存在；不能用其 odd-torsion 结论宣布 (F31) 在整紧致格上为单位。

原 §9 四阶指定配置的非重复邻对 $(j,k)$ 在 $p=8t+1,8t+3,8t+5,8t+7$ 四行分别给
$$
r=m+2,\quad m+3,\quad m+4,\quad m+1.
\tag{F34}
$$
它们不在 (F33)。重复邻对 $(j,j)$ 的符号可由反对称为零，但不能因此把不同角色的邻对也置零。

### 8.4 本文明确保留的 operator / unsmoothing 门

SV §6.5 的 big cocycle comparison 是实际 integral comparison；SV Lemma 7.2.5 的源 Hecke factorization 只需 $6$ 可逆。根端已逐原文核此范围。与之不同，SV Proposition 7.2.6 的排公共极大理想步骤要求 residual prime 不除 level，不能在这里取 residual prime $p=N$。

本文已给 (F17) 的原紧致读数、(F30) 的实际 target determinant 规范，以及 (F33) 的原紧致格单位理想。仍不得跳过以下两项：

1. 将 big comparison 对所有所选 full-level sections、$H$-transfer 和全部 determinant components 的 source–target action 逐式组成同一 Hecke-equivariant unsmoothing construction。其输入必须是 (F7) 的完整 $\theta_n$ 族，不能把 SV (7.6) 的有理 bare Siegel formula 直接约模 $p$。
2. 对 rank-one 的 (F26) 保留真实 diamond $\theta^2$ 及上述 quadratic 例外，支付其 square-level twist 或另一原源接口；不能从 $X(p)\to X_1(p)$ 的 degree $p$ pullback 构造一个未经证明的逆。

即使后续完成这些 operator 接口，所得仍先是一个真实的 cup/correlation 或 modular-symbol 映射。一个非零紧致循环的像可以非零；源块排除不自动等于指定单 cup 为零。真正四阶覆盖还需实际低 cochains、全部 crossed 项及 cusp inertia moments。

## 9. 同一标记的 bar-crossed 整消去

沿已发布的跨 line 弦线笔记，取非零原 $p$-torsion 点
$$
P=P_z,\quad Q=P_{az},\quad S=P_{\mathsf i z},
\qquad a\ne0,\pm1,\quad \mathsf i^2=\delta\notin\mathbb F_p^{\times2}.
$$
这里 $\mathsf i$ 只作用于 level 标签。令
$$
d(A,B)=x(A)-x(B),\qquad
U(T)=\ell_{P,Q}(T)/\ell_{P,-Q}(T),\qquad V=1-U,
$$
保持该笔记的首项归一 chord。两点 $S,-S$ 给
$$
A=U(S)U(-S)=\frac{d(S,P+Q)}{d(S,P-Q)},\qquad
W=1-A=\frac{d(P+Q,P-Q)}{d(S,P-Q)}.
\tag{F35}
$$
真实 elliptic addition identity
$$
d(P+Q,P-Q)d(P,Q)^2=-4y(P)y(Q)
$$
与已经核准的 $V(S)V(-S)$ 式给
$$
V(S)V(-S)=R\,W,\qquad
R=\frac{y(Q)}{y(P)}\,\frac{d(S,P)}{d(S,Q)}.
\tag{F36}
$$
各项都是原开曲线上的实际 weight-zero 单位；$p$ 奇且各点非零保证 $y(P),y(Q)$ 不为零，独立 line 条件避免其余 collision。

于是直接用整 Steinberg 关系得到
$$
\boxed{\quad
 \{U(S)U(-S),\,V(S)V(-S)\}
 =\{A,R\}.
 \quad}
\tag{F37}
$$
这是同一 $z$ 上四个 bar-crossed 项的完整消去，右边不是零。完整双权求和中 $z\ne z'$ 的 crossed 项仍存在；本文没有用 (F37) 删除它们。

## 10. 原始来源与复核范围

- Romyar Sharifi、Akshay Venkatesh，*Eisenstein cocycles in motivic cohomology*，Compositio Mathematica 160 (2024), 2407–2479；本文定理编号采用作者全文
  <https://www.math.ucla.edu/~sharifi/publ/eisensymbol.pdf>。
  实读 §§6.3–6.5、(6.10)–(6.11)、Theorem 6.4.1、Lemma 6.4.4、
  §§7.1–7.3，及 §4.3 的标准 Manin convention。
  其 $n$-符号与本文原辅助 $c$-torsion 平移符号分开。
- R1062、R1070：原 cusp/Galois 方向、真实整数权、all-vector division product
  及全 cusp leading 规范。
- R1131、R1132：原 same-prime 整 Chen/Hecke 接口；
  只按 (F33) 消费 R1132 的**整块**消失。
- [原跨 line 弦线源](../notes/2026-11-28-original-cross-line-chord-unit-equations.md)：
  实际 $U,V$、一次 bar norm、全部相位与 elliptic addition identity。
- [原辅助相关项](../notes/2026-11-28-original-auxiliary-c-torsion-Manin-correlation.md)：
  不删除 closed corestrictions 或不同标记交叉项。

本文无数学程序执行。o2_high_coefficient 独立纸核 fixed-determinant 多项式边界、
实际二槽角色、条件 Hecke 因式，以及 rank-one bottom-row 紧致循环/diamond 方向；
同一标记的 (F35)–(F37) 已由 root 与 o2 独立核准。


root 已逐原文核 SV 的 E′ 是 degree n+1 的 base change、完整 norm、§4.3 的 bottom-row 路径方向，以及 §§6.3–6.4 的 integral 范围；并独立支付 (F8)–(F10) 的 analytic dual convention。候选 4caa7fd50d18d28a71e13714c9fa44ce1bb7dc92 已保 θ²=1 的 quadratic 例外。上述未付 operator / rank-one twist / 四阶门仍按 §8.4 保留。
