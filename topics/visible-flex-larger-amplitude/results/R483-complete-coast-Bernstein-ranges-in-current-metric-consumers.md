# R483：当前完整 metric 消费者中的准确 coast 三 jet 与 Bernstein 包围

作者：OpenAI / ChatGPT exact_refinement agent  
日期：2026-11-16  
状态：源码与条件包含证明；未导入、AST、编译、运行或进行本地科学计算。本稿没有实际新 field、域证书、metric 成功或性能数据。

## 483.1 本次结论与实际作用点

本稿落实 [R481](R481-fixed-ten-semantic-domain-and-complete-coast-polynomial-enclosures.md) 的一个有限范围：保持原 72c 完整十族定义、实际 C/root 语义叶、当前 field、数值 compiler、全部控制系数及物质图不变，只在已经绑定的准确目标范围求值中，对 negative-speed-coast 使用同一多项式的完整 Bernstein 包围。其余准确片继续调用原 72c 的 piece_range。

新增库为 [geometry_20261116_complete_coast_bernstein_enclosures.py](../computations/geometry_20261116_complete_coast_bernstein_enclosures.py)。它既不生产 factory.result，也不更改任何已加载原模块或 current.target。四个明确的新 metric 源视图把独立 CoastTargetRange 对象作为局部参数传给原 Prefix.inspect；第五个新 R459 evidence 视图在真实闭域目标及时间见证的 target 调用处使用同一个适配器。源视图由小型生成器和逐项字面计划在 Actions 的实际 computations 目录生成，原基线文件不动。

此次原本已经存在的三个 field 来源分别是 original112、resolution112、completeM。完整 M 视图仍调用自己的 M Prefix/field 加载器，未用 112 标签冒充 M。R464 的 incremental-M union 来源尚未注册；五视图不构成这一后继来源的证据。后续若接 union，必须在其实际生成源上另列完整来源、schema 和差异。

本稿没有替换 72c 的 prove_domain 或 main，也没有消除其真实初始域未付状态。新的 range 求值并非新 BVP 接受条件、独立审计或原求解前门。

## 483.2 原对象与可选公式的完整条件

设原完整 72c 准确定义已经由实际 R400/R416 或其既有 resolution/M 加载器绑定。十个冻结参数是实际保存的准确有理数；C 的三个语义 cut 叶和完整允许 root 族沿原绑定，不把叶盒中心当一个真实成员。原准确 piece、支撑、DAG 以及当前 field 的数值长度均不修改。

库只有在下列源结构实际满足时选择新 coast 分支：

1. 原模型的 control_terms 与原完整十项表逐项相同，参数恰为十个，真实支撑恰为三个。
2. 当前片确是 negative-speed-coast，其局部闭区间为 $[0,1]$，基底系数恰为常数和线性项两项。
3. coast 的 anchor/width 与第三支撑的 left/width 使用相同 DAG 下标，width 也是原 coast_length 根。宽度区间严格为正。
4. 线性系数的原 DAG 节点确是共享宽度与一个准确常数 $-\kappa$ 的乘积，且 $0<\kappa<1$。代码从原 rational 或其显式 neg 节点读该常数；没有用区间线性系数除以区间宽度来反求它。
5. 前两个支撑的实际正宽度和完整右端点包围都在 coast 左端点之前或相等。所有相交闭端点仍保留。
6. coast 的三个控制项恰为索引 $2,5,8$，幂次 $0,1,2$；另外七项全部仍在完整表内，并由第 5 项证明在 coast 内为零。第十项 $\xi$ 在第二支撑，不被删除或改为零参数。

不满足这个结构选择时，实际调用原 Factory.piece_range，而不是新增拒绝、忽略某项或宣称其为零。原模型/来源本身绑定错误仍按原来源责任报错；不能用这种局部回退绕过原加载器。

原 bump 是

$$
b_k(t)=64t^3(1-t)^3(2t-1)^k.
\tag{483.1}
$$

它与其一、二阶导数在 $0,1$ 都为零。因此第 5 项即使只给闭支撑端点接触，也足以使另外七项在 coast 的完整二 jet 为零。该结论依赖准确支撑和零延拓，不依赖名义 midpoint 片查找。

记某一允许 C 成员的 coast 长度为 $\ell>0$、起点为 $S_1$，并记

