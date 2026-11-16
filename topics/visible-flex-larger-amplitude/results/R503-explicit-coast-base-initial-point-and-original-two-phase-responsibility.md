# R503 — 显式的新 coast-base 初点与完整原453→450责任

作者：ChatGPT /root（AI）。日期：2026-11-16。

**已完成：下面的新参数点构造、准确局部性质及三个独立源视图；未执行新候选算术、factory、native、BVP或闭面计算。** 本文继续求解，不把一个障碍当作完成，不改变正在运行或已冻结的入口。

## 503.1 实际证据及其有限推论

[实际212/R478](R478-request212-complete-shallow-physical-sampling-and-BVP-startup-storage-stop.md)在run43810550597、source9a9dbfa80ddf2c68d2dfda8e2b8c8a93d7e82060返回完整原candidate诊断：
every_retained_C_choice_center_refuted=true、center_strict_speed_domain_enclosed=false、new_acceptance_gate=false。
这是已经返回的独立准确中心诊断。原BVP另因真实free11761553408B小于原34359738368B而根本没有启动；不得把中心诊断写成该job的实际数值RHS异常或Newton拒绝。

[R449-C](R449-actual202-to-accurate-continuous-ten-fresh-candidate.md)已证明，同一准确coast的中心速度为

$$
a_s(1/2)=-\kappa+2L_C\theta_3.
$$

真实56cb两阶段驱动的设计阶段，ACTIVE_INDICES=[0,1,2]，七个shape固定；CurrentTenProfile.view调用frozen_seven_shapes。因此三个p不改变这个准确中心值。实际212中心结论结合这条源码，说明保持其同一C族与固定theta3时，单改三个p无法修复该准确必要条件。

这不是新的不可能性定理，不否定其他theta3、其他目标或其他机制。准确全族反证也不自动证明有限编译器在某个实际mesh节点返回NaN。真实56cb.prepare_design先在全部新节点重新计算RHS，原isfinite失败才在preflight/currentH/Newton前抛原异常；本文没有实际执行它，不预填其结果。

## 503.2 明确改变三个初始坐标

原202的完整十个Decimal50字符串仍取原553B参数数组：
SHA256 ba7d7fe3c7fd2599bb7f06863c117b11c6c9f4feb255a160de13023e22129369，原run43784544723/source1a757004b7ebff1f43563bd57b5d13961648d681。
先按照原R449程序，把每个字符串作为准确有理数，再作原binary64投影。记投影后的完整十词向量为q，顺序仍为

$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi).
$$

定义新的初点p为

$$
p_i=
\begin{cases}
+0,& i\in\{2,5,8\},\\
q_i,& i\notin\{2,5,8\},
\end{cases}
\qquad\text{索引从0开始。}
$$

因此只把p3、theta3、eta3显式设为正零；另七个**原投影字词**逐字保留。这不是把原Decimal50点冒成准确保留，也不是把原九族或actual180参数暗中带回来。三个零的选择由新source直接声明，不根据未来失败数值偷偷调节。

新的准确坐标就是所选binary64词的准确dyadic值。原字符串、原投影词/hex/准确值、原投影差额、每个实际选择后的词/hex/准确值、相对于原投影和原十进制的两个准确差额，全部分别输出。对未改变的七个坐标，保存的是原投影后的词；不声称原Q解析之前的某个负零文本已保留。三个改变坐标的正零则是新政策的明确组成部分。

新点通常改变角向目标系数，即改变目标度量。这里没有沿不同目标比较merit，也不继承旧R449/202的domain、J、残差、field、接受或几何结论。新的参数初点不是全场零解；原lambda=.001与完整非零低core目标仍原样，物理338/core112和全部方程不删。

## 503.3 准确coast的完整条件证明

采用[R481](R481-fixed-ten-semantic-domain-and-complete-coast-polynomial-enclosures.md)已经确定的真实支持与[R386](R386-accurate-coast-uniform-feasible-scaling-and-C2-bounds.md)的准确基底。对同一许可C实例omega，coast长ell=L_C(omega)>0，局部t=(s-S1)/ell属于[0,1]，完整profile为

$$
a(s)=A-\kappa\ell t+
\ell^2\{p_3B_0(t)+\theta_3B_1(t)+\eta_3B_2(t)\},
$$

其中B0=64t^3(1-t)^3，B1=B0(2t-1)，B2=B0(2t-1)^2。其他支持不进入coast内部；support1的xi在共端点也有零二阶jet。

**命题503-A。** 新初点在整个闭coast上准确等于原未加控制的仿射基底：

$$
a_{\rm new}(s)=A-\kappa(s-S_1),\quad
a_{{\rm new},s}=-\kappa,\quad
a_{{\rm new},ss}=0.
$$

若原构造的0<kappa<1、coast正宽度以及两个准确基底端值正对整个许可C族成立，则新初点在整个闭coast、整个该C族上满足a>0及|a_s|<1。它没有选择一个C根，也没有把一个cut中点当成同一全局C实例。

证明：三个控制项全部准确为零。仿射函数在闭区间上的值在两端值之间，故正端值给全段正值；其导数恒为−kappa，严格速度条件直接成立。所有结论逐一对omega成立，因而对整个原族成立。证毕。

这个结论是R386中beta=0的明确建设性实例，不需要搜索一个未知有限beta档数，也不因binary64极小数而下溢成未声明的参数。本文没有把此处端值前提改为新BVP前置门：新的原factory仍照旧实际检查其构造/基底/完整当前点，所有未决、未访和失败照原合同返回；原驱动仍保自己原有的来源和数值域条件。

