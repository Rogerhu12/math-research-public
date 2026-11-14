# 实际 request43：节点 G 求解仍未得到准确的原1372方向

2026-11-14，/root，GPT-6 Astra Pro（AI辅助）。本条依据公开 Actions 已保存的小文本原报告。终端仍不可用，未独立取回或审计本次430MB artifact及其大数组；以下数组SHA是原producer/publication记录，不冒本地全字节核。

## 1. 结论与原执行身份

本轮完成了保存节点G的形成、完整带状LU及三次原坐标全行exact残差读回。第一次校正严格改善原范数，第二次又变大，按既定有限改进规则保留iteration1。最佳原缺陷仍约 **3.25806697778557413e21**，未取得可据以推进原native接受的准确Newton方向。

这不是旧576长J诊断拒绝，也不是G坐标范数达标而被新增门卡住：本条所列量均直接来自恢复后的完整原Q/Pi及同一原1372矩阵、同一原sigma。没有新ODE/J、原nonlinear试步、native solve、cut-J或fresh audit；没有宣称BVP或课题完成。

- [公开run43626121246](https://github.com/Rogerhu12/math-research-public/actions/runs/43626121246)，job132542216129，lane rawcell0gauge。
- 科学源码提交：5c6f45fcac65d96f6b64c8d97f842efcd280f342。
- artifact14126695571，visible-mainline-rawcell0gauge-43626121246-1，430132210B。
- GitHub artifact ZIP digest：2fd2f07095dce463e7f57c473332a3cfc77cdd0cdaa2ad6e02d3b48f0c86b2f5。
- [原发布目录](public-actions-43626121246-1-rawcell0gauge)，publication时间2026-11-14T18:24:55.936167+00:00。
- 主summary：rawcell0-gauge-correction/summary.json，23811B，SHA a2db57bc44db85fa7d7ec2d431a1f20a79d88549ae356c945b64f741342d6f16。
- 完整result.json.gz：13672B，SHA cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e。此处未从connector读取gzip二进制。

原始28和41 artifact均按已钉下载器取入，输入身份继续是actual28 result ff53d954…和actual41 result6e9485dc…。原1372有限矩阵为：

~~~text
e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521
~~~

本轮system源24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92、driver源16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00、原binder fde0e039…均保持接口固定身份。Actions的新源编译成功；该事实不代数值质量。

## 2. 三次完整原坐标读回

每次均支付 **307552行、1372个完整stage、68841584个原乘积位置**，cut与far均在同一读回。原整数核对保存binary64输入计算精确实数线性缺陷；这不等于证明保存J是真实nonlinear flow的精确导数。

| 方向 | exact原sigma范数的原64位十进制显示 | 最坏位置 | 处理 |
| --- | --- | --- | --- |
| iteration0 | 7.099878303686308291209750982733912825511119155233007919123794002E+21 | new518=旧42/step0/Pi112，原方程行116367 | 首个可读回候选 |
| iteration1 | 3.258066977785574130660655122783393002794805785825075998182005090E+21 | new519=旧43/step11/Pi112，原方程行116591 | 比iteration0严格小，保留 |
| iteration2 | 3.769441938574015634509249565132710811608663625592442433418392534E+21 | 同new519/旧43/step11/Pi112 | 不严格改善，停止并保1 |

这些显示值不参加比较；producer保留完整有理数并用整数比较。iteration0的strictly_improved=true仅因此前没有候选，不表示比基态或原nonlinear residual改善。相同原基态全行sigma范数仍为4.177307820740198810865391958317089789308602682333899003945437350E-2，最坏new120=旧10/step11/Pi95。

最佳见证保：
- sigma binary64小端字为27c23cdad1aab53c。
- 未缩放exact residual为[0x779701b9e9a739d764bba46a505b8490792d24a849532e3ce91d8578e64e0ab9, -235]。
- 缩放有理数分子54092034802133273185182148578937011952488210006005503622607435550033831660217，分母16602493187202143890379075863613277664783769308525232128。
- 旧43/step11是ordinary末步，原x=.9166666666666666、h=.08333333333333333；原port应用且ratio1。没有以cusp或另一个profile替换。

三次原exact读回耗时分别42.519744810999995、42.56858381699999和42.492336198000004秒。主过程157.80718726秒，最大RSS1599696KiB。三份完整delta均307552个有限值，无NaN/Inf或负零；后者只是producer记录的数值类别，不保证精度。

## 3. 实际G形成、均衡与LU分别记账

唯一节点anchor及全部耦合沿已发表的[节点合同](2026-11-14-rawcell0-height-slope-node-gauge-contract.md)和[消费者接口](2026-11-14-rawcell0-gauge-band-consumer-interface.md)执行：
节点0..868用实际G，869..1372为I；共869个形成块，包含旧stage72的左G右I混合接口，503个后段原块逐字复用。cut保原target/H并显式乘alpha，far原样。新增形成J348823552B，全部保存artifact。

实际NumPy longdouble是16字节存储、**64个有效尾数位**、指数范围[-16382,16384]，不是把f16标签当成IEEE binary128。epsilon记录为1.084202172485504434e-19。G及完整块形成共43702010个cast条目，其中43680572个在最后binary64 cast后改变；没有所报非零舍入零或nonfinite。此计数不测量误差相对于原问题的放大，也不证明严格相似。

实际身份：
- 保存坐标identity：2fa67b8265873150d631642d3ca57a0e36c8e0549c9750e1313d4275a643ba88。
- 形成后矩阵identity：29bd79753f857d81329270ebb01c23d9a2f90869f8af469891389b68cbf78a19。
- 全部形成J虚拟拼接SHA：600fd77d6204876ab689c89868b11343bdf69342600d346ba4097de142b2ecf4。
- 869块原文件SHA：f917692b01323f05e20801cd8b570fc98a0f422e4c89b725d60692348e72595e。
- alpha/beta/eta原数组SHA依次cd096c91…、35c2357a…、de1f78e6…；全值见原manifest，不用文本四舍五入替它们。

幂二均衡请求最多3pass，实际iteration0改变、iteration1已固定。最终行列非零最大条目范围[1,1.9999999999999694]，无零行/列。这里69149136个带矩阵形成项没有所报nonfinite、非零到零或非可逆binary64缩放；这是**形成后G矩阵的dyadic scaling账**，不能覆盖前面G/J形成误差。

完整band560×307552，1377832960B；dgbtrf info0，1.6088009510000063秒，LU共享原带内存且保指针。LU Fortran原字节SHA97e778e368d40ba1c7c13a010e594b27317d1921550ebbc7f6e436f7b8f14806。LU成功与行列均衡不能替代上节原尺度读回；本次实际即给出反例。

## 4. 真正改进RHS没有用辅助下溢零

冻结原exact reader附带一份浮点RHS，为防它在特殊输入溢出，本轮明确把那份**从未送入LU的辅助副产物**统一乘2^-2048。三轮各有307440个非零原行在该辅助数组中下溢为零、112个exact零。这是已声明的诊断账，不能误称求解时删去这些行。

真正用于LU的RHS从保存完整exact dyadic ledger重新流式构造：cut乘保存alpha0，活动Q/Pi行按保存alpha/beta/eta做精确整数乘加，identity及far保原行，最后乘实际row exponent并一次nearest/ties-even舍入。每轮307552行/1374个block均在。

| 真正RHS | 最后舍入改变行数 | 非零下溢为零 | exact零行 |
| --- | ---: | ---: | ---: |
| 初始base RHS | 15484 | 0 | 179645 |
| iteration0改进RHS | 307331 | 0 | 112 |
| iteration1改进RHS | 307328 | 0 | 112 |
| iteration2记录RHS | 307328 | 0 | 112 |

iteration2后已停止，没有把其RHS再送入一次新solve。初次列幂二恢复307552项无所报损失；初次原Q/Pi恢复194656个活动值有194444个末次cast改变、无下溢零/nonfinite，identity节点直接复制。每个最终原方向仍由完整exact读回约束解释，恢复公式本身不提供误差保证。

## 5. 完整保留的候选与ledger

| 原件 | 字节数 | SHA256 |
| --- | ---: | --- |
| iteration0完整原delta | 2460416 | ce3369e45e2793b6101e3e67e6f7b98cb94b93e572d237d409a2381c44fdd64a |
| iteration1/最终完整原delta | 2460416 | 10ed4f19b2ea2acf2b3a218d2ce8ee6a575b1982c0fcda431c850a524903b128 |
| iteration2完整原delta | 2460416 | c50e82d27ac3814ac071acd572821280de84040f3e80bb7dc487884498aaf69e |
| 最终完整checkpoint.gz | 3277376 | 680f838603ac3c6f08b99ed1845d373306dc170b8171be25f61d090934aa8f49 |
| 原577节点限制delta | 1033984 | 62939e70eb366988c00623fc46645bb07c8a28f6619831916f69996a50c8aed7 |
| 限制checkpoint.gz | 1473203 | ff7027514d5ffed3930475c24e9ff583eb56dd7d06bc23dcd8b4bbef7ac36475 |
| iteration0完整exact ledger.gz | 8765846 | 52f4b16bf81cea8e32e37160149059ccc86589d19b01efb0f9c3ddb433be45c7 |
| iteration1完整exact ledger.gz | 8705720 | 7c53d29e9fd60376fc00cc8055cd9146defb12f017c7c94c743f0bcf7179f90b |
| iteration2完整exact ledger.gz | 8690486 | ac0e81f89f1f04e1dcff0cd78c6e843ef31e44e429a0206c1c4392bf06431aef |

大阵/完整ledger留artifact。output-array-manifest.json为25042B/SHAf0533e52327eff3789e41fea44077e711abf421138ef067069b660336067dbc4，原publication完整记录被排除Git的大阵与已发布小文件。这里亲读summary、formation、equilibration、factorization、三份iteration、初次solve/recovery和initial真实RHS；未声称逐一重核430MB压缩包或全部新数组。

## 6. 第42次只读摘要的范围纠正与下一实际工作

同一job的第42次只读summary步骤设置continue-on-error。GitHub步骤表面conclusion=success，**但本轮发布目录和publication.files均没有request42-receipt-summary.json**。因此此前进度中“该摘要已提取”的表述撤回；目前只能说该step运行状态表面成功，不能据此说七件SHA核或摘要产出已经完成。它未影响本轮G计算。

将给原只读提取器独立v2，始终保存phase、逐件身份进度及异常的小回执；仅读已完42报告，不重原科学，也不把失败改成成功。具体旧摘要失败原因在可读错误回执前保持未知。

本次G失败不证明完整矩阵奇异，不单独定位到形成、LU、恢复或原J的某一层；也不证明原非线性问题无解。不重复同方向同修正。下一native源码分析沿[R271](../results/R271-discrete-RK-stage-gauge-covariance.md)区分原RK各级的完整变分与端点保存J的有限精度，保真实schedule/port/全部模式；新G原十试步组件可保存但本次坏方向不调度。前缀同时继续R270完整局部QP实现，保全部原方程和真实试步验收。任务未完成。
