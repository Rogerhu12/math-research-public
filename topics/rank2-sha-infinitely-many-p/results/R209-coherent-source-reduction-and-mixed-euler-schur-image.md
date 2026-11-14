# R209 — 原源的相容二阶降阶、混合 Euler 耦合与完整 Schur 像

日期：2026-11-12。状态：本文各局部恒等式、整同构与有限像损失上界均已证明。它们把大素数标量问题压到一个更小的实际余矩阵；尚未给出有方向的严格全素数收益，原课题仍未完成。

本文使用 [R199](R199-exact-first-band-exponential-and-complete-divided-image.md) 的准确第一带公式、[R203](R203-finite-central-companion-and-rational-row-lattices.md) 的实际中央比较，以及 [R206](R206-fourth-layer-interior-schur-and-true-deleted-column-quotient.md) 的完整输出参数变换与图函数精度。以下源始终是原多项式，不把各齐次块分别放进前缀核。

## 1. 原对象与实际选行

设
$$
 p=4r-1\ge19,\qquad r>2D,\qquad O=\mathbf Z_p,
 \qquad R=r(p-1),\qquad a=17\tau_p\in O^\times.
$$
固定
$$
 E_D=O[A,C]_{\le D},\quad C=B-A,\quad
 e_{m,c}=A^{m-c}C^c\quad(0\le c\le m\le D),
 \qquad \ell=m+c,
 \tag{1}
$$
并置 $M_d=\binom{d+2}{2}$（$d\ge0$），$M_d=0$（$d<0$）。第一带内
$$
 A(w)=e^{aw^r/p}f(w),\quad C(w)=e^{aw^r/p}c(w),\quad
 f=w+\cdots,\quad c=v_0w^2+\cdots,\quad v_0=-22\in O^\times.
$$
对完整连续前缀 $n<k=rq+s$，$0\le s<r$、$q\le p-2$，记
$$
 J_n(P)=p^{\lfloor n/r\rfloor}[w^n]P(A(w),C(w)),
 \qquad \mathcal E=A\partial_A+C\partial_C.
$$
R199 的准确公式给出
$$
 \overline J_{rh+l}(e_{m,c})
 =\frac{a^hm^h}{h!}[y^l]\overline f^{\,m-c}\overline c^{\,c},
 \qquad 0\le l<r.
 \tag{2}
$$
它在 $l<\ell$ 时为零，在 $l=\ell$ 时是
$a^hm^hv_0^c/h!$。这里以及下文模 $p$ 的公式省略 $a,v_0$ 上的横线；$0^0=1$。

固定角阶 $\ell$ 的次数节点为
$$
 m_-(\ell)=\lceil\ell/2\rceil,\quad
 m_+(\ell)=\min(\ell,D),\quad
 q_\ell=m_+(\ell)-m_-(\ell)+1.
$$
对 $1\le j\le\lfloor D/2\rfloor+1$ 置
$$
 t_\ell=\min(j,q_\ell),\qquad
 \mathcal S_{D,j}=\{rh+\ell:0\le\ell\le2D,\ 0\le h<t_\ell\}.
 \tag{3}
$$
这是一组原 $J$ 的真实行；因 $2D<r$，各行号互不相同。其个数及最大行号是
$$
 \kappa_{D,j}=M_D-M_{D-2j},\qquad
 b_{D,j}=r(j-1)+2D-2j+2.
 \tag{4}
$$
计数可由下节两个原单项式核的任一个直接得到。对最大行号，$h=j-1$ 能出现当且仅当 $q_\ell\ge j$，其最大 $\ell$ 为 $2D-2j+2$；因 $r>2D$，任何较小 $h$ 都给较小行号。

## 2. 两个实际源降阶算子

以下两个算子均满射到同一个原次数空间 $E_{D-2j}$：
$$
 \begin{split}
 T^+_{D,j}&=\partial_C^j\prod_{i=0}^{j-1}(\mathcal E-D+i),\\
 T^-_{D,j}&=\partial_A^{2j}.
 \end{split}
 \tag{5}
