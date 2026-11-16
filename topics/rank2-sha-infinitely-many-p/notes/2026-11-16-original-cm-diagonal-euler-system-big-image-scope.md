# 原全 CM 对角循环与现成 Euler-system 定理的适用范围

状态：直接适用障碍已完整证明；这不是原 AJ 消失结论，也未关闭主目标。

## 1. 这次实际核读的两处来源

- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL2 × GL2*，[作者 PDF](https://web.math.princeton.edu/~raular/ES1.pdf)，核读 Theorem B 及其后 Remark (1)（印页 2–3）、§8.1 的 (HW)/(HS)（印页 40）。Theorem B 由非零底类推出 Selmer 一维时要求 big image；(HW)(1) 要求特征零绝对不可约，(HS)(1′) 要求剩余绝对不可约。Remark (1) 对复解析秩一仍明确保留 p-adic étale AJ 单射问题。
- Castella–Do, *Diagonal cycles and anticyclotomic Iwasawa theory of modular forms*，[arXiv:2303.06751v2](https://arxiv.org/html/2303.06751v2)，核读 Theorem B、§4.3.1、§4.3.2。其 Selmer 秩一应用明列 f 非 CM；证明使用 V 在 G_K 上绝对不可约。Theorem A 的类构造与这些应用须分开。

引用的是以上实际所读版本，不把网页抓取时间认作论文新定理。来源中的类构造没有被本札记否定。

## 2. 原表示直接不满足不可约条件

本课题固定 K=Q(ω)，两原 weight-two 输入 g,h 均由 K 的 Hecke 角色诱导。在包含角色值的有限系数扩张 E′ 上有

$$
 V_g|_{G_K}=E'(\psi_g)\oplus E'(\psi_g^c),\qquad
 V_h|_{G_K}=E'(\psi_h)\oplus E'(\psi_h^c).
$$

故对任一原标量角色 ρ 和 Tate twist，完整四维表示恰分成

$$
 (V_g\otimes V_h\otimes\rho)|_{G_K}
 =\bigoplus_{\epsilon,\eta\in\{1,c\}}
 E'(\psi_g^\epsilon\psi_h^\eta\rho).
 \tag{1}
$$

即使某两角色偶合，右侧仍有真一维不变子空间；任何改变整格或选好系数素数都不能使 (1) 绝对不可约。因此 ACR 的 (HW)(1) 对原四维输入不成立。

剩余条件也不能用换整格逃掉。设 T 是任何满 G_K-稳定整格，有限扩系数后为 T′。取 (1) 的一条直线 W，并令 L=T′∩W。L 在 T′ 中饱和，秩为一；T′/L 无挠，所以对系数均匀元 π，

$$
 0\longrightarrow L/\pi L\longrightarrow T'/\pi T'
$$

仍单射。它给出非零真稳定子空间，故剩余表示不绝对不可约；ACR 的 (HS)(1′) 同样失败。

若先按两个 CM 输入拆成 Castella–Do 的二维 V_{f,χ}，本课题剩余的 f 本身仍是同 K 的 CM 型，限制 G_K 后仍拆成两条线。于是其明示的非 CM 条件和证明中所需的绝对不可约均不满足。这里的 K 是原 CM 域，不可为套用定理而另换辅助二次数域并沿用原 Z 的比较。

## 3. 对当前工作的准确影响

本课题可以继续使用已付的原 CM 投影、原整 AJ/惯性 shadow 检测及全部原 Euler 因子。式 (1) 也允许逐角色投影已经构造的类。但投影后的单线表示不是 ACR Theorem B 的原四维输入；若另立一维 Euler-system 论证，须实际证明该类的范数关系、原局部条件、整格与所要通常全 Selmer 的比较。不能把完整特征多项式的其它因子直接删去。

此外，“原循环复高度非零”不能仅凭上述两处文献直接升级为“原 p-adic AJ 非零”。原坏处比较另见 [既有范围核对](2026-11-15-repaired-diagonal-global-comparison-scope.md)；当前执行的两张原坐标认证和完整闭点 shadow 正是在支付这个实际缺口。

结论只排除这两条未经补证的直接引用。它既不证明原循环为零，也不声称所有 CM Euler-system 方法均不可用。原 AJ 是否非零、由此到固定 E/Q 的无穷不同 p 的通常全 Sha[p∞] 有限，仍按 open.md 保留。
