# 真实58：保留已付可行环的原102系数body恢复模块合同

2026-11-16。本文及所附新模块只作源码文本与纸面推导；没有在本地导入、编译、运行科学程序或测试，没有重放任何已闭优化。唯一后续执行由独立公开Actions请求指定。本合同是一个新增body问题，不是free36的继续计费或换初点重解。

## 1. 已付结果决定的新问题

唯一祖先观察见[free R1/R2完整实际记录](true58-free-R1-R2-ring-success-wholebody-failure-20261116.md)：run `43884276617`，research `133358065602`，source `7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c`。一次SLSQP返回status0/success，11次完整新评价，把固定峰环的共同曲率上界降至约 $1000/61$；原环门和原172盒通过。这个向量尚未实际接受。

同一向量的唯一全body预测却给出约 $6.9794$ 的metric偏差，峰在原径向111即 $.585$；曲率约 $69803.9$，峰在径向131即 $.7125$。它没有进入actual。原接受点仍为58。该已闭任务的全域预测数组没有导出，本任务不能把其metadata冒作可恢复的免费输入。

新任务保留该**实际once-rounded环候选**的末51个原切向系数，释放原前六径向样条的102个系数，直接恢复整个body的metric与曲率门。依据是[R514第11节](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)，并非数值上看起来影响较小。

独立新policy为 `true58-fixed-ring-prefix102-body-repair-v1`，原stdout前缀为 `TRUE58_PREFIX102_`。祖先最终科学费用 **2974.589423877秒、147次原full值**原样封存；新600秒从本次imports及必要输入读取之前起，全部新输入、求值、Jac、求解、失败、序列化与输出均计入。

## 2. 原102纤维与不动的后缀

令 $q_A$ 为真正接受的58，$q_R$ 为free36实际保存的、已过原盒但未接受的binary64环候选。二者角色不交换。记 $F$ 为原168坐标中的以下单位列：

$$
I_F=\{0,\ldots,53\}\cup\{81,\ldots,128\}.
$$

它们分别是原 $u$ 的前六径向块、每块九角模式，以及原 $v$ 的前六径向块、每块八角模式。候选族为

$$
q(z)=q_R+Fz,\qquad z\in\mathbb R^{102}.
\tag{1}
$$

原五次样条完整结点向量和原entry权保持不变。B3至B8的支持右端依次为 $.36,.441,.522,.603,.684,.765$；这直接来自[原 `rational_knots`](../scripts/frame_collar_enriched.py) 的端点 $.036,.846$、九个等距内部结点以及 `supp B_i=[t_i,t_{i+6}]`。在 $s\ge153/200$，这些函数及必要一、二空间jets为零。因此，同一完整场在该后缀上的位置、一二jets、第一形式、法向和形算子都不随 $z$ 改变。高度、单Q及新增九列均固定，不存在一个被忽略的高度center前缀项。

这个结构同时给出限制：$.7125$处前缀只有B8仍可动；$.585$处只有B6、B7、B8仍可动。102个全域参数不是这些点上的任意二jets。新任务保全部真实耦合，不用逐点独立曲率修正替代它们。

实际候选仅对 $I_F$ 中的坐标作一次准确加法后转回binary64，其他66个168坐标逐位复制 $q_R$。因此，这里的后缀不变性不再依赖把一次新浮点R0/R1/R2消元舍入为零；它来自字面不改末51/Q/height/new9及原前缀基的零延拓。新浮点frame、FFT与ordinary之间仍只宣称相同数学定义，不宣称所有不同求值路径逐位相同。

## 3. 先支付固定后缀，失败即0solver

当前完整候选两网的scalar frame、固定 $a,a_s,a_{ss}$、高度 $b,b_s$及完整角原函数均须新支付。既有失败预测只保metadata，不能重标为paid数组。初次新全域值形成后，直接选择同一数组中 $s\ge153/200$ 的真实原径向行，不再重求几何。

后缀必须满足：

- metric真偏差不超过下节的严格新预算；
- 原四个scaled curvature PSD行不低于原容差；
- 独立直接曲率不超过原58上限及原直接容差；
- 原regular normal area严格大于原数值下界。

任一失败，模块返回 `fixed-suffix-excludes-this-numerical-fiber`，不调用SLSQP，不生成伪候选。数学上若某不动后缀点真违反约束，整个纤维都不能修复它；实际binary64读数只给本次数值模型的明确排除，不冒有向连续证书。后缀完整新数组、实际失败门和全部已付费用仍保存。

这一步不是只检查 $.78$。成功环只占后缀中的一圈；其它固定圈若失败，也不能被102个前缀列改变。只有后缀通过才开始新的body恢复会话。

## 4. 原盒、完整非线性值与固定有限约束

### 4.1 原物理盒

前102列在原172物理坐标中也是相同的单位列。对每个 $i\in I_F$，精确剩余区间为

$$
\ell_i-q_{R,i}\le z_i\le u_i-q_{R,i}.
\tag{2}
$$

