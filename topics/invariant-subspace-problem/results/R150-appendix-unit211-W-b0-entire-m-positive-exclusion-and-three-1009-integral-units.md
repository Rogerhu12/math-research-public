# R150：W/b0 整个 m 正阶排除及 m、k+2、Q−2 的 1009 整单位

日期：2026-11-29（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

**定理。** 在当前正确真 dual-germ 的 W、完整 $b_0=0$ 物理图的任意 1009 赋值位置，
$$
\boxed{v(m)=v(k+2)=v(Q-2)=0.}
$$
整 $v(m)>0$ 边界准确分成 $\bar k=-2$ 与 $\bar Q=2$ 两图。前图已有独立完整四维原返回；本次唯一新执行在后图的三个完整常数域中，实际返回未取商普通多项式环中的十二原源恒等式 $1$。下面同时补齐 $A_*=0$ 精确情形，保留所有谱根和所有头降次，不把有限域计算外推成未经证明的全 W 空性。

## 1. 全部前置范围与两图覆盖

固定剩余特征 $1009$，赋值可在任意有限扩张中取值，不假定阶已归一为整数。引用已刊原结果：

- [e、k、u 整单位](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)；
- [全 ell 整](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)；
- [整个 delta 正阶排除](R150-appendix-unit211-W-b0-entire-delta-positive-exclusion-and-1009-integral-unit.md)；
- [整个 Vbar 正阶排除](R150-appendix-unit211-W-b0-entire-Vbar-positive-exclusion-and-1009-integral-unit.md)；
- [m 正阶、k=-2 完整原排除](R150-appendix-unit211-W-b0-internal-m-positive-k-minus-two-entire-original-exclusion.md)。

原权定义为
$$
u=e+1,\quad Q=ek,\quad Vbar=uk+2,\quad \delta=1-Q,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{kVbar},\qquad
m=u-\ell=\frac{u(k+2)(Q-2)}{kVbar},\qquad
M=\ell^2\delta-m^2.
$$
所以 $m$ 整，$k+2,Q-2$ 整。若 $v(m)>0$，原单位 $u,k,Vbar$ 给
$$
\bar k=-2\quad\text{或}\quad\bar Q=2.
$$
两图交集会迫 $\bar u=0$，已经排除。在任一图上 $\bar\ell=\bar u\ne0$，并由 $\delta$ 单位得到 $M$ 单位；这里不借用另一个尚在推进的全 $M$ 整单位结论。

第一图的原 $q_2/R_6$ 强迫唯一中心
$$
\bar u=\frac{29}{49},\quad
\bar\mu=-\frac72,\quad\bar\lambda=-\frac14,\quad\bar T=-\frac{29}{28}.
$$
独立真 $E_1$ 的单位二次头先给 $f$ 整，原二矩给 $\sigma$ 整；唯一历史 run 46182562376 / job 141095189005 在四维环境中完整返回十源 $1$，最终只用真 $E_1,E_B$。本次不重做这一输入；下面处理全部第二图。

## 2. Q=2 图的准确权式及整个 Astar 深零排除

记 $U=\bar u$、$h=U+2$。由于 $\bar m=0$，
$$
\bar\ell=U,\quad \bar\delta=-1,\quad
\bar M=-U^2,\quad
\bar J=2U(2-U),\quad
\overline{A_*}=2U(U+2).
$$
$U$、$U-1$ 已是单位；而
$$
\overline{Vbar}=\frac{2(2U-1)}{U-1}
$$
使 $2U-1$ 为单位。这里不逆 $U+1$，它可以使 $\overline{P_{02}}=0$。

原必要式继续使用
$$
\mu=2\lambda-3,\quad
A_2=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
A_*T=uQ\ell\mu,\quad
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3,
$$
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2,
\quad C_*=A_*m^2+J\delta\ell^2,
\quad R_6=MK^2-4m^2D^3. \tag{1}
$$

