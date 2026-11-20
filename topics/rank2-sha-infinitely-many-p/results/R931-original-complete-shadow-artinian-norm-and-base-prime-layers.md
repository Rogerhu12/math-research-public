# R931 — 原完整 shadow 的厚代数范数与全部基素层

日期：2026-11-20。**状态：下述完整extra理想、厚代数椭圆点、原Tate范数与全部π层算法均已证明；root与独立审阅者全文核过。没有数学执行、性能回执或shadow数值。**

本文只处理 R883 的同一个有限 shadow，不改变原四条交除子、原 Artin 标签、两轴或完整18×9读者。目标是在已经取得 R925 的原完整正规化和四有效交理想之后，不逐个构造所有闭点剩余域，而仍准确计算 R883(19) 的整个和。固定辅助素数上的结果不替代 ordinary 或无穷个目标素数。

## 1. 原输入及不变的完整长度

固定原常数域 k=F_(r²)，(r,ell)=(29,5) 或(41,7)，q=r²；一切域嵌入、原ω和挠点基均保持。只在相应素数的原完整环、原映射及全部接受门已实际取得时执行。

沿 R925 记 ξ=y_s，A 为原 Y 去掉 ξ=∞ 全纤维后的完整整环。它是 k[ξ] 上的306秩自由模；无穷图表仍用于认证原完整有效交除子。对原四个 pair 中任一个，保 R883 的真实函数

$$
v=\xi^2-1,\qquad a=a_0,\quad c=c_0,\quad
y_1,\ y_2,\ g=y_1-y_2,
\quad f=f_{\rm out},\quad y=y_{\rm out}.
$$

在原函数域中有

$$
v a^3=y_1^2-1,\qquad
v^2c^3=y_2^2-1,\qquad
vf^3=y^2-1,
\qquad x=af/c.
\tag{1}
$$

这涵盖原两种循环呈示；c 中原 r 次幂不是常数 Frobenius 或 Artin 置换。原完整有效除子仍为

$$
E=\operatorname{div}(g)+\operatorname{Pole}(y_1)
+\operatorname{Pole}(y_2).
\tag{2}
$$

保全部两图表、真实极理想和完整度数2256+r d_F或2256(r+1)，按原实际d_F选择。下文的任何分离均记录被分离的完整长度，并以原(2)作为总长度检查。

## 2. 不拆闭点的准确除子操作

对有限有效除子D，I(D)是A中的完整消失理想。因为原Y光滑，每个局部环是DVR，所以

$$
I(D_1+D_2)=I(D_1)I(D_2),\qquad
I(\min(D_1,D_2))=I(D_1)+I(D_2).
\tag{3}
$$

若C≤D，完整理想商I(D):I(C)恰为I(D−C)。每次减法都须核回

$$
I(D-C)I(C)=I(D),
\tag{4}
$$

包括两边的全部HNF，不能只核范数相等。

还可按一个完整理想J的零支集，把D分成D_bad和D_good而不拆其闭点。置I=I(D)，在A/I中计算J的像。在长度n=deg D的有限Artin环内，J^n在每个局部分量上或为零、或为整个局部分量；故J^n是幂等理想。准确地，

$$
K=I+J^n=I(D_{\rm bad}),\qquad
I(D_{\rm good})=I:K,
\tag{5}
$$

这里bad指J在该点剩余值全零。可不断平方并在每步加回I，直至完整理想满足K²+I=K；这正是有限环中的幂等理想，故已到(5)。最迟指数达到n时终止。实际返回必须核

$$
I(D_{\rm bad})+I(D_{\rm good})=A,
\quad I(D_{\rm bad})I(D_{\rm good})=I,
\quad\deg D_{\rm bad}+\deg D_{\rm good}=\deg D.
\tag{6}
$$

这保每个原点的整个厚度；不是只取约化支集。指数n只用于终止证明，不要求先构造未经模I缩减的巨大J^n。

## 3. 原分歧和共同交重的完整理想公式

