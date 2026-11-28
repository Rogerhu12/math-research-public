# R150：P164 泛型原商的完整双数族、真正 D 返回与整个 W 的有限支撑

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

唯一实际 run46097558018 / job140832328219 完整成功：驱动 4.009465304 秒、峰值 RSS 94096 KiB、内层退出码 0。完整原 I6、同一 N1/qZ 坐标、五条 D 清分母原值和全部所需权逆均实际返回。

## 1. 结论及辅助原商的准确范围

沿 [完整两个残余主分量及泛型四维上界](R150-appendix-unit211-W-P164-two-complete-residual-quotients-and-generic-length-four.md)，令

$$
A=\mathbf Z_{(1009)}[k]_{(1009,k-3)},\quad
B=A[e]/(\widehat P_{97}),\quad
C=B[\lambda,z]/(\chi_6,q_z),
$$

$$
\mathcal M=C/I_{11}C,\qquad F=\mathbf Q(k).
\tag{1}
$$

I11 是原三条均值、N1、两个加权值和五个完整 D 清分母值的辅助理想。它没有倒置 D；在原物理 D 非零图中与完整相应原条件相接，但其 D0 点不能直接称作物理原解。此前已完成

$$
\dim_F(\mathcal M\otimes_A F)\le4.
\tag{2}
$$

本篇将这个完整辅助泛型代数精确识别为

$$
\boxed{\mathcal M_F\simeq
F[e,\epsilon]/(L_{1/2},\epsilon^2),}
$$

$$
L_{1/2}=4ke^2-(k^2+4k+8)e-(k^2+6k+8).
\tag{3}
$$

同构下

$$
\ell=\tfrac12,\quad \lambda=\tfrac12+\epsilon,\quad T=-\tfrac12,
\quad x=\tfrac12+2(1-e)\epsilon,\quad y=\tfrac12,\quad t=0,
$$

$$
f=\frac{e+1}{2}-(e-1)\epsilon.
\tag{4}
$$

因此原辅助泛型商中 D 真为零，当前物理 D 非零局部化泛型为空。这是通过特征零同维满射得到的身份，不是从模 D=0 提升。

结合此前 P 无未付竖直分量和 H198 整支有限交，可推出整个当前 W 的物理权支持零维，固定规范完整原商为有限维 QQ 代数。本篇没有给出非泛型 k 的显式覆盖多项式、其次数或新的全 W 数值点数界；全部有限原候选仍须继续返回，整个 W 尚未排空。

## 2. 完整四维权双数代数，绝不预设为域

设

$$
r_1=(k^2+4k+8)/(4k),\quad r_0=(k^2+6k+8)/(4k),
$$

$$
E=F[e]/(e^2-r_1e-r_0),\qquad S=E[\epsilon]/(\epsilon^2).
\tag{5}
$$

两个关系首一，所以 E 在 F 上自由秩 2，S 自由秩 4，有完整基

$$
1,\ e,\ \epsilon,\ e\epsilon.
\tag{6}
$$

不需要 E 的不可约性，也不取一个数值或代数根。对 v=a+be，其乘法范数及真逆为

$$
N(v)=a^2+r_1ab-r_0b^2,\qquad
v^{-1}=(a+r_1b-be)/N(v).
\tag{7}
$$

本次所有所需逆都先检查 N(v) 是 F 中非零有理函数，再实际返回 v v^{-1}=v^{-1}v=1。没有把 E 中任意非零元素当成可逆，没有删除一个坏的二次分量。

原 W 权式

$$
u=e+1,\quad Q=ek,\quad V=(e+1)k+2,\quad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV}
$$

满足

$$
2\ell-1=-L_{1/2}/(kV).
\tag{8}
$$

V 的实际逆属于第 4 节原单位返回，故在 (5) 中 ell=1/2。之后所有权都由同一个 e,k 恢复。

## 3. 显式原 Gram 与完整 I6 返回

在 S 中取 (4)。为避免混淆，新 epsilon 是系数环中的双数方向；原四坐标乘积仍使用原 jet 块的乘法

$$
(v_0,v_1,v_B,v_C)\cdot(w_0,w_1,w_B,w_C)
=(v_0w_0,v_0w_1+v_1w_0,v_Bw_B,v_Cw_C),
$$

及原迹 tau(v)=a v0+v1+b vB+c vC。两类 nilpotent 坐标没有混同。

