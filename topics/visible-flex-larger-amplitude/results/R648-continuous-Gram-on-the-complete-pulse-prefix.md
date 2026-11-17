# R648 — 固定 pulse 前缀全部 818 胞的连续 Gram 认证

**已证明。** 在 R641 已声明的 IEEE binary64 向外舍入模型下，同一固定 pulse 候选的整个 $[0,1]\times S^1$ 满足

$$\boxed{\ \|g^{-1/2}(\widehat F^*e-g)g^{-1/2}\|_{\rm op}
 <4.94\times10^{-7}<10^{-6}.\ }$$

这是全部818个胞元、全部径向位置与全部角度的连续界，不是有限采样最大值。原固定819片计划已真实完成，失败0、异常0；没有改变候选或增加后验网格。

## 1. 固定对象与实际结论

对象仍为 R638/R641/R642 的同一 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72` 完整前缀：M320、819 个保存节点、818 个共同五次胞元，径向域 $[0,1]$。全部保存的 $F,F_s,F_{ss}$ 按准确 binary 数解释；不以 M320 RHS 重生左侧 M112 二 jet。构造角数始终为 4096，中心为 $c=(0,0,Z_0)$，$b$ 是同 4096 角节点的准确有限速度均值，$\lambda=a/b$，$G=c+\lambda(F-c)$。$\widehat F$ 是 R638 同一 $q_{4096}$ 所定义的材料角拉回。

$a$ 保持原精确标量定义：旧节点准确有理 Hermite、从准确 $.99$ 节点运输至 $.995$ 的解析弧、再接已声明的精确 pulse 曲率积分。浮点 Profile/有限 Gauss 值不是另一个目标 $g$。本次 $\rho$ 来自同一保存 core；物理角中的目标为 $g=ds^2+a(s)^2\rho(\theta)^2d\theta^2$，其共同材料角写法为 $ds^2+a(s)^2d\Theta^2$。

完整上界的实际 binary64 报告值为 `4.936514796884016e-7`，最坏在胞817的 `before` 片；其范围为

$$[2251764629313133/2251799813685248,\ 1-5/2^{60}].$$

该片三项有方向预算为 $|e_r|\le1.829489\times10^{-7}$、$|e_\theta|\le3.547344\times10^{-7}$、$|f|\le2.077545\times10^{-7}$（此处均向上取整）。正文框中的 $4.94\times10^{-7}$ 也经准确有理比较向上放宽；取原报告未取整三项代入 R641 的二维对称矩阵算子公式，得到上述实际报告值。最后极短 `after` 片实际上界为 `4.926726545234174e-7`。

全域因此也满足 $(1-4.94\times10^{-7})g\preceq\widehat F^*e\preceq(1+4.94\times10^{-7})g$。

## 2. 完整覆盖证明

冻结原计划按准确 binary 径向节点形成闭区间：481 个旧 quintic 胞、17 个解析胞、319 个完整第一 pulse 胞，最后第817胞沿

$$s_* = \operatorname{binary}(.995)+\operatorname{binary}(.005)
       =1-5/2^{60}$$

分为两个闭片。共819个调用；相邻端点准确相等，首端0、末端1，两个末片的并恰为原末胞。没有用显示为1.0的浮点加法吞掉后一极短片。

每片调用同一已刊 d066 引擎。R641 的径向 Bernstein 凸包、角向二阶覆盖、全部非线性余项、实际 Gram 抵消与向外舍入在每片支付；旧标量使用准确五次多项式而非 pulse 的三次 Taylor 误差。最大物理角频率2688小于证明网格16384的 Nyquist8192。旧五次标量使某些径向次数增至14，引擎按真实多项式次数做 Bernstein 变换，不把第一 pulse 段的次数12假设挪到全域。构造 $q_{4096}$ 的 Nyquist 单余弦仍保其正确两半系数。

所有819份完整报告的覆盖范围/参数/同场身份均已核销，每份给出该闭片全部径向/角位置的

$$\|g^{-1/2}(\widehat F^*e-g)g^{-1/2}\|_{\rm op}\le \varepsilon_i.$$

因此闭覆盖有限并给全域上界 $\max_i\varepsilon_i$。公共节点的值/一阶导数来自同一共同五次场，R638 已给全域 C² 坐标，故交界处也属于这些闭区间的实际共同映射，无未支付的接缝或角域空隙。这一合并不是从有限采样最大值推测连续最大值。

## 3. 执行与来源

原全批源7bcbb9...的计划SHA为9b42d8cc8460318f83335f623ae762ad520678ac65f4a664137571c74c00b11d。原worker没有终态而停止，实际保存0...709共710份完整报告。已刊e024恢复入口逐份验证原计划范围/参数/源/输入身份，原样复用710份，只执行余下109个原计划槽。首缺710的旧调用是否已经开始未知，保持未决标记；旧完整报告从未重算或覆盖。

恢复清单SHA b7f56ca5c0a47dde3ff2b7b4e695b7721aa20db2420ab2a4dbce4aa8708971cb；恢复源SHA e024c7aa3d011090d79d00f8db97f931520e0b0abbacf9e24a7487cb71964627。新调用直接用原 d066 核，不用旧driver缓存；数学函数/参数相同，不声称相同计时。证明角16384、构造角4096、标量积分4096段均无后验改变。

本次唯一恢复 session 为57122，于19:13 UTC实际 exit0。终态计数为819已完成、0剩余、0失败、0异常、`fatal=null`；其中710份原样复用、109次新调用，覆盖818个不同原胞。恢复用时1360.232457秒，峰值RSS244888KiB；这不是宣称单次从空目录计算全部819片的耗时。

| 本次实际证据 | SHA256 |
|---|---|
| 完整恢复终态 `parallel-pulse-gram-fixed-recovery/result.json` | `df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb` |
| 简短终态摘要 `parallel-model-pulse-full-gram-terminal-summary.json` | `5e8faeb264315283ff0b749c38e9b75ace5bd0dfd146fb79f2013779691ab308` |
| 胞817 before | `b42fc9355cc1634ab5841ea185936091516e313eb1ce7f4dd724a3a14619d52f` |
| 胞817 after | `f137ec00250568821427e3bbcf134ddda8ab119bf5f091ddd4b94e81d53a7b37` |
| 完整逐call日志 | `0d030d92831e8d81bafbdb5857bacc10c2e7cb6a8f6139e23b91b676c37ad102` |

从空目录完整复现时，先按[实际完整pulse候选](../notes/2026-11-17-parallel-numerical-pulse-arclength-prefix.md)的配方重建相同输入，再用已刊[固定全批源](../notes/2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py)。T为题目录，WORK为仓库外目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 "$T/notes/2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py" \
 --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
 --engine "$T/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py" \
 --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
 --scalar-oracle "$T/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
 --outdir "$WORK/parallel-pulse-gram-full-fixed-new"
```

