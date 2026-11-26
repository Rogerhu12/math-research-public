# 实际父场 SO3 的严格内点 Phase I 继续入口

类型：完整算法推导和已保存的小源码；实际新求解尚未返回。来源是[02阶段43–45](2026-11-26-actual-normalized-parent-so3-four-restorations.md)，不是新几何证书。

## 1. 为什么改变搜索目标

真实3ef8568c末场仍有正物理违反量 $2.1482238210523974\times10^{-10}$。四次完整恢复均alpha1接受，内层均达到自己的face/release或数值KKT容差，并非64步预算耗尽。原Phase I同时惩罚共松弛和坐标步，因此即使内层求到所声明容差，也允许残余slack为正。继续只扩大内层预算没有处理这个结构。

此入口从该真实末场继续，只在恢复阶段引入明确严格向内目标 $\varepsilon_{\rm in}=10^{-8}$。原物理 $g_i$、完整目标度量、所有自由量、正权观察、范数、原几何/幅度行与完整非线性验收不变。这个数是新的搜索参数，不是容许正违约的误差阈值。

## 2. 完整虚拟行与正缩放

设完整已生成行保存原物理值 $g_i$、坐标导数 $\ell_i$、正行尺度 $s_i$，原缓存行为

$$
C_i=\ell_i/s_i,\qquad b_i=-g_i/s_i.
$$

实现先逐行核原 $b_i=-g_i/s_i$ 的浮点一致性，随后保留原缓存和全部原metadata，不改 $g_i$。恢复阶段的增强模型改为

$$
g_i+\ell_i z+\varepsilon_{\rm in}\le\tau,\qquad
\tau=\tau_0+\delta\tau\ge0.
$$

取

$$
\tau_0=\max(0,\max_i(g_i+\varepsilon_{\rm in}))+\eta_{\rm init},
$$

其中 $\eta_{\rm init}$ 是原代码量级的显式正浮点初始化padding，仅保证增强零步的工作可行性。令 $d_i=(\|\ell_i\|^2+1)^{1/2}>0$。完整虚拟行恰是

$$
\frac{s_i}{d_i}C_i z-\frac{\delta\tau}{d_i}
\le \frac{\tau_0-g_i-\varepsilon_{\rm in}}{d_i},
\qquad -\delta\tau\le\tau_0.
$$

乘回 $d_i$ 即得到原增强不等式；没有删行、丢失零梯度行、翻转不等号或只缩一侧。所有矩阵列仍使用原完整streamed C，另外一列为 $-1/d_i$；没有复制一份多GB行缓存。取 $z=0,\delta\tau=0$ 时，每行均满足初始化上界。

目标仍为

$$
\frac12(\tau_0+\delta\tau)^2+
\frac12\mu_{\rm restore}^2(\|z\|^2+\delta\tau^2).
$$

新模型若得到 $\tau\le\varepsilon_{\rm in}$，只能推出所选线性模型的原 $g_i+\ell_i z\le0$。它不能推出真正非线性几何可行，更不能推出连续reach或存在。每个实际试步仍重读完整场与全部永久地点，恢复仅按原严格真实违约下降接受；只有实际完整物理 $g\le0$ 后才进入度量方向。metric阶段原Phi下降和全几何筛原字保留。最终正g仍一律失败，不减margin后再验收，不舍零。

## 3. 真实继续身份

继续的原固定父与新坐标末场不可混为同一对象：

| 职责 | 实际SHA256 |
|---|---|
| 冻结的旧父bundle | `d021a50a492b941004ee75f5cba138d5b5bc07092073a642a027bde4f97bb478` |
| 冻结的旧父report | `86a79cc29fec40a6e1515fac355e7925c7fcae459dff4a76baddfbadddee45d5` |
| 准确固定scalar | `0a223b986f35263c168e26d30295fd84048e134c6b053ba90c7cd39beaf1f5cb` |
| 本次restart完整SO3场 | `3ef8568c75bee9e2fbc85756abc5d90a579059e25c1bb9a3f25aad02ea132077` |
| 本次restart完整SO3报告 | `3b73d81a30e1cb9925278549ee505462b175afae7da54b7e00b1c02948576b10` |
| 原SO3模型 | `ad01742ce5051188bafddf8e93046468788eb27e7ec948c26903578742f5bb92` |
| 原正坐标范数 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |

新driver仅允许两种完整报告来源：自身完整source/schema对，或实际已返原7e9095b3源码与原schema的精确对。原7e完整文件仍保留并再核字节；还核全部底层source roles、原父bundle/report、carrier、node/scalar输入、完整model/profile/norm，以及实际final bundle哈希和complete状态。不是放宽为任意旧报告，也不是把无场失败报告当checkpoint。

全部2775曲率/2743半径历史、原来源报告内其他地点及原双符号通过原history解析和新场完整重读保留；新的试步地点继续append-only记忆。重建准确固定目标后，当前场的实际Phi/Gram重新读取，不用旧报告数值直接当新baseline。

## 4. 三份完整新源与全部参数

三份是独立完整小文件，原7e/b534/eb26及其历史消费者不覆盖。完整底层21项SOURCE_PINS逐字保持。

