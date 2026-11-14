# R133：精确 fold 消去后六窗口完整源的实际计算

**状态：已证明的计算机辅助组件。** 本报告登记公开 Actions
[43642808159 / attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43642808159)
实际完成的六个标量 jet 表及 4377 条源积分。8 个数学门全部通过，
数学 child 返回 0。它证明下列同一源算子的完整上界；不声称这些上界
已经满足强返回、充分 cutoff 或全无限维逆的门。

## 1. 同一对象、证明与真正新计算

使用原真实 $Q_\delta=Q_0+\delta Z$，$|\delta|\le10^{-8}$，
固定物理 $\eta_0$、原根区 $\nu$ 方向及原有全部均值。
非均值输入为 $|j|\ge97$，物理频率 $n=4|j|$；输入密度归一化
$n^{7/6}$，源范数为
$$
H^{-4/3}\longrightarrow
L^2_r(H^{-2/3}\times H^{-2/3}).
$$
这里 $L^2_r$ 使用真实普通径向测度。

所用解析证明为 [C1–15 精确矩阵消去](R133-supplement-exact-fold-matrix-cancellation-and-leading-inverse-defect.md)
与 [N1–12 完整包络及积分复用](R133-supplement-exact-fold-source-envelopes-and-integral-reuse.md)。
尤其真实恒等式为
$$
g_d=Dw_0-\eta h_\phi,\qquad
q_v=v g_d+i\varepsilon v_\phi QK(T)w_0,\qquad
H^{-1}H_D=-i\varepsilon QK(T).
$$
旧代码中相加的幅度费用只是三角上界，不能用来改变本式的精确符号。

本次只新增六个 $G,G_r,G_{r\phi},Q,T$ 标量 jet 包络表，
再按上述恒等式支付 $h,g_d,q_v$ 的完整分量和角导。
旧 6 个 Airy profile、6 个 leading tensor、1328 条矩阵表和
1328 条 moment 表、所有原径向权与正区分窗费用全部复用。
原 target、系数、ray、幅度求解以及旧矩阵/profile/径向权计算次数均为 0。

源的六个可改进完整项分别为 $SQ,RQJg_d,RQJLh$、
primitive error、mean-$rQ$ 与 mean-$v_\phi$。
$SV$、原 raw-$D$ mean 与 $V_0$ mean 完整复制原项。
只有同一完整算子的两个合法上界才取最小值；
未把分量间可能抵消、独立 mean 或真实原接缝删去。

## 2. 实际身份和覆盖

workflow event 与不可变科学 checkout 均为
657e9b12edb7ab5bb81ea231ad837990ef788bce。
21 个输入文件逐项核验；科学实际耗时 14.890592036 秒，
wrapper child 耗时 15.193982181 秒。完整新输出为：

- native：0ceafc2ba2adb8c1e14ab74c3059b0a0fde39446855df0889dec741f1cb61cfe，3180936 B；
- process：67bf926abf9066d8f09dd8fbb16cd439770203b5e551c2fa374ef42f9abfc3b8，36740 B；
- worker：5f0a0e3df494ba20f4ed8ddbd6c497b244d5d29f9d2adbd17be9e62cf6ad4e66，2464 B。

完整回执目录是
[notes/exact_fold_cancelled_sources_ci/run-43642808159-1](../notes/exact_fold_cancelled_sources_ci/run-43642808159-1/)。
本次核对读取小文本 process、worker 与 publication；大 native 不通过连接器读取。

原根不确定区间与正主体切口原样保持：
$$
r_*\in
\left[\frac{1191984371497}{5000000000000},
      \frac{2383968743003}{10000000000000}\right],
\qquad
r_b=\frac{1192029371497}{5000000000000}.
$$
最大闭覆盖为
$$
\left[\frac{1091984371497}{5000000000000},
      \frac{2583968743003}{10000000000000}\right].
$$
六窗使用同一不确定根，半径依次为
$1/1000,1/500,1/200,1/100,3/200,1/50$。
全物理角输出、完整 even mean、原全局 seam 方程和费用均保留。
本次没有消费辅助复扩域，不从辅助域的成功借用新 fold 界。

原件身份如下，全部与执行回执一致：

| 原件 | 公开 run | SHA256 |
|---|---:|---|
| 原 root | 43616813816 | dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212 |
| 原完整 seam | 43625828234 | 871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642 |
| 原 moment | 43629465215 | 7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c |
| 原 Abar profile 与积分 | 43635999157 | fec8740c26064b973c61828a960c3e5c7e864b83542222c155b9e56474c39853 |
| 原负区 Cauchy | 43621934843 | 3a214897f5dc47e1a1fed3db327f54fcc0302ad6fd273ea96ecdbfcc0ca4f1e0 |

## 3. 六窗实际严格上界

下表十进制数均向上放宽，严格大于原 directed ball 的上端。
“负 primitive”只包含原报告声明的 leading/nonlocal/mean 分量，
由对应原负区 Cauchy gain 传播；不是完整 $L_0w_1$ 或强返回余项。

