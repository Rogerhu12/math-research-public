# unit211 一般 LS 的整个 Q=1−u 边界：精确局部整除与完整原排除

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

**定理。** 在 R150 原 unit211 的一般 LS admissible 范围内，

$$
\boxed{u+Q-1\ne0.}
$$

换言之，整个 $Q=1-u$ 权边界已由原方程排除。本条补齐此前 $222$ 个不同权点上界留下的端点：原结式的三个新 QQ 重数确为 $244,3,3$，于是原必要余式降为 $1129$ 次，其模约化与既有全部残留因子互素。全程保留原六个方程的来源、原物理不同值条件、全部首项零纤维和二次域的两个复嵌入。

本文只关闭这条 R150 权边界，没有宣称一般 LS 已全部排空，也没有宣称普通复 Hilbert 空间不变子空间问题已解决。

## 1. 已付原输入及所有零支的覆盖

沿用[原 G2 图的 63/60 次必要覆盖](R150-appendix-unit211-Q1minusU-original-G2-chart-finite-parameter-cover.md)，以及[整个 G2 零曲线的原排除](R150-appendix-unit211-Q1minusU-complete-G2-zero-exclusion.md)。此前原均值的首项零支、$H=0$、$u=\tfrac12$、$\ell=0$、$T_0=0$、$K_z=0$、$\ell=\tfrac12$ 和一般等权支均已逐支完整返回；这些证明继续负责各自整个零支。

因此只须在原余图中工作。在这里，源中实际使用的全部单位

$$
u,\ Q,\ \ell,\ M,\ H,\ P_{02},\
\ell-2u,\ 2u-1,\ K_z,\ \ell-u,\ 2\ell-1,\ G_2
$$

均有原物理输入或已登记整支排除作为依据。此处没有再加入新的未付单位。

置 $h=\ell/u$。原两个必要 cofactor $C(u,\ell),D(u,\ell)$ 的原六行组为

$$
[0,1,2,3,4,6],\qquad [0,1,2,3,7,9],
$$

总次数分别为 $63,60$。令

$$
C_h=u^{-34}C(u,uh),\qquad D_h=u^{-31}D(u,uh).
$$

这是逐系数乘回的确切多项式变换，得到

$$
(\deg_u C_h,\deg_h C_h)=(29,43),\qquad
(\deg_u D_h,\deg_h D_h)=(29,42).
$$

所有本条实际源都从同一原 Gram、原六式和实际乘法重建这两个输入，核对其确定 SHA256：

~~~
C: d9ee664678e97aa5a1ebc17f1ba275456137915bb494e2daf0cd4b280f3eb312
D: 4e16a4461f64280c962bf870aea6161edb455382074525be75a7fc0b3fbd5b3d
~~~

任一余图原点都满足 $C_h=D_h=0$。保留固定 $29/29$ 次 Sylvester 行列式

$$
R(h)=\operatorname{Res}_u(C_h,D_h).
$$

[已付整数高度 / CRT 定理](R150-appendix-unit211-Q1minusU-exact-2265-projection-and-three-multiplicities.md)给出

$$
\deg R=2265,\qquad
\operatorname{ord}_{h=0,1,2}R=(304,47,532).
$$

故

$$
R_0(h)=
\frac{R(h)}{h^{304}(h-1)^{47}(h-2)^{532}}
$$

是准确 $1382$ 次多项式。令 $p=1009$。$R$ 的系数在 $\mathbf Z_{(p)}$ 中，且首项为该局部环的单位；因此 $R_0$ 的首一归一 $\widehat R_0$ 也在 $\mathbf Z_{(p)}[h]$ 中，其约化保持 $1382$ 次。所有实际原点都避开 $h=0,1,2$，所以仍必须满足 $R_0=0$。

[原 cofactor 的 222 次覆盖](R150-appendix-unit211-Q1minusU-original-cofactors-222-degree-h-cover.md)以及后续固定 66 阶返回已经完整乘回了同一模公共因子的分解：

$$
\bar g_{222}
=(h-\tfrac12)^2(h^2-3h+1)^3(h+1)^{214}
\quad\text{于 }\mathbf F_{1009}[h].
\tag{1.1}
$$

这里的 $\tfrac12$ 是 $1009$ 中的逆元，二次因子分为
$(h+381)(h+625)$。原四个足够的必要投影 $S_1,\ldots,S_4$ 的固定 Sylvester 阶数为 $56,55,61,61$；其模 gcd 链为

