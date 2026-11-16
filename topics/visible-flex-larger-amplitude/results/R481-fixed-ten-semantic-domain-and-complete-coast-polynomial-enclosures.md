# R481 — 固定十参数域、同一 C 语义族与 coast 的完整局部多项式包围

作者：ChatGPT（amplitude，AI-assisted）  
日期：2026-11-16

**可信度：已证明，限本文的准确表达式恒等式、区间包含、参数范围与源码控制流命题。actual205 的准确十域仍未付；本文未执行新的区间计算、BVP、几何消费者或数值测试。**

## 1. 结论与作用范围

[R453](R453-actual205-new-ten-domain-partial-complete112-and-point-work-stop.md) 记录 actual205 的 requested_parameter_domain.complete=false，全部 10,594 个终端未决位于 piece416 coast，另有16个未访项。这一记录提出两个不同问题：原检查量化了哪些参数；既有表达式是否有可以严格消去的区间依赖。

本文得到以下结论。

- 72c factory 固定 recipe 中的十个准确系数；它没有对十维控制盒搜索。其区间证明统一覆盖同一 C 在 cut 处 E0/E1/E2 的合法外包，并进一步放宽这三项的相关性。准确目标的所选根规则、这些合法语义叶的实际联合值、以及区间算法使用的直积盒，不能混为一物。
- coast 上完整十控制只有 p3、theta3、eta3 三项有贡献。新增 support1/power4 的 xi 不作用于 coast 内部，且在共端点的二阶 jet 为零。
- 以真正 coast 局部坐标表示时，完整三 jet 可以先在准确代数中消去重复 coast 宽度，再对一个至多八次多项式求完整区间像。速度对 coast 宽度是仿射函数，因此对一个已证明的宽度盒，完整速度条件等价于两端宽度各自的两条完整多项式不等式；不需要在宽度方向采样。
- 这些是 [R352](R352-shared-calibration-normal-forms-and-complete-Bernstein-target-enclosures.md) 共享校准／全项合并方法在当前十族与 factory 局部域中的具体适用点，不是首次发明 Bernstein 或共享变量重写。原九族165 consumer不能不作来源与第十项处理就直接冒为十族消费者。
- 现有完整 metric、reach、held 消费者没有把 factory 初点域 complete=true 作为新增 BVP 前门。它们各自仍要实际完成准确目标、六 jet、正规性、全 pair／全像等责任；native 接受和有限采样不能补这些证明。

本文既不把失败归因为纯粹依赖膨胀，也不声称重写后该参数点会通过。没有修改72c、205、212或任何运行中的源，没有新 workflow、参数选择、fixture或验收门。

## 2. 确定的源码对象

以下短名均指完整已刊字节。

| 短名 | 文件 / SHA-256 |
|---|---|
| 72c | geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py；72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682 |
| 165 | root_20261115_continuous_nine_shared_target_enclosures.py；61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205 |
| R400 target | geometry_20261115_continuous_ten_frozen450_prefix_metric.py；011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84 |
| R416 | geometry_20261115_current_C_accurate_cut_patch.py；28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b |
| R418 | geometry_20261115_current_C_ten_complete_relative_metric.py；28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590 |
| R422 | geometry_20261115_current_C_ten_complete_reach_cover.py；3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834 |
| R425 | geometry_20261115_current_C_ten_held_and_rigidity_inputs.py；c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2 |

165 固定 source 是1f2ec637430e5c6b27b1a93720e106539281a156，其原94,125 B全文身份已核。R352证明17,736 B／58cdfeb61adb46378ca4f6c070b8b8e7d7c0ff3f9cf1b853e44a1c52316f5a85，已刊34fd5a7f241406a2bb48a6d8ed6f6ec1a4e69188。

原205控制流见 R453 §5：pipeline construct 保存域完整性但不据此阻断；实际 binding 在 current geometry 未 ready 处返回，未调用 R449.bind。因此以下域分析不能改写实际205的停止原因。

## 3. 量词：十系数固定，语义叶按同一来源外包

### 3.1 十个控制不是区间自由变量

72c.build_expression 直接把 recipe.ten_parameters 全部送入 rational，再保留十个准确有理常数。rational 对浮点输入使用其准确 binary64 有理值，对字符串使用准确有理解释。actual205 的十词、结构宽度、cut、core 和根规则均已由其实际来源固定。