其余物理坐标取 $q_R$ 的原精确值，不能拆开旧五height的准确映射。给backend的区间端点向内取相应binary64值；零宽区间原样保留。没有新小trust、旧159 defect guard或旧 $h\le1/128$ 的移用。最终另外输出相对真正58的完整172物理增量及 $4\|\Delta\|_\infty$，仅作实际幅度记录，不把它解释成已付全body保证。

### 4.2 新全域值

每个真正新坐标都直接调用原 `field.scalar_frame`，以完整 $\theta+u$ 和 $c(v)=(1+v^2)^{-1/2}$ 得到 $T,T_s,T_{ss},T_\theta$。完整角算子仍为原 `periodic_operator(...,-1)`。记其三个结果为 $P,P_s,P_{ss}$，则

$$
\begin{aligned}
U&=a_sP+aP_s+b e_3,\\
X_\theta&=aT,\\
X_{ss}&=a_{ss}P+2a_sP_s+aP_{ss}+b_s e_3,\\
X_{s\theta}&=a_sT+aT_s,\qquad X_{\theta\theta}=aT_\theta.
\end{aligned}
\tag{3}
$$

不调用ordinary，不重建 $X$或center，不把缺失的 $a_{ss},b_s$补零。固定metric必须以完整 `bind_current_168_curvature_metric` 对象传入；该绑定本身不免除外层取得这些数组的实际成本。

令

$$
e=U\cdot U-1,\quad f=U\cdot T,\quad
\eta=\frac{|e|+\sqrt{e^2+4f^2}}2.
\tag{4}
$$

`metric_budget`必须是调用者只减一次得到的

$$
\eta_{58}-10^{-7},\qquad \eta_{58}=.26600541463999305.
\tag{5}
$$

模块内不再减第二次。原actual最后仍以其自己的原下降比较为准，不能把阈值浮点减法当严格连续证书。

有限metric行使用原smooth spectral两支及原epsilon；曲率使用原 `curvature_values` 的真实 $I,II,G$、法向面积和四行，再乘原 `cap/scale` 与其平方。独立主曲率仍沿原 `independent_principal_curvatures`。没有 $G=1$替代、原metric的一阶化、或新的曲率上限放宽。

### 4.3 固定有限行与全域验收的区别

有限优化行固定为：当前两池中groups0、1、7、8、9、10的不同原row IDs，保原池第一次出现的顺序；再加入径向111、131上两网全部theta的这六组原行。已有行只判重，不重新解释同tag。原其它group并未宣称不变；它们仍由合格后完整actual的原14门判断。

每个新点同时计算所有原radial、所有原theta的两网值，因此初步有限问题并不是把已知两坏点误称全body覆盖。有限行只决定本次backend的约束矩阵；原全两网值门决定是否可以进入actual。若返回点在池外任何位置失败，本会话即无资格候选，不为这一个结果自动追加行、换初点或重启。

## 5. 一次phase-I会话与有限内存的解析Jac

将固定有限行写成 $g_i(z)$。初次已付解析Jac后固定

$$
s_i=\max\{1,|g_i(0)|,\|Dg_i(0)\|_\infty\}>0.
$$

唯一新优化是

$$
\min t,\qquad t\ge0,\quad
g_i(z)/s_i+t\ge0,\quad z\text{ 满足(2)}.
\tag{6}
$$

初点为 $z=0$，$t$取已付初值所需的最大normalized violation并向上一个binary64值。这个松弛是明示的可行性恢复变量；$t$小不免除任何最终原门。它与已闭的环minimax、fixedK19或射线LP都不是同一实例。

参数Jac只在SLSQP真正请求该点Jac时支付。每批最多四个原径向行，仍在每条原完整theta圈上调用 `angular_kernels`；选取真实原点后，`virtual_selected_jets`给三种径向jet方向。再按

$$
Dg=L_0R+L_1R'+L_2R''
\tag{7}
$$

展开到u54、v48。metric导数用原 `spectral_parameter_rows`，curvature导数用原 `curvature_parameter_jacobian`。新9、height、单Q及末51不生成零占位导数张量。源函数范围见[原径向因子化](../scripts/frame_selected_row_radial_jacobian.py)、[原current168入口](../scripts/frame_complete_body_extension168_joint_selected.py)及[原curvature数组接口](../scripts/frame_curvature_psd.py)。

不构造全grid乘102的position-J张量。每个已付点缓存真实selected unique points的五位置jets、T及原curvature输入与summary；完整全域场仅保初输入及最近点。若一个较早点首次请求Jac，使用同q的原 `grid.fields`恢复必要小径向上下文，仅组Tpart/Ts_value_part，作为该次新Jac工作；不重ordinary、U/T或全域值。相同actual binary64坐标的value及已算Jac都不再支付一次科学计算。

解析Jac是原连续场在当前binary64坐标上的导数，不被称为离散rounding算子的导数。实际候选逐坐标为 `float(Fraction(q_R[i])+Fraction(z_i))`，全域summary所绑定的正是这个同一实际168。最终必须逐字相同才有资格；缺少该返回点原summary时直接无资格，不为报告补算。

## 6. 唯一额度与状态

