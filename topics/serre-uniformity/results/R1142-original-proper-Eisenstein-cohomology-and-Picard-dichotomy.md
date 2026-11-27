# R1142：原 Eisenstein proper 上同调的整模与 Picard 二分

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，条件准确如下。** 只假设
$$
p>37,\qquad p\nmid B_{p-5}.
\tag{1142.1}
$$
在 R1141 的原算术模型、原角色及实际 $I_3$ Hecke 块上，整个 proper
$H^2$ 是自由秩一的 $\mathcal O/p\mathcal O$ 模。其 Picard 子模只能为零或整个
$H^2$，由同一个 Mordell–Weil 整模的秩 $d=0$ 或 $1$ 决定。

原指定杯积 $\kappa(F_{\chi_1})\cup\kappa(\epsilon_2)$ 在 proper $H^2$ 中
**非零**，生成该块的唯一 $\mathfrak m$-socle。它在函数域中非零当且仅当
$d=0$；若 $d=1$，则它是非零 Picard 类，函数域像为零。
本文不判断哪一种 $d$ 实际发生，也不把 R1141 的函数域杯积关系升级成
proper Heisenberg 或四阶覆盖。这里不增加 $B_{16}$ 或 $B_{p-15}$ 的假设。

## 1. 同一模型、同一格与有限 Teichmüller 扭转

完全沿用 [R1141](R1141-original-arithmetic-endpoint-and-circular-unit-cup.md)：
$$
K=\mathbb Q(\zeta_p),\quad
S=\operatorname{Spec}\mathcal O_K[1/p],\quad
S_0=\operatorname{Spec}\mathbb Z[1/p],\quad
\Delta=\operatorname{Gal}(K/\mathbb Q).
$$
$\mathscr X/S$ 是 R1067 的原 smooth proper 曲线，$f:\mathscr X\to S$；
其 cusps 给 $S$-sections。$\mathcal J=\operatorname{Pic}^0_{\mathscr X/S}$，
$J$ 是原 $J_{\rm ns}$。角色是
$$
\chi_1=\omega^{-2},\qquad \chi_2=\omega^{-4},\qquad
\theta=\omega^{-6},\qquad \xi=\theta\omega^{-1}=\omega^{-7}.
\tag{1142.2}
$$
固定原 $\zeta_p$ 后，$\mu_p^{\otimes2}$ 与 $\mu_p$ 的识别将
$\theta$ 改为 $\xi$。全文按这个角色偏移使用 Picard 与 Brauer 群。

$\mathbb T$ 是原 away-$p$ Hecke 整代数，
$$
\mathfrak m=(p,T_\ell-\ell^{-2}-\ell^3:\ell\ne p),\qquad
\mathcal O=(\mathbb T\otimes\mathbb Z_p)_{\mathfrak m}.
\tag{1142.3}
$$
负指数只表示剩余域中的值；$\mathfrak m$ 的定义用任一整数提升。
R1131 在 $j=1$ 时的两条件为 $B_6$ 与 $B_{p-5}$ 为单位。
$B_6=1/42$ 对 $p>37$ 恒为单位，因此 (1142.1) 已足够给出：

- $\mathcal O$ 是剩余域 $\mathbb F_p$ 的 DVR；
- $M=e_{\mathfrak m}T_pJ$ 为自由秩二 $\mathcal O$ 格；
- 实际 $J[\mathfrak m]$ 为非分裂扩张
  $0\to\omega^{-2}\to J[\mathfrak m]\to\omega^3\to0$；
- 左侧是原非零 $D_1=[\operatorname{div}(F_{\chi_1})/p]$ 尖点线；
- $J(K)[p^\infty]_{\mathfrak m}^{-}=0$。

