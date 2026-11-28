# Phi 整首头图：完整原 NV/F6 最高齐次行与首一 lambda 的新输入

日期：2026-11-28（Asia/Taipei）。状态：新源尚未执行，下面给出原输入与严格 lifting 判据。

## 1. 本次改变的数学输入

完整 H1 零支已排除，当前 $\Phi=0,D\ne0$ 余图的第一二次头可以合法倒置。既有三原均值提供 $v=(1,T,z)^{\mathsf T}$ 的真实规则

$$
M_Tv\equiv Tv,\qquad M_zv\equiv zv\pmod{I_{\rm mean}},
\qquad z=Qt.
\tag{1}
$$

这只是原商的三个生成元，不假设它们线性无关或原商自由。

本源的 $u+Q-1$ 单位来自[一般 LS 的整个 Q=1-u 边界排除](../results/R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)，其开头定理在整个原一般 LS、原物理不同值 admissible 范围给出 $u+Q-1\ne0$，因此包含当前 $\Phi=0,D\ne0$ 图；不是从仅 H1 的排除外推。$P_{02}=2(u-1)\ell Q$ 的单位性则来自已付原权恒等式。上述范围均不传给另一个 $D=0$ 碰撞图。

旧 bb35 在全 $\mathbb Q(u,Q)[\lambda]^3$ 弱 Popov 行消元中已于 120.073988817 秒中止，最后权分母已达 $(186,112)$。本次不重新启动该门，也不重算 P6/P9 的 D-cofactor。新输入是**原完整 NV 和 F6 的最高总次数行**，连同原 N1 与两条实际乘法歧义，只在权分式域 $\mathbb Q(u,Q)$ 做一个至多五行三列的原单位目标。

每条最后权分母均清回；若所得权支持 C 非常数，其全部零曲线继续保留。泛域常数返回本身不证明整 Phi 为空。

## 2. 最高齐次函子与真实矩阵

令 $d=(0,1,1)$，给 $\lambda,T,z$ 权 1，给 $u,Q$ 及原权有理函数权 0。既有规则的实际系数满足

$$
\deg_\lambda (M_T)_{ij},\ 
\deg_\lambda (M_z)_{ij}\le1+d_i-d_j.
\tag{2}
$$

新源逐项读取真实完整规则的最高 lambda 系数，得到 $\overline M_T,\overline M_z$。这等于把 $T=\lambda t,z=\lambda s$ 后提取最高总次，再令最高次中的 $\lambda=1$；不是把完整原式直接代入 $\lambda=1$。

对总加权次数至多 q 的三系数行 r，定义

$$
\operatorname{top}_q(r)_j=[\lambda^{q-d_j}]r_j.
\tag{3}
$$

由 (2) 直接有

$$
\operatorname{top}_{q+1}(rM_T)
 =\operatorname{top}_q(r)\overline M_T,
\quad
\operatorname{top}_{q+1}(rM_z)
 =\operatorname{top}_q(r)\overline M_z.
\tag{4}
$$

所有分母仅含权变量，所以 (4) 不引入谱分母。源码检查全部矩阵系数上界，并把完整原交换子行的 top 与两个最高矩阵的交换子逐项比较。

原 N1 余行次数至多 2，两条歧义行次数至多 3。对最高多项式 $t^as^b$，固定使用

$$
e_0\overline M_T^a\overline M_z^b
\tag{5}
$$

约化；不假设两个矩阵在自由三维模中交换。式 (1) 的真实原理想来源足以归纳证明完整相应行与原单项式的差在 $I_{\rm mean}$ 中。

## 3. 完整原 F6 与 NV 的最高部分

保持

$$
\begin{gathered}
m=u-\ell,\quad \delta=1-Q,\quad
M=\ell(2u-\ell Q)-u^2,\quad bc=M/(4\delta),\\
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3,\\
s_n=\ell B_3-A_2T,\quad z_n=TB_3-A_2^2,\\
Z=u s_n-2TD,\quad S=s_n+(3-2\lambda)D,\\
G=\lambda P_{02}+(u-1)T_0,\quad
f=\bigl(GT_0-QP_{02}(\ell+T)\bigr)/P_f,\quad
w=\lambda-1-T.
\end{gathered}
$$

本次完整原多项式为

$$
F_6=MK^2-4m^2D^3,
$$

$$
N_{F,4}
=4m\bigl((3-4\lambda)QD^2-Jz_nD\bigr)
 +2S(-2uQK+JZ),
$$

$$
\begin{aligned}
N_{C,4}={}&4mGz_nD-2GSZ-QT_0SK\\
&+4mQwu(3-2\lambda)D^2
 +2mQwu s_nD-2Qw(u-\ell Q)KD,
\end{aligned}
$$

$$
N_V=N_{F,4}f+N_{C,4}+2bcSZz.
\tag{6}
$$

它们就是此前原矩条件及完整原 $N(V)$ 清分母条件，未增加 $S,Z,D$ 的逆。上界分别是 6 与 7。

新源按加法和乘法的真实加权函子直接计算 (6) 的最高部分，不先展开整个高次有理行。若最高部分相消，仍保原次数上界，不把它静默改成更小次数。写

$$
D_2=2\ell-t^2,\quad K_3=4\ell^2-6\ell t+2t^3,
\quad S_3=2t(t-1),\quad Z_3=u(4\ell-2t)-2tD_2,
$$