$$
约定先作用右边的 Euler 多项式。若 $D-2j<0$，目标为零空间。

**定理 2.1。** 对 $\varepsilon\in\{+,-\}$，$T^\varepsilon_{D,j}$ 是整分裂满射。其核 $K^\varepsilon_{D,j}$ 是原单项式直和。选行映射
$$
 \Pi J:K^\varepsilon_{D,j}\longrightarrow O^{\kappa_{D,j}},
 \qquad \Pi=(J_n)_{n\in\mathcal S_{D,j}},
 \tag{6}
$$
是整同构。因此当 $k>b_{D,j}$ 时，
$$
 E_D\overset\sim\longrightarrow
 E_{D-2j}\oplus O^{\kappa_{D,j}},\qquad
 P\longmapsto(T^\varepsilon_{D,j}P,\Pi JP)
 \tag{7}
$$
是整同构，只使用这个完整前缀内已经出现的真实行。

**证明。** 在原单项式上，
$$
 \begin{split}
 T^+_{D,j}e_{m,c}
 &=(c)_{\underline j}(m-D)^{\overline j}
                      A^{m-c}C^{c-j},\\
 T^-_{D,j}e_{m,c}
 &=(m-c)_{\underline{2j}}A^{m-c-2j}C^c.
 \end{split}
 \tag{8}
$$
第一系数非零当且仅当 $c\ge j$ 且 $m\le D-j$；第二系数非零当且仅当 $m-c\ge2j$。每个非零整数因子绝对值不超过 $D<p$，所以全部为 $O$ 单位。非零列分别与目标 $E_{D-2j}$ 的原单项式一一对应，证明满射并给出齐次的整单项式截面 $\Sigma^\varepsilon$。

固定 $\ell=m+c$。$K^+_{D,j}$ 的节点准确为最高的 $t_\ell$ 个 $m$，因为核条件等价于
$m>\min(\ell,D)-j$。$K^-_{D,j}$ 的节点准确为最低的 $t_\ell$ 个 $m$，因为其条件是 $2m-\ell<2j$。将行与核列都按 $\ell$ 排列，(2) 使矩阵模 $p$ 为块下三角。每个对角块由 $h=0,\ldots,t_\ell-1$ 与上述连续 $m$ 节点组成，条目是
$$
 \frac{a^h}{h!}\,m^h\,v_0^{\ell-m}.
$$
行列单位之外是 Vandermonde 矩阵。节点差均为绝对值小于 $p$ 的非零整数，故行列式是单位。这证明 (6)，并与分裂满射一起证明 (7)。$\square$

两个算子满足不同但准确的 Euler 协变式：
$$
 T^\varepsilon_{D,j}\binom{\mathcal E}{h}
 =\binom{\mathcal E+\sigma_\varepsilon}{h}T^\varepsilon_{D,j},
 \qquad \sigma_+=j,\quad \sigma_-=2j.
 \tag{9}
$$
这里目标上的 $\mathcal E$ 是 $E_{D-2j}$ 的原总次数算子。第一算子还可写成逐次复合
$$
 T^+_{D,j}=
 [\partial_C(\mathcal E-(D-2j+2))]\cdots
 [\partial_C(\mathcal E-(D-2))]
 [\partial_C(\mathcal E-D)].
 \tag{10}
$$
故它确实逐次降低两次原总次数，而不是在目标中改名得到的形式次数。

若 $k=rq+s$ 且 $1\le q\le\lfloor D/2\rfloor$，可直接取 $j=q$：由 $r>2D$，有 $b_{D,q}<rq\le k$。于是已经完整观察的 $q$ 个径向块，允许把未知源减少到 $M_{D-2q}$ 列。取 $j=\lfloor D/2\rfloor+1$ 则余源为零，终止行准确为
$$
 b_{D,j}=r\lfloor D/2\rfloor+2\lceil D/2\rceil,
