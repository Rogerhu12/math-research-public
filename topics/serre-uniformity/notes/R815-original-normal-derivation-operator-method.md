# R815 执行契约：原 Wronskian 乘法与272维正规连接

日期：2026-11-15。状态：**执行契约；本任务尚无新的乘法矩阵或连接输出。**
证明依 R813 的原 Wronskian、cyclic唯一性和确定性准确点定理；
两图正则导子及下游消费者依 R814。
本任务只准备 $M_g,M_h,\Gamma$，不输出极理想、cusp理想、五函数DAG、$\eta$或高度。

## 1. 固定范围、源码和真实输入

- RESULT：R815-original-normal-derivation-operators。
- FINAL：p41-original-normal-derivation-operator-certificate.json。
- core：R815_original_normal_derivation_operators.py。
- CLI：--config --proof --method --retained --output --budget-minutes。
- proof：原 R813 证明；method：本契约。
- 首次固定三个目标 g,h,Gamma；核心300分钟、job350分钟，可同核续算。
- python-flint固定0.9.0，所有新算术只在本公开仓库Actions。

源码直接导入已审 R811 核心
R811_original_regular_multipliers.py，
SHA256 849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3。
复用准确有理重构、有限域插值、原 $M_w$ 装配、
点/Krylov缓存、CRT当前状态、小历史及分块候选恢复。
新子类必须真正覆盖 R811 的初始化、R809适配器、r5目标和终验：
不把 R813 文件改名假装成 R809；$\Gamma$不被冒称为一个与$M_w$交换的乘法矩阵。

只消费两组真正成功的producer：

| 源 | 实际必需数据 | 本任务不重做 |
|---|---|---|
| R806 | 34组完整原 $M_w$ 坐标、polynomial index、原cyclic witness、chart/accepted/definition与metadata | 原690块、筛选、Dixon、原cyclic秩 |
| R813 | 两列690维准确坐标及原column scale、normal interface、同一S3/原基的来源与metadata | 两个Wronskian卷积、原820行求解及旧模逆 |

R806 已真实完成，实际 $w_0=e_2$ 来自其证书；
实现仍读取真实定义，不由候选号猜坐标。
R813 仍运行时请求保持 pending，不能用理论正确或静态review填成功SHA。

## 2. 原两个有理 normal 向量

原
$$
g=\delta z=G/\tau^3,\qquad h=\delta w=J/\tau^3,\qquad
\delta=\tau^{-1}D_0,\quad D_0=(q_Y/82)d/dq_Y.
$$
R813 两列坐标的读法必须完整为
$$
\frac{\text{coordinate numerator}}{\text{column denominator}}
\cdot\text{original target rational scale}.
$$
按原 S3 行次序 $(a,j)$ 放入
$\sum_jv_{a,j}z^j$，其中 $j\le3-\epsilon_a$。
有理scale只乘一次；不补回任何已去content，
不新增 $82^2$，不把两个Q列扩成14列L字段任务。

得到的两个输入为Q系数、rank272、degree bound3。
它们的首项、零系数和源完整820行认证都必须保留。
$\Gamma$的首列零是导子约束，不是“整个目标向量为零所以矩阵为零”。

## 3. 基身份与目标身份分开

公共基标签包含 core/proof/method/framework SHA、
原R806的run/source/core/manifest/cert、
原polynomial multiplier、cyclic witness、
实际free-basis身份、$\epsilon$、$z$、原$\sigma$整数参数、
矩阵列方向、prime起点及准确终验规范。

g/h目标各绑定真实R813 producer、
exact-coordinate stage、normal interface和0/1列。
Gamma目标绑定同一两输入及方程
$[\Gamma,M_w]=M_h-M_gM_w'$、$\Gamma e_0=0$。
实际用于Gamma的已成$M_g,M_h$文件另外在每个相关stage保存完整SHA引用。