这些是原 Cartan 块的整结论，不能改成一个仅有相同半单化的表示。
取均匀元 $\pi$，写
$$
p=u\pi^e,\qquad u\in\mathcal O^\times,\qquad E=\operatorname{Frac}(\mathcal O).
\tag{1142.4}
$$
记 $\widetilde\omega$ 为模 $p$ 圆分角色的有限阶 Teichmüller 提升，定义
$$
V_r=(M\otimes\widetilde\omega^{\,7})/\pi^r
\quad(r\ge1).
\tag{1142.5}
$$
它们是 $S_0$ 上的有限 étale sheaves：原 $J$ 在 $p$ 外良约化。
这里的扭转是通过 $\Delta$ 的有限角色，**不是**完整 $p$-adic 圆分角色的七次幂。
对每一 $r$，degree-$p-1$ 的 étale cover $S/S_0$ 给
$$
H^i(S_0,V_r)
 \simeq H^i(S,J[\pi^r]_{\mathfrak m})_{\widetilde\omega^{-7}}.
\tag{1142.6}
$$
通过 $M/\pi^rM\simeq\pi^{-r}M/M$ 理解右侧；在 $r=e$ 时就是 $J[p]$，
其中 $p=u\pi^e$ 至多改变一个已保留的单位识别。

## 2. 剩余 sheaf 的 $H^0,H^1,H^2$ 全部确定

(1142.5) 的第一层是原扩张的准确扭转：
$$
0\longrightarrow\mathbb F_p(\omega^5)
 \longrightarrow V_1
 \longrightarrow\mathbb F_p(\omega^{10})
 \longrightarrow0.
\tag{1142.7}
$$
两个角色都非平凡，因此 $H^0(S_0,V_1)=0$。

先记录 $H^1$，同时把所用的类群条件明确写出。对任意 $s$，
因为 $p\nmid|\Delta|$，
$$
H^i(S_0,\mathbb F_p(\omega^s))
 \simeq H^i(S,\mu_p)_{\omega^{1-s}}.
\tag{1142.8}
$$
在 $s=10$ 时右侧的角色为 $\omega^{-9}$。
奇 $S$-单位部分只有 $\mu_p$ 的 $\omega$ 角色，唯一 $p$ 位的 valuation
角色为一；Herbrand 的正向定理及 $B_{10}=5/66$ 为单位又给
$\operatorname{Cl}(K)[p]_{\omega^{-9}}=0$。Kummer 序列因此给
$$
H^1(S_0,\omega^{10})=0.
\tag{1142.9}
$$
在 $s=5$ 时，R1069 §§2–3 的反射与圆单位定位、以及 (1142.1) 给
$$
H^1(S_0,\omega^5)
 \simeq H^1(S,\mu_p)_{\chi_2}
 =\mathbb F_p\,\beta_{\chi_2},
\qquad \beta_{\chi_2}\ne0.
\tag{1142.10}
$$
$\beta_{\chi_2}$ 仍是原固定奇生成元 $a$ 所定义的
$e_{\chi_2}[\zeta_p^{(1-a)/2}(1-\zeta_p^a)/(1-\zeta_p)]$。
由 $H^0(S_0,\omega^{10})=0$ 及 (1142.9)，
$$
H^1(S_0,\omega^5)\xrightarrow{\sim}H^1(S_0,V_1)\simeq\mathbb F_p.
\tag{1142.11}
$$

现在确定 $H^2$。R1141 §3 的全球 invariant 论证已给
$\operatorname{Br}(S)=0$：$K$ 无实位且只有一个 $p$ 位。因此
$$
H^2(S,\mu_p)=\operatorname{Pic}(S)/p.
\tag{1142.12}
$$
R1069 对 $B_{p-5}$ 单位的反射论证给
$\operatorname{Cl}(K)[p]_{\omega^{-4}}=0$；Herbrand 和 $B_{10}$ 给
$\operatorname{Cl}(K)[p]_{\omega^{-9}}=0$。
有限 $p$-群的该角色 $[p]$ 为零等价于其整个 $p$-primary 部分为零，
故其 $/p$ 也为零。$\operatorname{Pic}(S)$ 是类群的商，
所以 (1142.8)、(1142.12) 得
$$
H^2(S_0,\omega^5)=H^2(S_0,\omega^{10})=0.
\tag{1142.13}
$$
对 (1142.7) 取长正合序列，即得
$$
\boxed{\quad
H^0(S_0,V_1)=H^2(S_0,V_1)=0,\qquad
H^1(S_0,V_1)\simeq\mathbb F_p.
\quad}
\tag{1142.14}
$$
此处不需要假设 $H^3$ 消失，也没有用 Vandiver 或全类群消失。

