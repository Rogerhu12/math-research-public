# R442 固定准确 C 目标的完整有限 M 模态派生与深尾范围

- 作者：AI，GPT-6 Astra Pro，exact_refinement
- 日期：2026-11-16
- 状态：本稿给出条件性的完整有限模态深尾包含证明和源级维度合同。未选择实际 M，未运行新的科学计算，未取得新的接受场、原生 DN、同场 metric 或闭曲面证书。

本文固定 [R286](R286-original-stored-continuous-integral-and-metric-bridge.md)、[R312](R312-continuous-C-complete112-zero-tail-and-head-connection.md) 的准确连续对象、全部原允许根序列，以及实际连续十参数族的准确 DAG。只增加明确有限的模态数 M。空间网格、角求积、材料角和原生 RK 步数须随真实请求记录；它们不是准确标量目标的参数，但会改变有限计算及其来源身份。

这里不把 R312 原有的 112 模态统一常数直接用于更高频率。R312 的谱、投影和 Green 估计本来对每个 ν≥1 成立；其中平台与短段的统一扰动估计明确用了 m≤224。本稿重付后一项，并保持实际端口 F=159、physical node160 和原完整1440片有限头。没有通过提高 F 而略去新增的真实深胞元。

## 442.1 准确对象与有限计算身份

令 M≥112 是明确有限整数，所求全部频率为

$$
m=2,4,\ldots,2M,\qquad
\nu_m=\frac{m^2(m^2-1)}{12}\ge1.
$$

同一 source cell 的原 mode2 准确根 α_n 只选一次，所有频率共享它。仍允许 R312 的整个根族；不因 M 改变而重新选根，不将 α_n 换成65/64。原浅层保存数据、六 primitive、C 的原三输入、λ、真实 cut、自然外端和 root-family 声明全部保持。

准确十族的标量 DAG、core 几何输入、δA、δB、d、κ、全部十个准确有理系数和每个实际支撑，也不因 M 改变。现有数值 profile 的 field_modes 与 tail_modes 是有限场表示元数据；其导出 specification 包含这些字段，故 specification 的完整身份随 M 改变。不能仅因准确标量函数相同而复用旧 specification SHA、旧 J、旧 native 状态或旧几何证书。

准确 C 和标量参数相同也不自动固定完整闭面 g。当前 embedding core 决定材料映射 Φ；后继改变 core 时，材料拉回必须按实际新旧映射处理。全闭面还需要固定首次 construction 的 W、cap_height、所有 marker 原词，以及材料、运输和尾帽选择。本文的 M 派生不暗中完成这些额外责任。

## 442.2 不使用224上界的九因子扰动

保持 R312 的记号

$$
B(p)=
\begin{pmatrix}\beta&\nu/p\\-p&-\beta\end{pmatrix},
\quad
\beta=\frac{m^2-4}{\sqrt{12}}\ge0,
\quad
\kappa_m^2=\frac{7m^2-16}{12}>0,
\quad B(p)^2=-\kappa_m^2 I.
$$

全部矩阵范数为诱导列和范数。定义准确整数上界

$$
m_*:=2M,\qquad
\nu_*:=\frac{m_*^2(m_*^2-1)}{12},\qquad
b_*:=m_*^2,\qquad
A_*:=2\nu_*+b_*+64.
$$

因为 m 为正偶数，ν_* 是整数；并且对所有请求频率有

$$
\nu\le\nu_*,\qquad
0\le\beta<b_*,\qquad
0<\kappa_m^2<b_*.
$$

在原整个九段上，α∈[1/2,2] 与单调 quintic 对数插值给 δ/2≤p≤64/δ。因为0<δ<1，

$$
\|B(p)\|_1
 =\beta+\max(p,\nu/p)
 \le\frac{A_*}{\delta}.
$$

六个短段每个长度 cδ，所以它们的全部积分范数之和至多

$$
\ell:=6A_*c.
\tag{442.1}
$$

三个平台的准确指数仍是