设 rho²=1−Q、p=1+rho、q=1−rho，

$$
a=1-\ell=\tfrac12,\quad
b=\ell/2+(u-\ell)\rho/[2(1-Q)],\quad c=\bar b.
$$

所有式可在完整首一 rho 二次扩张中核对，无需选符号。令 gamma=2(2−u)epsilon，则原 Gram 的 A=0、r=s=gamma，四行为

$$
(0,0,p,q),\quad (0,0,\gamma,\gamma),\quad
(p,\gamma,0,0),\quad(q,\gamma,0,0).
\tag{9}
$$

gamma²=0。原 d 和 F2 为

$$
d=(u,\gamma/2,p/2+\gamma,q/2+\gamma),\qquad
F_2=u+\gamma=2f.
\tag{10}
$$

直接代入原 mean 定义得到三条完整均值 E1=EBe=EBo=0。原恢复式还有准确的权身份

$$
P_{02}=(2-u)T_0,\qquad T_0-J+Q=0.
\tag{11}
$$

因此原 E0/N0/P1 求得的 f、lambda、T 恰为 (4)。新源实际逐式检查这些恢复及 (9)，并直接把旧原六式代入 S 返回四个 F 坐标，没有只核约化点。

为显示 N/P 的完整来源，记 v 为 (9) 首行，w 为第二行。原多项式直接给

$$
N_4(v)=P_{02}+T_0\gamma=2\lambda P_{02},
$$

$$
N_4(v+w)-N_4(v)-N_4(w)=T_0\gamma,\qquad
P_{\rm jet}=\tfrac32T_0\gamma.
\tag{12}
$$

故

$$
N_1=T_0\gamma-\frac{4\lambda}{3}\frac{3T_0\gamma}{2}=0
$$

因 lambda=1/2+epsilon、epsilon gamma=0。

即使暂将 gamma 视为自由量，原单点行还满足

$$
N_4(\mathrm{row}_B)=2\gamma^2(\gamma-u-p),\qquad
P_2(\mathrm{row}_B)=\gamma^2(2\gamma-3p),
\tag{13}
$$

C 行为 q 的共轭式。在当前 S 中 (13) 全零。同时

$$
A_2=2\lambda^2-2\lambda+1=\tfrac12,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1=-\tfrac12,
$$

故原加权 NS/PS 的校正项

$$
\ell+2T+A_2,\qquad \ell+3T+3A_2+B_3
$$

也都为零。于是全部 I6 六式在 S 中为零，完整保留 epsilon 的非零一次方向。这个显式 Gram 族是一个用于构造满射的族，不被偷换成整个 ellhalf 原图的分类。

## 4. 原模型全部系数分母的穷尽覆盖

原模型的 67 个不同权逆来自下列完整入口；新源覆盖每一类，不添加未知 e 因子。

### 4.1 Native P 与 chi 的原系数

[全 W 原 native NS/PS 曲线](R150-appendix-unit211-W-entire-original-native-NSPS-necessary-weight-curve.md)第 2–4 节给出真实六规则、三轴矩阵、六行原迹及

$$
\det M_{\rm nat}=cU P,\qquad U\ \text{为原权单位}.
\tag{14}
$$

[全 W 首一物理 lambda 六次](R150-appendix-unit211-W-global-original-physical-lambda-monic-six.md)第 2–4 节给出

$$
(\lambda I-M_\lambda)v=E_\lambda F_4,\qquad
\chi(\lambda)\in I_4.
\tag{15}
$$

这两组原身份的全部分母均已实际剥至同一个 native 原子表：

$$
e,\ k,\ u,\ ek-1,\ V,\ k+4,\ \operatorname{num}P_{02},
\operatorname{num}M,\ k+1,\ k+2,\ H_{\rm old},\ C_9,\ J_{19}.
\tag{16}
$$

这里 H_old=4ek−k²−4k−8，不是未付 H198；源码名 bc 的原子实际是 M 的分子。本次将 (16) 的每一项在完整 E 中按 (7) 真逆，并全部乘回。所以旧权身份在这个非物理 D0 辅助族上仍然有定义，不能仅以“它们在物理图已付”来跳过本次检查。

M_lambda 的 36 个系数分母因此全有逆；Faddeev 只再除 1 至 6。没有其它 e 分母。由 v0=1 的伴随身份，(14)、(15) 严格给出

