# 同 g 的既有 154 个 u/v 列：入口体段与尾段两块提案半径

2026-11-15。只改变下一次提案的自由列和半径形状；原几何族、g、b0、原始参数盒和所有真实两网接受门保持。本文没有运行研究候选。

## 1. 明确的实际动机与唯一变化

公开 run 43691833140 的 103 列试验只用了一个 LP 即接纳，随后在第二次 Jacobian 前退出：固定尾域 t=.7725 的最大 eta=.26651073136454873，距离新末态两网最大值仅约2.06e-8，低于原最小接受下降1e-7。LP 用了新半径约4%，没有曲率拒绝。延长同一103列预算或再增它的半径都不能解除这个准确支持锁。

下一步用已有 154 个 u/v 参数，仍是原163维物理族，并固定9个高度参数。两块为

$$
B=[0,54)\cup[81,129)\cup\{153\},\qquad
T=[54,81)\cup[129,153).
$$

B有103列，T有51列。它们互不交，合为[0,154)。T正是剩余的三行既有五次径向样条乘原角方向；没有新增基函数或重定义系数。

初始参考仍是永久原c0；本次实际初值必须由同job恢复growth、strip、scaled-SOC、entry/body103四个必要前缀各一次得到。观察到的bfbd末态不是必须强迫的hash；若wall选择不同，只有实际完整两网合格态可进入，所有当前源、状态、原池和原门身份完整绑定。恢复不算新算法进展。

## 2. 支持与仍固定的几何

按公开准确样条及入口W2/W5乘积，全部154列在开放core前缀及开放tail准确灭二阶jet；其总可变径向区间为

$$
(t_c,t_f)=(9/250,423/500).
$$

入口权本身在左延的行为不能单独当作光滑性；是与保留样条相乘后的O(x5)/O(x8)保证相接。三个新增径向行的支撑依次为[.360,.846]、[.441,.846]、[.522,.846]。Q列仍只在[.036,.360]内。准确clamped五次基在右端的剩余三列满足

$$
B_9(t)=O((t_f-t)^5),\qquad B_{10}(t)=O((t_f-t)^4),\qquad
B_{11}(t)=O((t_f-t)^3).
$$

入口权在此邻域已恒1。故新增全部51列的值及前两径向导数都在tf为0，带任意所列准确角函数及其角导后仍如此；不是只在外侧强行置零。旧前六径向行及Q的支持更短。因此全部154个u/v扰动共同保持core/tail全二jet。实际t=.78的曲率峰在新增尾列的开支持内，本轮已可变化；这只是可变性，不保证曲率或metric改善。

原表示 $X=a\Pi T+z_c e_z$ 中Pi为每一圈的零均值角原函数。固定g和全部height列，故a、b、zc都固定；没有把横向几何当成径向积分。t在该开区间之外时，全部六个位置jets准确不变；H与开帽端口不变。当前height Jensen必要量约.0884仍是未来1e-6的欠账，但不阻本次目标.26，故本轮不混入height改变。

相应常量外域soft两支仍完整聚合为rho_out；外域hard及全局帽高只用原容差验收，不加入要求更高正floor的零Jac模型行。域内偶然零Jac行保留。所有原coarse/fine索引与完整163列J保持，用于学习和诊断；不声称LP投影减少几何J成本。

## 3. Primary 两块盒和原物理无穷范数代价

令 $D_i=u_i-l_i>0$ 是原参数盒宽，固定权

$$
s_i=1\ (i\in B),\qquad s_i=1/8\ (i\in T).
$$

用一个标量r记录控制器，初值和cap均为1/4000，故两块初始半径分别1/4000与1/32000。主步

$$
p_i=rD_i s_i z_i,\qquad |z_i|\le1
$$

并交原盒 $l_i\le x_i+p_i\le u_i$。height9逐位复制，不做全向量加零。

为保原物理正则而不多罚尾列，附加

$$
h\ge s_i|z_i|,\quad0\le h\le1,
\qquad\min\rho+10^{-3}r h.
$$

