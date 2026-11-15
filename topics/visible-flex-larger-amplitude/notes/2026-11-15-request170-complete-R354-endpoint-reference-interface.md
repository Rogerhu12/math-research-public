# Request170：原37模型后的R354准确有限端点与Hermite余项读回

作者：ChatGPT /root/exact_refinement（AI协作）；2026-11-15。

**本包是独立可执行源码及Actions接线，没有本地科学运行，也没有实际170结果。** 原actual98父件在同一Actions重新生成一次原37完整模型及其真实新warm FD；原结果先读回，随后才执行R354新的区间/整数算术。新诊断不进入原模型、17档回溯、域、merit或FD接受条件。171的37→38实际续接另行运行；本请求不修改它，也不拿已删除的155/166现场SHA伪造输入。

## 1. 已付依据与本次具体工作

[R353](../results/R353-actual166-complete37-affine-certificates-and-pointwise-Hermite.md)实际166已经支付完整37查询的原模型/FD、75776个字面仿射多项式、17档Bernstein以及已访问点的453行Hermite形成差。它没有把端点RHS沿完整步长线段的二阶余项变成零；最近拒绝12行的实际与仿射集合一致也不证明Hermite曲率普遍无作用。

本次按已发表[R354](../results/R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)实现以下有顺序的计算：

1. 复制真实原A分块已有的scalar基底及控制矩阵，并绑定该分块的原J/P；不新增原profile、RHS或J调用。
2. 对全部实际端点变体，准确作用全部338个物理列和3个参数列，保留115个常数RHS零行，形成完整453行的两个Hermite字面缺陷。
3. 在准确均匀角网格上独立包围端点参考RHS及其一次方向导数，得到原字面基点/RHS/J/P作用的误差区间。
4. 对每个端点变体、全部2048角和17个闭段，形成完整八次P及所需导数，用完整Bernstein和R354.14支付二阶界，或保留未决/准确参考端点反证。
5. 对全部37×17个声明末点alpha_j，用R354.21传递该末点完整453行的准确Hermite差。闭段[0,alpha_j]仅用于其导数上界和域；差区间本身是末点包围。实际原query返回存在且有限时，还读出该点原字面query相对准确参考的eta外包。

这里的最后一项是**已执行点的包含区间**，不是整个IEEE程序在所有alpha上的误差界。本包也没有实现R354第8节的完整query角域转移。因此即使端点/参考Hermite界全付，`entire_original_IEEE_execution_error_certified`和`complete_true_Hermite_query_angle_domain_certified`仍为false。

## 2. 冻结文件与独立身份

五件运行/参数文件如下。前三件和request位于`topics/visible-flex-larger-amplitude/computations/`，workflow位于`.github/workflows/`。完整blob仅保存小源码/参数文本，不含原数组或新科学结果。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_R354_thirty_seven_literal_endpoint_capture.py | 24543 | 74fc383db1b00c564ccab9709b1de5f500674914a5efef83997960c867950c4c | 6490fab8afd4d903b9e678d0ca4d2e1544f2206d |
| exact_20261115_R354_thirty_seven_endpoint_remainder.py | 75046 | 84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a | 4b1a7507b591ebd6fe378b8e3b64f3302051d48c |
| geometry_20261115_R354_thirty_seven_same_job.py | 23697 | 46f85ccec569533d8d7652d94b059dc9c8d49e926408f68dd131002ef5c71cbd | ae85013ee007cda390c04ad2ad5b9b20831cc625 |
| public-thirty-seven-R354-reference-diagnostic-request.json | 30406 | 4206610b365bd01e1ce2833c3cc78f3c4dd7ad15725b45db1486dc6c4d81f8cd | 56061593310ab3f05d298501523c4e603c59f682 |
| visible-larger-public-thirty-seven-R354-reference.yml | 9856 | 2334bce68a2f0e926e57eb86c6a1bd123bd2ce0e9b0d9a82bf196f314408c521 | 135fa63d812b9f22c2b7e0c05a79145a464f3c9d |

本接口目标路径为`notes/2026-11-15-request170-complete-R354-endpoint-reference-interface.md`。源文件、参数和接口是可复现定义；完整diff只供对已发表166的源码差异读回，不另作为科学门。

新schema分别为：

- 观察：`R354-original37-endpoint-literal-cache-capture-v1`。
- 新科学结果：`R354-original37-finite-endpoint-and-Hermite-enclosures-v1`。
- 同job编排：`actual98-original37-one-model-FD-then-R354-reference-diagnostic-v1`。
- 独立请求：`actual98-original37-R354-reference-post-model-request-v1`。

