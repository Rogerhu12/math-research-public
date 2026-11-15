# R164：正仿射字符的同一协变八矩乘子及权 −2 的唯一性

日期：2026-11-15。**纸面已证明。** 本稿证明 R140 的完整 action 乘子可以与正仿射字符一起严格协变；对当前真实八矩表示，进一步证明每个可行乘子本身都协变。权 $-2$ 时，可行乘子若存在就是一个由同一静态 cocycle 明确给出的单点。

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md) 和 [R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)。

没有新的研究符号计算、路径采样或 profile 评价。所得有限线性式不能代替全部真实路径不等式；其中一些兼容式已经由真实 cocycle 自动成立，不是新的独立正性障碍。

## 1. 规范化后的路径积分与同一个 cocycle

沿用有限真实算子空间、真实响应空间及成本闭锥

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad Q=U/R,
$$

$$
C=\overline{\operatorname{cone}\{V_B:M_B=T_B=0,
\ F_B=I,\ B\text{ 为同 scalar germ 的实际平端路径}\}}\subset U.
\tag{1}
$$

闭包在有限维真实函数空间中取。继续使用同一 canonical 目标、两个完整模式、同一个右锚和全部真实历史。本文的开平端路径允许不同的起止 scalar 状态和任意实际末 frame，始终满足

$$
h>0,\qquad \omega_s=\frac{k_s}{2h}.
$$

取 R130/R163 同一组八参考状态

$$
S_i^*=(1,k,d+k),\qquad d\in(0,1,-1,2),\quad k\in(0,1),
$$

以及 $M=\sum_i a_i(M)m_0(S_i^*)$ 的线性坐标。记

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*),\qquad
\mathscr L=L-\Gamma(m),\qquad m=m_0+m_2,
$$

$$
F_0(S)=L_0(S)-\Gamma(m_0(S)).
\tag{2}
$$

全部矩阵层都使用同一 $\Gamma$，特别保留 $-\Gamma(m_2)$。R163 通过完整正规式及零端势证明，对每条实际开平端 B，$\int_B\mathscr L\,ds\in U$。令

$$
\mathcal I(B)=\left[\int_B\mathscr L\,ds\right]\in Q.
\tag{3}
$$

设 $\lambda\in U^*$ 是真实正仿射字符：

$$
\lambda\in C^*,\qquad
\lambda\mathsf P_{H,d}=H^\sigma\lambda
\quad(H>0,\ d\in\mathbb R).
\tag{4}
$$

R127 保证：若闭锥仍为真子锥，某个非零此类字符存在，且 $\sigma$ 是整数；R145 进一步将非零正字符限制为偶整数权。由真实 lineality，$\lambda(R)=0$，所以也把 $\lambda$ 视为 $Q^*$ 的元素。

写 $g=(H,d)$、$\chi(g)=H^\sigma>0$。真实状态作用和复合约定为

$$
gS=(Hh,k,(\omega+d)/H),\qquad
g\circ g'=(HH',d'+H'd).
\tag{5}
$$

令 $\rho_g$ 是同一二阶矩阵算子在 $E_8$ 上的真实共轭，故
$M_{gB}=\rho_gM_B$。R163 给出

$$
\mathcal I(gB)=\mathsf P_g\mathcal I(B)+\mathcal C_g(M_B),\qquad
\mathcal C_g(M)=\sum_i a_i(M)[F_0(gS_i^*)].
\tag{6}
$$

置

$$
\Lambda(B)=\lambda\mathcal I(B),\qquad c_g=\lambda\mathcal C_g\in E_8^*.
$$

于是对所有开平端路径，

$$
\boxed{\Lambda(gB)=\chi(g)\Lambda(B)+c_g(M_B).}
\tag{7}
$$

矩阵自变量始终是原路径的 $M_B$。相应 cocycle 准确为

