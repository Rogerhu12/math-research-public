# R1067 — 原signed Kummer特化与有限幂检测

承接[同编号§§56–73](R1067-original-three-target-units-and-integral-isotropic-source.md)。本卷保§66起的原范围：p>211、p在K=Q(√−3)惰性、(17/p)=1，β=√17∈Zp×。仍研究同一固定E17、完整通常Sha及原canonical中央二阶；主目标尚未完成。

## 74. 同一 Robert 类在原 signed 反圆分线上的准确标量

在(AN1)的实际双变量单位上用 BKO 的 $T_\pi^{-1}$ 及反圆分
协不变量，记相应像为 $r^{\rm ac},d^{\rm ac}$。
用 R303 的相容原始 Betti 基、Tate 基和
$F_\theta:E_1\to E_{17}$，取(AO1)退回 $\Phi$ 的单位。
沿 R303(16)的 signed 变量（若经 BKO(3.1)的共轭，则两边同时
反演 $\gamma$）有
$$
 \boxed{r^{\rm ac}=72f(c^2-c)F_\theta^*\xi_{17},\qquad
 d^{\rm ac}=6fH^{\rm ac} F_\theta^*\xi_{17}
       =6fH^{\rm ac}\mathcal A_p(T)\xi_1.}                         \tag{AP1}
$$
其中 $H^{\rm ac}$ 是(AN5)的第一个整反圆单位，$c=103$；
$6f$ 亦为当前位单位。

取 $\pi=-p$ 相容的 $Q_j^\pi=(-1)^j\varpi/p^j$ 与
$T_{t,j}^\pi=[(-p)^{-j}]T_t$。两者同时改符号不改 Robert 偶函数。
在全 $t$ 和中 $\varepsilon(-p)=1$，所以按 Frobenius 平移驯点
不改其带标记和。在 $T_t$ 的剩余盘，$\Theta_c(T_t+z)$ 及其逆
均为好约化单位。逐项用其正规局部表达式、再取驯标记张量和，
给固定的 Coleman 对数表达式
$$
   \mathcal L(z)=\sum_t\varepsilon(t)
                         \log_p\Theta_{E_1,(c)}(T_t+z).
$$
不需对函数取非整数复幂。个别分量的无穷范数公式是 Rubin
Th. 7.6，在不同 $T$ 间相容；对 $\varepsilon$ 加权后因
$\varepsilon(\pi)=1$ 正好变成固定 $\pi$-范数。
等价地在有限未分歧 $L$ 分开各驯分量，使用算术 Frobenius
$\mathrm{Fr}(T)=[-p]T$ 的 Coleman 评价，再取驯和。
去除 Teich 常数不改每个对数导数。
在 $e_\tau$ 上，对导数的 $\Delta$ 投影准确为
$|\Delta|^{-1}\sum_{b\in\Delta}\mathcal L'([b]z)$，因为
$[b]$ 在不变导子上多 $b=\tau(b)$，与 $e_\tau$ 中的逆权相消。
这里 $\mathcal L'$ 始终表示相对于实际 $dz$ 的导数。

