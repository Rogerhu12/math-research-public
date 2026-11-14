# 交接：可见且有厚度的闭曲面等距弯曲

会话：Astra-visible-flex-4ffd372b；2026-11-09 接手。QUEUE认领提交7acd82077457a23caed9e982cc547c5087da6d2d。前会话Astra-visible-flex-effcccee的已审结果全部保留。

**尚无满足完成标准的解；状态保持进行中。** 已重读作者2026-11-09新版README（blob099f451b142e184c223d2d0764887d99bd492db5）：存在固定握持闭集H，内部非空且diam F0(H)≥0.2D；不作刚体对齐的δ_hold/D≥0.05，并须严格或带误差确认δ_E>0。全时reach/D≥0.03、同一g的相对误差≤1e-6、同一度量/参数/t范围下加密趋求解精度仍须全部满足。δ_hold/D≥0.2、δ_E/D≥0.05和严格存在证明为更强目标。

## 本轮接手核查与分工

- 已重新读根README、本题2026-11-09新版README、HANDOFF/open。当前文献复核仍只支持已核来源的范围：Ghomi2019 Problem1.1、Payne2023 cylinder talk不能提供定量闭嵌入族；不把搜不到当全球不可能。详notes/2026-11-09-resumption-and-literature.md。
- 最新邻题large-amplitude的R37/M20仍有曲率约95的尾部，不能直接满足本题reach/D≥.03；explicit已推进至R42但仍未闭。swarm的R520为非定量输入，不提供本题所需比例。
- fixed_metric_bvp负责冻结度量、非线性tail与加密；closing_geometry负责真正封口与全时reach；independent_audit保持未参与构造者身份，核查和独立重跑；root负责其他构造研究、HANDOFF及推送。旧工作区可只读复用，依赖先核SHA。

## 最新主线：椭圆柱＋固定两帽

- 中央精确同周长椭圆柱core，两个反射的非线性Frenet过渡prefix，圆形端口接固定帽。两帽可自然提供握持H；微小不对称标记只需证明δ_E>0，基础目标不再要求宏观帽锚定。
- 条件距离证书：core在|z|≤ell，初态|y|≤r且含(R,0,0)，其余初始曲面均在|z|≥ell；相位π/2时点(0,R,0)到初始整面距离≥min(R-r,ell)。若全形落在半径Rband、高度半范围Hprefix+ell圆柱，则D≤2sqrt(Rband²+(Hprefix+ell)²)。aspect约1.3、ell=.26的当前条件预算δ_hold/D约.0525。尚非已闭合曲面，R3在写，待独审。
- 低曲率profile参数vu=.35、vd=.5、ramp=.4、rCut=.6、wCut=.5；线性平面mode2稳定线rho=0的delta约.1914625166。非线性同周长ellipse BVP已从aspect1.02延拓至1.2。M4→8→12实际全角度metric_l1约2.255e-4→2.876e-6→3.59e-8；M12 flow defect约5.44e-8，prefix高度约1.883，采样kappa约4.237，未加中央柱/封帽的kappaD约19.04。
- 上述各M仍调整profile delta，故**还不是固定metric加密证据**；有限线性Robin端口也不是圆领或精确无限tail。下一步固定最终a(s)全部参数，将同周长core轴比改为BVP未知，只允许extrinsic embedding修正；中央柱长和相位范围也冻结。正核验轴比1.3和完整非线性tail。
- 独审audit_phase_bound已从头复现aspect1.02→1.05，并继续核实际C²导数、边界参数Jac和固定metric问题。大轴比M8 aspect1.5虽collocation收敛但实际metric约.00809，1.7域失败，均不采用。

## 本轮条件几何预算（R3–R4已独审采用）

- notes/2026-11-09-centred-diameter-candidate.md 的§§1–3已为R3，证明中心对称紧集D=2max|x|，用于半转/上下反射prefix，避免把最大半径和最高点硬合成圆柱角点；保留所有闭合条件。
- 旧M8轴比1.3、ell=.26采样：球包络D_prefix≈4.46855（旧圆柱4.95283），支持差R−r≈.260991；原rho≤.6预算已独审纠正：该前缀实际末半径.6008466；应至少用rho≤.601、高度≤sqrt(2.6²−.601²)。仍须严格证R−r≥.26与整个尾包含。现prefix最高z≈2.14170，尾新增高度预算约.38812。均非严格数值界，未闭合，未付reach。脚本scripts/root_phase_envelope.py与小JSON已写。

- 新条件工具notes/2026-11-09-marker-reach-candidate.md：若基准reach≥ρ，环境位移满足||Du||≤η<1、||D²u||≤L，则新reach≥(1−η)²ρ/(1+η+Lρ)。轴对称未标记帽使全phase基准图全等；四个正则性不同、仿射独立的固定小标记可严格排除E(3)，再用紧性得δ_E>0。完整条件证明已为R4，独审PASS；尚未付基准闭图/全局reach。