R883附B的准确分歧表给：原X/Y的全部分歧点恰在ξ=1,−1,∞。各点v的阶为1、289、−2或−578，均不被3整除。其它点的v为单位。因此原E在这些三条完整纤维上的所有厚分量统一记为E_ram。有限两条用(5)取J=(ξ²−1)，无穷整边界由原第二图表取得。原CM等变性给它们的整个[6]输出严格为零，正是R883(11)；它们的全长度仍保留。

令E_nr=E−E_ram。它的全支集已在A的v单位开集。记函数的完整正零除子为Z(·)，极除子为P(·)，定义

$$
C_{\rm pole}=\min(E_{\rm nr},P(y_1),P(y_2)),
$$
$$
C_{\rm zero}=\min\bigl(E_{\rm nr},
 3\min(Z(a),Z(c))\bigr),
\qquad
D=E_{\rm nr}-C_{\rm pole}-C_{\rm zero}.
\tag{7}
$$

**命题1。** D有效，且对每个原非分歧闭点Q，

$$
D(Q)=E(Q)-3m_Q=k_Q,
\tag{8}
$$

其中m_Q、k_Q严格是R883(13)–(15)的原数值。两种C支撑不交。

证明：在v单位开集，y_1有极当且仅当a有极，且极阶比为3:2；y_2与c同样。若两y均有极，R883的共同3m恰为两极阶之最小，且原完整E已含该重数，故(7)第一式准确。在两映射均有限且a、c均有零的点，若y_1、y_2的剩余符号相同，原E重数至少3min(ord a,ord c)，第二式准确给共同3m；若符号相反，g为单位且E(Q)=0，min自动给零。其余点两式均给零。由原(15)的逐点有效性得(8)。不以一个仿射分母的零阶代替这些真实零极除子。证毕。

这也给完整长度恒等式

$$
\deg E=\deg E_{\rm ram}+\deg C_{\rm pole}
+\deg C_{\rm zero}+\deg D.
\tag{9}
$$

共同部分的三个原提升经输出相加为零，按R883(16)消去，而不把共同部分误作唯一提升。

## 4. 原输出在整个厚extra代数上是椭圆点

以(5)按J=I(P(y))再分D，取得输出为O的完整部分D_O及余D_f。D_O按原射影延拓全部输出O；不能对该部分的仿射坐标作代入。令

$$
\mathcal B=A/I(D_f).
\tag{10}
$$

若D_f为空，相关后续范数按1处理。否则R883(18)逐点保证x=af/c与y在D_f支撑上正则。

**命题2。** 这两个原函数给整个有限非约化代数中的点

$$
P=(x,y)\in E_0(\mathcal B),\qquad
y^2=x^3+1\quad\text{在}\ \mathcal B\ \text{中}.
\tag{11}
$$

证明不只验约化点。由(1)，在原函数域准确有

$$
x^3-(y^2-1)
=(y^2-1)\frac{(y_1+y_2)g}{y_2^2-1}.
\tag{12}
$$

固定D_f的点，写e=E(Q)、k=k_Q>0；y²−1整。若两输入映射有限且m=0，y_2²−1为单位，否则同一E支撑会迫a、c同时有零。此时ord g=e=k，右边阶至少k。若有限且m>0，额外交重为正迫ord a=ord c=m；y_1+y_2是单位，ord(y_2²−1)=3m，故右边阶至少e−3m=k。若两输入有极，正extra迫两y极阶同为3m；ord g=e−6m、ord(y_1+y_2)≥−3m、ord(y_2²−1)=−6m，右边仍至少e−3m=k。只有一个输入极的点不在原E支持。以上穷尽原情形，故(12)属于D_f的整个消失理想，得到(11)。证毕。

### 4.1 同原分式的全局消零回收

对原f=N/D，不在0/0处擅自约化。取原完整图核

$$
\mathcal K_f=\{(n,d)\in A\oplus A:Dn=Nd\}.
\tag{13}
$$

