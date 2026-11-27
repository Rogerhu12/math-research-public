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


## 11. 完整 smoothed 来源的原 Hecke 相容性

本节补齐 §8.4 的第一项中 **smoothed** 来源的 Hecke 门。所有 $\ell$ 均为不同于 $p$ 的素数；辅助 $n$ 仍按 §2 取值。系数先在 $\mathbb Z[1/30]$ 上处理，再约模 $p$。没有引用 SV Proposition 7.2.6。

### 11.1 在所有真实 ordered bases 上保持 regularity

在 universal $E^2$ 上，把 SV §7.1 的 regular 子群改为沿所有原 ordered $p$-bases 的 sections 同时 regular 的子群，记为 $K_2^{\rm bas}(p)$。若需包含所有 Weil 分量，就在相应有限不交并上作同一构造。这是沿该有限 section 集的开邻域之 motivic cohomology 的直接极限。

determinant prime to $p$ 的整矩阵排列这些 sections。prime-to-$p$ isogeny 的源、靶基也仍是 ordered bases，所以物理 pullback–corestriction 保持这个 regular 子群。对 ${}_n\Theta$ 出现的每个 primitive row，其在任何 ordered basis 上都是非零 $p$-torsion 点；$n\ne p$ 保证它不碰 $E[n]$。因此整个 smoothed cocycle、各 source Hecke 作用及各 physical target Hecke 作用均取值于 $K_2^{\rm bas}(p)$。

SV Lemma 7.1.1 的 injectivity 证明对此有限 section 集原样成立。具体地，Gysin sequence 将不 regular 的差项放入经过这些 sections 的水平不可约 divisor 所给的有限支撑直和。在 generic non-CM elliptic fiber 上，
$$
\operatorname{NS}(E^2)\otimes\mathbb Q
$$
是 binary quadratic forms 的三维表示；非零有效 divisor 的 NS 类非零，且在 $\mathrm{SL}_2(\mathbb Z)$ 下轨道无限。在任意 finite-index subgroup 下轨道仍无限。因此上述有限支撑直和没有不变元，给出
$$
H^1(\Gamma,K_2^{\rm bas}(p))
 \longrightarrow H^1(\Gamma,K_2)
\quad\text{单射}
\tag{F38}
$$
对本文所用每个 finite-index $\Gamma$ 成立。沿 section 集移去的 divisor 都支配 base；垂直 divisor 不是这个相对 regularity 比较中的新增项。

所以 SV Theorem 6.5.4 在 big $K_2$ 中的相容等式已经在 (F38) 的 regular 子群中成立，可以实际 pullback 到原 full-level curve。这一步不需要先在 $p$ 处约化曲线，更不需要除以 $p$。

### 11.2 限制到原 Cartan 群的 CRT 陪集