$$
\exp(\delta B_i)
 =\cos(\kappa_m\delta)I+
       \operatorname{sinc}(\kappa_m\delta)\delta B_i.
$$

R312 的三个有序 shear 分别是 N1、N2(α)、N3。写 δB_i=(N_i−I)+D_i，可逐平台保留全部非理想项，得到

$$
\|D_i\|_1\le\beta\delta+2\nu\delta^2
 \le b_*\delta+2\nu_*\delta^2.
$$

令 $s_i=\|N_i\|_1$。仍有 $s_1=65$、$s_2=1+\alpha\nu\le3\nu$、$s_3=2$，故 $s_1s_2s_3\le390\nu$。使用准确实不等式

$$
|\cos x-1|\le x^2/2,\qquad
|\operatorname{sinc}x-1|\le x^2/6,\qquad
|\operatorname{sinc}x|\le1
$$

并利用 ||N_i−I||_1≤s_i，得到每个平台的相对误差

$$
\frac{\|\exp(\delta B_i)-N_i\|_1}{s_i}
 \le\frac23\kappa_m^2\delta^2+\|D_i\|_1
 \le e:=b_*\delta+(2\nu_*+b_*)\delta^2.
\tag{442.2}
$$

这一步没有交换原九个矩阵的次序。逐因子差分给

$$
\|\Phi_{m,n}-N_3N_2(\alpha_n)N_1\|_1
 \le390\nu_*
    \{\exp(\ell)(1+e)^3-1\}.
$$

令 $v=\ell+3e$。若 v≤1/2，则 (1+e)^3≤exp(3e)、exp(v)−1≤2v，故

$$
\|\Phi_{m,n}-N_3N_2(\alpha_n)N_1\|_1
 \le780\nu_*v.
\tag{442.3}
$$

原准确根偏离参考值的估计不依赖请求模态数。对全部 n≥160，R312已证

$$
|\alpha_n-65/64|
 <2^{14}c_n+2^{11}\delta_n^2.
$$

三个 shear 的实际有序乘积因此满足

$$
\|N_3[N_2(\alpha_n)-N_2(65/64)]N_1\|_1
 \le130\nu_*(2^{14}c_n+2^{11}\delta_n^2).
\tag{442.4}
$$

端口 diag(1,2^{-11/4}) 的范数等于1。归一矩阵 A_{m,n}=−2^{-11/2} T_hat_{m,n} 的缩放因子小于1/32。于是

$$
\|A_{m,n}-A_{m,0}\|_1
 <
 \frac{780\nu_*v+
  130\nu_*(2^{14}c_n+2^{11}\delta_n^2)}{32}.
\tag{442.5}
$$

## 442.3 F=159的明确适用范围

原参数范围给全部 n≥160 上

$$
c_n\le c_*:=2^{-84},\qquad
\delta_n<\delta_*:=2^{-163}.
$$

定义以下准确有理数：

$$
\ell_*=6A_*c_*,\qquad
e_*=b_*\delta_*+(2\nu_*+b_*)\delta_*^2,
\qquad v_*=\ell_*+3e_*,
$$
$$
\boxed{\quad
\varepsilon_M:=
 \frac{780\nu_*v_*+
  130\nu_*(2^{14}c_*+2^{11}\delta_*^2)}{32}.
\quad}
\tag{442.6}
$$

**适用条件是 v_*≤1/2 且 ε_M≤1/64。** 两个条件只用明确整数和二幂有理数，Actions实现可准确核验，不依赖浮点谱或采样。本文不声称固定F=159对任意大的M无条件有效；若条件未付，新深尾生产器输出完整请求频率和未开始后缀，不假造其 far 行。这是本定理的适用范围，不是对某个未求非零场新增接受门。

在该条件下，对每个原允许根序列、每个请求频率和全部n≥160，

$$
\|E_{m,n}\|_1
 <\varepsilon_M\,2^{-(n-160)/2}.
\tag{442.7}
$$

