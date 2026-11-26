# 新增独立 gamma 形状的完整六控制、九方程 KKT 与二十七角 jet 实现

日期：2026-11-26。状态：完整源码实现及静态代数审查；本记录不报告新的数值根、物理场、QP 方向或连续证书。科学调用只准在本公开仓库的 GitHub Actions 内进行。

本实现对应 [新增形状与 KKT 数学接口](2026-11-26-zero-endpoint-fold-and-added-shape-kkt.md)，沿用其中的条件范围。它增加一个与原两 bubble 线性无关的径向旋转形状，并以完整约束驻点方程选择内部控制。它不宣称已证明局部最小点、全局最小控制、全角同支或任何准确等距解的存在。

## 1. 实际改变的对象与保留的对象

底层仍为完整独立 R690 轴对称参考 `ClosedMeridianOperator`。当前外部点 $x$ 包括原全部自由 core 系数、全部共享五次/Fourier 旋转系数及最后一个高度 $H$。这些槽、顺序、固定前三个 core 系数及 core/cap 结构槽均不删改。新内部控制与乘子由隐式方程决定，不加入外部自由点，不以冻结原变量来换取闭合。

固定标量、准确符号域、固定材料角图及完整原始输入身份都来自本次真实 base。目标仍为该 base 已冻结的 $ds^2+a(s)^2d\theta_0^2$。改变的是实际嵌入的内部闭合机制；旧零控制场、旧目标值及旧几何证书均不继承。严格的旧参考输入模式与显式的新参考输入模式采用不同 schema，不能借用旧参考的哈希或仅更换标签。

外部 H² 坐标、正权观测、三个 Gram 分量、均值与混合行、全空间 QP、原曲率工作集、幅度双分支、永久位置及真实筛选仍须由完整独立 driver 接入。内部二次控制代价只选择闭合分支，不代替外部度量目标或几何条件。

## 2. 独立径向形状与完整六控制

设原两 C² bubble 为 $\beta_0,\beta_1$，其实际准确相对节点、十八个固定 binary64 矩阵字都进入模型身份。默认旧支持为

$$
(1/32,1/4,15/32),\qquad (17/32,3/4,31/32).
$$

新增 gamma 默认相对节点为 $(1/16,1/8,3/16)$。它在上升段用 $S_5(t)=10t^3-15t^4+6t^5$，下降段用 $1-S_5(t)$，支持外为零。构造器要求其整个支持严格包含在原某一个支持内部。它因此不扩大原修正支持并集，但增加一个独立径向函数：在 gamma 支持外、原第一 bubble 内仍有非空正区，第二 bubble 又与之分离，所以 gamma 不在两个旧函数的线性张成中。该函数独立性不等于某实际折叠点的端点导数必增秩。

记原矩阵函数为

$$
W(s,\phi)=\sum_i\beta_i(s)R_z(\theta_0(\phi))Q_iR_z(\theta_0(\phi))^T.
$$

使用明确的无量纲控制

$$
u=(\zeta,v)\in\mathbb R^6,\qquad \zeta=z/S,
\qquad B=[SW,\gamma I_3],\qquad w=Bu.
$$

本次源实际构造全部 $B,B_s,B_\phi,B_{\phi\phi}$，三个新 world 轴都保留。$v=0$ 时恢复原三控制的允许函数族；新 KKT 选出的驻点分支不保证恢复原算法选出的根或场。原三维球的半径不能直接解释为新六维球的半径。

修正后的单位切向量与端点缺陷为

$$
T=\exp([Bu]_\times)T_y,\qquad
C=\Gamma_c-P_{\rm cap}+\int_0^S T\,ds,
\qquad f=C/S.
$$

准确数学定义中的 $S$ 是原准确域长度；数值求值仍使用已记录的普通 carrier。这次实现不支付数值积分、准确宽度与 carrier 差、三角函数、归一化、root 或累计求和误差。

## 3. 九个 KKT 方程及完整 Hessian

选择的内部目标为 $|u|^2/2=(|z/S|^2+|v|^2)/2$，不增加 ridge、不删除零方向，也不把控制二次项混入原外部度量损失。引入全部三个等式乘子 $\ell$，令 $Y=(u,\ell)\in\mathbb R^9$。原始最终方程与 Jacobian 为

$$
\mathcal R(Y)=
\begin{pmatrix}u+f_u^T\ell\\f\end{pmatrix}=0,
\qquad
K=\mathcal R_Y=
\begin{pmatrix}
I_6+\sum_i\ell_i f_{i,uu}&f_u^T\\f_u&0
\end{pmatrix}.
$$