Tree 的十控制并不是十个 semantic-cut-leaf。唯一三种语义叶名称是 E0、E1、E2，分别代表同一准确 C 的同一个 cut 处的 $E,E_r,E_{rr}$。build_expression 的 cut_boxes 实参不被用作目标系数；目标 DAG 继续保存这些语义叶。随后 Tree.evaluate 用实际完整 cut readout 的三个闭盒求向外包含，区间端点／中点未被写成新的目标值。

设 $p^*\in\mathbb Q^{10}$ 是本次实际系数。设 $\mathcal E$ 是来源允许的准确 C 根选择在 cut 处产生的联合三 jet 集合。完整 cut readout 给出

$$
\mathcal E\subset B=I_0\times I_1\times I_2.
\tag{481.1}
$$

特定 recipe 的根选择可以指定其中一个准确对象；原 producer 同时保持对所有允许根选择的有效包围。不能从一个有限盒反向选择根，不能宣称每个独立盒点都对应某个真实 C。

若72c的区间检查完成，它证明的充分命题是：在合法构造条件下，对所有被区间扩展覆盖的 $e\in B$、全部准确分片的全部闭局部位置，固定 $p^*$ 满足所检查的半径／速度不等式。因此它支付实际语义对象的相应条件。它没有证明一个包含 $p^*$ 的十维控制邻域全部合法。

反之，complete=false可以由未访、分辨率／预算、区间依赖或真正缺乏严格裕量造成。它不证明特定 $e$ 失败，也不证明 $\mathcal E$ 上所有对象失败。

### 3.2 BVP 活动坐标与初点证书

原453可以改变三个活动标量，随后450固定其实际末十词。R400.AccurateTenTarget从实际 checkpoint.target_identity 的 complete_ten_exact_dyadics取当前十参数，而不是把factory.starting_parameters永远当作末点。源码还明确 actual_frozen_point_need_not_equal_factory_starting_point=true。

所以即使某次 factory 初点域 complete=true，也不能把它自动转移到未来变化后的参数。反之，初点未取得充分域证也不能偷偷成为阻止原BVP探索的新增门。当前点的准确目标、原求解门和后续完整几何责任必须分别付出。

## 4. coast 的准确三 jet 与第十项的严格支撑分离

沿72c记：

- $c$ 是固定准确 core 末坐标；$R_A,V_A,B_A$ 是同一准确 core 末二 jet；
- $\kappa\in(0,1)$、$d,d_A,d_B>0$ 是原 recipe 固定有理数；
- $I_A=d_A(V_A-\kappa)/2+d_A^2B_A/12$；
- $S_1=c+d_A$，$\ell=L_C(e)>0$，coast 为 $[S_1,S_1+\ell]$；
- $t=(s-S_1)/\ell\in[0,1]$，这里 $t$ 是该片局部坐标，**不是整个闭面变形时间**。

定义

$$
b_j(t)=64t^3(1-t)^3(2t-1)^j,\qquad
P(t)=p_3b_0(t)+\theta_3b_1(t)+\eta_3b_2(t).
\tag{481.2}
$$

**命题1。** 对每个固定准确语义叶选择，coast 上完整十族的实际函数和关于原物理坐标 $s$ 的导数恰为

$$
\begin{aligned}
a(s)&=A-\kappa\ell t+\ell^2P(t),\qquad A=R_A+I_A,\\
a_s(s)&=-\kappa+\ell P'(t),\\
a_{ss}(s)&=P''(t).
\end{aligned}
\tag{481.3}
$$

**证明。** 原 coast base 的系数为 $[R_A+I_A,-\kappa\ell]$，宽度为同一个 $\ell$；原 support2 的 left/width恰为 $S_1,\ell$。72c的第2、5、8个零基索引控制在此给 $\ell^2P((s-S_1)/\ell)$。固定语义对象时 $\ell$ 是常数，$dt/ds=1/\ell$，两次链式法则给后两式。