其分母投影准确是I(P(f))，没有选中分母的额外零点。若f在D_f支撑正则，则I(P(f))+I(D_f)=A。利用两完整k[ξ]模的HNF变换，取得

$$
\sum_j b_jd_j+e=1,\qquad e\in I(D_f),\quad b_j\in k[\xi],
\tag{14}
$$

其中(n_j,d_j)是同一图核的完整基。于是f在\(\mathcal B\)中的原值准确为\(\sum_j b_jn_j\)；因为同一全局身份\(f\sum b_jd_j=\sum b_jn_j\)和分母模I等于1。这连所有共同零和整个厚度都保住，无需任选当地参数或仅取一个模I的Dn=N解。

同理，有限代数中单位的逆必须用完整单位证或完整线性解核回乘积1。下文所有分式求值均以此意义进行。

## 5. 两个原辅助点的全厚分离

保R883附G原挠点基T_1,T_2、另一轴U_i及同一Miller函数f_(T_i)。对每个i，R883(G9)只需R=U_i或2U_i。

在(10)上，集合\(\langle T_i\rangle-U_i\)由ell个互异的原k有理仿射点组成；因为U_i不在\(\langle T_i\rangle\)，其中无O。按(11)将其完整理想拉回\(\mathcal B\)，再用(5)分离：在good分量取R=U_i；在bad分量取R=2U_i。对bad的每个剩余点，若P+2U_i也在该循环子群，则两个值之差U_i在子群中，矛盾。故两分量上所选P+R都避开整个\(\langle T_i\rangle\)。

所有Miller中间线/竖线的零极均在这个子群，因而同一真实比值

$$
h_{i,R}=f_{T_i}(P+R)/f_{T_i}(R)
\tag{15}
$$

在相应完整厚代数中为单位。没有只检查最终f的两个支点。

计算(15)不能因为P+R有限，就在P=R时使用有0/0的单一仿射弦公式。这里有一个完整的两chart实现。令R=(x_R,y_R)；R是奇数ell阶非零点，所以y_R非零。已选辅助分量上P不等于−R，于是x−x_R与y+y_R没有共同剩余零。再按(5)用J=(x−x_R)分离；在其单位分量使用

$$
\lambda=(y-y_R)/(x-x_R),
$$

在其零支集的整个厚分量使用

$$
\lambda=(x^2+xx_R+x_R^2)/(y+y_R).
$$

第二个分母在该完整分量上是单位。两式由原曲线恒等
\((y-y_R)(y+y_R)=(x-x_R)(x^2+xx_R+x_R^2)\)相容，并准确覆盖P=R。随后

$$
x(P+R)=\lambda^2-x-x_R,\qquad
 y(P+R)=-y+\lambda\bigl(x-x(P+R)\bigr).
$$

这是同一个真实群律，不另改P。所得点仍避开完整循环子群，所以原Miller链所有中间分母和分子都是完整厚代数中的单位。两个加法chart的范数再相乘，仍为原辅助分量的范数。固定ell的小函数也可先在原E0坐标环中取同一平移后函数的完整图核，再按(14)求值；两种实现都不得跳过各自的完整单位及回代门。

## 6. 厚代数范数准确等于完整原trace乘积

对有限k代数C及单位h，定义

$$
\operatorname{N}_{C/k}(h)=\det_k(m_h:C\to C).
\tag{16}
$$

若C是原厚除子\(\sum_Q n_QQ\)的坐标代数，则按各局部极大理想的全旗标，乘h在每层的作用都是乘同一剩余值，故

$$
\operatorname{N}_{C/k}(h)
=\prod_Q\operatorname{N}_{\kappa(Q)/k}(h(Q))^{n_Q}.
\tag{17}
$$

因此不可先将C约化；那会丢掉n_Q。也不能把任何范数目标换为F_r。

对i的两个辅助分量分别取(16)并相乘，记结果N_i∈k×，再令

$$
u_i=N_i^{(q-1)/\ell}\in\mu_\ell.
\tag{18}
$$

由原R883(G3)、(G7)与(17)，准确有