$$
f_1=P_{02}(T_0-Qt)/P_f.
$$

最高完整式为

$$
\overline F_6=MK_3^2-4m^2D_2^3,
$$

$$
\begin{aligned}
\overline N_{F,4}
 &=-4mJ(4t-4)D_2+2S_3(-2uQK_3+JZ_3),\\
\overline N_{C,4}
 &=4mP_{02}(4t-4)D_2-2P_{02}S_3Z_3,\\
\overline N_V
 &=\overline N_{F,4}f_1+\overline N_{C,4}
   +2bcS_3Z_3s.
\end{aligned}
\tag{7}
$$

源把完整表达式的函子结果与 (7) 精确比较，再按 (5) 得到两个新的真实最高行。没有取某个数值权点，也没有把必要标量式替换成未知来源的裸行。

## 4. 权分母全部清回

固定输入顺序为

$$
r_{NV}^{\rm top},\ r_{F6}^{\rm top},r_{N1}^{\rm top},r_{T^2z}^{\rm top},r_{Tz^2}^{\rm top},
\qquad q_i=7,6,2,3,3.
\tag{8}
$$

每个权域行变换保存这五条原行的组合，最终必须实际返回三系数恒等式

$$
e_0=\sum_i\alpha_i r_i^{\rm top}.
$$

若该目标未返回，源只记真实剩余秩，不宣称首一 lambda 或排空。若返回，取全部最终 $\alpha_i$ 分母的最小公倍式 C，逐项返回多项式 $\beta_i=C\alpha_i$ 及

$$
Ce_0=\sum_i\beta_i r_i^{\rm top}.
\tag{9}
$$

所有中间主元零均在最终多项式身份中保全，不加入单位。只从 C 剥真正已付权因子，写 $C=U C_*$，$U$ 为原单位；$C_*=0$ 的全部权曲线仍保留。没有由多变量 gcd 等于 1 推出单位理想。

## 5. 从最高原行到精确原首一关系

令 $N=\max\{q_i:\beta_i\ne0\}$。对每条 (8) 使用其完整原行 $r_i(\lambda)$，定义

$$
L(\lambda)=\sum_i\beta_i\lambda^{N-q_i}r_i(\lambda).
\tag{10}
$$

(10) 是同一原理想中的真实行。由 (3)、(9)，它的最高向量为 $C\lambda^Ne_0$。因此，以恒等定义

$$
(a_0,a_1,a_2)=C\lambda^Ne_0-L(\lambda),
$$

有完整原关系

$$
\boxed{C\lambda^N=a_0(\lambda)+a_1(\lambda)T+a_2(\lambda)z\pmod I,}
\tag{11}
$$

且

$$
\deg a_0\le N-1,\qquad
\deg a_1,\deg a_2\le N-2.
\tag{12}
$$

这是由已实际返回的最高系数身份与原行 DAG 直接得到的完整多项式身份，不需要把所有低次系数再次展开成大载荷作为额外门。$\lambda=0$ 从未除去。

把同一个关系分别乘以 $1,T,z$ 并用 (1)，令

$$
B=a_0I+a_1M_T+a_2M_z.
$$

则 $(C\lambda^NI-B)v=0\pmod I$，而

$$
\deg B_{ij}\le N+d_i-d_j-1.
$$

所以

$$
\chi_C(\lambda)=\det(C\lambda^NI-B)\in I\cap A[\lambda]
$$

的真实最高项恰为

$$
C^3\lambda^{3N}.
\tag{13}
$$

任何含 B 的行列式项均至少少一次 lambda，基权在置换中完全相消。此处只使用真原点/原理想矩阵恒等式，不假设原三生成元自由。

在 $C_*$ 非零图上，(13) 可除已命名的 $C^3$ 成为原物理 lambda 首一多项式。更直接地，三条由 (11) 乘 $1,T,z$ 得到的关系均有首项 $C\lambda^Ne_i$，其余项的总权严格较低；递推约化表明原代数由 $\lambda^j e_i$、$0\le j<N$ 生成，故至多 $3N$ 个权模生成元。这里不另多乘一个虚构自由模维数。

本次只构造新的最高原行、权组合与明确的原 lifting 定义；完整 $\chi_C$ 的大系数没有展开或保存。其首一性和次数是 (12)–(13) 的代数推论，而非未经运行的系数报告。

## 6. 唯一源与资源

建议源：

`notes/2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py`

- blob：`999ac2498063d206315dd37a64a02a438d10d918`。
- SHA256：`4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41`。
- 12941 字节，尚未执行，固定 120 秒 / 1 GiB。
- 唯一源码依赖：`2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，SHA `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`。
- 环境路径可用 `ISP_PHI_FIRST_HEAD_RULE_SOURCE`。只执行旧 `det0=determinant(rows)` 前的 7097 字节必要原规则；该前缀 SHA 为 `9467955925e4f6bd05aaf74c5d8fb7e747a03c0a5119fb17ee2b87e7703a701b`。
- 前缀 alarm 在执行期间钳制到最初绝对 120 秒截止时刻；不延长总限额。

没有历史 JSON、旧多项式载荷、编码或分片依赖；不执行旧 D-cofactor、F6 大行、P6/P9 范数、bb35 弱 Popov 或任何已结论门。所有新权残留与未成功返回均如实保留，ordinary ISP 尚未完成。
