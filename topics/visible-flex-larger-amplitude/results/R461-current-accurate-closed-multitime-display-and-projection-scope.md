# R461 — 当前准确完整场的多时刻显示与逐顶点投影范围

可信度：**已证明（限本文明确条件下的同图像、点包围与投影命题，以及所列来源组合）；实际当前场显示尚未执行。** 本文不报告未来 accepted450、M 场、网格、运行时间或几何通过值。源码准备仅用了文本、JSON 和字节身份操作，没有本地导入、AST、编译、fixture、benchmark 或科学运算。

作者：OpenAI ChatGPT `/root/amplitude`（AI），2026-11-16。

## 1. 所解决的真实缺口与保留范围

R409、R441、R442 的 shared producer 建立真实当前有限场及完整七元组，但都没有产生当前多时刻显示网格。旧 `exact_20261114_closed_mesh_summary.py` 只认旧 refined-A 来源；旧 mesh 的环、三角索引及 PLY 格式可以作格式依据，不能把旧 loader、旧点样本或旧 `A.phase_jets` 的值重新命名为当前准确场。

尤其，R416 及其 R441/R451 变体以同一准确 C/DAG 的语义系数替换 cut 修正的径向两阶目标。其 `source_bundle` 内的 `A` 仍是原 shared 数值表达的资料对象。调用 `A.numeric`、`A.phase_jets` 或从旧图像数组旋转，并不能实现这个新准确 cut 表达。本源实际调用 `Cut.load_accurate_cut_field`，随后以返回对象的 `current.field.evaluate` 求点；完整帽另调用同族帽源的准确 Cartesian 公式。[R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md)、[R417](R417-current-ten450-fixed-cap-six-jets-curvature-and-normal-balls.md) 已区分这些定义责任。

本次只增加一个独立显示消费者：

`geometry_20261116_current_C_complete_multitime_display.py`，41,002 B，SHA256 `f3211ba9d74cf2be99d47fe56fcbd5526e8143f8a114364ffdc725382c286bf3`。

它不改 BVP、准确 C、十系数、网格/M 源、曲率或 metric/reach/held 消费者。显示完成仅表示指定有限点和两份有界大小的文件完成；显示失败、宽点包围、时间用尽或未访时刻，也不构成原科学问题的拒绝。

## 2. 当前表达及真实来源

记 $j$ 为当前已真实形成的有限场。其上活动半面在原坐标中记为 $K_j(r,q)$；这里 prefix 的 $r$ 是当前数值自然长度坐标，tail 的 $r$ 是实际物理半径。完整的分片、所有原频率、共享节点、原 registration、mean/background、归一化与 cut 定义全部由实际 loader 决定。本显示只选择有限查询坐标，不删改定义中的任何一列、节点或分片。

允许的三个明确来源族如下。

| 当前族 | 准确 cut 源 SHA256 | 同源帽 SHA256 | 实际 shared 家族 |
|---|---|---|---|
| `current112` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` | R409 |
| `resolution112` | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` | `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` | R441；含 R456 的真实当前来源 |
| `completeM` | `747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492` | `21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a` | R442/R451；含 R457 的真实来源注册 |

所有族继续使用完整 `675ab8df…` 六 jet 解释器。新源自己不重构 Fourier FFT、不重新取 BVP 解，不用给定 SHA 冒已删除的 raw。原 shared loader 真实消费自己的 checkpoint、radial、plan、assembly、target 与 background；准确 cut loader 保完整目标及 C 源；帽 binder 保真实 cuff、全 marker 及实际 Python 模块所有者。现有同源检查全部保留，显示不新增科学阈值。

在当前场定义中，首节点反射不是由显示采样猜测。`Shared.load_shared_bundle` 调用其 `normalize_inlet`，沿原 R249 规则把首节点所有 $z$ 的 0/2 阶与所有 $R,T$ 的 1 阶置准确零块，保其余节点及 cut 两 jet，并记录 `exact_real_shared_node_inlet_reflection_C2=True`。675 解释器读取这份共享 Hermite normal form。因此本源使用一条共享 equator 环，不再做额外的 hull 焊接或零残差验收。该几何定义投影相对原 BVP 的误差，并未由显示支付。

## 3. 准确材料逆、两个显示参数模式

令当前完整 core 给出准确实有限材料 lift

$$
\Theta_j(q)=2\pi q+
\sum_{m=1}^{M_j}\frac{(1-4m^2)c_{j,m}}{2m}\sin(4\pi m q).
$$

原完整 loader 的严格正材料密度下界为 $\rho_j\ge\beta_j>0$，故