## 3. 从一层到每一层：不是只作维数计数

记 $A_r=H^1(S_0,V_r)$。$V_r$ 的 successive quotients 都是 $V_1$，
所以由 (1142.14) 归纳有
$$
H^0(S_0,V_r)=H^2(S_0,V_r)=0.
\tag{1142.15}
$$
对 $r\ge2$，实际 sheaf 的两条正合序列是
$$
0\to V_{r-1}\xrightarrow{\pi}V_r\to V_1\to0,
\qquad
0\to V_1\xrightarrow{\pi^{r-1}}V_r\to V_{r-1}\to0.
\tag{1142.16}
$$
(1142.15) 使它们在 $H^1$ 上分别给
$$
0\to A_{r-1}\to A_r\to A_1\to0,\qquad
0\to A_1\to A_r\to A_{r-1}\to0.
\tag{1142.17}
$$
故 $\operatorname{length}_{\mathcal O}A_r=r$。
更关键的是，$V_r$ 上的乘 $\pi$ 正是
$$
V_r\twoheadrightarrow V_{r-1}\xrightarrow{\pi}V_r
$$
的复合。第二条 (1142.17) 的满射与第一条的单射给
$$
\pi A_r=\ker(A_r\longrightarrow A_1).
\tag{1142.18}
$$
于是 $A_r/\pi A_r\simeq\mathbb F_p$。Nakayama 迫 $A_r$ 为循环
$\mathcal O$ 模；它被 $\pi^r$ 杀且长度恰为 $r$，遂有
$$
\boxed{\qquad H^1(S_0,V_r)\simeq\mathcal O/\pi^r
\quad(r\ge1).\qquad}
\tag{1142.19}
$$
同构未指定生成元。这里显式支付了乘 $\pi$ 的模结构，
没有从“长度 $r$”直接猜循环性。

上述识别可按 (1142.17) 的 reduction 递归选择相容生成元。
在 $J[\pi^r]\hookrightarrow J[\pi^{r+1}]$ 的真正 inclusion 下，
(1142.19) 的 transition 是乘 $\pi$。
因此也有
$$
H^1(S,\mathcal J[p^\infty])_{\mathfrak m,\widetilde\omega^{-7}}
 \simeq E/\mathcal O.
\tag{1142.20}
$$
这里只是同一有限 sheaf 链的 filtered colimit，不将较高层的
$\mu_{p^r}^{\otimes2}$ 与有限 Teichmüller 扭转混同。

## 4. 原 proper $H^2$ 与这个 $H^1$ 的完整同构

R1141 已付 $f$ 的有限系数 Leray 序列中
$$
R^1f_*\mu_p=\mathcal J[p],\qquad R^2f_*\mu_p=\mathbb F_p.
\tag{1142.21}
$$
第二个是 degree 的常值 sheaf，带原 $\Delta$ 作用仍平凡。
因为 $\xi=\omega^{-7}\ne1$，
$H^0(S,R^2f_*\mu_p)_\xi=0$。

base 的 $H^2$ 也消失，但所用 Bernoulli 不是 (1142.1)。
由 (1142.12) 及 Herbrand，$\xi=\omega^{1-8}$ 对应
$B_8=-1/30$，所以
$$
H^2(S,\mu_p)_\xi=(\operatorname{Pic}(S)/p)_\xi=0.
\tag{1142.22}
$$
$p>37$ 已保证这个常数 Bernoulli 为单位。