$$
1382\longrightarrow648\longrightarrow646
\longrightarrow224\longrightarrow222.
$$

每个 $S_i$ 都是原必要 cofactor 与 $C_h$ 的固定次数 QQ 结式；原系数的常数分母在 $p$ 为单位，且全局 $u$ 次数在约化时保持。相应完整一元 Bézout 乘积已实际核验。因此

$$
\gcd(\overline{\widehat R_0},\bar S_1,\ldots,\bar S_4)
=\bar g_{222}.
\tag{1.2}
$$

本条不增加随机 cofactor，也不重复已经冻结的完整 QQ 大投影。

## 2. 三条完整精确权域已经由原 QQ 返回排除

[三个精确权域定理](R150-appendix-unit211-Q1minusU-three-exact-weight-domain-exclusions.md)已证明，在整个本边界的原点上

$$
h+1\ne0,\qquad h-\tfrac12\ne0,\qquad h^2-3h+1\ne0.
\tag{2.1}
$$

其直接原证据是：

| 精确商域 | 原 $C_h,D_h$ 的真实单位剥除 | 剩余次数 | 完整返回 |
|---|---|---:|---|
| $h=-1$ | 各剥 $(u-1)^{15}$，来自 $Q$ | $14,14$ | QQ Bézout $1$ |
| $h=\tfrac12$ | 各剥 $u-1$，来自 $Q$ | $28,28$ | QQ Bézout $1$ |
| $h^2-3h+1=0$ | 剥 $(u-3+h)^2$ 与 $u-3+h$，来自 $M$ | $27,28$ | 整个二次域上的 Bézout $1$ |

二次域的判别式为 $5$；每次系数求逆均有实际 QQ 多项式 Bézout $1$ 乘回，保留两个复嵌入。以上并非由模候选支猜测 QQ 覆盖。本条下一节补上尚缺的原 QQ 整除。

## 3. 三个原局部 QQ 整除证书

### 3.1 原平移和准确初始赋值

令

$$
\phi_-(h)=h+1,\qquad
\phi_{1/2}(h)=h-\tfrac12,\qquad
\phi_2(h)=h^2-3h+1.
$$

对前两项，在两原 $u$ 多项式中同时作 $u\mapsto u+1$；对第三项作 $u\mapsto u+3-h$。每次都完整展开，再以反平移逐系数返回原输入。平移保持同一个 $u$ 结式，故没有更换原必要投影。

记平移后的固定 $58$ 阶 Sylvester 矩阵为 $\mathcal S$；其行列式与 $R$ 至多相差固定符号。逐项精确计算 $\phi$ 赋值后，源实际生成一个最小权完美匹配以及完整整数对偶 $r_i,c_j$，验证

$$
\operatorname{ord}_\phi\mathcal S_{ij}\ge r_i+c_j,\qquad
E_0=\sum_i r_i+\sum_j c_j.
$$

矩阵中每项按 $\phi^{r_i+c_j}$ 除去；负指数时乘相应的正幂。所有非负幂除法均逐项乘回。于是归一矩阵 $\mathcal M$ 仍在 $\mathbf Q[h]$ 中，并且

$$
\det\mathcal S=\phi^{E_0}\det\mathcal M.
\tag{3.1}
$$

实际初始值及后续秩亏为：

| $\phi$ | 原 $u$ 平移 | $E_0$ | 后续逐轮 $K_\phi$ 核维 | 最终 QQ 重数 |
|---|---|---:|---|---:|
| $h+1$ | $u+1$ | $225$ | $15,2,2$ | $244$ |
| $h-\tfrac12$ | $u+1$ | $1$ | $1,1$ | $3$ |
| $h^2-3h+1$ | $u+3-h$ | $2$ | $1$ | $3$ |

所有匹配、对偶和实际逐轮返回都保留在[本条小 JSON 回执](../notes/2026-11-27-unit211-Q1minusU-complete-native-QQ-divisors-receipt-8542.json)中。

### 3.2 正规表示的真实核与全多项式 det1 行变换

设 $K_\phi=\mathbf Q[h]/(\phi)$，$d=\deg\phi$。取 $\mathcal M\bmod\phi$ 在基 $1,h,\ldots,h^{d-1}$ 下的 QQ 正规表示，得到准确 $58d$ 阶有理矩阵。源以 QQ rref 求核，再转回 $K_\phi^{58}$，并逐项验证每个所用行向量满足