$$
\Theta_j'(q)=2\pi\rho_j(2\pi q)>0,
\qquad
\Theta_j(q+1)=\Theta_j(q)+2\pi.
$$

由严格单调、无穷端点和周期 lift 关系，存在唯一准确实逆 $I_j:\mathbb R\to\mathbb R$，且 $I_j(\eta+2\pi)=I_j(\eta)+1$。这个逆是定义中的函数；有限 interval Newton 仅给它的包含区间，不把某个 midpoint 或一次有限迭代定义成准确逆。[R443](R443-common-material-angle-pullback-and-fixed-closed-target.md) 与 R447/R457 保留了这个区别。

写 $\alpha=\pi t/2$。共同物理角表示为

$$
\Gamma_j(r,\eta,t)=R_\alpha
 K_j\bigl(r,I_j(\eta-\alpha)\bigr).
$$

### 3.1 默认 `physical-angle-image`

本模式的网格角点是 $\eta_k=2\pi k/N$。每个固定 $t$，$\eta\mapsto I_j(\eta-\alpha)$ 是圆的双射，所以完整参数圆的图像等于当前物理相位场的图像。

若另有真实首材料 lift $\Theta_0$，其固定首 $q$ 表达为

$$
F_{j,t}(r,q)=\Gamma_j(r,\Theta_0(q),t).
$$

由于 $\Theta_0$ 也给圆的双射，两式在每个 $t$ 的完整活动图像相同。**它们的有限顶点对应通常不同。** 默认 $k/N$ 不是固定首材料 $q=k/N$；本源不据默认网格比较冒出固定首点随时间运动的结论，也不把顶点云距离当全像距离。

### 3.2 可选 `first-material`

此模式必须实际消费 R457 `bind_loaded_common_material` 所要求的完整 B、first plan、first assembly，并由其真实 R437 或 R452 第一记录及当前完整目标检查建立来源。R452 模式还核原 A/B 配对。随后用 $\eta_k=\Theta_0(k/N)$。不伪造丢失 B，不由 construction 标签或一个 hash 恢复材料定义。

默认模式不要求 B；B 缺失不阻原几何，也不阻明确请求的默认图像显示。选择 first-material 却不给真实 B 时，该显示模式仍未建立。两种模式都使用当前完整材料系数和原严格正下界，不减少 M，不替换为首 core。

## 4. 帽、反射及接缝

对 side $\sigma\in\{+1,-1\}$，帽必须沿已冻结的 R409/R417 定义：

$$
F_\sigma(x,y)=\bigl(x,y,\sigma(H+b_\sigma(x,y))\bigr),
\quad
b_\sigma=\sum_{\ell\text{ 属于该侧}}A_\ell
\left(1-\frac{(x-x_\ell)^2+(y-y_\ell)^2}{R_\ell^2}\right)_+^4.
$$

每个实际 marker 都参与求和，包括重叠、负振幅和支撑边界。source 不调用旧帽 binder，不用旧 `index/kappa` 模式代替当前四字段 marker。帽在相位下保持 Cartesian 固定；不把整个闭面作刚转，也不因活动材料图的性质假定非对称帽旋转不变。

在 cuff，原同源准确表达为

$$
K_j(r_\mathrm{cuff},q)=
\bigl(r_\mathrm{cuff}\cos\Theta_j(q),
r_\mathrm{cuff}\sin\Theta_j(q),H\bigr).
$$

将 $q=I_j(\eta-\alpha)$ 代入再旋转，得到 $(r_\mathrm{cuff}\cos\eta,r_\mathrm{cuff}\sin\eta,H)$，恰为同源帽的外边界；下侧由完整反射给出。source 因而在共享 cuff 环使用帽公式，在 common cut 使用 prefix endpoint 的相同 0-jet。所有 accurate cut 两 jet 与归一化责任仍留在原表达中，没有用显示面片证明它们。

下活动面为准确上活动表达的 $z$ 反射。本源复用一次上面点包围，按 $[z_-,z_+]\mapsto[-z_+,-z_-]$ 得到下面；这只是完全相同表达的反射。两帽仍各自使用各侧完整 marker，不从上帽镜像冒下帽。

## 5. 点求值实际包围

对每个实际时间与角点，R457 `MaterialAngle.inverse_enclosure` 首先给完整实 lift 逆的区间 $Q_{t,k}$，包括原材料全频率和严格正全局导数界。有限包含收缩的任何已完成结果仍是包含区间；没有宽度通过门。source 在全部径向点之间共享同一个已得 $Q_{t,k}$，不更换它的含义。