$$
c_{g\circ g'}=c_g\circ\rho_{g'}+\chi(g)c_{g'}.
\tag{8}
$$

这里没有把一般非零 M 路径的 $\Lambda$ 误当成其完整第四 period。

## 2. R140 乘子的平移归一化与紧可行集

R140 对任意固定延拓 $\widetilde\lambda$ 给出原乘子 $\mu_{\rm raw}$，使

$$
\int_B\widetilde\lambda(L)\,ds-\mu_{\rm raw}(M_B)\ge0
\tag{9}
$$

对全部开平端 B 成立。由于 (3) 属于 U，

$$
\Lambda(B)=\int_B\widetilde\lambda(L)\,ds
-\widetilde\lambda(\Gamma(M_B)).
$$

因此正确的规范化乘子是

$$
\boxed{\mu=\mu_{\rm raw}-\widetilde\lambda\circ\Gamma.}
\tag{10}
$$

定义

$$
K_\lambda=
\{\mu\in E_8^*: \Lambda(B)-\mu(M_B)\ge0
\text{ 对每条实际开平端 }B\}.
\tag{11}
$$

(10) 证明 $K_\lambda$ 非空；(11) 本身只依赖 $\lambda$ 和固定规范化 (2)，不依赖延拓。反向从 (11) 加回 $\widetilde\lambda\Gamma$，就恢复同一 R140 条件。

**引理 1。** $K_\lambda$ 是有限维非空紧凸集。

凸性和闭性来自 (11) 是闭半空间的交。取 E8 任意固定实基 $E_1,\ldots,E_8$。R70 对每个 $j$ 给两条有限真实路径 $B_j^+,B_j^-$，准确满足

$$
M_{B_j^+}=E_j,\qquad M_{B_j^-}=-E_j.
$$

可同时指定其 scalar 常值端芽和 frame；无需指定空间位移。对任意 $\mu\in K_\lambda$，

$$
-\Lambda(B_j^-)\le\mu(E_j)\le\Lambda(B_j^+).
\tag{12}
$$

所有右端都是固定真实有限数，故八个坐标统一有界。闭且有界即紧。这里没有假设 R140 下包络的 infimum 被实际路径取到，也没有把矩阵目标的负号当作负时间。

## 3. 仿射自同构与相对体积重心

对每个 g 定义 E8 对偶空间上的仿射映射

$$
\boxed{
T_g\mu=\chi(g)^{-1}(\mu\circ\rho_g-c_g).
}
\tag{13}
$$

若 $\mu\in K_\lambda$，将 (11) 用在真实变换后的 gB，并代 (7)，得

$$
0\le\Lambda(gB)-\mu(M_{gB})
=\chi(g)\{\Lambda(B)-(T_g\mu)(M_B)\}.
$$

因为 $\chi(g)>0$，这证明 $T_gK_\lambda\subseteq K_\lambda$。逆变换
$g^{-1}=(H^{-1},-d/H)$ 也是真实允许的变换，由 (8) 给

$$
T_{g'}\circ T_g=T_{g\circ g'},\qquad
T_gK_\lambda=K_\lambda.
\tag{14}
$$

次序是反序作用；它不影响共同固定点。每个 $T_g$ 是整个 E8 对偶空间上的可逆仿射映射。

令 A 为 $K_\lambda$ 的仿射包，$d_A=\dim A$。若 $d_A=0$，K 是单点，该点已被所有 $T_g$ 固定。若 $d_A>0$，K 含一个在 A 中满维的单纯形，因而其相对 Lebesgue 体积严格正且有限。用 A 上任意固定欧氏体积定义重心

$$
\mu_*=\frac{1}{\operatorname{vol}_A K_\lambda}
\int_{K_\lambda}\mu\,d\mu.
\tag{15}
$$

它属于 K。每个 $T_g$ 将 A 和 K 双射到自身，其在 A 方向空间上的 Jacobian 为一个非零常数。换元公式及 $T_gK=K$ 证明

$$
T_g\mu_*=
\frac{1}{\operatorname{vol}_A K_\lambda}
\int_{K_\lambda}T_g\mu\,d\mu=\mu_*.
$$

具体地，$\operatorname{vol}_A(T_gK)=\operatorname{vol}_A(K)$ 先给该 Jacobian 的绝对值为 1；即使直接保留这个常数，它也在归一化重心中相消。故得到对**全部 g 同时成立**的固定式

$$
\boxed{\mu_*\circ\rho_g=\chi(g)\mu_*+c_g.}
\tag{16}
$$

这个证明不需要群平均、amenability 或实际第四成本的逆元。重心平均的是有限维可行乘子，并非平均实际几何路径。

## 4. 真实八矩表示的两个生成元

为明确方向，按 R73 固定坐标

$$
M\longleftrightarrow(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1),\qquad
t_0=p_0/4+s_1/2.
\tag{17}
$$

即

$$
M=
\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix}.
$$

