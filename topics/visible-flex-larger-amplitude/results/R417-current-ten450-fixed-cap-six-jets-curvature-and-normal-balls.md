# R417：当前连续十族真450的固定帽六jet、曲率与完整闭盘法向球

作者：OpenAI / ChatGPT amplitude agent。日期：2026-11-15。

## 417.1 结论与执行范围

本项把已冻结 [R409](R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md) 的两个固定帽，接到真实当前连续十族、真正零active450的完整七元组及 [R413](R413-original-C-cuff-word-and-fixed-cap-target-atlas-binding.md) 的独立目标attachment。新源提供完整Cartesian闭四叉覆盖，每个闭cell的六个坐标jet、诱导度量、第二基本形式、主曲率界、位置球及单位法向球。

“六jet”指 $F,F_x,F_y,F_{xx},F_{xy},F_{yy}$，不是六阶导数。新源定义准确有理区间算法，但本轮未执行任何区间求值，也没有实际帽参数、450场、cover或数值证书。本项条件证明可独立成立；它不要求等待某次BVP结果，也不成为193或其他原科学任务的新接受前门。

源只复用旧 geometry_20261115_fixed_cap_rational_balls.py 的 disk_partition、graph_at、cap_cell 等纯函数；不调用旧 bind_geometry、load_sqrt_kernel 或 main。旧入口要求旧e70d/ac635对象及含index/kappa的marker，不能接新R409七元组。新接口使用独立schema和当前来源，保原source与所有未付责任。

## 417.2 准确对象与两侧符号

条件是实际消费者已经通过原R400/R409完整loader得到

$$
(\mathrm{paths},\mathrm{plan},\mathrm{assembly},\mathrm{target},
 \mathrm{saved},A,\mathrm{bindings}),
\tag{417.1}
$$

并由R413得到与它相同的atlas和attachment。当前十词、准确连续C目标、原112/338响应、真正450接受及完整数组认证，仍由原loader承担；本源不从元数据重新宣布接受，不把453删除三行当450。

原R409 plan给出准确半径 $c>0$、有限高度 $H$ 和完整marker列表。每个marker仅有

$$
(\mathrm{upper},z_i,\rho_i,A_i),\qquad
z_i\in\mathbb R^2,\quad \rho_i>0,\quad |z_i|+\rho_i<c.
\tag{417.2}
$$

浮点数字按完整binary64字词对应的准确dyadic解释，整数按准确整数解释；不把显示小数改成准确十进制。保原字词和有理值二者。$A_i$ 可正、负或零；列表可为空；同侧支撑可相交，全部项都必须求和。

令 $D_c=\{X=(x,y):|X|\le c\}$，$\sigma\in\{1,-1\}$ 对应upper/lower，定义

$$
t_i(X)=1-\frac{|X-z_i|^2}{\rho_i^2},\qquad
b_\sigma(X)=\sum_{i\in I_\sigma}A_i(t_i(X)_+)^4.
\tag{417.3}
$$

冻结R409实际cap的准确表达是

$$
F_\sigma(X)=\bigl(x,y,\sigma(H+b_\sigma(X))\bigr).
\tag{417.4}
$$

下帽的 $b_-$ 同样整体反射。式(417.4)不是 $\sigma H+b_\sigma$；后式与原程序及以下法向不一致。两侧marker可不同，不能把upper结果直接反射后冒充lower的全部marker。

原数值renderer将背景高度转成浮点，可能规范化负零或产生显示舍入。这里准确帽高度来自plan和同一准确共享背景的首datum。新接口记录原plan高度字词、renderer高度字词及准确差，不额外要求舍入后renderer逐字等于准确datum，也不给renderer误差证书。

## 417.3 支撑边界上的完整六jet

函数 $u\mapsto(u_+)^4$ 为 $C^3$，所以(417.3)在整个Cartesian平面为 $C^3$，包括所有支撑圆和重叠区域。写 $d_i=X-z_i$、$T_i=(t_i)_+$，逐项有

$$
\begin{aligned}
b_i &= A_iT_i^4,\\
(b_i)_x &= -\frac{8A_i}{\rho_i^2}d_{ix}T_i^3,&
(b_i)_y &= -\frac{8A_i}{\rho_i^2}d_{iy}T_i^3,\\
(b_i)_{xx}&=-\frac{8A_i}{\rho_i^2}T_i^3
 +\frac{48A_i}{\rho_i^4}d_{ix}^2T_i^2,\\