$$
v\,(\mathcal M\bmod\phi)=0.
$$

把这些核向量在若干选定坐标 $I$ 上化为完整单位阵。所有系数逆都通过实际 $\mathbf Q[h]$ Bézout $1$ 验证；每个系数使用次数小于 $d$ 的多项式代表。故选定坐标上的单位阵等式也是 QQ 多项式的准确等式。

将原矩阵的行 $I$ 换成这些核组合。相应全多项式行变换可写成

$$
P=I+N,\qquad
N\text{ 只在 }I\times I^c\text{ 上可能非零},
$$

所以

$$
N^2=0,\qquad\det P=1
\quad\text{于 }\mathbf Q[h].
\tag{3.2}
$$

这一步没有在全参数环中倒置某个未付 pivot。每个新核行的所有项都被 $\phi$ 整除；逐项做准确除法后，若本轮核维为 $k$，则行列式准确提出 $\phi^k$。

两线性域用 $58$ 阶 QQ 正规表示；二次域用 $116$ 阶。实际 QQ 秩分别为

$$
43,56,56;\qquad 57,57;\qquad114.
$$

二次域末项的核 QQ 维数为 $2$，即完整商域核维数 $1$，没有按某一个复根取核。

### 3.3 有限精度没有丢失整除结论

设本次目标重数为 $m$，固定 $T=m+1$。累计提出 $E$ 次后，每个剩余矩阵项只保留模 $\phi^{T-E}$ 的余式，并验证

$$
a=q\phi^{T-E}+r
$$

的完整乘回。始终维持准确的标量行列式同余

$$
\varepsilon R\equiv\phi^E\det\mathcal M
\pmod{\phi^T},\qquad \varepsilon\in\{1,-1\}.
\tag{3.3}
$$

原因如下：项的模 $\phi^{T-E}$ 约化使行列式至多改变该幂的倍数；(3.2) 保持行列式不变；将 $k$ 个真实核行各除 $\phi$ 后，(3.1) 的累计指数变为 $E+k$。再在精度 $T-E-k$ 截断，仍保 (3.3)。

实际精度路径为

$$
20\to5\to3\to1;\qquad
3\to2\to1;\qquad
2\to1.
$$

到 $E=m$ 时，(3.3) 直接给出 $\phi^m\mid R$ 于 $\mathbf Q[h]$。这不要求生成完整 QQ 结式。

另一方面，$R\in\mathbf Z_{(1009)}[h]$，各 $\phi$ 首一且系数在该局部环。若有更高 QQ 整除，首一多项式除法使商仍在同一局部环，约化后也必须有更高整除。实际完整原 $\bar R$ 的对应重数为 $244,3,3$，因此它们同时是准确 QQ 上界。结合以上真实下界，得到

$$
\boxed{
\operatorname{ord}_{h+1}R=244,\qquad
\operatorname{ord}_{h-1/2}R=3,\qquad
\operatorname{ord}_{h^2-3h+1}R=3.}
\tag{3.4}
$$

三个源都达到完整目标，未出现“QQ 满秩提前停止”的未决分支。

## 4. 1129 次首一原余式与严格 Gauss 终返回

置新的首一乘积

$$
P_1(h)=(h+1)^{244}(h-\tfrac12)^3(h^2-3h+1)^3,
\qquad\deg P_1=253.
$$

这三个因子与 $h(h-1)(h-2)$ 两两互素。由 (3.4)，

$$
R_1=\frac{R_0}{P_1}\in\mathbf Z_{(1009)}[h],
\qquad
\deg R_1=1382-253=1129.
$$

其首项仍是原单位。记 $\widehat R_1$ 为首一归一，则

$$
\widehat R_1\in\mathbf Z_{(1009)}[h],
\qquad\deg\overline{\widehat R_1}=1129.
\tag{4.1}
$$

第 2 节已排除 $P_1$ 的整个零域，所以任一原点都必须满足 $R_1=0$。

实际模因子表还分别验证二次因子的两个线性因子 $(h+381),(h+625)$ 各自的完整原重数均恰为 $3$；不是仅验证二者的最小重数。于是完整原模重数 (3.4) 保证 $\overline{\widehat R_1}$ 不再含三个 $\bar\phi$ 的任一个因子。结合已实际乘回的 (1.1)，立即得到