其 $\Phi_M$ 中

$$
\begin{aligned}
A_1(x)&=p_0+p_1x+p_2x^2,\\
B_0(x)&=r_0+r_1x-p_0x^2/4,\\
B_1(x)&=s_0+s_1x-p_1x^2/4,\\
B_2(x)&=t_0+t_1x-p_2x^2/4.
\end{aligned}
\tag{18}
$$

在 R89 的真实 $x=H\xi+d$ 输运下，完整同右锚共轭给

$$
\begin{aligned}
\widetilde A_1(\xi)&=H^{-1}A_1(x),\\
\widetilde B_0(\xi)&=H^{-3}\{B_0(x)+dB_1(x)+d^2B_2(x)\},\\
\widetilde B_1(\xi)&=H^{-2}\{B_1(x)+2dB_2(x)\},\\
\widetilde B_2(\xi)&=H^{-1}B_2(x).
\end{aligned}
\tag{19}
$$

例如三个正右尾依次变为
$H^{-3}J_0$、$H^{-2}J_1+dH^{-3}J_0$ 和
$H^{-1}J_2^*+2dH^{-2}J_1+d^2H^{-3}J_0$。
右端同时变为 $Hr+d$，因 $H>0$ 不改变积分方向；(19) 不含额外锚常数。$A_0,A_2$ 由同一八矩关系确定，没有另留自由参数。

定义

$$
R_N=\left.\partial_d\rho_{1,d}\right|_{d=0},\qquad
R_D=\left.\partial_t\rho_{e^t,0}\right|_{t=0}.
$$

由 (18)–(19) 直接逐系数得

$$
\boxed{R_D=\operatorname{diag}(-1,0,1,-3,-2,-2,-1,0),}
\tag{20}
$$

$$
\boxed{
\begin{aligned}
R_N M=(&p_1,\ 2p_2,\ 0,\ r_1+s_0,\ s_1-p_0/2,\\
       &p_0/2+2s_1,\ 2t_1-p_1/2,\ -p_2/2).
\end{aligned}}
\tag{21}
$$

两生成元满足 $[R_D,R_N]=-R_N$。$R_N$ 降低 (20) 的权，故幂零。对标准常态 (R89 式 (10)) 求 d 导数也逐项回到 (21)，与真实状态的 $+\partial_\omega$ 方向相符。

## 5. 更强结论：每个可行乘子都协变

**定理 2。** 对当前真实八矩表示，$K_\lambda$ 的每一点都满足 (16)。其仿射方向只可能属于

$$
\mathcal E_\sigma=
\{\nu\in E_8^*: \nu R_D=\sigma\nu,\ \nu R_N=0\}.
\tag{22}
$$

证明取任意 $\mu\in K_\lambda$，置 $\nu=\mu-\mu_*$。由 (13)、(16)，

$$
T_g\mu-\mu_*=\chi(g)^{-1}\nu\rho_g\in K_\lambda-\mu_*.
\tag{23}
$$

右侧为固定紧集。只取正缩放，(20) 使第 j 坐标为
$H^{w_j-\sigma}\nu_j$。令 $H\to0$ 和 $H\to\infty$，统一有界性迫使
$\nu_j=0$，除非 $w_j=\sigma$。再取全实平移，(23) 为

