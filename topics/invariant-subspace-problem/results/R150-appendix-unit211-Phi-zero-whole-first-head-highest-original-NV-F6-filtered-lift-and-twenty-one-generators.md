# Phi 整首头图：完整原 NV/F6 的最高行、七次滤过关系与二十一生成表示

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 本次已成结果

在[完整 H1 排除](R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md)后的当前 $\Phi=0,D\ne0$ 原余图，第一原二次头已可合法倒置。保持原三生成元

$$
v=(1,T,z)^{\mathsf T},\qquad z=Qt.
$$

本次加入同一完整原 $N_V,F_6$ 的最高总次数行，与原 N1 一起实际返回一个权多项式 C 和真实原关系

$$
\boxed{C\lambda^7=a_0(\lambda)+a_1(\lambda)T+a_2(\lambda)z\pmod I,}
\tag{1}
$$

其中

$$
\deg_\lambda a_0\le6,\qquad
\deg_\lambda a_1,\deg_\lambda a_2\le5.
\tag{2}
$$

$I$ 是同一原三均值、N1、完整 $F_6,N_V$ 生成的必要理想；全过程保持这些原来源。

实际 C 的分次为 $(78,52)$、2611 项。仅剥实际已付的 $Q$ 和 $(Q\ell)^2$ 以及非零有理常数，得到

$$
C=U C_*,\quad U\text{ 为已付原权单位},\qquad
(\deg_u C_*,\deg_Q C_*)=(74,49),
$$

$C_*$ 共 2403 项。

因此，在 $C_*\ne0$ 的完整权图上：

- 原物理 $\lambda$ 满足一个真正首一的 21 次多项式；
- 原必要代数在权环上由至多 **21** 个元素生成；
- 每个固定权点的 $(\lambda,T,z)$ 必要纤维长度至多 21，因而不同点数也至多 21。

没有假设原三生成元自由。$C_*=0$ 的全部权曲线仍保留；**$C_*=0$ 不是本稿给出的原解必要条件**，它是本次有限表示的例外权集合。整 Phi 余图没有在此排空。

## 2. 真原规则与最高次函子

在已付权环 A 中，原三均值给

$$
M_Tv\equiv Tv,\qquad M_zv\equiv zv\pmod{I_{\rm mean}}.
\tag{3}
$$

给三个基元素权 $d=(0,1,1)$，给 $\lambda,T,z$ 权 1。完整原矩阵系数的实际次数上界为

$$
\deg_\lambda(M_T)_{ij},\deg_\lambda(M_z)_{ij}\le1+d_i-d_j.
\tag{4}
$$

从 (4) 的精确最高系数构造 $\overline M_T,\overline M_z$。对次数至多 q 的原行 r，定义

$$
\operatorname{top}_q(r)_j=[\lambda^{q-d_j}]r_j.
$$

权分母都与 $\lambda$ 无关，因此逐项乘法给

$$
\operatorname{top}_{q+1}(rM_T)
 =\operatorname{top}_q(r)\overline M_T,
\qquad
\operatorname{top}_{q+1}(rM_z)
 =\operatorname{top}_q(r)\overline M_z.
\tag{5}
$$

本次源实际检查全部矩阵上界，并把两条真实原歧义行的最高部分与 $\overline M_T\overline M_z-\overline M_z\overline M_T$ 逐系数比较。

这里是在原完整多项式中取最高总次数；不是把其完整表达式直接取 $\lambda=1$。最高部分相消时也保原次数上界，不把尚未计算的下一阶冒称为最高阶。

对最高单项式 $t^as^b$，固定使用 $e_0\overline M_T^a\overline M_z^b$。由 (3) 归纳可知，相应完整行与 $T^az^b$ 的差在原均值理想内；不要求两个矩阵在自由三维模中先验交换。

## 3. 完整 NV/F6 输入及实际最高返回

原变量保持

$$
\begin{gathered}
m=u-\ell,\quad\delta=1-Q,\quad
M=\ell(2u-\ell Q)-u^2,\quad bc=M/(4\delta),\\
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell T A_2+2T^3,\\
s_n=\ell B_3-A_2T,\quad z_n=TB_3-A_2^2,\quad
Z=u s_n-2TD,\quad S=s_n+(3-2\lambda)D,\\
G=\lambda P_{02}+(u-1)T_0,\quad
f=\bigl(GT_0-QP_{02}(\ell+T)\bigr)/P_f,\quad
w=\lambda-1-T.
\end{gathered}
$$