(b_i)_{xy}&=\frac{48A_i}{\rho_i^4}d_{ix}d_{iy}T_i^2,\\
(b_i)_{yy}&=-\frac{8A_i}{\rho_i^2}T_i^3
 +\frac{48A_i}{\rho_i^4}d_{iy}^2T_i^2.
\end{aligned}
\tag{417.5}
$$

在 $t_i=0$ 处这些项也准确为零。证明是在内外分别求导并用四次正部的 $C^3$ 性匹配，不是把max的分支误称处处光滑再套链式法则。

先按完整同侧列表求和，再形成

$$
\begin{aligned}
F_\sigma&=(x,y,\sigma(H+b_\sigma)),\\
(F_\sigma)_x&=(1,0,\sigma b_x),&
(F_\sigma)_y&=(0,1,\sigma b_y),\\
(F_\sigma)_{xx}&=(0,0,\sigma b_{xx}),&
(F_\sigma)_{xy}&=(0,0,\sigma b_{xy}),&
(F_\sigma)_{yy}&=(0,0,\sigma b_{yy}).
\end{aligned}
\tag{417.6}
$$

lower的所有高度导数都乘 $\sigma$。没有用旧独立kappa代替实际导数。供旧纯函数使用的内部记录明确令

$$
\kappa_i^{\rm graph}=8A_i/\rho_i^2,
\tag{417.7}
$$

其index只是当前完整marker列表的位置，不是冒造旧数据字段，也不修改原plan。

## 417.4 闭区间算法与准确开方责任

取任意闭矩形 $B=[x_-,x_+]\times[y_-,y_+]$。源码用准确有理端点的闭区间加法、乘法和正部。平方使用

$$
[\ell,u]^2=
\begin{cases}
[0,\max(\ell^2,u^2)],&\ell\le0\le u,\\
[\min(\ell^2,u^2),\max(\ell^2,u^2)],&\text{其他}.
\end{cases}
\tag{417.8}
$$

逐项构造 $[d_x],[d_y]$、$[t]=1-([d_x]^2+[d_y]^2)/\rho_i^2$，
$[T]=[\max(0,t_-),\max(0,t_+)]$，再按(417.5)求六区间。
$T\ge0$，整数幂端点单调；有符号 $A_i$ 与交叉乘积使用完整端点乘法。所有重叠项先相加，不把各项的局部结果当成完整和。

区间包含性证明返回值包围 $B$ 上所有准确六jet，因此也包围实际cell $B\cap D_c$。相关性丢失只放大区间；没有有限点采样证明。无需Arb、三角函数、RHS或Decimal/IEEE算法导数。

原 sqrt_upper 对非负有理 $q$ 返回有证明的有理上界。对正区间 $[a,b]$ 使用

$$
\sqrt{[a,b]}
\subseteq
\left[\frac{a}{\operatorname{sqrt\_upper}(a)},\
      \operatorname{sqrt\_upper}(b)\right].
\tag{417.9}
$$

$a=0$ 时左端取0。下文分母均有准确下界1，没有跨零倒数。所有输出端点为准确有理字符串，不经浮点中点解释。

## 417.5 全部重叠与有符号marker的统一界

若marker支撑与 $B$ 不相交，该项在 $B$ 上的六jet为零。对其余项令 $u=|d|^2/\rho^2\in[0,1]$。可取

$$
\|\nabla b_i\|\le8|A_i|/\rho_i.
\tag{417.10}
$$

这是有效而非最优的常数。Hessian的切向和径向特征值分别为

$$
-\frac{8A_i}{\rho_i^2}(1-u)^3,\qquad
-\frac{8A_i}{\rho_i^2}(1-u)^2(1-7u).
\tag{417.11}
$$

$u=0$ 时二者相同，无需选择径向向量。
$(1-u)^2(1-7u)$ 在 $[0,1]$ 最小值为 $-32/49$（在 $3/7$），最大值为1，因此

$$
\|D^2b_i\|_{\rm op}\le8|A_i|/\rho_i^2.
\tag{417.12}
$$

支撑外Hessian为零，边界连续，故界全局成立。这解释了旧cap_cell中的常数8，不是把采样最大值当严格界。

