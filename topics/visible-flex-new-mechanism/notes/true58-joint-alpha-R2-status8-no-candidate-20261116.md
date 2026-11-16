# 真正58：共同反射幅度与R2新问题返回status8，无候选闭账

日期：2026-11-16。**读取唯一已完成公开Actions的原始输出；没有在本地重算几何、导数、约束、优化或数学积分。**

本任务完成了一个新的19变量共同问题的实际观察。SciPy SLSQP返回status8、success=false，原消息为“Positive directional derivative for linesearch”。原raw19与全部后端字段已保留；没有合格舍入候选、全body预测、actual pair或59。该局部返回不是整条射线、完整51控制或主问题的准确不可行证书。原两网实际58保持不变。

## 1. 唯一来源、规则与读出

- [公开run43880150928](https://github.com/Rogerhu12/math-research-public/actions/runs/43880150928)，research **133343574077**，report **133344023593**；两job最终均success。
- workflow：`.github/workflows/visible-true58-joint-alpha-r2.yml`；source **25c98ff4198cfc10552ddcd0dc9307110a6be8de**。
- research作业13:53:30→13:54:16 UTC；其原日志 **6343887 bytes**，SHA256 **06dbe91e2fd93053904e27784be35e4856a137bf4d800f8713fbad3f2334541d**。
- 唯一request `computations/request-true58-joint-alpha-r2.json`：**71258 bytes**，SHA256 **383d0d45ecd6c617385eae3a4979856db997beb2b1c76029b7e98b7702c037d3**，326个源hash绑定。
- 只读report原日志 **1123024 UTF-8 bytes**，SHA256 **ea7cd279bae41e3548cb8f5b1d963132de4ee26caa7e46e6224d9cf6c68aa33d**。observer **2.331433289000003秒**独立于全部科学账；原research日志读一次。
- report解出 **10条记录、0 parse errors、0未解析记录**，projection level0、semantic incomplete=false。大数组只在原stdout保值；report按原元数据/节点指纹选读，不能把元数据当新输入数组。NONLINEAR_RESULT全部后端字段确实完整转发。

research实际public pull于13:53:49.766444→13:53:50.148699，已读 **25c98ff4198cfc10552ddcd0dc9307110a6be8de**；private于13:53:52.190972→13:53:52.567854，已读 **d0f167e40e085e3d4508d658c8bf14b9241ebf11**。report实际public pull于13:54:29.862736→13:54:32.379395，已读 **2d24741f9fdd36088ff28184eab749159044f25e**；private于13:54:35.233758→13:54:37.333686，已读 **0e2bfe83d4592292f66350dcf4a102f06ffe235f**。四次均按实际回执检查：public根/题README空diff、private根不变/题无、QUEUE本会话唯一进行中。私有正文不发表。

## 2. 新问题的原范围

[完整设计](true58-joint-alpha-R2-original-box-design-20261116.md)使用原58及已闭[反射R1](true58-reflected-R1-ray-selected-fiber-infeasible-no-candidate-20261116.md)的完整V17和唯一射线Lx/Hxx；不把Hxstar,xstar扩成任意R1二次张量。

物理变量为(α,y17,h)，后端为(α,z17,h)，α∈[1/64,1/2]，固定正尺度y_j=s_j z_j。一次SLSQP，目标min h，h约束完整R1+R2合成物理增量的四倍无穷范数；原172盒、51个受影响坐标及其余121个固定坐标保留。上界从原paid source取
`18014398507545773/281474976710656`，没有恢复旧1/128小域门。

两圈384/768个原角度，共 **7362条新约束**：6912条metric/Q/完整谱行，另450条原物理线性行，其中344盒行、102 norm行及α/h上下界各两行。实际G保原数组，谱三门保中间R≥0；原曲率目标1000/61，metric budget .26600541463999305。

固定半径由原58 CACHE2已有selected metric的径向行141读取：
a=.3399084551031785，准确binary64为6123246366971023/18014398509481984；两份原数组值一致。没有调用metric补值、以Xt范数反推、重算旧frame/Π/J/ordinary或重解BVLS/LP。

新MODEL binding为 **80d8e99e84134de793cdc3ecf6a41938beb42819ba8d2b101b800e56d3f311a8**。新多项式系数原样在MODEL输出；求解后新产生的固定行尺度、首次完整残差/Jac、末次实际完整评价及全部评价/迭代记录在SOLVE_TRACE。

## 3. 唯一初点与真实返回

初点α=1/4，y17取原剩余准确盒中点，再按固定尺度编码/解码；**该次实际解码后的准确盒判定为true**，没有预设所有未来浮点中点都必然通过。初h=31.999999993121197。初线性浮点行最大违约3.552713678800501e−15，初完整缩放违约1；初点没有曲率可行声明。

SLSQP设置固定为maxiter160、ftol1e−9、disp=false；solver时限120秒、最多400完整新评价，总科学scope600秒，均未耗尽。其真实返回：

| 字段 | 原值 |
|---|---:|
| status / success | 8 / false |
| nit / nfev / njev | 16 / 46 / 12 |
| backend elapsed seconds | .5783401090000027 |
| 原raw α | .2934209846189501 |
| 原raw h与fun | 63.99998934237297 |
| 新完整value+解析Jac评价 started / completed / failed | 46 / 46 / 0 |
| 实际迭代callback数 | 12 |
| 同输入完整评价cache hits | 14 |
| 本地solver过程时间 | .6084992910000011秒 |
| solver观察到的超时 | 0 |

nit16和callback12是两个原字段，不能互相改写。约束value调用47、Jac调用12；同输入复用不会额外重做完整收缩。后端raw19的SHA256为 **e0cbb9f4da45f1ac5cf3aefcbd75022e3c7ae827b2228a21bc17e95030e51f20**；解码物理19的SHA256为 **82131d4f5d697757de1b25035640cd39dd4c21af1ca864dfa98e2fad31685519**，二者原数值及每项准确binary64都在NONLINEAR_RESULT，不在Git复制机器向量。

原OptimizeResult全部字段fun、jac、message、multipliers、nfev、nit、njev、status、success、x均保。原multipliers为7362项、58896 bytes，SHA256 **57af2f56d44c269268079d8fa03cce184f95bccc989ee7185d61bb9917df8852**。它们是该SLSQP内部QP近似乘子；没有返回bounds乘子，不补造，没有准确非线性分离证明。此口径按[本次固定SciPy1.17.0官方说明](https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize-slsqp.html)。

## 4. 最后已付完整评价确实仍违反谱门

最后完整评价的输入hash恰与实际后端raw19相同；以下直接读取已保存的每类原单位最小值，没有另评价返回点。

| 原单位约束的最小值 | coarse | fine |
|---|---:|---:|
| metric_minus | .012699114535612527 | .012606304733782707 |
| metric_plus | .03889690861893339 | .03887479260201133 |
| Q lower-bound residual | .049560089659056894 | .049046063520417404 |
| spectral_trace_square | −7.691665448032268 | −7.69247368609058 |
| spectral_determinant_sign | 140.18584105104202 | 140.18572433421147 |
| spectral_determinant_square | −114413.81398399523 | −115012.2181772776 |
| Qcross minimum | .7835546750190638 | .7830406488804244 |
| actual G minimum | .9999999999999993 | .9999999999999993 |

最后完整缩放违约 **.2445904937714127**；原线性行最大违约 **.00005137100275298678**。初/末原7362×19解析Jac的hash分别为b19fb9fe1e2523caeda7504af8d601fc0317dd3f263335c28ca30330dfaa686f及e4eca439183b8f1e6c7f7ac62d335d909d00afd02160b4522db4a4482186f484；每份1119024 bytes，属于该次科学评价。

这些是新有限多项式约束值，**不是**未平方全body曲率或actual14门。status8已使后端资格失败，因此没有构造准确舍入168/172候选，也没有进入原单位候选过滤、固定metric/首jets绑定、全body预测或actual。不能在事后把某个callback点提升成59，不能从此表发明全body κ值。

## 5. 费用原账与关闭

FINAL_CLOCK在大MODEL、SOLVE_TRACE和COMPLETE输出/flush之后采样。其原值为：

| 成本项 | 原计数／时间 |
|---|---:|
| 新联合模型 | 1 |
| 新联合SLSQP会话 | 1 |
| 新fixed metric / paid first-jet bindings | 0 / 0 |
| 全body非线性候选预测 | 0 |
| actual trial pairs / full values | 0 / 0 |
| 当前58 ordinary / 参数J重放 | 0 / 0 |
| 新开发调用 | 0 |
| 本任务科学时间 | **19.9540876秒** |
| 前序已闭科学时间 | 2882.412483226秒 |
| 相关累计科学时间 | **2902.366570826秒** |
| 相关累计完整取值 | **147** |
| 观察到的总超时 | 0 |

model事件.05934976900000066秒、solver事件.6087249650000004秒均嵌在终账内，不能再相加。process_seconds=19.954150823999996是另外一个过程采样，不能替代或叠加正式科学时间。剩余580.0459124秒随本次观察关闭，不延长或重启这个共同α实例。

COMPLETE状态为complete-true58-joint-alpha-r2-observation，new_acceptances=0；actual未调用的原因为“the one joint alpha/R2 local solver returned no qualified rounded candidate”。report success、research success及COMPLETE均不覆盖这条原科学结果。

## 6. 原stdout记录的准确身份

以下身份均指原JSON加一个LF；机器payload继续只留原Actions stdout／临时runner，没有Git、artifact、Release或cache上传。

| tag | bytes | SHA256 |
|---|---:|---|
| PUBLIC_PULL | 1485 | `2f006f1a589889cdc70aca222ddcd67cff7242695f2b76167e3fd86f97617d06` |
| PRIVATE_PULL | 584 | `5b3b70362c32ca0a50e68266f37f03baf0ac0ca80443f9f3816bbf3cf4e6f083` |
| REQUEST | 3468 | `d9fbdb0235bbc54d54060c2d36175c40af18fa69e65ebdd0a14e8531adcb5f91` |
| INPUT | 225480 | `cc905cd2b31142c7758c31eabe77c22efee51d6f6ef8c2d1df286279d3104d10` |
| MODEL | 1530371 | `20f225f7b8101bb0732d9134c1af1c7b58fa5f242449725e979239e6c82edd90` |
| NONLINEAR_RESULT | 67886 | `a2f2db970ceffe1be4587e035873533dad0fec49eb48f12476f5b420f7a78320` |
| SOLVE_TRACE | 4206744 | `39cd015c5c85fd1ad37bc494a1986f220ad5e0eaeccc1fe9fc3ba8c83563403c` |
| RING_SOLUTION | 2827 | `f0d48ebb372de17a8e2450cf11e1b2bf2ed649d9984f113dad5e1bb23ee63932` |
| COMPLETE | 182315 | `293424d38ad60946773491574af45e6bfdc6f4b17d49344fb1442eb231811203` |
| FINAL_CLOCK | 4998 | `76b7397f0ae2f845dce969c75f1e32f511257b3a895dd299e273b35a0afa3dac` |

## 7. 该子问题完成后的继续方向

该任务已取得并公布真实局部返回与完整成本，当前实际点仍为58。它没有产生准确整射线不可行证书；旧纯R2 LP、旧3/8纤维LP及本次共同α会话均不重开。

下一具体问题回到[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)原51控制：在同一固定R0环态中释放射线以外的R1方向，并与完整R2共同处理原172盒。任意R1的Z17/L17及二次交互若尚未付出，必须由一个明确新科学scope取得；不能从单一Hxstar,xstar冒充全张量。若需R0亦须完整当前值、frame/Π和实际G的新模型。代码来源、必要新数组和实际全body延拓先纸面明确，所有新执行仍只用本公开Actions。

主README的同g全时连续族、完整metric精化、嵌入/reach及宏观位移门全未支付。有限环模型、局部求解失败或已有两网58均不替代这些门。