若 $A_*$ 正阶或恰为零，则唯一 $U=-2$。先设 $A_*\ne0$，记 $b=v(A_*)>0$；若 $\mu\ne0$，设 $s=v(\mu)$，并先允许 $\mu$ 有极点。由原 $b_0$ 有 $v(T)=s-b$。在 $s\le0$ 或 $0<s<b$ 时，$q_2$ 的 $T^2$ 项严格最低，矛盾。在 $s>b$ 时，其剩余常数为 $224\ne0$，也矛盾。若 $\mu=0$ 而 $A_*\ne0$，原 $b_0$ 直接给 $T=0$，同一常数 $224$ 排除。剩下 $s=b$，此时 $\bar\mu=0$ 且 $T$ 单位，
$$
\bar q_2=64\bar T^2+224,
\qquad \bar T^2=-\frac72.
$$
$D,K$ 整，$M$ 单位与 $v(m)>0$ 使 $R_6$ 迫 $\bar K=0$；但
$$
\bar K=14+15\bar T+2\bar T^3=14+8\bar T.
$$
于是 $\bar T=-7/4$，与 $\bar T^2+7/2=105/16\ne0$ 冲突。还必须单独处理 $A_*=0$ 的精确情形，不能对 $v(T)=s-b$ 使用 $\infty-\infty$。此时原 $b_0$ 因 $uQ\ell$ 为单位而直接迫 $\mu=0$。原 $q_2$ 的 $T^2$ 头为单位，其他系数整，所以先得到 $T$ 整；再取剩余得
$$
64\bar T^2+224=0.
$$
因此 $T$ 还是单位，且 $\bar T^2=-7/2$。同一原 $R_6$ 仍迫 $\bar K=14+8\bar T=0$，再得 $105/16=0$ 的矛盾。所有明确常数在特征 1009 非零。

所以整个 $U=-2$、$A_*$ 深零层，包括 $A_*=0$，均已由完整原估值式排除。互补图可付 $h$ 为赋值单位；这条纸面补全不改动已执行源或任何实际运行记录。

## 3. 全部 mu 极点的纸面排除

在 $U\ne-2$ 图，$A_*$ 为单位，原 $b_0$ 给 $T=\kappa\mu$，其中 $\bar\kappa=U/h$。完整 $q_2$ 的剩余为
$$
\bar q_2=-\frac{2U^3}{h^2}\,\widehat q,\qquad
\widehat q=G_3(U)\mu^2+4(1-U)h^2\mu+(4-5U)h^2, \tag{2}
$$
$$
G_3(U)=8-4U-2U^2-U^3.
$$
完整 $K$ 的剩余为
$$
\bar K=\frac{U^2}{2h^3}\,\widehat K, \tag{3}
$$
$$
\widehat K=
H_3(U)\mu^3+6Uh^2\mu^2+3(4U+3)h^2\mu+7h^3,
\qquad H_3(U)=U^3+3U^2+4U-4.
$$

若 $s=v(\mu)<0$，$q_2=0$ 迫 $G_3(U)=0$。若 $H_3(U)\ne0$，则 $v(K)=3s$，而 $v(D)\ge2s$；在 $M$ 单位、$v(m)>0$ 下，$R_6$ 两项的阶分别为 $6s$ 与至少 $2v(m)+6s$，不可能相消。因此还必须 $H_3(U)=0$。然而有准确原系数恒等式
$$
\boxed{(U+3)G_3(U)+(U+2)H_3(U)=16,} \tag{4}
$$
与特征 1009 矛盾。故 $\mu$、$\lambda,T,D,K$ 都整。

此后 $R_6$ 给 $\bar K=0$，但新源不会仅凭这一模幂零事实把原理想替换。下面将 $\widehat K$ 直接通过两个完整原谱矩返回。

## 4. 两个完整原矩给 khat 的直接来源

取 $\rho^2=-1$，可选 $\rho=469\in\mathbb F_{1009}$，另一根只把两个原 singleton 标签同时交换。保留未知 $\sigma$，定义
$$
b=c=\frac U2,\quad
h_v=1+\frac TU+\rho\sigma,\quad
k_v=1+\frac TU-\rho\sigma.
$$
下标 $v$ 区分原值和权参数 $k$。完整原第二、第三矩为
$$
E_2=b(h_v-1)^2+c(k_v-1)^2-A_2,\qquad
E_3=b(h_v-1)^3+c(k_v-1)^3-B_3.
$$
不取 $\sigma$ 根，直接有
$$
E_2=\frac MU\left(\sigma^2-\frac DM\right),\qquad
\boxed{K=3UT\,E_2-U^2E_3.} \tag{5}
$$
因此由 (2)–(3)，$\widehat q,\widehat K$ 都有原 $q_2,E_2,E_3$ 的完整多项式来源。它们不是独立的不同谱根 norm 条件。