support0 严格位于 core 内；support1 是 $[c,c+d_A]=[c,S_1]$，故它们在 coast 内部均为零。support1 的第十项是 $d_A^2\xi b_4((s-c)/d_A)$。因 $t^3(1-t)^3$，每个 $b_j$ 在0、1的0、1、2阶导均为零；它们延拓为支撑外零函数仍为 $C^2$。因此共端点 $S_1$ 也没有遗漏 xi 的二阶贡献。命题不依赖 xi 的数值大小。证毕。

这里没有删掉十参数；只是依据**准确真实支撑身份**把该片上本来为零的项明确为零。数值编译自己的支撑字词如果有边界缺陷，仍须按它自己的全部字面定义处理，不能套用此准确支撑结论。

全三支撑合并时，support0与support2多项式次数至多8；support1含 $b_4$ 后次数至多10。165的原 range(3)／九系数／degree≤8实现不能不修改就对全十族使用；coast局部的三项仍正好适用原 degree≤8公式。

## 5. 旧 piece_range 中确实存在的依赖来源

72c.piece_range 先以区间宽度计算基底各阶，再形成 $s=[S_1]+[\ell]T$，随后对support2重新计算

$$
X=\frac{s-[S_1]}{[\ell]},
\qquad
p[\ell][\ell]\frac{b_j^{(k)}(X)}{[\ell]^k}.
\tag{481.4}
$$

它逐个控制形成多项式、Horner求区间、再相加。以下三层必须分开。

### 5.1 可准确消除的重复宽度

设合法宽度盒 $I=[\ell_-,\ell_+]$，$0<\ell_-<\ell_+$。即使局部位置已收成单点 $T=\{t_0\}$，$t_0>0$，按旧自然区间运算，在支撑截取之前得到

$$
X=
\left[
t_0\frac{\ell_-}{\ell_+},
t_0\frac{\ell_+}{\ell_-}
\right].
\tag{481.5}
$$

准确对象却恒有 $X=\{t_0\}$。在截取不把区间压成单点的情形，位置盒宽为

$$
t_0\left(\frac{\ell_+}{\ell_-}
        -\frac{\ell_-}{\ell_+}\right)>0.
\tag{481.6}
$$

原基底的一阶导也形成

$$
\frac{-\kappa I}{I}
=
\left[-\kappa\frac{\ell_+}{\ell_-},
      -\kappa\frac{\ell_-}{\ell_+}\right],
\tag{481.7}
$$

准确值则是单点 $-\kappa$。以上是精确有理区间计算的依赖扩张，不是binary64舍入误差。只继续缩小局部 $T$，不能消掉式(481.5–7)中固定宽度盒所产生的这部分放宽。

实际205返回的 coast_length 上下端点文字不同；本文只核了原字段文字，没有计算其宽度或与实际速度裕量比较。因此并未证明这层依赖主导那10,594个未决叶。

### 5.2 同一个局部变量的多项式抵消

各 $b_j$ 的展开式有正负系数；先分别求区间再加，会丢掉同一 $t$ 在三项及同一项内部的抵消。先准确合并式(481.2)的系数，再形成完整多项式像，是 R352 的既有办法。

该办法不保证对每个查询都严格更窄。若同时保旧合法界并与新合法界取交，结果不会比任一被保留的界宽；空交集表示来源／实现错误，不能作为该准确目标被反证的证据。

### 5.3 不能靠局部细分消除的输入信息宽度

coast 长度还依赖原 C 的三个准确 cut 量。沿72c，

$$
v=-E_0^{-1/2},\qquad
b=-\frac{E_1}{2E_0^2},\qquad
q=\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}}.
\tag{481.8}
$$

同一个 $E_0$ 出现在平方根与多次分母，同一个 $E_1$ 同时线性和平方出现；普通Box不是仿射／相关区间，重复节点的值虽复用，组合时相关性并未保留。更重要的是，真实 $\mathcal E$ 未必填满其直积外包 $B$。

这些是可定位的来源，不是本次实际误差分解。不得把合法旧盒端点改窄、选择中点、把 root-family 责任丢掉，或由一个有限盒宣称可以任意精化。更窄同C信息必须来自真正的同对象上游查询；本次纸证没有做它。

## 6. 完整 coast 速度判定：只需宽度两端的整多项式

