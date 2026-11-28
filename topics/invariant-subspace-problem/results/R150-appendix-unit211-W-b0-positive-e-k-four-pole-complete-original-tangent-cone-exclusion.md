# R150：W/b0 正 e、k 首值四的全部 lambda 极点由三个原二次切锥排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，不存在满足
$$
v(e)>0,\qquad v(k)=0,\qquad \bar k=4,\qquad v(\lambda)<0
\tag{1}
$$
的 $1009$ 进原解。完整原 $q_2,R_6,N_5$ 在该中心有三个二次最低齐次部分；它们在 $\overline{\mathbb F}_{1009}$ 上的共同零点只有原点。准确的高阶余项界把这个同点切锥矛盾用于全部估值比例，包含 $k=4$ 和任意更深相消。

结合[正 e 原 lambda 估值限制](R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)，得到
$$
\boxed{\quad
v(e)>0,\ v(k)=0,\ \bar k\ne-2
\ \Longrightarrow\ \lambda\ne0,\ v(\lambda)=0.
\quad}
\tag{2}
$$
本条没有关闭单位 lambda 或 $\bar k=-2$ 的全部中心，也不宣称正 e 射线、整个 W 或普通 ISP 已完成。

唯一新运行 run46169312729 / job141053873646 实际完成三个四阶原局部式与完整余式返回，0.346877190 秒、42804 KiB、exit 0。以下排除是基于其原二次系数和明确余项的纸面证明，不把成功退出当作空性。

## 1. 同一原中心与完整原来源

设 $\mathcal O$ 为包含假想原解的 $1009$ 上方赋值环，$\mathfrak m$ 为极大理想。引入实际坐标
$$
E=e,\qquad Y=k-4,\qquad X=(2\lambda-3)^{-1}.
\tag{3}
$$
在 (1) 上，$E,X$ 是非零正赋值元，$Y\in\mathfrak m$ 且允许等于零。反恢复是
$$
k=4+Y,\qquad \lambda=(X^{-1}+3)/2.
$$
没有倒 Y，没有为不同原式选择不同点。

三个输入使用已刊[完整 b0/N5 原定义源码](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)中原必要定义，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。其
$$
u=e+1,\ Q=ek,\ \delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad m=u-\ell,
$$
$$
M=\ell^2\delta-m^2,\quad
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
T=\frac{uQ\ell}{A_*}(2\lambda-3)
$$
保持完整原 $b_0$ 图。设
$$
A_2=2\lambda^2-2\lambda+1,\quad B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell A_2T+2T^3,\quad
C_*=A_*m^2+J\delta\ell^2.
$$
原必要式仍为
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2,
\qquad R_6=MK^2-4m^2D^3,
$$
以及同一点完整
$$
N_5=2mD(Z_0+Dz_2)+MKz_1.
$$
$Z_0,z_1,z_2$ 由该源的完整原 $f$ 常数系数定义给出。其原身份保持
$$
N_5=2mD\ell^2NV+M z_{1,\rm full}H_{\rm val}
       -2mD z_{2,\rm full}q-\frac{2f}{MQ}C_4.
\tag{4}
$$
在当前原条件上，右侧为零；这不是施加物理 $f=0$，也没有倒 D。完整常数系数公式亦可见[负 k 原证明](R150-appendix-unit211-W-b0-entire-negative-k-ray-original-q2-R6-N5-exclusion.md) §1。

本次新的局部原式固定为
$$
F_q=q_2X^2/Q,\qquad F_R=R_6X^6,\qquad F_N=N_5X^5.
\tag{5}
$$
(1) 中 $Q,X$ 非零，所以原解必使 (5) 同时为零。它们的尺度不新增任何未证明的原支删除。

## 2. 实际原局部返回与明确余项