设 $\eta$ 为非平凡反圆有限 Galois 角色，其实际分歧导子
为 $(M)=(p^j)$、$j\ge2$，以 $w$ 记作用 $[w]$ 的值 $\eta(w)$。
不变dlog的原始规范亦可逐式见 Yan–Zhu [§1.2.1](https://arxiv.org/html/2401.09037v1#S1.SS2.SSS1)：δ_n=(f′/f)/λ′；仅采用该不变导数公式，其κ采用逆标记，本节群作用仍统一依BKO。BKO(2.1)的完整 Coates–Wiles 读者为 $\pi^{-j}$ 乘全
$A_j^\times$ 的 $\eta$ 权和。如其(2.3)–(2.9)，这也是
$\sum\eta(\sigma)\exp^*(z^\sigma)$ 在原不变微分下的系数。
在全 $w$ 和里前段的 $\Delta$ 平均不再留下额外分母；
$(-1)^j$ 的 $Q_j^\pi$ 由 $w$ 换元且 $\eta(-1)=1$。由
(AN2)得
$$
 \delta_\eta(r^{\rm ac})=\pi^{-j}
    \sum_{w,t}\eta(w)\varepsilon(t)
     \{-12cX(cP_{t,w})+12c^2X(P_{t,w})\}.
$$
$cT_t=T_t$，$\eta(c)=1$，故两项共同留下 $12(c^2-c)$。
$\eta(f)=1$：$f=34\delta$ 的实方向无反圆分量，纯虚
$\delta/\bar\delta=-1$ 也仅为 tame 单位。
$\varepsilon(p^j)=(-1)^j$；因此(AK3)的全导子分解现在给
$$
 \delta_\eta(r^{\rm ac})
      =\frac{72 f(c^2-c)}{\varpi}
                    L(\bar\psi_{17}\eta_{\rm ideal},1),\qquad
       \eta_{\rm ideal}((a))=\eta(a).                               \tag{AP2}
$$
特别 $M/(\pi^j\varepsilon(M))=1$。算术 Frobenius 理想标记如
Rubin Th. 7.4(ii)，况且从 CM Tate 标量 $a/\varepsilon(a)$ 到
反圆 pro-$p$ 商时 $\mu_6$ 消失。因此 BKO 的
$\eta_{\rm ideal}((a))=\eta(a)$；R716 的 idèle 写成 $p$ 处
为 $\eta(w)$ 时，其理想值则为 $\eta(a)^{-1}$。对理想取共轭
把 $L(\bar\psi_{17}\eta_{\rm ideal},1)$ 变成 R716 规范的
$L(\psi_{17}\widetilde\eta,1)$。同一事实也可直接由
$\bar\psi_{17}((a))/Na=\varepsilon(a)/a$ 看出，正是(AK3)使用
的完整格和。非平凡 $\eta$ 分歧于 $p$，所以 BKO 所去 $p,f$
因子在该 primitive $L$ 上不再增减。

平凡 $\eta$ 时可在 $j=1$ 非零 $p$ 挠上求和。
由(AL1)常数项
$\sum_{Q\in E_1[p]}X(T_t+Q)=pX(pT_t)$，去掉 $Q=0$ 后取驯投影
得 $(-p-1)\sum_t\varepsilon(t)X(T_t)=0$。
该最后的零由(AK3)的 $M=1$ 格和及 R298(9)的 $s_0=0$ 给出，
参考 $c$ 的置换仍准确相同。BKO 平凡有限角色也取零，去掉
Euler 因子不改变此零。

BKO Prop. 3.1(3.3)对标准 $\xi_{17}$ 正给
$L_{pf}(\bar\psi_{17}\eta_{\rm ideal},1)\omega_{17}/\varpi_{17}$。
选用 R303 的原 CM 生成 Betti 基；$F_\theta^*\omega_{17}
=\theta^{-1}\omega_1$，$\varpi_{17}=\varpi/\theta$，故在
$\omega_1$ 下比较标量恰为(AP2)的 $72f(c^2-c)$。
因此(AP1)首式之差的 $\delta_\eta$ 在所有有限角色为零；
BKO §2.1.2(2.2)、Th. 2.1 的两个 signed 直和子模交为零，
故差本身为零。不借助任何个别中央 $L$ 非零。
由(AN4)–(AN5)再乘 $-H^{\rm ac}/(12(c-c^2))$ 得(AP1)第二式。
这里从实际空间导数和全角色识别，不需要将 R303 所用的另一
辅助惰性素数平滑系数改为本节的 $c$。
[BKO 原期刊 §2.1–2.2 与 Prop. 3.1](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/padic-lfunctions-and-rational-points-on-cm-elliptic-curves-at-inert-primes/7F847A218FE1F6DBB390CC0279089C34)

因 $\xi_1$ 为该原 signed 整直因子的基，(AP1)尤其给
$$
 d^{\rm ac}\in T^2V_\infty^*,\qquad
 [T^2]\mathcal A_p=0\quad\Longleftrightarrow\quad
                 d^{\rm ac}\in T^3 V_\infty^*.
                                                                    \tag{AP3}
$$
R303(6)又使右端在坏中央时自动加强为 $T^4$。这是真正原
signed 类的整除，而不是(AO1)的有限 Kummer 对数非零断言。

## 75. 原 $[T^2]\mathcal A_p$ 在每个整精度的有限 Kummer 幂充要测试

令 $k\ge1$、$j=k+1$，沿用(AO1)下降到 $\Phi_j$ 的实际
$d_j\in e_\tau(U^1(\Phi_j)\otimes\mathcal O)$。
$A_j^\times=(\mathcal O/p^j)^\times$，依原反圆生成元写
$[a]_{\rm ac}=\gamma^{s(a)}$，$s(a)\in\mathbf Z_p$。
对模 $p^j$ 的 $a$ 取任一 $\mathcal O^\times$ 提升，
下式的系数均读在 $\mathcal O/p^k$：
$$
 Y_k=\sum_{a\in A_j^\times}
           a^{-1}\binom{-s(a)}{2}\,[a]d_j\quad\in
  (\Phi_j^\times/(\Phi_j^\times)^{p^k})
                           \otimes_{\mathbf Z/p^k}(\mathcal O/p^k).
$$
加法记号表示单位的乘法 Kummer 群及外部系数张量。
$1+p^j\mathcal O$ 的反圆指数属于 $p^{j-1}\mathbf Z_p$，
因规范的 $\log q_{\rm ac}$ 赋值为一；二可逆，故 $Y_k$ 与
各提升无关。它读取(AN1)的真实 $D_{p^{-j}t}$ 与全驯系数，
或可用(AN4)的整 Robert 单位重建。精确地，
$$
 \boxed{\quad Y_k=0\quad\Longleftrightarrow\quad
              [T^2]\mathcal A_p(T)\in p^k\mathcal O.\quad}          \tag{AQ1}
$$
$Y_k$ 非零对这个 $p$ 即已强迫通常全 $\Sha[p^\infty]$ 有限。
它不是特征零单位对数的非零测试。

证明。记 $T'=T_\pi^{-1}(1)$、$R=(\mathcal O/p^k)[X]/(X^3)$。
对 $T'_R=T'\otimes R$ 另以 $g\mapsto(1+X)^{-s(g)}$ 给
Iwasawa–Shapiro 的逆群作用。在系数环中因此 $\gamma$ 的
模变量仍为 $1+X$；若同时采用相反群环约定，应作
$1+X\mapsto(1+X)^{-1}$，其在 $X^2/(X^3)$ 恒等。
因 $(1+X)^{p^k}=1$，此系数分解通过第 $k$ 反圆有限层。
有自然同构
$$
 V_\infty^*/(p^k,T^3)\simeq H^1(\Phi,T'_R).                      \tag{AQ2}
$$
具体，BKO §2.2(2.7)、Lemma 2.2(1) 给有限群环
$\mathcal O[\Gamma/\Gamma^{p^k}]$ 的准确控制而非仅有有限核余核。
先模 $p^k$ 再用 Shapiro，得到同一有限群环模 $p^k$ 上的
$H^1$；模 $p^k$ 的满射使用 $H^2(\Psi_k,T')=0$，由局部对偶
及对偶 Tate 格的剩余非平凡 $\Delta$ 型可见。
再商到 $R$ 不需假定 $R$ 平坦：对有限群环模 $p^k$ 的每个
有限子商 $W$，$\Delta$ 对 $W$ 平凡，对 $T'/p$ 的型是
$\tau^{-1}\tau^{p+1}=\tau^p$，对其 Tate 对偶的型是 $\tau$。
故 $H^0(\Phi,T'\otimes W)=H^2(\Phi,T'\otimes W)=0$。
这里可按 $p$ 及反圆增广理想的有限过滤逐层论证。长正合列使
$W\mapsto H^1(\Phi,T'\otimes W)$ 精确；对 $R$ 取有限自由
表示即与 $H^1$ 的标量变换交换，得(AQ2)。

$\Phi_j$ 包含 $E_1[p^j]$ 与 $\mu_{p^j}$，故 $T'_R$ 在该域
平凡。限制
$$
 H^1(\Phi,T'_R)\longrightarrow H^1(\Phi_j,T'_R)
$$
为单射：膨胀限制的核是 $H^1(A_j^\times,T'_R)$，
而 $A_j^\times=\Delta\times G_j$，$|\Delta|$ 与 $p$ 互素，
$T'_R$ 的 $\Delta$ 不变量为零，Hochschild–Serre 使这个群为零。
现在用 BKO(2.3)–(2.4)记录的**有限模 Tate 扭转**：第 $j$ 层
的 Kummer $d_j$ 张量所选 $Q_j^\pi$ 对应的对偶基及 $1\in R$，
由 corestriction 产生(AQ2)下的有限类。此处可直接从 Shapiro
映射看出这一步：先到 $\mathcal O/p^k[\Gamma/\Gamma^{p^k}]$
的指标列，把该层的相容单位推成基类，再将 $[a]$ 送到
$(1+X)^{s(a)}$。也即从给定层作 norm，此后每层追加
$1+p^j\mathcal O$ 时 $a^{-1}$ 与 $s(a)$ 在 $R$ 内均平凡，
所以相容性确保同一个类。若在 $\Delta$ 下降上取不变量的
归一迹而非直接 corestriction，两种得到的类只差
$|\Delta|=p^2-1$；下述检测及每个整精度完全相同。

限制回 $\Phi_j$ 后，Mackey 的 $\operatorname{res}\operatorname{cor}$
是完整陪集和。在此域上 Kummer 同构及所选对偶基把所得元素
写成（上述可逆 $\Delta$ 归一除外）
$$
  \sum_{a\in A_j^\times}a^{-1}(1+X)^{-s(a)}[a]d_j.               \tag{AQ3}
$$
$a^{-1}$ 是**完整** Tate 作用而非其 $\tau(a)^{-1}$ 部分。
Kummer 映射与 $a$ 交换，故 cyclotomic Tate $(1)$ 已在真实
单位的 Galois 置换中；不可再乘一次 $Na$。每个 $[a]d_j$
作用在外部 $\mathcal O/p^k$ 张量以前的域单位上。
式(AQ3)的二次系数恰是 $Y_k$。

(AP1)与 R303(6)给 $d^{\rm ac}\in T^2 V_\infty^*$，所以(AQ3)
的常数与一次项在真实模 $p^k$ Kummer 群中均为零。
其二次项为零当且仅当整个(AQ3)为零；限制单射及(AQ2)
又使之当且仅当 $d^{\rm ac}$ 在 $V_\infty^*/(p^k,T^3)$ 为零。
$V_\infty^{*,+}=\Lambda\xi_1$ 是完整整模的直接因子，
$6f H^{\rm ac}$ 可逆，故最后条件由(AP1)正是(AQ1)。
特别若取相反符号，$\binom{s(a)}2-\binom{-s(a)}2=-s(a)$，
其差是上述已经为零的一次项。

对任一选定的 lifts，把(AQ3)系数提升为 $p$ 进数并在所选
域嵌入先取普通 $p$ 对数，(AO1)可证明许多此类线性组合非零；
(AQ1)要求的是有限 Kummer 类，须证明它没有落入 $p^k$ 次幂。
即使非零域对数也可能达到该整除。(AQ1)尚未对无穷多个
不同 $p$ 排除所有 $Y_k$ 同时为零。

## 76. 首整精度退到实际循环同源邻曲线上的一阶挠点

沿 §74 之素数范围与同一 Tate 基。置 $q=p^2$、$b=q-1$、
$k=\mathcal O/p$。在 $\Phi_2/\Phi_1$ 的 Galois 群
$(1+p\mathcal O)/(1+p^2\mathcal O)$ 中取 $g_+=1+p$，
$g_-=1+ph$，其中 $\bar h=-h\bmod p$ 且 $s(g_-)=1\bmod p$。
这是可作的，因为反圆生成元在 $1+p$ 阶为本原。
$X=g_+-1,\ Z=g_--1,\ N_+=\sum_{i=0}^{p-1}g_+^i$。
置 $F=\Phi_2^{\langle g_+\rangle}$，$y=N_{\Phi_2/F}r_2$，
按(AN1)保留 $e_\tau$、所有实际驯扭标记及 $c=103$。
则首整精度的准确零测试为
$$
 [T^2]\mathcal A_p=0\bmod p\quad\Longleftrightarrow\quad
 Z^{p-3}y=0\quad\text{在 }e_\tau(F^\times/F^{\times p})\otimes k .
 \tag{AR1}
$$
此处与下文的 $e_\tau$ 应施在带外部 $k$ 的张量上。
实际上在模 $p$ 的野群环内，
$$
 N_+=X^{p-1},\qquad
 \sum_{i=0}^{p-1}\binom{-i}2g_-^i=g_-Z^{p-3}.
$$
第二式由 $\sum x^i=(x-1)^{p-1}$ 施 $x^2\partial_x^2/2+
x\partial_x$ 即得。模 $p$ 的 Tate 标量仅余 $\tau^{-1}$，
故(AQ3)对 $r_2$ 的二次项正是 $|\Delta|g_-Z^{p-3}N_+r_2$。
(AP1)与同一整直接因子给出它的零测试；或用(AN4)两可逆算子
将 $d_2$ 换为 $r_2$。从 $F$ 限制到 $\Phi_2$ 时该
$e_\tau$ Kummer 群无核：膨胀限制的可能核是
$H^1(\langle g_+\rangle,\mu_p)$，其 $\Delta$ 型为
$\tau^{p+1}$，因为群是阿贝尔且 $\mu_p$ 的型为范数。
此外 $|\Delta|$ 可逆，$g_-$ 为单位，证(AR1)。

以下给 $y$ 的几何输入。先用(AN1)的 $+p$ 标记，以
$C=\langle Q_1\rangle_{\mathbf F_p}\subset E_1[p]$、
$q_C:E_1\longrightarrow E_C=E_1/C$ 表示对应的循环 $p$ 同源。
在当前第 $2$ 层两套 $\pm p$ 标记一致。令
$W=q_C Q_2,\ V=q_C([h]Q_1)$，则 $W,V$ 是 $E_C[p]$ 的
$\mathbf F_p$ 基：$pQ_2=Q_1$，且若 $iW+jV=0$，先乘 $p$
在源曲线得到 $iQ_1=0$，再由 $h\bmod p\notin\mathbf F_p$
得 $j=0$。$g_-$ 固定 $C,E_C,V$ 并送 $W$ 到 $W+V$。
有完整带标记公式
$$
 y=e_\tau\sum_t\varepsilon(t)\,
       \Theta_{E_C,(c)}\big(q_CT_{t,2}+W\big)                     \tag{AR2}
$$
（加法 Kummer 记号）。确实 $g_+^iQ_2=Q_2+[i]Q_1$；
$P\mapsto\prod_{S\in C}\Theta_{E_1,(c)}(P+S)$ 的除子等于
$q_C^*\operatorname{div}(\Theta_{E_C,(c)})$。这是因为
$q_C$ 在 $E_1[c]$ 上同构到 $E_C[c]$，而 $c$ 与 $p$ 互素。
可以直接用(AN2)对 $E_C$ 任一 Weierstrass 模型定义此
$\Theta$；比较差一个与 $P$ 无关的常数，对 $\sum_t\varepsilon(t)$
为零。因平移中的 $T_{t,2}$ 均在固定未分歧扩域中，
(AO1)的整下降适用。式中 $e_\tau$ 的每个 $\Delta$ 共轭连
$C,q_C,W,V$ 一起移动，保全 $p+1$ 个方向及其相位。
因此 $Z^{p-3}$ 作用在(AR2)的各条 $W+\mathbf F_pV$ 上。
每项已为该循环邻曲线的真正 $p$ 挠点加上原驯点。

## 77. 实际邻点单位的八个剩余单位商

置 $e=pb=v_F(p)$，$U_m=1+\mathfrak m_F^m$。在与原
$\pi=-p$ Tate 基相应的 Lubin–Tate 坐标中，可以选
$[\pi](v)=\pi v+v^q$、$[a](v)=av$ 对 $a\in\Delta$。
唯一具有导数一的严格同构把原椭圆形式参数送到此参数
（原参数取 $dz/dt(0)=1$）。以 $v_i$ 记相应原 Tate 基点坐标，
即 $[\pi]v_2=v_1$。取 $t=N_{\Phi_2/F}v_2$；
这是 $F$ 的素元，$[a]t=a^p t$ 对 $a\in\Delta$ 准确成立。

$F/\Phi_1$ 的唯一下分歧断点为 $b$。事实上，在
$\Phi_2/\Phi_1$ 每个非平凡 $[1+ph]$ 均使
$v_{\Phi_2}([1+ph]v_2-v_2)=q$，因形式群加上本原
$\pi$ 挠点后，差是该挠点乘一个单位，而
$v_{\Phi_2}(v_1)=q$。对 $\Phi_2/\Phi_1$ 及其子群
$\Phi_2/F$ 作 different 求和，指数分别为 $(p^2-1)q$
与 $(p-1)q$。由 different 的塔公式，
$d_{F/\Phi_1}=(p-1)q$；循环 $p$ 扩张只有一个断点，
故其值恰为 $q-1$。从而 $Z(U_m)\subset U_{m+b}$
对 $m\ge1$ 成立：令 $g_-t=t(1+O(t^b))$，各未分歧
系数固定，逐项相减即可。

对 $i>pe/(p-1)$，$U_i\subset(F^\times)^p$。
此由 $\log,\exp$ 在深度 $>e/(p-1)$ 互逆并先除以 $p$ 得到。
而 $i<pe/(p-1)$、$p\mid i$ 时，$U_i$ 在
Kummer 商的 $i$ 次分次为零：对任一首系数从完美剩余域中
取 $p$ 次根，再在 $U_{i/p}$ 提起；其 $p$ 次幂的所有
二项式中间项均有严格较大赋值。
因此(AR1)只需 $y$ 到 $i\le pe/(p-1)-(p-3)b=4b+p+1$。
$U_i/U_{i+1}\simeq k$ 上 $\Delta$ 型是 $a^{pi}$；
外部张量 $k\otimes_{\mathbf F_p}k$ 的两个嵌入给
$a^{pi},a^i$。于是 $e_\tau$ 只容许 $i\equiv p,1\bmod b$，
且每个容许的 $i$ 至多一条 $k$ 线。最高的 $4b+p+1$
没有这两种型。去掉能来自 $p$ 次幂的分次，实际只余
$$
 \boxed{\quad 1,\ 1+2b,\ 1+3b,\ 1+4b;\qquad
                  p+b,\ p+2b,\ p+3b,\ p+4b.\quad}                \tag{AS1}
$$
$F$ 的赋值分次及剩余域乘法部分在 $e_\tau$ 内皆为零。
这些是 $y$ 的 Kummer 输入的分次上界，求(AR1)时仍需保留
$Z^{p-3}$ 在相继分次之间的实际提升。

## 78. 用原秩零单位固定首读数，三项邻点对数微分给出原二阶系数模 $p$

置 $f_1=2\delta$；在(AN1)的 $r_j$ 中把 $f,\varepsilon$
换为 $f_1,\varepsilon_1$，仍用同一 $E_1,c,\varpi,\pi$，
得 $r_j^0$。则按(AP1)的同一规范
$$
 (r^0)^{\rm ac}=72f_1(c^2-c)\xi_1 .
$$
对非平凡反圆角色的证明逐式为(AP2)，其中 $f_1$ 的反圆
投影仍平凡。对平凡角色，完整 $j=1$ 和是
$\pi^{-1}(-p-1)=1+1/p$ 乘在 $Q=0$ 的驯导数，此因子
正是去 $(p)$ 的 Euler 因子，因为 $N(p)=p^2$ 且
$\bar\psi_1((p))=-p$。R302(5)在实际 $\varpi$ 下给
$L(E_1,1)/\varpi=(1-\omega)/6$。
再以所有有限角色与 signed 直和唯一性即得断言。

在 $F$ 的模 $p$ Kummer 张量中，(AR1)可加强为元素等式
$$
 Z^{p-3}y=17\, a_2\, r_1^0,\qquad
                   a_2=[T^2]\mathcal A_p\bmod p.                 \tag{AT1}
$$
这里 $r_1^0$ 从 $\Phi_1$ 限制入 $F$。
在(AQ3)对 $r$ 展开的二次项是
$|\Delta|g_-Z^{p-3}y$。另一方面 $r^{\rm ac}=
(f/f_1)\mathcal A_p(r^0)^{\rm ac}$，前两阶为零，而
$(r^0)^{\rm ac}$ 的常数项是同一(AQ3)中的
$|\Delta|N_{\Phi_2/\Phi_1}r_2^0=|\Delta|r_1^0$。
两边的 $\Delta$ 正规化及 Tate 基完全相同。
利用 $f/f_1=17$、$g_-r_1^0=r_1^0$，再用(AR1)中的限制单射
即得(AT1)。

把 $\Omega^1_{\mathcal O_F/\mathcal O}/p$ 中的系数张量
$k\otimes_{\mathbf F_p}k$ 以当前选定的乘法嵌入读入 $k$。
以 $t$ 为 §77 的素元，$v_1=P(t)$ 为 $F$ 中的整幂基表示，
$d_0=(p-1)q$。则
$$
 v_F(P'(t))=d_0,\qquad
 \rho=\overline{t^{-d_0}P'(t)}\,
                  72f_1(c^2-c)\,(1-\omega)/6\in k^\times.
$$
确实 $\mathcal O_F=\mathcal O[t]$，
$\Omega^1_{\mathcal O_F/\mathcal O}$ 由 $dt$ 生成，
长度为绝对 different 指数
$d_{F/\Phi}=d_0+p(b-1)$。商去 $dv_1=P'(t)dt$
给 $\Omega^1_{\mathcal O_F/\mathcal O_{\Phi_1}}$，
长度恰 $d_0<d_{F/\Phi}$，故得所示准确阶。
又 $d_0<e<d_{F/\Phi}$，因此原绝对微分模 $p$ 在 $t$ 坐标
正是 $k[t]dt/(t^e)$，$d_0$ 次首项可读。
$r_1^0$ 对 $v_1$ 微分的常数项为
$72f_1(c^2-c)L(E_1,1)/\varpi\bmod p$：沿(AP2)在 $z=0$
求驯全和，用 $[\pi]^{-1}T_t$ 的置换不改带标记和，
因为 $\varepsilon_1(-p)=1$。$\Delta$ 平均在常数导数上
权与导数的 $a$ 作用准确相消，且严格 LT 参数导数为一。
所有更高项乘 $P'(t)$ 后在 $t^{d_0+1}$ 内。
$d\log$ 在模 $p$ 后杀所有 $p$ 次幂，故(AT1)给
$$
 17\rho\, a_2=[t^{d_0}]\,
       (g_-^*-1)^{p-3}\big(d\log y\big)/dt\quad\text{于 }k.       \tag{AT2}
$$

右侧只需 $(d\log y)/dt$ 的实际三项系数
$$
 L_i=[t^{p+ib-1}](d\log y)/dt,\qquad i=0,1,2.                   \tag{AT3}
$$
因为 $[a]t=a^pt$、$e_\tau$ 及所选乘法嵌入共同强迫
非零的 $[t^{m-1}]$ 有 $pm\equiv1\bmod b$，即
$m\equiv p\bmod b$。$g_-t=t(1+\lambda t^b+O(t^{2b}))$
模 $p$，其中 $\lambda\in k^\times$ 由恰好一个断点保证，
而 $\Delta$ 交换性保证其余指数也为 $1\bmod b$。
每次 $(g_-^*-1)$ 至少将微分的 $t$ 次数提高 $b$。
$d_0+1-(p-3)b=p+2b$，故只余(AT3)。
更明确，令 $L(t)=\sum_{i=0}^2 L_i t^{p+ib-1}dt$，
将(AT2)的输入换为 $L(t)$ 即为准确等式。
末格 $L_2$ 的乘子是
$$
 \lambda^{p-3}\prod_{j=1}^{p-3}(p+(2+j)b)
                 =-\lambda^{p-3}/2\quad\text{于 }k^\times,         \tag{AT4}
$$
因为 $t^{m-1}dt$ 的一次最低增阶项为
$(m+b)\lambda t^{m+b-1}dt$，而 $b=-1\bmod p$。
前两格的乘子也由同一 $g_-$ 的实际置换决定，不能由(AT4)
丢掉。用(AR2)代入(AT2)所得是原三格的组合；
右端非零仍是原 $a_2\ne0\bmod p$ 的充分且必要条件。

## 79. 原中央消去前两格，实际邻点的一个对数微分系数给整二阶模 $p$

沿(AT2)–(AT4)，有
$$
 L_0=L_1=0,\qquad
 \boxed{\quad [T^2]\mathcal A_p\bmod p=
           -\frac{\lambda^{p-3}}{34\rho}\,
       [t^{p+2b-1}](d\log y)/dt .\quad}                           \tag{AU1}
$$
为证第一项，从 $\Phi_2$ 的原单位 $r_2$ 开始。
以 $x=v_2$ 为素元，$\Delta$ 作用是 $x\mapsto ax$。
在 $U_1/U_2$ 的两外部嵌入上，$e_\tau$ 只保乘法嵌入。
在此嵌入的首系数就是 $\sum_t\varepsilon(t)$ 加权的
$\Theta_{E_1,(c)}(T_{t,2}+x)$ 的不变对数导数于零的值。
由(AP2)的驯和计算与 $\varepsilon(-p)=1$，此值为
$72 f(c^2-c)L(E_{17},1)/\varpi=0$。因此 $r_2$ 属于
$(U_2(\Phi_2)\otimes\mathcal O)$ 的像。
而 $N_{\Phi_2/F}U_2(\Phi_2)\subset U_2(F)$：
在模 $x^{p+1}$ 的商环内，每个 $g_+^i$ 都恒等，
因为其断点是 $q-1$；$u\in U_2$ 的所有共轭之积等于
$u^p=1\bmod x^{p+1}$，而 $v_{\Phi_2}(t)=p$。
故原 $y$ 也由 $U_2(F)$ 的张量表示。
对任一实际 $u\in U_2(F)$，在模 $p$ 的 $t$ 展开中
$[t^{p-1}](d\log u)/dt=([t^0](d\log u)/dt)^p=0$。
这一 Cartier 恒等式也可直接由 Euler 乘积验证：
在 $k[[t]]$ 写 $u=\prod_{n\ge1}(1-a_nt^n)$，
则 $[t^{m-1}](d\log u)/dt=-\sum_{n\mid m}n a_n^{m/n}$。
仅使用模 $t^{p+1}$，因而任一单位提升均给同一值。
外部张量逐项线性求和，得 $L_0=0$。

原 $\mathcal A_p\in T^2\Lambda$ 还给(AQ3)真正的一次项为零。
而 $\sum_{i=0}^{p-1}(-i)g_-^i=g_-Z^{p-2}$ 模 $p$，
故由(AR1)的限制单射，$Z^{p-2}y=0$ 在 $F$ 的
模 $p$ Kummer 张量内。施同一 $d\log$ 后取 $[t^{d_0}]$。
因 $d_0+1-(p-2)b=p+b$，只余 $L_0,L_1$；
$L_0$ 已零，故所得零为
$\lambda^{p-2}\prod_{j=1}^{p-2}(p+(1+j)b)\,L_1$。
乘积的各因子模 $p$ 依次为 $-2,\ldots,-(p-1)$，
皆非零。得 $L_1=0$，再由(AT2)–(AT4)即得(AU1)。
因 $\Delta$ 型，$\omega_y=d\log y$ 在此嵌入首次可能非零
之阶已升到 $p+2b-1$；这个单格非零正等价于原首整证书。

## 80. 规范分歧常数与原曲线 Coleman 全微分的有限方向迹

置 $x=v_2,\ \sigma=g_+,\ t=\prod_{i=0}^{p-1}\sigma^ix$，仍取
$[\pi]x=\pi x+x^q,\pi=-p$。用严格参数将 $E_1$ 形式群送
到此 LT 群，写 $P(x)$ 为相应的椭圆形式点。令
$$
 B(x)\,dx=e_\tau\sum_t\varepsilon(t)\,d\log
                \Theta_{E_1,(c)}(T_{t,2}+P(x))\pmod p
           =\sum_{j\ge0} B_j x^{jb}\,dx.                          \tag{AV1}
$$
右端用所选剩余域乘法嵌入；式中作为驯指标的 $t$ 与素元 $t$
各按其上下文。$\varepsilon(-p)=1$，故 $T_{t,2}$ 可以在全和
里换为 $T_t$。这给单一固定代数 Robert 微分在当前 LT
参数的驯 Galois 全和与 $\Delta$ 准确投影。令
$R=72 f_1(c^2-c)(1-\omega)/6\in k^\times$，则
$$
 \lambda=h-h^p,\quad \rho=R,\qquad
 34R\,a_2=(h-h^p)^{p-3}\,[x^{3pb}](\sigma-1)^{p-1}B(x).         \tag{AV2}
$$
这里 $\sigma$ 对函数作用为代入 $[1+p]x$。

证明。令 $\ell$ 为规范 LT 对数，则 $\ell'(0)=1$ 且
$\ell'(x)=\ell'(\pi x+x^q)(1+(q/\pi)x^{q-1})$；$\ell'$ 是整
不变微分的系数，故 $\ell'(x)=1\bmod p$。任意 $a\in\mathcal O$
因而满足 $([a]x)'=a\bmod p$。并且
$\sigma x=x-x^q+O(x^{q+1})$，由 $[p]x=-x^q\bmod p$ 及形式加法
可见。更一般 $[1+ph]x=x-hx^q+O(x^{q+1})$。
在本节各需用的阶数内，$x$ 的有限层导数与形式求导可交换：
$d_{\Phi_2/\Phi}=q b+q(b-1)>e_2=v_{\Phi_2}(p)=qb$，
所以 $\Omega^1_{\mathcal O_{\Phi_2}/\mathcal O}/p=
k[x]dx/(x^{e_2})$。下文各取项指数均 $< e_2$。

因 $\sigma^i$ 的导数均为一，有
$t'/t=\sum_i(\sigma^i x)^{-1}=(\sigma-1)^{p-1}x^{-1}$。
一次最低增阶将 $x^m$ 送至 $-m x^{m+b}$，所以右端首项为
$-x^{-1+(p-1)b}$（用 $(p-1)!=-1\bmod p$）。
$t$ 的首项是 $x^p$，从而 $t'=-x^{d_0}+\cdots$。
$\Delta$ 强迫 $t$ 只有指数 $p+jb$，而 $1\le j<p$ 时
$p+jb\not\equiv0\bmod p$。逐项积分到此阶给
$$
 t=x^p-x^{p+(p-1)b}+O(x^{p+pb}).
$$
$g_-$ 代入右边，$x^p$ 的首差系数为 $-h^p$，第二项的首
差系数为 $h$，误差的差阶严格更高。因 $t^q$ 的首项为
$x^{pq}$，故 $\lambda=h-h^p$。另一方向 $v_1=[\pi]x=x^q\bmod p$。
以 $t$ 展开 $v_1$，由 $\Delta$、准确 different 及
$t^p$ 的首项为 $x^q$，必为
$v_1=t^p+\eta t^{p+(p-1)b}+\text{更高项}$。
取 $x^{q+p(p-1)b}$ 系数即得 $\eta=1$。这个指标仍小于
$e_2=qb$，因为 $pb>q$，所以得 $\overline{t^{-d_0}P'(t)}=1$，
从而 $\rho=R$。

原 $y=N_+r_2$ 的微分拉回 $\Phi_2$ 是
$\sum_iB(\sigma^ix)dx=(\sigma-1)^{p-1}B(x)dx$。
(AU1)中两个低格均已为零，故此处首个可能的项是
$L_2 t^{p+2b-1}(dt/dx)=-L_2 x^{3pb}+\cdots$。
将此系数代入(AU1)得(AV2)。
