# R614：实际本原筛的可见射线误差与正负根号的 radical 充分条件

日期：2026-11-14。状态：**下述实际本原误差界、充分区域和素性/参数证书已证明；绝对目标仍 OPEN。**

本条接 R608 的实际角色同一化，不重新选取 `κ4` 方向，也不援引固定素数的反圆分高层定理。新步骤是把每个可见 Eisenstein 射线上的整数倍先作完整求和，再控制本原筛新增方向。它给所有 `p` 上可计算的误差式，并在 `rad((p+1)/3)` 较小时给明确统一充分条件。

## 1. 固定同一实际族

沿用 R317/R587/R608 的实际偶分支参数：

\[
p>37,\quad p\equiv2,5\pmod9,\quad
d=p^m d_0>0\text{ 立方自由},\quad (d_0,6p)=1,
\]
\[
m=1\ (p\equiv5\pmod9),\qquad
m=2\ (p\equiv2\pmod9),\qquad d\equiv\pm1\pmod9,
\]
\[
D=\operatorname{rad}(d_0),\quad
s(D)=\#\{q\mid D:q\equiv2\pmod3\}.
\tag{614.1}
\]

`K=Q(ζ)`，`ζ²+ζ+1=0`。写

\[
p+1=3M,\quad (M,3)=1,\quad2\mid M,
\quad R=\operatorname{rad}(M),\quad
\mathcal O=\{o:o\mid R,\ o>2\},
\quad J=|\mathcal O|=2^{\omega(M)}-2.
\tag{614.2}
\]

这里的 `R` 是正整数 radical，不是先前局部曲线上的有理核。另记

\[
\mathcal L=1+\log D,\quad r=p/D,
\quad c=\frac\pi{3\sqrt3},\quad t=\frac c{pD},
\quad S=\prod_{q\mid2pD}(1+1/q).
\tag{614.3}
\]

R608 已按 primary 生成元 `α≡1 mod3` 证明

\[
g_{\theta,d}
 =\operatorname{AI}_{K/\mathbb Q}(\Psi\theta\kappa_4\kappa_d^{-1})
 =\operatorname{AI}_{K/\mathbb Q}(\lambda_0\nu),
\tag{614.4}
\]

其中

\[
\lambda_0((\alpha))=\alpha\kappa_4((\alpha))
                              \kappa_{d_0}((\alpha))^{-1}.
\]

本原 `θ` 恰对应导子 `p`、群阶 `M` 的全部本原环类角色 `ν`；完整 `Θ_p` 恰对应这个循环群中的全部奇角色。两个平均均保留**同一** `λ0`，没有把 `d0` 当成可随平均改变的变量。

设 `A_full^(1),A_prim^(1)` 分别为完整 `Θ_p` 和本原轨道的归一化 `L′(g,1)` 平均；只在 `s(D)` 偶的负根号支使用。设 `A_full^(0),A_prim^(0)` 为相应 `L(g,1)` 平均；只在 `s(D)` 奇的正根号支使用。归一化分母分别是 `M/2` 和 `φ(M)`。

## 2. 新增的方向与整数倍的精确和

对 primary `β=a+bζ≡1 mod3`，称它**可见**，若 `gcd(a,b)=1`。令 `\mathcal V` 为所有可见且范数与 `6pD` 互素的 primary 元素。每个与 `6pD` 互素的整理想的 primary 生成元 `α` 可唯一写成

\[
\alpha=\chi_{-3}(n)n\beta,
\quad n\ge1,\quad(n,6pD)=1,\quad\beta\in\mathcal V.
\tag{614.5}
\]

证明：取 `n=gcd(a_α,b_α)>0`。因为 `α≡1 mod3`，`3∤n`，将 `α/n` 再乘 `χ_{−3}(n)` 就恰好是 primary `β`。反向明显且唯一。由于有理主理想上的三次角色为一，

\[
\lambda_0((\alpha))=\chi_{-3}(n)n\lambda_0((\beta)),
\quad N\alpha=n^2N\beta,
\quad o(\alpha)=o(\beta),
\tag{614.6}
\]

其中 `o(β)=ord(β^{3(p−1)} modp)` 是 `C/μ3` 中的阶。

