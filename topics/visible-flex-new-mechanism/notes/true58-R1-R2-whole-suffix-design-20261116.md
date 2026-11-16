# 真正58后继：原R0平面内R1/R2的完整后缀共同minimax

日期：2026-11-16。新科学范围设计；所有实际数值/导数/求解仅在本公开仓库GitHub Actions执行。此稿和新源码不表示已经运行或已有新接受点。

## 1. 已观察的障碍与本次问题

[固定prefix102的实际闭账](true58-prefix102-fixed-suffix-metric-failure-zero-solver-20261116.md)已经表明：未接受free36候选的s≥.765后缀η粗.5451750803995812/细.5451744553138167超本次metric预算.26600531463999305；该域曲率约50.65482小于58、原PSD/area门通过。原102前缀在这里二jets准确为零，因此只动102不能修该固定后缀。本次不重启它，也不重解旧的单环问题。

本次在同一个原R0平面中释放R1/R2的34方向，将一个s=.78环的问题改成**s≥153/200的完整21径向后缀**。两张原完整角网各384/768个角都保留，所有径向/角向点共同进入metric及曲率约束。即使这一步成功，也只授后缀数值合格；全body原预测及14actual、连续主门仍分别支付。

当前唯一接受点是58；其η最大.26600541463999305、κ最大57.9997782607127、两网14门及准确172盒通过。fixed g/b0、永久参考、原角网/径向网、原物理盒、所有容差/floor与实际验收定义不换。

## 2. 四份原stdout及真正可复用的数据

| 来源 | run / research job | source | 需要的原记录 |
|---|---|---|---|
| 真正58 | 43859882465 /133273598120 | 0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881 | COMPLETE、CACHE2、FINAL_CLOCK |
| 永久55 | 43832870561 /133182173190 | 23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db | 仅constructor COMPLETE |
| 自由36 | 43884276617 /133358065602 | 7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c | MODEL、RING_SOLUTION、COMPLETE、FINAL_CLOCK |
| prefix102 | 43891282963 /133382836465 | 30136a383796ea3a255c00e10e482c358b4e822b | MODEL、COMPLETE、FINAL_CLOCK |

四份body各读取一次，run/job/source/raw-log与JSON+LF字节/哈希逐项绑定，不重新调用其旧模型、优化器、frame、Π或实际验收。

free36 MODEL的JSON+LF为25755139B / 89cc1b6ed0eedaaf18d454206f98831fb3decb8d401212493420bf80deb9ad31，含原准确34坐标嵌入。原RING_SOLUTION含未舍入raw36和准确一次舍入候选q_R。

prefix102 MODEL的JSON+LF为42929879B / 64d1fdd63d339b102d0ce73f92e1f042110bc2fbe11ce95a92ec59d443663921。它确实保存：

- 全160径向两角网q_R的u/v value、s、ss、theta四scalar字段；
- 固定a/a_s/a_ss及b/b_s，原径向/角网和前102的径向/角基；
- 两网完整21径向后缀的T、metric_e/f/eta、Xs/Xss/Xst/Xt/Xtt、两主曲率、normal area、四PSD行；
- 该准备点和后缀的完整summary、身份、费用及原行ID。

它没有保存全域派生frame/Π/curvature大数组，没有任何Jac。既有scalar inputs不被冒称这些未存派生数组。新任务只按已保存字段复用，缺失的末3径向基、非线性I/II/导数或新点值另付。

## 3. 准确R0平面、一次舍入和唯一初点

令q58为原准确binary64接受点，z_R为free36原返回前34个后端变量，P为其同一个原准确线性嵌入（含原后端坐标缩放）。新控制δz仍为34个后端变量。候选定义为：

`q(δz)=RN(q58 + P (Q(z_R)+Q(δz)))`。

每个后端binary64输入先解释成准确有理，整个线性表达式在准确算术中相加，最后各独立坐标只舍入一次。原172物理系数也由同一原准确映射取得并检查原盒。不能以已舍入q_R直接加Pδz冒称保原q58的准确R0平面；q_R自身的舍入残差如实保留，不删掉。

唯一后端初点固定为：

- δz0=−z_R，逐个binary64取负，准确和为零，因此候选恰为q58；
- K0=58；
- norm epigraph h0=0，对应相对q58的零物理步长。

q_R只是已付几何基准。原q_R后缀值直接读缓存，绝不重算；新初点q58的完整后缀值是本次实际求解所需的新查询，单独计数。不能仅根据原全域峰在.4725就假定后缀具有1e−7余量，初始原metric门由这次实际值决定。

这里的h是原物理步长norm的辅助量，**不是**改变几何帽高或另加小信赖半径。

## 4. 唯一新求解问题与全部行

后端36变量为δz34、K、h。一次SLSQP最小化 **K+10⁻⁶h**；准确K区间[1000/61,58]，backend端点按原向内binary64包，h及原norm线性行保持free36的原物理盒语义，不新增小步门或重启phase-I。

非线性部分为每个后缀点的原2个metric行和4个未平方PSD曲率行，总 **145152行**。不只选已知峰，不用孤立角或轴对称曲率公式，不用平方行冒未平方谱门。全部实际I/II和G均由同一个当前候选读取，不把G强设为1。

两网metric预算同一次原要求：

- source η：.26600541463999305；
- 最小原下降：准确1/10000000；
- 本次binary64预算：.26600531463999305。

