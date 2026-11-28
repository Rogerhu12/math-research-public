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

## 81. 四个原标记 Taylor 系数给出整个模 $p$ 方向迹

沿(AV1)。原固定有理微分的全系数满足
$$
 B_0=B_1=0,\quad B_{p+1}=B_2,\qquad
 [x^{3pb}](\sigma-1)^{p-1}B
            =-B_{2p+1}+2B_{p+2}-B_3-2B_2 .                       \tag{AW1}
$$
因此右端经(AV2)的明示单位正好读取原 $a_2$。这里 $\Delta$
投影对所列指数仅保留原系数，不另混合相邻 Taylor 阶。

置 $Y=x^b,\ \sigma_i=[1+pi]$，$i\in\mathbf F_p$。
其整数提升、及以 $\sigma^i$ 代替，在此窗口已相同：
标量模 $p^2$ 的差始于 $x^{q^2}$，因为 $[p^2]x=x^{q^2}\bmod p$。
由 $\sigma_i'=1$ 及 $\Delta$ 等权，$\sigma_i x/x$ 除常数以外
只允许 $Y^{1+mp}$。准确到所需深度为
$$
 \sigma_i x/x=1-iY-iY^{p+1}
             +(Di-i^2/2)Y^{2p+1}+O(Y^{3p+1}),\qquad D\in k.      \tag{AW2}
$$
为证中间系数，写 LT 加法律为 $\mathcal F(X,Z)$。
其 $\Delta$ 权要求单项总次数为 $1\bmod b$；由不变微分模
$p$ 为 $dx$，模 $p$ 的非线性单项在两个变量上的次数都为 $p$
的倍数。最低可能总次数为 $q$，再下一种至少 $1+(p+1)b$。
总次数 $q$ 的部分为
$-((X+Z)^q-X^q-Z^q)/(\pi-\pi^q)$，由 $\ell$ 的首个高阶
系数 $1/(\pi-\pi^q)$ 得到。代 $Z=[pi]x=-ix^q+O(x^{q^2})$，
对 $Y^{p+1}$ 仅 $X^{q-p}Z^p$ 有贡献，其分母消去后的
系数是 $\binom{p^2}{p}/p=1\bmod p$。
故得 $-iY^{p+1}$。写 $D_i$ 表示下一格，
$\sigma_i\sigma_j=\sigma_{i+j}$ 给 $D_{i+j}=D_i+D_j-ij$：
除两个 $D$ 项，只有先前的 $-i x^{1+(p+1)b}$ 在
代入 $\sigma_jx$ 时产生 $-ij$；这是因为
$(1+(p+1)b)/p=-1\bmod p$。由此得(AW2)。

$B_0=0$ 为(AU1)用过的实际驯导数。对(AV1)的每个单位
在 $k[[x]]$ 应用两次(AU1)的 Euler 乘积系数等式，
外部权与 $\Delta$ 权均在 $\mathbf F_q$，得
$B_1=B_0^q=0$。现可用 $\sum_i i^K=-1$ 当
$K>0,\ (p-1)\mid K$，其余为零（包括 $K=0$），逐项收取
$\sum_iB(\sigma_ix)$ 的 $Y^{3p}$ 系数：
$$
\begin{array}{c|c|c}
 \text{从(AW2)用到的高阶项}&\text{余下可能的原指标 }j&
      \text{相应全幂和贡献}\\ \hline
 \text{仅用 }-iY &2p+1,\ p+2,\ 3&
         -B_{2p+1}+2B_{p+2}-B_3\\
 \text{恰一次 }-iY^{p+1} &p+1,\ 2&
          B_{p+1}-2B_2\\
 \text{恰一次 }-i^2Y^{2p+1}/2 &2&-B_2
\end{array}
$$
例如首行需 $K=3p-j$ 是 $p-1$ 的正倍数。
Lucas 公式给 $\binom{jb}{K}=1,-2,1$（依表列顺序），
再乘 $-1$。第二行需 $K=2p-j$，因选 $K$ 个非恒项的
一个作替换，二项式系数再乘 $K$；在两格分别给 $1,-2$
的最终贡献。第三行在 $j=2$ 时共选 $K=p-2$ 个非恒项，
$i$ 总次为 $p-1$，得
$\binom{2b}{p-2}(p-2)/2=-1\bmod p$，其中已计幂和与符号。
两次 $-iY^{p+1}$ 或一次 $DiY^{2p+1}$ 的唯一可能
指标 $j=1$ 已因 $B_1=0$ 消去。其余阶数或幂和皆不贡献。

同一运算于 $Y^{2p}$：仅通常项 $j=p+1,2$ 给
$-B_{p+1}+B_2$，另有的 $j=1$ 项为零。由(AU1)和(AV2)证明中
的准确最低阶，整个迹在 $x^{3pb}$ 前各项皆零，故得
$B_{p+1}=B_2$。代回三行之和即给(AW1)。

## 82. 原四格余数在固定 $E_1$ 特殊纤维上为全驯挠点的一个 Frobenius 图像和

本节 $\mathrm F$ 为 $E_1:y^2=x^3+1$ 特殊纤维上的 $p$ 次
幂 Frobenius，$\omega=dx/(2y)$，$f=34\delta,\ f_1=2\delta$。
对每个 $a\in\Delta,\ i\in\mathbf F_p$，任取
$d_{a,i}\in\mathcal O_K$ 满足
$d_{a,i}\equiv a(1+pi)\bmod p^2$ 且 $d_{a,i}\equiv1\bmod f$。
可由 CRT 任取非零提升。置
$$
 W(P)=-\frac{y(P)}{x(P)}
       \left(\frac{y(\mathrm F^3 P)}{y(\mathrm F P)}-1\right).
$$
则(AV2)等价于全代数点的等式
$$
 \boxed{\quad
 34 f_1(1-\omega_K)\,a_2=
 -\frac{(h-h^p)^{p-3}}{b}
  \sum_{a,i,t} a^{-1}\varepsilon(t)
   \sum_{R\in E_1[d_{a,i}]} W(-T_t+R)
            \quad\text{于 }k.\quad}                               \tag{AX1}
