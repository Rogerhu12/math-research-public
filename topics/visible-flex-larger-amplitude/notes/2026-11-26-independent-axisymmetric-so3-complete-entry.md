# 独立 R690 轴对称单位子午线的完整 SO(3) 求解入口

本入口以原完整 warm 的准确标量、符号节点和完整 core 为输入，直接构造 R690 的轴对称单位子午线。它不需要旧 q 场的 28 个非线性方向，也不把旧固定深谷、moving mean 或 normalized-parent SO(3) 的报告改标签后使用。原先六源入口保留其字节与父类型；这里是另一组完整源码、独立 schema、实际新场和实际新基线。

本说明落实 R690 的标量输入与 R692 的旋转表示。R694 提供条件误差代数；它没有替本入口支付连续积分、逆图、浮点或全曲面几何证书。下述所有科学计算只在 Rogerhu12/math-research-public 的公开 Actions 内运行。

## 1. 实际输入与准确固定问题

必要前缀由独立 warm-only recipe 再生。它保留原 prefix / pulse / fullclosed-hold-warm producer，输出：

- fullclosed_solver/data/fullclosed-hold-warm.npz；
- fullclosed_solver/data/fullclosed-hold-warm.json；
- fullclosed_solver/data/pulse-a5-complete-base.json.gz。

本入口只从 warm 的 qjets 读取完整 core 系数；不将其旧物理场的 Fs 或几何状态用作 T0。准备程序核 warm 自身 producer SHA、bundle SHA、scalar-input SHA、923 个节点、M=160、固定前三个 core 系数和准确 affine core 条件。旧 warm 高度仅记录来源；新的初始自由 H 明确选为工作 Gauss 规则下 c 的全径向积分。H 仍是完整自由未知量。

准确域继续是原节点报告中的 affine-in-S 节点和准确原 S。mesh 中的 binary64 数是这些对象的计算载体，不能将它们偷偷改成新的准确物理域。完整原标量参数与节点身份先核对，再构造 R690 的准确新尾。新固定度量是

$$
g=ds^2+a_{\rm deep}(s)^2\,d\theta_0^2.
$$

准确 a_deep 的定义由实际 e091 标量源码、实际原标量输入和完整 R690 参数生成。准备报告记录其完整 canonical definition 及 SHA256。没有把历史 profile 383168… 当作不可解释的常数；实际准备得到什么准确 profile 身份，后续就逐字冻结什么身份。不同工作积分精度或 cutoff 不改变这一定义。

每次正常续接必须保留同一 reference bundle、observation carrier、原 node report、scalar input、完整准备报告、来源和 canonical model。修改标量公式或参考 core 属于新输入，不能用普通 restart 掩盖。

## 2. 完整轴对称参考 T0

令 $\theta_0(\phi)=\Theta_{c_0}(\phi)$ 为由初始完整 warm core 冻结的材料图，$\rho_0=\theta_0'$。定义

$$
T_0(s,\phi)=b(s)e_r(\theta_0(\phi))+c(s)e_z,
\quad b=a_{\rm deep}',\quad c\ge0,\quad b^2+c^2=1.
$$

完整输入不能只实现最后一段新尾。WholeAxisymmetricLaw 分别实现四段：

1. 原 quintic prefix：从原准确 quintic 系数直接计算 b 与 b_s；复用原 oracle 已证的全 prefix $|b|<1$，由正分支 $c=\sqrt{1-b^2}$、$c_s=-bb_s/c$ 求值。
2. 原解析延拓：同原准确相位 $\alpha$，取 $b=\sin\alpha,c=\cos\alpha$，且 $\alpha_s=-K$，因此 $b_s=-Kc,c_s=Kb$。
3. 原完整 Hold：同已刊 e091 复用的原准确相位 / 曲率公式，取 $b=\sin\alpha,c=\cos\alpha,b_s=-Kc,c_s=Kb$。
4. 完整 R690 新尾：取 $b=-\cos\beta,c=\sin\beta$，$\beta_s=-K$，因此 $b_s=-K\sin\beta,c_s=-K\cos\beta$。

靠近帽端不以浮点 $1-b^2$ 求一个可能已经消减为零的 c，也不在该处除以 c。cutoff 以下仍包含整个无限尾及完整误差盒；没有删除无限尾。跨新旧连接位置的点盒用两侧并集包围。准确端口明确置为