理由是 c、δ、δ² 的每一项在n增长时至少按2^{-(n-160)/2}衰减，(442.6)的所有系数非负。可用更紧的实际参数上界，但本合同只采用上面统一常数；并未以名义参数中心替全根族。

## 442.4 完整M模态半线与深端图

R312的理想矩阵

$$
T_{m,0}=
\begin{pmatrix}
1-65\nu&(65/64)\nu\\
65d(\nu-1)&d(1-(65/64)\nu)
\end{pmatrix},
\qquad d=2^{-11/4},
$$

对所有ν≥1都有相同的完整谱估计：

$$
64\nu\le L_m<66\nu,\qquad
0<S_m<1/(64\nu),\qquad
\|P_u\|_1<2,\quad\|P_s\|_1<3,
$$
$$
\lambda_u=2^{-11/2}L_m\ge\sqrt2,\qquad
\lambda_s=2^{-11/2}S_m<2^{-11},\qquad
\|\mathcal G\|<9.
$$

这些证明只用了ν≥1，没有使用ν的224频率上界。全部M个二元块取有限直和、每节点取块ℓ1和，再对节点取上确界，仍保同一个Green范数。

采用与R312完全相同的有界类和边界规范

$$
X_n=(-1)^n\delta_n^{-11/2}(Q_n,\Pi_n/\nu),\qquad
P_uX_{159}=v_m z,\quad
v_m=(1,s_m),\quad
-d<s_m\le0.
$$

(442.7)给收缩常数9ε_M≤9/64<1。故对每个固定原根序列、每个完整M维z，有唯一有界解；未消去任何模态、均值或有限头责任。

当z=1时，||v_m||_1<5/4，深端偏差属于P_s。于是

$$
\|X_{159}-v_m\|_1
 <
 \frac{3}{1-2^{-11}}\,
 \frac{5/4}{1-9\varepsilon_M}\,\varepsilon_M
 <5\varepsilon_M.
\tag{442.8}
$$

最后严格不等式可直接在ε_M≤1/64处用有理数核验；没有采用新的数值特征向量。特别地X_{159,1}>1−5ε_M≥59/64>0。商差因此有保守统一界

$$
\left|\frac{X_{159,2}}{X_{159,1}}-s_m\right|
 <20\varepsilon_M.
\tag{442.9}
$$

例如先用分子≤(5/4)||X−v_m||_1及分母≥1−5ε_M即可得到比20更小的常数；这里保留原生产器的20倍误差形式。

因此全部M条原坐标深尾关系均为

$$
\Pi_m=\nu_m\mathfrak g_{m,159}Q_m,\qquad
\mathfrak g_{m,159}\in
 [s_m-20\varepsilon_M,s_m+20\varepsilon_M].
\tag{442.10}
$$

$m=2$仍因原每层准确校准而有 $\mathfrak g_{2,159}=0$：其真实传递上三角，归一第一对角由ε_M≤1/64保持模大于1，故Pi=0列属于同一有界类，再由唯一性得到准确零。此结论不属于有限RK校准的近似根，也不把浅层binary64根改为准确根。

对于每个固定有限M，R312的胞元内传播及cuff两jet衰减证明逐模态照用，其常数可依赖M。有限角和保持C²零延拓。这里没有转成无限频率统一角解析结论，也没有从线性高度的C²延拓推出完整非线性mean、帽、嵌入或reach。

## 442.5 原有限头与正端点Prüfer责任

新深端仍F=159，故原160个source cell、每个九片，共1440片有限头全部进入后继。原准确C全root-family、实际自然域和cut逆像不改变。对每个新增m仍使用完整物理方程

$$
\frac{d}{dr}\binom uk
 =
\begin{pmatrix}
0&1\\
m^2w_r/(rw)&-w_r/w
\end{pmatrix}\binom uk,
\qquad
\det\Psi_m(r_1,r_0)=w(r_0)/w(r_1)>0.
$$