完整奇角色平均的核，在阶一元上为 `1`，阶二元上为 `−1`，其他元素上为零。本原核为 `μ(o)/φ(o)`。所以二者在 `o=1,2` **完全相同**，只在 `\mathcal O` 中的平方自由阶上有差。这里既没有把完整奇角色平均误换为所有角色平均，也没有删去 `κ_p` 以外的实际三次特征。

定义两个真实倍数核

\[
G_L(u)=\sum_{(n,L)=1}\frac{\chi_{-3}(n)}n E_1(un^2),
\qquad
F_L(u)=\sum_{(n,L)=1}\frac{\chi_{-3}(n)}n e^{-un^2}.
\tag{614.7}
\]

由 (614.5)–(614.6) 及各自准确 AFE，得绝对收敛的等式

\[
\boxed{A_{\rm prim}^{(1)}-A_{\rm full}^{(1)}
 =2\sum_{o\in\mathcal O}\frac{\mu(o)}{\varphi(o)}
  \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
  \frac{\lambda_0((\beta))}{N\beta}
  G_{2pD}(tN\beta),}
\tag{614.8}
\]

\[
\boxed{A_{\rm prim}^{(0)}-A_{\rm full}^{(0)}
 =2\sum_{o\in\mathcal O}\frac{\mu(o)}{\varphi(o)}
  \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
  \frac{\lambda_0((\beta))}{N\beta}
  F_{2pD}(tN\beta).}
\tag{614.9}
\]

在证明误差之前，整数倍中的符号已经完整保留在 `G` 或 `F` 中。直接对原二维格点逐项取绝对值，会丢失这一结构。

`χ_{−3}` 的部分和始终为 `0` 或 `1`。对正递减函数作 Abel 求和，得

\[
0<G_1(u)\le E_1(u),\qquad
0<F_1(u)\le e^{-u}.
\]

对 `2pD` 的全部素因子包含排除，遂有

\[
\boxed{|G_{2pD}(u)|\le S E_1(u),\qquad
       |F_{2pD}(u)|\le S e^{-u}.}
\tag{614.10}
\]

又因 `D` 奇且不含 `p`，

\[
S=\frac32(1+1/p)\sum_{e\mid D}\frac1e
 \le\frac{63}{41}(1+\log D)<2\mathcal L.
\tag{614.11}
\]

这一步只用平方自由的 `D`，不把 split Euler 因子的损失当常数。

## 3. 本原方向的长度下界：偶阶可用半次迹

对 `o∈\mathcal O`，定义

\[
H_o=
\begin{cases}
(\sqrt3p/2)^{1/o},&o\text{ 奇},\\
(p/2)^{2/o},&o\text{ 偶}.
\end{cases}
\tag{614.12}
\]

**引理 614.1。** 若 `β∈\mathcal V` 且 `o(β)=o>2`，则 `|β|≥H_o`。

**证明。** 模 `p` 时 Frobenius 是复共轭，故令 `h=\barβ/β=β^{p−1}`。其像在 norm-one 群模 `μ3` 后阶为 `o`。

若 `o` 奇，`h^o∈μ3`，写作 `ζ^j`。选单位 `u∈μ6` 满足 `u/\bar u=u²=ζ^j`，则

\[
T_-=u\beta^o-\bar u\bar\beta^o
\]

在 `O_K` 中被 `p` 整除，且是某个整数乘 `√−3`。若它不为零，就有 `|T_-|≥√3p`；另一方面 `|T_-|≤2|β|^o`，给奇数情形。

若 `o` 偶，`h^{o/2}` 在 quotient 中是唯一二阶元，因此 `h^{o/2}∈−μ3`。写作 `−ζ^j`，仍选 `u²=ζ^j`，则

\[
T_+=u\beta^{o/2}+\bar u\bar\beta^{o/2}
\]

是被 `p` 整除的有理整数。非零时 `p≤|T_+|≤2|β|^{o/2}`，给偶数情形。

两种迹都不会为零：否则 `β/\barβ` 的一个正整数幂是根单位，所以 `β/\barβ` 本身是 `K` 中的根单位，即在 `μ6` 中。若它属于 `μ3`，乘单位后 `β` 为有理整数；可见性迫它为单位，primary 规范迫 `β=1`，其 quotient 阶是一。若它属于 `−μ3`，乘单位后 `β` 为纯虚 Eisenstein 整数，即整数乘 `√−3`；其范数被 `3` 整除，与 `\mathcal V` 矛盾。证毕。