新统一600秒包含imports、三份必要源日志读取、field恢复、固定metric、全部新准备、失败及最后大stdout输出。独立solver180秒包含它的新import、初Jac、所有callbacks与保存；底层调用不抢占，真实超时及实际费用都如实列，不称严格后端wall保证。

| 项目 | 本次上限或口径 |
|---|---|
| 新body输入准备 | 一次；原height导数一次、每网scalar frame一次、每网三个完整Pi |
| 固定suffix核对 | 一次，仅读上述真实新数组，不重geometry |
| 新solver会话 | 至多一次SLSQP，无重启 |
| 原始backend向量 | 103：102原物理增量及phase-I slack |
| SLSQP | maxiter120、ftol1e-9、dispFalse |
| 真正新两网value点 | 至多240，包含build已付初点；缓存命中不冒新点 |
| 解析selected-J | 仅实际请求时计started/completed/failed；不声称240点都付了J |
| 径向Jac批宽 | 4 |
| actual | 全域资格后至多一pair、两次原ordinary完整值 |
| 旧科学调用 | 旧64、32及全部已闭LP/NLP/开发集均0次 |

外层debit接口为 `prefix102_model_builds`包整个build；build内 `charge_prepare(metadata)`对应一次 `new_body_input_preparations`，`charge_suffix(metadata)`对应一次 `fixed_suffix_checks`；solve内 `charge_solve(metadata)`对应至多一次 `prefix102_solver_sessions`。这些回执不另设时间。内部组件事件保真实elapsed与失败；原angular-kernel helper成功包含三次Pi，若其内部异常未回，则只保存实际helper异常/elapsed与当时真实返回范围，不臆造三个Pi均完成。

SLSQP的原status、success、message、raw103、全部OptimizeResult实际字段先保存，再作任何资格筛选。其QP近似乘子不标成严格非线性证书。只有status0/success的真实返回可作为solver候选；另允许build的原初点若已完整通过全域门则0solver进入actual。任意未返回的中间callback点不能被冒成backend成功。

最终还要求phase-I slack及scaled finite残差过明确数值阈值、同一actual168的两网全域metric/PSD/directκ/area过门、unrounded与rounded原172盒均准确通过。通过只意味着可交外层原14门与原严格下降actual，不意味着已接受，更不意味着主reach已付。

## 7. 稳定源码接口

模块为[frame_metric_current168_fixed_ring_prefix102.py](../scripts/frame_metric_current168_fixed_ring_prefix102.py)。

```python
build_fixed_ring_prefix102_model(
    field, accepted_state168, ring_candidate168, radial, thetas,
    fixed_metric, cfg, lower172, upper172, source_receipt, wall,
    capture=None, *, metric_budget, original_pools,
    charge_prepare, charge_suffix)
```

`thetas`及`original_pools`均为coarse/fine字典；fixed_metric是完整bound而非其data子对象。source_receipt由wrapper认证实际58 CACHE2/COMPLETE/FINAL、原55constructor COMPLETE及free36 RING_SOLUTION/COMPLETE/FINAL。本模块不读旧ring/ray MODEL、不重三jet恒等或125生成器；旧成功环只消费原真实候选及source身份。

返回model具 `status`、`binding`、`binding_sha256`、`summary()`及`full_record()`。完整MODEL保存公开build_receipt，故suffix失败也不丢frame/Pi/准备费用。

```python
solve_fixed_ring_prefix102_once(
    model, *, wall, charge_solve, emit=None, capture=None,
    solver_time_limit_seconds=180, maxiter=120,
    max_evaluations=240)
```

返回 `qualified_candidate/qualified/candidate168/candidate/candidate_record/report/status`。原返回tag为 `NONLINEAR_RESULT`；独立 `SOLVE_TRACE`由wrapper调用 `fixed_ring_prefix102_capture_record(capture, include_arrays=True)`输出。回调字典是费用回执，不授新数学调用。

## 8. 原stdout保存范围与失败

MODEL一次保存：完整当前scalar u/v四jets、固定metric/height、原径向与角基、精确盒及来源、固定有限row IDs、固定suffix全二jets和原门数组。它不重复全域frame/Pi/I/II的可还原副本。成功构造后若suffix失败，仍保存上述实际支付输入，0solver退出。

SOLVE_TRACE保：每个真实新point的raw102/actual168/fullgrid extrema和费用；所有真实raw103迭代、完整backend原返回；固定row_scales真实值；初J和最后计算J至多各一份。last_selected只存J身份引用。若最后J就是初J，值只存一次。失败J只输出确实完成的列块，未写入的 `np.empty` 存储绝不是科学输出。

最近完整全域value保五二jets/T/e/f/eta/PSD/direct主曲率/area一份；失败保实际已完成grid及当前partial。其它成功的大数组明确未保存，不能在后继称免费可恢复。数据输出仍计总600秒，权威最后钟由外层在全部大输出后写出；report job只读该原stdout，费用另列且不重研究。

本任务可能在固定suffix、准备、原box、面积退化、solver时限、非合格后端返回或池外全网门处停止。每一种都保持真实已付来源与成本；没有自动扩域、追加rowset重解、恢复旧epoch或虚构未来候选的路径。
