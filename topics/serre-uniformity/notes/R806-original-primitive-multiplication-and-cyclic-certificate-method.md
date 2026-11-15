# R806 原分次整基的 primitive 乘法与实际 Krylov 证书

日期：2026-11-15。状态：**准确算法及有限证书已证明；R805 的真实成功输出尚待绑定，以下没有新的秩、primitive 候选或运行结果。**

本任务只将 [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)
已经证明的原自由整基变成一个实际的 primitive 乘法矩阵。
先在同一个原690阶单位 minor 上筛选，再仅恢复成功候选的特征零坐标。
不生成全部幂基变换，不将 primitive 成功解释为极除子、Jacobian、刚性化或高度已完成。

## 1. 原对象、列约定与最小输入

保持原 $Y/K$、$K=\mathbb Q(\zeta)$、$g(Y)=127$、线丛 $\mathcal H$ 的次数272。
记 $e_i$ 为 R786 的原146条 M2 截面，使用已登记的整数尺度 $82^2$。
成功 R805 给出实际整数 $n$ 和无基点铅笔
$$
\tau=e_0,\qquad \sigma=e_1+n e_{73},\qquad z=\sigma/\tau.
\tag{806.1}
$$
此处不能预填 $n$、模素数或 minor。
一次补基固定为 $b_i=e_{i+1}$，$1\le i\le144$；
二次补基 $c_1,\ldots,c_{127}$ 是 R805 实际选出的原 V2 行。
原尺度分别为 $82^2$、$82^4$。

在 $U_\tau=Y\setminus\operatorname{div}(\tau)$ 上保持原正规整基
$$
\mathcal E=(1,b_1/\tau,\ldots,b_{144}/\tau,c_1/\tau^2,\ldots,c_{127}/\tau^2),
\qquad \epsilon=(0,1^{144},2^{127}).
\tag{806.2}
$$
其对应齐次分子记为 $d_a$，$0\le a\le271$，即 $d_0=1$。
原环是自由 $K[z]$ 模秩272；不能在后继处理中把可能非正规的 $K[z,w]$ 代替它。

直接消费两组原 producer：

- **R805**：真实完整证书、stage manifest、铅笔、分次补基、全部690条 S 基行、实际短 minor、原 alias 索引及此次确实复用的新单项式 stage；
- **R786**：原 p1、p2、p3 的146、418、690条行与原完整 manifest/证书，仅用其前41项和原 recipe。

R786 从 R805 一日输入包取出，逐 run/source/core/manifest/certificate/文件 SHA 与 R805 配置比较。
R775/R799 对三锚和原阶段的来源已由成功 R805 的完整证书绑定，本阶段不重求它们的秩。
R805 的完整源身份仍保留，不能用同名但不同次序的旧690维空间代替新 S 基。

原 S 基690条的顺序固定为
$$
\tau^3,\tau^2\sigma,\tau\sigma^2,\sigma^3;\quad
(\tau^2b_i,\tau\sigma b_i,\sigma^2b_i)_{i=1}^{144};\quad
(\tau c_j,\sigma c_j)_{j=1}^{127}.
\tag{806.3}
$$
所有行统一尺度 $82^6$。它们在原 $v$ 相位、$t_\xi=\xi+\xi^{-1}$ 中的
41项乘20坐标组成准确整数矩阵 $C\in M_{820,690}(\mathbb Z)$。
R805 实际行集 $I$ 给 $A=C_I$，并附某个素数下的非零行列式。
先读取这个既有见证，不能重跑已完成的选行或秩计算。

## 2. 每个候选的原272个乘法右端

选 $w_0\in V_1$，保存其原146个准确整数坐标，定义 $w=w_0/\tau$。
只从 V1 选候选，才能使全部
$$
P_a=\tau^{2-\epsilon_a}w_0d_a\in V_3,
\qquad 0\le a\le271,
\tag{806.4}
$$
仍落在同一已成690维原空间。每个右端有明确的原截面乘积生成见证，
不是因为一个有限前缀恰好能解就宣称它属于 V3。

先按排序后的 M2 叶索引查原 R786 p2/p3 recipe alias，
再查成功 R805 已成的新单项式。
只有两处均没有的乘积才新增原前41项卷积。
新积同时核原 qY/xi 与 v/$t_\xi$ 两种坐标，相位沿原 $\xi^{10m}$，
每个因子的整数尺度相乘为 $82^6$；已经完成的同一积不因候选或素数改变而重算。

对稠密整数候选，以这些单项式的准确整数线性组合形成右端，
不把相同叶积在每个候选中重新卷积。
初始候选 $e_2,e_3,\ldots$ 都没有额外场系数。
第一列 $P_0=\tau^2w_0$ 若已由 (806.3) 直接给出坐标，可只保存完整820行认证而省去 Dixon；
它仍计入全部272列，不减去该列的认证义务。