使用的完整原多项式是

$$
F_6=MK^2-4m^2D^3,
$$

$$
N_{F,4}=4m\bigl((3-4\lambda)QD^2-Jz_nD\bigr)+2S(-2uQK+JZ),
$$

$$
\begin{aligned}
N_{C,4}={}&4mGz_nD-2GSZ-QT_0SK\\
&+4mQwu(3-2\lambda)D^2+2mQwu s_nD-2Qw(u-\ell Q)KD,
\end{aligned}
$$

$$
N_V=N_{F,4}f+N_{C,4}+2bcSZz.
\tag{6}
$$

这是原完整 $N(V)$ 的已付清分母形式，没有解 $S,Z$ 或 D 的逆。$F_6,N_V$ 的总次数上界分别为 6、7。

写

$$
D_2=2\ell-t^2,\quad K_3=4\ell^2-6\ell t+2t^3,\quad
S_3=2t(t-1),\quad Z_3=u(4\ell-2t)-2tD_2,
$$

$$
f_1=P_{02}(T_0-Qt)/P_f.
$$

源实际核回

$$
\overline F_6=MK_3^2-4m^2D_2^3,
$$

$$
\begin{aligned}
\overline N_V={}&
\bigl[-4mJ(4t-4)D_2+2S_3(-2uQK_3+JZ_3)\bigr]f_1\\
&+4mP_{02}(4t-4)D_2-2P_{02}S_3Z_3+2bcS_3Z_3s.
\end{aligned}
\tag{7}
$$

(7) 经同一真实最高规则约化为两条三系数行。加上原 N1 及两条歧义，固定五条候选的次数上界为 $7,6,2,3,3$。

实际按 NV、F6、N1 的顺序，权域秩依次为 1、2、3。最终常数行只用了这三条原行；两条歧义的最终乘子准确为零。五来源的组合始终保留，没有把泛域秩 3 当作原图排空。

## 4. 最后权分母的实际完整取消

令 $r_{NV}^{\rm top},r_{F6}^{\rm top},r_{N1}^{\rm top}$ 为第 3 节的最高行。本次在 $\mathbb Q(u,Q)$ 中实际返回

$$
e_0=\alpha_{NV}r_{NV}^{\rm top}
   +\alpha_{F6}r_{F6}^{\rm top}
   +\alpha_{N1}r_{N1}^{\rm top}.
$$

令 C 为这三个最终系数分母的最小公倍式，$\beta_i=C\alpha_i$。源逐项返回三个完整权系数身份

$$
\boxed{
Ce_0=\beta_{NV}r_{NV}^{\rm top}
    +\beta_{F6}r_{F6}^{\rm top}
    +\beta_{N1}r_{N1}^{\rm top}.
}
\tag{8}
$$

全部临时主元的零点已经由最终多项式恒等式保留。没有把任一 Gaussian 主元加入物理单位。

实际多项式资料为：

| 定义 | $u,Q$ 分次 | 项数 |
|---|---:|---:|
| C | $(78,52)$ | 2611 |
| $\beta_{NV}$ | $(69,50)$ | 2058 |
| $\beta_{F6}$ | $(66,51)$ | 1886 |
| $\beta_{N1}$ | $(69,48)$ | 2225 |
| 仅剥已付单位后的 $C_*$ | $(74,49)$ | 2403 |

C 的规范 SHA 为 `662239cc0ed91ebf8b96e4e5f5dc282db19c58963e203d3e342c64fd183c1970`；$C_*$ 的规范 SHA 为 `f2fcd6f323adaf47121341fc2e28c8af92dfba0e84dd13ed87e96f1f77081d8a`。它们由本节明确定义及源唯一再生；没有另存可重算系数载荷。

已付权表中的 $u+Q-1$ 来自[一般 LS 整 Q=1-u 排除](R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)，不是 H1-only 推论；$P_{02}=2(u-1)\ell Q$ 也是原恒等式。实际剥除仅为 Q、$Q\ell$ 两次及非零有理常数，未剥其它未知权因子。