$$
P|_S=0,\qquad\chi(\lambda)|_S=0.
\tag{17}
$$

它们来自已刊原理想来源及本次真逆，不是重复计算旧 determinant 或 QQ 特征系数，也不是只用集合上的必要性。

### 4.2 N1 坐标、原几何及额外值的系数

旧完整模型 groups/evalpoly 的剩余输入恰为 beta0、beta1、N1 的 a,c,DeltaN 与 p0,p1,p2、原 t 恢复式、六个 physical-lambda 原式、ntag/ztag、old-lambda/T、u,Q,ell,M,P02,J，以及原 NB/PB 奇部和整个 N4(V) 的三个系数。新源直接对这些实际表达式及其分母求完整 E 范数逆；physical-lambda 六式是旧六式经 tnew 代换，所增分母仅来自已实际可逆的 alpha_t=bc Q/P02 和旧 lambda 系数。

旧 C 类显式除法只再使用 m=u−ell、u、Q、ell、delta=1−Q、M 及其乘积与 QQ 常数，新源也全部乘回。旧 p 内容归一只乘 QQ 常数；将 P 对 e 首一化的头仅为纯 k 非零有理函数，属于 F 的单位。没有任何几何 D、lambda 首项或未经核验的范数逆。

## 5. 同一个 N1 坐标、qZ 与全 I11

新源准确代入旧

$$
n=p_0+p_1x+p_2y,\quad p_1=a\lambda+b,\quad p_2=c\lambda+d,\quad
\Delta_N=ad-bc,\quad z=ax+cy.
$$

DeltaN 在完整 E 中实际返单位，且以下两个方向全部返回：

$$
n=0,\quad \Delta_Nx=p_2z+cp_0,\quad
\Delta_Ny=-p_1z-ap_0,\quad z=ax+cy,
$$

$$
q_z=z^2+\beta_1z+\beta_0=0.
\tag{18}
$$

这是原有限模型的同一点坐标，不是重新选另一个根。

由 (4) 和 epsilon²=0，

$$
D=\ell A_2-T^2=0,\qquad
K_{\rm moment}=\ell^2B_3-3\ell TA_2+2T^3=0.
\tag{19}
$$

[完整 I11 原二十行二列定理](R150-appendix-unit211-W-H198-complement-exact-twenty-two-full-original-values-and-two-scalars.md)中的五式 qT4、R6、Nlow、Plow、Vlow 每一项都含 D 或 Kmoment。它们的全部其它系数在第 4 节原环上有定义，所以五式都在 S 中为零。新源也按完整原公式实际形成并返回它们，包括整个 N4(V) 三个系数，未以 Phi 倍数代替原值。

这一返回只给辅助 I11 在 D0 上的族；不声称 D0 族满足物理 D 非零条件，也不把五个清分母式在 D0 上误称全部个别原值的充分条件。

## 6. 四维满射才给真正的 QQ 身份

由 (17)、(18)、全部十一原式和系数逆，得到 F 代数同态

$$
\mathcal M_F\longrightarrow S.
\tag{20}
$$

e 与 lambda−1/2 的像分别为 e、epsilon，故产生 (6) 的全部四个基元，(20) 满射。S 的 F 维数恰为 4，而已成 (2) 给来源维数至多 4。因此 (20) 是同构，证明 (3)，且

$$
D=0\ \text{in }\mathcal M_F,\qquad
(\mathcal M_F)[D^{-1}]=0.
\tag{21}
$$

这是特征零的同维论证。此前模商的 D0 身份只用于发现候选族；真正上界、完整 QQ 族、全部原关系与满射缺一不可。没有从模理想为空、模幂零或多变量 gcd1 推出 (21)。

## 7. 从泛型排空到当前全 W 的有限原支撑

本节只推出有限性，全部有限原纤维继续保留。

在 H198 非零补图上，将 P、chi、qZ、I11 的有限多个有理系数清到它们已付纯权分母，得到一个有限型原环及同一个辅助原商。对 QQ[k] 的非零元素局部化就是第 6 节的泛型模型（或其进一步原权局部化）。由 (21) 的局部化定义，存在某个非零

$$
h(k)\in\mathbb Q[k]
$$

使 hD 在该辅助商中为零；若为书写统一环须再乘有限个纯 k 分母，可并入 h。物理 D 非零后，h 本身为零。因此所有这个补图的物理权点都在有限个 k 纤维上。