**命题2。** 固定 $P,\kappa$，给定合法正宽度区间 $I=[\ell_-,\ell_+]$ 和闭局部区间 $T$。下述两条件等价：

1. 对所有 $(\ell,t)\in I\times T$，$-1<-\kappa+\ell P'(t)<1$；
2. 对 $\ell=\ell_-,\ell_+$ 分别，以下两条完整多项式在全部 $T$ 上严格为正：

$$
1-\kappa+\ell P'(t)>0,\qquad
1+\kappa-\ell P'(t)>0.
\tag{481.9}
$$

**证明。** 固定任意 $t$，速度和上述两个余量均为 $\ell$ 的仿射函数。区间内每个值是两端值的凸组合，故端点严格为正推出全部为正。反向由区间包含端点立即得出。证毕。

这个等价命题针对**给定盒的完整矩形范围**。真实 C 家族产生的宽度集合可以更小，故盒端点未通过不构成实际 C 的反证。它不是额外 native 或 BVP 门，只是原 $|a_s|<1$ 充分检查的一种等价实现。

$P$ 至多八次，所以式(481.9)的四个多项式各至多七次。它们可以使用全8个 Bernstein 系数向外包围，在同一个 $T$ 上保全所有位置。不是只检查 $t$ 两端或采样若干点；“只需两端”仅指对宽度 $\ell$ 的仿射依赖。

若原严格速度条件对整个矩形有正裕量，存在某个有限细分可以证明这四个多项式。具体地，对其中一个次数 $n\le7$ 的多项式 $f$，设全 $T$ 上 $f\ge\delta>0$，且 $|f^{(r)}|\le M_r$。在长度 $h$、左端为 $a$ 的子区间上，完整 Bernstein 系数为

$$
b_j=f(a)+\sum_{r=1}^{j}
\frac{f^{(r)}(a)}{r!}h^r
\frac{\binom{j}{r}}{\binom{n}{r}}.
$$

因二项比值在 $[0,1]$，$|b_j-f(a)|\le\sum_{r=1}^{n}M_rh^r/r!$。取足够小的正 $h$ 使右侧小于 $\delta/2$，全部系数即正；有限闭分割覆盖紧区间。对四个 $f$ 取共同细分即可，常数多项式直接处理。这个存在性结论不保证已声明300s／depth32／65536预算足够，也不在裕量为零或条件失败时给终止保证。

## 7. 半径与二阶导也可完整形成，不把速度证据冒全域

只有速度检查仍不完整。半径原条件 $a>0$ 必须同时保留。

由(481.3)，$a$ 对 $(\ell,t)$ 的双次数至多为 $(2,8)$。令

$$
\ell=\ell_-+(\ell_+-\ell_-)y,\qquad
t=t_-+(t_+-t_-)x,\qquad 0\le x,y\le1.
$$

准确展开得到

$$
a=\sum_{r=0}^{2}\sum_{s=0}^{8}c_{rs}y^r x^s.
$$

形成全部 $3\times9=27$ 个双变量 Bernstein 系数

$$
\beta_{ij}=
\sum_{r=0}^{i}\sum_{s=0}^{j}
c_{rs}\,
\frac{\binom{i}{r}}{\binom{2}{r}}\,
\frac{\binom{j}{s}}{\binom{8}{s}},
\quad 0\le i\le2,\ 0\le j\le8.
\tag{481.10}
$$

双 Bernstein 基非负、和为一，所以 $a(I\times T)$ 包含于这些全部系数的最小／最大外包。若其下界严格为正，就支付同一矩形中的半径条件。不得只取四个 $(\ell,t)$ 角点：半径关于宽度一般是二次，内部极值可能存在。退化宽度或单点 $T$ 可直接代入相同完整多项式，不除以零宽度。

同理 $a_{ss}=P''$ 至多六次，用全7个 Bernstein 系数给其完整包围。二阶导不是原域通过谓词的一部分，但原 ledger 的 a/ap/app 与后续六jet消费者需要它，不能为省工作删掉。

式(481.9–10)保留原全部十点系数、同C宽度包围和两个闭端点。也可先以原Box运算形成(481.3)的粗界，再与完整 Bernstein 界取交；没有改原严格半径／速度阈值。

## 8. 长度输入的校准与一个真实单调方向