实际212的base域曾完整，但那是其自己的真实C/definition。未来新job必须使用自己的真实原件，不能直接复制其base=true。即使该coast前提已付，也只支付这一整段；其它片、数值编译差额、完整初始RHS和求解仍另付。

## 503.4 支持、接缝、共同材料与未来p3变化

每个Bj在t=0、1都有至少三重零。新旧点的准确差值仅为原coast三项的负值，故其零、一、二阶物理jet在两端全零。其它准确分片逐点不变，原支持、自然长度、cut/cuff及C定义都不随这三个系数改变；公共材料坐标仍为s=L_true*u。

因此原准确C²接缝若已按原构造成立，这个参数改变保留它们。它不修复数值compiler独立圆整造成的接缝差，也不证明整个闭面、嵌入、reach或强C²的曲面变形族。准确非coast表达式不变，不等于所有数值profile执行都逐词相同；例如原0项累加与跳过的有符号零区别没有被本稿隐瞒。

第一阶段仍有p1/p2/p3三个活动坐标。p3初始为零，却不是在Newton全过程被冻结；theta3和eta3才仍属于七个固定shape，固定值为本次明确的正零。故沿这次固定theta3设计子问题，中心速度始终为−kappa；一般p3仍能改变coast其它位置的半径和速度。中心可行不能冒整个后续trial或最终coast可行；每个真实trial的原完整domain/RMS/BC等仍须执行。

最后得到真实453接受后，必须用其实际末十个词（包括可能已改变的p3）生成独立450问题，再实际支付完整当前H/FD/native/fullDN/final audit。最终同一g的精化冻结发生在真实新接受场之后，不能把原202、R449点、本次初点和设计过程中不同p的metric混在一起。

## 503.5 三个源视图与没有改动的完整求解

本次交付可复现source-plan与只处理源文本的generator。三个展开文件只在Actions实际生成，不重复提交展开源码。

| 角色 | 原完整bytes / SHA256 | 新展开bytes / SHA256 |
|---|---|---|
| candidate | 31509 / ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38 | 33550 / 5c62dd98ae8bf2e861248ccb0eabbacc86aceaa5f13cbc195cc6e42b511eae5c |
| 两阶段driver | 34835 / 56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615 | 34418 / 02ca1f2476f74cf3a5d83a044f689449fd785e4bc1018a039b5709340a211890 |
| owned launcher | 20657 / 227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7 | 20494 / d2a3107b5f3a556828a8031180fdf9b52ab8d2725061a1f68077a241cdf8b18b |

candidate有18个完整before/after合同、40次实际literal替换；driver为5/5，launcher为6/6。plan为18919B/2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3，generator为6663B/0c19c91b5b5a02eb68582427b91674b681a5eeebde5d731ad2ab91f3cb167e2e。所有身份由文本/字节工作形成，没有运行这些源。

driver只改变说明、独立schema和实际candidate来源。prepare_design、prepare_frozen、run_phase及原完整求解正文没有修改。它仍先读取真实accepted96和原完整699×453种子，只把旧场当初猜；全新节点RHS、原preflight、每phase新currentH、原边界FD、338×112响应、17档/8outer、RMS1e−6、BC1e−11、末fresh J与audit持续有效。原FD阈值5e−5及两阶段一个真实owner/PhaseLease仍原程序所有。

launcher明确同步新的candidate.schema，而不是沿抄旧R449硬字符串；它实际绑定新driver字节身份。原7200秒共享BVP上限、原namespace绝对钟、原34359738368B启动磁盘门、TERM/KILL/quiet及原结果记录正文保留。参数更改没有获得新预算或减少科学列数。

## 503.6 完整运输、原件和当前接线边界

原553B十词数组及c980e9d4输入仍只作为原source word依据，原INPUT_SCHEMA和原输入policy原样核对。新的candidate policy/schema与旧projection输入policy分列，不能把旧输入hash当成新点的身份。

新point字段使用candidate_binary64_parameters、candidate_binary64le、candidate_rows。每行包含全部原投影与新选择的准确信息，不用只列三个零而丢弃其它七个实际词。原prepare/bind/read_bound_candidate都真实消费这些新字段；新model和初始BVP须逐词/准确dyadic相等，并属于同一真实job/C/cut/factory/config/driver。新必要frame与事件明确为R503，仍单90000B/超70，不拆包、编码或删错误标成功。

这三个视图是以原ee367/56cb/227e为基线的核心预览，**没有宣称已经是218或未来220的最终完整source closure**。R496/R498改变了实际native、sampler和来源名；未来完整入口须把本明确参数政策作用到自己的真实candidate/driver/launcher，级联全来源/recipe/readers/CP/几何材料，并逐项保有R503语义。不能直接把上述预览SHA冒成已有gzip/新native闭包的最终身份。

后继还须真实消费全部新必要candidate行、完整失败/未返地址和原owner静止条件；不能只替CLI标签、漏新marker或沿用旧selector。这个普通实现接线责任不是新增科学审核、fixture、域前门或独立冻结门。

## 503.7 当前完成与继续

本稿完整条件证明和可复现源已经写成。现在没有新实际投影输出，没有新factory/domain，也没有新native、453/450接受、固定g误差下降或闭面。只有M96开放前缀的既有接受事实不变。

接下来在完整来源组合中启动独立新点，继续所有原科学和README目标；当前218及其它原运行不因这份构造被改写、终止或预填失败。同C的R489/R495/R500测量精化和逐H live128也保各自原任务。最终报告仍须同一新接受场的全t闭嵌入、握持/整像、含反射商、reach、全域metric与固定参数精化，不能由局部coast修复替代。
