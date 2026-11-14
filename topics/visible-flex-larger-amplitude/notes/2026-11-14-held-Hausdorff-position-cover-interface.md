# 用同一闭面的覆盖块给真正整面 Hausdorff 见证下界

2026-11-14，geometry，AI 辅助研究。`computations/geometry_20261114_held_hausdorff_cover.py` 同时提供一个小包导出 API 和通用消费者。它不依赖旧 A 的 SavedPrefix，也不假定新 M96 BVP、非线性尾或闭组装已经成功。

## 1. 一个真实像点到整面的距离

设未标记闭面的活动部分已被全部位置球 $B(c_i,e_i)$ 覆盖。这里 $e_i$ 已经包括块内点到材料中心的路径半径和中心坐标误差；无需 reach 点对筛查也全部通过，才可使用这个位置覆盖。

取同一个 phase0 闭网格中的活动点 $p\in S_0$，例如零角核心点。由实际轴旋转族的定义，

$$x=R_\alpha p\in S_\alpha.$$

给其计算值 $\widetilde x$ 及总位置误差 $\epsilon_x$。则对整个第 $i$ 块，

$$\operatorname{dist}(x,F(C_i))
\ge |\widetilde x-c_i|-e_i-\epsilon_x. \tag{H.1}$$

这约束的是到该块**所有像点**的距离，不是 $p$ 与自己材料对应点之间的位移。

式 (H.1) 的右端范数在数学上是准确实数。程序对范数及后面的圆盘距离还另外减去一个数值距离评价误差 $\epsilon_{\rm dist}$；导出器默认将其设为现有位置误差预算，也允许生产者显式给出已支付的数值上界。不能把坐标误差和距离运算本身的舍入误差混为同一项。

两帽分别用完整平圆盘处理。若圆盘中心为 $c$、单位法向为 $n$、半径为 $r_c$，令

$$z=(\widetilde x-c)\cdot n,\qquad
R=|\widetilde x-c-zn|.$$

点到整个闭圆盘的距离准确为

$$d_{\rm disk}=\sqrt{z^2+\max(0,R-r_c)^2}. \tag{H.2}$$

若该帽的固定标记总图高度不超过 $A_c$，则到完整带标记帽的距离至少

$$d_{\rm disk}-A_c-\epsilon_x. \tag{H.3}$$

导出器保守使用该帽各标记峰值绝对值之和作为 $A_c$，即使支撑重叠也合法。已有不相交标记可另用最大峰值改进，但当前大核预算不需要这个可选改进。

对 (H.1) 的所有活动块和 (H.3) 的两整个帽取最小，再与0取最大，得到 $d_-$。于是

$$d_H(S_\alpha,S_0)\ge\operatorname{dist}(x,S_0)\ge d_-,$$

故 $\delta_{\rm hold}\ge d_-$。若 $D_+$ 是同一**完整带标记闭族**对所有相位的直径上界，则

$$d_-\ge .2D_+\quad\Longrightarrow\quad
\delta_{\rm hold}\ge .2D.$$

这里没有以核心直径替代 $D$。一个正的 $d_-$ 同时证明两个连续像不同，但经过任意欧氏刚体最优配准的 $\delta_E>0$ 仍需 R238 的独立输入。

## 2. 固定 H 的直径见证

消费者使用两个固定帽的并作为 $H$。标记支撑严格在帽内，因而对应的圆周边界点不受标记影响。对于标准同轴、同半径、平行水平两帽，选相同水平坐标的两个边界点，距离就是两帽平面高度差。这给 $\operatorname{diam}H$ 的合法下界，并与同一 $D_+$ 比较。两帽半径为正，且整个图盘映射固定，所以 $H$ 有非空内部并在全相位保持不动。

## 3. 从现有覆盖生产器直接导出

已有 reach 覆盖生产器已经持有 `points[:active_count]`、位置球 `enclosure[:active_count]` 及整个家族的 `marked_D_upper`。在其末尾调用下面 API 即可；不重复求解，也不重新枚举几亿点对：

```python
from geometry_20261114_held_hausdorff_cover import write_position_cover

write_position_cover(
    args.out.with_name('position-cover.json'),
    directory=args.directory,
    centers=points[:active_count],
    enclosures=enclosure[:active_count],
    source_vertex_indices=(indices[:, None]*N+angles[None, :]).ravel(),
    marked_diameter_upper=marked_D_upper,
    witness_position_error=position_error,
    supplied_envelopes=result['supplied_envelopes'],
    supplied_envelopes_contain_saved_samples=samples_contained,
    producer_source_sha256=sha(__file__),
)
```

必须导出**全部活动块**，不能只导出未覆 reach 块对涉及的块。默认每个压缩数据分片最多50000个中心，每文件检查小于5MB。packet 绑定同目录 plan、assembly 和 phase0 mesh 的 SHA256，保留原网格顶点索引，便于复核。

当前标准闭包文件名仍沿用 `refined-A-closed-*`，这是现有封装约定，并不要求数据来自旧 A。未来新大核生产器应保留这一兼容文件名，或给消费者提供明确的同等绑定适配；不应将旧 A 的任何中心、均值、尾或直径放进新面的 packet。

R239 的单一平面配准应在整个闭面中一致使用。最省事的规范是将整块前缀用同一个逆 $\mathrm{SE}(2)$ 刚体变换送入 native 尾框架，使两帽仍在 $xy=0$ 同轴、角参数仍是 $r(\cos\theta,\sin\theta)$。消费者的默认轴为零；若换了轴，数据生产者必须明确声明正确轴和帽几何。

## 4. 消费方式与误差范围

```bash
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261114_held_hausdorff_cover.py \
  --directory CLOSED_OUTPUT --cover OUTPUT/position-cover.json \
  --out OUTPUT/held-Hausdorff-witness.json
```

默认选零角核心活动顶点并取相位 $\alpha=\pi/2$。在标准零轴坐标下，该旋转只交换水平坐标并改变一个符号，不引入额外三角函数评价误差。其他相位默认另付一次源位置误差预算作为旋转评价误差；可用 `--rotation-position-error` 明确指定已支付的上界。消费者检查所选相位在已声明的族区间内，且见证源顶点属于活动部分。

这只是消费已经生成的真实闭包与位置覆盖。输出逐项记录最限制的活动块、两完整帽的距离、整面 $D_+$、固定 $H$ 直径下界及最终比值。若当前闭面仍是小幅 A，必须如实返回幅度不足；源码的存在不是新大核闭族已经成功的证据。

所有连续位置包络、实际族的轴旋转恒等式、完整闭面与固定帽几何仍是生产者输入。消费者不额外把它们变成区间证明，也不增加课题 README 没有规定的新完成门。尚未有新大核闭包时，不制造该消费者的数值返回。