还须处理可能的 transgression
$$
d_2^{1,1}:H^1(S,\mathcal J[p])\longrightarrow H^3(S,\mu_p).
\tag{1142.23}
$$
原 cusp section $s:S\to\mathscr X$ 给 $s^*f^*=1$，
故 $f^*:H^3(S,\mu_p)\to H^3(\mathscr X,\mu_p)$ 单射。
其 Leray edge 经 $E_\infty^{3,0}$ 分解，
所以一切进入这个 base 项的 differential 都为零，特别是 (1142.23)。
不要求所选 section 在 $\Delta$ 下固定：全群上的 $f^*$ 已单射，
而 $f^*$ 本身是 $\Delta$-等变的。

$(1,1)$ 项没有其他可能的 incoming 或 outgoing differential。
结合 (1142.21)–(1142.23)，Leray filtration 的另外两项在 $\xi$ 上都为零，
故有真正的 edge 同构
$$
\boxed{\quad
H^2(\mathscr X,\mu_p^{\otimes2})_\theta
 \xrightarrow{\ \sim\ }
H^1(S,\mathcal J[p])_\xi .
\quad}
\tag{1142.24}
$$
这里尚未取 Picard 商，因而比 R1141 的 Brauer 单射更强。

R1141 §2 的水平 Hecke 闭包、cycle class 与 smooth-proper trace
在左侧定义全部实际 $T_\ell$，并保持 Leray filtration；
它在 $R^1$ 上正是原 $\mathcal J[p]$ 的 Hecke endomorphism。
因此 (1142.24) 是 Hecke 等变同构。
特别，左侧在此角色上的整代数关系由右侧真实 Jacobian 的关系保证，
可以合法取 $\mathfrak m$-因子，而不是先假设所有形式 correspondence 关系
自动在绝对 $H^2$ 上成立。

令
$$
\mathcal H=H^2(\mathscr X,\mu_p^{\otimes2})_{\theta,\mathfrak m}.
$$
由 (1142.6)、(1142.19) 的 $r=e$ 情形，
$$
\boxed{\qquad
\mathcal H\simeq\mathcal O/p\mathcal O
\quad\text{作为实际 }\mathcal O\text{ 模}.
\qquad}
\tag{1142.25}
$$
它的 $\mathbb F_p$ 维数是 $e$，不必为一；
只有 $\mathfrak m$-socle 必为一维。

## 5. Picard 子模只能为零或整个块

定义真正 Mordell–Weil 整模
$$
N=(J(K)\otimes\mathbb Z_p)_{\mathfrak m,\widetilde\omega^{-7}}.
\tag{1142.26}
$$
此处用同一个 completed Hecke projector 和 Teichmüller 幂等元。
$J(K)$ 有限生成，$\mathcal J$ proper 保证 $\mathcal J(S)=J(K)$。

$\widetilde\omega^{-7}$ 是奇角色。R1131 的
$J(K)[p^\infty]_{\mathfrak m}^{-}=0$ 因而保证 $N$ 没有 $p$-torsion。
对任一非零 $a\in\mathcal O$，存在 $n$ 使 $a\mid p^n$；
若 $a$ 杀掉 $N$ 中的元素，该元素便被 $p^n$ 杀掉，只能为零。
所以 $N$ 是有限无挠 $\mathcal O$ 模。$\mathcal O$ 是 DVR，遂有
$$
N\simeq\mathcal O^d
\quad\text{对某个整数 }d\ge0.
\tag{1142.27}
$$
这一步没有把“奇圆分 torsion 消失”误用为“奇 Mordell–Weil 秩为零”。