预算、传输artifact地址和后继消费者不改变公共数学身份。
所有R815点stage另保原R806及free-basis来源，
使未来R811可以通过真正的外部cache adapter读取。
不改tag、不改producer label来伪装已有点是另一个任务自产。

## 4. g/h：六点模插值、七点准确交换子

对 $f=g,h$，
$$
\deg(M_f)_{ba}\le3+\epsilon_a-\epsilon_b\le5.
$$
每个可用素数共用同一原 $M_w(t)$ 和cyclic逆缓存。
按R811原顺序寻找6个不同好点：
原成功$z_0$优先，随后非负整数。
若原R806成功点的同一prime/z0已经给Krylov矩阵，
原矩阵直接读回，仅新增尚未算过的逆及两边乘回。

每点以
$$
M_f(t)=
(v_f(t),M_w(t)v_f(t),\ldots,M_w(t)^{271}v_f(t))
\mathcal K(t)^{-1}
$$
求真实模像，再核首列及完整模交换子。
六点插值后逐项核更细的weighted支持；
超界项必须为零，不能截断掉一个实际非零系数。

CRT只保每目标当前完整向量及小历史；
一个模像仅在CRT原子提交、双同余逐项核后才可裁掉其临时大表。
公共Krylov点缓存保留给三个真实消费者共用。
准确重构使用固定对称矩形
$|a|,b\le\lfloor\sqrt{(M-1)/2}\rfloor$，
接受条件仍是完整准确恒等式，不是模数够大。

终验先逐多项式系数核首列等于原$v_f$。
交换子每项次数最多6：
$$
\deg(M_fM_w-M_wM_f)_{ba}
\le4+\epsilon_a-\epsilon_b\le6.
$$
所以必须在固定整数点 $0,\ldots,6$ 的全部7点，
逐272×272矩阵、逐行块准确清分母验零。
这等价于全部系数为零；
这些终验点不要求cyclic，也不使用随机通过代替证明。
cyclic唯一性于是识别为原真实$M_g,M_h$。

## 5. Gamma：五点模插值、六点准确非齐次恒等式

先复用已经准确完成的 $M_g,M_h$。
在一个好点写
$$
W=M_w(t),\quad \dot W=M_w'(t),\quad
k_0=e_0,\ d_0=0,
$$
$$
k_{j+1}=Wk_j,\qquad
d_{j+1}=\dot Wk_j+Wd_j.
$$
这里$d_j$是原$M_w(z)^je_0$的导数在$t$处的值。
由R813，
$$
\Gamma(t)k_j=jW^{j-1}v_h(t)-M_g(t)d_j,
$$
$j=0$的右端为零。
形成这些272列后右乘同一$\mathcal K(t)^{-1}$，
不构造特征零Krylov逆。
点上还须准确模核
$$
\Gamma e_0=0,\qquad
\Gamma W-W\Gamma=M_h-M_g\dot W.
$$

理论界是
$$
\deg\Gamma_{ba}\le2+\epsilon_a-\epsilon_b\le4.
$$
因此仅需5个模好点；它们可以是同prime的原6点grid的前5个，
全部点缓存仍逐SHA读取，不重新计算已有逆。
插值后核每个weighted界及全部首列零。

准确终验的残差
$$
\Gamma M_w-M_w\Gamma-M_h+M_gM_w'
$$
每项次数至多
$3+\epsilon_a-\epsilon_b\le5$。
所以用固定 $0,\ldots,5$ 的全部6点、逐行块准确验零，
并逐系数核$\Gamma e_0=0$。
乘法顺序是 **$M_gM_w'$**，不能换成$M_w'M_g$。

若写$\Gamma=A/d_A,W=B/d_B,M_g=C/d_C,M_h=E/d_E$，
可取
$D=\operatorname{lcm}(d_Ad_B,d_E,d_Cd_B)$，
在整数矩阵中核
$$
\frac D{d_Ad_B}(AB-BA)-\frac D{d_E}E
+\frac D{d_Cd_B}CB'=0.
$$
所有分母、源矩阵和每个行块见证都保存。
两个满足方程和首列零的连接之差与$M_w$交换并杀$e_0$，
故cyclic性给唯一性。这认证整个原$\delta$，不需要数值微分或原高阶torsion。