源码保留乘子 Hessian 项，使用当前完整 KKT 图的实际导数。没有将 KKT 换成 Gauss–Newton、仅六变量正定近似、有限差分或原三根 Jacobian。九维 KKT 的数值最小奇异值只作为同场诊断，不升级为连续可逆证明。

即使数值 KKT 残差达到阈值，本实现只记录 `selected_KKT_stationary_branch=True`，并明确 `SOSC_verified=False`、`global_minimum_verified=False`。由数学稿中的约束秩与切空间二阶正性可以条件性推出非退化局部最小点，但代码没有验证这些连续条件。

## 4. 完整角导数由同一约束生成

内部控制沿每条 meridian 不依赖 $s$，但随固定 chart 地址 $\phi$ 变化。设 $u_0,u_1,u_2$ 是控制的零、一、二角 jet。先由完整物理旋转公式计算 $T,T_\phi,T_{\phi\phi}$，并由同一 core/cap 三 jet 得到 $g_0,g_1,g_2$，即 $f$ 的全部 total 角导数。

把三套控制暂视为独立自变量，令 $A_j=\partial g_j/\partial u_0$。链式法则给 $A_j$ 正是 $f_u$ 沿所选控制角 jet 的第 $j$ 个 total 角导数。完整 stationarity 三 jet 因而为

$$
S_0=u_0+A_0^T\ell_0,
$$

$$
S_1=u_1+A_1^T\ell_0+A_0^T\ell_1,
$$

$$
S_2=u_2+A_2^T\ell_0+2A_1^T\ell_1+A_0^T\ell_2.
$$

源码等价地对标量 $\sum_{k=0}^j {j\choose k}\langle g_{j-k},\ell_k\rangle$ 关于完整控制 jet 求反向导数，再取 $u_0$ 槽，最后加 $u_j$。这保留全部乘子、原外部参数与控制混合链。`create_graph=True` 用于建立这些导数本身的图；当只进行 detached 数值 root 求值时才丢弃返回值的图。

零阶为 9 维，一阶 metric 隐式系统为 18 维，完整二角 six-jet 隐式系统为 27 维。27 个未知量包括三套六控制和三套三乘子。其块下三角 Jacobian 的三个对角块都是同一最终 $K$。物理场仅消费控制六槽，乘子仍留在全隐式系统及其转置中。

求得数值 $\widehat Y$ 及角 jets 后，源码以保持前向值的 surrogate

$$
\widehat{\mathcal Y}-\mathcal K^{-1}
\bigl(\mathcal R_{\rm jet}(x,\widehat{\mathcal Y})
-\operatorname{stopgrad}\mathcal R_{\rm jet}(x,\widehat{\mathcal Y})\bigr)
$$

实现一次外部参数导数。$\mathcal K$ 为该点完整 18 或 27 维数值 Jacobian，前向只减零，反向保留 $-\mathcal K^{-1}\mathcal R_{{\rm jet},x}$。没有对 Newton、continuation 或回溯轨迹求导。该方法声明的范围仅为一次外部参数 J/J*；不宣称可继续对该 surrogate 求准确二次外部参数导数。

## 5. 四阶混合导数与零旋转处的解析分支

角二 jet 的 stationarity 已含约束的三阶混合导数，完整物理 six-jet 再对外部点求一次 J/J* 会需要约束的四阶混合导数。不能把旧三根、九 jet 实现的标签当作这一责任已经支付。

本源复用并逐字绑定实际完整 base 中的 `rotation_coefficients`，不复制一个较低阶替代函数。以 $q=|w|^2$ 记其原小范数分支：当 $q<1/4$，$A(q)$ 与 $B(q)$ 分别采用

$$
\sum_{k=0}^{12}\frac{(-1)^kq^k}{(2k+1)!},\qquad
\sum_{k=0}^{12}\frac{(-1)^kq^k}{(2k+2)!}.
$$

原函数的 $A_q,B_q,A_{qq},B_{qq}$ 正是这两个同一多项式的准确符号导数经 Horner 表达的计算图。继续对该图求混合导数不会在 $w=0$ 引入 $|w|$ 的不可微范数或除零。未选中的大范数分支先把 $q$ 限制到至少 $1/4$，再做平方根与除法，所以零点附近也没有隐藏的无穷/NaN 分支。