$$
A=R_A+I_A,\qquad
P(t)=p_3b_0(t)+\theta_3b_1(t)+\eta_3b_2(t),\qquad
t=\frac{s-S_1}{\ell}.
$$

则对该同一成员，在整个 coast 上有准确恒等式

$$
a=A-\kappa\ell t+\ell^2P(t),\qquad
a_s=-\kappa+\ell P'(t),\qquad
a_{ss}=P''(t).
\tag{483.2}
$$

这里 $a_s,a_{ss}$ 是物理准确径向坐标 $s$ 的导数；并非公共 $u$ 或数值坐标的导数。三式来自同一表达式，$dt/ds=1/\ell$。消去相同的宽度因子只改区间表达方式，不改变准确函数。$\deg P\le8$，故 $\deg P'\le7$、$\deg P''\le6$。本次不新增比 R481 更强的十维参数量词。

## 483.3 单变量的全部 Bernstein 系数

对次数不超过 $n$ 的准确多项式 $p(t)=\sum_{j=0}^{n}c_jt^j$ 和任意闭区间 $T=[t_0,t_1]$，令 $h=t_1-t_0\ge0$，先形成

$$
p(t_0+hx)=\sum_{k=0}^{n}d_kx^k,\qquad
d_k=\sum_{j=k}^{n}c_j\binom jk t_0^{j-k}h^k.
$$

再形成全部 $n+1$ 个系数

$$
\beta_i=\sum_{k=0}^{i}d_k\frac{\binom ik}{\binom nk},
\qquad
p(t_0+hx)=\sum_{i=0}^{n}\beta_i B_i^n(x).
\tag{483.3}
$$

其中 $B_i^n(x)=\binom ni x^i(1-x)^{n-i}$ 非负，且在 $[0,1]$ 上总和为一。于是

$$
p(T)\subseteq[\min_i\beta_i,\max_i\beta_i].
\tag{483.4}
$$

实现对未达最高次数的多项式保留所有高阶零槽，不只取非零槽或端点值。$h=0$ 时同一公式仍成立，不除以 $h$。

helper 的 affine_coefficients 与 bernstein_coefficients 按 (483.3) 完整形成；系数和变换使用原 Fraction 有理数。原 Factory.Box 端点也是准确有理数，树中平方根已经由原求值器以受证包围形成。本层没有偷偷把这些盒当准确点。

## 483.4 半径的完整 27 系数

令 $\ell\in I=[\ell_0,\ell_1]$，$t\in T=[t_0,t_1]\subseteq[0,1]$，令 $A$ 属于原 DAG 给出的完整区间 $I_A$。实际同一 C 成员的 $(A,\ell,t)$ 可能相关；用包含它们的完整笛卡尔盒只扩大需要包住的集合。

写

$$
\ell=\ell_0+h_\ell x,\qquad
t=t_0+h_ty,\qquad (x,y)\in[0,1]^2.
$$

(483.2) 的半径是双次数不超过 $(2,8)$ 的多项式

$$
a=\sum_{r=0}^{2}\sum_{s=0}^{8}d_{rs}x^ry^s.
$$

所有 $d_{rs}$ 按原完整 $A-\kappa\ell t+\ell^2P(t)$ 形成。其二维 Bernstein 系数是

$$
\beta_{ij}=
\sum_{r=0}^{i}\sum_{s=0}^{j}
d_{rs}
\frac{\binom ir}{\binom 2r}
\frac{\binom js}{\binom 8s},
\qquad 0\le i\le2,\ 0\le j\le8.
\tag{483.5}
$$

当 $A$ 用区间表示时，各 $\beta_{ij}$ 按原 Box 运算给出包含所有准确系数的盒。二维 Bernstein 基函数非负且和为一，故

$$
a(I_A,I,T)\subseteq
\left[\min_{i,j}\inf\beta_{ij},\
      \max_{i,j}\sup\beta_{ij}\right].
\tag{483.6}
$$

代码形成并使用全部 $3\times9=27$ 项。没有用四个矩形角点冒充二次 $\ell$ 依赖，也没有只检查名义长度。若 $h_\ell=0$ 或 $h_t=0$，同一多项式变换保留退化方向的全部槽，证明不变。

这是对包含所有实际相关成员的盒的充分包围。不能从盒上某个不真实组合的宽度、符号或失败推出真实 C 成员反例；也不能把本式改称盒内所有组合都能由原 C 实现。

## 483.5 速度与二阶导数