没有把新来源改称166。原37 producer/observer/FD及完整原模型schema保留自己的实际身份。

## 3. 全来源和真正父输入

本次明确从actual98原父另起。原artifact run43677587785、ID14147700690、名称`visible-followup-condensedqp-43677587785-1`，完整ZIP809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。原source为`918fdb11dbb7a424b6149b405e2c7fab3cc0c737`。原完整ZIP先核真实size/SHA，按既有运输器提取以下原pair：

| 原件 | 字节 | SHA256 |
|---|---:|---|
| warm-001.json.gz | 4927052 | b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |
| driver-status.json | 3379453 | b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |

原status保压缩/JSON原bytes，不以新序列化代替父原件。没有actual155/166新warm被当成本次父件。若历史运输或来源绑定失败，原样报告工程/来源失败，不从SHA制造数组。

原155 recipe `public-thirty-seven-model-recipe.json`的SHA仍为`f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea`。其90source pins、原worker1件、158历史独立3件、166历史独立3件全保，再新增170三件，共**100 source pins**。旧158/166诊断源码只作精确provenance，不执行它们的主程序。三参数文件仍为原source-dependencies及两原recipe，逐字不改。

原78公共source恢复、accepted/profile/mesh等实际输入恢复都由原155 helper/worker执行，未插入未被消费的新历史数学输入。source闭包的完整逐basename SHA在唯一request中，工作流逐项核；不另以复制一张来源清单当数值认证。

R354原证明20501 B / `b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183`，发布提交`f55808987a14ffaccf066e97a37094893c6207de`。工作流与consumer都核这个真实文件。

## 4. 原模型、FD及所有未改门

完全沿原37集合：21 LEFT-RMS、16 collocation-midpoint，37×2048=75776个B行。原LEFT fraction字面0.17267316464601146，原MID为0.5。全部24捕获区间、29端点463..491、原完整236036坐标、699×453态、109自由core、完整外变量恢复及原C/H/权重来源保持。实际不同chunk的端点变体数在运行时形成，不预填为29或74。

原模型仍：

- 一次原complete model，damping270、LSMR200、projection200；
- 原17档、angles4096、Jacobian workers2、预算1200s；
- condensed预算600s，trial/recovery reserve90/30，完整working512及dual200；
- 原全节点、中点、左右RMS、selected query、真实merit等全部接受条件；
- 对原真正产生的新warm执行原FD入口及原阈值，不把父warm或旧FD改标签。

新consumer在原model/FD attempt返回后启动。即使独立诊断exit2/3，原已记录的model/FD exit及accepted字段不被重分类。完整原主结果先用旧worker的全字段readback输出，随后保存独立诊断。没有新native/fullDN调用、没有新的优化或试步。

## 5. 原A分块与scalar缓存的真实配对

原`AugmentedFlow.scalar_jets`在每次实际调用中使用：

$$
b(x)+C(x)p.
$$

其`_base_cache`键是该次完整station数组的原`x.tobytes()`，值是原实际`base_jet`数组和全部`control_jets`数组。新观察器在原Domain构造返回后只读取这个已存在字典：

- 对`EndpointJacobianCapture.calls`中的每个实际原A调用，按完整station count、shape、dtype和原framed SHA匹配一个缓存条目；
- 保存完整station数组、三列baseline和3×3控制矩阵的全chunk原words；
- 按同一chunk中原mesh相邻二词定位LEFT/RIGHT，不按近似float距离猜位置；
- 每个query保原`endpoint_original_call_number`及同号scalar cache；
- 原J/P的物理338×338、参数338×3和每个端点原SHA仍逐项绑定。

原166已解决的query control配对继续保留：station字面加原explicit B控制身份，全部观察调用完整保留，不要求总调用数等于query数。原166实际74次是历史事实，本次计数由真实调用产生。

端点计算只在**同节点、J/P、baseline及controls全words相同**时复用；每个来源call/position仍列在`all_identical_word_origins`。任何不同word变体都独立处理。不得从Bz反造query输入，也不把两个chunk的共享节点随意合并。

该扩展只复制已返回/缓存数值。原返回对象、原flow别名、原observer以及临时control方法都按finally恢复；复制失败被写为observation error，原科学decision仍照原代码返回。

## 6. 准确参考、有限字面与三种误差

固定原mesh节点，参考使用实际b/C二进制字面的准确实提升：

$$
(a,\nu,\mu)(\alpha)=b+C\bigl(p_0+\alpha\,\Delta p\bigr).
$$

所有三scalar字段及三参数保留。这里nu仍是原`ap`返回字段，不借此声称旧有限积分的准确空间导数。端点状态保原全部453行；core/parameter的局部RHS及其两次方向导数是原公式中的115个零行，原全问题的这些变量没有被删除。

