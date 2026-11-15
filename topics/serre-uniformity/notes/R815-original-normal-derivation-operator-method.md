# R815 执行契约：原乘法、正规连接与嵌套交换子

日期：2026-11-15。状态：**执行契约；尚无 R815 算术输出。**
本修订在首次运行前，以 R817 的嵌套交换子缩小已发布的初稿范围。
原 R813 两个 Wronskian 向量不变；实际重构目标只有 $M_g,\Gamma$，
不独立生成 $M_h$ 的 CRT 或完整多项式系数表。

证明依 R813 的原 Wronskian/连接次数界、R817 的唯一性认证；
两图正则导子和后继降重数消费者依 R814。
此任务不输出极理想、cusp 理想、五函数 DAG、$\eta$或高度。

## 1. 固定范围、源码和真实输入

- RESULT：R815-original-normal-derivation-operators。
- FINAL：p41-original-normal-derivation-operator-certificate.json。
- core：R815_original_normal_derivation_operators.py。
- CLI：--config --proof --nested-proof --method --retained --output --budget-minutes。
- proof：R813；nested-proof：R817；method：本契约。
- requested_targets 只有 g,Gamma；原 h 是必要输入向量。
- 核心300分钟、job350分钟，同核续算；python-flint固定0.9.0。
- 所有新算术只在本公开仓库 Actions。

源码直接导入已审 R811 核心 R811_original_regular_multipliers.py，
SHA256 849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3。
复用其严格有理重构、有限域插值、原 $M_w$ 装配、
点/Krylov缓存、CRT当前状态、小历史、分块候选恢复及普通$M_g$认证。
新子类真正覆盖原初始化、R809适配器、r5目标、十四列循环和$\Gamma$终验；
R813有自己的真实 producer，不改名假装成 R809。

| 源 | 实际必需数据 | 本任务不重做 |
|---|---|---|
| R806 | 34组完整原$M_w$坐标、polynomial index、cyclic witness、chart/accepted/definition与metadata | 原690块、筛选、Dixon及cyclic秩 |
| R813 | 两列690维准确坐标、原column scale、normal interface及同一S3来源 | 两个Wronskian卷积、原820行求解及旧模逆 |

R806 的实际证书给$w_0=e_2$，实现仍读其原146坐标并逐项核。
R813 尚未成功时请求保持 pending，绝不以证明或静态审阅代替真产物SHA。
预算与artifact传输身份不进入数学标签。

## 2. 原两个Q向量与尺度

原
$$
g=\delta z=G/\tau^3,\qquad h=\delta w=J/\tau^3,\qquad
\delta=\tau^{-1}D_0,\quad D_0=(q_Y/82)d/dq_Y.
$$
R813 的准确坐标必须完整读取为
$$
\frac{\text{coordinate numerator}}{\text{column denominator}}
\cdot\text{original target rational scale}.
$$
按原S3行次序$(a,j)$放入$\sum_jv_{a,j}z^j$，
其中$j\le3-\epsilon_a$。
scale只用一次，不补回已去content、不新增$82^2$、
不把两个Q列扩为14个L字段任务。
原源820行认证、零系数与非零标志全部保留。

原基次数为
$$
\epsilon=(0,1^{144},2^{127}),\qquad \beta_0=1.
$$
实际 R805 原 degree1 补基首项是 $e_2$。
连同R806实际$w_0=e_2$，给
$$
M_we_0=e_1,\qquad M_w'e_0=0.
$$
实现必须对已装配的原$M_w$逐系数核这个恒等式，
再使用$\Gamma e_1=v_h$；
不能仅看候选号推断列身份。

## 3. 来源与断点身份

公共基标签绑定 core/proof/nested-proof/method/framework SHA，
真实R806 run/source/core/manifest/cert、原polynomial index和cyclic witness、
原free basis/S3、$\epsilon$、原$\sigma$参数、矩阵列方向、
prime起点、块大小及准确终验规范。

g与h向量各绑定真实R813 producer、exact-coordinate stage、
normal interface和0/1列。
Gamma目标绑定这两个原输入与嵌套方程。
实际使用的已成$M_g$文件另在每个Gamma相关阶段保全SHA引用。
h标签明写 original_vector_only，不产生h算子或CRT目标。