$$
u_i=\prod_{Q\in|D_f|}
 t_{d_Q}(T_i,P_Q)^{k_Q},\qquad
d_Q=[\kappa(Q):k].
\tag{19}
$$

辅助点虽在分量间不同，原配对的无交代表独立性仍逐点适用。常数分母f_T(R)须在各厚范数中按该分量的完整k维数保留；不得丢掉它或只按约化点数计幂。

取原已校准根ξ_ell和原配对矩阵M，原shadow的坐标准确为

$$
\binom{z_1}{z_2}=M^{-1}
\binom{6\log_{\xi_\ell}u_1}{6\log_{\xi_\ell}u_2}
\pmod\ell.
\tag{20}
$$

所有原d_Q都通过准确范数保留，包括ell整除d_Q的情形；只有完整(18)之后才在ell个实际根内取离散对数。乘6仍在原位置。由(9)及D=D_O+D_f，分歧、共同、O及实际extra的全长度共同核回原degE。

## 7. 仅分解基多项式的完整范数算法

(16)不要求真的建立degD_f阶的稠密k矩阵。下面给一个只使用原306秩k[ξ]模及基素多项式的精确替换；没有声称其实际耗时已取得。

令I为某辅助分量的完整理想，H为其306行HNF基，N_I=monic(det H)。它的次数就是完整有限长度。对N_I作完整k[ξ]不可约分解；不拆Y上的闭点，也不另建其剩余域。对每个实际因子π，令k_π=k[ξ]/(π)，并取全部理想

$$
H_j=I+\pi^j A\quad(j\ge0),\qquad H_0=A.
\tag{21}
$$

直到H_j=H_(j+1)的完整HNF相等时停止。每个商

$$
V_j=H_j/H_{j+1}
\tag{22}
$$

被π消去，是k_π向量空间，维数至多306。因为H_j都是A理想，乘h保持每个H_j，故在V_j上有准确诱导矩阵B_(π,j)。h为A/I的单位使每个非空商上的该矩阵可逆。 h取在A中的任一整代表；改变代表的差属于I，而I·H_j包含于I并包含于H_(j+1)，所以所有层算子与这个选择无关。

具体构造：取H_j、H_(j+1)的完整R基，核回包含矩阵C_j满足H_(j+1)=C_j H_j；乘h在H_j上的完整矩阵由原乘法回代取得并核所有坐标。还应核π乘单位矩阵的各行属于C_j的完整R行模，等价于原πH_j包含于H_(j+1)。模π后在完整\(k_\pi^{306}/\operatorname{rowspan}\bar C_j\)取确定商基，核诱导关系及所有列。这不是抽取原306矩阵的任意主子式。

H_j相等时，π主分量已耗尽：在有限π主模中由Nakayama，π^jM=π^(j+1)M迫该层为零；其它基素分量从H_0/H_1起就不出现。因此

$$
\boxed{\quad
\operatorname{N}_{A/I\,/k}(h)
=\prod_{\pi\mid N_I}\prod_j
 \operatorname{N}_{k_\pi/k}\bigl(\det B_{\pi,j}\bigr).
\quad}
\tag{23}
$$

所有π层和全部厚度由

$$
\sum_{\pi,j}(\deg\pi)\dim_{k_\pi}V_j=\deg N_I
\tag{24}
$$

独立核全。完整因子相乘必须回到monic(det H)。每个k_π范数可用同一单项π与实际剩余代表的resultant，结果在原k；这明确避开某有限域库默认取到F_r的绝对范数。

层空间虽至多306维，其基素次数仍可能很大；不能据此给出固定RAM或短耗时承诺。这个替换的数学优点是无需再识别π纤维内部的所有κ(Q)、幂等元和当地参数，而仍经(17)完整保留那些点的次数、厚度及原值。

## 8. 接入时必须保持的原门

先取得原两图表/全乘法、全部映射与原实际d_F、四个完整E及其真实全度数；再执行(7)、所有厚分离、原分式图核回收与完整(11)。每个辅助分量核原Miller单位、所有π层及(24)，最后使用同一原挠点基/校准矩阵/ω/Artin行及18×9两轴读者。不能将本理论写成已取得shadow数值或新的PASS。