这说明所需四阶导数由同一有限工作函数的完整解析图给出。它不是高阶导数的向外误差证书：截断余项、普通浮点运算、分支交界处的工作差异均未包围。精确指数及其混合导数与工作表达的差仍需另付连续误差。

## 6. 数值 continuation 与真实单位

每一个新外部点、每一个 literal 角地址，都从独立的 $Y=0$ 与辅助 `continuation_parameter=0` 开始。记 $r_0=\mathcal R(0)=(0_6,f(0))$，辅助方程为

$$
\mathcal R(Y)-(1-\tau)r_0=0,\qquad 0\le\tau\le1.
$$

$\tau$ 仅为数值求根参数，不是 README 的物理弯曲相位，也不是乘子 $\ell$。当前外部点、固定标量、$Q$、gamma 和外部损失均不随它改变。

预测使用完整九维 $K$ 解切向方程。每个角有独立的步长、阶段预算、拒绝与恢复；拒绝时准确恢复最后接受的完整九变量及其辅助参数后再缩步。阶段 corrector 用完整九方程的 Newton/Armijo，不以闭合三行代替完整 KKT。所有阶段失败只表示本次所选算法与域未获得根，不表示不存在闭合场。

默认新算法域明确为 $|u|<2$、$|\ell|<64$；不是旧三维 .5/.75 球的继承。默认物理闭合阈值与无量纲 KKT 阈值分别为 $2\cdot10^{-12}$。阶段求解的阈值取二者换算后的较小值：

$$
\min(\varepsilon_{\rm KKT},\varepsilon_C/S_{\rm working}).
$$

最终必须在 $\tau=1$ 重读原始未平移的九方程，并分别检查实际 $\|\mathcal R\|$、实际物理 $\|C\|=S_{\rm working}\|f\|$、两个开放算法域。把 $f=C/S$ 的阈值直接称作旧物理闭合阈值会暗中放宽尺度；本实现没有这样做。角 jet 的实际残差单列记录，仍不当连续 C² 接合证明。

## 7. 物理六 jet、端点和对称范围

对所有实际径向查询，完整当前旋转向量为 $w=Bu$，并使用

$$
w_s=B_su_0,\quad
w_\phi=B_\phi u_0+Bu_1,\quad
w_{\phi\phi}=B_{\phi\phi}u_0+2B_\phi u_1+Bu_2.
$$

物理场由帽向内积分，$F_s=T$、$F_{ss}=T_s$、$F_{s\phi}=T_\phi$，其余三 jet 由帽三 jet 与完整有向积分给出。角中心、core/cap 全链及原 meridian 所有变量均在同一计算图中。

因为两个旧支持和 gamma 都严格位于内域，准确数学输入的端口由原完整 base 条件保留。准确的全角反射、周期与 C² 拼接还要求所选 KKT 分支确为群作用下关联的同一连续分支，不能仅凭每个离散角数值收敛而宣布。这一条件在数学稿中明确；代码记录 `complete_continuous_root_branch_certified=False`。

在准确指数、准确单位参考切向、准确积分及准确闭合根定义下，径向 Gram 恒为一。数值实现仍计算原径向行，未删除其残差。混合与角向 Gram、全像握持幅度、含反射欧氏商非零、连续嵌入、reach 及固定问题精化收敛仍是原任务责任。

## 8. 源码、输入和缓存的身份边界

模型包含完整 base 模型、实际 source SHA、准确 scalar 定义与身份、固定 chart、原与新增支持、全部十八个常量字、控制代价、新 root policy、来源及 27 维隐式合同。restart 必须逐字相同模型及相同完整 source，不把旧三根 checkpoint 改标签接入。

当前 root 缓存以完整外部点哈希加 literal binary64 角字建立。外部点一变即清空；一角从 metric 读数升级到二角六 jet 时补全其角导数与 27 维矩阵，不把旧 18 维子矩阵冒完整二角线性化。缓存只保存本次实际数值根与当前图的数值矩阵，没有旧场证书继承。

旧参考模式保持原完整 `validate_frozen_moment_input` 函数不变。新参考模式必须经独立完整 binder，核本 run 的完整 base/ref/profile/initial point，再把十八个已刊字采用为明确常量参数。旧 trace 仅是常量来源，不能称本次真实工作矩的逆；默认不声称新参考与旧 raw 身份对应同一数学 $g$。若以后要主张相同数学输入，需另付完整定义等号，不能由路径、shape 或看似相同的数值参数代替。

## 9. 读数与失败范围