因为 `R` 偶，任一奇的 `o|R` 至多是 `R/2`，偶的 `o|R` 至多是 `R`。因此有共同下界

\[
\boxed{H_o\ge H:=(p/2)^{2/R}\quad(o\in\mathcal O).}
\tag{614.13}
\]

这个下界来自真实 Frobenius 同余。它不声称一般新增方向的范数至少 `p²/4`；R608 的范数七例子仍与本引理一致。

## 4. 每个模 p 射线上的可见点计数

把 `Z[ζ]` 嵌入复平面。模 `p` 的一个射线给指数 `p` 的格子 `Λ`，其 Euclidean covolume 为

\[
V=\frac{\sqrt3}{2}p.
\]

取最短非零向量 `u`，令 `λ=|u|`。它在 `Λ` 中 primitive，故可补成格子基 `(u,v)`；减去 `u` 的整数倍后，可令 `v` 沿 `u` 的投影在 `[−λ/2,λ/2]`。记 `v` 的垂直分量为 `h_Λ=V/λ`。由最短性，`|v|≥λ`，所以

\[
h_\Lambda\ge\frac{\sqrt3}{2}\lambda,
\qquad\lambda^2\le p.
\tag{614.14}
\]

半径 `T` 的盘内，横行 `jv+Zu` 必须有 `|j|≤T/h_Λ`，每个非零横行至多 `2T/λ+1` 个点。零横行只含至多两个在原 `Z²` 中可见的点：`nu` 可见仅可能 `n=±1`，如果 `u` 本身不可见则一个也没有。因此

\[
\#\{\beta\in\Lambda:\gcd(a_\beta,b_\beta)=1,\ |\beta|\le T\}
\le2+\frac{4T^2}{V}+\frac{2T\lambda}{V}
\]
\[
\le2+\frac8{\sqrt3}\frac{T^2}p
       +\frac4{\sqrt3}\frac T{\sqrt p}
<\boxed{4+6T^2/p}.
\tag{614.15}
\]

最后用 `2x≤1+x²` 和 `√3>5/3`。这是真正使用可见性的地方；若计入同一短向量的全部倍数，零横行不能用常数二控制。

`C/μ3` 中阶为 `o` 的元素有 `φ(o)` 个，升回 `C` 后有 `3φ(o)` 个模 `p` 射线。令

\[
B_o(T)=\frac1{\varphi(o)}
 \#\{\beta\in\mathcal V:o(\beta)=o,\ |\beta|\le T\}.
\]

由 (614.12)、(614.15)，

\[
B_o(T)=0\ (T<H_o),\qquad
B_o(T)\le3(4+6T^2/p).
\tag{614.16}
\]

这里保留 primary 与坏素数删去条件只会减少计数，不会漏掉应计的射线。

## 5. 两种核各自的完整误差

设

\[
f_1(T)=T^{-1}E_1(tT^2),\qquad
f_0(T)=T^{-1}e^{-tT^2}.
\]

二者均正且递减。由 (614.16) 作 Stieltjes 分部积分，对每个 `o∈\mathcal O` 有