$$
与既有 R191 界相符。

## 3. 完整余矩阵与真实前缀值理想

固定 (5) 中任一个算子，简写 $T,K,\kappa,\Sigma,\sigma$。令 $J^\circ$ 为一个同样满足 (2) 的实际比较矩阵；例如 R203 中删中央项的比较轴。选行 (6) 在 $J^\circ$ 上也可逆。定义
$$
 U=(\Pi J^\circ|_K)^{-1}:O^\kappa\longrightarrow K,
 \quad F=\Pi J^\circ\Sigma,
 \quad \mathcal R=\Sigma-UF.
 \tag{11}
$$
于是
$$
 T\mathcal R=1,\qquad \Pi J^\circ\mathcal R=0,
 \qquad P=U(\Pi J^\circ P)+\mathcal R(TP).
 \tag{12}
$$
这些源映射只由固定的短选行确定，随着 $k>b_{D,j}$ 增长保持不变。令
$$
 B=J^\circ_{<k}U,\quad Q_0=I-B\Pi,\quad
 S^\circ=Q_0J^\circ_{<k}\mathcal R=J^\circ_{<k}\mathcal R.
 \tag{13}
$$
$\Pi B=I$，$Q_0$ 投影到 $\ker\Pi$。删去恒零的选行后，把这个目标视为 $O^{k-\kappa}$，就得到准确的整等价
$$
 J^\circ_{<k}\sim_O I_\kappa\oplus S^\circ.
 \tag{14}
$$
特别，$S^\circ$ 是原多项式 $\mathcal R(E_{D-2j})$ 的真实剩余行。这里没有把它认作 $J^\circ$ 在次数 $D-2j$ 原源上的矩阵。

这也保持未来的严格前缀值理想。对 $n\ge k$，用同一源映射，将第 $n$ 行减去它在 $U$ 上的值乘以已经出现的选行，得到 $J^\circ_n\mathcal R$。这是整行操作；在前 $k$ 行准确为零的源上，所减项本来就是零。因此前缀核内的第 $n$ 行取值集合准确等于相应余矩阵的取值集合。有限精度前缀也有相同的整同构。

尤其，对 $P\in\{J^\circ_{<k}P\in p^NO^k\}$，
$$
 P\in p^NE_D\quad\Longleftrightarrow\quad TP\in p^NE_{D-2j}.
 \tag{15}
$$
因为 (12) 的第一坐标已经属于 $p^NO^\kappa$。这是一条原源整性检测结论，不是对独立齐次 summand 的假定。

## 4. 扰动的完整 Schur 公式与全精度损失界

在同一个真实目标参数下写
$$
 J=J^\circ+\Delta,\qquad \Delta\in p^t\operatorname{Mat}(O),
 \quad t\ge1.
$$
保持 (11) 的全部源映射不变，置
$$
 A_*=\Pi\Delta U,\quad C_*=\Pi\Delta\mathcal R,
 \quad D_*=Q_0\Delta U,\quad E_*=Q_0\Delta\mathcal R.
$$
由于 $I+A_*$ 为整单位矩阵，原 $J$ 的完整余矩阵准确为
$$
 \boxed{\quad
 S=S^\circ+E_*-D_*(I+A_*)^{-1}C_*.
 \quad}
 \tag{16}
$$
**证明。** 用 (12) 的源坐标和 (13) 的目标消元，原矩阵成为
$$
 \begin{pmatrix}I+A_*&C_*\\D_*&S^\circ+E_*\end{pmatrix}.
$$
整消元给 (16)。等价地，新的固定源截面是
$\mathcal R-U(I+A_*)^{-1}C_*$，它的 $T$ 值仍为恒等，且原 $J$ 的选行准确为零。故这个消元同样适用于以后每一个完整前缀和未来值理想。$\square$

式 (16) 中的最后一项不能略去。它从 $p^{2t}$ 起，在更高精度会影响实际像，而不是一个可以免费的源旋转。