本次实际中断续接的准确CLI与完整来源见[恢复说明](../notes/2026-11-17-parallel-model-fixed-certificates-interruption-recovery.md)。直接科学内核仍为d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882，区间算术f512c96c、整数标量oracle babd589d及其完整证明沿[R641](../results/R641-continuous-Gram-certificate-for-one-pulse-cell.md)。报告含计时/路径，重新执行不承诺整份JSON SHA相同；本条SHA识别实际证据，数学输入/参数/运算预算完整保留。输入、原始单片JSON、清单和终态报告仅保留研究仓库外。

## 4. 同一开放前缀族与结论边界

为说明全phase的准确范围，可沿R240取 $\Theta(\theta)=\int_0^\theta\rho$，$\eta_t=\Theta^{-1}(\Theta-t)$（圆上解释），并令

$$F_t(s,\theta)=\mathcal R_t\widehat F(s,\eta_t(\theta)),$$

其中 $\mathcal R_t$ 为绕z轴刚体旋转。因为 $\eta_t^*g=g$，且刚体旋转保持欧氏内积，上述全域误差上界对每个 $t$ 完全相同。R638的C²正坐标及共同五次场给 $t\mapsto F_t$ 的强C²连续性；R642的同场嵌入在此刚体旋转/重参数下保持。这只是带边前缀族。

本次只把同一开放前缀的有限采样/指定胞度量证据升级为全域连续界。R638/R642的同场 C² 与嵌入可以合用；原 R240 材料角平移/刚体旋转产生的带边 phase 族也继承同一度量界。闭合尾帽、固定有内点 H、完整闭面 D、整像 held/反射 E3、全闭面 reach 及 README 第5项的固定度量/参数/t 求解精化仍必须另付。证明网格加密并不等于数值解在固定问题下加密收敛。