\[
\frac1{\varphi(o)}\sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
f_j(|\beta|)
\le3\int_{H_o}^\infty(4+6T^2/p)(-f_j'(T))\,dT.
\tag{614.17}
\]

### 5.1 负根号的 E1 核

记 `H=H_o` 暂仅限本段。直接积分得

\[
\int_H^\infty E_1(tT^2)\,dT
=-H E_1(tH^2)+\sqrt{\pi/t}\operatorname{erfc}(\sqrt tH).
\]

因此 (614.17) 的右边等于

\[
3\left[\left(\frac4H-\frac{6H}p\right)E_1(tH^2)
 +\frac{12}p\sqrt{\pi/t}\operatorname{erfc}(\sqrt tH)\right]
\le3\left[\frac4H E_1(tH^2)+\frac{12}p\sqrt{\pi/t}\right].
\tag{614.18}
\]

将 (614.10) 及 `|λ0(β)|=|β|` 代入 (614.8)，得

\[
\boxed{|A_{\rm prim}^{(1)}-A_{\rm full}^{(1)}|
 \le E_1^{\rm rad}:=
24S\sum_{o\in\mathcal O}
 \left[\frac{E_1(tH_o^2)}{H_o}
             +3\sqrt{3\sqrt3/r}\right].}
\tag{614.19}
\]

右侧的 `E1` 是指数积分，不是新增的任意误差参数。式中 `√(π/t)/p=√(3√3/r)` 保留了准确尺度。

### 5.2 正根号的指数核

对 `f0`，(614.17) 的右边为

\[
3\left[\frac4H e^{-tH^2}+\frac{6H}p e^{-tH^2}
                    +\frac{12}p\int_H^\infty e^{-tT^2}\,dT\right].
\]

用 `H e^{−tH²}≤1/√(2et)<√(π/t)` 及高斯积分不超过 `√(π/t)/2`，得上界

\[
3\left[\frac4H e^{-tH^2}+\frac{12}p\sqrt{\pi/t}\right].
\tag{614.20}
\]

故

\[
\boxed{|A_{\rm prim}^{(0)}-A_{\rm full}^{(0)}|
 \le E_0^{\rm rad}:=
24S\sum_{o\in\mathcal O}
 \left[\frac{e^{-tH_o^2}}{H_o}
             +3\sqrt{3\sqrt3/r}\right].}
\tag{614.21}
\]

若要纯初等的充分条件，可将 `e^{−tH_o²}` 换成一。它与 (614.19) 是分别推导的两个核；没有把导数公式直接当成中心值公式。

## 6. 任意 radical 的可计算充分判据

负根号时，R608 在 `r≥40` 给

\[
A_{\rm full}^{(1)}>\mathfrak L(p,D),
\]
\[
\mathfrak L(p,D)=2cP_{2D}\left[
\log(pD/c)-29/50+
2\sum_{q\mid2D}\frac{\chi_{-3}(q)\log q}{q-\chi_{-3}(q)}
\right]-1/250.
\tag{614.22}
\]

所以 `r≥40` 且 `E1^rad≤\mathfrak L(p,D)` 即充分证明实际指定本原因子的

\[
\operatorname{rank}A_{-1,d}(\mathbb Q)=\dim A_{-1,d}=\varphi(M),
\quad\log_p\text{ 是同构}.
\tag{614.23}
\]

正根号时，R602 在

\[
r\ge40+\frac{20}{3}\log\mathcal L
\tag{614.24}
\]

给 `A_full^(0)>1/\mathcal L`。所以 (614.24) 加上 `E0^rad≤1/\mathcal L` 即充分证明

\[
\operatorname{rank}A_{-1,d}(\mathbb Q)=0.
\tag{614.25}
\]

两处从平均非零到指定实际单因子的步骤，都是 R600/R608 的本原 Galois 轨道及已证明的任意水平 Heegner 秩接口。负号用导数非零；正号用中心值非零。没有把根号单独当作算术秩结论。

式 (614.19)、(614.21) 对每一个满足 (614.1) 的参数有效，不要求 radical 预先固定。若某个充分不等式未成立，不能由此推出任何中心值消失。

## 7. 简明的固定 radical 区域

若 `J=0`，则 `M` 是二的幂，所有奇角色已本原，两个误差均为零。这正好恢复原先全族等于本原族的情形。

以下设 `J>0`，故事实上 `J≥2`。使用共同下界 `H=(p/2)^{2/R}`。

### 7.1 负根号

假设

\[
\boxed{H\ge480\mathcal L^2J,\qquad
       \sqrt r\ge720\mathcal L^2J.}
\tag{614.26}
\]

等价地，可写为

\[
\boxed{p\ge2(480\mathcal L^2J)^{R/2},\qquad
       p/D\ge(720\mathcal L^2J)^2.}
\tag{614.27}
\]

第二条件自动给 `r>40`。记

\[
B=\log r+\frac53\log D-1.
\]

R608 已给 `\mathfrak L(p,D)>12B/(11\mathcal L)−1/250`，且 `B>(5/3)\mathcal L`、`B>2`。又 `H≥1`、`t<1`，因此

\[
E_1(tH_o^2)\le E_1(t)<\log(pD)+2<\frac52B.
\tag{614.28}
\]

最后一个不等式由 `logr>3` 直接展开：
`(5/2)B−(logr+2logD+2)=(3/2)(logr−3)+(13/6)logD>0`。

用 `S<2\mathcal L`、`√(3√3)<5/2`，由 (614.19) 得

\[
E_1^{\rm rad}
 <\frac{120\mathcal LJ B}{H}
       +\frac{360\mathcal LJ}{\sqrt r}
 \le\frac B{4\mathcal L}+\frac1{2\mathcal L}
 <\frac B{2\mathcal L}.
\tag{614.29}
\]

因此

\[
\boxed{A_{\rm prim}^{(1)}
 >\frac{13B}{22\mathcal L}-\frac1{250}
 >\frac{65}{66}-\frac1{250}
 =\frac{4046}{4125}>0.}
\tag{614.30}
\]

指定真实因子的 (614.23) 成立。该证明并不要求非本原比例随 `p` 趋于零。

### 7.2 正根号

假设

\[
\boxed{H\ge192\mathcal L^2J,\qquad
       \sqrt r\ge1440\mathcal L^2J,}
\tag{614.31}
\]

即

\[
\boxed{p\ge2(192\mathcal L^2J)^{R/2},\qquad
       p/D\ge(1440\mathcal L^2J)^2.}
\tag{614.32}
\]

须先检查 R602 区域，而不能只引用其结论。由 `\mathcal L≥1`、`J≥1`，第二条件给
`r≥1440²\mathcal L^4≥40\mathcal L`。又 `log\mathcal L≤\mathcal L−1`，故

\[
40+\frac{20}{3}\log\mathcal L
 \le40+\frac{20}{3}(\mathcal L-1)
 \le40\mathcal L\le r.
\tag{614.33}
\]

所以 R602 的真实全族均值确实适用。由 (614.21)，

\[
E_0^{\rm rad}
 <\frac{48\mathcal LJ}{H}
       +\frac{360\mathcal LJ}{\sqrt r}
 \le\frac1{4\mathcal L}+\frac1{4\mathcal L}
 =\frac1{2\mathcal L}.
\tag{614.34}
\]

于是

\[
\boxed{A_{\rm prim}^{(0)}>\frac1{2\mathcal L}>0,}
\tag{614.35}
\]

从而指定真实因子的 (614.25) 成立。

这些条件可用于任何满足 (614.1) 的 `p,D`。固定 `D` 及 `R` 时，条件在 `p` 足够大后自动满足；这句话是条件不等式的性质，不声称某个形状 `p+1` 中的素数无限。

## 8. 一个同时验证两种根号区域的精确素数证书

取

\[
p=15\cdot2^{73}-1
 =141670994486089356410879.
\tag{614.36}
\]

此时 `M=5·2^{73}`、`R=10`、`J=2`。非本原比例为 `1/5`，而本条的射线误差仍能有效。

程序 `R614_radical_mean_certificate.py` 先给 `p` 的完整 Lucas `p+1` 素性证书。取 Lucas 参数 `P_L=7,Q_L=−1`，判别式 `53`，递推

\[
U_0=0,\quad U_1=1,\quad
U_{n+2}=7U_{n+1}+U_n.
\]

完整整数矩阵幂运算得到

\[
U_{p+1}\equiv0\pmod p,
\quad\gcd(2\cdot53,p)=1,
\]

| `q` | `U_{(p+1)/q} mod p` | 与 `p` 的 gcd |
|---|---:|---:|
| 2 | 32474318418204000764314 | 1 |
| 3 | 5499712679302342699383 | 1 |
| 5 | 82997583978335411958271 | 1 |

又 `p+1=2^{73}·3·5`，其完整分解已知。下面给判据的短证，避免依赖一个 probable-prime 标签。若素数 `ℓ|p`，二次多项式 `X²−7X−1` 在 `Fℓ²` 中有不同的非零根 `α,β`。`U_n=0 modℓ` 当且仅当 `(α/β)^n=1`。由上面终端等式及三个 gcd，`α/β` 的阶必须恰为 `p+1`。若二次式在 `Fℓ` 分裂，该阶除 `ℓ−1`；否则 Frobenius 交换两根，该阶除 `ℓ+1`。所以 `p+1≤ℓ+1`，即 `ℓ≥p`。这迫使 `p` 本身为素数。

在同一素数下取两组参数：

| 分支 | `d0` | `d` | `D` | `s(D)` | `d mod9` |
|---|---:|---|---:|---:|---:|
| 负根号 | 169 | `169p²` | 13 | 0 | 1 |
| 正根号 | 65 | `65p²` | 65 | 1 | 8 |

`p≡2 mod9`，所以两行都使用原分支规定的 `m=2`。`13≡1 mod12`，额外支撑并未被 R604 的缺少 split 支撑结论排除。这些参数仅用于证明同一实际族的解析/秩结论，未宣称对应原有理候选存在。

全部解析条件只需有理上界：

\[
\log13<13/5,\quad1+\log13<18/5,
\qquad
\log65<21/5,\quad1+\log65<26/5.
\tag{614.37}
\]

程序分别用 `exp(13/5)` 和 `exp(21/5)` 的 `k=0,…,12` 正 Taylor 部分和严格大于 `13` 和 `65` 来证 (614.37)，不调用浮点对数。然后直接检查：

| 分支 | 所需 `H` 的有理上界 | 所需 `√(p/D)` 的有理上界 |
|---|---:|---:|
| 负根号 | `62208/5` | `93312/5` |
| 正根号 | `259584/25` | `389376/5` |

因 `R/2=5`，只须比较 `p/2` 与第二列的五次幂，以及 `p/D` 与第三列的平方。四个差均为严格正的有理数，完整数值保存在 `R614-radical-mean-certificate.json`。

因此同一实际指定本原因子分别满足

\[
\dim A_{-1,169p^2}=\operatorname{rank}A_{-1,169p^2}(\mathbb Q)
 =\varphi(5\cdot2^{73})=2^{74},\quad\log_p\text{ 为同构};
\tag{614.38}
\]

\[
\dim A_{-1,65p^2}=2^{74},\qquad
\operatorname{rank}A_{-1,65p^2}(\mathbb Q)=0.
\tag{614.39}
\]

程序并没有枚举这个大素数的挠点、Fourier 系数或全部 `L` 值；这里的非消失来自已证明的统一误差式，有限证书只证明素性及充分不等式的准确输入。

## 9. 正号结论在原 Xd/c0 图式中的准确作用

R593 §2 的 (593R.4)–(593R.5) 已证明实际 `μ3` 保持的 CM 项链给 `c_base∈Y(Q)`，在规范化 `v=db³` 上的唯一 `b=0` 点是

\[
c_{0,d}\in X_d(\mathbb Q),\qquad
j_d(P)=q_d[P-c_{0,d}],\qquad j_d(c_{0,d})=0.
\tag{614.40}
\]

R597 的 (597.8) 保持同一个 `Y` 点，送 `c0,d` 到 `c0`；(597.17) 以相同的有理 Abel 基点定义真正的曲线到实际商的映射。因此一旦 (614.25) 成立，任何真实 `P∈Xd(Q)` 都满足 `j_d(P)∈A_{−1,d}(Q)_tors`，其**从这个 c0,d 出发**的实际阿贝尔对数为零。不需要、也没有默删一个非有理基点常数。

这可给 R603 的秩零入口；仍需同一 `c0` 局部盘上的实际系数与尾界。负号 (614.23) 只提供 R593/R596 真正二次高度路线的秩和对数输入，不能取代该高度关系，也不能推出有理点零像。本文没有在 (614.36) 上计算或宣称 `M0` 单位。

一般 radical 较大或 `D` 相对 `p` 较大的范围仍可能不满足本条条件；上述解析结果没有覆盖所有实际候选。继续研究的对象是这些新方向的真实带符号和及同一全局—局部接口。

### 配套文件

- `scripts/R614_radical_mean_certificate.py`：完整 Lucas 素性及有理充分条件核查程序。
- `notes/R614-radical-mean-certificate.json`：本次已实际执行的精确证书。
- `notes/R614-agent-visible-ray-manifest.json`：代理冻结记录及范围。
- `notes/R614-handoff-manifest.json`：实际发布字节和 root 核查。

复现时把程序复制至新临时目录后运行；它在自身目录输出证书。此次只核对保存的实际证书、代码和完整证明，不为了调整发布路径再运行数学计算。