所有新R815点stage另保完整原R806与free-basis数学身份，
供未来R811通过真正的外部cache adapter消费；
外部消费者保原R815标签和来源，不伪装为另一个producer自产。
预算、传输地址和后继消费者不改变数学身份。

## 4. 原$M_g$：六点模插值、七点准确认证

原weighted界是
$$
\deg(M_g)_{ba}\le3+\epsilon_a-\epsilon_b\le5.
$$
每个可用素数按原R811顺序找6个不同好点：
原成功$z_0$优先，随后非负整数。
原R806已经给出的同prime/$z_0$ Krylov矩阵直接读取；
只新增尚未求过的逆及双边乘回。
同一准确点缓存给Gamma复用。

点上用
$$
M_g(t)=
(v_g(t),M_w(t)v_g(t),\ldots,M_w(t)^{271}v_g(t))
\mathcal K(t)^{-1}.
$$
必须核完整模交换子与首列。
六点插值后逐项核更细weighted界，不能删掉实际超界非零项。
CRT只保当前大向量、小历史及尚未提交的模像；
临时矩阵只能在原子CRT提交及双同余全核之后裁掉。

严格有理重构使用固定矩形
$$
|a|,b\le\left\lfloor\sqrt{(M-1)/2}\right\rfloor.
$$
准确终验先逐系数核首列$v_g$。
交换子每项次数至多
$$
4+\epsilon_a-\epsilon_b\le6,
$$
故固定整数点$0,\ldots,6$的全部7点，
逐272×272矩阵、逐16行块准确清分母验零。
这些点无需cyclic；没有随机通过或模数足够的替代判据。
原cyclic唯一性识别完整真实$M_g$。

## 5. Gamma模像直接使用原$h$向量

不先求$M_h$。
在好点写
$$
W=M_w(t),\quad \dot W=M_w'(t),\quad
k_0=e_0,\ d_0=0,
$$
$$
k_{j+1}=Wk_j,\qquad d_{j+1}=\dot Wk_j+Wd_j.
$$
这里$d_j$是原$M_w(z)^je_0$的多项式导数在$t$处的值。
直接用R813原$v_h$形成
$$
\Gamma(t)k_j=jW^{j-1}v_h(t)-M_g(t)d_j,
$$
$j=0$列为零；再右乘同一$\mathcal K(t)^{-1}$。
不构造特征零Krylov矩阵或逆。

点上令
$$
H=\Gamma W-W\Gamma+M_g\dot W.
$$
同时模核$\Gamma e_0=0$、$He_0=v_h$和$[H,W]=0$。
这里$H$只是此点上的临时矩阵，不保完整$M_h$多项式表。

由
$$
\deg\Gamma_{ba}\le2+\epsilon_a-\epsilon_b\le4,
$$
每prime只需5个好点。它们复用原$M_g$六点grid中相同点的Krylov缓存。
插值后核每个weighted界与首列零。
$\Gamma e_0=0$是导子约束，不允许走“零首向量所以整个矩阵零”的捷径。

## 6. Gamma准确终验：七点嵌套交换子

重构候选先逐系数核
$$
\Gamma e_0=0,\qquad \Gamma e_1=v_h.
$$
由第2节实际$We_0=e_1$，这准确给$He_0=v_h$。
再令
$$
H(z)=\Gamma M_w-M_w\Gamma+M_gM_w'.
$$
乘法顺序是$M_gM_w'$，不能交换两因子。
$H$的weighted阶为3，$[H,M_w]$的weighted阶为4，故每项次数至多6。
因此用固定$0,\ldots,6$的7点、全部272×272行块准确核
$$
[H(z),M_w(z)]=0.
$$
**初稿在独立$M_h$已成条件下的6点非齐次终验，
不能沿用于本次不重构$M_h$的版本。**

若$\Gamma=A/d_A,\ M_w=B/d_B,\ M_g=C/d_C$，
取$D=\operatorname{lcm}(d_Ad_B,d_Cd_B)$，
逐点先形成整数矩阵
$$
H_{\rm num}
=\frac D{d_Ad_B}(AB-BA)+\frac D{d_Cd_B}CB',
$$
再核$H_{\rm num}B-BH_{\rm num}=0$。
保所有正分母、两个整系数因子、源SHA和每个行块证书。
不需把整个$H(z)$插值/CRT/存储。