$$
\nu\exp(dR_N).
$$

这是关于 d 的有限多项式；若它在整个实轴有界，每个非恒定系数都为零，特别 $\nu R_N=0$。因此 $\nu\in\mathcal E_\sigma$。
正缩放和平移生成全部正仿射群，所以
$\nu\rho_g=\chi(g)\nu$，代 (23) 得 $T_g\mu=\mu$，证毕。

这一加强用到了当前整权、幂零表示；不是任意紧凸集上的一般仿射群都逐点固定。

由 (21) 解 $\nu R_N=0$，只余

$$
\nu=a\,(p_1+4t_1)+b\,p_2
\tag{24}
$$

这两个坐标泛函，分别具有对偶权 0 和 1。故

$$
\boxed{
\mathcal E_\sigma=
\begin{cases}
\mathbb R(p_1+4t_1),&\sigma=0,\\
\mathbb R p_2,&\sigma=1,\\
\{0\},&\sigma\notin\{0,1\}.
\end{cases}}
\tag{25}
$$

特别，若 $\sigma\notin\{0,1\}$ 且 $\lambda$ 正，则 $K_\lambda$ 是一个单点。权 0、1 时，K 至多是相应仿射直线上的紧区间；没有断言该区间一定非退化。R145 排除了非零正字符的奇数权，所以正字符的实际例外只剩权 0。

## 6. 同一份状态数据给出的十六条线性式

令

$$
\mathfrak c(M)=\sum_i a_i(M)[\partial_\omega F_0(S_i^*)],
$$

$$
\mathfrak c_D(M)=\sum_i a_i(M)
[(h\partial_h-\omega\partial_\omega)F_0(S_i^*)].
\tag{26}
$$

微分 (16) 得

$$
\boxed{\mu R_N=\lambda\mathfrak c,\qquad
\mu R_D=\sigma\mu+\lambda\mathfrak c_D.}
\tag{27}
$$

$\Gamma$、参考状态和 $a_i$ 固定；(26) 不对它们再作状态微分。所有括号是实际 Q 类，$\lambda$ 杀 R 后取值无歧义。权 $\sigma$ 的 $\lambda$ 只读取 $\Pi_\sigma F_0$，所以 (26) 使用与 R163 单权头部相同的一份真权数据，不需另编相邻权。

写 $c_j=\lambda\mathfrak c(E_j)$、$d_j=\lambda\mathfrak c_D(E_j)$，并按 (17) 的八坐标表示 $\mu$。平移的八式为

$$
\begin{aligned}
c_{p_0}&=(-\mu_{r_1}+\mu_{s_0})/2,\qquad&
c_{p_1}&=\mu_{p_0}-\mu_{s_1}/2,\\
c_{p_2}&=2\mu_{p_1}-\mu_{t_1}/2,&
c_{r_0}&=0,\\
c_{r_1}&=\mu_{r_0},&c_{s_0}&=\mu_{r_0},\\
c_{s_1}&=\mu_{r_1}+2\mu_{s_0},&c_{t_1}&=2\mu_{s_1}.
\end{aligned}
\tag{28}
$$

缩放的八式为

$$
\boxed{(w_j-\sigma)\mu_j=d_j,\qquad
(w_j)=(-1,0,1,-3,-2,-2,-1,0).}
\tag{29}
$$

反过来，(27) 是 (16) 在连通正仿射群上的充分生成元条件：沿缩放和平移各自的一参数群，用 (8) 解其线性微分方程，便恢复 (16)。但这不说明解 (27) 的 $\mu$ 自动属于 $K_\lambda$；全部路径不等式仍须另外支付。

## 7. 权 −2：显式消去全部八个乘子未知量

现在取 $\sigma=-2$。由 (28)–(29)，协变乘子必须是

