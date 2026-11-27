# 原标量全厚支撑的软件入口与生产接续

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**数学依据 [R1050](../results/R1050-original-scalar-thick-fibers-and-exact-cusp-transfer.md) 已证明；本页所列新软件检查尚待实际回执。没有新生产运行，没有宣称原几何或主目标完成。**

## 1. 原函数中准确的一处替换

新脚本 [original_scalar_base_divisor_support.py](../scripts/original_scalar_base_divisor_support.py) 保存原 geometry callable，复制该函数的完整源码，只改函数名及内部唯一的支撑调用。将两处名称改回后，字节逐一相同；原上下文、所有七个实际映射、两图、完整零极点、W/反射搬运、whole ZD/PN/unit-sum、108尖点与54分歧点的所有门均保。生产必须在 triangular producer 捕获几何 callable 前绑定，或精确更新其已经捕获的同一个别名。

每次 geometry 调用创建独立 session；同一 session 中，只对相同 engine、环、常数域、chart及不可约 $\pi$ 复用完整 $A/\pi A$。原实际 $A/\pi^mA$ 始终保全部 $m$ 层，未用 reduced support 替代。

每个目标仍先执行原 infinity boundary（需要时），核实际完整 HNF 为 $hI$、整个 determinant 为 $h^N$、全长度为 $N\deg h$。每个 $\pi$ 仍执行原 primary_block 并核完整 HNF 为 $\pi^mI$。原 complete Frobenius、非约化幂等分量、真实 residue field/原常数嵌入、完整 maximal HNF、registry继续执行；局部全长为 $m\deg(\pi)d_i$，重数为 $md_i/f_i$，所有分量的全长必须返回原 primary 和目标长度。

返回只提供调用者实际消费的 point 和 multiplicity，另附全长及诚实滤过回执。**不提供或伪造** full_local_primary_ideal、全厚局部 projector HNF 或旧 projector 运行成功记录。需要这些对象的通用分解接口完全保留。

## 2. 有必要的软件核验及精确来源

[新 checker](../scripts/check-original-scalar-base-divisor-support.py) 使用完整自由9维变形代数
$$
F=(x-\eta t)^2(x-\eta t-1)^3((x-\eta t)^2-\eta)^2+t(t-1)(x-\eta t),
$$
其中 $\eta$ 是 $\mathbf F_{29^2}$ 的乘法生成元。$t=0,1$ 时三个实际局部分量维数为2、3、4，残域次数为1、1、2；后者是真正二次扩张。比较对象是未改的原通用厚分解，不是另造的预期点表。

覆盖厚度1、2、3、双base prime、完整infinity boundary、单位理想、同一点对象复用，以及调用者修改返回字典后再次返回。每次比较全maximal HNF、所有原ambient坐标的剩余域值、完整常数幂基、全部厚局部长和multiplicity。另用行列式及总长度相同、实际HNF不同的输入，验证必须在看纤维前拒绝；重叠倒数图必须先取原边界。

固定软件 selector 增加第三个已知 kind，不接受任意脚本路径。去掉新分支后全文等于已发布入口；两个已PASS分支及default正文不改。请求列齐新helper完整依赖并含selector/checker，共22文件。

| 文件 | SHA256 |
| --- | --- |
| helper | c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a |
| checker | 3dd124a953a0a5dc160dd35a3a6ef6a04af11cf0231a947b32053cec40af297c |
| selector | d585a2c584166fe71079ef6f808ef74f4331f0cacfe98e384279cc97a37fdb35 |
| request | e975abf27099a035553cf5b881e8b4d4c20ef2735eb6620ec219a302b6a7df8c |

本次只触发既有公开软件workflow，Sage10.6固定镜像、只读source挂载、network none、420秒内门和10分钟job门。AST及实际数学软件核验都只在公开Actions。脚本不生成持久结果、日志缓存或artifact。

## 3. 新生产接入的明确未付项

v12先前真实终态见[完整记录](2026-11-27-v12-terminal-and-captured-return-binding.md)。本次不会重复同一生产输入。后继须同时采用已实际PASS的captured-return最小绑定和同商current-square复用，并完成本专用支撑的真实核验。

旧 projector producer 末尾有“确实使用过完整projector”的实现性断言；原geometry曾调用它24次。专用支撑将省掉这里未被调用者消费的局部projector，不能用测试夹具填生产records，更不能把未执行的旧projector标成PASS。新生产副本必须核本次实际完整scalar-filtration回执，保所有原数学终点并如实区分所用方法。原一般分解接口及其原完整返回门不动。

旧24个maximal返回至厚局部分量返回的区间合计10082.829秒。这只定位旧运行的主要成本，不保证新运行总时长。所有四次完整交、一般Artinian Norm、原完整 $18\times9$、两char0输入pins与29/2453/64/minimal均保；有限影子即使通过，也不支付真正无穷$p$的通常全$\Sha$主门。


## 4. 第一次软件执行的真实失败与唯一修正

run46079094064/job140773624197/source0002ceca5ad8fa084d450fcaf7064def524d9d6b在2026-11-27 22:51:57UTC失败，exit1。固定selector的AST及源hash通过；第一夹具的原通用分解已返回，新helper在完整small fiber的Frobenius/primitive-idempotents之后，执行 snapshot=idempotents.copy() 时出现 AttributeError：Sage的 Matrix_generic_dense 没有该方法。此运行没有PASS回执，未执行原几何。

job日志19829B，SHA256 838d805d45cde103ba176f178728d461777c5d937e8ee8ce1f5474a9ef51a4ec；不保存日志。失败源helper/check为 b392e988… / d66165c8…，原完整hash在前次提交可追溯。

修正只在helper和checker各导入标准 copy.copy，将快照及故意非scalar夹具的同类复制改用此接口；不删任何门、行、比较或数学步骤。上表更新为实际第二次请求的四份源码。固定selector/request同时换成新hash并再次触发公开核验，后续实际回执仍待消费。