R352已给出总长度展开。对 coast 宽度本身，准确代入72c的 $R_B,V_B,B_B,I_B$ 得

$$
\ell=A_0+c_vv+c_bb+c_qq,
\tag{481.11}
$$

其中

$$
\begin{aligned}
A_0&=\frac{R_A-R+I_A-\kappa d_B/2}{\kappa},\\
c_v&=\frac{d+d_B/2}{\kappa}>0,\\
c_b&=-\frac{d^2/2+d_Bd/2+d_B^2/12}{\kappa}<0,\\
c_q&=\frac{d^3/6+d_Bd^2/4+d_B^2d/12}{\kappa}>0.
\end{aligned}
\tag{481.12}
$$

证明只需把 $R_B=R-vd+bd^2/2-qd^3/6$、
$V_B=v-bd+qd^2/2$、$B_B=b-qd$、
$I_B=d_B(-\kappa+V_B)/2-d_B^2B_B/12$ 代入原
$\kappa\ell=R_A-R_B+I_A+I_B$ 并按 $v,b,q$ 收集。没有更换长度或调参。

该式提供另一份同对象合法包围，可与原 DAG 的宽度界相交；它不自动消除 $v,b,q$ 共同依赖 $E_0,E_1$ 的信息损失。特别地，在 $E_0>0$ 下，

$$
\frac{\partial\ell}{\partial E_2}
=\frac{c_q}{2E_0^{5/2}}>0.
\tag{481.13}
$$

故对独立 $E_2$ 盒，固定 $E_0,E_1$ 时长度极值在 $E_2$ 两端；若未来采取联合区间细化，这是一条可直接利用的准确单调性。它不允许逐片换成不同 C 根，不证明关于 $E_0,E_1$ 也单调。本文没有代入 actual205 端点评价新宽度，没有把单调性当成已经付出的数值收窄。

## 9. 公共 u、实际几何与真正域责任

### 9.1 不可把 coast 局部坐标当公共 u

R400.AccurateTenTarget.closed_range 的实际路径是

$$
u=s_{\rm num}/L_{\rm num},\quad
s_{\rm true}=L_{\rm true}u,\quad
t_i=(s_{\rm true}-A_i)/W_i.
\tag{481.14}
$$

它枚举全部原 accurate pieces，对每个可能 local 区间调用72c.piece_range，保全部闭端点，再取 union hull。若未来仅把 coast 的该次 piece_range 换为(481.3)，必须继续使用由(481.14)合法推得的完整 $T$，并保其他全部候选片。不能设 $t=u$，也不能用 numeric length 代替真实 $L_{\rm true}$。

速度公式关于物理 $s$；若改在公共 $u$ 求导，仍须用 $a_u=L_{\rm true}a_s$、
$a_{uu}=L_{\rm true}^2a_{ss}$。目前域证书与metric证书作用点不同，不能从某片坐标重写省去公共长度误差或材料角责任。

### 9.2 实际消费者需要什么

| 消费者／函数 | 实际需要／报告 | 不自动证明 |
|---|---|---|
| 72c.prove_domain | 固定十点、完整piece，严格 $a>0,\ |a_s|<1$ 的充分区间检查；全部终端／未访 | 未来变化参数，数值BVP，完整闭面 |
| R400.AccurateTenTarget | 完整DAG、十个当前准确词、同C叶、所有piece/support正宽度、真实与数值长度正 | 初点domain flag等于末点domain，任意可精化C名字 |
| R400.inspect | 真实cell $a$ 下界正后，比较六jet实际Gram与 $((L_{\rm true}/L_{\rm num})^2,\ a^2\Phi_q^2)$ 的原四Loewner | 全部 $|a_s|<1$、所有seam、native或闭面成功 |
| R416.AccurateCutModel | 原 $E_0,L$ 正、准确cut三导与完整chart／修正表达式 | 用旧renderer切向jet冒准确cut，原BVP自动 $C^2$ |
| R418.inspect_cell | prefix按R400；native/collar需同C完整闭query，目标为 $(E_C(r),r^2\Phi_q^2)$ | 用 $1+B'^2$ 替代C，或外推cut点盒到全tail |
| R422.CurrentGeometry/cover | 真实全piece／两帽、完整六jet、非零面积/法向球/曲率及完整pair条件 | 一份初点scalar域flag代替embedding/reach |
| R425.witness_points/cover | 真实准确field点和全像覆盖、原H/直径/rigidity责任 | 仅点位移、有限native余量或factory域替代全像结论 |