$M=-U^2$ 为单位且 $D$ 整，所以原 $\sigma$ 整。$\bar\lambda=0$、$\bar D=0$ 不在这里被删除。

## 5. 真 E1 给全 Q=2 图的单位 f² 头

仍使用完整原仿射恢复
$$
T_0=-2U^2,\quad \Phi=-2(U-1)^2,\quad
P_{02}=2U(U-1)(U+1),\quad J=2U(2-U),
$$
$$
G=\lambda P_{02}-(1-U)T_0,\quad
P_f=T_0(J-Q),\quad P_c=QP_{02}(U+T)-GT_0,
$$
$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\quad
V=\frac{Jf+bcQt-G}{Q},\quad
W_1=2Uf+\frac{T_0}{2}, \tag{6}
$$
$$
X=\frac{W_1-qV}{b(p-q)},\quad
Y=\frac{pV-W_1}{c(p-q)},\quad
A_1=2f-2V+2bct,\quad
r=X-(1-U)p-ct,\quad s=Y-(1-U)q-bt.
$$
这里 $p=1+\rho,q=1-\rho$，$bc=U^2/4$。全部实际分母只在
$$
U(U-1)(U+2)(2U-1)
$$
支持上或是特征 1009 非零常数；特别不逆 $P_{02}$、$m$、$D$、$\lambda$、$t$ 或 $f-U$。

由 $J-Q=\Phi$，完整普通 $f$ 系数为
$$
t_f=4,\quad V_f=2U,\quad X_f=Y_f=2,\quad r_f=s_f=2-2U. \tag{7}
$$
使用真 dual germ 乘法，$d_1$ 的 $f$ 系数为 $2-2U$，$(\mathcal Kd)_1$ 的 $f^2$ 系数为 $4U(1-U)$。因此
$$
\boxed{[f^2]E_1=-8U(1-U)+4(2-2U)=8(U-1)^2\in A^\times.} \tag{8}
$$
原 $E_1$ 其余系数整，故实际原解的 $f$ 必整，全部原 Gram 坐标也整。这一步在投影或有限域选列以前完成，不由计算 rank 反向推整性。

## 6. 新固定五阶 U 投影及全部常数域

$\widehat q$、$\widehat K$ 的固定 $\mu$ 容量为 2 和 3。源码采用五个原行
$$
\widehat q,\quad\mu\widehat q,\quad\mu^2\widehat q,\quad
\widehat K,\quad\mu\widehat K
$$
在 $1,\mu,\ldots,\mu^4$ 上的方阵 $S(U)$，定义 $F(U)=\det S(U)$。固定容量不随任何 $U$ 的头退化而改变。源码计算第零列的伴随余子式并逐五坐标返回
$$
F(U)=a(U,\mu)\widehat q+b(U,\mu)\widehat K. \tag{9}
$$
所有矩阵条目的 $U$ 次数至多 3，故 $\deg F\le15$。若实际 $F=0$，本门准确保留全部原纤维，不宣有限；若实际为非零常数，则 (9) 已是原单位来源。

此次实际 $F$ 非零、次数恰为 15，完整五坐标身份 (9) 已返回。其 canonical 定义有 16 项、65 字节，SHA-256 为
`0553ec5de8c46a65fefd617935f08f141b9bbb9d82b67d9bc1f408fb235407ac`。
这些参数由冻结源定义，不另存可重算系数。

完整 $\mathbb F_{1009}$ 因式分解逐项乘回，实际结果如下；编号采用源码固定排序。

| 因子编号 | 不可约次数 | 投影重数 | 完整分支处理 |
|---|---:|---:|---|
| 0 | 1 | 6 | 整域迫 $U=-2$，由 §2 完整排除 |
| 1 | 1 | 1 | 整个常数域进入十二原源返回 |
| 2 | 1 | 1 | 整域迫 $e=U-1=0$，已付赋值单位排除 |
| 3 | 2 | 1 | 整个二次常数域进入十二原源返回 |
| 4 | 5 | 1 | 整个五次常数域进入十二原源返回 |

每个未排除因子 $\phi$ 均取整个
$$
K_\phi=\mathbb F_{1009}[U]/(\phi),
$$
不挑一个代数根，也不把模因子解释成有理数因子。每次系数求逆均在全 $K_\phi$ 中乘回。