$$
\boxed{
\begin{aligned}
\mu_{p_0}&=d_{p_0},&
\mu_{p_1}&=d_{p_1}/2,&
\mu_{p_2}&=d_{p_2}/3,&
\mu_{r_0}&=-d_{r_0},\\
\mu_{r_1}&=(c_{s_1}-4c_{p_0})/3,&
\mu_{s_0}&=(c_{s_1}+2c_{p_0})/3,&
\mu_{s_1}&=d_{s_1},&
\mu_{t_1}&=d_{t_1}/2.
\end{aligned}}
\tag{30}
$$

所需的其余兼容条件是

$$
\begin{gathered}
d_{r_1}=d_{s_0}=0,\qquad c_{r_0}=0,\qquad
c_{r_1}=c_{s_0}=-d_{r_0},\\
c_{t_1}=2d_{s_1},\qquad
c_{p_1}=d_{p_0}-d_{s_1}/2,\qquad
c_{p_2}=d_{p_1}-d_{t_1}/4.
\end{gathered}
\tag{31}
$$

**这些兼容条件对真实权 $-2$ 仿射字符已经自动成立，不是新增的八条独立正性限制。** 说明如下。记 $D_H=(H,0)$、$T_t=(1,t)$，按 (5) 有

$$
D_H\circ T_t=T_{t/H}\circ D_H.
$$

将两边代入 (8)，先对 t 在 0 求导，再对 $H=e^s$ 在 1 求导，得到真实 Lie cocycle 身份

$$
\boxed{c\{R_D-(\sigma+1)I\}=dR_N.}
\tag{32}
$$

它不需要预先存在乘子，也不需要 $\lambda$ 非负。$\sigma=-2$ 时是
$c(R_D+I)=dR_N$。其 $p_0,s_1$ 两坐标分别给
$-d_{r_1}+d_{s_0}=0$、$d_{r_1}+2d_{s_0}=0$，迫两者皆零；其余坐标恰给 (31) 的剩余条件。

所以任一真实权 $-2$ 仿射字符，即使尚未证明正性，也有 (30) 给出的唯一协变乘子，记作 $\mu_{\rm cov}(\lambda)$。若该字符正，定理 2 进一步保证

$$
\boxed{K_\lambda=\{\mu_{\rm cov}(\lambda)\}.}
\tag{33}
$$

结合 R140，可把这一权的准确正性条件写成

$$
\boxed{
\lambda\in C^*\quad\Longleftrightarrow\quad
\Lambda(B)-\mu_{\rm cov}(\lambda)(M_B)\ge0
\quad\text{对每条实际开平端 }B.
}
\tag{34}
$$

这里已假设 $\lambda$ 是 U 上真实定义、杀 R 的权 $-2$ 仿射字符。右侧依然是全部路径条件。实际用途是消掉八个独立乘子未知量，并使不同必要测试使用同一个明确的 $\mu_{\rm cov}(\lambda)$。

若实现暂只掌握一个包含真实字符的外部坐标候选空间，(31)–(32) 可作为 sound 线性约束加入。它们在这个较大候选空间中可能有用，但不能把候选空间中新增的约束秩宣称为真实字符空间的新独立障碍。

## 8. 修正后的局部正规 action 同样严格协变

使用 $u=h_s,w=k_s,a=h_{ss},b=k_{ss}$。取满足 (16) 的同一乘子 $\mu$；特别可以取 $K_\lambda$ 的任一点，权 $-2$ 时可直接用 (30)。定义三个实正规 action 层

$$
\begin{aligned}
A_0^\lambda(S)&=\lambda F_0(S)-\mu(m_0(S)),\\
A_2^\lambda(S;u,w)&=\lambda\widehat Q_2(S;u,w)-\mu(m_2(S;u,w)),\\
A_4^\lambda(S;u,w,a,b)&=\lambda\widehat L_4(S;u,w,a,b).
\end{aligned}
\tag{35}
$$

这里将完整最高正规式记为

$$
\widehat L_4=\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+(H_1u+H_2w)(ub-wa)+\sum_{i=0}^4F_{4,i}u^iw^{4-i}.
$$

