# 真正58：完整168维全body与后缀的共同非线性问题

日期：2026-11-16。**新问题尚未执行，当前实际接受点仍为58。** 前一[full62原观察](true58-full62-whole-suffix-successful-backend-strict-metric-failure-20261116.md)已经闭账：SLSQP原status=0/success=true，但fine metric严格失败，0完整预测/actual。它的返回只作未接受原观察；本范围从唯一true58起步，不延长原范围、不把旧raw向量作为初点，也不改判旧失败。

## 1. 这一问题改变什么

full62只开放后缀上的62个真实独立方向，不能约束其变化在整个body造成的全部原门费用。本范围使用原完整168维场，在同一个rounded168候选上联合处理：

- 原永久enriched reference下，真正58冻结的两网全部selected行：coarse 4454、fine 4549，原pool版本15/14；保原11种行及其原顺序、数值尺度和硬门。
- 原s≥153/200的21径向行139…159、完整384/768角网：所有两metric行及四个未平方PSD行，保实际G、法向、形算子及共同K。
- 原完整172物理盒、完整真实物理增量范数、K/h四个边界。

不是只保活跃行、只保曲率行或把height/shape/mirror行移除。后缀的其余106个独立方向二jets准确为零，只是一条局部支持结论；它们在原body中全部开放，必须进入共同模型。q153…156也在body中保持真实自由。

固定g/b0、原材料参数、完整core/caps、168→172准确null-height图、永久reference、全部原14actual门、pool身份和连续主门均不变。K是后缀曲率epigraph，不能称全body曲率达到K，也不能称连续或非局部reach已经支付。

## 2. 唯一初点与完整准确物理映射

后端为(z168,K,h)，共170变量；初值z=0、K=58、h=0。独立增量图为原坐标中的E=(1/4)I。每个后端binary64先按准确有理数解释，实际候选按照

q_i = RN(q58_i + z_i/4)

逐独立坐标作一次binary64舍入，再调用原field.full_coefficients(q168,exact=True)。九个依赖物理高度始终保原准确线性关系，不作九次各自舍入。完整P172×168是原准确affine物理图与E的复合；172个物理行均有真实非零控制。

未舍入physical58+Pz的线性门、一次独立舍入后的准确172盒和准确norm终门分别记录。范数为h≥4·max|physical172−physical58|，包含全部耦合物理行，不能换成独立z的最大模。344条原盒、344条norm和K/h四界共692线性行。保原向内binary64上下界；最终准确门失败时不夹坐标、不抬h、不修返回。

K在[1000/61,58]，目标K+h/1000000。hmax保18014398507545773/281474976710656作为本次明确的有限限制。旧推导仅涉及旧51行；此处不声称该hmax覆盖全部168维原物理盒，也不从旧证明推出新全盒充分性。

## 3. 原门与内部metric余量

原最低接受下降为准确1/10000000，原科学程序先按既定binary64次序得到

metric_budget = SOURCE_ETA - float(Fraction("1/10000000")),

其中SOURCE_ETA=.26600541463999305，原budget=.26600531463999305。这个原终门不放松。

本新求解器在原body selected metric行和全部后缀metric行中，使用额外准确1/100000000的内部余量。其实际binary64值只在本公开科学钟内按

float(Fraction.from_float(metric_budget) - Fraction("1/100000000"))

形成并原样报告。SLSQP及scaled residual使用这个更严的内部预算；候选的unsmoothed全域eta和后缀eta准确比较原budget。内部margin不给原终门添加容差，也不把内部预算重新当成另一个要求逐位贴边通过的终门。

selected body保原全局硬曲率cap58。后缀21行使用共享K，但全body原14门仍按原定义。SLSQP ftol=1e−9只是后端选项，不授严格metric容差，不替代准确盒或norm。

原selected总9003行、后缀145152行，非线性合154155；加线性692，总154847行，J有170列。每个后端请求对应同一候选及当前K/h。数值solved、原返回success、necessary qualification、canonical prediction和actual acceptance分别记录。

## 4. 同一个全域几何及全部新增费用

本模型不把旧true57固定仿射交换器的alpha=1或1/128比例假设搬来。使用原168场低层公式，从已付q_R scalar输入与原basis开始，新增完整径向、角向、body和height依赖；它是新全域非线性模型。

prefix102确存原full scalar，以及suffix数据；true58确存完整U/T/e/f及两网selected二jets。本次一次绑定两份literal first-jet数组及一份literal fixed metric数组，不重放原ordinary全grid field.geometry作为基础。原fixed metric直接绑定，不重新调用metric构造器。基准frame/Π、所需新primitive、缺失二jets和导数均是本次科学工作，不称免费恢复。

新增准备按原定义完成最后三径向样条、原Q角基、body径向与全部五个null-height及body-height primitive/b/b_s；原前六径向与确存角basis只按身份绑定。每个实际q共享一次完整scalar/frame/角primitive链，body和suffix不能分别偷用旧点几何。

完整U/T/e/f按literal paid true58一jets加原场真实增量得到。selected X按paid58 selected X加同一Π_N切向primitive及准确null-height增量得到，其余selected二jets和全部suffix二jets来自同一原链。初始selected二jets按literal paid true58恢复；初始缺失suffix二jets及所有新frame/Π/J明确计费。

这个增量模型在实数数学上是原场；其binary64结合顺序不承诺与canonical全body逐位同一。因此即使同点necessary全域eta/selected/suffix等门合格，仍只允许一次原canonical预测及其后至多一次原actual pair。两者都使用同一个原返回rounded168，禁止换候选、回调升格或后处理。