在这三个整域上，对真正专门化后的 $\widehat q,\widehat K$ 作完整 $\mu$ Bézout，
$$
g=a\widehat q+b\widehat K.
$$
因为 $\widehat q$ 的一次系数 $4(1-U)(U+2)^2$ 是单位，它不可能成为整式零。此次三个实际 $g$ 均首一次数 1；全部 Bézout 系数和短除乘积已返回，未倒某个未付的 $\mu$ 头以跳过它的零纤维。

本门的目的为赋值剩余点排除。投影幂次已经完整记录，各不可约剩余域的全部嵌入覆盖所有可能原剩余点。这里不声称原 $U$ 商约化，不给 scheme 长度，也不把模因子或模 $D$ 幂零升级为一个一般有理数理想结论。

## 7. 新有限原模型、十二源与最终普通多项式返回

在 $\deg g=d>0$ 的整域中，使用三个显示首一关系
$$
g(\mu),\qquad q_f=\frac{E_1}{8(U-1)^2},\qquad
q_\sigma=\sigma^2-\frac DM=\frac U M E_2.
$$
$q_f$ 对 $f$ 首一二次且不含 $\sigma$，$q_\sigma$ 对 $\sigma$ 首一二次且不含 $f$。它们给出真正的三角有限自由环境，基为
$$
U^j\mu^i f^a\sigma^b,\qquad
0\le j<\deg\phi,\quad0\le i<d,\quad0\le a,b<2.
$$
其 $\mathbb F_{1009}$ 维数为 $N=4d\deg\phi\le120$。只环境自由，不假定原条件商自由；所有 $\mu/f/\sigma$ 重数完整保留。