其中最后的五项速度四次式仍是 R163 的 $\widehat Q_4$，不与完整 $\widehat L_4$ 混同。$F_0,\widehat Q_2,\widehat L_4$ 使用 R163 已完成分部积分的正规式；全部端势在平端路径上为零。因此

$$
\mathcal A_\lambda(B):=\Lambda(B)-\mu(M_B)
=\int_B(A_0^\lambda+A_2^\lambda+A_4^\lambda)\,ds.
\tag{36}
$$

只用整个路径的矩阵变换、(7) 和 (16)，已经有

$$
\boxed{\mathcal A_\lambda(gB)=\chi(g)\mathcal A_\lambda(B).}
\tag{37}
$$

由此可以在不假设任意局部矩阵代表逐点协变的前提下，证明三个**已正规化** action 层逐点协变。

固定 g，对任意 scalar 轨迹作真实时长缩放 $s=\delta t$。三个 action 层的积分分别乘 $\delta,\delta^{-1},\delta^{-3}$，且 (37) 对任意实际末 frame、矩阵与开端口都成立。比较这三个不同幂，得到每一层的协变差分别在全部开平端路径上积分为零。

静态层取任意状态的常路径即得到其点态式。二次层在任意 $S_*$ 取

$$
u_\varepsilon=\varepsilon U,\qquad
w_\varepsilon=\varepsilon W,\qquad
\omega_{\varepsilon,s}=\frac{\varepsilon W}{2h_\varepsilon},
$$

并以真实积分定义 $h_\varepsilon,k_\varepsilon,\omega_\varepsilon$。两端只须平，不必同状态。除以 $\varepsilon^2$，令 $(U,W)=(\alpha\psi,\beta\psi)$，其中非零光滑 $\psi$ 紧支撑，便逐项分离二次层的三个系数。最高层也可沿 R163 的正规式唯一性，依次用 $\varepsilon^2,\varepsilon^3,\varepsilon^4$ 分离加速度二次、面积型、速度四次；或者直接用 R163 已证的十个最高层协变式。故

$$
\boxed{
A_j^\lambda(gS;Hu,w,Ha,b)
=\chi(g)A_j^\lambda(S;u,w,a,b),\qquad j=0,2,4.
}
\tag{38}
$$

缺省变量在较低层省略。上述论证使用**零积分**的系数唯一性；它没有从非负积分推断原密度逐点非负，也不擅自更换一个未支付端势的 $m_2$ 代表。

把二次层写为
$A_2^\lambda=\sum_{i=0}^2 b_i^\lambda(S)u^iw^{2-i}$。
其余最高层系数为 $\lambda\bar A_{hh},\lambda\bar A_{hk},\lambda\bar A_{kk},\lambda H_1,\lambda H_2,\lambda F_{4,i}$。对十四个标量系数统一记作 $f(S)$，其对应指数 e 是

| 系数 | $A_0^\lambda$ | $b_i^\lambda$ | $\lambda\bar A_{hh}$ | $\lambda\bar A_{hk}$ | $\lambda\bar A_{kk}$ | $\lambda H_1$ | $\lambda H_2$ | $\lambda F_{4,i}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| e | 0 | i | 2 | 1 | 0 | 2 | 1 | i |

(38) 准确给出

$$
H^e f(Hh,k,(\omega+d)/H)=H^\sigma f(h,k,\omega).
$$

先取 $H=1$，得到 f 与 $\omega$ 无关；再从参考状态 $(1,k,0)$ 用 $g=(h,h\omega)$ 到达一般状态，得到

$$
\boxed{f(h,k,\omega)=h^{\sigma-e}f(1,k,0).}
\tag{39}
$$

因此所有残留 $\log h$ 项和 $\omega$ 项在作用于这个真实字符、并扣掉同一乘子后准确相消。原始 U 值系数可以有这些项；不能把 (39) 冒为未经 $\lambda$ 或未经矩阵修正的原式恒等。

