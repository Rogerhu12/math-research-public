# R125：九级固定曲线的显式实乘法及实际五进全局高度

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明，附标准库精确证书。** 延续 [R120](R120-nine-cartan-twist-and-explicit-cubic-cover.md) 和 [R124](R124-nine-twist-exact-rank-two-and-five-adic-logarithms.md)，本文给出固定亏格二曲线的一个明确 $(3,3)$ 同源、实际三次同源实现的 $\sqrt3$ 作用，以及一个明确各向同性微分补空间所对应的 Coleman–Gross 全局高度。

在 R120 的椭圆点 $P_H,P_2$ 上，高度矩阵是
$$
\boxed{H_E\equiv
\begin{pmatrix}275&270\\270&10\end{pmatrix}\pmod{5^5}.}
\tag{125.1}
$$
这里高度使用 $K=\mathbb Q(\sqrt{-3})$ 上的全局迹对数，且微分补空间在下面准确指定。没有把未计算的 unit-root 补空间代入，也没有把数值近似称为零点或有理点分类。全局高度矩阵非退化；完整二次 Chabauty 尚需曲线上局部高度函数、坏素数高度值集合和共同零点的证明。

## 1. 固定模型及两个互补三次覆盖

写 $w^2=-3$，$K=\mathbb Q(w)$，并令
$$
\begin{aligned}
S(x)&=7x^6+12x^5-36x^4-10x^3+84x^2-72x+19,\\
\mathcal C&:y^2=S(x),\qquad J=\operatorname{Jac}\mathcal C,\\
E&:V^2=U^3+AU+B,\\
A&=-\frac{21+27w}{2},\qquad B=28w-10.
\end{aligned}
$$
所有横线上标表示 $K/\mathbb Q$ 的共轭。沿用 R120 的三次覆盖 $\phi:\mathcal C_K\to E$，设
$$
r=\frac{1-w}{2},\qquad
f=x^3+\frac{6-3w}{7}x^2-\frac{45+9w}{14}x+\frac{17+9w}{14},
$$
$$
P=(x-r)^2(x+1),\quad \gamma=\frac{9-w}{14},\qquad
H=\frac{6-10w}{7}x^3-\frac{36+24w}{7}x^2+\frac{20w-12}{7}.
$$
则
$$
\phi(x,y)=\left(w+2+\gamma\frac P f,
                 \frac{\gamma yH}{3f^2}\right),\qquad
\phi^*\omega=\frac32(x-r)\frac{dx}{y},
\quad\omega=\frac{dU}{2V}.
\tag{125.2}
$$
R120 的系数恒等式证明这是实际映射，而不是只在几个点上匹配。

