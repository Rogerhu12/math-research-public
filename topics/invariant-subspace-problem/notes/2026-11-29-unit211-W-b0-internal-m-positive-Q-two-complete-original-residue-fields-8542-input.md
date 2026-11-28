# W/b0 内部 m 正阶、Q=2 整剩余图：新五阶投影与十二原源有限模型

日期：2026-11-29（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 命名范围、已付赋值单位及唯一新目标

固定剩余特征 $p=1009$，取当前正确 W、完整 $b_0=0$ 物理图的一个赋值位置。本输入只处理
$$
v(m)>0,\qquad \overline Q=2.
$$
不是把原特征零权曲线施加 $m=0,Q=2$。以下所有带横线的式均为原解已经证明整的系数在该位置的剩余；未带横线的原式仍作为整性论证的来源。

已刊原结果给 $e,k,u=e+1,\delta=1-Q,Vbar=uk+2$ 全为赋值单位，$\ell$ 整：

- [e、k、u 整单位](../results/R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)；
- [全 ell 整](../results/R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)；
- [整个 delta 正阶排除](../results/R150-appendix-unit211-W-b0-entire-delta-positive-exclusion-and-1009-integral-unit.md)；
- [整个 Vbar 正阶排除](../results/R150-appendix-unit211-W-b0-entire-Vbar-positive-exclusion-and-1009-integral-unit.md)。

原等式
$$
m=\frac{u(k+2)(Q-2)}{k(uk+2)}
$$
把内部 $m$ 正阶分为 $\bar k=-2$ 与 $\bar Q=2$，交集会迫 $\bar u=0$。第一图已由 [完整四维真 Gram 返回](../results/R150-appendix-unit211-W-b0-internal-m-positive-k-minus-two-entire-original-exclusion.md) 独立关闭。本次只接第二图，不重跑该四维门或任何旧射线、初始理想、投影、N5 门。

新计算先对两个完整同 $\mu$ 原必要式作一个固定五阶投影，再对每个完整 $\mathbb F_{1009}$ 常数因子保留全部 $\mu$ 根、$f$ 根及谱根，构造最多 120 维的真实有限模型。唯一目标是 $1$；最终必须合回完整十二原多项式。若任一环节或原单位目标未返，该整域保留。

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

若 $A_*$ 正阶，则唯一 $U=-2$。设 $b=v(A_*)>0$、$s=v(\mu)$，并先允许 $\mu$ 有极点；由原 $b_0$ 有 $v(T)=s-b$。在 $s\le0$ 或 $0<s<b$ 时，$q_2$ 的 $T^2$ 项严格最低，矛盾。在 $s>b$（包括 $\mu=0$）时，其剩余常数为 $224\ne0$，也矛盾。剩下 $s=b$，此时 $\bar\mu=0$ 且 $T$ 单位，
$$
\bar q_2=64\bar T^2+224,
\qquad \bar T^2=-\frac72.
$$
$D,K$ 整，$M$ 单位与 $v(m)>0$ 使 $R_6$ 迫 $\bar K=0$；但
$$
\bar K=14+15\bar T+2\bar T^3=14+8\bar T.
$$
于是 $\bar T=-7/4$，与 $\bar T^2+7/2=105/16\ne0$ 冲突。所有明确常数在特征 1009 非零。因此整个 $U=-2$、$A_*$ 深零层已由完整原估值式排除，互补图可付 $h$ 为赋值单位。

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

否则第一次对 $F$ 作完整 $\mathbb F_{1009}$ 因式分解、逐项乘回，记录每个因子及其重数。仅当整个不可约因子迫已付
$U(U-1)(U+2)(2U-1)=0$ 时删除该整分量。其余每个因子 $\phi$ 都取整个
$$
K_\phi=\mathbb F_{1009}[U]/(\phi),
$$
不挑其中一个代数根，不把这些模因子解释成有理数因子。

在每个 $K_\phi$ 上，对真正专门化后的 $\widehat q,\widehat K$ 作完整 $\mu$ Bézout，
$$
g=a\widehat q+b\widehat K,
$$
其中 $g$ 首一。因为 $\widehat q$ 的一次系数 $4(1-U)(U+2)^2$ 始终为单位，它不可能成为整式零；因此 $\deg_\mu g\le2$，所有头降次与全部 $g$ 重数均保留。$g=1$ 时直接合回 (5)、(9) 的原三个源即可关闭该整剩余域。

本门的目的为赋值剩余点排除。$U$ 投影的完整幂次被准确记录；各不可约剩余域的全嵌入已覆盖所有可能原剩余点。本门不据此声称原 $U$ 商约化、给 scheme 长度，或无证把 $\phi$ 的幂零结构提升成全有理数理想单位。

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

每个十二源乘每个基元，依次做 $f$、$\sigma$、$\mu$ 的首一短除；每次都保留三首一关系的原十二源 tag，并逐普通多项式返回，得到完整 $N\times12N$ 原列。Gaussian 只作用于这些实际原列，唯一目标 $1$；没有为失败目标改用某个几何正幂。

若成功，合并全部实际列乘子，在未取 $\mu/f/\sigma$ 商的普通环中必须准确检查
$$
\boxed{\sum_{i=1}^{12}\Omega_iF_i=1
       \quad\text{于 }K_\phi[\mu,f,\sigma].} \tag{11}
$$
(11) 涵盖 $K_\phi$ 的全部剩余嵌入及全部可能原根，因此排除该整个剩余因子。若任何因子未返，整因子和实际 $g$ 全留。只有全部因子实际关闭或由既有明确单位排除后，才关闭整个命名的 $v(m)>0,\bar Q=2$ 边界。

## 8. 冻结源与预算

新自含源：
`2026-11-29-unit211-W-b0-internal-m-positive-Q-two-complete-original-residue-fields-8542.py`。

源 SHA-256：
`783208e869a0daecb194439a0ef09c698424f1020d7188ebd7b0334891997e6d`。

源 19195 字节，零源码执行依赖；固定首次 120 秒、1 GiB，建议外层 135 秒。只新增完整五阶原投影、该新剩余域模型和同点原目标。标准 Python 精确算术加 python-flint 0.9.0 的完整有限域因式分解；每个因子乘积、全部逆、所有短除与原组合都乘回。无旧 gate、历史大参数、可重算系数缓存、素数更换、预算追加或候选点重试。

本稿为派发前输入，未预记投影非零、因子次数、rank、单位返回或整个 $m$ 边界已闭。
