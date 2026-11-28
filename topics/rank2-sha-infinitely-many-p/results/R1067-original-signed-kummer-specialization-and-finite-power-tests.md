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