证明依赖R883正文及附B/G的原完整交重、真实三次分歧、唯一额外提升和原Tate规范；R925的原完整正规化/理想；所有新的消零、厚范数及π层身份已在上文给出。没有新增自由函数、删去原边界或将闭点次数模ell。

来源：[R883](R883-original-relative-six-shadow-and-complete-boundary.md)、[R925](R925-original-ys-affine-rings-and-complete-divisor-ideals.md)、[R927§9](R927-original-yF-pole-degree-from-mixed-kernel-and-cusps.md)。最后一项已实际确定r29的d_F=1296及F_first，每E的应核全长度39840；本篇不替代其尚未完成的完整E接受门。

## 9. 基础完整运算 helper 已接源

[原源](../scripts/original_ys_artinian_norm_tools.py)共37221字节，SHA256 `9b2a00b0a92b697ae509f649c840060afffad2677cbae768dbda8573c56e355f`；[全部接口及实现证明](../notes/2026-11-20-original-artinian-norm-tools-contract.md) SHA256 `29b4ea5c418003634e455225db950a621c7d6ab38a452ee55ce5e2713b118b5b`。global实现，root/deep分别全文审查，逐项对回原 ideal/local/closed/fast API；本地仅AST和源码检查，尚无公开数学回执。

入口绑定同一个原 engine、306权基/完整乘法回执、实际k=F_(r²)与调用者原ω；所有理想必须来自这个engine。已实现完整理想和、有效商、Fitting厚分离及CRT、原分式全paired图核与任意共零回收、全厚单位逆、全π层范数。I=A的空商明确返回长度零/范数1。

有效商只在I包含于C的全HNF门后构造；每个完整核的候选都包含真正I:C，达到准确monic Norm(I)/Norm(C)才早停，最终仍全核(I:C)C=I。Fitting每次平方后加回I，完整HNF稳定及互补乘积/长度付清所有厚分量。分式始终以同paired图核的真单位分母组合回收，不能用一个可能有共零的D乘法方程替代。

Norm实际构造所有H_j=I+π^jA，核全部306行的包含坐标、商关系与诱导算子，直到完整HNF稳定；每层用原k的resultant并沿原嵌入交核，最后核Σdegπ·dimV_j=degdetI。全π因子实际乘回，不把原k范数降到Fp，也不把厚度或剩余次数模ell。源码不自动无限缓存图核/乘法算子；详细成本保在契约，不冒速度保证。

本次只接基础源，不触发新数学作业。四E构造、ram/common3m/outputO分离、原厚椭圆点和Miller链、原双轴/乘6及18×9仍由后续上层消费器逐门接入并实际执行。原完整Tate作业保其source继续；本节不能据此填任何shadow值或关闭ordinary/无穷p门。

## 10. 完整上层、两图真实验收与独立公开入口

完整上层现在接源：[源码](../scripts/original_ys_artinian_shadow_consumer.py)及[全部契约/证明](../notes/2026-11-20-original-artinian-shadow-consumer-contract.md)。global实现，root/theta全文独审，deep另核来源API和全部厚分区。源码的993行均已静态核对原bridge/reuse/ideal/local/closed/Tate API；这里只登记实现和公开请求，不登记数学PASS。

| 文件 | SHA256 |
|---|---|
| original_ys_artinian_shadow_consumer.py | `a543c957c539fecef082cf26860cb321a3731d0c19e29e34205d8346f279c2e4` |
| launch-original-artinian-shadow.py | `1d3848ada1077029d8ffd7b1882711730f0e109ac2d831e7dedc2cdd70263038` |
| produce-original-artinian-shadow.py | `f83cba8aae5cb15380483f007f1bfec18a646161443c48edd686e0cb7871ba90` |
| original-artinian-shadow-request.json | `1510d21b2ffc5fa2a8f9d890f2c7c884465b8aaccc35bc2168062b6a4d7caa87` |
| rank2-sha-original-artinian-shadow.yml | `c82f7483c18531cf6d424dae6663e63a640334fbd20c421ac49c49572c2ebabb` |