其最优h正好对应 $\|D^{-1}p\|_\infty/r$，所以代价是原 $\rho+10^{-3}\|D^{-1}p\|_\infty$。把未加权max|z|代入会改变代价，本实现不这样做。模型的soft、hard、fraction-to-boundary、strip/curvature floors均沿原公式；只有自由列和已明示两块盒改变。

同一中心、行集、D和s下增r时，旧物理步仍可通过z按旧新半径比缩放表示，h同缩，目标不变。因此准确LP总最优值不增；这不单独证明rho不增，更不证明真实eta下降。

## 4. SOC 与同一两块盒尺度

令实际被试的primary步为p（包括backtrack比例），并定义

$$
n_s=\max_i\frac{|p_i|}{D_i s_i},\qquad r_c=\tfrac12 n_s.
$$

保留旧SOC变量 $v_i=w_i/D_i$ 和辅助 $h_i$，约束

$$
|v_i|\le r_c s_i,\quad h_i\ge|v_i|,\quad0\le h_i\le r_c,
$$

以及真累计盒 $l\le x+p+w\le u$。目标仍是 $\sum_i h_i=\|D^{-1}w\|_1$ 的epigraph。辅助上界统一rc是本新扩展LP的明确定义，允许直接使用已发表的正缩放helper。

SOC用同一真实y=x+p处的两网残差和旧中心Jacobian：soft target保原预测下降一半的预算，hard target保原实际规则及floors。所有rho预算/抛物预测仍max(rho_out,...)。如果原步零或无预测下降，保持原不调用SOC分支。

对rc>0，已有变换 $v=r_c z, h=r_c t$，以及每标量仿射行除正2幂，在这个新数组LP内准确双射，原目标为rc乘新目标。tail的z盒为±1/8。几何修正恢复为w=Dv，独立用原单位A,b和原盒残差验收；再执行原两网真实门。浮点轨迹与旧LP不要求相同。没有把单行尺度变换套进二阶锥；SOC此处是second-order correction linear program。

## 5. 控制器、门、预算与可归因范围

共同r沿原实际质量/曲率失败缩步、两次全步高比率增长规则更新，最大r仍1/4000。增长的“用足半径”量改为真实两块归一范数 $\max|p_i|/(rD_i s_i)$，并另报原物理范数，避免混用。最小共同r仍1/102400；对应tail派生最小半径1/819200，是本两块政策的明确结果，不称旧全163统一半径保持。

同一阶段原预算12 primary+SOC LP、40粗细完整值、120活动秒、每LP10秒不增加；每模型至多一次SOC、原抛物/回退规则不变。接受必须两网全部原门通过且真max eta下降至少1e-7（或达到新目标.26），原metric预算167/625、硬曲率58、内条带.38999、球1.01、正z、镜像.061、帽高和原盒均保持。

全域curvature/metric真实值仍每trial独立验证；外域preflight仍在新J前。高度9位、g/b0和开端外域全6jet同态检查。总下降1e-4仍只是量级参考，不是接受条件；若未达到，按新的可变尾行/曲率和固定height诊断决定结构方向，不再把每轮1e-5预算续接当作完成路线。

## 6. 实现与人工范围

新helper只消费数组和准确row坐标；新库用原全几何缓存/J与新数组模型；新driver消费四个临时前缀并保只有一个新顶层audit。旧三个科学前缀、旧103算法、原物理模块全部不改。

必要人工覆盖：154/9映射含signed zero、两块主步/物理目标、扩半径可行域包含、SOC按两块半径及累计原盒、原单位缩放残差、固定域与cap处理、真实微型SingleQ接口、四前缀一次handoff及失败checkpoint。人工没有研究候选。具体源码/开发回执冻结后另记；本稿不预授passed。

## 7. 新源、入口与人工结果

本次交付为三个独立新源，不改任何恢复前缀或物理评价器：