每次读数保留当前根数量、全角 grid 根是否齐备、物理端点/KKT/stationarity 残差、控制与乘子范数、两个角 jet 残差、数值 KKT 最小奇异值及原 core 逆图读数。失败记录保存实际原因、全部失败角索引与 literal 地址、完整九变量和残差，不以零控制补洞。

成本计数区分 KKT 方程角读数、KKT 矩阵角读数、stationarity 反向角乘积、隐式矩阵行数，以及所有九维线性求解的角尝试次数。求解尝试包括失败与随后被拒阶段；不能把尝试数称为成功求逆数。数值循环耗时和根迭代预算不是解析存在范围。

本次仅完成源码、静态代数与标准库 AST/compile 检查。未运行本地科学计算、随机 fixture、root、四阶导数样例、场、QP 或证书。真正公开 Actions 返回后，须按实际 source/input/完整报告逐条记真实成功、失败、未知和成本，不能把本说明的条件恒等式写成已达 README 完成标准。

## 10. 完整新入口与两个互斥的输入合同

新 driver、launcher 和纯 reader 已完整生成，未使用一段运行时补丁替换旧驱动。driver 从完整 `9649ed99` 入口的 `def save_report()` 至文件末尾保留逐字相同的完整优化体，包括所有原恢复/度量方向、原 C 前缀、幅度行、common-slack 的真实语义、同场度量/几何回读、拒绝后的永久地址和实际终态保存。新增代码位于源、参数、输入、模型及 root 读数接口。它不宣称接入尚未复合的 SOC 后继。

`--moment-input-binding same-reference` 保持原输入 schema、原完整定义和原当前 base/ref/profile/initial 哈希守卫。`new-reference` 则先由原纯参数文件读取器严格读取已刊 `df11d8a4...` 文件和 `05dc5ed7...` 原定义，再调用独立新 binder 生成新的完整定义。原十八字、原支持不拟合、不重新计算；旧 trace 的来源保留在 provenance。本次真实 base/ref/profile/chart/initial 的身份都进入新的十字段定义，旧 raw 身份不填到新字段。

新外层 schema 为 `new-reference-literal-zero-endpoint-Q-input-v1`，新定义 schema 为 `new-reference-literal-two-bubble-endpoint-Q-v1`。十个字段是 schema、全部十八个 hex 字、两支持节点、当前标量身份及完整定义、当前 reference bundle 身份、完整 reference model 身份、完整 base model 身份、实际 `base.initial()` 身份及固定 chart core 身份。新 operator 同时核独立 binder 的完整 source 和 `bind_to_base`、`parse_literal_Q` 的真实 codefile，再核转换后的每一个 binary64 字和反射稀疏模式。原 `validate_frozen_moment_input` 函数全文不改。

new-reference 只解决来源合同，不证明与旧数学 $g$ 相同或不同。新 raw 身份本身不能成为遗忘已指定永久点的理由。随附 portable ready 仅包括新 prepare 真实产出的 `locations.json` 所含初始历史；它明确不声称旧 run 的后继报告已经存在。最终控制器必须如实记录所选分支的历史范围，并显式提供全部应保的可用地址；带旧 carrier 身份的文件不能静默改标签通过既有地址守卫。

## 11. 完整 snapshot 与失败读数

driver 新增独立 `actual-added-gamma-nine-KKT-current-point-snapshot-v1`，从本次 `q.metadata()` 明确取出 27 个已声明的 root/KKT/continuation 字段，同时保存实际 operator source、完整 model 和当前外部点身份。纯 reader 递归绑定每一个 snapshot，完整 `latest_operator_metadata` 另行核来源和模型。当前点尚无成功根时，相关最大值保持 `null`；成功次数为零时，成功根累计最大值也为 `null`。不存在的点读数不从另一点的 latest metadata 回填。

这专门避免把旧 finite snapshot 中未提供的 continuation 键当作必有数据。标准库 AST 检查已逐项确认新 driver 与 reader 使用相同键表，并且每个键在锁定 operator 的实际 metadata 返回中存在；没有构造根或伪造数值报告来让该检查通过。

仅对真正失败的 stage，报告可保留该角最后一次已经计算的 9×9 K，附它自身的九变量、Newton iteration、shifted residual、stage target 和当前外部点身份。若之后返回状态不同，矩阵仍标原求值状态，不能冒作新状态矩阵。这只复制已经完成的求值，没有额外 F/J/SVD；完整矩阵与科学状态仅留 runner raw。随附 scalar selectors 不选择长异常 repr、完整矩阵或完整状态列表。