$$
$\omega_K=(-1+\delta)/2$ 以免和微分混淆，标记 $T_t$ 均指同一
primitive $f$ 挠点的好约化，$a^{-1}$ 指剩余域标量。
所有点 $-T_t+R$ 保有原 $17$ 部分，故 $x(P)$ 与
$y(\mathrm F P)$ 都不为零。不存在因选模型或点而漏掉的极点项。

具体地，在固定特征零曲线上取有理微分
$$
 \nu=\sum_t\varepsilon(t)
       \frac{y(P)-y(T_t)}{x(P)-x(T_t)}\,\omega .
$$
$\zeta$ 加法式给它等于 $\sum_t\varepsilon(t)X(P+T_t)\omega$：
$\sum_t\varepsilon(t)=0$，而 $\sum_t\varepsilon(t)X(T_t)=0$
由实际 $L(E_{17},1)=0$。$\nu$ 只有 $-T_t$ 处的单极，
留数为 $\varepsilon(t)$。$\Theta_c$ 的固定标记全微分准确
等于 $12(c^2-[c]^*)\nu$，由(AN2)与 $cT_t=T_t$ 得到。
这些函数在当前好约化处定义良好，所有不同 $T_t$ 保持不同。
在 $E_1/\overline k$ 上组成有理微分
$$
 \Omega_p=b^{-1}\sum_{a,i}a^{-1}[d_{a,i}]^*\nu .
$$
在 $O$ 的原 LT 参数 $s$ 中，至 $s^{3pb}ds$ 为止，这给出
完整的 $\Delta$ 投影及 $g_+$ 方向迹：两 CM 标量模 $p^2$
相合同其形式端同态的差为 $O(s^{q^2})$，且相应导数均为该
标量模 $p$；此窗口严格小于 $q^2-1$。$12(c^2-[c]^*)\Omega_p$
在该窗口即(AV2)的实际 $\sum_iB(\sigma^is)ds$。
$\Omega_p$ 在窗口内因 $\Delta$ 只容许 $s^{m-1}ds,\ 
m\equiv1\bmod b$。若其首非零项在这样的 $m$，
$12(c^2-[c]^*)$ 在该项乘 $12(c^2-c^m)=12(c^2-c)$，是单位；
所以整个 $\Omega_p$ 在 $s^{3pb}$ 前的系数均为零，且
$$
 34 f_1(1-\omega_K)a_2
    =(h-h^p)^{p-3}[s^{3pb}](\Omega_p/ds)
$$
由 $R=12 f_1(c^2-c)(1-\omega_K)$ 及(AV2)给出。
因所有更低项均零，此系数对任一同向切线的严格参数相同。

在特殊纤维上有恒等有理函数
$W=-(y/x)(y^{p(q-1)}-1)$。它仅 $O$ 为极点：
$x=0$ 时 $y^2=1$，而 $y^{p(q-1)}-1$ 可被 $x^3$ 整除。
在 $u=-x/y$ 处首项是 $u^{-3pb-1}$，
且 $\omega/du(0)=1$。因此
$\operatorname{Res}_O(W\Omega_p)=[s^{3pb}](\Omega_p/ds)$。
每个 $[d_{a,i}]$ 均可分、étale，
$[d_{a,i}]^{-1}(-T_t)=-T_t+E_1[d_{a,i}]$；
其各点处留数是 $a^{-1}\varepsilon(t)/b$，
重合点按有理微分的加法计全部重数。
对 $W\Omega_p$ 用完备曲线全局留数定理即得(AX1)。
此式同时证明右侧与各 CRT 提升无关；它的跨素数非零
仍需控制这个完整加权点和。

## 83. 原筐内的全局三维 Hecke 特征空间及其前三个不变导数

在 $E_1/k$ 上记 $s$ 为(AV1)的严格 LT 参数，$D$ 为对实际 $\omega$ 的对偶导子；模 $p$ 有 $\omega=ds$，故 $D=d/ds$。对 $n>1$ 奇，以 $L_n$ 表示唯一奇有理函数，仅 $O$ 可有极，主部准确为 $s^{-n}$。主部的唯一剩余障碍是与 $k\omega$ 的留数配对：$s^{-n}\omega$ 的留数为零，由 Serre 对偶可实现该主部；取奇部保主部且除去常数。定义
$$ M_j=(j+1)pb+1,\qquad W_j=L_{M_j},\qquad j=0,1,2.$$

对奇、有唯一可能极点 $O$、极阶不超过 $3pb+1$ 的函数 $W$，置
$$ \mathcal H(W)=b^{-1}\sum_{a,i}a^{-1}[d_{a,i}]_*W.$$
推前是可分同源的函数域迹。$O$ 附近只有零逆分支贡献主部，其余分支正则，所以主部正是将 $W$ 的主部代入 $[d_{a,i}]^{-1}(s)$，不乘同源度。相同模 $p^2$ 的 CM 标量逆代入相差 $O(s^{q^2})$，在此界内保全部主部；差函数全局正则且奇，故为零。因此 $\mathcal H(W)$ 与 CRT 提升无关，且对任一 $d\bmod p^2=a(1+pi)$ 有 $[d]_*\mathcal H(W)=a\mathcal H(W)$，由乘法重排整组陪集得出。记 $U_j=\mathcal H(W_j)$。

在 $\Delta$ 挑出的极阶 $n\equiv1\bmod b$ 上，$g_+$ 逆代入为 $s+s^q+\cdots$，正规迹 $(g_+^{-1}-1)^{p-1}$ 将极阶至少降低 $(p-1)b$。对 $n=M_j$，$p-1$ 次首系数依次为 $-1,-2,\ldots,-(p-1)\bmod p$，乘积 $-1$，故 $U_j$ 首项为 $-s^{-((jp+1)b+1)}$。

反之在极阶不超过 $(2p+1)b+1$ 的全部此类奇函数中，若 $[d]_*U=aU$ 对这些 $d$ 成立，$\Delta$ 迫最高极阶 $n\equiv1\bmod b$。若 $n>b$ 且 $p\nmid n$，$g_+$ 逆代入之差仍有 $n-b$ 次极点，矛盾；$n\le b$ 只容 $n=1$，而椭圆曲线上不存在仅一单极的函数。因此最高极阶只可能为 $q,(p+1)b+1,(2p+1)b+1$。逐级消首项给出整个空间恰为三维，基为 $U_0,U_1,U_2$。