令 $I=(E,Y,X)$。实际在 $\mathbb Q[E,Y,X]$ 中分别生成 (5) 的完整约分分子 $n_i$、分母 $d_i$，并取四阶多项式 $J_i$。唯一实际运行逐式返回
$$
n_i-d_iJ_i\in I^5.
\tag{6}
$$
所有 $n_i,d_i,J_i$ 和完整余式的系数都在 $\mathbb Z_{(1009)}$。三个分母的原点值分别为
$$
d_q(0)=279936,\quad
d_R(0)=25389989167104,\quad
d_N(0)=-33853318889472;
\tag{7}
$$
它们均为 $1009$ 单位。因此 (5) 在整个 $\mathfrak m^3$ 上的这些分母都为赋值环单位，不需进一步删除中心。

实际 profile 如下。每个 SHA 是规范多项式编码的 SHA256；未保存大系数缓存。

| 原式 | 分子 $(E,Y,X)$ 次数 / 总次数 / 项数 | 四阶式项数 | 四阶式 SHA256 |
|---|---|---:|---|
| $F_q$ | $(10,9,2)$ / 18 / 279 | 25 | ce510cddb0f39e8f95b095dc2512f852c9ce4e43230aa62b9e11f1df8fb5f345 |
| $F_R$ | $(21,21,6)$ / 40 / 2996 | 31 | b2b137ff9df26578ddbb16d49391fb2f76aa2bfd88c3689d2df259dd3ac227ef |
| $F_N$ | $(21,22,5)$ / 40 / 2726 | 31 | cc172682709b6b5a0bdd0f3beb6dbcd677c6cc0ff876ededda93a2d80cb79d79 |

三个完整原局部式的常数项和一次项都为零。其二次齐次部分准确为
$$
H_q=\frac16(2E+3X)(8E-Y-6X),
\tag{8}
$$
$$
H_R=\frac3{512}\,\mathscr R,
$$
$$
\mathscr R=Y^2+8EY+48YX-112E^2+192EX+288X^2,
\tag{9}
$$
$$
H_N=\frac1{256}\,\mathscr N,
$$
$$
\mathscr N=2024E^2-418EY+1056EX-33Y^2-1188YX-2376X^2.
\tag{10}
$$
(6) 与完整四阶式说明
$$
F_i-H_i\in I^3
$$
在上述 $1009$ 整局部环中成立。这里的余项包括四阶式中所有三、四次项和 (6) 的完整高阶有理余项；没有把截断多项式当成完整原方程。

## 3. 第一条 q 切线没有非零共同点

在剩余域中先取
$$
2E+3X=0,\qquad E=-3X/2.
$$
将它代入 (9)–(10) 得
$$
\mathscr R=Y^2+36XY-252X^2,
$$
$$
\mathscr N=-33(Y+18X)(Y-X).
\tag{11}
$$
若 $X=0$，则 $E=0$，再由 $\mathscr R=0$ 得 $Y=0$。

若 $X\ne0$，由于 $33$ 在特征1009中非零，$\mathscr N=0$ 迫 $Y=X$ 或 $Y=-18X$。在这两个点分别有
$$
\mathscr R=-215X^2,\qquad \mathscr R=-576X^2.
$$
两常数均非零，所以不存在共同非零点。这里没有在原点集上先假定某一坐标非零；$X=0$ 已单独保留并处理。

## 4. 第二条 q 切线也没有非零共同点

取另一整条切线
$$
Y=8E-6X.
$$
直接代入 (9)–(10) 得
$$
\mathscr R=4C,\qquad \mathscr N=-132D_0,
$$
$$
C=4E^2+108EX+9X^2,\qquad
D_0=26E^2+21EX-27X^2.
\tag{12}
$$
准确原组合为
$$
2D_0-13C=-3X(454E+57X).
\tag{13}
$$
若 $X=0$，由 $C=0$ 得 $E=0$，继而 $Y=0$。