## 12. 锁定完整源与首预算

| 完整文件 | 字节 | SHA256 |
| --- | ---: | --- |
| `so3_zero_gamma_kkt_operator.py` | 94323 | `b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a` |
| `so3_zero_gamma_kkt_geometry.py` | 51803 | `0c4886237d642382a1ae329d36517d5752ba717f0fa1471993bb98769e828f17` |
| `new_reference_literal_zero_moment_input.py` | 22763 | `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39` |
| `fullclosed_zero_gamma_kkt_so3_qp.py` | 64235 | `5134d34d4f4393fc57d86eed329bd107b631b693668d1d04d602af5f286dc3f5` |
| `launch_zero_gamma_kkt_so3_actions.py` | 14969 | `e0925d2628bf88760042dcdc3d998ec3a4ff51977d49a4568f6a543bf5fa4bb0` |
| `read_zero_gamma_kkt_so3_report.py` | 38861 | `42c0c0f043cbbbc0335a8faed9d91f9f6583cb7501d40dca0fcef6b834d69e14` |

另附纯源码再生器 `derive_zero_gamma_kkt_entry.py`，30119 B，SHA `350dabb5b2f1252e5486c596bc7faaba465f99c301b5b498b4471ced425949a5`。它读取逐字绑定的三个完整旧入口以及明确传入的三个新依赖，产生完整新 driver/launcher/reader；只使用标准库，并核原优化体逐字等号。它不导入科学模块，不在科学运行时替换方法。

geometry 的 `_set_x` 至文件末尾与原完整 `e4a3271d` 版本逐字相同，后缀 SHA 为 `50d6f1414807ea91710ecf3a0e3e52d9530a04f299763d2a05f30c372f27bf7e`。新的 constructor 仅绑定实际新模型、六控制/九 KKT/二十七 jet 合同及双输入 schema；完整原扫描、工作集、world pullback、两套永久地址和幅度计算未删减。

首 portable ready 给出完整 argv 与纯读数步骤：实际全角 $N=2048$、原全部正权径向观测、工作积分阶 8、角块 8、固定原 jet-sum H² 坐标与明确 $\mu=.01$、一个最多 16 步的完整 metric QP 方向及最多四个 64 步恢复方向，原 15 次真实 ray 筛。新增 root 默认采用前述 $|u|<2$、$|\ell|<64$ 与双 $2\cdot10^{-12}$ 阈值，辅助 continuation 参数明确列入 argv。首预算并不限制以后继续研究的总时长或可用空间。

源码默认的外部变量、范数、C 与真筛均完整；首预算是否获得初始根、是否形成完整物理场、是否到达外部 QP 及实际成本都必须等公开 Actions 返回。本说明没有给未返回的科学值。`--print-command` 只用于完整 argv 复核；launcher 的其余科学执行与固定 CPU PyTorch 安装均保公开仓库双重 Actions 守卫。


## 13. Root实际复核与刊出边界

Root完整读数学/实现说明，逐段核新增operator全部方法和原源AST差异、driver/launcher/reader完整diff、geometry完整diff；再次实际AST/compile全部八份新源，并逐字核原driver `save_report` 至EOF、原geometry `_set_x` 至EOF及旧完整输入validator均不改。operator相对3f的39个方法/顶层函数AST完全相同；新增完整9/18/27链单独审读，不把未变计数冒科学验证。两代理另核四阶隐式链、constructor关键字及27键snapshot生产/读取合同。

完整operator再生器 `derive_zero_gamma_kkt_operator.py` 为46612 bytes/SHA256 `8b257d145772a26a45ef78c43b06fce970998c1465aa35b45c9d48230146f5bb`；它与实际完整body一并刊出。geometry完整实现说明见[几何接口](2026-11-26-complete-gamma-kkt-geometry-interface.md)，派生记录见[operator](../computations/resume-20261126-gamma-kkt-operator-source-derivation.json)和[geometry](../computations/resume-20261126-gamma-kkt-geometry-source-derivation.json)。

[完整portable参数](../computations/resume-20261126-zero-gamma-KKT-new-reference-first-ready.json)仍只声明初始reference locations，不是最终已入队科学请求；旧g的适用完整永久历史必须另明确补入。05实际run45870334713/1已执行必要warm/reference bootstrap（触发c6ed266ecbb59043328c5a033389cbf379344c35），尚未执行本gamma机制。其后继将保原数学输入及所需历史闭包；不为省旧永久位置而微改g。本次没有科学执行或数值成功结论。