原完整线性172盒/norm/K/h残差、原row tolerance以及准确172盒/K-h区间另检查。backend norm epigraph的准确有理是否覆盖单独报告，不把容差通过写成精确覆盖，也不因此偷加一个新物理门。

每个新物理点都评价完整后缀两网。Jac在首次显式缩放请求及后端实际请求时构造，保所有34物理方向与K/h列。最终候选必须来自真实成功原返回，先完整保OptimizeResult/raw36，再做准确解码/原盒/原未缩放残差/实际η、PSD、直接κ和area资格门；不能提升未返回callback点。

## 5. 付费增量值、浮点语义与缓存

为了复用已付q_R scalar字段和原角基，新点scalar以q_R字段加上实际一次舍入q−q_R对应的末51系数变化形成。数学上是同一个原场；有限浮点求和次序可能不同于canonical `field.scalar_frame`，必须在binding、输出和结论中明说，不能称为逐bit相同。

因此后缀模型合格只进入外部原全body预测；该预测按同一个真实q168走原canonical链，最后接受仍以原14actual为准。既有q_R点直接返回保存的T/jets/e/f/η/PSD/κ/area；尚未存的导数输入须真实另付。

原末三样条支持之外的径向行保持原已付binary64身份，并同时以其准确有理值比较原准确右端423/500和原BSpline实际binary64右端。满足两者的固定行直接复用T/jets/e/f/η/κ/area及K58的PSD；新frame/Π/物理J只在可变行形成。全部21行仍进入约束，新K的PSD及K列仍按当前K组装，固定行缺失的I/II首次新付后缓存，不用近零阈值代替准确支持。

缓存层级分开：

- 几何值以实际q168字节为键；改变K/h不重新生成同一个frame或Π；
- K无关的物理导数输入按同一q保存，最终PSD/Jac组装仍读当前K；
- 最终Jac键含q字节及K字节，不能把旧K的Jac误用于新K；h只进入固定线性行；
- 大数组只可在同次Actions进程的临时目录作原字节缓存，所有读写时间计入同一范围；没有artifact、Release、Git数据或跨run cache上传。
- 初/末实际值、初/末实际Jac和真正partial保原stdout，重复者只写一次；其它临时中间缓存不承诺为未来免费输入。未填充np.empty内容不输出，不为报表重算。

## 6. 原全body预测和实际接受

只有完整后缀qualified返回点才恢复原58 CACHE2的第一jets及prefix102已付a/a_s/a_ss，进行至多一次原完整两网metric/curvature/area预测。固定metric只作原数组binding，不再调用field.metric取得同一已付数组。

预测必须用同一准确一次舍入q168，原全bodyη下降、四PSD、直接主曲率、regular area及准确盒共同通过，才调用至多一个原actual pair，即两次原ordinary full values。actual完整14门及原学习池顺序照旧，接受后才可称59；新row学习和已算selected jets仅从同一个真实ordinary缓存导出，不重跑。

后缀通过而全body失败就完整记账，保持58并继续相应新前缀问题。后缀后端不成功或返回不合格则0预测/0actual，不把局部优化结果写成全几何不可行。

## 7. 唯一范围与完整费用

新总科学范围 **600秒**，从import/input之前同一monotonic起点计，包含所有原日志读取、恢复、缺失输入、后端、所有新值/J、临时数组IO、异常、失败与输出。

- 一次whole-suffix model build、一次必要input preparation；
- 至多一次SLSQP，180秒solver、120iter、240个不同backend36输入点；实际新q几何点数单列且不超过此数，同q的新K/h仍占backend点但复用已有几何/物理导数，K/h重组及所有实际Jac同钟计费；
- 至多一次原完整body预测；
- 至多一次原actual pair、两次ordinary values；
- 不运行开发/冻结复核/旧optimizer/旧点独立重放。
- 后端限时为非抢占检查；如一次调用越过时钟，真实已用时间与partial必须明报，不改成正常候选。
- FINAL_CLOCK在所有大输出和COMPLETE之后采样，优先于更早时钟；余额在此新范围结束后关闭，不沿旧session加时重启。

祖账完整保 **3047.102915103秒 /147原full values**。其中已付prefix102的一次新完整准备point与0solver/J/actual分别保留，不把它伪称0科学，也不加到原actual累计。新的whole-suffix模型值/J/全body预测另计，只有真正ordinary实际调用才增加原147口径。

原数学stdout上限512MiB；只读report最多读640MiB原log并给8MiB语义输出，任何省略都指回原数组元数据/原record哈希，不能造截断结果或伪造原返回。当前同次临时缓存不是持久产物。

## 8. 来源绑定、规则与发布

新request保全部旧348源hash不变，追加新模块、scope/transfer/actual/audit/report/workflow、此设计、模块合同、原prefix102 request与闭账结论。具体最终字节/SHA均由request manifest固定；request自身在原REQUEST记录中留字节/SHA。

research和report均真实pull public/private并只读根/题README差异，记录已读commit和本会话QUEUE唯一进行中。科学过程在绑定source上执行，private MR_TOKEN在进入科学过程前移除。PAT仅CLI或Actions secret，不写明文。

本次无本地科学执行；源码与参数准备不是验收。README的闭连通C²嵌入、同固定g全时精化、.3D整像位移、固定握持H及全时全域reach仍必须共同支付，后缀优化不能代替主完成。