[P164 无未付竖直分量定理](R150-appendix-unit211-W-native-P164-integral-specialization-no-vertical-component-and-local-weight-model.md)已经证明：P 的 QQ[k] 内容只含原已付纯 k 因子。所以每个允许的有限 k 纤维上 P(e,k) 不会作为 e 多项式恒零。由 P=0，每个这样的 k 只留下有限多个 e。这个论证保留所有头降次；不是把 P 对 e 的某个未付首项强加为单位。

整个 H198=0 原支则由[H198 与 P164 的有限交定理](R150-appendix-unit211-W-entire-H198-native-P164-finite-intersection-and-original-length.md)独立给出权长度至多 4100，不依赖本篇 DeltaN 逆。于是两图合起来，当前整个 W 的物理权支持零维。

这也给出固定规范完整原商有限长度。原均值商已有全 W 的六生成元；在有限权 Artin 环上基变换、取其它原条件商或局部化都仍有限。加 rho²=1−Q 最多乘二；完整 HA/HB 在原 ell、m、D 单位上唯一恢复

$$
\zeta=\frac{T+uK_{\rm moment}/(2mD)}{\ell}.
\tag{22}
$$

其余规范值和 Gram 由同一原恢复式决定。因此固定七坐标 (e,k,rho,x,y,t,zeta) 的原商是有限维 QQ 代数。

h 尚未显式计算，所以本篇不声称新增数值总长度或点数界，也不将任何有限纤维删去。有限性仍不足以关闭这个课题或整个 W。

## 8. 唯一实际执行与范围

唯一首次 run46097558018 / job140832328219，source commit 292beb620132a650f6323e3bebf07c3b22f139f5。源在 3.248548937 秒完成全部 I6 与原恢复，在 3.929393601 秒完成同点 qZ、全部 I11、四维满射和真范数逆；驱动 4.009465304 秒，峰值 RSS 94096 KiB，内层退出码 0。

本次检查 27 个实际表达式分母定义，完成 61 个整个二次代数的真逆及 59112 个 QQ(k) 多项式精确除法乘积。这个计数不同于旧 1164 模源的 67 个逆：旧源还逐个处理 native Mlambda 等系数，新源通过第 4.1 节完整原子表统一支付那些分母，再直接检查其余原表达式；没有遗漏旧源的某类分母，也没有假称两计数一一对应。

原坐标完整定义串仅 968 字节，SHA-256 ce7037b479f69e0e790303442c1553e6df681871ad8b6ea9dd7295b672e0eab5；具体参数已在 (3)–(5)、(18) 给出，不另保存可重算载荷。

2026-11-28 02:20:31.654626 UTC 真实 pull 后仍为 292beb620132a650f6323e3bebf07c3b22f139f5。两 README blob 为 282e86b03385d3b6245ce7100ae2e2af7b103c2d 和 5fbd905291dd044c88d35bd9c07ac0e586ff795a，均无变化。

stdout 4514 字节，SHA-256 0555b4577b08009a0f036dd6f85534c25835ecfbe1204d9fca8275d4e4d39386。附[唯一实际小回执](../notes/2026-11-28-unit211-W-P164-true-QQ-dual-family-generic-D-finite-support-actual-receipt-8542.json)。此前发布器的大写 workflow 名未通过既有小写前缀校验，未启动数学进程；更名后的本次是唯一真正数学执行，不是重复运行。

冻结源：

[2026-11-28-unit211-W-P164-true-QQ-dual-family-complete-original-return-8542.py](../notes/2026-11-28-unit211-W-P164-true-QQ-dual-family-complete-original-return-8542.py)。

blob fdaea116782aec79f68113d7ffd4a8f6204a915e；15359 字节；SHA-256 529eb09a14f050f9cb086a1f42d8313c3fd3cdd45d59e5894f6699e6715c1753。仅取旧完整值源 5551 字节必要原定义前缀，SHA-256 9a6f12dad89cc77c651f902bf881b53eca708cd8f0dcfab2961dabb089ed3523。180 秒 / 4 GiB，全部 timer 受最初绝对截止约束。

只保存小源、参数定义、原返回标记和 SHA，没有可重算系数缓存、编码或分片载荷。没有重跑旧 P determinant、QQ 特征多项式、模 primary 或范数门。普通无限维 ISP 与整个 W 仍未排空。