这些源码未要求 requested_parameter_domain.complete=true 来开启原BVP／几何。R400.inspect 在真实cell无法隔正 $a$ 时返回 unresolved，明确不推速度域反证；R416的分母与chart、R422的真实法向／Gram等仍按各自原完整责任处理。对某个域条件的未付，不能偷换成另一个条件已过。

$a>0$ 使该标量目标的角向度量不退化；原 $|a_s|<1$ 是当前构造所要求的严格scalar域条件。是否得到整个准确闭面 $C^2$、全 $t$ 强连续、嵌入和reach，还需要同场的实际六jet与接缝／覆盖等完整结论。不能只因某native离散gate通过，就补上这些连续结论；也不应把factory对更大语义盒的充分证书未完成改造成新solver拒绝。

## 10. 可直接实现的最小作用点与必须保留的来源

本节是**源码接口设计，未实现／未执行**，不是已经注册的新 API。

最窄独立消费者只需读原完整 definition、实际 recipe/current ten identity、原 cut leaf盒与 source receipt，重用72c的原合法值树。对准确名字、piece anchor/width 与 support2 的真实同一表达式索引全部一致的 negative-speed-coast 分支，返回(481.3)、(481.9–10)的完整合法范围；其余piece仍用原72c完整调用。身份核对只是确保公式作用于它所证明的对象，不是半径／秩／精度前门。

拟输入合同：

- 固定72c source/schema和完整DAG/三个真实support/十control terms；
- 本次真实十个准确有理词，不能默取旧九或factory初点替当前末点；
- 原 $R_A,I_A,S_1,\kappa$ 的准确来源，原正宽度 $[\ell]$；
- 一个完整闭 local 区间 $T\subset[0,1]$；用于公共u消费者时另保全部原候选分支来源；
- 与原求值相同的clock／cell／depth资源范围，无独立fixture或科学通过门。

拟输出合同：

- 完整 a/as/ass 合法盒，所有原参与参数/宽度/区间/源身份；
- 原 strict-domain predicate 的结果，不能仅回速度true就写全域true；
- 未决／未访／原异常全保；所有原419片、全部十项、inside/outside与闭端点都不减少；
- 若取原界与新界交集，保两份实际原界来源；不以空交集作为数学域反证；
- 只保存本次Actions临时完整账本与必要原结果，不复制原大raw或重标旧72c身份。

既有165可复用的纯公式接点是 bernstein_enclosure、CompleteTarget._base_polynomials 的准确coast分支、_add_supports 与全多项式合并思想；其整个九族binder／literal-reference流程不应直接套到十族。若以后推广全十piece，support1必须纳入xi/b4、保degree10全部系数，其他分片保持各自真实domain。当前最窄coast分支不需要复制或改名整个94KB消费者。

本设计不对IEEE数值shadow作逐字等价承诺：准确代数先约简与重新区间化改变的是包围程序，不是原数值BVP算术图。原 numeric compiler、原三活动／七冻结配置、完整native/J/FD/453→450和全部最终门可保持原字节。

## 11. 本次能与不能归责的最终界限

actual205确实提供了集中于coast的原未决地址，但旧reader没有导出每个未决叶的完整 a/ap/app 科学盒。现有证据不足以在以下原因之间作唯一归因：该固定准确点严格域条件本身失败；合法C叶盒/其直积放宽过宽；重复宽度／多项式区间依赖；有限depth和300s预算。它们也可能共同出现。

本文严格证明了一个可去的重复量机制及完整替代包含；并保留真正上游不确定性和公共坐标责任。没有证明 actual205 通过重写即可取得完整域，也没有新参数点、数值速度界、严格反证或下一实验结果。已刊 R453 仍是唯一 actual205 结论，运行中的212／204／211不能由本纸证预判。

若后续实际执行上述独立包围，它应在原完整链中返回新的真实范围；此处不另设前置审核／短跑／测试，不修改已冻结请求，不占一个新科学job。