令 $\omega_0=dx/y$、$\omega_1=x\,dx/y$。在 $K(U)$ 上，$x$ 满足
$$Q(x)=(U-w-2)f(x)-\gamma P(x)=0.$$
因为 $P(r)=P'(r)=0$，有
$$
\operatorname{Tr}\frac1{x-r}=-\frac{Q'(r)}{Q(r)}
=-\frac{f'(r)}{f(r)}=-w.
$$
由 (125.2) 的微分迹得到
$$
\phi_*\omega_0=-\frac{2w}{3}\omega,
\qquad \phi_*\omega_1=\frac23(3-rw)\omega.
$$
因此 $\Omega=\phi^*\phi_*$ 在微分系数列向量上的矩阵是
$$
\Omega^*=\begin{pmatrix}(3+w)/2&w\\-w&(3-w)/2\end{pmatrix},
\qquad \Omega+\bar\Omega=[3].
\tag{125.3}
$$
最后一式先在微分上成立，再由特征零时同态到 Lie 代数作用的单射性得到实际 Jacobian 同态恒等式。同样可直接计算 $\phi_*\bar\phi^*=0$。故
$$
\Phi=(\phi_*,\bar\phi_*):J_K\longrightarrow E\times\bar E
$$
满足
$$
\Phi\Phi^\vee=\operatorname{diag}([3],[3]),\qquad
\Phi^\vee\Phi=[3],\qquad \deg\Phi=9.
\tag{125.4}
$$
这里对偶取各自的典范主极化。特别地
$$\Phi^*\lambda_{E\times\bar E}=3\lambda_J.$$
共轭交换两个覆盖，故 $\Phi$ 下降为 $J\to\operatorname{Res}_{K/\mathbb Q}E$ 的有理同源。

## 2. 明确三次同源与有理实乘法

设
$$
h=\frac{3(1+w)}2,\qquad v_0^2=8-8w,
\qquad t_0=3h^2+A,\qquad u=\frac{3-w}2.
$$
精确核验
$$h^3+Ah+B=v_0^2,\qquad
3h^4+6Ah^2+12Bh-A^2=0.$$
故横坐标为 $h$ 的两个非零点与原点组成 Galois 稳定的三阶子群。令 $z=U-h$。Vélu 公式给实际同源
$$
\boxed{
\mu:E\longrightarrow\bar E,\qquad
\begin{cases}
U\longmapsto u^{-2}\left(U+\dfrac{2t_0}{z}+\dfrac{4v_0^2}{z^2}\right),\\[4pt]
V\longmapsto u^{-3}V\left(1-\dfrac{2t_0}{z^2}-\dfrac{8v_0^2}{z^3}\right).
\end{cases}}
\tag{125.5}
$$
程序清去 $z^6$ 分母，逐系数核验像点满足 $\bar E$ 方程；并核验导数恒等式
$$\mu^*\bar\omega=u\omega.$$
由于 $u\bar u=3$，$\bar\mu\mu$ 的微分与 $[3]$ 相同，因而
$$\bar\mu\mu=[3],\qquad \bar\mu=\mu^\vee.$$

在乘积上定义
$$T_E(P,Q)=(\bar\mu Q,\mu P).$$
它满足 $T_E^2=[3]$，并对乘积主极化自伴。因其与共轭交换作用相容，
$$
T=\frac13\Phi^\vee T_E\Phi\in\operatorname{End}^0_{\mathbb Q}(J)
\tag{125.6}
$$
也是有理自伴的，$T^2=[3]$。在 $(\omega_0,\omega_1)$ 的系数列向量约定下，
$$
\boxed{T^*=\begin{pmatrix}-2&-1\\1&2\end{pmatrix}.}
\tag{125.7}
$$
这给出了 R124 实乘法的实际实现，且 $(3T)=\Phi^\vee T_E\Phi$ 是整同态。本文只对 $T$ 声称有理同态；没有仅因 (125.7) 的系数整便宣称 $T\in\operatorname{End}(J)$。

### 2.1 在已知 Mordell–Weil 点上的作用

令
$$P_H=\left(\frac{7-w}{2},4w-4\right),\qquad
P_2=\left(\frac{1+w}{2},2w+4\right).$$
从 (125.5) 和椭圆群法直接计算
$$
\begin{aligned}
\overline{\mu(P_H)}&=
\left(\frac{13+5w}{6},\frac89w\right)=-P_H-P_2,\\
\overline{\mu(P_2)}&=
\left(\frac{31+15w}{6},6+\frac{64}9w\right)=-2P_H+P_2.
\end{aligned}
\tag{125.8}
$$
程序以精确有理数验证两式，也验证再次作用等于乘三。

R120 的两个有理除子
$$D_1=[(-1,12)-(-1,-12)],\qquad D_2=[(1,2)-(-1,12)]$$
满足 $\phi_*D_1=4P_H$、$\phi_*D_2=P_2-2P_H$。在 $J(\mathbb Q)\otimes\mathbb Q$ 中，因 $\phi_*$ 单射，得到
$$
[T]_{D_1,D_2}=\begin{pmatrix}-3&3/2\\-4&3\end{pmatrix}.
\tag{125.9}
$$
单射也可从 (125.4) 看出：有理点的一分量为零时其共轭分量同为零，故该点是三挠；张量 $\mathbb Q$ 即消失。这里不需要先证明 $D_1,D_2$ 已经是完整整数格基。

## 3. 与实乘法相容的明确微分补空间

在 $E$ 上令 $\eta=U\omega$。Vélu 横坐标的表达式，以及平移在 $H^1_{\rm dR}(E)$ 上作用恒等，给出
$$
\mu^*\bar\eta=\frac{3\eta-2h\omega}{u}
=\bar u\eta-2w\omega.
\tag{125.10}
$$
具体地，Vélu 横坐标是 $U+U(P+Q)+U(P-Q)-2h$；三个 $U\omega$ 的上同调类都等于 $[\eta]$。因此 (125.10) 是上同调恒等式，不声称这些第二类微分逐点相同。

于是取
$$
\boxed{W_E=K_5\cdot(\eta-2\omega),\qquad K_5=\mathbb Q_5(w).}
\tag{125.11}
$$
它确为 $H^1_{\rm dR}(E)$ 中全纯微分的补空间，椭圆情形自动各向同性；并且
$$\mu^*(\bar\eta-2\bar\omega)=\bar u(\eta-2\omega).$$
所以 $W_E\oplus W_{\bar E}$ 既与同源相容，又对共轭稳定。经 $\Phi^*$ 得到 $J/\mathbb Q_5$ 上的各向同性补空间 $W_J$，且 $T$ 保持它。

这些是足以定义 Coleman–Gross 高度的明确数据。$W_E$ **没有**被识别成 unit-root 线；以下全部高度均使用 (125.11)。这不会妨碍自伴性和高度的同源函子性。

## 4. 高度归一化与可直接计算的公式

取 $K$ 上的循环全局 idele 对数，在唯一的五进素数处取
$$\ell_5=\operatorname{Tr}_{K_5/\mathbb Q_5}\log_5,
\qquad\log_5(5)=0,$$
其余素理想 $\mathfrak q$ 处取不分歧角色
$$\ell_{\mathfrak q}(\pi_{\mathfrak q})=-\log_5\operatorname{Norm}\mathfrak q.$$
这里没有额外除以 $5$ 或 $[K:\mathbb Q]$。

设 $R=[m]P$ 在所有坏素数处有非奇异约化，并在五进处进入形式群。写
$$t=-U(R)/V(R),\qquad z=\int_0^R\omega,$$
并令 $\mathfrak d$ 为 $U(R)$ 的平方根分母理想，即 $\operatorname{ord}_{\mathfrak q}\mathfrak d=\max(0,-\operatorname{ord}_{\mathfrak q}U(R)/2)$。

记 $\sigma_0$ 为形式 sigma 函数，按 $\sigma_0(z)=z+\cdots$ 及
$$\frac{d^2}{dz^2}\log\sigma_0=-U$$
正规化。对于 $W_E=\langle\eta+s\omega\rangle$，同一微分方程给
$$\sigma_s=\sigma_0\exp(-s z^2/2).$$
本文 $s=-2$，故 $\sigma_{-2}=\sigma_0\exp(z^2)$。Balakrishnan–Besser 的局部高度公式是 $-2\log\sigma_s$；这也可直接由其 Theorem 4.1 代入杯积对偶微分 $-(\eta+s\omega)$ 得到。取局部域迹，再加上非五进处的分母交数，得到
$$
\boxed{h_E(P)=\frac2{m^2}
\left(\log_5\operatorname{Norm}\mathfrak d
-\log_5\operatorname{Norm}t
-\operatorname{Tr}\log\frac{\sigma_0(t)}t
-\operatorname{Tr}z(t)^2\right).}
\tag{125.12}
$$
非五进处公式与 Balakrishnan–Besser Corollary 4.3 相同；在数域中每处乘剩余域次数，即合并成理想范数。这里用的是 Coleman–Gross 的自配对归一化，而非某些 sigma 文献中另除以 $-2p$ 的高度。

### 4.1 模 $5^5$ 的全部形式误差

对于 $V^2=U^3+AU+B$，参数 $t=-U/V$ 给
$$
\begin{aligned}
\omega&=(1+2At^4+3Bt^6+\cdots)dt,\\
z(t)&=t+\frac{2A}{5}t^5+\frac{3B}{7}t^7+\cdots,\\
\log\frac{\sigma_0(t)}t&=\frac{5A}{12}t^4+\frac{13B}{30}t^6+\cdots.
\end{aligned}
\tag{125.13}
$$
$A,B$ 五进整，且 $v_5(t)\ge1$，所以后两式给
$$\log(\sigma_0(t)/t)\equiv0\pmod{5^5},\qquad z(t)^2\equiv t^2\pmod{5^5}.$$
为排除截断后的隐藏分母，令 $F(t)=\omega/dt\in1+t^4\mathcal O_{K_5}[[t]]$。由 $U(t)F(t)$ 的整 Laurent 系数及两次积分，第 $t^n$ 项的可能五进分母至多有
$$\lfloor\log_5n\rfloor+\lfloor\log_5(n-1)\rfloor$$
个 $5$。对所有偶数 $n\ge8$，减去这个数后的 $n$ 至少为 $6$，并趋向无穷。$n=4,6$ 的例外已在 (125.13) 明确计算。形式对数平方的同类估计更强。因此 (125.12) 严格化为
$$
\boxed{h_E(P)\equiv\frac2{m^2}
\left(\log_5\frac{\operatorname{Norm}\mathfrak d}{\operatorname{Norm}t}
-\operatorname{Tr}(t^2)\right)\pmod{5^5}.}
\tag{125.14}
$$
这一步只要求 $5\nmid m$，并不依赖猜测高阶 sigma 系数。

## 5. 该模型的全局最小性和统一倍数 $66$

令 $\alpha=(1+w)/2$，则 $\mathcal O_K=\mathbb Z[\alpha]$、$\alpha^2-\alpha+1=0$。有
$$A=3-27\alpha,\qquad B=56\alpha-38,$$
$$\Delta=55296(w-1)=2^{12}\cdot3^3(\alpha-1).$$
在 $w\mid3$ 处 $v_w(\Delta)=6<12$，故模型最小。在 $2$ 处，先明确未扭曲曲线的好约化来源：R124 的 (124.3) 把 $\operatorname{Jac}X_{\rm ns}(9)$ 识别为层 $81$ 的新模因子，故在 $2$ 好约化；R120 的 $\mathcal C$ 是它的 $-1$ 扭曲。将 (125.4) 同时扭回，$E^{(-1)}$ 成为该好约化 Jacobian 在 $K$ 上的同源商，因此也在 $2$ 好约化。这一步可直接在奇数阶 Tate 模上用不分歧性与 Néron–Ogg–Shafarevich 判据确认。

而 $K_2/\mathbb Q_2$ 不分歧，$K_2(i)/K_2$ 分歧；再乘非平凡的分歧二次角色使 $E$ 的奇数阶 Tate 模惯性非平凡，所以 $E$ 没有好约化。如果当前整模型不最小，则判别式指数 $12$ 只能降到 $0$，将给好约化，矛盾。其余素数处判别式为单位。因此这是全局最小模型。

在 $2$ 处的特殊纤维是
$$V^2=U^3+(1+\alpha)U,$$
唯一奇异点为 $(\alpha,0)$。精确倍点公式给
$$
2P_H=(1+2\alpha,\alpha-1),\qquad
2P_2=\left(\frac{108+82\alpha}{49},\frac{412-130\alpha}{343}\right).
$$
它们分别约化为 $(1,\alpha+1)$、$(0,0)$，均非奇异。在 $w\mid3$ 处，$P_H,P_2$ 分别约化为 $(2,2)$、$(2,1)$，也非奇异。非奇异约化点组成子群，故 $2P_H,2P_2,2(P_H+P_2)$ 处处有非奇异约化。

R124 已精确计数 $\#E(\mathbb F_{25})=33$。所以
$$m=66$$
把上述三个点同时送入五进形式群，且保持处处非奇异约化。程序另外验证三点乘 $66$ 后横、纵坐标的五进赋值分别为 $-2,-3$，因此 $v_5(t)=1$。独立的 $m=132$ 计算也满足同一条件。

## 6. 无需分解巨大分子的实际证书

为精确计算 $\operatorname{Norm}\mathfrak d$，在 $\mathbb Z[\alpha]$ 使用范数
$$N(a+b\alpha)=a^2+ab+b^2.$$
把除法商的两个有理坐标分别取最近整数，余数范数至多为除数范数的 $3/4$；这是一个精确的欧几里得算法，同时证明该环是 PID。

若 $U(R)=(a+b\alpha)/D$，其中 $a,b,D$ 为整数、$D>0$，令
$$g=\gcd_{\mathbb Z[\alpha]}(a+b\alpha,D).$$
则横坐标分母理想的范数为 $D^2/N(g)$，从椭圆方程可知它是一个整数平方，故
$$\operatorname{Norm}\mathfrak d=\sqrt{D^2/N(g)}.$$
程序用整数平方根并核对平方等式；不需要分解乘 $66$ 后的大坐标。

全部输出如下；四个数值栏都取模 $3125$。

| 点 | $m$ | $N\mathfrak d$ | $\log_5(N\mathfrak d/Nt)$ | $\operatorname{Tr}(t^2)$ | $h_E$ |
|---|---:|---:|---:|---:|---:|
| $P_H$ | $66$ | $425$ | $1225$ | $2275$ | $275$ |
| $P_2$ | $66$ | $1675$ | $2705$ | $2800$ | $10$ |
| $P_H+P_2$ | $66$ | $650$ | $2950$ | $2975$ | $825$ |
| $P_H$ | $132$ | $2325$ | $1775$ | $2850$ | $275$ |

最后一行重新计算更大的有理点和分母理想，并非把第一行高度乘除某个标量。它独立复核倍点归一化。由极化恒等式
$$h_E(P_H,P_2)=\frac12\{h_E(P_H+P_2)-h_E(P_H)-h_E(P_2)\}$$
得到 (125.1)。此外
$$\det H_E\equiv1725\pmod{3125},\qquad v_5(\det H_E)=2.$$
所以此实际全局高度不退化。实乘法自伴要求
$$h_E(P_2,P_2)=2h_E(P_H,P_H)-2h_E(P_H,P_2),$$
证书核验该关系；它是与四次独立计算相容的交叉检查，没有被用来制造任何一个输入高度。

## 7. 搬回 $J(\mathbb Q)$ 的实际全局高度

在 $J/\mathbb Q$ 上取第 3 节的补空间 $W_J$，及 $\ell_5=\log_5$ 的循环对数。对 $D,E\in J(\mathbb Q)$，由 (125.4) 的极化倍数和数域基变换次数，有
$$\boxed{h_J(D,E)=\frac13h_{E/K}(\phi_*D,\phi_*E).}\tag{125.15}$$
准确地说，基变换到 $K$ 使 $J$ 的高度乘二；乘积上的两项为共轭高度，相等，故又给因子二，两者消去。剩下的 $1/3$ 来自 $\Phi^*\lambda=3\lambda_J$。

令
$$C=\begin{pmatrix}4&-2\\0&1\end{pmatrix}.$$
因此在 R124 的有限指数除子基 $(D_1,D_2)$ 中
$$
H_J\equiv\frac13 C^{\mathsf T}
\begin{pmatrix}275&270\\270&10\end{pmatrix}C
\equiv\begin{pmatrix}425&1710\\1710&10\end{pmatrix}\pmod{3125}.
\tag{125.16}
$$
证书同时输出这个矩阵和其行列式，精度没有在未声明的矩阵求逆中损失。$3$ 和 $\det C=4$ 都是五进单位，所以 $v_5(\det H_J)=2$。结合 R124 的实际对数矩阵可据此求全局二次型，但本文不把这一全局矩阵等同于曲线上局部高度函数。

## 8. 复验入口与后续边界

在仓库根运行：

```sh
python topics/serre-uniformity/notes/verify_r125_explicit_rm_heights.py --check
```

脚本只使用 Python 标准库及已发布 R120 的精确二次域/椭圆群法辅助函数；不调用浮点高度、BSD 假设、GRH 或黑箱类群计算。它核验三次同源的整个方程、微分矩阵、两个 Mordell–Weil 作用、坏素数处明确约化，并从精确大有理点重新计算全部四个高度证书。

相关文件：

- `notes/verify_r125_explicit_rm_heights.py`；
- `notes/r125_explicit_rm_heights_certificate.json`。

本结果是固定九级扭曲上的实际全局高度步骤。尚未给出全部 $\mathcal C(\mathbb Q)$、有效最大分母或原 Serre 统一性问题的完整结论。固定曲线的定性有限性与更一般的非九次幂分母支应另行区分；不能因本例已有秩二和高度矩阵便宣称主任务完成。

## 原始文献

1. J. Vélu, *Isogénies entre courbes elliptiques*, C. R. Acad. Sci. Paris Sér. A-B **273** (1971), A238–A241。本文 (125.5) 另外以完整系数恒等式核验。
2. J. S. Balakrishnan, A. Besser, *Coleman–Gross height pairings and the p-adic sigma function*, J. reine angew. Math. **698** (2015), 89–104，DOI [10.1515/crelle-2012-0095](https://doi.org/10.1515/crelle-2012-0095)；[作者稿](https://arxiv.org/pdf/1201.6016)，§2、Theorem 4.1、Corollaries 4.2–4.3。本文用 Theorem 4.1 对明确补空间的公式；不把仅对 unit-root 的 Corollary 4.2 自动套入。
3. B. Mazur, W. Stein, J. Tate, *Computation of p-adic heights and log convergence*, Documenta Math., Extra Volume Coates (2006), 577–614，DOI [10.4171/dms/4/17](https://doi.org/10.4171/dms/4/17)。其 sigma 高度的标量约定与本文 Coleman–Gross 约定不同；(125.12) 已固定本文采用的符号和因子。