记非零 Smith 指数为 $s_i$，并定义
$$
 \mathcal L_N(H)=\sum_i(N-s_i(H))_+
 =\operatorname{length}_O\big((H(O^d)+p^NO^e)/p^NO^e\big).
$$
则所有 $N\ge1$ 准确满足
$$
 \begin{split}
 \mathcal L_N(J)&=N\kappa+\mathcal L_N(S),\\
 \mathcal L_N(J^\circ)&=N\kappa+\mathcal L_N(S^\circ).
 \end{split}
 \tag{17}
$$
又由 $S-S^\circ\in p^t\operatorname{Mat}(O)$，两者小于 $t$ 的 Smith 指数完全相同，所以
$$
 \boxed{\quad
 |\mathcal L_N(J)-\mathcal L_N(J^\circ)|
 \le (N-t)_+M_{D-2j}.
 \quad}
 \tag{18}
$$
证明上界时，先把共同的模 $p^t$ 像消去；每个剩余列在精度 $N$ 最多再贡献 $N-t$ 个长度单位。若已知其中更少的 Smith 指数至少为 $t$，可用那个数替换 $M_{D-2j}$。

R203 的中央比较在原 $w$ 参数下满足 $\Delta\in p^2\operatorname{Mat}(O)$，所以可以取 $t=2$。由首中央项属于 $pO^2$、后续中央项整，原轴差的 ramified 加权赋值至少为 $2r$；共同指数及原多项式 Taylor 展开给出的每个项均保持这个界。故 (18) 在任意所需精度为
$$
 |\mathcal L_N(J)-\mathcal L_N(J^\circ)|
 \le (N-2)_+M_{D-2j}.
 \tag{19}
$$
这条界付清了全部未消去的列数及高精度尾；它是双向损失上界，没有提供收益的符号。对全素数求和时仍必须保留右端，不能将它视作已取得的严格斜率改善。

## 5. 图函数间唯一的共同径向换参

在 R206 的输出参数中写
$$
 \Phi(z)=C(A^{-1}(z)),\qquad
 \Phi^\circ(z)=C^\circ((A^\circ)^{-1}(z)),\qquad
 \delta=\Phi-\Phi^\circ.
$$
在所需第一带截断内，R206 已证明
$$
 \operatorname{ord}\delta\ge r,\quad
 \Phi(\pi z)/\pi^2,\ \Phi^\circ(\pi z)/\pi^2\in O_\pi[[z]],\quad
 \delta(\pi z)\in\pi^{2r}O_\pi[[z]],\qquad \pi^r=p.
 \tag{20}
$$
令
$$
 V=\Phi/z,\quad V^\circ=\Phi^\circ/z,\quad
 \psi=(V^\circ)^{-1}\circ V,\quad \tau=\psi^{-1},\quad
 \eta(z)=\tau(z)/z-1.
 \tag{21}
$$
两个 $V$ 的线性系数均为单位 $v_0$，所以形式逆存在。对原 $m$ 次齐次多项式 $P_m$，准确有
$$
 P_m(z,\Phi(z))
 =\left(\frac z{\psi(z)}\right)^m
       P_m(\psi(z),\Phi^\circ(\psi(z))).
 \tag{22}
$$
因为 $V^\circ(\psi(z))=V(z)$，两个坐标对相差同一倍数 $z/\psi(z)$。复合一次共同的 $\tau$，即得
$$
 P(\tau(z),\Phi(\tau(z)))
 =\sum_{h=0}^D\eta(z)^h
       \left(\binom{\mathcal E}{h}P\right)(z,\Phi^\circ(z)).
 \tag{23}
$$
这里 $\binom{\mathcal E}{h}$ 在次数 $m$ 上准确乘 $\binom mh$，所以是原整源上的算子。