现在准确识别 Picard 项。degree 的角色平凡，而 (1142.22) 已消
$\operatorname{Pic}(S)/p$ 的 $\xi$ 部分。
原 section 使 relative Picard 的 degree-one 类存在，
并给 Poincaré rigidification；因此其 degree-zero $S$ 点正是
$\mathcal J(S)$，且能由 $\operatorname{Pic}(\mathscr X)$ 提升。
也可从 Picard–Brauer exact sequence 与 $\operatorname{Br}(S)=0$ 得同一满射。
对 degree、base Picard 及 relative Picard 序列取 $/p$ 和 $\xi$ 部分，
得到
$$
\bigl(\operatorname{Pic}(\mathscr X)/p\otimes\mu_p\bigr)_{\theta,\mathfrak m}
 \simeq N/pN.
\tag{1142.28}
$$
这里无需声称 $\operatorname{Pic}(S)$ 本身为零；只用了已付的准确角色。
该识别对实际 Hecke 等变。

Kummer 正合序列及 (1142.25) 因而是
$$
0\longrightarrow N/pN
 \longrightarrow \mathcal H
 \longrightarrow \operatorname{Br}(\mathscr X)[p]_{\xi,\mathfrak m}
 \longrightarrow0,
\qquad
N/pN\simeq(\mathcal O/p\mathcal O)^d.
\tag{1142.29}
$$
左侧单射到一个长度为 $e$ 的循环模，迫 $de\le e$，即
$$
\boxed{\qquad d\in\{0,1\}.\qquad}
\tag{1142.30}
$$
若 $d=1$，该单射两侧长度相同，所以是满射。
因此恰有以下二分：

| 原 MW 秩 | proper Picard 子模 | 原 Brauer 块 |
|---|---|---|
| $d=0$ | $0$ | $\operatorname{Br}(\mathscr X)[p]_{\xi,\mathfrak m}\simeq\mathcal O/p\mathcal O$ |
| $d=1$ | $\mathcal H$ | $\operatorname{Br}(\mathscr X)[p]_{\xi,\mathfrak m}=0$ |

不存在一个非零真 Picard 子模的第三种可能。
这个结论依赖 (1142.27) 的真实无挠性；只知道 $N/pN$ 长度有限不足以得到它。

由于 regular 模型的 Brauer 群向函数域单射，在 $d=0$ 时，
$\mathcal H\to H^2(K(X),\mu_p^{\otimes2})$ 单射。
在 $d=1$ 时该映射在整个 $\mathcal H$ 上为零。
本文不以二分本身选定其中一项。

## 6. 原指定 proper 杯积确为非零 socle 生成元

取原全局单位 $\epsilon_2$ 代表 (1142.10) 的 $\beta_{\chi_2}$，并保留
R1141 的原 finite étale torsor $\kappa(F_{\chi_1})$。置
$$
\widehat B_{12}
 =\kappa(F_{\chi_1})\cup\kappa(\epsilon_2)
 \in H^2(\mathscr X,\mu_p^{\otimes2})_\theta.
\tag{1142.31}
$$
R1141 (1141.26) 的准确 Leray product 是
$$
-\bigl(\kappa(\epsilon_2)/\zeta_p\bigr)\otimes D_1
 \in H^1(S,\mathcal J[p])_\xi.
\tag{1142.32}
$$
$D_1$ 为原 $J[\mathfrak m]$ 中非零 $\omega^{-2}$ cusp vector。
所以 (1142.32) 是 (1142.11) 的指定非零方向在
$H^1(S_0,V_e)$ 中的像。

这个像非零必须另证，不能只引用 (1142.11)。
若 $e>1$，实际序列
$$
0\to V_1\to V_e\to V_{e-1}\to0
$$
和 $H^0(S_0,V_{e-1})=0$ 给
$H^1(S_0,V_1)\hookrightarrow H^1(S_0,V_e)$；
$e=1$ 时则是恒等映射。
因此 (1142.32) 确实非零。
由 (1142.18)–(1142.19)，其像恰为唯一一维 socle。
经 (1142.24) 得
$$
\boxed{\quad
0\ne\widehat B_{12}\in\mathcal H,\qquad
\mathbb F_p\widehat B_{12}
 =\mathcal H[\pi]
 =\pi^{e-1}\mathcal H.
\quad}
\tag{1142.33}
$$
这不选择 $\mathcal H\simeq\mathcal O/p$ 的任意生成元，也不改变原函数、
$\epsilon_2$ 或 $\zeta_p$ 的规范。