$$
T_0(0,\phi)=e_z,\quad (T_{0,s})_z(0,\phi)=0,\qquad
T_0(S,\phi)=-e_r(\theta_0),\quad T_{0,s}(S,\phi)=0.
$$

向量接口全部是真正 world 坐标。准确角 jets 为

$$
T_{0,\phi}=b\rho_0e_\theta,\qquad
T_{0,\phi\phi}=b(\rho_0'e_\theta-\rho_0^2e_r).
$$

每次查询返回 T0、T0_s、T0_phi、T0_phiphi 和固定 chart 数据。数值载体 b,c 再以自身正范数归一，b_s,c_s 同时通过完整归一导数转换。准确 T0 本来是单位向量；此操作只规定实际计算图，不能代替其浮点误差付款。

prepare 在原全 Gauss6 观察点与工作全胞 Gauss8 积分点的并集缓存四个标量 jet / 误差。之后新永久位置的标量由同一个 WholeAxisymmetricLaw 实际求值，不插值旧数组，不重建旧优化 q 场，也不为每个角块重新构建 300 秒的尾积分表。

## 3. 真实新场、所有变量与 J/J*

新的完整 operator 保留原 SO(3) 的旋转、shared quintic、全部正权 residual、J/J*、世界六 jet 与 point VJP 主体。令

$$
T=\exp([\omega]_\times)T_0,\quad
P=R e_r(\theta_0)+H e_z,\quad
G=P+\int_S^sT,\quad
\Delta=\Gamma_c(\theta_0)-G(0,\theta_0).
$$

本首版实际场仍为

$$
F=G+h(s)\Delta,\qquad
h=1-10(s/S)^3+15(s/S)^4-6(s/S)^5.
$$

故实际径向导数是 $F_s=T+h'\Delta$，而不是单独 T。全部 Gram、六 jet、J/J* 和几何 covector 都使用完整 hDelta 场。径向误差没有被声明恒零。H 的实际导数包含 $(1-h)e_z$。

完整变量是 M−3=157 个自由 core 系数、所有三旋转通道的共享 quintic 节点 jets，以及自由 H。旋转通道采用 x 的 odd sine、y 的 odd cosine、z 的 even sine；仅强制 core omega 值为零与 cap omega 值、斜率为零。共 $2766\times482+157+1=1333370$ 个自由变量，没有低模求解或部分固定 core 替代。

固定初始 chart 与移动 core 不混淆。每次真实场都解
$\Theta_c(\phi_c)=\Theta_{c_0}(\phi)$，实际完整 current core 进入 Gamma、Gamma_phi、Gamma_phiphi 与全部参数导数。有限 Newton 迭代的实际根残差必须通过所声明容差；其误差与浮点尚未作全域严格付款。首次完整方向使用与原 SO(3) 相同的完整 CPU torch 2.5.1 图；不能把其有限 root 图叫成已证明的准确无限迭代导数。

旋转的规范冗余没有删掉。一般位置的规范方向是右旋转 about T0 经 chart pullback 的方向；只有 omega=0 时才可简单写成平行于 T0 的 omega 变化。新正定母范数与正 mu 明确支付全空间。

连续 omega 空间只在 R692 指明的经典正则性、局部非反平行图及端口范围内有覆盖解释。有限 M / quintic 试探空间的逼近、固定问题精化和完整非圆存在仍需实际推进，不能由本源码归因推出。

## 4. 正权目标、母范数与 Phase I

每个原 node / midpoint 观察位置保留，继续增加每胞六 Gauss 点：1845 个原观察与5532 个正权观察，总计7377径向点。全角 N=2048；quarter orbit含513角位置，全部角轨道重数的和仍为2048。母问题完整 metric 三分量全部保留，包括所有均值与 cross 行。

首建议 p4、epsilon=.001、scale=.05、legacy_fraction=.5。Phi 使用同已刊 centered 形式和完整正 Hessian；不能把先前 normalized-parent / q / moving-mean Phi 减去这个新初始 Phi。

坐标范数完整继承已刊 SO(3) 的显式新 norm：默认正 node-jet H2-type jet-sum，径向长度 .05，角频过渡24。每个实际通道频率 k 的因子为 $1+(k/24)^2$。它不是原 q 的 H²，也不是 exact integral Sobolev 范数。可明确选 integral 分支；失败不会静默改 norm。mu=.01 是该新坐标单位内的算法参数，记录真实 norm identity 与每步实际 mu。

完整旧 e783 selector 的192工作行前缀保留；新 world point shim 将每条导数回传到真实新场的所有变量。再追加选定幅度的半径、±p 两支距离及 cap/H 行，最多12行。原前缀不删以腾位置。行 cache 原位追加，实际行数和字节进入报告。

第一场不假定满足几何。若不满足，完整 CommonSlackRows Phase I 同时保所有原/幅度工作行。tau 是共松弛算法变量；接受恢复步仍需真实域通过、完整新场全观察网格与所有永久位置重读、最大正 physical g 严格下降。恢复到正残余或预算用完不会被称为真实可行。进入 metric 方向后，每个可接受 trial 都需要原完整 Phi 下降与完整真实几何 / 幅度筛通过。

固定算法幅度预算为 marked Dbar=4.2、Lbar=.9、Hmin=1.01；原同场 R 作为 cap radius。它们是本分支设计约束，初始场是否满足由真实第一次扫描决定。相同 core 数据、节点或固定前三系数不能替代幅度检查。必要数值筛仍不能替代真正 whole-image D/L、embedding、reach 连续证书。

## 5. 历史位置的完整范围

独立准备显式读取已刊 scripts/resume_20261120/a04_historical_location_seeds.json，不能因为它位于 scripts 而误去 computations 找空路径。文件包含11个有序 seed payload，均保留：

| payload | 原位置 / 参数结构 |
|---|---|
| legacy_memory |32 curvature、4 radius 的 legacy indexed列表与容量/计数|
| restore_grid |32/4 indexed列表与2048/1845/7377绑定|
| restore_local |12/2 literal点与容量|
| witness_positive、witness_lowphi |各一个实际字面终点|
| full13_curvature、full13_radius |57/13字面 witness dictionaries|
| r17_grid |32/4 indexed列表|
| r17_local |12/2字面点以及5个 protected点|
| r17_fixed |45/7字面点及65/9原优化角grid位置|
| continue_union |1107/180字面点及18个 protected点|

准备先比较原准确 symbolic node definitions 的 canonical SHA 与原完整 scalar definition 的 canonical SHA，核 J=923、M=160、N=2048、legacy=1845、observed=7377。旧 grid index 才由同观察地址转换成 (cell,u,phi)。r17_fixed 的 diagnostic N=8192 不拿来重解释其明确标注 N=2048 的优化 grid；已经写成 literal phi 的诊断位置保持原浮点字面。

旧容量、插入/移除计数、原顺序、所有源引用和完整 payload 存入 supplied-location-provenance.json，并写实际文件 SHA。新永久集合只精确去重，不以旧32/4或12/2容量删除位置。protected位保留。供新求解器的 union 按明确 canonical tuple 顺序输出；历史原顺序独立保留，未伪称新 selector 复制了旧队列的逐步选择轨迹。

旧 normal-angle 数值 phi 被明说作为新 fixed-chart phi0 数值地址重读；不宣称跨模型同一物理点。旧全部几何值、符号、导数、feasible状态与证书都不继承。

run1/run2 后续新发现的位置若只存在于其 runner 报告，不能从 bundle/report hash 重建，也不能把重算得到的 raw 位置假装成已刊参数。本03首次只声称全部提供的11个 payload 及显式额外 manifest 已纳入。以后拿到真正后续报告可显式追加；新分支每次自己发现的全部点继续永久保存。

## 6. 程序接口与真实运行顺序

六个独立源为 so3_axisymmetric_reference.py、so3_axisymmetric_meridian_operator.py、so3_axisymmetric_meridian_geometry.py、fullclosed_axisymmetric_so3_qp.py、launch_axisymmetric_so3_actions.py、read_axisymmetric_so3_report.py。

prepare 需要 --repo、--warm-bundle、--node-report、--scalar-input、--outdir、--manifest。输出 reference.npz、observations.npz、locations.json、supplied-location-provenance.json、report.json。它本身是实际科学准备，必须在公开 Actions 执行；complete=true 仅表示此准备预算完整返回，不表示新物理场已经读过，更不表示求解完成。

solver 使用上述实际 reference、carrier、原 node/scalar 和准备 report。--manifest 至少包括准备输出的 locations.json；全部hash绑定。首版保持全 N=2048，跨网格 refinement 不能通过静默变 --angles 实现。正常 restart 需 --restart-checkpoint 与 --restart-report 同时给出，并继续同 source/model/target。

first建议完整预算：metric方向1、maxiter16、restoration方向4、restoration maxiter64、mu=.01、全192工作行，line-trials15。此为可实际运行的新完整方向预算，不是缩减变量、稀疏观察或零步 fixture。实际返还的 Pg/tolerance、活动行、J/J*成本、真实 g、trial接受与stop原因决定后继预算。

CPU runtime 使用官方已核命令：
python -m pip install --disable-pip-version-check --no-input torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
来源 https://pytorch.org/get-started/previous-versions/ 。job03可在workflow安装；launcher的--install-torch只在实际公开Actions内执行相同命令。--print-command仅生成argv。

read_axisymmetric_so3_report.py 只读完整来源与报告，不重算F/J。它独立复核新 target definition、reference model、母范数和全部 source roles，分开 actual metric / restoration 方向与真实几何。未知profile身份不能冒历史383168；incomplete报告不能升级complete预算。

## 7. 本次已完成的验证与未完成责任

六源已实际做 Python AST/compile、字面 dict 重键与尾空白检查，没有在本地运行科学场或fixture。完整新 solver 的 optimization while loop 与原9cf源逐 AST相等；新 RotationH2Coordinates 全方法相等；new geometry除init来源/schema guard以外全部方法相等；旋转、core/cap、积分、六jet、residual/J/J*、point VJP主体逐体保留。launcher parser 删去自身print/install两flag后与driver逐AST相同。

这证明来源改接没有悄悄裁剪已有全变量算法，不能证明数值收敛或新场可行。实际新初值、Phase I、完整方向、全部永久点、同场连续证书与固定问题精化仍须由真实Actions返回。设计target只是本轮候选筛值，不能重定义README的原求解精度，也不能用fine零步退出冒充误差持续下降。

本入口的价值是形成一个实际可重建的独立新输入和全空间方向，消除旧非线性重放作为必要依赖；不存在任何已完成闭嵌入连续flex的结论。

## 完整刊载身份

| 完整源 | SHA256 |
|---|---|
| [so3_axisymmetric_reference.py](../scripts/resume_20261126/so3_axisymmetric_reference.py) | `e3fb126b1d72808188f08371cdd522c5bf3d9183e8e31399432dbfc14157de4b` |
| [so3_axisymmetric_meridian_operator.py](../scripts/resume_20261126/so3_axisymmetric_meridian_operator.py) | `7624643d9ee05c1c7f0439050d71e1b8401a60a1b7e75fe63915c03ce24aafbb` |
| [so3_axisymmetric_meridian_geometry.py](../scripts/resume_20261126/so3_axisymmetric_meridian_geometry.py) | `c0aa15ef62a0ad74e34e88ea97a6aad7f69833bf7b11a6b3dd55b13dc4feecaa` |
| [fullclosed_axisymmetric_so3_qp.py](../scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py) | `e95725a541c9e920b28b0532e297c8cca85578474ce7f23e33d90906f263cf34` |
| [launch_axisymmetric_so3_actions.py](../scripts/resume_20261126/launch_axisymmetric_so3_actions.py) | `8d0e88573bf13fb5d35a8bc05b29903b0f80e3712c8293394bbd3c211eadb575` |
| [read_axisymmetric_so3_report.py](../scripts/resume_20261126/read_axisymmetric_so3_report.py) | `0c44ed4962fa6812f91c888d869d50ab089a70438fc933d0fc5589a53a23700c` |

全部源保原始字节。完整三步参数另见 `computations/resume-20261126-axisymmetric-so3-first-steps.json`；控制器只接标量dot-path，因此四项标量误差、历史计数、算子计数及幅度分量逐项取值，不把数组/字典送入紧凑scalar summary。原科学argv/输入/预算不变。