- `scripts/frame_entry_tail_blocks.py`：准确布局、154/9映射及两块primary/SOC数组。保留原完整行ID、原单位residual与固定域处理。
- `scripts/frame_metric_entry_tail154.py`：`EntryTail154Objective` 和一次共享预算控制器。全几何与Jac仍是原163列；只在LP组装投影为154列。`configuration` 明确B半径1/4000、T权1/8、共同cap1/4000、streak0及由共同最小半径派生的尾最小值。
- `scripts/frame_metric_entry_tail154_audit.py`：严格四前缀handoff及唯一新stage。新lane为 `metric_entry_tail154`，原生stage为 `metric_entry_tail154_stage`。

实际CLI保持旧24个输入路径、24个输入SHA及 `--out`，合计98个独立参数项；仅把输出名换为 `metric-entry-tail154-audit.json`。它仍要求真正公开Actions环境和原仓库，不能通过本地置假环境变量执行研究。开发入口是

```text
python topics/visible-flex-new-mechanism/scripts/frame_metric_entry_tail154_audit.py \
  --check-only --out "$OUT/metric-entry-tail154-development.json"
```

实际阶段结束会另产临时 `metric-entry-tail154-audit-summary.json`，并直接stdout打印完整模型/trial/实际两网布尔门、proposal floors/SOC原单位残差与对偶、两块利用率、entry/body/new-variable-tail/fixed-outside峰、固定b的Jensen量、四前缀各自计数/墙钟/状态关系。数据文件只存在本次runner临时工作目录，不提交或上传payload。只有源码、参数、run和输出SHA以及科学结论留存。

driver对第四个103前缀核完整source、原24输入绑定、准确163系数、原固定60位、g/b0、原两网门、完整学习池与原径向/角坐标。其旧controller按已完成 `scale_feedback_update` 记录复原；末模型无完成反馈时不计为成功。该controller如实报告，新154阶段不暗称继承它的单块域，而按本设计的两块域启动。恢复的bfbd是否与观察到的旧bfbd一致会显式打印，但不是进入条件。

本地仅执行新的人工入口，结果如下：15项两块数组检查、10项新库/控制器检查、8项真实微型SingleQ接口检查、15项新driver/IO检查全部通过。微型核心为A=9/10、B=18/25，人工c0为 `0.0002*sin(arange(n)+0.3)`，从未载入研究候选。真实类测试确认新增尾列改变t=309/400的几何，同时core/开tail全六jet、完整共同center与b/b_s/b_ss保持。新IO测试用四个显式stub前缀，各调用一次，核源/系数/门/池/采样错误拒绝与异常后的最后checkpoint保留；没有重跑旧科学前缀或旧开发suite。

新接口开发中发现并修正了两处纯接线错误：人工原单位residual字典键名写错；第四前缀的打印器需要controller `origin` 文本。最终入口覆盖了这两个调用分支。它们不涉及真实几何、原物理函数或验收门。开发通过不预言实际154阶段会下降，也不建立连续证书。

## 8. 与旧103源的可审差异范围

主控制器仍以原完整两网真eta严格下降决定接受；primary、SOC、parabolic三种候选均只给154位置赋值并逐位保留height9。旧比例反馈、失败回退、一次SOC、全部预算和最终两网独立重构没有放宽。实际改变为：可变列扩到所有原u/v、固定域右端移到tf、权重盒与相应SOC相对半径、growth用两块利用率而非物理norm/r、显式新域元数据和第四必要输入前缀。

完整差异文件随pending交付，供root相对于已发表103 helper/library/driver阅读。数组helper较旧版缩短是因为复用未变的准确布局/全网数据/常量门类型，非删除实际门。旧版人工fixture的方法也只作为新小数组开发的缓存适配；任何实际执行不走这些fixture。


最终根审仅要求把输入控制器标签从fullspace改为 `restored_entry_body103_controller_not_inherited`，以及对应policy布尔名；它准确指向第四前缀的103列受限controller。两处均为新源元数据，数学、数组、控制分支和已过人工路径不变。改名前源及driver的真实本地开发回执保留原SHA，不把其内容重写为改后源的执行结果；公开 `--check-only` 将消费最终三源。