准确角参考是theta_n=2πn/2048以及完整频率0,2,...,224。`arb.sin_cos_pi_fmpq`用准确有理数乘π得到sin/cos包围；不把np.pi、原FFT的舍入twiddle或已形成jet字面当作准确三角值。

旋转坐标两jet逐式沿原源码。r包含113项，t包含112个sine项，z包含113项；两个mean分别在物理row0及225。z常数对角导数为零是公式的平移不变性，z均值RHS投影仍完整计算。准确投影保全部338行，均值权1/2048、其余2/2048；原115零行明确补入到453行。r/z非均值行用cos，t行用**正sin**：原`geometry_20261114_fft_frenet.py`的`real_project`和实际`geometry_20261114_r225_free_core_bvp.py`的`BatchedFFTFlow.project_real`均取`-(2/N)*rfft(...).imag`，而DFT虚部是负sine和，因此这与`+(2/N)*sum(value_t*sin)`一致。consumer已将审读稿中的负sine改正；R354使用绝对投影行和的2/1二阶界不受这一符号修正影响。

R354速度用完整有限多项式：

$$
Q=d\cdot d,\quad S=d\cdot e,\quad C=d\times e,\quad
W=C\cdot C,\quad B=Qe-Sd,
$$

$$
P=a^2W-\nu^2Q^3,\quad T=\nu QB,\quad D=aW,
\qquad V=(\sqrt P\,C-T)/D.
$$

所有九个P系数、六个D系数、每个T分量的七个系数均保。正a、正P以及原scalar的绝对nu<1分别处理；只要盒跨零就保未决，不把区间过宽写成原模型失域。准确端点值的上界已非正时才可记录该**准确参考端点**的严格反证；它仍不替代原浮点trial。

以下三个对象不混用：

1. 原实际完整RHS字面`fhat0`。
2. 存储原J/P字面对完整实际方向的**准确dyadic作用**`ell_exact`。
3. 本次后置算术新形成的binary64 matvec及query方向`q1`。

consumer单独记录新formed action减准确JP作用，并将新q1写入临时原字节NPZ。它不声称q1逐bits等于原稀疏B内部未导出的中间数组。

准确有限RHS及其一次方向导数投影后，逐行包围：

$$
e_0=f^\ast(0)-\widehat f_0,\qquad
e_1=(f^\ast)'(0)-\ell_{\rm exact}.
$$

完整453行向量在临时ledger中；紧凑readback保全行范围、最大绝对上界/对应行、全部非零形成范围以及两个mean原区间，未声称在chat重新逐读大向量。

## 7. 闭段二阶界和Hermite传递

对j=0..16，alpha_j=2^-j。本次对每个原端点变体和全部2048角的**二阶导数及域证明**处理整个闭段[0,alpha_j]。随后`endpoint_E`以及完整453行Hermite差使用固定alpha=alpha_j，分别包围这17个末点；它们不是让alpha在整个闭段内变化的统一gap盒。

P、a、nu、D及C/T各分量和一、二阶导数均用完整向外Bernstein。与全区间Horner包围取交只收窄同一准确多项式的包含区间。系数盒包含固定真系数；不是随alpha任意更换函数。

当闭段严格正a/P和原scalar域均已付时，使用

$$
D_-\ge P_-/a_+>0
$$

与直接D包围取更强下界。R354.14的所有平方根、除法、乘加都向外计算；没有用浮点采样max代替二阶sup。非均值物理行使用2×全角m_V上界，两个mean使用1×，115常数行保持精确零。缺一个角就不把已访问角的最大值冒充完整RHS界。

原h及四Hermite权取其实际finite字面的准确提升。先以整数dyadic计算全453行delta_H0、delta_H1；随后按R354：

$$
E_i(\alpha)\in[e_i^0]+\alpha[e_i^1]
+\frac{\alpha^2}{2}[-M_i,M_i],
$$

$$
Y_H^\ast-\bigl(\widehat q_0+\alpha\widehat q_1\bigr)
=\delta_H^0+\alpha\delta_H^1
+h\{w_{10}E_L+w_{11}E_R\}.
$$

上两式在本实现中均于固定alpha_j代入。每个query/alpha_j保存`accurate_reference_pointwise_Hermite_bound_available`或具体未付端点变体；旧审读稿中的`closed_Hermite_bound_available`名称已删除，避免把点态gap误认成整段统一gap。结果同时明确`Hermite_gap_intervals_are_pointwise_at_declared_alpha=true`、`whole_alpha_uniform_Hermite_gap_enclosure_computed=false`。完整453逐行区间留临时ledger；所有query/末点状态、极值、常数行、两个mean及未访问pairs在结果中。若将来需要t遍历[0,alpha_j]的统一gap，必须另将delta_H0+t*delta_H1、e0+t*e1及t²余项整体包围；本包没有声称已做这一步。