全部新基准frame/Π、新selected二jets、共享全域值、后缀完整II/PSD、完整168导数及失败工作进入本scope。ordinary source actual调用数与新模型完整点值/J数独立报告；前者为0并不意味着新科学为0。缓存只保当前q的实际大数组；淘汰后重访必真实重算并计费。K无关几何/导数与最终K谱J分开绑定，初末元数据不伪作返回点J。

## 5. 输入：五份原日志，旧数组边界保留

| 原输入 | run / research job | 本次确切用途 |
|---|---|---|
| 真正58 | 43859882465 / 133273598120 | 原q、门、pool和确存U/T/e/f及selected二jets |
| 永久55 | 43832870561 / 133182173190 | 原永久reference constructor，不作为58导数 |
| free36 | 43884276617 / 133358065602 | 原basis、q_R与已闭记录，不复用旧34控制图 |
| prefix102 | 43891282963 / 133382836465 | 确存完整scalar与21行后缀数据，不冒全域派生数组 |
| full62 | 43916013327 / 133470222034 | 仅BODY_SOLUTION、COMPLETE、FINAL_CLOCK核原失败及费用 |

full62原job log为3395530B / c436813e829af5c1c2c7f636d69a199eba4f071395a728abd82995c1f34c251f。三个输入JSON+LF分别为：

- BODY_SOLUTION：103421B / 7d824a6b892ad75c69c45c890240e0cd8acadc869e6d40b5a01a8b519626d17b。
- COMPLETE：277795B / f5fd3c226627321f9676688d65ca526d3c3e61ab9cf2a1299bdbcdc5318ea865。
- FINAL_CLOCK：6684B / 423abbc12eecb6c900e797a58a7d016fa9782e85d31f39cf93620f56b08b06cf。

父scope新115.53521002299999秒、累计3757.97482037秒/147原full值已经闭。原strict fine metric false、0预测/actual原样保留。其大MODEL/J数组只有bindings，原末J属value69而返回属value70；都不能当本次免费值/J。full51钟停无返回、whole34原缺失正文也不补造或重跑恢复。

新request逐字保382个旧源hash，再绑定本次8个Python源、workflow、设计与模型合同、父full62 request和闭账note，共13新增、395来源。request自身不自引用hash，其准确bytes/hash从原REQUEST记录。只读取这五份指定原日志；input读取、解码、构造器恢复和失败也在科研钟内。

## 6. 一次正式公开范围

POLICY=true58-joint168-body-suffix-v1。

| 项目 | 本范围上限或定义 |
|---|---|
| 整个科学钟 | 1800秒，含导入、输入、所有新工作及输出 |
| solver钟 | 1200秒且不超过实际剩余全钟 |
| solver sessions | 1，无重启、无备用候选 |
| SLSQP | maxiter240、ftol1e−9、disp=false |
| 新实际q168 | 至多480个不同真实字节态；淘汰重算另计实际工作 |
| 后端输入 | 至多960个不同literal backend170，含同q不同K/h |
| 初点 | 唯一true58的z0/K58/h0 |
| first-jet/fixed metric binding | 2 / 1，各一次绑定确存正文 |
| 原canonical全body预测 | 至多1，仅原成功返回且necessary gates合格后 |
| 原actual | 至多1 pair、2 grid values |
| 祖科学费用 | 3757.97482037秒 / 147原full值 |
| 科学stdout | 至多96MiB，逐原记录bytes/SHA256 |
| 只读观察 | 单独记录wall时间，不重复加入生产科学费 |

一次模型构造、一次新输入准备、一次求解；初始缩放J与实际后端请求J均计费。没有单独开发、preflight、旧秩、冻结校准或报告补算任务。失败、钟超额、真实重复请求与缓存淘汰都记录；余额关闭，不以新编号重开同一原范围。

只保同过程RAM中的当前大数组，不写科学磁盘payload，不向Git、artifact、Release或cache上传。array binding注明values_saved=false，不承诺未来免费输入。原实际raw170、每一个OptimizeResult字段、实际小q168/physical172、有序状态、失败和费用完整输出；大J或几何只输出实际元数据、身份与原摘要，不能填零、重建缺失值或为报告再求一次J。

## 7. 原返回后的严格顺序与闭账

若SLSQP没有原始返回，保存实际partial与费用，不取最后callback作为候选。若返回，先保存实际raw170及全部原字段，再按同点的原成功标志、全selected门、全后缀原metric/PSD/direct-curvature/area、全域原eta及准确172盒/norm等条件报告qualification。scaled residual通过不能掩盖严格原metric失败。

只有合格返回才作一次原canonical全body预测；完整预测全部原门合格才用同一个rounded168作一次原actual pair。原14门/严格下降全部通过才能记实际59。否则保持58，关闭本scope，原返回的每一个失败原样保留。任何有限grid通过也不授连续全时间reach、同g精化或README完成。

## 8. 运行、规则与发布边界

本次所有数值/符号/科学执行只由公开Rogerhu12/math-research-public的GitHub Actions承担。研究job与完成后只读report job各先执行真正public/private git pull，按所读root/topic README的差异立即应用，输出准确读SHA；private正文不外传，QUEUE仍为本会话唯一进行中。MR_TOKEN只用于private规则同步并在进入科学和观察进程前清除。

当前本地执行环境不可用，源和MD按根§8以每件小于100000B的小UTF8接口发布；expected-head、force=false，失败先取新head再顺序重试，API更新不冒原生pull/rebase。workflow位于topic外仅因本题公开Actions所需，理由同时记log。真实双仓pull和规则回执写入HANDOFF，至少每小时继续；若README变更只读新diff并立刻照新规则做。

同一scope启动后不读运行中的科学stdout。完成后读取原research记录与只读report，核全部记录身份/缺失边界、保存原观察与费用，写完结论立即推送并接open下一实际子问题。运行时长或余额不是主课题停下的理由。