随后 `current.field.evaluate(piece,(r,r),Q_{t,k},False)` 给实际准确分片的六 jet；显示只取其 0-jet，再使用包含 $\alpha$ 的 Arb sin/cos 旋转。这里有意调用 `field.evaluate`，因为便利 wrapper `current.evaluate` 将输入 $q$ 限于 $[0,1]$；取模截断一个跨周期的区间会丢掉完整 lift。源不作这种截断。

帽角点使用包含 $r\cos\eta,r\sin\eta$ 的 Cartesian 矩形，再调用同源 `graph_six_jets` 与 `geometric_six_jets`。矩形可能伸出准确圆点所在的盘边，然而正部四次公式在整个 Cartesian 平面有效，所得值仍包围该准确盘点；这不构成一个新的帽全域 cover。

因此，在现有原 source/interval 实现的条件下，对每个显示顶点地址 $v$ 和坐标 $a$，实际返回一个准确有理闭区间

$$
x_{v,a}\in[\ell_{v,a},u_{v,a}].
$$

所有 C 语义叶、有限 source 系数、三角函数、逆的包含及相关计算舍入均通过原外包解释器进入这个点区间。若当前 C 记录包围一个完整许可根族，本命题按该源原来的统一范围解释；没有从区间中另挑一个新的 C 成员。

这只是**所声明有限表达的点包围**。它不是 native 轨迹误差、BVP 离散误差、归一化修正误差、无限频率尾误差或与目标度量之间的误差。

## 6. 最终 binary64 投影与逐顶点半径

对每个坐标，令

$$
m=(\ell+u)/2,
\qquad d=\operatorname{float64}(m),
\qquad \widehat d=\mathbb Q(d).
$$

这里只把最终显示坐标投影；$m$ 不回写到 C、cut、场系数、材料逆或任意 parent 状态。计算三个准确非负数

$$
e_\mathrm{eval}=(u-\ell)/2,
\quad e_\mathrm{proj}=|\widehat d-m|,
\quad e_\mathrm{point}=\max(|\widehat d-\ell|,|\widehat d-u|).
$$

有 $e_\mathrm{point}=e_\mathrm{eval}+e_\mathrm{proj}$。source 将 $e_\mathrm{point}$ 转为有限 binary64 半径 $\varepsilon$，然后用 `Fraction.from_float` 检查 $\mathbb Q(\varepsilon)\ge e_\mathrm{point}$；若初转偏小，向 $+\infty$ 移一个相邻词并重新准确检查。仍不能有限包围时如实报错，不截尾或输出 NaN/Inf。

于是每个存储顶点满足逐坐标不等式

$$
|x_{v,a}-\mathbb Q(d_{v,a})|\le\mathbb Q(\varepsilon_{v,a}).
$$

PLY 每个 vertex 直接保留 `x,y,z,error_x,error_y,error_z` 六个 little-endian binary64 词及一个 piece byte。因此不需把逐点原区间大表送进工具，也能从实际 PLY 恢复每个显示点的准确外包盒 $\mathbb Q(d_a)\pm\mathbb Q(\varepsilon_a)$。上溢会真实停止；次正规或下溢到零仍由准确有理比较及 `nextafter` 覆盖，不用一个任意误差容限把它通过。

单份必要摘要逐帧保每坐标的 $e_\mathrm{eval}$、$e_\mathrm{proj}$、$e_\mathrm{point}$ 实际最大值的 outward binary64 表示、完整 little-endian 词、达到最大值的显示地址，以及实际存入 PLY 的最大半径。原精确最大值表只给 canonical 身份；逐顶点半径留在本次 Actions 文件。摘要明确原未刊原表的范围，不能以 maxima 冒逐点正文已由根代理阅读。

点误差不控制任意三角面内插值：即使三个顶点误差很小，也不能由此推出面内 Hausdorff 距离、法向误差、$C^2$ 误差或嵌入。本源没有这种声明，也没有把半径大小变成 BVP 或几何的接受门。

## 7. 有限网格、文件容量与未访

默认显示时刻是准确有理词 $0,1/2,1$；默认 prefix/tail/cap 区间数分别为 8/8/4，角向点数为 32。这是小显示工作量选择，不是误差估计、采样证书或未来运行记录。实际调用可显式覆盖，并同时给独立显示预算、shutdown reserve、free-space reserve 和 interval/inverse-work 参数。

prefix 径向点覆盖其两端；tail 的显示点另纳入原 inner、cut-start、cut、cuff 这些明确边界。cut 点用 prefix endpoint 一份，cuff 用帽一份。每个其余实际径向点按完整原分片表选择真实包含它的闭片。所有未采样原分片仍保留在定义及其身份中，显示不声称遍历完整径向 cover。