如果该档真实原query返回存在且有限，将它的准确字面提升减上述参考盒，得到该点eta的外包。该区间包含状态形成、原RHS执行及原SciPy/query形成差异，并不按一次宽盒拆定唯一因果。它没有对IEEE舍入映射求导，也没有证明未执行alpha处的执行误差。

本阶段止于准确端点与准确Hermite差。将其进一步传入全部query角域的R354第8节、全699节点/698中点/两组RMS以及连续角，需要各自后继。输出明确保这些flags为false。

## 8. 向外算法及精度含义

全部通用区间为闭盒[lo,hi]×2^-320。加减和整数倍精确；乘法、除法、sqrt使用Python任意整数floor/ceil/isqrt向外。sqrt上下端各自按平方比较支付ceil，不转换成binary64。

原binary64输入先用准确`as_integer_ratio`/dyadic整数表示。原JP乘积和Hermite形成差不先做浮点减法。角合成的完整线性组合先在共同二进制单位累加整数，再一次向外投到320-bit网格；完整DFT投影同样先累加所有有符号权乘积再向外除2048。这避免每一项被不必要的额外网格舍入放大，同时保所有原项。

Arb工作精度384bits，仅用于准确有理π角的sin/cos。取其严格lower/upper有限dyadic，再向外投到320-bit网格。包络依赖的是Arb提供的包含保证，并非仅取一个高精度近似。所用公开API见python-flint官方`arb`文档及0.8.0发布页；0.8.0具有CPython3.12 Linux轮子。本请求固定python-flint0.8.0，numpy2.3.5、scipy1.17.0、Python3.12.14保持原版本。

320-bit是本次区间表示，不是“误差小于2^-320”的统一数值结论。窄正裕量、依赖放大或大输入可以使盒过宽；这些情况保持unresolved，不能声明全局误差底线或无根。

## 9. 执行顺序、资源与部分结果

全局clock在输入恢复之前开始，包含历史运输、原78恢复、原完整A/J/QR模型、FD和诊断。全局资源10800s，保300s清理/读回余量；独立诊断上限5400s，并在实际剩余量中再留60s给consumer形成末结果。没有给后置算术另外一个从零开始的无限总预算。

工作流science190min、job215min、always readback15min。原规则监控3b8仍每2700s真实同步；根21bd、题bff是当前已读规则字节，保原真实pull/rebase/diff-stop逻辑。contents write仅沿原规则同步职责，不发布科学raw。原科学checkout固定触发SHA。

原model/FD自己的1200/600等预算不改。完整端点数和每个界的实际成本尚未数值试跑，5400s不保证完成全部端点×2048×17；不能把范围声明写成已完成计算。

优先顺序是完整JP/Hermite形成、各端点准确基点/一次导数、全部闭段二阶界、全部Hermite传递。已合成的完整角输入保存为临时gzipledger，后段复用它而不重复原profile/RHS/J，且逐文件size/SHA和全部angle顺序核同。计算中的bounds计数在完整17档该角记录写入后才前进，避免byte-cap中断造成count先行。

资源partial保：

- 所有未完成的完整JP作用变体和453行形成query；
- 每个端点实际已处理角数、未访问角闭区间；
- 每个alpha的准确域未决/准确端点反证角范围；
- 不完整投影不能补零，也不计算假完整mean；
- 所有未访问query/alpha及完整453行责任；
- 原17档每档真实visited/unvisited、原trial记录和实际返回有无。

暂时ledger未压缩总额上限8589934592 B。大逐行表只在RUNNER_TEMP；结果记完整写入scope、size/SHA、紧凑极值/未决范围，不把它们编码、切分或复制到Git/Release，也不要求主控把大表逐值读完才能推进后继。没有新artifact上传。

## 10. 停止、输出和清理

`scientific_completed`只表示本次声明的独立计算序列全部访问完，不表示域界、IEEE执行或native成功。结果另列全部准确Hermite界是否可用。

- 原输入/源码/程序异常：consumer exit2，完整exception/traceback保留。
- wall或ledger cap：exit3、resource_partial=true，保已完成前缀及未付后缀。
- 所有计算访问完但准确域/参考界仍未决：scientific_completed=true，exit3；这不是原模型数学失败。
- 全部声明准确参考Hermite界可用：exit0；原IEEE闭段、query角域/native/fullDN flags仍按未付保持false。

