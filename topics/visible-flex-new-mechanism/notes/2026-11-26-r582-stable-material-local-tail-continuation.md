# R582 同 p=0.181：稳定材料求值与16个实际尾形自由列

2026-11-26；会话 Astra-new-mechanism-0105020f-20261126。

这是已闭账 radius-only 失败后的新有限逆设计空间。没有本地科学执行；旧求解、旧三种子比较、旧射击根不重放。失联前已完成新源码 AST、绑定和真实续态静态核；本地环境于随后失联，三份源码从精确编辑恢复，逐字 SHA256 与失联前相同。本说明在云中重新整理，原始源码身份保持。

## 1. 实际来源与保留状态

来源 run 45827253372 /job 139934478969，source d4a5b41506139a2bd7ad6d53a473e1766f536377；原 FINAL JSON SHA256：
397a1a6fb7999c36f4849956ef6b820ba615118ce9733ebf0e6356a6ecbfb169。

采用真正保留的81q，binary64 SHA256：
d4afde612de65692d4f0184948565ca13b39a4bc04d85429a9103fae7e41f2b0。
未接受的末 natural backend q 不作新输入。p从0.181开始，原 actual trust=1.220703125e-6 与 proposal=1e-6分别保留。原状态未过几何门，不能自动提高p。

原实际约束124×192、完整 fine 10835×384、pending径向空/角升级false。输入所需旧5911个材料观察位置、124个实际圈，连同既有4811个基础点及124圈相邻中点，准确重组原10835个位置，SHA256：
5205d5a834717e06250bcbb1f98bec1139130ed42c20ed7e77d274ccf6346f52。
失联前此并集已与原 FINAL 完整数组逐项相等核过；正式入口再次核这一身份。全部这些位置进入新接受门，不能因表示或自由列改变而删旧物理观察点。

已发表原收据 commit f28e377f69168b22537e82f49a4993349c1fa919，路径 notes/2026-11-26-r582-finite-radius-only-original-receipt.md，9762 bytes，SHA256 e8781d68fca91b48896369af506b1ddc3ba904f81cc3d7d4eb15937c73537a4f。本请求绑定该公开版本。

新 input 剥去 resume_origin、resume_state、本次已付成本并恢复原 schema 后，canonical JSON 必须恢复原 radius-only input SHA256：
187a463fdd777d2884310ac0793ed96583d5216d47407795b53daae633c46ac4。
旧验证器继续核到真实共振根、mouth和更早成本，不替换原mu/nu或paid M169/factor8口。

## 2. 已知失败的位置限制了什么解释

原首完整细网即观察 eta≈0.996、曲率≈8413。原核心射击阶段的场幅和二阶幅只覆盖到mouth，不能充当整尾界。

纯原日志解析进一步给出：5911个材料观察恰为2×2956−1，无合并丢点；eta峰 s=0.8691932771929971 是 index2074，即所选材料端点。在旧 endpoint evaluator 该点 t=0，value/first/second恢复共享端jets。因此严重一阶尾部变形不能仅由区间内二导相消解释。

曲率峰 s=0.8716776757406842 位于已选材料观察端点之间，仍需同点 dense/原Hermite/稳定Hermite对照。原日志未保存62878端点六jets，故没有在本地补算或断言全部失效来自浮点。两名agent纸核每段canonical log-scale及真实 field_jets，没有发现尺度方向/链式导数错误，但此纸核也不是ODE或C²误差证书。

## 3. 同一端点quintic的稳定求值

新 helper r582_stable_material_field_20261126.py 保留材料结点及共同端点0/1/2jets。对宽h、t=(s−s0)/h，采用

$$
P(t)=v_0+htv'_0+\tfrac12h^2t^2v''_0
+R_0H_{01}(t)+R_1H_{11}(t)+R_2H_{21}(t),
$$

$$
R_0=v_1-v_0-hv'_0-\tfrac12h^2v''_0,\quad
R_1=h(v'_1-v'_0-hv''_0),\quad R_2=h^2(v''_1-v''_0).
$$

右端基为10t³−15t⁴+6t⁵、−4t³+7t⁴−3t⁵、t³/2−t⁴+t⁵/2；实际一、二导均从此同一多项式微分并除h、h²。二导先取v0''，再加三个余差项，不把两个独立O(value)项相消后整体除h²。

余差与求值使用numpy.longdouble，正式记录实际mantissa位数和成本。literal结点直接返回共享输入jets。数学定义仍是同一端点quintic；余差是求值辅助数据，不是重新拟合的独立系数。guard bits不消除端点本身的不确定性，未认证C²误差。

同一正式run在两个旧峰和邻接端点/中点打印少量新诊断：真实h、两端六jets、旧基式/稳定式/dense值与ODE jets、余差及余差/h²。还报告epsilon乘seed A_s/C_s后，相对原冻结背景a_s/z_s及子午速度的比例。这里的原背景身份明确，不冒称当前有限trial的实际度量；a_s/z_s从真实尾公式读取，不额外求不需要的高度积分。所有诊断收费后自动继续优化，不另开预检run。