真实 Gram 与上一独立输入相同：
$$
R_0=(0,0,p,q),\quad R_1=(0,A_1,r,s),\quad
R_B=(p,r,0,t),\quad R_C=(q,s,t,0).
$$
乘法的 dual 系数必须是 $v_0z_1+v_1z_0$。取
$$
\tau(v)=(1-U)v_0+v_1+bv_B+cv_C,\quad
(\mathcal Kv)_j=\tau(R_jv),\quad
d=\mathcal K\mathbf1,\quad F_2=2f,
$$
$$
\mathcal N(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
 +2F_2\tau(v)^2+\tau(v\mathcal Kv),\quad
\mathcal P(v)=\tau((v-\tau(v)\mathbf1)^3).
$$
完整十二源为
$$
q_2,E_2,E_3,E_1,E_B,E_C,N_1,N_B,N_C,P_B,P_C,NV, \tag{10}
$$
其中 $N_1=\mathcal N(R_0+R_1)-\mathcal N(R_0)-\mathcal N(R_1)-4\lambda wP_{02}$，
$N_B=\mathcal N(R_B)-2\lambda P_{02}h_v^2$，
$P_B=\mathcal P(R_B)-P_{02}h_v^3$，$C$ 行同式，$NV=\mathcal N(1,w,h_v,k_v)$。源码先返回原 $E_0$、N0、P1、$F_2$ 和 (5)，保证所有行来自同一点。

每个十二源乘每个基元，依次做 $f$、$\sigma$、$\mu$ 的首一短除；每次都保留三首一关系的原十二源 tag，并逐普通多项式返回，得到完整 $N\times12N$ 原列。Gaussian 只作用于这些实际原列，唯一目标 $1$；没有把某个几何正幂替代单位目标。

此次三个整域均成功。合并全部实际列乘子后，在未取 $\mu/f/\sigma$ 商的普通环中实际准确返回
$$
\boxed{\sum_{i=1}^{12}\Omega_iF_i=1
       \quad\text{于 }K_\phi[\mu,f,\sigma].} \tag{11}
$$
(11) 涵盖 $K_\phi$ 的全部剩余嵌入及全部可能原根，故排除该整个剩余因子。实际三个环境如下。

| 因子编号 | $\deg\phi$ | $\deg_\mu g$ | 环境维数 | 原列数 | 实际 rank | 最终原目标 |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 4 | 48 | 4 | $1$ |
| 3 | 2 | 1 | 8 | 96 | 8 | $1$ |
| 4 | 5 | 1 | 20 | 240 | 20 | $1$ |

合计 384 个完整原列、384 次原短除、32 个 Gaussian 坐标返回与三个最终普通十二源返回均已完成。更具体地，最终非零乘子全部来自 $q_2,E_2,E_3,E_1,E_B$；其余七个实际乘子为零。没有把较少的最终支撑误记成未构造其余原列。

任意假设原解在本图已有 $\mu,f,\sigma$ 及所有原系数整性；其剩余因此必落在上述完整不可约常数域的某一嵌入中，并满足同一点的十二原式。恒等式 (11) 对每种嵌入都保持，产生矛盾。因此整个 $v(m)>0,\bar Q=2$ 边界关闭。实际 retainedFields 为空，未留下一条未返回的原纤维。


## 8. 整 m 结论和两个新整单位

§2–7 排除整个第二图，§1 引用已成第一图，故当前范围内不存在 $v(m)>0$。因 $m=u-\ell$ 已整，
$$
v(m)=0.
$$
再用原准确等式
$$
m=\frac{u(k+2)(Q-2)}{kVbar},
$$
其中 $u,k,Vbar$ 为单位，$k+2,Q-2$ 皆整，有
$$
0=v(m)=v(k+2)+v(Q-2).
$$
两项非负，故分别为零。这一步得到的是所有原 1009 位置的三个整单位，不只三个有限域样本的非零性。

此定理不宣称当前全部 W/b0 原解不存在，也不增加规范点数或 scheme 长度界。它支付后续原估值中三个明确权分母的整单位性；其余内部权边界继续保留。

## 9. 唯一实际执行、原来源及工程边界

源：[新整剩余域原返回](../notes/2026-11-29-unit211-W-b0-internal-m-positive-Q-two-complete-original-residue-fields-8542.py)；派发前输入：[完整原图及整性](../notes/2026-11-29-unit211-W-b0-internal-m-positive-Q-two-complete-original-residue-fields-8542-input.md)；小回执：[唯一实际记录](../notes/2026-11-29-unit211-W-b0-internal-m-positive-Q-two-complete-original-residue-fields-receipt-8542.json)。

源 blob `8634ac81c968927a6a227f2acc881fd2a95a8cfb`，19195 字节，SHA-256
`783208e869a0daecb194439a0ef09c698424f1020d7188ebd7b0334891997e6d`。
零源码依赖，固定 120 秒 / 1 GiB，外层 135 秒。源和输入先经 root 及独立 peer 全文静读；只发生这一次数学执行，无旧投影、四维门或 N5 门重播。

唯一 [run 46184328225 / job 141100717128](https://github.com/Rogerhu12/math-research-public/actions/runs/46184328225/job/141100717128)：

| 项目 | 实际记录 |
|---|---|
| driver elapsed | 2.6567879320000003 秒 |
| 数学最后完整 stage | 2.5853332410000007 秒 |
| 峰值子进程 RSS | 39408 KiB |
| 内层退出 | 0 |
| 数学记录 | 14 行 |
| 完整 U 投影 | 次数 15，固定五坐标返回 |
| 全因子乘积 | 已返回 |
| 实际关闭整域 | 1、3、4 |
| 已付缺席整域 | 0、2 |
| 未返回整域 | 无 |
| 全原列 / 原短除 | 384 / 384 |
| 全域系数逆 / 原首一关系 | 117 / 9 |
| 普通十二源最终返回 | 3 次 |
| stdout | 23850 字节 |

stdout SHA-256：
`289cb46058a86808aa0ff7af55a1e37543b191a1f591786834ec273f07a16d5a`。
本文作者亲读唯一 job 的全部数学行，并按行重组 stdout 后逐字节核得该字节数与 SHA。

source commit 为 `2df05945997be8717912b04692b834846f1775fd`；
实际 pull 后 commit 为 `52937a89ed7db0955993c22230239f8a414d5651`，
时间 2026-11-28T20:03:20.574819Z。两 README 分别为
`99c5ad8d06e939e6cfbbab1afdeffa5463f15f18`、
`5fbd905291dd044c88d35bd9c07ac0e586ff795a`，实际规则无变。

本次代码中的“noSmallMOrDOrLambdaOrP02Inverse”准确指小写 $m$、$D$、$\lambda$、$P_{02}$ 未反演；大写 $M$ 在该命名图中已先证明单位，合法用于原二矩首一化。实际源、输出和冻结输入字节均保持不变。§2 新增的精确 $A_*=0$ 纸面分支只完善完整覆盖，没有补跑或修改已成计算。