令 $\Gamma_{H'}\subset\mathrm{SL}_2(\mathbb Z)$ 为 $H'=J^{-1}HJ$ 的 inverse image。取 $b_\ell$ 为原 Cartan 中 norm 为 $\ell\bmod p$ 的元素，置
$$
\bar g=J^{-1}b_\ell J.
$$
存在整矩阵 $g$ 满足
$$
\det g=\ell,\qquad g\bmod p=\bar g:
\tag{F39}
$$
从 $\operatorname{diag}(\ell,1)$ 出发，左乘一个 lifting
$\bar g\operatorname{diag}(\ell^{-1},1)\in\mathrm{SL}_2(\mathbb F_p)$
的 $\mathrm{SL}_2(\mathbb Z)$ 元即可。因 $b_\ell$ 正规化 $H$，$g\bmod p$ 正规化 $H'$。

在 $\ell$ 处，$g$ 的 Smith form 为 $\operatorname{diag}(\ell,1)$。条件
$g^{-1}\gamma g\in M_2(\mathbb Z)$ 恰为 $\gamma\bmod\ell$ 保持一条 line；在 $p$ 处不添加条件，因为 $\bar g$ 正规化 $H'$。CRT 给
$\Gamma(p)\twoheadrightarrow\mathrm{SL}_2(\mathbb F_\ell)$，所以
$$
[\Gamma_{H'}:\Gamma_{H'}\cap g\Gamma_{H'}g^{-1}]=\ell+1.
\tag{F40}
$$
可取 $\gamma_i\in\Gamma(p)$ lifting 各个
$\mathbb P^1(\mathbb F_\ell)$ coset，令 $g_i=\gamma_i g$。
于是 $g_i$ 同时是一组 full-$\mathrm{SL}_2$ Hecke right-coset representatives 和一组 $\Gamma_{H'}$ representatives，且全满足 $g_i\bmod p=\bar g$。

若 $\gamma\in\Gamma_{H'}$ 且
$\gamma g_i=g_{\sigma(i)}\gamma_i'$，则
$\gamma_i'\bmod p=\bar g^{-1}\bar\gamma\bar g\in H'$。
因此 big cocycle 的 Hecke 公式限制后逐项就是原 $\Gamma_{H'}$ 公式，没有暗中换 level，也没有以较大群的一个 double coset 代替原群的多个未知 double cosets。由 $2$ 可逆，从 SV 的 $\mathrm{GL}_2$ convention 限制到 determinant-positive 部分不添加整 $p$ 分母。

### 11.3 determinant-$\ell$ 的 dual convention 与同一 $\sigma_\ell$

对 $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$、$\det g=\ell$，实际 degree-$\ell$ analytic isogeny 是
$$
E_\tau\longrightarrow E_{g\tau},
\qquad z\longmapsto\frac{\ell z}{c\tau+d}.
$$
在 $(\tau/p,1/p)$ 的 level columns 上，其矩阵为
$$
\ell g^{-T}=JgJ^{-1}.
\tag{F41}
$$
所以不能在 determinant $\ell$ 时只搬用 $g^{-T}$，但实际 isogeny 的这个 $\ell$ 恰好补足该因子。按 (F39)，所有 Hecke summands 的 physical marking change 都是同一个 $b_\ell$。

经 $H$-trace 后，该 coefficient action 正是原 $\sigma_\ell$。由 (F38)–(F40) 限制 big comparison，并用有限商 transfer 与 isogeny pull–push 的相容性，得到
$$
\sigma_\ell\,
 \mathfrak z_{n,X}(T_\ell c)
  =\widetilde T_\ell\,\mathfrak z_{n,X}(c)
  =\sigma_\ell T_\ell\,\mathfrak z_{n,X}(c).
$$
这里所有 $T_\ell$ 均用 SV (6.14)–(6.15) 的同一 source–target convention；在 coarse quotient 的 elliptic stabilizers 处保留原 pull–push multiplicities。约去两侧同一个可逆 $\sigma_\ell$，即
$$
\boxed{\;
\mathfrak z_{n,X}(T_\ell c)
 =T_\ell\,\mathfrak z_{n,X}(c).
\;}
\tag{F42}
$$
$\Delta$ 与 $T_\ell$ 交换，故 (F42) 也保持 $e_\theta$ 部分。它只陈述完整 $B_n$ 读数的相容性，未将 $B_n$ 的 cyclic correlation 删掉。

## 12. rank-one source 的 exact twist 与 away-from-$p$ 整 Hecke 商

本节补齐 (F26) 的实际谱及整算子来源。将 $\theta$ 作 Teichmüller 提升 $\widehat\theta:\mathbb F_p^\times\to\mathbb Z_p^\times$。它非平凡且偶。下列特征零论证用一个兼容的复嵌入；最后的整 Hecke 商及其模 $p$ 约化独立于此选择。

### 12.1 exact conductor 为 $p^2$

对 $S_2(\Gamma_0(p),\widehat\theta^2)$ 中任一 normalized eigenform $f$，令
$$
g=f\otimes\widehat\theta^{-1},
\qquad
a_\ell(g)=\widehat\theta(\ell)^{-1}a_\ell(f)
\quad(\ell\ne p).
\tag{F43}
$$
该 level-$p$ source 全部 new：若 $\widehat\theta^2\ne1$，nebentype 已有 conductor $p$；若 $\widehat\theta^2=1$，level-one 的 weight-two cuspidal space 为零。

若 $\widehat\theta^2\ne1$，$f$ 在 $p$ 的 local type 是一条 unramified character 与一条 conductor-one character 的 principal series。twist 后两条 inertia characters 为 $\widehat\theta^{-1}$ 与 $\widehat\theta$，均非平凡，各有 conductor exponent one，所以 exact conductor exponent 为 two。若 $\widehat\theta^2=1$，$f$ 的 local type 是 Steinberg 的 unramified twist；再扭以非平凡 ramified quadratic $\widehat\theta$，conductor exponent 亦为 two。

这也直接满足 Shemanske–Walling Theorem 7.1(2)：原 level exponent 为 one、twisting conductor exponent 为 one，而 $\operatorname{cond}(\widehat\theta^2\widehat\theta^{-1})=p$。因此 $g$ 是 exact level $p^2$、trivial nebentype 的 normalized newform；(F43) 是实际 Fourier coefficient 等式。

### 12.2 真实正规化子正号

上述 principal-series finite type 为
$\operatorname{Ind}_B^{\mathrm{GL}_2(\mathbb F_p)}
(\widehat\theta^{-1},\widehat\theta)$。
其 non-split Cartan fixed space 是一维。对反射 coset 作 character average：split 半部贡献 $2\widehat\theta(-1)$，non-split 半部贡献零，故 normalizer involution 在固定线上作用为
$\widehat\theta(-1)=1$。

quadratic 例外的 finite type 为
$\operatorname{St}\otimes(\widehat\theta\circ\det)$。
其 Cartan fixed space 也为一维；反射 coset 上每个 character value 都是
$\widehat\theta(-1)$，故仍取正号。这项保留了 §7 的真实例外，没有把它误并入 irreducible principal series。

这些是原 full-level 的有限表示，因而 $g$ 出现在原 $X_{\rm ns}^+(p)$ 的 Hecke 谱中。经原 Chen 比较，它属于 $p^2$ 的 Fricke 正 new 部分。等价的 local epsilon 检查是
$\tau(\widehat\theta)\tau(\widehat\theta^{-1})
=\widehat\theta(-1)p$；两条 unramified factors 抵消，quadratic Steinberg twist 给相同正号。此 Gauss 恒等式只核符号，下一步并不以 Gauss sum 除整格。

### 12.3 不需 integral twisting matrix 的整 Hecke 商

令 $\mathbb T_X^{(p)}$ 是原 compact $X$ 的 $\mathbb Z_p$-Hecke order，由 $T_\ell$、$\ell\ne p$ 生成。令
$\mathbb T_{1,\widehat\theta^2}^{(p)}$
是 compact level-$p$ source 的对应 away-from-$p$ Hecke order，diamond 已固定为 $\widehat\theta^2$。则有实际满射
$$
\boxed{\quad
\mathbb T_X^{(p)}
 \twoheadrightarrow\mathbb T_{1,\widehat\theta^2}^{(p)},
\qquad
T_\ell\longmapsto
 \widehat\theta(\ell)^{-1}T_\ell^{(1)}.
\quad}
\tag{F44}
$$

证明不需要在 $p$ 整同调上制造除以 Gauss sum 的 twisting operator。若 $P(T_{\ell_1},\dots,T_{\ell_s})=0$ 是原 compact Hecke order 的关系，则它在每个实际 $g$ 上为零；(F43) 使
$P(\widehat\theta(\ell_i)^{-1}T_{\ell_i}^{(1)})$
在 source 的全部特征零 eigenforms 上为零。Eichler–Shimura 与特征零 Hecke semisimplicity 使其在 compact source 的 rational homology 上为零。该 homology 的 $\mathbb Z_p$ 格无挠，所以它在整格上也为零。所有 $\widehat\theta(\ell_i)$ 为 $\mathbb Z_p$ 单位，故所得 image 包含全部 source generators，证明满射。

此证明只用 same-spectrum 的实际 Fourier coefficient 关系，既不声称两个 compact homology 格同构，也不声称 normalized analytic twist 本身是 $p$-integral。**(F44) 不包含 level-$p$ 的 $U_p$**：exact level-$p^2$ new source 的 $T_p=0$ 不能自动运输为 $U_p$；本文不需要这个未经证明的扩大。

## 13. 原 line 加权 pull–push 与 twisted source 的相容

本节全在模 $p$ 中；(F44) 给所需的整来源，约模后使用。设 $c$ 属于 compact level-$p$ source 的 diamond-$\theta^2$ 部分，定义
$$
\Phi_n(c)=\frac1{p+1}
 \operatorname{Cor}_{K(Z)/K(X)}
 \sum_{L\in\mathbb P(V)}
 m^{-2}\theta(Nv_L)^{-1}
 \,\pi_L^*\mathfrak z_{n,1}(c).
\tag{F45}
$$
其 source conventions 与 (F23)–(F26) 完全相同。更换 $v_L\mapsto tv_L$，权乘 $\theta(t^2)^{-1}$，被 pullback 的实际 diamond eigenclass 乘 $\theta(t^2)$，所以每项不变。norm-one 和反射的变换同 §5，故可作原 $H$-trace。Cartan determinant $d$ 的重指标给
$$
\sigma_d\Phi_n(c)=\theta(d)\Phi_n(c).
\tag{F46}
$$
没有第二次 Galois projection 或额外 bar norm。

固定 $\ell\ne p$。从 full level 忘到 $(E,P_L)$，再加一个 cyclic order-$\ell$ kernel，与先加该 kernel 再忘标记，是同一个 Cartesian moduli square。quotient 把 $P_L$ 送到 $P_L+C$；所有原 norm 权保留不变。有限 $H$-corestriction 与这个 pullback–pushforward 交换。因此直接由 SV Proposition 7.1.3 的 **smoothed** Hecke 等式得到
$$
\Phi_n(T_\ell^{(1)}c)
  =\widetilde T_\ell\Phi_n(c)
  =\theta(\ell)\,T_\ell\Phi_n(c).
\tag{F47}
$$
这里 $\widetilde T_\ell=\phi_*\psi^*$，
$\phi(E,P,C)=(E,P)$、
$\psi(E,P,C)=(E/C,P+C)$，与原 (F30) 同方向。没有额外 adjoint 或 diamond factor；若换成 dual Hecke convention，必须同时改两端。

所以 (F45) 对 (F44) 的 quotient action 真正 Hecke-equivariant：
$$
\Phi_n\bigl(\theta(\ell)^{-1}T_\ell^{(1)}c\bigr)
 =T_\ell\Phi_n(c).
\tag{F48}
$$
这支付的是实际 weighted line pull–push；没有把 full-level 至 $X_1(p)$ 的 degree-$p$ pullback 反除，也没有假定一个整 $p$ twisting matrix。

对 §7 的指定 $C_{\chi,\psi}^{(1)}$，(F26) 在原 $X$ 上的读数为 $2\Phi_n(C_{\chi,\psi}^{(1)})$。将 (F44) 作用于 (F31) 得
$$
\widetilde V_\ell^{(a)}
 \longmapsto
 \ell^4-\ell^2T_\ell^{(1)}
       +\ell\,\theta(\ell^2).
\tag{F49}
$$
因此在明确混合门 (F33) 成立时，原 compact $X$ 上的 smoothing unit-ideal 也满射到这个真实 rank-one compact source；quadratic 例外仍照 (F43)–(F49) 处理。这不需要 SV Proposition 7.2.6 的 $p\nmid N$ 假设。

### 13.1 单位理想上的真实 unsmoothing，以及它没有消掉的部分

设 (F33) 成立，记
$$
L=H_1(X,\mathbb F_p)\ \oplus\
  H_1(X_1(p),\mathbb F_p)_{\theta^2},
\quad
\Psi_n(x,y)=2(p-1)e_\theta\mathfrak z_{n,X}(x)+2\Phi_n(y).
\tag{F50}
$$
第二个 summand 的 $\mathbb T_X^{(p)}$-action 是 (F44) 的约化，仍用同一 SV compact-source convention。以
$V_n=n^4-n^{a+2}T_n+n^{2a+1}$
表示该代数在 $L$ 上的作用。

SV Lemma 7.2.1 的证明只使用 big integral comparison 及 (F38) 的 injectivity；加上 (F40) 的限制后，完整 smoothed family 满足
$$
\Psi_n\circ V_\ell=\Psi_\ell\circ V_n,
\qquad
\widetilde V_\ell\,\Psi_n=\Psi_n\circ V_\ell.
\tag{F51}
$$
$\widetilde V_\ell$ 在这里是 target 上的真实 physical correspondence polynomial；虽然在 $\theta$ 部分公式与 source 的 $V_\ell$ 相同，暂不将 source Hecke order 的全部关系强加给整个 target。

(F33) 与 (F44) 给有限多个 $n_i>3$、$n_i\ne p$，及 source Hecke operators $A_i$，使
$\sum_iA_iV_{n_i}=1_L$。
这里只用 $n_i>3$ 仍足够：若有 maximal ideal 同时包含这些 $V_n$，则其实际 residual Galois traces 在所有 $n>3$、$n\ne p$ 上为 $n^r+n^{1-r}$。Chebotarev 迫同一 residual pseudorepresentation，故也满足被排除的 $I_r$；删去 $2,3$ 不产生新 block。

现在定义一个实际 source map
$$
\Psi=\sum_i\Psi_{n_i}\circ A_i.
\tag{F52}
$$
由 (F51) 直接得
$\Psi\circ V_\ell=\Psi_\ell$，且 $\Psi$ 为 Hecke-equivariant。
若另一个 map 有同样性质，其差 precompose 每个 $V_{n_i}$ 都为零，再 precompose $\sum_i A_iV_{n_i}=1$ 即知差为零。因此 (F52) 不依赖所选 unit-ideal expression。这是 source 上的真实 unsmoothing，未引用需要 $p\nmid N$ 的 SV Proposition 7.2.6。

为了明确其与裸 cup 的范围，[R1138](R1138-original-integral-bare-cup-smoothing-comparison.md) 已从实际单位除子与完整 cyclic norms 给出整模 $p$ 比较
$$
\Psi_n(c_{\chi,\psi}^{(2)},C_{\chi,\psi}^{(1)})
 =\frac4{m^2}\widetilde V_n\{F_\chi,F_\psi\}.
$$
则能严格推出的是
$$
\frac4{m^2}\{F_\chi,F_\psi\}
-\Psi(c_{\chi,\psi}^{(2)},C_{\chi,\psi}^{(1)})
\ \in\
\bigcap_{n>3,\ n\ne p}\ker\widetilde V_n
\quad\text{在原 target 的 }\theta\text{ 部分}.
\tag{F53}
$$
不能把 source 中的 $\sum_iA_iV_{n_i}=1$ 直接视为整个 $K_2/p$ target 的恒等式；也不能把 (F52) 中非零 compact cycle 的像说成零。

至此，§8.4 保留的两个 **smoothed source/operator** 门都已支付。在明确的 (F33) 范围内，(F52) 又支付了 source 上的唯一 unsmoothing。裸比较的实际单位常数现由 R1138 支付；target common kernel、指定 compact cycle 的值及真正四阶 cochains 仍分别处理。本节没有宣告指定不同角色的 cup 为零。

### 本次后继使用的原文与复核

- SV 作者全文 §§6.5、7.1，尤其 Theorem 6.5.4、Lemma 7.1.1、Proposition 7.1.3；(F38) 与 (F40) 给 full-level/Cartan 限制所需的两个额外论证。
- Thomas R. Shemanske、Lynne H. Walling，*Twists of Hilbert modular forms*，Trans. Amer. Math. Soc. 338 (1993), 375–403；作者全文
  <https://people.maths.bris.ac.uk/~malhw/twists.pdf>，Propositions 5.1–5.2、Theorem 7.1(2)（作者 PDF 第 14、25 页）。
- Luis Dieulefait、Ariel Pacetti、Panagiotis Tsaknias，*On the number of Galois orbits of newforms*，作者全文
  <https://sweet.ua.pt/apacetti/papers/OrbitsInvariants.pdf>，Theorem 4、Theorem 20 的 local-type/root-number 证明。这里的具体 normalizer 正号另由 §12.2 的 character average 自证。
- 原 full-level 表示及 same-spectrum 接口见 R1083 §1 的 Mercuri–Schoof 原来源；这里只消费其中对任意奇 $p$ 的有限表示证明，不搬用固定 $47$ 的数值或整格证书。

o2_high_coefficient 已独立核准 exact twist / away-from-$p$ order，以及 (F45)–(F48) 的真实 $\phi_*\psi^*$ 方向。以上无数学程序执行。

root 另亲读 SV Lemma 7.1.1、7.2.1 及 Shemanske–Walling Theorem 7.1(2)，并纸核两个 finite-type 的 Cartan fixed line 与反射平均；(F53) 现直接消费已发表 R1138，不再是假设裸比较。§8.4 的旧待付项目以本 §§11–13 的后继为准。