由(AX1)的同一留数配对及 $\Omega_p$ 在原点的首个可能 $3pb$ 格，实际泛函
$$ \ell_{17}(U)=\sum_t\varepsilon(t)U(-T_t)$$
在 $U_0,U_1$ 恒为零，在 $U_2$ 上按(AX1)的准确非零单位读取 $a_2$。若用(AX1)的 $W$ 或 $-yx^{(j+1)pb/2-1}$ 替换 $W_j$，同首项及上述全空间分类表明其像只添更低基。因此 $a_2=0$ 等价于 $\ell_{17}$ 在整个三维空间为零，并非等价于此空间为零。

### 准确主部与原不变导数

以留数配对将 $\mathcal H$ 转置到微分 $s^{lb}ds$，局部变量代换给
$$ [s^{-(lb+1)}]U_j
 =[s^{(j+1)pb}]\sum_i(\sigma_i s)^{lb}.$$
每个 $\sigma_i'=1$，$\Delta$ 权在这些次数相消。这正是(AW2)的逐列系数，此处不能删去 $B_1$ 列。$Y^p$ 窗只有普通项的 $l=1,K=p-1$，给 $-1$。$Y^{2p}$ 窗的普通项 $l=p+1,2$ 给 $-1,+1$，恰一次高项的 $l=1,K=p-1$ 给 $+1$。$Y^{3p}$ 窗按(AW2)的三类贡献，两个高项或 $Di$ 项仅落 $l=1$。因而
$$\begin{aligned}
 U_0={}&-L_q,\\
 U_1={}&-L_{(p+1)b+1}+L_{2b+1}+L_q,\\
 U_2={}&-L_{(2p+1)b+1}+2L_{(p+2)b+1}-L_{3b+1}\\
       &+L_{(p+1)b+1}-3L_{2b+1}+\kappa L_q,\qquad \kappa\in k.
\end{aligned}$$
没有 $l=0$：常数微分被全 $p$ 迹杀，亦无仅一单极的函数。

令 $G=L_p$。$G^p=L_q$ 由主部及奇性得到。$DG$ 全局正则故为常数 $c_p$，且 $c_p\ne0$，否则 $G$ 为 $p$ 次幂，其 $p$ 根仅有一阶极点，矛盾。准确有
$$ \boxed{U_0=-G^p,\qquad DU_1=x^q,\qquad D^2U_2=2y^q.}\tag{AY1}$$
第二式的主部中，仅 $2b+1=2q-1$ 不是 $p$ 倍，一导只余 $s^{-2q}$。$x^q$ 也恰有这个主部：$x=s^{-2}+O(s^4)$；正则差常数由 $\mu_6$ 的非平凡权杀去。第三式只有 $3b+1=3q-2$ 不是 $0$ 或 $-1\bmod p$，二导只余 $-2s^{-3q}$；$y=-s^{-3}+O(s^3)$，二导保奇，故与 $2y^q$ 的正则差为零。因此 $DU_0=D^2U_1=D^3U_2=0$，后两基均不是 $p$ 次幂。

置 $g=G/c_p$。由 $k(E)=k(E)^p(g)$、$Dg=1$，可唯一写为
$$ U_1=x^qg+A^p,\qquad U_2=y^qg^2+B^pg+C^p.\tag{AY2}$$
这里 $A,B,C$ 为唯一相应有理函数，极阶分别是 $q+p-1,\ q+2p-1,\ 2q+p-2$，$A,C$ 奇而 $B$ 偶。各阶数从上列真实主部及(AY1)逐项读取：$A^p$ 和 $C^p$ 各承原最高极；$DU_2-2y^qg=B^p$ 的最高极来自 $2L_{(p+2)b+1}$ 的一导。尚须判定这些真实函数在原 $\varepsilon$ 全驯和中的值，空间与导数非零都不能替代该泛函非零。

## 84. 整个原驯挠点上的固定代数 zeta 值与有限 CM 等变窗

沿(AY1)取 $G=L_p$，$DG=c_p\ne0$。在 $E_1\times E_1$ 的函数域有
$$ G(P+Q)-G(P)-G(Q)=
 \left(\frac{y(P)-y(Q)}{x(P)-x(Q)}\right)^p.\tag{AZ1}$$
先在几何泛点 $Q$ 的完美系数闭包上就 $P$ 比较。左对 $P$ 的不变导数为零，其 $p$ 根仅在 $P=-Q,O$ 各有简单极点，主系数分别为 $+1,-1$；右侧斜率函数同样。由 $G(P)=s^{-p}+O(s)$ 在 $P=O$ 比较，两者常数项皆为零，故相等并自动下降。尺度始终是原 $y=\wp'/2$。

对非零 $\alpha\in\mathcal O_K$ 素于 $2p$，取除函数 $\psi_\alpha$ 满足
$\operatorname{div}\psi_\alpha=[\alpha]^*[O]-N\alpha[O]$。奇阶核各点之和为 $O$ 保证存在；常数归一不影响对数导数。有
$$\begin{aligned}
 G([\alpha]P)-\alpha G(P)&=K_\alpha(P)^p,\\
 K_\alpha&=\alpha^{-1}D\log\psi_\alpha
          =X(\alpha P)-\bar\alpha X(P).
\end{aligned}\tag{AZ2}$$
最后一式在特征零先解释，整体为可约化有理函数，由 zeta 准周期或各极部及奇性得出。在特征 $p$，左边导数零；其 $p$ 根在非零 $E[\alpha]$ 各点的首系数为 $\alpha^{-1}$，在 $O$ 为 $\alpha^{-1}-\bar\alpha$，因为 $\alpha^{1/p}=\bar\alpha$ 于 $\mathbf F_q$。$K_\alpha$ 有相同极部，两边的 $p$ 根皆奇，故无多余常数。

特别取 $c=103\equiv1\bmod f$，在每一个原始驯点上
$$ \boxed{G(T_t)=X(T_t)^p,\qquad
 X(T_t)=K_c(T_t)/(1-c).}\tag{AZ3}$$