令 $I_\sigma(B)$ 包含所有与 $B$ 相交的同侧支撑闭盘，包括相切者。定义

$$
M_1(B)=\sum_{i\in I_\sigma(B)}\frac{8|A_i|}{\rho_i},\qquad
M_2(B)=\sum_{i\in I_\sigma(B)}\frac{8|A_i|}{\rho_i^2}.
\tag{417.13}
$$

则 $\|\nabla b_\sigma\|\le M_1$、$\|D^2b_\sigma\|_{\rm op}\le M_2$。
这是对完整和用三角不等式，保所有重叠项及负振幅，不要求支撑互斥。空和为零，平帽分支自然成立。

## 417.6 同一目标度量、法向与曲率

省略侧下标，记 $v=(b_x,b_y)$，$q=\sqrt{1+|v|^2}$。选择冻结R409法向

$$
N_\sigma=(-b_x,-b_y,\sigma)/q.
\tag{417.14}
$$

它正交于(417.6)的两个切向。upper向上／lower向下是既定取向；未证明整闭面单射前，不借此称它为某个已嵌入闭面的全局外法向。

第一基本形式满足

$$
g=I+vv^{\mathsf T},\qquad \det g=q^2=1+b_x^2+b_y^2\ge1.
\tag{417.15}
$$

每个单帽因此为正则Cartesian图。该局部结论不证明两帽互不相交或不与活动片相交；例如 $H=0$、两侧平帽重合时局部公式仍正确，而全局embedding/reach未付。

按 $\mathrm{II}_{ij}=N_\sigma\cdot F_{ij}$，两side因子抵消：

$$
\mathrm{II}=D^2b/q,\qquad \mathcal S=g^{-1}\mathrm{II}.
\tag{417.16}
$$

$\mathcal S$ 与对称矩阵 $g^{-1/2}D^2b\,g^{-1/2}/q$ 相似；由 $g\ge I$、$q\ge1$ 得两个实主曲率

$$
|k_1|,\ |k_2|\le M_2(B).
\tag{417.17}
$$

这是整个cell的曲率界，不是特征值采样。源码还返回完整区间 $g,\mathrm{II},\mathcal S$、单位法向以及

$$
\begin{aligned}
H_{\rm mean}
&=\frac{(1+b_y^2)b_{xx}-2b_xb_yb_{xy}+(1+b_x^2)b_{yy}}
 {2(1+b_x^2+b_y^2)^{3/2}},\\
K&=\frac{b_{xx}b_{yy}-b_{xy}^2}{(1+b_x^2+b_y^2)^2}.
\end{aligned}
\tag{417.18}
$$

signed区间保该平均曲率约定，不把局部 $M_2$ 冒整闭面的曲率比较。
R413给帽的既定准确目标正是(417.15)，所以该帽图相对metric误差恒零。不能以此把活动场目标改成其诱导度量：原C、prefix长度比例、cut图和全部活动域比较仍保原责任。

## 417.7 位置球与单位法向球

令 $m$ 为矩形中心，$r_B$ 是其半对角线的有理上界。旧纯函数准确求 $b(m),v(m)$，取

$$
P_0=F_\sigma(m),\qquad
r_P=r_B\,\operatorname{sqrt\_upper}(1+M_1(B)^2).
\tag{417.19}
$$

$\|DF_\sigma\|_{\rm op}=\sqrt{1+|v|^2}$；在矩形内连接 $m,X$ 的线段上积分，得
$\|F_\sigma(X)-P_0\|\le r_P$。$m$ 可以在 $D_c$ 外，准确graph在全平面有定义，线段仍在矩形内，所以这不影响 $B\cap D_c$ 的包围。

记 $w=(-b_x(m),-b_y(m),\sigma)$，$s=w\cdot w\ge1$，取原开方上界 $L_+\ge\sqrt s$ 及有理法向中心

$$
N_0=w/L_+,\qquad e_0=1-s/L_+^2.
\tag{417.20}
$$

有 $e_0\ge0$ 且

$$
\|w/\sqrt s-N_0\|
=1-\sqrt s/L_+\le1-s/L_+^2=e_0.
\tag{417.21}
$$

映射 $v\mapsto(-v,\sigma)/\sqrt{1+|v|^2}$ 的导数算子范数至多1，故