$H$与$M_w$交换且有原首列$v_h$，
原cyclic唯一性给$H=M_h$。
于是原非齐次式
$$
[\Gamma,M_w]=M_h-M_gM_w'
$$
成立。与真实连接的差既交换于$M_w$又杀$e_0$，
再次由cyclic性唯一地识别原$\Gamma$。
这完成原导子的认证；没有引入新的周期、平移或局部参数常数。

## 7. 两图正规导子输出

$M_g$作为原r3截面的齐次第二图矩阵为
$$
M_{G/\sigma^3}(t)=t^3D(t)M_g(1/t)D(t)^{-1},
\qquad D(t)=\operatorname{diag}(t^{-\epsilon_a}).
$$
逐项反转weighted系数并保完整分母。
同截面齐次化与同函数运输分别标明。

R814第二图用$\delta_\sigma=t\delta_\tau$，所以
$$
M_{\delta_\sigma t}=-t^3D(t)M_g(1/t)D(t)^{-1},
$$
$$
\Gamma_\sigma=
tD(t)\Gamma(1/t)D(t)^{-1}
-t^2D(t)M_g(1/t)D(t)^{-1}\operatorname{diag}(\epsilon).
$$
保底变量导数的负号。
Gamma不是简单反转；两个部分可能各有$t^{-1}$项，
必须准确相消后才记录第二图多项式和weighted阶2。
底变量导数可用已有g第二图blocks加标量$-1$表示，
不复制一份仅差符号的大矩阵。

后续R814直接消费$(M_g,\Gamma)$与上述第二图二元组。
本任务不以原h的r3齐次化冒称$\delta_\sigma(w_0/\sigma)$；
若将来需要$M_h$，可另从已认证表达式按需导出。

## 8. 数据形状、实际成本与续算

| 实际重构对象 | weighted阶 | 有理系数位置数上界 |
|---|---:|---:|
| $M_g$ | 3 | 295936 |
| $\Gamma$ | 2 | 221952 |
| 合计 | — | 517888 |

这是位置数而非实际非零数。
相较初稿删除独立$M_h$的295936个位置。
每个矩阵按16个输出行一块，共17块；
每块保共同正分母和“输出行、输入列、幂次升序”整数组。
Gamma必须按阶2读取。

每个已成目标保全部tau/sigma块SHA、实际CRT素数与模数bit、
原列约束、准确7点与17行块见证、cyclic来源。
Gamma另保真实$M_g$和原$v_h$来源、嵌套式、两图负一次项相消。
Krylov点缓存保留给实际两个算子和后继共享消费者；
每目标只保当前大CRT及小历史。

原$M_w$系数很大，模点逆、CRT、准确点的大整数乘法和产物大小
仍是实际成本，不能保证单次300分钟完成。
完成目标、点、行块不重算；硬中断从完整原子阶段续接。
任何改变裁剪规则的工程适配保同数学身份和小历史，
不能删掉仍需的旧矩阵后再重算。

不构造ambient场迹全表、全$k(z)$ Krylov逆或272个普通基乘法表。
此范围直接服务原$\delta$与R814理想降重数。

## 9. 最终完成字段

只有g/Gamma两目标都准确完成，FINAL才置complete=true。
输出至少包括：

- original_Mg_computed=true；
- original_normal_derivation_connection_computed=true；
- independent_Mh_reconstructed_or_stored=false；
- original_Mh_identified_by_nested_commutator_and_original_first_column=true；
- all_weighted_supports_and_original_column_constraints_verified=true；
- all_complete_polynomial_defining_identities_verified=true；
- g与Gamma各自固定7个准确点；
- 同原正规基两图矩阵/连接索引；
- original_cusp_zero_ideal_computed=false；
- original_function_DAG_polar_divisors_eta_or_height_computed=false。

一日source-bound bundle只含直接消费的原阶段。
Git/Release不保存可重算矩阵或证书；
仓库只登记脚本、参数、run、SHA与实际结论。

来源（2026）：本仓库R805/R806、R811、R813、R814、R817。
原R815初稿在首次运行前由本契约收紧；
没有任何已成数学因本次缩小而重算。