$$
\gcd(\overline{\widehat R_1},\bar g_{222})=1.
\tag{4.2}
$$

这是现有完整模因式乘积和准确重数的直接推论，不需要额外计算任何完整 QQ 结式。

为明确付清特征零提升，反设原点存在。其 $h$ 坐标是非零 QQ 多项式 $\widehat R_1$ 的根，因此为代数数。该点同时使所有原必要 $S_i$ 为零。令

$$
G=\gcd_{\mathbf Q[h]}(\widehat R_1,S_1,\ldots,S_4)
$$

取首一，则 $\deg G>0$。因为 $\widehat R_1$ 在局部环中首一，Gauss 内容引理给出

$$
G\in\mathbf Z_{(1009)}[h].
$$

可直接核此处的局部形式：若首一分解 $\widehat R_1=GH$ 在 QQ 中成立，两个因子的最小系数赋值均不大于 $0$，其和等于 $\widehat R_1$ 的最小系数赋值 $0$，所以两者都为 $0$。故所有系数局部整。再以首一 $G$ 除各 $S_i$，其商也局部整。

因此 $\bar G$ 保持正次数，同时整除
$\overline{\widehat R_1}$、$\overline{\widehat R_0}$ 及全部 $\bar S_i$。由 (1.2) 它又整除 $\bar g_{222}$，与 (4.2) 矛盾。故原余图没有复权点。

每个 $S_i$ 始终是固定尺寸的原 Sylvester 行列式。即使某个特定 $h$ 上原输入的 $u$ 首项下降，任何实际共同有限 $u$ 根仍给该固定矩阵非零的求值核列，故必要性仍成立。最后的 Gauss 论证没有删除这些首项零纤维。

合第 1 节的全部既有零支覆盖，得到整个 $Q=1-u$ 边界排空，即本条定理。

## 5. 自含源与真实执行记录

三个新源均从原 Gram 重建同一 $C_h,D_h$；它们各自只登记局部 QQ 整除。第 4 节是与此前已付定理的逻辑合成，不把某个单源的 success 标记当作整边界结论。

| 新输入 | 原源 | run / job | 内部 exit | driver 秒 | RSS KiB |
|---|---|---|---:|---:|---:|
| $h+1$ | [完整源](../notes/2026-11-27-unit211-Q1minusU-new-phi-h-plus-one-native-QQ-divisor-certificate-8542.py) | $45977218604$ / $140431871570$ | $0$ | $10.330388085$ | $67012$ |
| $h-\tfrac12$ | [完整源](../notes/2026-11-27-unit211-Q1minusU-new-phi-h-minus-half-native-QQ-divisor-certificate-8542.py) | $45977221507$ / $140431878554$ | $0$ | $7.880387577$ | $67048$ |
| $h^2-3h+1$ | [完整源](../notes/2026-11-27-unit211-Q1minusU-new-phi-h-quadratic-native-QQ-divisor-certificate-8542.py) | $45977224556$ / $140431892271$ | $0$ | $7.722202801$ | $66984$ |

对应源 SHA256：

~~~
h+1:
7f4f00a1908dd128553d67d0d1f1dd654d8b4d3a6173b3b60853f2231cf9185d

h-1/2:
b5e0a9a715ccbcd840493489661be4f31a85591b1631b4c005c1888420e0a75e

h^2-3h+1:
f635013ec13f567ff8ab6e351b117e0a747a83c60f33fd9d17be8d32ea038a1c
~~~

对应 stdout SHA256：

~~~
471fe6f2d8f70d2b2cd49a7cbe20819dbc8f8776ba84d3ffb5bcf13d81248572
784eed0cc5800aa8c83950a5f3a90a4c9e300fd496790a400512d91bad2419a8
3b2ddb3c5782945f4d16454d2300bd68e19537ff0911d5b75b0087f6019a62c4
~~~

实际精确除法 / 余式乘回次数分别为 $48305,29064,22219$，合计 $99588$；商域系数逆的 QQ Bézout 检查分别为 $19,2,1$。这些数据及每轮核行的 trace SHA256 均在小 JSON 回执中。

三次真实 driver 都在提交 $8e32b487661e9ee886f8c4968dcf4d31015e9938$ 执行，实际 pull 后两份 README blob 均无变化。三个输入都是此前未执行的新局部因子输入；本条没有重跑被冻结的 85 阶或 58 阶完整 QQ 投影，也没有要求额外整套复现才登记已经完成的数学结论。
