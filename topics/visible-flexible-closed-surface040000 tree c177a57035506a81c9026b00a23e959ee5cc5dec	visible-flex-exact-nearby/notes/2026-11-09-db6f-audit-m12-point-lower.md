# R21 M12 严格点态误差下界：完整独立审查

审查者：`/root/independent_geometry`，2026-11-09。本岗位未参与被审 M12 图的求解优化、root 的点搜索或 wrapper 实现；既有底层组件按各自已经完成的独审记录引用，不把本岗位此前编写的区间存储适配器重新称为独立设计审查。

**结论：新 wrapper、固定对象连接及完整方法稿审查 PASS；独立同参 12 点重放实际退出 0，全部数学字段相同；额外直接 Fraction 径向对角项重构实际退出 0，并被原区间严格包含。** 未发现数值或数学修正需求。

## 1. 冻结审查对象

| 对象 | SHA256 |
| --- | --- |
| `scripts/db6f-root-tail-m12-point.py` | `5d950fa6caa3aff062ba5a62e743abac5b00d7ef0721930f299135d1dbdc1bb1` |
| 作者报告 `2026-11-09-db6f-root-tail-m12-point-metric-witness.json` | `13311ea4ecb781d0607ff6b58880c5f70bd79db2df2527aa9de3b6d9ad2e1b5e` |
| 最终证明 `2026-11-09-db6f-root-tail-m12-point-lower-proof.md` | `955a6550b43efb88f25767eaa0636fdb2be6eb397175507319c96fdddb2b8f92` |
| 旧点公式 `scripts/db6f-root-tail-metric-point.py` | `cde5264c884d261450add564b818cd9f863937c703017f1bc4df9b2443b0f7cc` |

初读证明版本为 `a3456aaffe2a9f770218186b110cd8dcc7a752b828e120f261932ca10d546603`。审查指出径向归一化因子 $\beta$ 为一般精确有理数，故派生多项式系数未必是 dyadic。作者只将“精确二进五次多项式”澄清为“由保存二进数据及精确径向增量定义的五次多项式”。对新文件反向替换这一句即逐字还原旧哈希；公式、数据和结果未变。独立 Fraction 检查也确证当前 $\beta$ 不是 dyadic。

## 2. 同一实际闭图与同一个目标 g

wrapper 的 `EXPECTED` 固定六项输入：旧点公式、M12 critical 第一档 manifest、其共同 cut 几何、该图完整低 metric 背景 transfer 包、R21 whole 汇总，以及旧 M8 point 证书。每项都检查冻结文件 SHA256；它没有删除或放松旧 CLI 的原背景 checkpoint guard 来接收任意新 manifest。