对每个固定 $t$，速度 $-\kappa+\ell P'(t)$ 对 $\ell$ 仿射。因此它在 $I\times T$ 的所有值包含于两个端点多项式的值域 hull：

$$
a_s(I,T)\subseteq
\operatorname{hull}\left(
  -\kappa+\ell_0P'(T),\
  -\kappa+\ell_1P'(T)\right).
\tag{483.7}
$$

实现对两个端点分别用次数 7 的全部八个 Bernstein 系数，最后取这 16 个准确系数的最小/最大值。它没有固定长度中点；也不要求 $P'$ 保持同号。

二阶导数没有剩余的 $\ell$ 因子。实现对完整 $P''$ 用次数 6 的全部七个 Bernstein 系数：

$$
a_{ss}(I,T)=P''(T)\subseteq
[\min_{0\le j\le6}\gamma_j,\max_{0\le j\le6}\gamma_j].
\tag{483.8}
$$

若 include_controls 为 false，$P$ 全部系数准确为零，仍使用相同完整槽与基底公式。当前五个实际 metric 视图均对完整十控制调用 true；这里的 false 只保库函数与原片范围函数的显式参数合同。

**命题 483.A。** 在 §483.2 的实际结构条件和原树包围合同下，complete_coast_range 返回的三盒，对每个允许 C/root 成员、每个 $t\in T$，同时包含原完整十族的 $(a,a_s,a_{ss})$。

证明由 (483.2)、(483.6)–(483.8) 逐分量成立。支撑外的另外七项由准确零延拓及闭端点二 jet 为零，不改变三盒。未选择新公式时，调用原完整片求值器，因此本次没有缩小原允许族或丢掉一个未识别分支。

## 483.6 公共坐标、所有准确片与原 radial target

设当前 field 保存的准确 binary64 长度词为 $L_{\rm num}>0$，原目标的准确长度为 $L_\omega\in I_L$。对数值坐标闭区间 $[s_0,s_1]$，适配器沿原 R400 的实际公式形成

$$
U=[s_0/L_{\rm num},s_1/L_{\rm num}],\qquad
S=I_LU.
$$

对每一个原准确 piece $j$，保其真实 anchor 盒 $A_j$、正宽度盒 $W_j$ 及原 local_interval $J_j$，形成

$$
T_j=((S-A_j)/W_j)\cap J_j.
\tag{483.9}
$$

只在交为空时略过该候选。所有非空候选调用本稿 piece_range，再对三 jet 分量取 hull。代码循环整个原 pieces 列表；未以名义 $u$、数值 piece、某个中心或单一支撑决定唯一准确分支。

任取实际成员 $\omega$ 及区间内一点。它的真实 $s=L_\omega u$ 落在某个完整准确 piece 的闭范围，故其真实局部坐标属于 (483.9)，该候选不会被删。共享端点可以同时属于多个片；全部保留只扩大包围。命题 483.A 或原非 coast 包围覆盖它，因此最终 hull 覆盖全部成员和全部点。

原径向 metric 不被 coast 消去式替换：

$$
g_{11}=(L_\omega/L_{\rm num})^2,\qquad
g_{22}=a_\omega(L_\omega s_{\rm num}/L_{\rm num})^2\,\Phi_q^2.
\tag{483.10}
$$

适配器沿原 Box 公式返回 $(I_L/L_{\rm num})^2$。它不令 $L_\omega=L_{\rm num}$，不令 coast 局部 $t=u$，也不把当前 field 变化的物质密度 $\Phi_q$ 当准确 C 的函数。

缓存只按完整准确有理端点 $(s_0,s_1)$ 保存已经形成的完整返回，容量仍为 64。缓存不跨 field、目标、参数或 job。开始而未返回的查询保留 completed=false；缓存计数不等于全域证明。

## 483.7 原 metric 与 evidence 的条件传递

新固定-query视图以 R418 为准确基线。新 original112、resolution112、completeM live 视图分别以 R426、R441、R451 为准确基线。每个视图保持原完整加载器和实际 family，唯一数学调用差异为：

- genuine current_bundle 加载完后构造独立 prefix_range；
- 原 prefix 分支调用 Prefix.inspect 时，把该局部 range 对象作为 target 参数；
- native/collar/tail、帽、反射、原 angular density、六 jet、全部模态与 means 的路径不改；
- 原四个 Loewner 条件、所有严格比较、eta、空间根 universe、细分与预算停止保持原文；
- live 查询仍由原 R426 provider 处理同现场 C，原 11 个参数和已提交粗界责任不改。