设 $x_a$ 为 $C x_a=P_a$ 的唯一坐标。
R805 的短前缀注入给其唯一性；(806.4)给存在性。
$C,P_a$ 均为准确有理数据且 $A$ 可逆，所以 $x_a\in\mathbb Q^{690}$。
这项有理性来自实际原矩阵，不将原标准截面的有理 Fourier 系数泛称为扭曲曲线上截面已在 $\mathbb Q$ 定义。

将 (806.3) 各项除以 $\tau^3$，从 $x_a$ 得到乘法矩阵
$$
w\mathcal E_a=\sum_b (M_w)_{ba}(z)\mathcal E_b.
\tag{806.5}
$$
**列是输入，行是输出，不能转置。** 其准确支撑满足
$$
\deg_z(M_w)_{ba}\le1+\epsilon_a-\epsilon_b;
\quad1+\epsilon_a-\epsilon_b<0\Longrightarrow(M_w)_{ba}=0.
\tag{806.6}
$$
S 基四/三/二个项分别读作同一整基行的 $z^0,\ldots,z^{3-\epsilon_b}$ 系数。
超出 (806.6) 的项必须逐项准确为零；先模筛时核其模零，特征零恢复后再核其准确零。

## 3. 先模筛选为何是原特征零的有效证书

取素数 $\ell\nmid82\det A$。
初次可沿 R805 的实际单位 minor 素数；若另选素数，只检查同一 $A$ 是否可逆，
不重新搜索行集。新保存 $A^{-1}\bmod\ell$ 及完整乘回见证。
已成的这个模逆是原矩阵的新解算输入，所有候选共用它。

对候选的272右端，求
$$
\bar X=(A\bmod\ell)^{-1}(P_I\bmod\ell).
\tag{806.7}
$$
必须在全部820行核 $\bar C\bar X=\bar P$，并按 (806.5)–(806.6)组成
$\bar M_w(z)\in M_{272}(\mathbb F_\ell[z])$。
由于 (806.4) 已给真实 V3 归属、$A$ 的行列式是 $\ell$ 单位，
原有理坐标 $A^{-1}P_I$ 的分母也为 $\ell$ 单位；
(806.7)正是原 $M_w$ 的准确约化，不是一个随意拟合的辅助矩阵。

选 $z_0\in\mathbb F_\ell$，实际形成
$$
\bar K_w(z_0)=
[\mathbf e_0,\bar M_w(z_0)\mathbf e_0,\ldots,\bar M_w(z_0)^{271}\mathbf e_0].
\tag{806.8}
$$
若实际 $\det\bar K_w(z_0)\ne0$，则原 $K_w(z)$ 的行列式不为零，
所以 $1,w,\ldots,w^{271}$ 是 $K(z)$ 上的基，且
$$
K(Y)=K(z,w).
\tag{806.9}
$$
这个结论没有要求特化纤维是 étale、没有要求 $\mathbb F_\ell$ 分裂原曲线，
也没有要求先求原曲线的高次平面方程。
它只用原自由模上实际乘法和真实非零 determinant。

每个失败特化只登记该 $(w_0,\ell,z_0)$ 的实际模秩或零 determinant。
一个失败的 $z_0$，甚至某个素数下所有试过的 $z_0$，都不能宣称原候选非 primitive。
特征零失败若要声明，必须另有准确的 $K(z)$ 秩证明；本任务不需要生成这种失败结论。

## 4. 有限见证的存在与公平搜索

原无基点铅笔使 $[K(Y):K(z)]=272$。
$\mathcal H$ 次数272大于等于 $2g+1$，其完整 V1 给嵌入，
因此在泛几何纤维的任意两个不同点上，至少一个 $b_i/\tau$ 取值不同。
考虑
$$
w_0(a)=\sum_{i=1}^{144}a^{i-1}b_i,\qquad a\in\mathbb Z.
\tag{806.10}
$$
每一对泛纤维点的相等条件是 $a$ 的一个非零、次数至多143的多项式。
故至多
$$
D=143\binom{272}{2}
\tag{806.11}
$$
个整数是坏参数，$a=0,\ldots,D$ 中至少一个给 primitive $w$。
这项界按全部几何点对计数，不把不同代数共轭点合并为一个条件。
$a=0$ 是初始候选 $e_2$，可直接 alias，不重算。

对原 $K_w$，由 (806.6)迭代得第 $j$ 列、第 $b$ 行次数至多 $j-\epsilon_b$。
因此
$$
\deg\det K_w\le\sum_{j=0}^{271}j-\sum_b\epsilon_b
=\binom{272}{2}-(144+2\cdot127)=36458.
\tag{806.12}
$$
一个 primitive 候选只在有限多个素数下失去这个非零多项式。
对足够大的好素数 $\ell>36458$，$z_0=0,\ldots,36458$ 中必有实际非零 minor。
小素数时不能把这些整数当作互不相同的剩余类；只枚举不同的 $z_0\bmod\ell$。