新 manifest 的哈希为 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`，共同图哈希为 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。wrapper 核 whole 与几何、packet 与新旧 manifest、whole 的独立 metric 证书与 packet 的连接。读入的几何和 whole 正是已独审 R21 的对象，未混用 uniform M12 或第二档 critical 图。

背景 point 算法沿用旧 M8 的严格 primitive 和 calibration table，但这里依赖的是 **同 $g$ 连接**，不是两个求解状态相同。新旧 packet 的六项非空 `background_definition_hashes` 逐项一致，并重核六个实际文件。独立脚本又实际比较新旧 manifest 的全部参数，而没有仅信任 `all_other_parameters_identical` 标记。只有已审的 11 个数值字段变化：`auditSteps`、`depth`、`farPadding`、`initialCheckpoint`、`maxIterations`、`modes`、`physicalDepth`、`quadrature`、`shootingParts`、`steps`、`traceFile`。所有其他参数严格相同；其中 `physicalDepth` 在固定保护层 160 的已审模型中只控制数值截断／展开，并未改变定义无限背景的物理保护位置。

primitive 的完整参数字典与旧 manifest 的参数字典逐项相等。审查还重核旧 point 列出的源依赖、primitive 保存的全部模型依赖及系数算术后台哈希。其 strict calibration、唯一原精确背景 $\alpha$、raw source 和径向 primitive 的结论按已审依赖链使用。

R21 已将这个 manifest 定义的实际有限尾嵌入同一个闭图。上尾完整高度的反射以及竖直平移是环境等距，保持所有一阶点积；因此这里的内部点是 R21 闭图的合法度量误差见证，而非仅有形式 ODE 意义的点。

## 3. 点公式手核与范围

对 planar 模 $m\equiv1\pmod3$，旋转标架中的相位为 $(m-1)\theta$；height 模为 $3$ 的非负整数倍。取 $\theta=q\pi/6$ 后，所有这些因子为精确的 $0,\pm1$。模 4 的整数查表对负 planar 模同样成立，未调用近似三角函数。

令旋转标架中的实际切向量为

$$
X_r=(1+R_r,T_r,w+Z_r),\qquad
X_\theta=(a,r+b,c).
$$

planar 角导数的系数必须使用原 Cartesian 频率 $m$，而其相位使用 $m-1$；源码恰当地分别处理这两个量。height 角导数带负的 $m\sin(m\theta)$ 因子。逐项展开得到

$$
E_r=2R_r+R_r^2+T_r^2+Z_r^2+2wZ_r,
$$

$$
F_r=(1+R_r)a+T_r(r+b)+(w+Z_r)c,
$$

$$
G_r=a^2+2rb+b^2+c^2.
$$

背景度量为 $(1+w^2)dr^2+r^2d\theta^2$，所以归一化矩阵三项为

$$
\frac{E_r}{1+w^2},\qquad
\frac{F_r}{r\sqrt{1+w^2}},\qquad
\frac{G_r}{r^2}.
$$

源码的有理物理半径、精确局部参数、区间 Horner 和这三个归一化因子均正确。两个独立区间类型之间只复制已有 binary 端点，未添加额外算术运算或改变端点。背景供应器的近似 inverse 只提议合法 source 点；真实半径由严格 primitive 包围，再用完整连接区间上的 $|w_r|\le24$ 传递到目标半径。本例未错误地只凭 source cell 标签使用内域更小常数。

任何对称矩阵条目的绝对值都是算子范数下界；对区间取其绝对值下端点再最大化仍正确。12 个候选点中选择最大的有效下界只是存在性选择，不生成任何全域上界。

## 4. 独立完整重放

原 wrapper 换输出路径运行，真实退出 0，输出为 `2026-11-09-db6f-audit-tail-m12-point-replay.json`，SHA256 `4b66a167f34802d4b1017382e7b634f3b0ab11ffa64ed5f6d03f78d4758142d5`。完整 JSON 与作者报告除 `seconds` 外逐字段相等。

默认搜索恰为 span 17148 中的 $u=1/4,1/2,3/4$ 乘四个特殊角，共 12 点。选中 $u=3/4,\theta=\pi/3$，其精确半径为

$$
r=\frac{542597661727932063391508010872115368615351}
{1247347073977141182794646048914448905666560}.
$$

该半径严格位于该实际 span 内部。报告中的正径向对角项下端点给出

$$
\mathcal E_{12}\ge
L=\frac{370012576184137}{18889465931478580854784}
>1.95883\times10^{-8}.
$$

输出只保存被选中的见证及检查数；本审查的“12 点复跑”是实际重新执行全部默认循环，不声称作者保存了未输出的其他 11 点数组。

## 5. 额外独立 Fraction 重构

新脚本 `scripts/db6f-audit-m12-point-lower.py`，SHA256 `9241d028664af723e8314a9d88ea87e8f3d77dc97d7308fc9025349641b50dc6`，另行真实退出 0。其输出 `2026-11-09-db6f-audit-m12-point-lower.json` 的 SHA256 为 `5da4dbd618f2a0d7866e8fffdb0abc3a398dd264c395d00554160f1c7dfee181`。

这一步没有调用 `point_metric`、区间多项式构造器或浮点 Horner。它从保存的 first／second 端点数据、中点数据以及独立重算的有理长度 $L_r$，直接构造 quartic 导数。若

$$
u_0=V_r(r_i),\quad u_1=V_r(r_{i+1}),\quad
v_0=L_rV_{rr}(r_i),\quad v_1=L_rV_{rr}(r_{i+1}),
$$

$$
b=16u_{1/2}-8(u_0+u_1)-2(v_0-v_1),
$$

则导数的五个幂系数为

$$
(u_0,\ v_0,\ -3u_0+3u_1-2v_0-v_1+b,
\ 2u_0-2u_1+v_0+v_1-2b,\ b).
$$

这些量在 Python Fraction 中精确计算，再以 $u=3/4$ 和精确特殊角求 $R_r,T_r,Z_r$。本点 $T_r=0$ 恰成立。背景 $w$ 的合法点区间仍引用独立重放过的已审供应器；这个补充重构没有重新声称独立证明整个解析背景。

设 $C=2R_r+R_r^2+T_r^2+Z_r^2$，则直接用精确有理区间运算包围

$$
\frac{C+2Z_rw}{1+w^2}.
$$

所得区间显示约为 $[1.9588302686627234,1.95890803881998]\times10^{-8}$，其精确有理端点全部保存于 JSON。它被原报告径向区间严格包含，因而提供了不依赖原区间多项式实施顺序的额外交叉核验。这个补充只独立重构径向对角项，不冒称重新推算全部三项和整个尾域。

## 6. 实际误差比较与保留限制

Fraction 账本独立验证 $L>1.95883\times10^{-8}$ 以及

$$
L>\frac{195883}{20000}\,(2\times10^{-9}).
$$

所以若未来另一个**同 $g$ 的实际完整闭图**严格满足 $\mathcal E_{\rm new}\le2\times10^{-9}$，才可以合取推出

$$
\mathcal E_{12}>9.79415\,\mathcal E_{\rm new}.
$$

当新误差为零时该写法也成立，不需要除以它。当前并没有该完整新图的上界；M15 辅助 affine prefix 的采样量不能代入。全相位下界沿用 R21 已审的材料角平移／空间等距作用。G5、精确等距解、无限极限和最终完成均未由本点证书支付。

复现命令（wrapper 拒绝覆盖已有输出，请选择新路径）：

```sh
python scripts/db6f-root-tail-m12-point.py \
  --out notes/2026-11-09-db6f-audit-tail-m12-point-replay.json

python scripts/db6f-audit-m12-point-lower.py \
  --author notes/2026-11-09-db6f-root-tail-m12-point-metric-witness.json \
  --replay notes/2026-11-09-db6f-audit-tail-m12-point-replay.json \
  --proof notes/2026-11-09-db6f-root-tail-m12-point-lower-proof.md \
  --out notes/2026-11-09-db6f-audit-m12-point-lower.json
```