契约SHA256为 `8ec59c4e30a97fe7a69edcddbc8ff4689cb5aeed17f99c4b4ea3d5c47ab3ab42`。基础helper仍为§9的 `9b2a00b0a92b697ae509f649c840060afffad2677cbae768dbda8573c56e355f`，未重新改动。host/producer两份完整清单同序同集合、32个互异源；上层14份直接依赖全在其中。全部Python只作AST，JSON/YAML解析通过；没有本地数学。

### 10.1 同原两图的真实厚范数预门

为核实新接口在原环上完整执行，新的producer在同进程原cube、紧缩截面、306全乘法及全部maps之后，对两张实际原图各作下述门。设R=k[ξ]、A仍为同一个R自由秩306的正规化，c是调用者实际k=F_(r²)的乘法生成元，令

$$
\pi=\xi^2-c,\quad\rho=\xi-1,\quad I=\pi^2\rho A.
$$

c不是平方，所以π真不可约，且与ρ互素。原完整长度准确为1530，π厚部为1224，ρ部为306。代码以全HNF/Fitting和完整商回乘实际检查这份分离与两个CRT幂等元，再核ξ的全厚单位逆。原分式(πξ)/π在π整支上同时为零；必须以整个paired图核恢复真实ξ，不能只求模I的πx=πξ。

A是原R自由模，故标量ξ在A/I的范数等于其在R/(π²ρ)的范数的306次方。后者为(-c)²·1=c²，所以

$$
\operatorname{Norm}_{A/I\,/k}(\xi)=(-c)^{612}.
$$

对r29/41，r+1=30/42均不整除612；由于c的阶恰r²−1，该结果**不在F_r**。新门实际核范数、完整1530长度和这一非素域属性，直接检查原k嵌入/相对结果式是否保持。所有π层都实际执行；空商范数另核为1。该预门使用完整原Y而非另造测试曲线，仍不能代替四大E的后续门。

### 10.2 同一四E的完整上层

上层沿实际v=ξ²−1的完整零理想与既有全分歧来源，分别保留有限/无穷所有被消项的长度；余部实际核v为单位。此后Zero(c0)=r Zero(xp)严格来自同一真实幂，Pole(y2)=r Pole(yp)也保持原对象。幂采用每步全截回I的准确I+J^e，恒等式I+(I+J^a)(I+J^b)=I+J^(a+b)支付全部重数；共同pole/zero的3m、输出O及其余厚代数恰还原六类全长度。

原xout/yout经完整图核恢复，并在全厚商上实际核y²=x³+1。禁止集用全部原有理点的两坐标完整理想，常数输出/零生成元仍由I保证全秩，不调用零主理想。U/2U两辅助和两条加法图都核全厚支集/单位；每条Miller分子和分母均须单位，原f_T(R)在Norm前除去，因此自动带完整长度幂。每层Norm回原k后才取最终指数，原6M^(-1)、四个独立输出、W/反射、九点和全18×9/双轴逐字保持。

独立入口只请求r29、phase=shadow、trace_method=artinian，原F/P两个公共PASS、q_precision2453、batch64、minimal核、固定Sage10.6镜像保同源。source只读且数学容器断网，令牌仅host公共回执读者使用。现有完整Tate及closed/local作业不变、不取消。新工作流按同一进程依次支付预门、完整几何/原极次数、四E及全厚迹；最终明确all_intersection_closed_points_computed=false，以全部原长账及Norm定理认证完整迹。实际run/job/source在建立后登记，不预填结果。

实际公开运行已建立：run `44747799006` / job `136327515753`，source `632cef5af919da67776803cd36346a5cc3941363`，创建于2026-11-20 13:50:06 UTC；状态 in_progress。此前推送遇远端推进，已立即pull --rebase、核两README差异为空后重推成功；实际运行以此最终source为准，不用被重写的本地提交号。尚无任何新数学PASS。