实现可先试简单原 $e_2,e_3,\ldots,e_{145}$ 和少数 $z_0$，
随后以确定性、可续接的公平顺序枚举候选、好素数和不同特化值。
每轮只增加尚未做过的三元组，已成模逆、候选模矩阵、特化秩全部复用。
公平枚举最终覆盖 (806.10) 的有限参数集合及某个足够好的素数和特化，
因而保证存在有限成功证书；不预设首候选、首素数或 $z_0=0$ 一定成功。
预算停止只表示保留前缀，绝不登记为原数学失败。

## 5. 只恢复成功候选的原有理乘法矩阵

找到实际 (806.8) 非零见证后，冻结同一 $w_0,\ell,z_0$。
只对该候选、同一 $A$ 和272个原右端做有理恢复；没有需求时不恢复失败候选。
允许按若干右端分组 Dixon，共用同一个模逆。

对每组保存模数 $m=\ell^k$、$X_k$ 和准确残差
$$
R_k=(P_I-A X_k)/\ell^k.
\tag{806.13}
$$
每轮取 $\Delta_k=A^{-1}R_k\bmod\ell$，再令
$$
X_{k+1}=X_k+\ell^k\Delta_k,
\qquad R_{k+1}=(R_k-A\Delta_k)/\ell.
\tag{806.14}
$$
每个除法须准确整除。只保每组最新大向量/残差、前项 SHA 与小阶段历史；
不保所有历史完整大向量而造成位数平方增长。

有理重构使用每轮固定对称界
$$
|a|\le B_m,\quad0<b\le B_m,\quad
B_m=\left\lfloor\sqrt{(m-1)/2}\right\rfloor.
\tag{806.15}
$$
因为 $2B_m^2<m$，同一剩余类在这个固定矩形中至多有一个既约分数。
不能以单个候选的 $2|ab|<m$ 代替唯一性条件。
模数增长最终容纳全部真实坐标；每次尝试必须准确核原 $A X=P_I$，
以及**完整820行** $C X=P$ 后才接受该组。
除选行外的130行不能删除，也不把已有有限域结果写作有理坐标。

最终重新从准确坐标构造 $M_w$，核所有 (806.6) 支撑、原 $82^6$ 尺度、
272列的实际原生成来源，以及 $M_w\bmod\ell=\bar M_w$。
把实际 (806.8) 和这个相等连接即可得到原特征零 primitive 证书；
无需再做庞大的特征零272阶 Krylov determinant。

## 6. 输出、断点身份与未完成边界

数学身份固定为原 core/proof/method SHA、R805/R786 全部 producer 身份、
原 S 行顺序、I、82尺度、候选编码和 prime/specialization 搜索规则。
预算、每轮允许扫描的范围、已经完成的候选数只是运行记录，
不得通过改变这些上限重复已完成数学。

按完整 stage 保存：原输入索引；新增且确有需求的单项式；各素数模逆；
候选272个生成右端或其准确组合；候选模乘法；实际特化秩/成功 minor；
成功候选的各组完整有理坐标；原 $M_w$；最后 certificate。
唯一允许 `complete=false` 的大数学文件是明确命名的当前 Dixon 向量 checkpoint，
它也绑定同一个 core、minor、候选、右端源 SHA 与实际位数。
已成有理组原子保存后，即使硬中断留下旧 current 文件，续接须先核同一组身份后删除旧 current，
不能为此重解已完成的有理组。

最终字段必须区分：

- `exact_polynomial_multiplication_computed=true`；
- `actual_cyclic_minor_certified=true` 与 `original_function_field_primitive_generator_certified=true`；
- `normal_integral_basis_preserved=true`；
- `characteristic_zero_Krylov_matrix_or_inverse_computed=false`；
- `M6_clearing_computed=false`、`original_function_DAG_computed=false`；
- `polar_ideals_or_KM_representatives_computed=false`；
- `actual_eta_rigidification_or_height_computed=false`。

后继需要把一个实际函数转换为 $K(z,w)$ 或求原整基中的商时，
才按真实右端形成/求解 $K_w$，全272坐标乘回认证。
本阶段不隐含已做这个可能很大的有理函数域转换，也不把 $K[z,w]$ 默认为整闭。
原两图过渡、M6清极、原 $b,\rho$、三同源主函数和刚性化常数仍沿 R805/R804 原接口。

所有新数学只在公开仓库 Actions。R805 未真实成功前请求保持 pending，
成功后只填真实 source/run/artifact/manifest/certificate/行 SHA。
大矩阵和向量仅供一日活跃 artifact 传递与续接；仓库只登记脚本、参数、run、SHA及实际结论。