$X(T_t)$ 是原特征零固定代数值的好约化，$p>211$ 保全分母。(AZ3)也解释 $G^p$ 在原驯泛函的零：$\varepsilon(-p)=1$ 且 $\sum_t\varepsilon(t)X(T_t)=0$。原角色方向一直是 $\psi_{17}((a))=a/\varepsilon(a)$、$\varepsilon(u)=u$。

写 $g=G/c_p=s+H(s)^p$，令 $a_0=c_p^{-1/p}$。$\mu_6$ 权及 $Dg=1$ 给
$g=a_0^p s^{-p}+s+O(s^{5p})$；$H$ 主部为 $a_0s^{-1}$、权为 $\zeta^{-1}$。置 $V=DH+a_0x$，它在 $O$ 正则。将(AZ2)用 $g=s+H^p$ 展开、取 $p$ 根后求导，得
$$ \alpha V([\alpha]s)-\bar\alpha V(s)
       =-D([\alpha]s-\alpha s)^{1/p}.\tag{AZ4}$$
这里 $DK_\alpha=-\alpha x([\alpha]s)+\bar\alpha x(s)$，且 $([\alpha]s)'=\alpha$ 于特征 $p$。

对各 $a\in\Delta$ 以 CRT 取 $\alpha$ 素于二且 $\alpha\equiv a\bmod p^2$。有 $[\alpha]s=as+O(s^{q^2})$，故(AZ4)右端阶至少 $q^2/p-1$；在严格小于此指标的窗，$V$ 只容次数 $p-1\bmod b$。任何形式导数的 $s^{p-1}$ 项皆零，所以
$$ DH=-a_0x+C_p s^{p-1}+O(s^{b+p-1}),\qquad
 C_p=a_0[s^{p-1}]x\ne0.\tag{AZ5}$$
规范 LT 对数在 $s^q$ 前等于 $s$，该 $x$ 系数即[R301 (12)–(13)](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)的原 $X_{(p+1)/6}$，已证模 $p$ 为单位。

用 $\mu_6$ 的非平凡权固定下式偶函数的常数，则
$$ L_{p-1}=\frac{G^2-x^p}{2c_p},\qquad
 L_{p-2}=\frac{G^3-3x^pG-2y^p}{3c_p^2}.\tag{AZ6}$$
这里 $L_{p-1}$ 以所示权及唯一主部定义，$L_{p-2}$ 如§83。由
$G=s^{-p}+c_ps+O(s^{5p})$、$x=s^{-2}+O(s^4)$、$y=-s^{-3}+O(s^3)$，两右端各有准确的单一负幂主部。(AZ3)、(AZ6)在每个原固定 $T_t$ 上只用 $X(T_t),x(T_t),y(T_t)$ 的 Frobenius 像及 $c_p$；仍未算尽(AY2)中 $B^pg+C^p$ 的全驯贡献。

## 85. 原固定曲线的精确 Cartier 校正及第二次 Frobenius 退根

沿(AZ4)。全局微分 $Gx\omega$ 仅 $O$ 可有极点，其留数为零。由(AZ6)的首窗，只有 $G$ 的 $s^{-p},c_ps$ 两项可贡献，故
$$ [s^{p-1}]x+c_p=0.$$
[R301 (12)–(13)](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)的原有理系数给 $c_p\in\mathbf F_p^\times$，所以 $a_0=c_p^{-1}$。实际上整个 $k((s))$ 中有
$$ \boxed{DH=-x/c_p-s^{p-1}.}\tag{BA1}$$

为证此式，严格 LT 的整不变微分满足
$$ \ell'(s)=(1-p s^b)\ell'(-ps+s^q).$$
常数为一，模 $p^2$ 迭代得
$$ \ell'(s)=1-pE(s)\pmod{p^2},\qquad
 E(s)=\sum_{j\ge0}s^{q^jb}.$$