记其实际函数域像为
$B_{12}=\{F_{\chi_1},\beta_{\chi_2}\}$。由 §5，
$$
\boxed{\quad
B_{12}\ne0\ \Longleftrightarrow\ d=0,\qquad
B_{12}=0\ \Longleftrightarrow\ d=1.
\quad}
\tag{1142.34}
$$
在第二种情形，$\widehat B_{12}$ 仍然非零，而是一个非零的 Picard Kummer 类。
这准确说明 R1141 为何必须允许其一维方向在 Brauer 商中变成零。

## 7. 对原杯积及高 cochain 的准确界限

(1142.25)–(1142.34) 只使用 (1142.1)，不使用混合门。
若另外 $p\nmid B_{16}B_{p-15}$，R1141 给出的函数域关系仍是
$$
\{F_{\chi_1},F_{\chi_2}\}
 =c_p B_{12}.
\tag{1142.35}
$$
当 $d=0$ 时，$B_{12}\ne0$，所以此式的 $c_p$ 唯一；
其实际数值仍未求出。
当 $d=1$ 时，$B_{12}=0$，故此门内原函数域杯积也为零，
但这仍不证明原 proper 杯积零。

特别，不作以下任何越界：

- 原 $\widehat\beta=\kappa(F_{\chi_1})\cup\kappa(F_{\chi_2})$
  尚未证明在 proper $H^2$ 中被 $\mathfrak m$ 杀掉；
- 函数域的 Hecke 特征只说明差在 Picard 子群中，不能由此把
  $\widehat\beta$ 的 $\mathfrak m$ 部分放进 (1142.33) 的一维 socle；
- 其他 Hecke 块可能仍有 proper Picard 类，不能从函数域只剩 $I_3$
  就删除这些类；
- 常数 twist 消掉 field cup 不自动给 proper Heisenberg lift，
  更不自动给所需四阶 cover 或一般素数排点。

继续需要的具体输入是实际 $d$、实际端点倍数，以及原 proper cup 的
Picard cochain。该二分精确缩小这个任务，没有完成主课题。

## 来源与核准范围

- [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md)：
  §§2–4、§7 的原 smooth proper 模型、全部 cusp sections 及原 torsor 算术延拓。
- [R1069](R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)
  §§2–3：$\omega^{-4}$ 反射、类群消去与实际圆单位基。
- [R1131](R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)
  §§1–5：真实 DVR、自由秩二格、原 cusp 方向、奇 $K$-有理 $p^\infty$ torsion 为零。
- [R1141](R1141-original-arithmetic-endpoint-and-circular-unit-cup.md)
  §§2–6：原全部算术支撑、实际 Hecke 闭包、全球 Brauer、socle 来源与准确杯积 edge。
- J.-L. Colliot-Thélène and A. N. Skorobogatov,
  *The Brauer–Grothendieck group*, 2021；
  [作者 2019 草稿](https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf)，
  §2.2.3 的 Leray sequence、§2.5 的 relative Picard 与 section，
  Theorem 3.5.4 的 generic Brauer injectivity，
  Theorem 12.1.8 的 global invariant exact sequence；这些部分已在 R1141 工作中亲读。
- R. Sharifi, [*Iwasawa Theory*, Chapter 4](https://math.ucla.edu/~sharifi/notes/iwasawa-ch04.html)，
  Theorem 4.5.7：本文奇角色分别为 $\omega^{1-10}$、$\omega^{1-8}$，
  所用 Bernoulli 常数为 $B_{10}$、$B_8$。

全部为纸面证明，没有数学程序执行。
o2_high_coefficient 另核 (1142.18) 的真实乘 $\pi$ 分解、
Nakayama 循环性及 (1142.29) 的无挠 Picard 二分；
这条独立代数核准不替代全文其余已显示的证明。