## 4. 新97q空间

新 model r582_local_tail_columns_model_20261126.py 的坐标顺序为：原前80项，新增u的8项，新增v的8项，原高度h在最后。零新增项将真实原81q嵌入新空间。

四个C∞开启函数χ_j的开启区间为(.78,.82)、(.82,.84)、(.84,.86)、(.86,.88)，每个配sin2theta与sin4theta。若U,V是原实际材料场经过相同a商法和core补偿后的径向函数，新增项为

$$
\Delta u=\sum_{j,m\in\{2,4\}}b^u_{jm}\chi_j(s)\varepsilon U(s)\sin(m\theta),\quad
\Delta v=\sum_{j,m\in\{2,4\}}b^v_{jm}\chi_j(s)\varepsilon V(s)\sin(m\theta).
$$

每场8列，onset-major、mode-minor；0/1/2jets包含χf、χ'f+χf'、χ''f+2χ'f'+χf''。角导含真实m，参数AD含完整新列。实际位置primitive、T和空间jets、E均值微分、全部基本形式及曲率行保持原参数式，不除a_s或z_s。

新列在s≤.78恒零，核心准确数据不变；它们共享数值seed零suffix。原beta列仍保留。新增系数盒[-2,2]，原坐标和h盒不变。这些是新的有限逆设计方向，没有宣称它们仍属于准确线性核。稳定求值的浮点值可略异；新网重新观察，旧资格不免费转移。

## 5. 真正的续接与接受门

新 driver r582_local_tail_continuation_20261126.py 从原124圈/192角开始，加开启口作为新约束位置；构造且完整扫描后才记新实际状态。所有旧10835位置、新材料观察、实际圈和中点进入fine精确并集；fine角数是实际的2倍。

新initial trust显式取1，绝不冒称原trust未变。步尺度为原角系数0.05、原a/z均值系数0.02、新尾系数1、高度0.01。这样给新尾形方向真实幅度，未把原所有坐标都放大到1。

恢复slack包含已知完整fine违反量，不将明知旧峰当作第一步新发现。恢复保留须改善超过max(1e-10,1e-9*max(1,V))或真正可行，避免旧7.7e-12的变化再次被算作有用进展。无接受、无新峰的自然outer连续3次后保真末态，不重复旧14次无效减trust。

完整门仍为R=1.012、Y=.3928、tau=.06072、meanE≥.25、det≥.1、margin=.001、tol=1e-8。metric接受先要求完整fine几何。p固定.181，只有全部几何及eta≤2.5e-7才能提高p；最终p=.8还须eta≤1e-7。改变q/p会改变均值g，没有固定g精化宣称。

新97维参数算子在同正式run只做一次必要方向核对，成功后继续且复用已付相同初值Jacobian。原81维核不冒作新核。实际保留态、未接受trial、natural OptimizeResult、actual/pending网格及trust继续分开输出。

## 6. 费用、失联恢复与完成范围

一lane，Python3.12.14/numpy2.3.5/scipy1.17.0；50分钟job、科学2400秒合作时钟、stdout-only。入口先真实pull双仓并核规则；18个源/工作流/已发表收据绑定。API读取不称为pull。

原setup 70.62187625499996秒、有限失败214.6783520880001秒及全部更早账均保留。原15outer/43callback、旧inner DtN、三seed比较和旧射击根不重放。原大dense/端点数组未保存，下一必要内部场构造须新计全部成本，不叫免费恢复。

失联使当时尚未发表的新request与本地原log暂不可读。恢复输入只从同一已自然结束的官方原job重新读取必要q/观察位置，核原raw和FINAL hash；禁止以旧q、少点近似或未接受trial替代。仅必要下一步数学配置可checkpoint，原raw和大FIELD数组不入Git。

必要输入现已实际恢复：run45839756631/job139977999607，source67771b35a44860689e39e4175f2b65220c55407c，于14:31:11UTC自然success。读取同一原13MB日志，原raw及FINAL身份均准确命中，失联前218542B配置SHA470a67d1b19249bdd08fc8b63cd129c12a4bf71b8e30c5b24a51c0ef496d0e3b逐字恢复；仅补已发表收据来源后，实际下一输入为218828B、SHA2e8a7c17398dde5e2e9fedfdf39f81823664b3861e3a33b6563da633b8fd5b91。恢复自身wall4.237356066000018秒、科学调用0。真实public pull读至8bed9c0efe6bdca745b65dba7eb8f8d702c3ed5e，private读至cbdb77bda461f510b4685e9be7b31253ddd8bbec，三个规则blob未变。恢复后本地只用stdlib核81q/124圈/5911材料位置/10835完整并集和原98910B输入哈希，不调用数值模型。独立恢复收据保留此次来源及费用。

本包没有预先执行科学。有限非圆、准确等距族、固定g收敛、连续全曲面reach和README完成门均未付。数值零suffix与无限flat核不同，ODE/DtN/材料/FFT/求积误差仍未严格包住。