每一固定次数仅有限项。记 $f_\alpha(s)=[\alpha]s$，由
$\ell'(f_\alpha)f_\alpha'=\alpha\ell'(s)$ 得
$$ (f_\alpha'-\alpha)/p
       =\alpha\bigl(E(f_\alpha)-E(s)\bigr)\pmod p.$$
两边乘 $ds$ 后施 Cartier。左边在 $s^{pn-1}$ 的系数为
$n[s^{pn}](f_\alpha-\alpha s)$，所以其 Cartier 正是
$d((f_\alpha-\alpha s)^{1/p})$，其中先模 $p$ 约化再取根。右边第一项为 $f_\alpha^*(E(s)ds)$，而
$$ C(E(s)ds)=s^{p-1}ds,$$
因为只有 $j=0$ 的 $q^jb+1$ 被 $p$ 整除。由自然性和系数的 $p$ 根，以 $\alpha$ 表示剩余标量、$\bar\alpha$ 表示有限域共轭，精确得到
$$ D((f_\alpha-\alpha s)^{1/p})
       =\alpha f_\alpha^{p-1}-\bar\alpha s^{p-1}.$$
结合(AZ4)，$V^*=DH+x/c_p+s^{p-1}$ 满足
$\alpha V^*(f_\alpha)=\bar\alpha V^*(s)$。

取奇整数 $\alpha=1+2p$，两侧标量模 $p$ 都等于一。其特征 $p$ 形式端同态仍有无限阶：任意正幂与恒等之差来自非零 $\mathcal O$ 标量，而形式端乘以非零标量不为零。由(AZ5)，$V^*$ 正规且常数为零；若非恒定，则 $k((s))/k((V^*))$ 为有限扩张，$f_\alpha$ 却给它无限多个不同自同构，矛盾。因此 $V^*=0$，证明(BA1)的全形式域等式。

令 $A,B$ 为(AY2)的实际函数。其主部分别为
$$\begin{aligned}
 A&=-s^{-(q+p-1)}+s^{-p}-x^pH+O(1),\\
 B&=2s^{-(q+2p-1)}-3s^{-2p}-2y^pH+O(1).
\end{aligned}$$
第一式由 $U_1=x^qg+A^p$、$g=s+H^p$ 及 $U_1$ 的三个主部取 $p$ 根；第二式由 $DU_2=2y^qg+B^p$ 和 $U_2$ 的准确一导同样得到。

对偶指标 $p+1$，选任一偶函数 $L_{p+1}$ 实现唯一主部 $s^{-(p+1)}$，常数另外指定；$p+2,2p+1$ 如§83。逐项代(BA1)，比较全部主部得
$$\begin{aligned}
 DA&=-L_{p+1}^p+x^{p+1}/c_p+L_{p+1}+\kappa_A,\qquad \kappa_A\in k,\\
 DB&=2L_{p+2}^p+2xy^p/c_p-2L_{2p+1}.
\end{aligned}\tag{BA2}$$
确实 $x^ps^{p-1}$ 唯一主部为 $s^{-(p+1)}$，
$y^ps^{p-1}$ 唯一主部为 $-s^{-(2p+1)}$。首式主部相同只差常数；次式全奇，差常数为零。这些真实 $O(p)$ 极阶函数仍须在完整原17驯泛函内评价。

## 86. 原完整驯微分的三个第一次 Cartier 像

**已证明。** 沿用 §§82–85 的原 $E_1$、全部原 $f$ 挠标记、$\nu,g,H,c_p$。对非零原始 $f$ 挠点 $P$ 定义全局有理微分
$\kappa_P(Q)=K_P(Q)\omega(Q)$，其中
$$
 K_P(Q)=X(P)-\frac{y(Q)-y(-P)}{x(Q)-x(-P)} .
$$
特征零的完成 $\zeta$ 加法式给 $K_P(Q)=X(Q)-X(Q-P)$；这里任意点的 $X$ 只在此加法式指完成 $\zeta$，约化后始终使用上面的有理式。其在 $O,P$ 的简单留数依次 $+1,-1$，原点首项 $s^{-1}+X(P)$。
沿(AX1)，$\nu=-\sum_t\varepsilon(t)\kappa_{-T_t}$，其中
$\sum_t\varepsilon(t)X(-T_t)=0$ 由原中央 $L$ 零。
令 $\mathcal C$ 为 $E_1$ 的绝对 Cartier。对 $r=0,1,2$ 有
$$
 \nu_r:=\mathcal C(g^r\nu)=
  -c_p^{-r}\sum_t\bar\varepsilon(t)X(-T_t)^r\,\kappa_{-T_t}.       \tag{BB1}
$$
在各实际 $-T_t$，Cartier 将简单留数
$\varepsilon(t)g(-T_t)^r$ 取 $p$ 根。由(AZ3)与
$c_p\in\mathbf F_p$ 正是右边的留数。在 $O$，$\nu$ 正则而
$g$ 极阶 $p$。$r=0$ 时 Cartier 仍正则；$r=1,2$ 最多产生
$r$ 阶极点，由局部挑取 $s^{pj-1}ds$ 后变为 $s^{j-1}ds$ 可见。
$\mu_6$ 满足 $[u]^*\nu=u\nu,\ [u]^*g=ug$，因为
$\varepsilon(u)=u$；Cartier 后权为 $u^{-(r+1)}$。$r=1$ 时
这不许简单极的平凡权；$r=2$ 时不许简单极的平凡权或双极的
$u^{-1}$ 权。右端在 $O$ 的可能简单留数亦消失，因为
$\sum_t\bar\varepsilon(t)X(-T_t)^r$ 在 $t\mapsto ut$ 时的权为
$u^{-1-r}\ne1$。两边差全局正则，而 $\omega$ 权 $u$ 与
$u^{-(r+1)}$ 在 $r=0,1,2$ 都不同，所以差为零。

在原点完整形式域内，$s=g-H^p$ 给
$$
 \mathcal C(s^r\nu)=
 \sum_{j=0}^r(-1)^j\binom rj H^j\nu_{r-j}.                        \tag{BB2}
$$
这是实际全源，保留每一驯标记及所有混合 $H$ 项。
在第二次 Cartier 之前，所用三个全局系数均已只涉及固定代数
驯点及其原 $X$ 值。从斜率式及原严格坐标在这些低次与不变对数一致，
$$
 K_P=s^{-1}+X(P)+x(P)s-y(P)s^2+x(P)^2s^3-x(P)y(P)s^4+O(s^5).
$$
故(BB1)的首许可幂分别为 $s^{4-r}ds$，其系数准确是
$\sum\bar\varepsilon xy,\ -c_p^{-1}\sum\bar\varepsilon Xx^2,\
c_p^{-2}\sum\bar\varepsilon X^2y$，每个点均为 $-T_t$。
本节未把这些首许可系数的非零、或其余混合 $H$ 项的总和非零作为已证结论。

## 87. 原十七加权的两个固定代数矩与三条第一 Cartier 首项

**已证明。** 沿用(AY2)的原椭圆曲线、LT模型及既定CM嵌入。写 $P_t=-T_t$，指标跑遍 $t\in(\mathcal O_K/f)^\times$，$f=34\delta,\ \delta=\sqrt{-3}$。横杠在特征零中表示选定的复共轭。定义
$$
 M_1=\sum_t\varepsilon(t)x(P_t)\overline{X(P_t)},\qquad
 M_2=\sum_t\bar\varepsilon(t)\overline{y(P_t)}X(P_t)^2. \tag{BC1}
$$
这两个都是原标记点的固定代数数。另定义
$\Psi_0=\sum\bar\varepsilon xy,\ \Psi_1=\sum\bar\varepsilon Xx^2,\
\Psi_2=\sum\bar\varepsilon X^2y$，每个因子均取同一个 $P_t$。五数均非零。

取标准Weierstrass统一化 $x=\wp,y=\wp'/2$，周期格 $\Lambda=\varpi\mathcal O_K$。实解析函数
$Z(z)=\zeta_\Lambda(z)-(\pi/\operatorname{area}(\mathbb C/\Lambda))\bar z$
为格周期函数：六次旋转令全纯准周期修正为零，Legendre关系给出所写反全纯项。
对 $m=103$，sigma乘法公式给
$m^{-1}D\log\psi_m=Z(mz)-mZ(z)$。因 $m\equiv1\bmod f$，在每个原点 $P_t$ 这给 $X(P_t)=Z(P_t)$，其中
$X=(1-m)^{-1}m^{-1}D\log\psi_m$ 为固定有理函数。
缩放到短向量长一的 $\mathcal O_K$，所有同一和式的项仅共同乘固定非零常数。此时反全纯修正系数是 $2\pi/\sqrt3<4$，令 $F=|f|=34\sqrt3$。
每个原剩余类在最近六边形取一代表，$z=-t/f$ 满足
$r=|z|\le1/\sqrt3,\ |t|\le34$；边上的任选固定代表。写
$t=a+b e^{i\pi/3}$，$j=\max(|a|,|b|,|a+b|)$。
每壳恰 $6j$ 元，$\sqrt3j/2\le|t|\le j$。
六单位为六个不同的原点，均在最近壳。

由壳计数
$S_6=\sum_{\lambda\ne0}|\lambda|^{-6}\le6(2/\sqrt3)^6(1+1/32+1/64)<15$。
故 $|G_{6n}|\le S_6$。以 $w=r^6\le1/27$，从
$\zeta=z^{-1}-\sum_{n\ge1}G_{6n}z^{6n-1}$ 及其导数得
$$
 |zZ-1|\le4r^2+16w,\quad
 |z^2x-1|\le90w/(1-w)^2<98w,\quad
 |z^3y+1|\le270w(1+w)/(1-w)^3. \tag{BC2}
$$
全域有 $r|Z|<3,r^2|x|<5,r^3|y|<13$。
在 $j\le8$ 时 $r<1/7$，三误差依次小于 $1/10,1/100,1/100$。
因此对 $V=y\bar Z^2,yZ^2,x^2Z,xy$，近壳
$4/5<r^5|V|<5/4$，全域 $r^5|V|<117$。
在 $\overline{M_2}=\sum\varepsilon y\bar Z^2$ 中，六单位的项完全同相，由
$\varepsilon(ut)=u\varepsilon(t),\ y(uz)=u^{-3}y(z),\
Z(uz)=u^{-1}Z(z)$ 可见。
三个 $\Psi_r$ 的完整项各自旋转权均为 $-6$，六项亦分别同相。
每和的这六项模大于 $24F^5/5$。
去掉单位，$2\le j\le8$ 项和的绝对值除 $F^5$ 至多
$(5/4)6(2/\sqrt3)^5\sum_{j\ge2}j^{-4}<5/3$，这里尾级数至多 $5/48$；
$j\ge9$ 项的相同上界为
$117\cdot6(2/\sqrt3)^5\int_8^\infty u^{-4}du<117/120<1$。
故 $M_2\Psi_0\Psi_1\Psi_2\ne0$。

对于 $M_1$ 比较原加权函数与极项 $z^{-2}\bar z^{-1}$。
其单位六项同相，模为 $6F^3$。非单位原代表为所有与 $2\delta$ 互素的非单位格向量的一个子集。
Eisenstein整数类数一、有六单位，$2,\delta$ 素理想范数为 $4,3$，故
$$
 \sum_{(t,2\delta)=1}|t|^{-3}
 =6(1-4^{-3/2})(1-3^{-3/2})\zeta(3/2)L(3/2,\chi_{-3}). \tag{BC3}
$$
交错项界给 $L<1-2^{-3/2}+1/8<4/5$，积分界给
$\zeta<1+2^{-3/2}+\sqrt2<14/5$。
另有 $1-3^{-3/2}<5/6,\ 1-4^{-3/2}=7/8$。
故除去六单位后，所有极项尾部绝对值小于 $19F^3/5$。
由(BC2)与 $r|Z|<3$，
$|z^2\bar z\,x\bar Z-1|\le4r^2+310r^6$。
原代表至多 $Nf=3468$ 个、只有 $j\le39$，故
$\sum|t|^{-1}\le6(2/\sqrt3)39<312$，
$\sum|t|^3\le3468\cdot34^3$。
全部椭圆误差除 $F^3$ 至多
$$
 {4\cdot312\over3468}
 +{310\cdot3468\cdot34^3\over(34\sqrt3)^6}<2/5+11/10=3/2 .
$$
因 $6-19/5-3/2>0$，有 $M_1\ne0$。

令有限Galois扩张 $L/\mathbb Q$ 含所用全部挠点坐标、$\varepsilon,X$、
其复共轭、$\mu_{204}$ 及 $\sqrt{17}$。
Chebotarev用选定复共轭 $c$ 的共轭类，并在每个这样的素数上选择Frobenius恰为 $c$ 的一个素位。
所用标准定理见 Andrew V. Sutherland, *Global class field theory, the Chebotarev density theorem*,
18.785 Lecture 28 (2019), Theorem 28.9, p.6，
[原讲义](https://math.mit.edu/classes/18.785/2019fa/LectureNotes28.pdf)。
此列有无穷多 $p\equiv-1\bmod204$，故 $p$ 在 $K$ 惰性且在
$\mathbb Q(\sqrt{17})$ 分裂，$\beta=\sqrt{17}\in\mathbb Q_p$。
去掉有限坏素位、分母及五个非零数的范数因子，此列每个 $p>211$ 上
$p$ 次方在所有真正标记的代数数上是所选复共轭，$q=p^2$ 次方固定它们。
结合 $G(P_t)=X(P_t)^p$、$g=G/c_p$、$c_p\in\mathbb F_p^\times$
与 $\ell_{17}(U_1)=0$，(AY2)的两个精确输出为
$$
 \sum_t\varepsilon(t)A(P_t)^p=-M_1/c_p\ne0,\qquad
 \ell_{17}(U_2)^{1/p}
 =\sum_t\bar\varepsilon(t)\bigl(C(P_t)+X(P_t)B(P_t)/c_p\bigr)
  +M_2/c_p^2. \tag{BC4}
$$
第一式按 $x(P_t)^q=x(P_t)$ 使用 $U_1=x^qg+A^p$；
第二式来自原 $U_2=y^qg^2+B^pg+C^p$ 逐项取唯一 $p$ 次根。
于是若 $a_2=0\bmod p$，原 $B,C$ 对合和必须恰等于
$-M_2/c_p^2\ne0$。这是第三分量与第一原函数所强迫的补偿值。
排除第二式整体抵消仍是原非消失问题。

另由§86的(BB1)及其初始消失格，$r=0,1,2$ 的首非零系数
（除去 $\omega$）依次确为
$\Psi_0$ 在 $s^4$、$-c_p^{-1}\Psi_1$ 在 $s^3$、
$c_p^{-2}\Psi_2$ 在 $s^2$。
这个第一Cartier首项结论在一切充分大的原允许惰性素数上成立：
所用五数固定非零，排除其分母与范数因子只排除有限多个有理素数。
$\Psi_2$ 中是 $y$，(BC4)的 $M_2$ 中是 $\bar y$，二者的角色与来源各自保留。
以上没有宣称 $\ell_{17}(U_2)$ 或 $a_2$ 已非零。

## 88. 原四项的第二次 Cartier 及固定标记系数的下降

**已证明。** 记 $P_t=-T_t,w_t=X(P_t)$。对 $i+j\le2$ 置
$$
 \nu_{ij}=\mathcal C(g^i\nu_j),\qquad
 D_{ij}=-c_p^{-i-j}\sum_t\varepsilon(t)w_t^i(w_t^j)^{1/p}\kappa_{P_t}.
$$
则 $\nu_{ij}=D_{ij}$，惟 $\nu_{11}=D_{11}+\kappa\omega$
可有常数 $\kappa$。其中 $\nu_{00}=\nu$ 准确成立。

先证 $\mathcal C(\kappa_P)=\kappa_P$。取 $mP=0$，$m$ 素于 $p$。
在等边复格上，记面积除 $\pi$ 为 $A_\Lambda$，则
$$
 u_P(z)=\left(\frac{\sigma(z)}{\sigma(z-P)}\right)^m
             \exp(-m\bar Pz/A_\Lambda)
$$
由 $mP$ 为格点及Legendre周期式是椭圆函数：
平移 $\lambda$ 的倍数为
$\exp(m(P\bar\lambda-\bar P\lambda)/A_\Lambda)=1$。
其除子为 $m([O]-[P])$，且 $m^{-1}d\log u_P=\kappa_P$。
函数比例不影响此等式，故可在原代数除子域选同除子的代数函数，
再沿好约化约化。绝对Cartier固定对数微分及其 $\mathbb F_p$ 标量倍。
因此(BB1)给 $\nu_{00}=\nu$。

其余各对先在实际驯点把简单留数取 $p$ 根，得到 $D_{ij}$。
在 $O$，$\nu_j$ 均正则，最多产生 $i$ 阶极点，实际权为
$u^{1+j-i}$。当 $(i,j)=(1,0)$ 时，可能简单极的系数来自
$c_p^{-1}s^{-p}\nu_0$；当 $(i,j)=(2,0)$ 时，可能双极的系数
来自 $c_p^{-2}s^{-2p}\nu_0$。它们均由
$$
 [s^{p-1}](\nu_0/ds)=(\nu(O)/ds)^p=0
$$
消去。后一对的其余项不能贡献双极，简单极又被权 $u^{-1}$ 排除。
其余各对没有容许的极阶。$D_{ij}$ 在 $O$ 的简单留数由同一
单位权或 $\sum\varepsilon(t)w_t=0$ 排除。
全局正则差的权只有 $i=j$ 才容 $\omega$；$(0,0)$ 已准确定出。

$q$ 次系数Frobenius在 $E_1$ 的标记点上为 $[-p]$。
$X(P_t)=K_{103}(P_t)/(1-103)$ 来自固定有理函数，
$\varepsilon(-p)=1$，因此 $t\mapsto-pt$ 使上列每个完整和
被 $q$ 次系数Frobenius固定。这也适用于 $w_t^{1/p}$，
因为有限域根与Galois重标交换。
$g,s,H$ 由原 $\mathbb F_p$ 模型及唯一主部、严格坐标下降。
所以所用完整微分和最终标量的系数在 $\mathbb F_q$；
没有逐点假设 $P_t$ 或 $w_t$ 在 $\mathbb F_q$。

写 $R_m(\eta)=\operatorname{Res}_O s^{-m}\eta$。
在§83将 $U_2$ 加 $U_1$ 并调 $U_0$ 不改 $\ell_{17}$，故容取
$$
 V_2=-L_{p(2q+p-2)}+2L_{p(q+2p-1)-1}
                       -L_{3q-2}-2L_{2q-1}.
$$
因 $\nu$ 在 $O$ 正则，$L_n$ 可在任一
$\operatorname{Res}_O L_n\nu$ 换为 $s^{-n}$。
将 $n=p^2N-pr-e$，两次使用
$R_{pm}(\eta)^{1/p}=R_m(\mathcal C\eta)$。
由上段的完整源下降，两次 $p$ 根后最终值不变，得到
$$
\begin{aligned}
 \operatorname{Res}_O V_2\nu={}&
 -R_{2p+1}(\nu_{20}-2H\nu_{10}+H^2\nu_{00})\\
 &+2R_{p+2}(\nu_{11}-H\nu_{01}-\mathcal C(sH\nu_0))\\
 &-R_3(\nu_{02}-2\mathcal C(H\nu_1)+\mathcal C(H^2\nu_0))\\
 &-2R_2(\nu_{01}-\mathcal C(H\nu_0)).
\end{aligned} \tag{BD1}
$$
具体四个 $(N,pr+e)$ 依次是
$(2p+1,2p),(p+2,p+1),(3,2),(2,1)$。
用 $s=g-H^p$ 展开后恰给显示的全部混项。
$\nu_{11}$ 的可能 $\kappa\omega$ 因 $p+2>1$ 不贡献。
所有 $H$ 项中仅
$R_{p+2}(\mathcal C(sH\nu_0))$ 触及 $q+2p$ 的窗；
其余最多使用 $3p+1$。
由全局留数及(AX1)，
$$
 34f_1(1-\omega_K)a_2=(h-h^p)^{p-3}\operatorname{Res}_O V_2\nu.
$$
这仍是原完整二阶量；本节不给四项的总和非零。

## 89. 唯一深窗的特征零 ζ 规范与自由 Witt 项的全源相消

**已证明。** 写 $x_{\rm cl}(z)=\wp(z)$ 为原特征零曲线的Laurent级数，
$\zeta'(z)=-x_{\rm cl}(z),\ \zeta=z^{-1}+\cdots$，取
$$
 u=-1/[z^{p-1}]x_{\rm cl}(z)\in\mathbb Z_p^\times,\qquad
 Z(s)=u\zeta(\ell(s))-\ell(s^p)/p. \tag{BE1}
$$
这里 $Z$ 是本节新定义的规范函数，不是此前几何分支的坐标。
R301(12)与(BA1)给 $u\bmod p=c_p^{-1}$；$\ell$ 仍是原严格LT对数。
到次数 $<pq$，$Z$ 的Laurent系数全整，且
$$
 H(s)=\overline{Z}(s)+\kappa s^p+O(s^{pq}),\qquad\kappa\in\mathbb F_p.
 \tag{BE2}
$$
本模型的 $\kappa\in\mathbb F_p$ 来自真实下降：
$E_1$ 的原参数及 $[\pi]s=-ps+s^q$ 均定义在 $\mathbb Z_p$，
二者导数一的严格LT同构由唯一性被未分歧Frobenius固定。
$G=L_p$ 由其主部及奇性同样下降，且 $u,\zeta,\ell$ 属原有理基。

对奇且素于 $p$ 的 $\alpha\in\mathcal O_K$，令 $f_\alpha=[\alpha]s$；
$f_{\bar\alpha}$ 是其系数Frobenius。Witt商
$$
 Q_\alpha=\frac{f_\alpha(s)^p-f_{\bar\alpha}(s^p)}p
 \quad\hbox{整，且}\quad
 \overline Q_\alpha^{\,p}=f_\alpha(s)-\alpha s\pmod p. \tag{BE3}
$$
横杠 $\overline Q_\alpha$ 在此表示约化。
由 $[\pi]f_\alpha=f_\alpha([\pi]s)$ 及 $f_\alpha'\equiv\alpha\bmod p$，
模 $p^2$ 有
$f_\alpha(s)^q-pf_\alpha(s)\equiv f_\alpha(s^q)-p\alpha s$。
又 $f_\alpha(s)^q\equiv f_{\bar\alpha}(s^p)^p\bmod p^2$，
故取商后得
$Q_{\bar\alpha}(s^p)\equiv f_\alpha(s)-\alpha s
\equiv Q_\alpha(s)^p\bmod p$，证(BE3)。

$\ell'$ 整，且两个内参数相差 $pQ_\alpha$，所以
$$
 \frac{\ell(f_\alpha(s)^p)-\ell(f_{\bar\alpha}(s^p))}{p}
       \equiv\overline Q_\alpha\pmod p
$$
并且全级数整。严格地，Taylor第 $j\ge2$ 阶的系数至少被
$p^j/j$ 整除，除 $p$ 后仍为零模 $p$。
因 $\ell(f_{\bar\alpha}(s^p))=\bar\alpha\ell(s^p)$，由
特征零 $\zeta(\alpha z)-\bar\alpha\zeta(z)=K_\alpha$ 得
$Z(f_\alpha)-\bar\alpha Z$ 全整，约化为
$c_p^{-1}K_\alpha-\overline Q_\alpha$。

$Z$ 首主部 $u/s$ 整，导数
$-u x_{\rm cl}(\ell(s))\ell'(s)-s^{p-1}\ell'(s^p)$ 全整：
$x_{\rm cl}(\ell(s))$ 是原严格形式参数中的代数坐标。
若在 $0\le n<pq$ 有第一个非整系数，则 $p\mid n$；
前段的换元取遍模 $p$ 的 $\mathbb F_q^\times$，
比较 $s^n$ 强迫 $n\equiv p\bmod b$。
这两个条件在此范围唯一可能 $n=p$。
$\ell(s)=s+O(s^q)$，而(BE1)的 $s^p$ 系数为
$-u[z^{p-1}]x_{\rm cl}/p-1/p=0$，矛盾。

比较 $\overline Z$ 与 $H$，(BA1)给两导数相同；
(BE3)与(AZ2)的 $p$ 根给相同CM换元缺陷。
在此窗对各Teich类取奇 $\alpha\equiv a\bmod p^2$，
则 $f_\alpha(s)=as+O(s^{q^2})\bmod p$。
两个条件排除所有次数，仅 $s^p$ 可留，证(BE2)。

在(BD1)内将每一个 $H$ 换为 $\overline Z$，
同时将Cartier乘子的每个显式 $s$ 换成
$w=g-\overline Z^p$，特别包括 $\mathcal C(sH\nu_0)$ 之 $s$。
末端 $R_N$ 仍用实际 $s$。
这个完整规范表达式仍等于原 $\operatorname{Res}_O V_2\nu$。
证明如下。由(BE2)，
$w=s+\kappa s^q+O(s^{p^2q})$；任取更高尾延拓不影响所需范围。
还原两次Cartier前各项为
$\operatorname{Res}_O s^{-p^2N}s^{pr+e}\nu$，
现在分子改为 $w^{pr+e}$。
四个 $pr+e=2p,p+1,2,1$，令 $Y=s^b$，
相应多出因子
$(1+\kappa Y)^{2p},(1+\kappa Y)^{p+1},(1+\kappa Y)^2,1+\kappa Y$。
记 $B'_j=\operatorname{Res}_O s^{-(jb+1)}\nu$，
原 $j$ 依次 $2p+1,p+2,3,2$，系数 $-1,2,-1,-2$。
由于 $\kappa^p=\kappa$，新增部分依次为
$$
\begin{aligned}
 &-2\kappa B'_{p+1}-\kappa^2B'_1,\\
 &2\kappa B'_{p+1}+2\kappa B'_2+2\kappa^2B'_1,\\
 &-2\kappa B'_2-\kappa^2B'_1,\qquad -2\kappa B'_1 .
\end{aligned}
$$
合计 $-2\kappa B'_1$；而
$B'_1=R_q\nu=0$ 由 $\mathcal C^2\nu=\nu$ 及 $\nu(O)=0$ 得到。
故规范替代准确，未单独丢弃任何自由项或混项。

所需唯一深窗明确由
$$
 Z(s)=u\zeta(s)-u\ell_qs^q x_{\rm cl}(s)-s^p/p
                    +O(s^{2q-3}),\qquad
 \ell_q=1/(\pi-\pi^q),\quad\pi=-p                         \tag{BE4}
$$
给出，因为 $q+2p<2q-3$。
这里整性针对完整组合，没有孤立假设 $\zeta$ 的各个系数整，
也没有用规范化替换原canonical量。