## 新实际尾部探索（不是闭族）

- scripts/root_cut_preserving_tail.mjs改造有限浅尾：cell0末transition从低cap回到raw，保cut slope/second和深背景；重算径向warp，不继承旧DN。rCut=.6,wCut=.5,width=.35,K6,cap=.02/.05的背景采样κ<6，高度.02163/.02913；cap=.1宽度不足。原buffer粗界9.909，尚无连续曲率证书。
- cap=.02的真实有限profile线性DN初算m2斜率5.676917（s512/far32）；线性Hθθ正性端口height阈值约4.11e−6，旧前缀末height约.0037，不能直接拼。低cap/warp破坏浅cell的模式同步，需要新匹配/校准；不是一般不可能性。数据root_cut_tail_*，独审另核。
- 独审确认新非线性DN必须含均值：旧M12平均z_s修正1.5983e−4，忽略会留一阶缝。反向段输入DN(sigma*H)，sign须在非线性函数内部。详audit-tail-interface与audit_port_trace.py。

## 已证明的中间结果

- R3 中心对称直径/握持距离条件证书；R4 全相位reach与固定小标记工具，均独审PASS。不能代替真实闭图。
- R1（results/R1-phase-quotient-and-narrow-cap-bound.md）经未参与者独审PASS。它全文的旧符号delta专指新版delta_E：wide-m2整带同轴旋转，配准后变化只在窄帽，delta_E/D<2.7325581396e-5；任意加高同一窄帽模板仍有(delta_E/D)(reach_min/D)≤1/3200。**此结果不排除新版基础目标**，仅限制该模板的更强delta_E目标。精确输入按binary64，D下界约1.72但不能把十进制1.72当精确下界。
- R2双模块直径条件证书和内部滚动球必要条件已独审/复核。旧.98圆柱直径witness与reach≥.03D联合不可能；.97/.96未被该必要条件排除。它也是delta_E强目标的储备路线，没有已实现模块。

## 已核查的仓库和文献

- 已读根README、QUEUE、本题及相关课题源文件。continuous-flexibility-swarm/HANDOFF声明R520完成非定量存在性目标；不能直接代替本题定量实例和独审。当前邻题closed wide-m2有精确局部机制，但旧完整tail具有构造残差底，且旧曲率采样约94.69；不能作为本题合格解。
- 文献核查见notes/2026-11-08-literature-mechanisms.md及repo-amplitude-review。Ghomi2019 Problem1.1、Payne2023官方讲座摘要均未提供本题闭嵌入定量族；Anderson arXiv0709.3202撤稿，不能作rigidity定理。Bobenko等2025紧Bonnet对只给两个等距浸入环面，非连续同metric闭嵌入族。以上是所核来源结论，不宣称截至今日全球不存在新结果。
- explicit-flexible-closed-surface现有R1–R36仍为带边/端口片；R34并非四个全圆柱端口。固定净格Goursat/T/Monge与纯负曲率ruled片闭合有具体障碍，保留在文献笔记；不作为本题收尾。

## 其他计算、文件和审核

- scripts/explore_direct_rotational_band.py六轮三分量坐标求解全未合格：最小metric缺陷.005662，采样kappa16.16。独审完整复现小例、核Jac/实际Cartesian一二阶导数PASS；确认target平均E也在变化，Hessian惩罚不等于reach。见direct-coordinate-search及independent-direct-band-review。
- scripts/explore_closed_sphere_metric.py的全局解析多项式闭球面搜索误差.16849，未合格。新版固定开握持区与非平凡全局解析映射由解析延拓不相容，暂停此参数化；保留脚本和失败checkpoint，不继续盲加阶。
- notes/repo_scan_ellipse_*存非线性搜索及小摘要，raw压缩.gz；geometry脚本含严格有理预算。旧宏观非圆帽/双模块预算保留供更强目标，不再阻挡基础路线。
- 上轮代理角色仅保留于旧报告；本轮角色见开头，所有新结论及时写回本文件。

## 接手必须继续的关口

1. 在冻结a(s)、core长度、phase范围下得到真正收敛的完整prefix＋非线性tail＋圆领＋两帽，排除固有taper残差。
2. 核C²接缝、连通闭M、全时embedding；可用phase旋转使band内几何不依t，但band与固定帽的全局距离仍须覆盖全部t。
3. 将中央距离条件和固定H尺寸实现在完整像上；用不对称C²标记及紧性严格证明δ_E>0。
4. reach同时证明曲率与全局法向瓶颈，不能只报1/kappa。完整误差及加密证据经未参与者独立重跑；通过后才输出<5MB的各t网格。

普通HTTPS git缺终端认证，使用已连接GitHub API以最新main为父节点原子提交、expected_sha租约和非强推；只写本题及根LOG追加。所有障碍与局部解都只是中间进展，不标完成。