## 5. 精确 lifting、首一 lambda 与 21 生成元

令 $r_{NV},r_{F6},r_{N1}$ 是按同一完整原矩阵约化的完整行。它们的原来源及次数上界已经由 (3)、(5)–(6) 支付。定义

$$
L=\beta_{NV}r_{NV}
  +\lambda\beta_{F6}r_{F6}
  +\lambda^5\beta_{N1}r_{N1}.
\tag{9}
$$

这是实际原理想中的行。由 (8)，最高向量正是 $C\lambda^7e_0$。以恒等定义

$$
(a_0,a_1,a_2)=C\lambda^7e_0-L
$$

便得到 (1)–(2)。原所有低次系数由 (9) 唯一定义；它们不需再次展开成巨大载荷，才能使用这一已经证明的完整原身份。

把 (1) 同时乘以 $1,T,z$，用 (3)，得到

$$
(C\lambda^7I-B)v=0\pmod I,
\qquad B=a_0I+a_1M_T+a_2M_z.
\tag{10}
$$

由 (2)、(4)，

$$
\deg B_{ij}\le6+d_i-d_j.
\tag{11}
$$

令

$$
\chi_C(\lambda)=\det(C\lambda^7I-B).
$$

乘伴随矩阵，再取 $v$ 的首坐标 $1$，可得 $\chi_C\in I\cap A[\lambda]$。每个含 B 的行列式项至少比最高项少一次 lambda，因为基权在每个置换中相消。因此

$$
\chi_C=C^3\lambda^{21}+\text{更低 lambda 次数}.
\tag{12}
$$

在 $C_*\ne0$ 图上，$C$ 是单位，$C^{-3}\chi_C$ 正是首一 21 次原 lambda 多项式。这里从未倒置 lambda，零谱值也完整保留。

还可以直接从 (10) 得到更紧凑的生成陈述：其第 i 行以 $C\lambda^7e_i$ 为首项，所有其余项按权 $d$ 严格降低。在 $C\ne0$ 图递推约化，任意 $\lambda^ne_i$ 都落在

$$
\{\lambda^je_i:0\le j<7,\ i=0,1,2\}
$$

的权环跨度内。共 21 个生成元；不再把这个数额外乘以 3，也不称这些生成元一定自由。

旧 P6 在其真实 lambda 头 $H_{19,11}\ne0$ 图仍给六次首一必要式，故该图的固定权必要纤维至多 18。两种有限图可并用；目前剩余的最高次有限性缺口至多位于完整权交集 $H_{19,11}=C_*=0$。本稿未计算这两个权多项式的 gcd 或结果式，也没有由“互素”预先排除交点。

## 6. 实际执行及继续边界

[唯一新源](../notes/2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py)与[执行前完整输入](../notes/2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.md)：

- 源 blob `999ac2498063d206315dd37a64a02a438d10d918`，12941 字节。
- SHA256 `4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41`。
- [run 46086798707](https://github.com/Rogerhu12/math-research-public/actions/runs/46086798707)，job `140798154313`，attempt 1。
- 源提交 `ecdb640dca08aca97aab5a8b5b56fc3fa49b6a4c`。
- 实际 **4.083557464 秒 / 58608 KiB / exit 0**。
- stdout 5322 字节，SHA `9a54fa97a5cadaef41da03abc5275390b47da68174ee9ecc5d19225ad9e6b75d`。
- 2026-11-28 00:14:31.069820 UTC 真实 pull 到同一源提交，两 README 未变。

新最高矩阵于 0.242 秒返回，完整 F6/NV 最高行于 0.378 秒返回，三行权秩于 3.651 秒返回，最终全部权系数组合与支持于 4.045 秒返回。没有重放旧 bb35 弱 Popov、P6/P9 D-cofactor、范数、完整 F6 大行或 Gram 门。保存只限源、定义、次数、哈希和小回执；未输出或保存可重算系数、编码或分片。

$C_*=0$ 整曲线及原个别 N/P 条件继续处理；整个 Phi 与 ordinary ISP 均尚未完成。