## 9. 权 −2 的完整两标量函数 action

令 $r(s)=\log h(s)$；本节 r 是几何函数，不是 profile 右端。则

$$
u=e^r r',\qquad a=e^r(r''+(r')^2),\qquad
w=k',\qquad b=k''.
\tag{40}
$$

将 (39) 的十四个系数在 $(1,k,0)$ 的值分别记作
$a(k),b_0(k),b_1(k),b_2(k),A(k),B(k),C(k),H_1(k),H_2(k),q_0(k),\ldots,q_4(k)$。
它们都由同一个 $\lambda$ 和 (30) 的同一个 $\mu_{\rm cov}(\lambda)$ 给出，不能在不同项中独立选择乘子。

定义完整多项式

$$
\begin{aligned}
P_\lambda(k;x,y,z,t)={}&a(k)
+\sum_{i=0}^2 b_i(k)x^iy^{2-i}\\
&+A(k)(z+x^2)^2+B(k)(z+x^2)t+C(k)t^2\\
&+(H_1(k)x+H_2(k)y)\{xt-y(z+x^2)\}\\
&+\sum_{i=0}^4q_i(k)x^iy^{4-i}.
\end{aligned}
\tag{41}
$$

这里保留全部静态、二次、加速度、面积和四次速度项；$z+x^2$ 来自真实 $h''/h$，不能只留下 $r''$。由 (35)、(39)–(40)，在权 $-2$ 时有准确恒等

$$
\boxed{
\mathcal A_\lambda(B)
=\int_B e^{-2r(s)}
P_\lambda(k(s);r',k',r'',k'')\,ds.
}
\tag{42}
$$

反过来，任意有限区间上两端为常值 germs 的光滑实函数 r、k，都给真实水平 scalar 路径：

$$
h=e^r>0,\qquad
\omega(s)=\omega(s_0)+\frac12
\int_{s_0}^s e^{-r(t)}k'(t)\,dt.
\tag{43}
$$

所得 $\omega$ 同样两端平，frame 按原真实 ODE 演化；其末值不需要预设，因为 R140 已允许全部开端口和末 frame。取定有限路径后，可选择其共同物理支。故对真实权 $-2$ 仿射字符，(34) 等价于

$$
\boxed{
\int e^{-2r}P_\lambda(k;r',k',r'',k'')\,ds\ge0
\quad\text{对任意有限时间的光滑平端 }r,k.
}
\tag{44}
$$

这是完整全路径正性任务的准确重写，不是 $P_\lambda\ge0$ 的逐点要求。它也不把时长层、面积项或不同转向段的贡献分开赋予非负性。固定轴 sharp/Sturm 条件只是 (44) 的必要子测试；目前没有由这些子测试得出 (44) 已解的结论。

## 10. 八个参考状态进一步把乘子缩到两个静态值

本节是上述完整规范化的直接推论；不作新的原式编译或研究数值计算。
仍取任意真实权 $-2$ 仿射字符，不额外假设它已为正。由第 7–8 节，
其唯一协变乘子存在，且

$$
\lambda(F_0(h,k,\omega))-\mu m_0(h,k,\omega)=h^{-2}a(k).
\tag{45}
$$

R163 使用的八个实际参考状态为

$$
h=1,\qquad k\in\{0,1\},\qquad d=\omega-k\in\{0,1,-1,2\}.
\tag{46}
$$

它们满足原函数恒等 $F_0(S_i^*)=0$，不是只在某个 profile 上为零。因此对每个固定 $k=0,1$，$\mu m_0(1,k,d+k)$ 在四个不同 d 上都等于 $-a(k)$。
使用 [R73 的原八矩公式](R73-pointwise-eight-matrix-and-local-third-bridge.md)，在 $k=0$ 上准确得到

$$
\mu m_0=-\frac18\bigl[
\mu_{r_0}d^3+(\mu_{r_1}+2\mu_{s_0})d^2
+(\mu_{r_0}+2\mu_{s_1})d+\mu_{r_1}+\mu_{t_1}\bigr].
\tag{47}
$$