## 11. 同原单位的完整循环商与可选范数算法

[完整证明](../notes/2026-11-20-original-cyclic-unit-thick-norm.md)及独立 helper `original_ys_cyclic_unit_norm.py` 已完整写出并作源码检查。当前32源运行/基础工具/上层消费器均未改，没有新数学或性能PASS。

只在同一原完整理想I满足R·1+I=A时，才有由实际单位诱导的原R代数同构A/I≅R/(d)，d是完整HNF首一行列式，保所有重复因子。整个307×306矩阵的H=UM和全部原行反向成员关系认证完整HNF；恰为单位阵才接受。全变换给每个原基的gamma像，所有306基/理想行、实际单位、omega、d·1和真全长逐项返回；实际值h还须h−c·1∈I。

因此其完整厚范数恰为Res(d,c)，目标仍原k；完整gcd认证单位，常数范数按全长幂返回，空商为1。非循环明确miss，只有norm_unit_with_fallback继续原所有π层并保其完整错误/回执，try的miss本身不认证所给值为单位。算法不假设理想约化、闭点横坐标分离或一般循环性，完整HNF本身的成本也未实测。

源SHA256 `b3b2bfc21328e164de64845bc906efbaa01d143f6de7d80829c1bbbd4d775eb8`，证明SHA256 `602ce98ca9d1106d505dda15c6525573ffb4122ce58fa43a9cd7b6a7fb038e0e`；root/global全文核，只有AST/文本身份门。后续只有真实应用和公开接受门通过后，才能声明此路线实际命中或给出原shadow。

### 11.1 全商不循环时，读取这次真实标量值

[完整短补证](../notes/2026-11-20-original-scalar-value-thick-norm.md)给严格较弱的实际值门。沿同一次已认证HNF，K的行模是R·1+I；即使K不是单位阵，也可完整除这次真实h。余式为零时，以原307行变换直接返回h=c0·1+bH_I，降c=c0 mod d后仍核d·1∈I及h−c·1∈I。于是h在整个原A/I上等于标量c作用。

原完整R-module的Smith因子乘积为d=det H_I，故完整厚范数仍是Res(d,c)，无须全商循环或实际计算Smith分解。gcd(c,d)=1准确支付单位门，原k、omega、所有重复因子和全长度保持。只有真实值仍不在R·1+I时才回原所有π层；这种miss不认证单位，原fallback的错误保留。

独立helper已更新至SHA256 `d5d1761bbf63f6a558b71d9d7fd2cd165bd1576c3c3400737be62011e10138ed`，原版b3b2bfc2仍由§11及git历史标识。root/global全文核增量、仅AST；未接当前32源consumer或触发重跑，没有新数学/性能PASS。

## 12. 真实运行故障及原native域的绝对次数兼容门

§10的 run44747799006/job136327515753 已在14:57 UTC失败：
同source632cef5af完成了完整maps，随后固定Sage10.6的原Givaro域
在基础初始化 `absolute_degree()` 处报 AttributeError。
原1530长度/非Fp厚范数预门未开始，不能登记其PASS；
完整原始日志和实际maps回执hash见
[故障、完整修复证明和全部源码hash](../notes/2026-11-20-original-native-field-degree-compatibility.md)。

现对同一个实际native域用 degree=n 与cardinality=p^n共同认证绝对次数，
保原k二次性、所有相对剩余次数、实际两向域映射/omega及Frobenius指数。
基础工具当前源为 `f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714`；
闭点读者及最终Tate层相同接口也完整修正。没有放宽成相对degree检查，
没有改变任何原域或删掉完整k长度门。

六P首run44759336052/source da34ea30a也依赖旧门；取消接口返回403，
旧实例并未成功取消。修正来源以独立固定组继续，所有旧source及回执保留。
新Artinian、Tate、closed/local、六P公开入口将实际重走各自完整门；
静态检查和新启动均不代原范数、四E、trace或shadow PASS。
