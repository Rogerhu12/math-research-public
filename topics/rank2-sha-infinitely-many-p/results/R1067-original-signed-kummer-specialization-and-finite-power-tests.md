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