## 6. 两图输出与必要负号

g/h两个r3截面的齐次第二图乘法矩阵为
$$
M_{F/\sigma^3}(t)=t^3D(t)M_{F/\tau^3}(1/t)D(t)^{-1},
\quad D(t)=\operatorname{diag}(t^{-\epsilon_a}).
$$
逐条反转weighted系数并保完整分母。
这个“同截面齐次化”与“同函数运输”须分别标明。

R814的第二图改用正则导子
$\delta_\sigma=t\delta_\tau$，所以
$$
M_{\delta_\sigma t}=-t^3D(t)M_g(1/t)D(t)^{-1},
$$
$$
\Gamma_\sigma=
tD(t)\Gamma(1/t)D(t)^{-1}
-t^2D(t)M_g(1/t)D(t)^{-1}\operatorname{diag}(\epsilon).
$$
必须保首式的负号。
Gamma第二图不是简单反转；
每项可能产生的$ t^{-1}$系数须准确相消，
然后才记录多项式连接与原weighted界。
可以用已有g第二图block加明确标量$-1$表示底变量导数，
不必复制一份仅差负号的大矩阵。

本任务不把h的r3齐次第二图矩阵误叫作
$\delta_\sigma(w_0/\sigma)$；后者有另一个乘积项。
所有后继输入明确导子、底变量和基。

## 7. 数据形状、断点和仍然存在的成本

不计实际偶然零，weighted存储的有理系数位置数为：

| 对象 | weighted阶 | 系数位置数 |
|---|---:|---:|
| $M_g$ | 3 | 295936 |
| $M_h$ | 3 | 295936 |
| $\Gamma$ | 2 | 221952 |

这是存储界，不是实际非零项统计。
矩阵按16个输出行一块，共17块；
每块保存共同正分母与
“输出行、输入列、幂次升序”的整数扁平数组。
gamma block采用自身阶2；
不得按r3解读。

每个完整目标包含：
来源、全部tau/sigma block SHA、
真实CRT prime数/模数bit、
首列准确证书、
全部7或6个准确点及17行块见证、
cyclic唯一性和未完成事项。
Gamma另含实际$M_g,M_h$来源、
非齐次式及两图修正的准确证书。

源$M_w$有很大的有理系数；
点缓存、CRT、准确点大整数乘法和输出体积都是真实成本。
不能保证一次300分钟完成。
完成目标/点/行块不重算，只保存当前大CRT；
任何临时模像裁剪必须在原子CRT提交之后，
并保原文件名/bytes/SHA小历史。
如果实际存储成为限制，只作明确、同数学身份的续算适配，
不能静默删除仍被消费者需要的旧矩阵后再重算它。

当前只做这三个实际需要的算子，
不构造ambient场迹全表、不生成全$k(z)$ Krylov逆，
也不生成272个无消费需求的普通基乘法表。

## 8. 最终完成字段

只有三目标都准确完成，FINAL才置complete=true。
至少输出：

- original_Mg_and_Mh_computed=true；
- original_normal_derivation_connection_computed=true；
- all_three_weighted_supports_and_original_first_columns_verified=true；
- all_complete_polynomial_defining_identities_verified=true；
- g/h的准确7点和Gamma的准确6点；
- 同原正规基的两图矩阵/连接索引；
- original_cusp_zero_ideal_computed=false；
- original_function_DAG_polar_divisors_eta_or_height_computed=false。

最后两个false避免把R814或后继的算法证明当成实际数据。
source-bound一日bundle只含直接所需原阶段；
Git/Release不保存这些可重算矩阵或证书，
仓库只记脚本、参数、run、SHA和真实结论。

来源（2026）：本仓库R805/R806、R809、R811、R813、R814。
数学认证边界已经由这些完整证明给出；本任务只新增相应实际算术。