R459 的新 evidence 视图显式加载这三个新 live metric 来源以及 helper；构造相同适配器。在其真实 target 方法的 prefix 分支，closed_range 改为该适配器调用，因此全空间闭域 metric 评价和实际 nested-time 见证都使用同一范围实现。all_time_transfer、共同 first material/完整闭面目标签名、原 deadline、真实 sup 下降与仅上界改善的区分、compare 及 strict 条件保持原文。原 current.target 本身保留，因此场、共同材料与目标身份没有被区间实现替换。

**命题 483.B。** 若原相应 consumer 的实际输入与原条件满足，则把它的 prefix 目标三 jet 替换为命题 483.A 和 (483.9) 的包含盒，不破坏原 metric/evidence 所声明的包含结论及通过判据。新的独立 schema 只标记实现来源，不增加数学通过条件。

证明是原包含运算的代入：场和目标准确对象未变；新范围包含全部所需目标值；原区间 Gram/Loewner 或相对算子包围的每一步仍作用在一个包含盒上。原严格成功因此仍是同一准确对象的充分结论。新盒与旧盒不必逐 cell 相互包含，代码也未声称必然更窄；数值成本、通过次数和能否消除某次未决都需实际 Actions，不能由恒等式预付。

本命题不把 prefix radius/metric 成功扩张成全部 scalar speed、factory 起点域、native、FD、全 DN、reach、held、IEEE 形成误差或最终求解成功。它也没有补付固定 C cut 叶宽度、全头累计积分或模型语义盒造成的不可由空间细分消除的责任。

## 483.8 实际源生成与身份不混用

小计划包含五个原基线完整 bytes/SHA、各新 basename/schema/frame、每个唯一字面替换及预期计数、完整新输出 bytes/SHA。生成器先逐个核原件与所有替换计数，并在内存形成五个完整结果；只有全都符合声明输出身份后才逐个以新名字写入真实 checkout 的 computations 目录。每个已写结果再次核完整字节，原文件不覆盖。原 transitive source graph 留在实际目录；没有复制为一个缺 import 的私有目录。

生成器不导入、AST、编译或执行科学源。它的正常源身份/路径检查是形成可执行输入的工程绑定，不是新增数学 fixture。实际科学仍只有未来显式 caller 才调用；本文没有创建 request、workflow 或 dispatch。

计划的小直接清单不代表全部科学递归闭包。后继 caller 必须保原每个 consumer 的完整旧 pins、原输入以及原递归加载器，再增加 helper/generator/plan/五个生成源的实际身份。旧 schema/field/result 不被改名成新源。五个 review 文件和完整 diff 是暂存审阅材料，不把五份大源码重复放入 Git。

helper 为 18291 B /3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae；generator 为 8742 B /d149d85103fd555908239f71f963b575a8197a210584d0b043b5d9415c106ae1；完整 plan 为 31012 B /7e71fe0cbff882060bb64b576f3b9e5f56fc6b548f97d1786587ad1bceef00d1。逐基线及输出身份、实际命令在[独立接口](../notes/2026-11-16-complete-coast-metric-range-adapter-interface.md)。

## 483.9 事务、未付与当前结论

各原 metric/evidence 的原 wall clock、累计 C-query work、原资源停止、pending/coverage、90KB 必要摘要与溢出返回仍保。适配器不另开时钟、不删 raw、不启动 child，也不声称持有外层 owner quiet。新输入绑定写入 range 实现 receipt，实际开始/完成/回退计数另列 actual_prefix_range_work；该计数不会改原 completed 或 whole-domain flags。

生成器自身只产生一份必要 metadata receipt。源生成完整和科学完成分开。早期参数/路径绑定失败可能连 receipt 都未产生，后继必须保存真实退出/stderr并保持未启动，不能造完整 receipt 或据此清除未读现场。写到一半失败则记录已写源和当前地址；未完成的输出不冒完整五视图。任何必要摘要超 90000 B 返回 70，不拆包、不截断成功；后继 cleanup 仍须遵从真实 owner/必要读回合同。

当前已完成的是独立源文本、字节组成和上述条件证明。没有运行新的区间计算，因而没有声称初点全域已付、metric 达到某值、真实误差下降、同一 job 能完成全部工作，或 R464 union 已被这五视图覆盖。