若 $X\ne0$，则 (13) 迫 $E=-57X/454$。$454$ 是特征1009的单位。代入 C，得到
$$
454^2 C=-926784X^2
\equiv487X^2\pmod{1009}.
\tag{14}
$$
非零，矛盾。因此第二条切线也没有共同非零点。

(8) 的两个因子覆盖整个 $H_q=0$，包括它们的交点。第3–4节证明
$$
H_q=H_R=H_N=0
\quad\Longrightarrow\quad E=Y=X=0
\quad\text{于 }\overline{\mathbb F}_{1009}.
\tag{15}
$$
这里使用的是同一点的三个首项，不是三个独立范数分别取根。

## 5. 由完整余项排除所有更深原解

假设 (1) 的原解存在。令
$$
t=\min\{v(E),v(Y),v(X)\}>0
$$
并忽略零坐标的无穷赋值。选一个非零坐标 $\tau$ 达到该最小值。于是
$$
E/\tau,\quad Y/\tau,\quad X/\tau\in\mathcal O
$$
且其三个剩余值至少一个非零。

由第2节全部系数整、分母在 $\mathfrak m^3$ 上为单位，任一总次数至少三的项估值至少 $3t$；(6) 的完整余项估值至少 $5t$。所以
$$
v(F_i-H_i)\ge3t>2t.
$$
原 $F_i=0$ 除以 $\tau^2$ 后取剩余值，得到一个非零剩余向量同时满足
$$
H_q=H_R=H_N=0,
$$
与 (15) 矛盾。这覆盖不同坐标任意正估值比例、所有首项相消和 $Y=0$；没有使用某一条固定权斜率代替全中心。

因此 (1) 完全排除，继而有 (2)。正 e 剩余问题现在只需保留：

- $\bar k\ne-2$ 的单位 lambda 情形；
- $\bar k=-2$ 的整位移 $Z=(k+2)/e$，其中 ell 为单位或有极点，全部 lambda 情形继续。

整位移结论的独立原证明见[正 ell 排除](R150-appendix-unit211-W-b0-positive-e-k-minus-two-positive-ell-exclusion-and-integral-center.md)。这些未闭中心和其它权射线/内部不被本文关闭。

## 6. 唯一实际执行与可复核身份

[源码](../notes/2026-11-28-unit211-W-positive-e-k-four-pole-three-original-local-jets-8542.py)；
[首次输入](../notes/2026-11-28-unit211-W-positive-e-k-four-pole-three-original-local-jets-8542-input.md)；
[小回执](../notes/2026-11-28-unit211-W-positive-e-k-four-pole-three-original-local-jets-8542-execution.json)。

源码 blob dbe928f3d984b0d24fa1e0876bbe5e0f2f5d2325，5716字节，SHA256 eb5463c4638bfa434add15bb7d2c3258353bee86fdc4a5bef569af3c67c1a147。首次固定120秒/1GiB，外驱动135秒，无增加预算或后续运行。

唯一实际 [run46169312729 / job141053873646](https://github.com/Rogerhu12/math-research-public/actions/runs/46169312729/job/141053873646)：

- 源提交8a62659e732a4289b94dc5a2c8d9878f18dd07b9。
- 2026-11-28 17:13:32.063693 UTC实际pull同提交，根和本题README无变。
- 驱动0.346877190秒、42804KiB、exit0；最后数学记录0.278074247秒。
- stdout4854字节，SHA256 54a4508e4a0b71872fbd6d3695754206b6663a90071dae481e62549c96402223。
- 五条数学记录完整读取；三个原有理式、三个四阶式及三个完整余式均返回。所有分母原点值及全部系数的1009整性已核。
- 没有gcd、因式分解、resultant、Gröbner或局部单位搜索；未重放旧六射线目标、旧原投影或冻结门。

旧执行的保留纤维和资源边界不改写；新增排除只来自本条 (3)–(15) 的完整新原局部来源。普通 Hilbert ISP 尚未完成。