| 半径 | 完整积分行数 | 负区完整普通 $L^2$ 源 | 正区完整普通 $L^2$ 源 | 负 primitive |
|---|---:|---:|---:|---:|
| 1/1000 | 144 | 713579.527495 | 651026.601467 | 108158.346702 |
| 1/500 | 274 | 904852.494833 | 795133.764970 | 231250.956949 |
| 1/200 | 627 | 1439935.197078 | 1084288.822033 | 1147772.111362 |
| 1/100 | 898 | 2574848.964908 | 1538838.001449 | 13484460.558476 |
| 3/200 | 1106 | 3873685.444804 | 2078917.951413 | 139647514.092774 |
| 1/50 | 1328 | 5093852.021530 | 2665261.915332 | 1124928043.384460 |

正区两个真实分窗也单独保留，未用一个输出替代另一个：

| 半径 | 正 root collar 普通 $L^2$ 源 | 正 body 普通 $L^2$ 源 |
|---|---:|---:|
| 1/1000 | 198347.529763 | 620075.715743 |
| 1/500 | 201040.806176 | 769298.575618 |
| 1/200 | 213370.786537 | 1063087.558500 |
| 1/100 | 251542.396606 | 1518139.920236 |
| 3/200 | 303389.997958 | 2056660.972997 |
| 1/50 | 357114.504186 | 2641228.939002 |

正分窗仍保独立 mean，不授 source 到 root 的转换或 head/mean Schur。
例如最小窗原负源界为 715694.724049，现为 713579.527495；
最大窗原界为 5549241.466141，现为 5093852.021530。
这些是完整合法 upper 的改进，不是实际算子范数的下界。

最小窗负区九项的独立上界如下：

| 完整源项 | 普通 $L^2$ 上界 |
|---|---:|
| $SV$ | 59576.353657 |
| $SQ$ | 9352.062272 |
| $RQJg_d$ | 630060.993942 |
| $RQJLh$ | 7618.586534 |
| primitive error | 9361.990806 |
| mean raw-$D$ | 9.826480 |
| mean $V_0$ | 1.425716 |
| mean $rQ$ | .065493 |
| mean $v_\phi$ | .501766 |

逐项三角费用仍由 $RQJg_d$ 主导。这里“主导”仅指已取得的上界账本；
不能由此断言真实残差也具有该大小。

## 4. 从已付包络到本次结论的证明

N1–12 对新 scalar jets 的有限乘积、Leibniz 全导及全部 mean
给出真实源的逐行包络。新程序使用 256-bit directed Arb 算术，
原 profiles 的全 Fourier 指数尾及两分量矩阵作用不变。
对每个原闭行，完整新源及 full mean 分别被新包络控制，
于是原合法径向平方积分权仍可使用。

正 collar/body 的旧完整数值积分费用记为 $J_{\rm old}$。
N1–12 中的分母是旧**数值上包络平方**的严格正下界 $N_-$，
而不是实际物理源的下界。程序只在 $N_->0$ 时使用
$$
J_{\rm new}\le
J_{\rm old}\,
\frac{F_{\rm new}^2+M_{\rm new}^2}{N_-}.
$$
因为 $J_{\rm old}$ 已覆盖原相同权乘旧包络平方，
该比值给同一分窗新包络的合法完整上界；
原精确零项仍保持零。逐行求和后取平方根，得到第三节各列。
负 primitive 列再乘原完整负区传播 gain；
该 gain 的定义、均值和源窗口未改变。

实际门逐项为：

1. 原 radial-reference native 完整，九个原门和 child 0 回执都在。
2. 原 root、seam、moment 的完整参数身份一致。
3. 六 profiles、六 tensors、1328 directed rows 全部已完成并复用。
4. 同一 1328 闭行覆盖保持，未重求系数。
5. 同一根区间与准确正 body 切口保持。
6. 六个新标量 jet case 均保原 profiles 和完整两分量 tensor。
7. 原 4377 源行、两侧及正分窗费用全部完成。
8. 原 target、幅度、矩阵、profile 和径向权科学计算均未重复。

所有门在实际 native 中为 true，process 的 mathematical_complete、
mathematical_proved 为 true，failure 为 null。
这些记录和上述解析估计共同证明第三节的组件界。

## 5. 可复现入口和同步回执

科学程序
[scripts/fourfold_codazzi_exact_fold_cancelled_sources.py](../scripts/fourfold_codazzi_exact_fold_cancelled_sources.py)
SHA256 52426ffbf1286f3ab06138879c03feb3795f5300a9e1f1e6625f6b1e2cf6a689；
CI 为 0fe34702c3d536450a79ba1d9a28db6fff3d935537d8130b8fe9832ac8195714；
[21-pin manifest](../notes/2026-11-14-R133-exact-fold-cancelled-sources-CI-inputs.json)
为 c7c772e582a3d9197ab20e9df1c8efb1ad4ff0c881ea597c6e720e44fe85012d。
完整旧参数/源递归、原件获取路径、每项 bytes/SHA 在 manifest 和 process 中。

runner 在计算前后实际执行 git pull --rebase：
657e9b12edb7ab5bb81ea231ad837990ef788bce 到自身，
随后到 cc813fa7521098fdeba86b8bf8c0fe7d8c96bba0。
两次根 README 和课题 README 的 actual_diff 均为空。
全部原行与新行及源前缀已保存，出版失败不得要求重算成功数学。

下一数学输入直接使用本次成功 native。
仍需辅助复域的真实 fold/leading、同一 $w_1$ 的完整 $L_0w_1$、
原所有 $I/J$ 修正与接缝、正侧 source-to-root、强返回范数及真实充分 cutoff。
它们不由本次“全部八门成功”自动得到。