$$
\|N_\sigma(X)-N_\sigma(m)\|
\le\|\nabla b(X)-\nabla b(m)\|\le M_2(B)r_B.
$$

于是

$$
r_N=M_2(B)r_B+e_0
\tag{417.22}
$$

包围cell上所有真实单位法向。球中心本身可以不单位，(417.21)明确支付其归一化误差；未把上开方近似中心当准确单位法向。

位置／法向球直接用旧cap_cell原函数，新六jet与曲率输出绑定同帽参数、当前source和同Cartesian cell。

## 417.8 两个完整闭盘的四叉覆盖与未访责任

从 $[-c,c]^2$ 开始，原0、1、2、3顺序分别为左下、右下、左上、右上闭子矩形，边界重叠保留。只有

$$
\min_{X\in B}|X|^2>c^2
\tag{417.23}
$$

才省略该box；相切保留。最小值用两个坐标至闭区间的准确距离平方之和，不采样圆周。

逐层归纳可知盘中每点始终落在某个没有被严格排除的子box。达到depth后全部保留cell覆盖 $D_c$；上下帽各用同一完整地址表和各自marker子表，覆盖两帽全部边界与内部。固定帽不参与R409活动旋转，故同一球对原全部相位成立，但不替代活动／mixed-pair的相位覆盖。

depth取0至30，base sqrt bits取16至4096，每cell有效bits=base+depth。最坏 $2\cdot4^{\rm depth}$ 必须不超过调用者显式max_cells；这是资源容量，不是几何接受门。

若资源回调或求值异常，已完成cell保留；只有两侧全部地址完成才置complete。partition尚未返回则两个盘均未付，否则给真实cap顺序后接path顺序的未完成半开索引与下一个地址。不得把未访片填平、删掉失败cell或将预算结束作为数学反证。

## 417.9 新薄API的来源合同

新 bind_loaded_shared_bundle(bundle, atlas, attachment, computations)：

1. 核冻结R409源和真实CurrentSharedAssembly对象，保saved、plan、共享背景、原反射及Cartesian轴。
2. 调用原R413同名绑定函数得到当前attachment，与已给attachment逐字核对；当前十词、原C、原cuff和同场身份由原函数处理。
3. 读取全部当前marker与准确H，核同一背景首datum，不读取旧kappa/index。
4. 直接pin旧帽纯函数与原sqrt，不触旧e70d/ac635 binder。
5. 返回独立消费者和binding，不替换七元组、原guard、target未付标志或原接受记录。

| 冻结源 | 本项使用范围 | SHA256 |
|---|---|---|
| geometry_20261115_current_C_ten450_shared_field.py | 真七元组、类与帽准确表达 | 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 |
| geometry_20261115_current_C_original_cuff_target_atlas.py | 原cuff与当前target attachment | 02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2 |
| geometry_20261115_fixed_cap_rational_balls.py | 原闭四叉、点graph、位置／法向球纯函数 | a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e |
| root_mixed_phase_normal_balls.py | 仅准确有理sqrt_upper | ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6 |

四个直接pin不替代R400/R409的完整闭包。675 ExactFiniteField仍负责活动片；本项未假称它已生成帽jet，也不需复制其Arb runtime。帽公式只用标准库准确分数和原sqrt上界。

## 417.10 交付和完成边界

独立源码为 [geometry_20261115_current_C_ten450_fixed_cap_balls.py](../computations/geometry_20261115_current_C_ten450_fixed_cap_balls.py)，完整API见[接口](../notes/2026-11-15-current-ten450-fixed-cap-interval-interface.md)。

本项给出完整两帽条件算法和证明，尚无实际运行。真实结果必须绑定实际450→R409→R413对象、参数、source、run和输出身份。大cell表只留实际Actions自有临时目录，必要研究结论另行小摘要；本源没有request、workflow、artifact、分块／编码传输、主动清理或未来run。

仍未付：活动prefix/tail/collar/patch准确jet与共同目标比较；准确C根族与场关联、完整径向域和cut公共图；整闭面metric／曲率与规定尺度比较；完整活动／固定／混合pair、injectivity、reach、held；renderer误差、native/BVP重新接受及最终课题完成。

R413局部cuff目标衔接与本项帽六jet可以作为两个同场子责任合用；合用不自行关闭上述其他责任。