**精度核查。** 用 $\nu_\pi(H)=\min_d(rv_p(H_d)+d)$ 表示 $H(\pi z)$ 的系数最小 $\pi$ 赋值。由 (20)，两个整参数 $V(\pi z)/\pi$ 与 $V^\circ(\pi z)/\pi$ 之差在 $\pi^{2r-2}$ 中。单位线性项的整形式取逆保持这一精度。因此
$$
 \operatorname{ord}(\psi-z),\operatorname{ord}(\tau-z)\ge r-1,
 \qquad \operatorname{ord}\eta\ge r-2,
 \qquad \nu_\pi(\eta)\ge2r-2.
 \tag{24}
$$
若 $M_H$ 是在行归一 $p^{\lfloor n/r\rfloor}$ 下乘以 $H$ 的目标矩阵，则
$$
 \nu_\pi(H)\ge\lambda
 \quad\Longrightarrow\quad
 M_H\in p^{\lfloor\lambda/r\rfloor}\operatorname{Mat}(O).
 \tag{25}
$$
事实上条目为 $p^{\lfloor n/r\rfloor-\lfloor m/r\rfloor}H_{n-m}$；把 $n-m=ur+v$、$0\le v<r$ 代入加权界，并用原系数赋值为整数，即得 (25)。

由 $2h\le2D<r$，(24)–(25) 给出
$$
 M_{\eta^h}\in p^{2h-1}\operatorname{Mat}(O),\qquad
 (M_{\eta^h})_{n,m}=0\quad(n-m<(r-2)h),\qquad1\le h\le D.
 \tag{26}
$$
共同复合 $\tau$ 的归一目标矩阵也是整下三角、对角为一，且模 $p$ 为单位矩阵：展开 $\tau^i=z^i(1+\eta)^i$，各非恒等项由 (24)–(25) 属于 $pO$。因此该共同变换保持全部真实有限像和严格前缀值理想。

本节只在 $k=rq+s$、$q\le p-2$ 的前缀内使用；此时 $n<k\le R-1$，构造 $V,\psi,\eta$ 所需至多额外两个图系数均仍位于 (20) 的第一带内，没有偷读带外 carry。

式 (23) 给完整的 Euler 展开，但混合次数的不同倍数确实存在。不能给各 $P_m$ 分别采用不同目标变换，然后宣称整个 $E_D$ 的标量像格保持。事实上固定 $m$ 的原齐次块在行 $m,m+1,\ldots,2m<r$ 已经是三角单位阵，其所有非零 Smith 指数本来就是零；困难只在不同 $m$ 的像相加后的关系格。

## 6. 所有 Euler 耦合由一个真实短前缀矩阵决定

仍用 §3 的 $T,U,\Sigma,F,\mathcal R$。取
$$
 B_h=\binom{\mathcal E}{h},\quad
 C_h=\binom{\mathcal E+\sigma}{h}\big|_{E_{D-2j}},\quad
 G_h=\Pi J^\circ B_hU.
 \tag{27}
$$
$K$ 是原单项式直和，故在所有 $B_h$ 下不变，且
$B_hU=UG_h$。齐次截面 $\Sigma$ 满足 $B_h\Sigma=\Sigma C_h$。
于是准确有
$$
 \boxed{\quad
 B_h\mathcal R=\mathcal R C_h+U A_h,\qquad
 A_h=F C_h-G_hF=\Pi J^\circ B_h\mathcal R.
 \quad}
 \tag{28}
$$
这不仅给出 Euler 协变，还把全部非协变部分明确写在已知原核里。所有 $A_h$ 使用同一个 $F=\Pi J^\circ\Sigma$；它们只依赖已观测选行和原源上的次数算子，没有引进独立可选的导数坐标。

