# R210 完整帽条件的保守连续高度引导及全部参数链

2026-11-13。父几何源 SHA27c3a30c…60b7；新工厂为
scripts/fd2d-R210-amplitude-height-allowance-geometric-guide.cjs::createR210AmplitudeGeometryProvider。
它消费已完成的 results/R210-extended-throat-caps-for-far-radius-core-protrusions.md，
对应真实新帽，不是保留旧R204帽却删除高度条件。

## 连续蕴含

取柱半径 r=sqrt(Xx²+Xy²)，固定
δ=.0195、r0=.52、r1=.54，令
χ(r)=0(r≤r0)、χ(r)=1(r≥r1)，中间用
S5(t)=t³(10−15t+6t²)，t=(r−r0)/(r1−r0)。
于是χ是全域C²、0≤χ≤1；在轴附近恒零，径向范数在轴的奇性不传入χ。

新两条高度约束为
h±=±Xz−Z−δχ(r)≤0。
如果它们在整个核上成立，则|z|≤Z+.0195<Z+1/50；
又若|z|>Z，必有χ(r)>0，从而r>.52>257/500。
因此准确满足R210的两个新的全域前提。有限数值目标零只支付取样点，不冒连续前提；末值须由严格全域包围消费。原R205整个尾/补盘已在|z|≤Z内，新条件只可能约束prefix。guide采用cutWindow[.41,.60]，也严格落R210实际Z∈[.40,.61]，留出端窗和余项空间。

源码允许显式更小δ以及更大的r0；始终δ≤.0195、r0≥.52、r1>r0。这里所有有限数值常量按保存的binary64理解，其与准确cap偏移1/50、准确远径阈257/500的余量远大于舍入。最终帽仍按R210准确参数定义。

## 完整微分与有限normal

当r0<r<r1，
χ_r=30t²(1−t)²/(r1−r0)，两外区为0。
任意真实参数p满足
d h± = ±dXz − dZ − δ χ_r (Xx dXx+Xy dXy)/r。
χ_r=0时直接用零，避免轴上0除。dZ对cut列是1，其余0；所有dX来自完整R201/R205位置列，包括实际A、rho、高度、正余弦及mean-phase链。

七条R203约束的其余五条、样本、权重和normal归并顺序不变。高度hinge在精确阈值采用原零广义斜率。新source把旧rawHeightExcess与扣除allowance后的maxAdjustedHeightExcess分别记录，不能把允许的正raw excess误报为新约束失败。definition显式标记R210新帽、完整height链和未付连续证书。原物理field/metric/曲率不因改罚项改变，但目标函数明确改变，必须重新完整baseline/normal及真实Armijo。

## 实际验证

V8真6.861秒完成J3/K2/N32、35完整参数、23324条几何行。完整混合JVP包含cut/A/rho/phase全部列；中心差分relative L2=1.428243765918592e−8。d·g与r·Jd的相对差0，dᵀHd与|Jd|²的相对差2.09097561303178e−16。
另在r=.50/.52/.53/.54/.56、上下两种高度符号真实核过完整δχ/r链，最大差4.936523412268912e−12；内部过渡点的径向导数非零，未只测常数区。

检查源 scripts/fd2d-check-R210-height-allowance-guide.cjs，
完整输入/方向/规则/结果在 notes/2026-11-13-fd2d-R210-height-allowance-guide-check.json。
实际是纯V8，无OS进程/退出；CLI仅编译，没有大normal或LM步骤。
先前R210第4态finite screen通过新高度/远径条件，仍未支付原metric、width、held、wholecore reach或强目标；此guide也不替它们支付。