三次多项式在四个不同点等于同一常数，故

$$
\mu_{r_0}=\mu_{s_1}=0,\qquad \mu_{r_1}+2\mu_{s_0}=0.
\tag{48}
$$

再在 $k=1$ 代入 $\mu_{r_0}=\mu_{s_1}=0$，得到另一个三次多项式

$$
\mu m_0=\frac{\mu_{r_1}+\mu_{s_0}}4d^3
-\frac{\mu_{p_0}}2d^2
+\left[-\mu_{p_1}+\frac{\mu_{r_1}-\mu_{s_0}+\mu_{t_1}}4\right]d
-\frac{\mu_{p_0}+\mu_{p_2}}2.
\tag{49}
$$

同一四点常值条件连同 (48) 迫

$$
\mu_{p_0}=\mu_{r_1}=\mu_{s_0}=0,\qquad
\mu_{p_1}=\mu_{t_1}/4.
\tag{50}
$$

令 $a_0=a(0)$、$a_1=a(1)$；这里 $a_1$ 是在 $k=1$ 的函数值，**不是** a 的一次多项式系数，也不是最高加速度族的系数。比较 (47)、(49) 的常数项便得

$$
\boxed{\mu=(0,2a_0,2a_1,0,0,0,0,8a_0)}
\tag{51}
$$

（坐标顺序仍为 $p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1$）。因此这个规范化乘子只落在
$\operatorname{span}\{p_1^*+4t_1^*,p_2^*\}$，即前文两个矩阵对偶字符方向。
直接用 (24) 的 $R_N$ 得

$$
\boxed{c=\mu R_N=0.}
\tag{52}
$$

这里是作用于真实字符之后的数值向量为零，不能将未经取字符的原 U 值 cocycle 全部删掉。
对较大的有限外部坐标系统，(48)–(52) 已由完整参考等式和修正协变推出；不能把它们重复计作新的独立正性障碍。

进一步，R73 的完整矩阵密度在包括几何二次导数层时满足

$$
p_1+4t_1=\frac12\left(k^2-1-\frac{h_s^2}{h^2}\right),
\qquad p_2=-\frac{kh}{2}.
\tag{53}
$$

所以同一个乘子的两个时长层准确为

$$
\boxed{\mu m_0=a_0(k^2-1)-a_1kh,\qquad
\mu m_2=-a_0(h_s/h)^2.}
\tag{54}
$$

特别地，未扣矩阵项的低阶正规系数可写成

$$
\lambda F_0=h^{-2}a(k)+a_0(k^2-1)-a_1kh,
\tag{55}
$$

$$
\lambda Q2_0=h^{-2}b_0(k),\quad
\lambda Q2_1=h^{-3}b_1(k),\quad
\lambda Q2_2=h^{-4}b_2(k)-a_0h^{-2}.
\tag{56}
$$

这既保留了原八矩规范化的低阶修正，也显示对这个真实字符，十四族的平移参考修正数值都为零。若该字符为正，任意常态路径还给 $a(k)\ge0$，从而 $a_0,a_1\ge0$；本节本身没有证明其他成本系数非负或全路径 action 已非负。

## 11. 作用范围

所有群作用、紧集和字符在 R127 的 universal 真实函数空间上定义。每次使用有限组实际路径、补偿和参数紧族时，先固定它们，再选择共同物理支与右锚区间；不声称一个任意预设的窄 I 或固定控制盒容纳全部正仿射群。有限维乘子的重心及有界轨道论证不要求构造一个包含无穷多几何路径的共同带。

本稿的结论是：正字符的 R140 乘子全部协变；对权 $-2$，它由 (30) 唯一确定，完整正性等价于保留全部层的 (44)。没有证明该权存在或不存在非零正字符，没有把闭成本锥变成实际成本半群，也没有支付完整第四 period/ruling、高阶收敛或主课题的闭嵌入与 reach 条件。