若为了计算采用 §5 的共同图坐标，则先把 $J^\circ$ 的选行泛函从原 $w$ 目标通过 R206 的整单位目标变换运输过去。它们仍是已经出现的前缀行的整组合，(11)–(19)、(27)–(28) 不变。于是把 (23) 的非恒等部分记为 $\Delta_{\rm rad}$，完整地有
$$
 \begin{split}
 \Delta_{\rm rad}\mathcal R
 &=\sum_{h=1}^D M_{\eta^h}
     \{S^\circ C_h+B(F C_h-G_hF)\},\\
 \Delta_{\rm rad}U
 &=\sum_{h=1}^D M_{\eta^h}B G_h.
 \end{split}
 \tag{29}
$$
将这两个实际矩阵代入 (16)，就得到共同径向换参后的完整标量余矩阵。在精度 $p^N$ 下，(26) 只要求保留
$h\le\min(D,\lfloor N/2\rfloor)$；$(I+A_*)^{-1}$ 也只需其有限几何级数。这是任意有限精度的准确计算，不遗漏高阶 Schur 交叉项。

这里 $\Delta_{\rm rad}$ 一般只在 $p\operatorname{Mat}(O)$ 中。§4 对原共同参数的 $p^2$ 结论，不应套到已经额外复合 $\tau$ 的差上。共同目标变换保持有限像，故 (19) 仍可在原参数中使用。

## 7. 短前缀耦合的真实边界支撑

在原 $w$ 行坐标中，把 $A_h$ 的选行标为 $(b,\ell)$，其中 $0\le b<t_\ell$。由 (2)，对任何原 $Q$ 和 $u\ge0$，
$$
 \overline J_{rb+\ell}(\mathcal E^u Q)
 =\frac{(b+u)!}{b!\,a^{u}}\,
       \overline J_{r(b+u)+\ell}(Q),
 \tag{30}
$$
只在右边的真实行已经处于所需第一带时使用；分母中的 $a^u$ 是 §1 的单位参数 $a=17\tau_p$ 的幂。

将 $B_h$ 展开为次数至多 $h$ 的 Euler 多项式，并用 $\Pi J^\circ\mathcal R=0$，得到
$$
 \overline A_h(b,\ell)=0\qquad\text{若 }b+h<t_\ell.
 \tag{31}
$$
因此第 $h$ 个耦合模 $p$ 只可能出现在每个角块最高的
$\min(h,t_\ell)$ 个已选行。对 $h\le j$，可能非零的行数为
$$
 \sum_{\ell=0}^{2D}\min(h,q_\ell)=M_D-M_{D-2h}.
 \tag{32}
$$
特别 $A_1\bmod p$ 至多使用 $2D+1$ 行；并且所有更高 $A_h$ 已由 (28) 的同一个 $F$ 决定。

式 (31) 只是一条经过原真实选行证明的模 $p$ 支撑结论。更高 $p$ 位包含 R199 的角向移位尾，必须继续用 (16)、(28)–(29) 保留；不能把 (31) 逐位重复，或把它升级为免费读取的完整导数束。

## 8. 已获得的范围与未完成的实际问题

本篇给出了两个原源上的相容二阶降阶，并明确了它们的真实观察截止。对每个 $k>b_{D,j}$，全部有限像长度、严格前缀值理想和源整性，都可以在固定的 $M_{D-2j}$ 列余矩阵上准确计算。中央比较的所有高精度尾满足 (19) 的明确损失界。共同径向换参后，全部混合 Euler 耦合由一个已观察短前缀矩阵 $F$ 编码，完整余矩阵由 (16)、(29) 给出。

未证明的仍是：实际中央零条件会使这些真实余矩阵的像，产生足够且同方向的收益，从而支付全素数预算。矩阵 $F$ 的存在、边界行数减少、以及各固定齐次块的整等价，都不能单独给出这个符号。后续可以直接研究 (16) 的真实余矩阵，或者用 $T^-_{D,1}=\partial_A^2$ 的核基
$\{C^b:0\le b\le D\}\cup\{AC^b:0\le b\le D-1\}$
将它表示为两个实际形式级数的连续余项；无论哪种表示，都要保留 (28) 中的耦合项及 (16) 的交叉项。