环按旧格式形成两个反射半面与固定帽，另加两帽极点。若上半环数为 $U$、角点数 $N$，则 $R=2U-1$、$V=RN+2$、$F=2RN$。这些是文件结构的准确计数，未作为非退化、嵌入或接受条件。源不做新的面积/拓扑数值验收。

每个 vertex 为 49 B，每个三角 face 为 13 B，header 有明确保守界。申请数组前先按有限环数上界检查容量；实际写文件前再按真实 header 和计数检查，要求 uncompressed **严格小于 5,000,000 B**。gzip 的 sink 在越界块写入**之前**拒绝，使失败时的 partial 文件也不越过同一上限。压缩固定 `mtime=0`，不是压缩科学表送工具的协议。

每个真实尝试的 frame 保三类进度：angle inclusions、upper-ring-major 的上下点对、两 pole；另保实际文件写阶段。中断时当前未提交地址范围和全部未起时间后缀都保留；不把刚计算过但未完成文件的帧标为完成。若在 frame 建立与统计对象建立之间收到实际信号，统计明确为 null 且 `vertex_error_statistics_initialized=false`，不会因缺对象而丢失必要结果。已完成帧的源、时间、vertices/faces、两文件 size/SHA、误差范围全部返回。

## 8. 同 job、原钟、必要读回与清理

源只认真实 original193、joint203 或 actual202205 launcher/source/deadline tuple。它逐原 `origin.actual_job_deadline` receipt 比较实际 deadline 的 bytes/SHA，并核本 run/SHA、原 recipe SHA、18,900 s science 与 2,700 s readback reserve。组件的显式 display 秒数只是原剩余 science 内的更小工作限制；不重启总钟、不延长 upstream 预算。

当前 shared result、原 checkpoint 及全部七元组文件都必须实际存在并处于同一 owned namespace，原 loader 的接受及来源责任照常执行。输出仅可在 `RUNNER_TEMP` 内新建独立兄弟目录。它不启动子进程、不编辑 parent、不删除 raw；不凭一项 `completed` 推断整个上游进程树已静止。

所有实际算术只能在本公开库 Actions 中发生。SIGTERM/SIGINT、资源停止、真实异常分别记录。source 恢复进入前的 Arb precision，写必要范围，再由真正 host 等进程退出、完成必要读回并确认 owner quiet 后清理。显示工作本身不承担或伪造 host 的 quiet 证明。

必要输出为一份 ASCII JSON，硬上限 90,000 B；完整 failures/partial/未访属于所选范围。若实际超限，明确返回协议 70 及原 result/尝试 size/SHA，保临时文件，不截字段、不换编码、不分包避限。正常科学资源 partial 返回 124，普通异常 2，有限显示完成 0；三者都不表示全数学任务成功。

源输入格式或路径错误若发生在建立 fresh `Display` 对象之前，属于原 host 的完整 stderr/异常读回责任，不伪造一个已建立 result 或 necessary marker。原 host 仍须按真实 scope 决定清理。

## 9. 完成标准中仍未支付的部分

本源没有实际 parent，也没有一个生成好的网格。未来一次成功显示仍只支付有限显示及其点投影包围。以下范围继续独立：

- 准确场与目标的全域 metric、reach、held、刚性及所有原接受门；
- 连续全 $t$ 强 $C^2$ 控制或相位比较的实际完整量；有限三个时间不代替它；
- 当前有限 node/Hermite/FFT 场相对真实连续/native 解的误差及归一化修正误差；
- 三角面内、法向、全像和网格拓扑的几何误差；
- future refinement 后完整 fixed construction 与真实第一材料来源的运输责任。

因此 R458 首版不必等待此显示源；未来若接入，也只在相同实际 raw 生命周期内消费已经真实形成的当前场，不增 metric/reach/held 成功前门。

## 10. 逐来源引用与准备记录

核心来源为 [R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md)、[R417](R417-current-ten450-fixed-cap-six-jets-curvature-and-normal-balls.md)、[R443](R443-common-material-angle-pullback-and-fixed-closed-target.md)、[R457](R457-actual202-complete-M-source-and-first-material-registration.md) 及其各实际 source。旧环/PLY 的格式来源是 `geometric-closed-assembly.py`；没有执行其 loader、`main` 或旧字段判断。R409/R441/R442 当前表达、R413 cuff attachment、R400/对应新 checkpoint 的原接受门均由真实调用保留。

本文及源码只作文本/纸证工作。未运行显示、未执行 scientific import、未解析 AST、未编译，也没有添加独立 fixture、数值对拍、benchmark 或审核前门。源码的可信度与未来真实运行的必要读回分别负责，不能互相替代。