| 完整文件 | SHA256 | 字节 |
|---|---|---|
| `fullclosed_so3_actual_profile_interior_restore_qp.py` | `0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6` | 49378 |
| `launch_so3_actual_profile_interior_restore_actions.py` | `95e90ac02f05df24b2fca7e2cdd6f3dcc051edc6ffd9973e26073a21314057b2` | 9928 |
| `read_so3_actual_profile_interior_restore_report.py` | `1e2071b2b0dfa4d25f73678450321f67fd47257d045a09179afae32fb3bfc362` | 17301 |

[完整两步参数](../computations/resume-20261126-so3-actual-profile-interior-restore-ready-steps.json)保存所有argv、来源及标量投影；SHA256 `af9709b1302208dbc922280de9888b9ec814f9628eb506bc516dc41cf2154c63`，14364字节。旧完整四输入路径和全部科学参数保留，另显式加入真实restart checkpoint/report与 `--restoration-interior-margin 1e-8`，输出用全新目录。完整计算仍M160/J923/N2048、1333370变量、45324288残差行；至多四条64步恢复后，一条16步metric，原mu均.01，原192几何选择加所有幅度行，原积分8阶、正测度、p4谱目标、root设置及全量实际筛不改。

新launcher逐字核driver及其全部完整依赖，再在原公开Actions执行。新reader核每一条恢复二次模型都携同一个正margin、原物理g未改、真正验收未松弛，仍把slack、原物理违反量和真实可行分开，并核完整report/source/model/profile/final。

root已完整读原7e/b534/eb26源码和全部修改片段，逐字变更锚点及UTF8摘要核对完成；13:55 UTC起终端执行环境失联，未声称新三源已在本地AST/compile通过，也没有运行本地科学。公开Actions实际入口保留Python解析和完整源码pin检查；具体运行结果待真实返回后登记，不预填成功。恢复后补真实git pull和双README差异检查，不把connector在线读写称为终端pull。

## 5. 仍未完成的数学责任

向内恢复只针对当前有限非线性screen；即使它真实通过，仍需实际度量下降、同场连续六jet误差与全域metric、整像握持幅度和含反射非全等、全t嵌入/reach、固定g/参数的真实加密及严格存在缺口说明。原约.0368误差不能靠恢复或正常exit变成课题完成；继续求解而不另设阶段结束门。

## 6. 真实46–47：一条恢复后进入原可行侧并接受metric方向

root已亲读公开 [45800076687/1第5卷](2026-11-26-public-actions-45800076687-1-part-005.md) 的完整紧凑实际46–47。科学子进程实际退出0、外层2765.206435963002秒；driver记录2761.091256161999秒，完整首次重建及读取1812.1884115920002秒。执行源码提交为 `a552c4310b408277601f218f90dc130b25fdd1ab`，三完整源身份与上表相同。原1,333,370变量、45,324,288行、固定profile0a223、modelad017、normc4b2及四原输入不变。

| 同一场/目标下的真实读数 | 初读 | 末读 |
|---|---:|---:|
| 相对Gram最大工作误差 | 0.036815450191476695 | 0.0367702256157602 |
| centered Phi | 0.006744440394939325 | 0.006732795879926417 |
| 原物理最大g | 2.1482382539517175e-10 | -6.229263438406463e-9 |

实际只需要一条完整恢复，随后一条metric方向接受；两类各1条均accepted。末有限必要reach乘积0.9919999937707366，完整真几何screen通过；body、两个witness符号、cap、height的g依次为−0.0478184890624751、−0.09045752237074689、−3.3090759487602863、−0.12674488163262654、−0.9649116696511933。全部2813曲率/2781半径永久地点及双符号实际重读。原g≤0验收未改；没有把正违反量或公共slack当可行。

完整初场仍为3ef8568c；新末bundle为 `793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044`（10720258字节），完整报告为 `bb5c52e02af18b02cd2aed9a9d64fe6bb687f8f1f1510fe0792684ff241f9241`（28986791字节）。二者只留runner。原1e207纯reader真实第47步输出66929字节、SHA256 `9f04f25265f53d37950ae243f1d865d04ea116778428f84dbbbc6943a00899cb`；无summary错误或缺失输出。

实际residual/J/Jtranspose计数为9/18/19，point covectors392，parent provider调用21331、累计22981115点，完整field求值200592367点。逆图工作残差6.661338147750939e−16，最小工作rho为0.165900335171834；这些不是连续误差界。末两种mu都为.01。停止原因是已声明metric方向预算，不能由此称驻点或停滞。

46–47现有紧凑公开字段没有该两方向的alpha、QP状态、Pg和原容差；[完整纯归因参数](../computations/resume-20261126-interior-first-direction-details.json) 已追加02，仍使用同一完整1e207 reader读取已有bb5c报告，不重算科学。完成真实归因后继续新方向。下一完整入口可以明确采用固定参考缓存，但须核实际来源、全query及新文件字节；不能声称旧报告从未记录的缓存SHA已经历史绑定。

本次仅将完整有限screen推入可行侧并取得实际目标下降，最大误差仍约0.03677。连续metric/reach、精化与严格存在责任完全保留。环境恢复后的实际AST/compile-only已在2026-11-26 14:51:46 UTC完成，详见同日SOC入口§9；不再把此前终端失联时未运行检查写成当前状态。