R380全实角lift、正幅度、二幂换帧与正端点算术均逐模态保留。全部cut/far候选先按实际同一角和w形成相关行，再作全族包含。名义数值行依R419只作完整有限系统的实际坐标代表；不能把参数盒中的名义点称为某个已选全局C成员。

完整Robin行不需要高度投影非零；DN商仅在该模态完整高度盒严格隔零后另付。增加M不会自动给出新模态的DN，也不把原112条行补零作为新增行。有限头的资源截止、角lift未付、自然域未付和height分母未付分别记真实范围。

## 442.6 全维数合同与无伪高模零

使用原频率间隔2、原576个native stage和577个节点。所有尺寸随实际M一致变化：

| 对象 | 完整维数 |
|---|---:|
| 原角root乘子 | 2M+1 |
| 每stage完整状态，含两均值 | 2M+2 |
| native非均值状态及stage J | 2M、2M×2M |
| 完整far Robin矩阵 | M×2M |
| 全节点对M个高度的灵敏度 | 577×2M×M |
| 物理prefix状态r/t/z | 3M+2 |
| 完整endpoint物理J | (3M+2)×M |
| 固定全部十参数的平方BVP | 4M+2 |
| 三个active参数的平方BVP | 4M+5 |
| 左边界，k个active参数 | 3M+2+k |
| 右边界 | M |
| 核心和tail模式计数 | K=k、T=M |

物理prefix顺序仍为r0..rM、t1..tM、z0..zM；增广core为随后M项。旧M0初猜嵌入M≥M0时，必须把这三个不同块和增广core分别拷贝到新的真实偏移，保r0/z0两均值；不能把旧4M0+2向量作为新向量的共同前缀。新高模初值可明确置零，但这只是初猜。随后每个新模态的完整RHS、J、boundary、H、FD、final audit以及nativefar均真实重算。

原generic Householder前缀QR可复用，因为它对完整增广矩阵与所有右端列一起正交变换，循环来自实际矩阵形状。同步桥、QR包装器和native owner各自原来的112/224常量必须同时独立派生；单改外层schema不足。完整affine行、far/cut行、两mean传播和所有M个灵敏度右端均保留。

原32次非线性迭代、每次10档真实noJ回溯、严格完整残差下降、2e−9以及原FD/fullDN/fresh audit责任不因M变化而放宽。这里不将已有局部隐式J称为R411的有限root匹配J；使用哪个真实引擎必须保其原源码身份和范围。

## 442.7 检查点、来源与后续几何

新profile、writer、reader、SavedPrefix和后续radial/shared入口须实际读取M、N及分辨率记录，独立绑定来源。完整record至少包含

- field_modes=M；
- field_angular_quadrature和native_quadrature，按本条实际同N合同；
- native_steps_per_stage；
- material_angles、physical_angles；
- native_stage_count=576。

旧检查点只可经其原reader真实读取。新检查点以新writer/schema保存全部真实数组和mean、实际target、owner/source闭包、原参数和当前M；不能把旧actual_driver_source改名。完整scientific bytes可重算且仅在本次Actions namespace中保留；退出、必要读回、原clock和quiet按原生命周期合同。

若重建后的SavedPrefix、radial、atlas、shared或metric/reach消费者尚未适配，必须明确该项未完成；仅有新writer/native源不能冒全部几何可执行。即使它们已适配，旧场的几何证书也不得迁移到新M场。每个实际新checkpoint需要重新执行相应完整消费者。

## 442.8 本稿实际范围

本稿付的是固定F159下显式有限M适用条件、全根族深端包含以及全链必须保持的维度和准确目标责任。科学源实现可据此采用准确有理条件、原Arb外包、原全模态有限头和真实全J/FD入口。源码、proof和当前运行身份仍分别登记。

本次没有选择M、角网格、参数、λ、未来parent或run；没有本地科学、编译、导入、AST或fixture。只做源文本和纸面证明。未返回的计算、清理后失去的现场和旧hash均不能用来伪造接续。