`result.json`保存完整标量、元数据、所有未决/未访scope，`summary.json`保存有界主读数与真实原件SHA。完整453向量及每角多项式/二阶表在临时ledger，不冒已全部公开。同job always readback读取原主结果、诊断result/summary、capture全部实际控制/端点来源、原rule-runner结果及每个异常child日志。错误字节沿冻结155 helper的12000-byte surrogateescape/ASCII双层JSON传输，无70KB尾截断。

只有实际`complete_readback.outcome == success`才执行workflow清理；runtime还要求自己的readback-complete原记录。若读回解析、超时或中断，未读数据保留到runner自然销毁，明确不能据此宣称完整读回。SIGKILL、平台中止或硬资源故障不被伪装成某个准确域反证。

输出仅脚本、参数、run/source、输入/输出SHA和紧凑结论。科学raw不进Git/Release/artifact，且没有未来170 run/result/accepted身份写入本包。

## 11. Actions入口和差异范围

独立触发文件为`computations/public-thirty-seven-R354-reference-diagnostic-request.json`；独立workflow/concurrency不取消166、171或其它请求。

唯一入口：

```sh
python -u geometry_20261115_R354_thirty_seven_same_job.py \
  --repo-root "$GITHUB_WORKSPACE" \
  --request "$VISIBLE_COMPUTATIONS/public-thirty-seven-R354-reference-diagnostic-request.json" \
  --work "$RUNNER_TEMP/visible-R354-170"
```

`--mode readback`只读已生成原字节/JSON；`--mode cleanup`仅在完成读回后移除本请求namespace。实际模型命令由原155 helper构造，只把私有MODEL_ENTRY指向新观察器；观察器调用原37 observer.main。FD入口没有替换。

consumer实际CLI：

```sh
python -u exact_20261115_R354_thirty_seven_endpoint_remainder.py \
  --capture "$WORK/batch-000/thirty-seven-condensed-warm/R354-return-capture" \
  --model-directory "$WORK/batch-000/thirty-seven-condensed-warm" \
  --code-directory "$VISIBLE_COMPUTATIONS" \
  --seconds 5400 --max-ledger-bytes 8589934592 \
  --out "$WORK/post-model-diagnostic"
```

实际seconds由同job剩余时间clip；上面的5400是上限。capture其余原命令flag保持原37全部预算。

相对公开166提交`c3a7531db21286c7b4dec98904f8ac4a020dafa4`完整五diff如下：

| 新文件对应差异 | diff字节 | diff SHA256 | 临时源码diff blob |
|---|---:|---|---|
| geometry_20261115_R354_thirty_seven_literal_endpoint_capture.py | 10405 | 1dbbda1b07b81e7b54b61f738a056a283a0cc65de310b02fd1bffa3572c0299a | 60375c555e6f9b7a7d031d502494417b67582b8f |
| exact_20261115_R354_thirty_seven_endpoint_remainder.py | 91573 | ec542e6c55d5b41f5dda5559458c0c5fc2efc00ae60b109c1b03b82e7e331543 | 1011b556fb1ab4503f6295e74d7802d4aed8bd8f |
| geometry_20261115_R354_thirty_seven_same_job.py | 18094 | e6d2a9b9c697e9ee97e2eb241420afe593fffde804020d10bd0f2890f04e9838 | 49bdbecdfadc6186edf0c0d67003e803a2bf3e3c |
| public-thirty-seven-R354-reference-diagnostic-request.json | 14774 | cd48662ff6d63d5f86f40bc565fa50559b3d0f4c26e571602f1209e64a260f64 | efc46589b150b1584019def6d5c46fc213e09b2f |
| visible-larger-public-thirty-seven-R354-reference.yml | 10719 | d750b19440306593e433e7336e2d71eb5c595f3a46b54c95ee410db9663b9243 | b9a2c2af09996d76b3fc390dbd39a53945f52dd4 |

新consumer保原Packets/raw身份、全部query controls配对、完整原trial绑定的实际逻辑；新准确算术独立有新schema。完整capture和coordinator继承166运行/错误/元数据协议，仅新增本次缓存来源、R354入口/参数、预算及读回字段。旧37数学四源和原FD门完全未改。

当前终端不可用，未声称本地Python AST、bash-n、导入、编译或科学测试。已完成的是完整源码文本、精确byte/SHA、既有来源/字段和数学公式读核。Actions原source检查逐字核100源/3参数及R354文件，并AST解析Python后执行。它不是新增的数学试验或等待批准门。本包没有本地计算新模型、任何范数、区间数值或未来结果。
