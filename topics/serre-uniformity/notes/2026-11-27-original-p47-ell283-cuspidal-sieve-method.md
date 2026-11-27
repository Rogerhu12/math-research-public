# p47 / ell283：原完整同点 cuspidal 筛选请求

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

## 新任务和已认证输入

本次执行 R1073 的新辅助筛选，固定 $p=47,\ell=283,c=5,\delta=5$。
输入是 R1072 真实 run45925829303/job140266778118 已认证的全部
235 个原 coarse 圆盘、235 个完整十维 global 候选。
旧输入由钉住的原 consumer 重建，并强制比对原角色与 coarse-point SHA-256；
这只是为新比较消费已成输入，不重开旧结论，也不计算旧 scalar、
最低泛函或 p41 窗口。

全部数学来源是 R1071 §§11–17 和 R1073 §§1–9。
脚本只在本公开仓库 Actions 执行，root/global 已全文纸审。

## 完整原辅助行

枚举全部 $j\in\mathbf F_{283}$。一般 $j$ 用一个 quadratic representative；
$j=0$ 保六个 sextic twists，$j=1728$ 保两个 quartic twists。
总共 289 个模型表示，不将这个数称作原曲线点数。
逐模型实际点计数给 trace；R1073 的
$283<47^2/4$ 排 scalar，只有 irreducible Frobenius 有 fixed necklaces。

对每个有贡献模型，以完整 Frobenius 阶 $f\mid48$ 构造实际
$\mathbf F_{283^f}$，按 exact trace recurrence 求曲线群阶。
先除去群阶的全部 $47$ 部分，再从非零 Sylow 点逐次乘 $47$
取得真正非零 $P\in E[47]$；不能用群阶除一个 $47$ 的错误 cofactor。
取 $Q_0=\pi P$，核实际 characteristic equation 和独立性；
真正 normalized Miller pairing 给 $\zeta_{\rm nat}=e_{47}(P,Q_0)$，
并核 $e(P,2Q_0)=e(P,Q_0)^2$。

全部原 necklaces 由
$$
J=\begin{pmatrix}a&b\\d&-a\end{pmatrix},\quad
a^2+bd=5,\quad J\sim-J,\quad AJA^{-1}=\pm J
$$
列出。非零 trace 恰一条，trace zero 恰 25 条。
实际 Cartan basis 为 $(P,JP)$，真实 root 是
$\zeta_J=\zeta_{\rm nat}^d$；不替换为未经运输的任意 root。

## 完整 half-orbits 和真实 base-field 乘积

native 半点共有 1104 个。每条完整 Frobenius half-orbit 只真评价一次
原 $\psi_5$，然后逐次 Frobenius 得
$$
W_O=\prod_{i=0}^{|O|-1}\psi_5(P_O)^{283^i}\in\mathbf F_{283}^\times.
$$
必须用实际 half-orbit 长度，不能使用 ambient extension norm；
trace zero 的 full order 为四，而 half-orbit 长度为二。
逐 orbit 核实际 closure、符号、$\psi_5$ 非零与 base-field 下降。

对每个 stable $J$，用原
$v_1=w/d,v_0=u-aw/d$ 按 $[v_0^2-5v_1^2]\in\mathbf F_{47}^\times/\pm$
分组。逐组核整 orbit 标签恒定、48 个半点重数和总数 1104。
所有 $S_h$ 都是这些真实 $W_O$ 的 base-field 乘积。

在真实 $\zeta_J$ 下计算 R1073 的完整两侧 $D_\chi,B_\chi$；
不在大域中误用 Kummer 指数。这里 base-field 指数是
$(283-1)/47=6$。
固定 prime-field 最小 primitive root $\zeta_0$，写
$\zeta_J=\zeta_0^a$，然后按已经证明的
$$
D_\chi^0=a^{1-R}D_\chi,\qquad
a^{1-R}B_\chi(\zeta_J)=B_\chi(\zeta_0)
$$
运输；后一式逐点核准。全部候选在共同 root 下用同一个完整向量
$(C_\chi B_\chi(\zeta_0))_\chi$ 匹配。
任何 $B_\chi=0$ 坐标仍要求相应 $D_\chi^0=0$，不作除法。

最后加入 R1073 (A20) 的全部 23 个 rational cusps；
同一行所有角色用同一个 cusp $h$，并真正计算所需
$B_{\chi^2}$，即使 $\chi^2$ 不属于实际 $V$。
只有一个完整 affine/cusp 行同时通过全部十个角色才保留候选。

## 八个原 CM 输入的独立定位和控制

R1071 §17 从经典 CM 表和逐项原惯性论证支付八个已知输入：
$$
j=0,1728,-3375,8000,54000,287496,-12288000,16581375.
$$
$j=0,1728$ 是已认证原模型的中心。
其余六项用同一 good short equation
$A=3j/(1728-j),B=2j/(1728-j)\pmod{47^2}$，
按已证明的原 Hasse 梯度求旧 $t_*$。
以这个新的 marked first lift 重新求原完整 profile 的 constant vector，
必须与 235 输入中的相应整向量相同。
这是新的 CM 输入识别及独立来源核验，不预设辅助筛选答案。

六个 $j=0$ auxiliary twists 的固定-root 标签必须相同并保留真实 $j=0$
候选；全部八个 CM 标签都必须在最终筛选中保留。
这些控制不能替代全部原模型/necklace/cusp 的实际枚举。

## 预算、源码与输出

只用一个公开 Actions job；总数学预算 600 秒、预留 30 秒，
workflow 的 15 分钟仅作为安装/调度外限。
python-flint 固定 0.9.0，所有算术都是 exact finite-field/integer arithmetic。
先核实际 Actions 环境、仓库、请求 SHA、源码和两 README 的 SHA，
并核 source commit 等于 GITHUB_SHA，再导入算术。

全部 torsion/orbit 明细、tag vectors 和完整输出只留 runner scratch，
不上传 artifact/Release，不提交可重算 raw arrays。
stdout 仅保原输入/相位/特殊模型、进度、最终 survivor IDs、
来源/run/attempt、SHA-256 和预算回执。
排序后的 fixed-root 标签集合不依赖 finite-field 模型或 native basis 选择。

若失败或预算终止，仅输出准确完成范围与失败回执；
不能据此排除未完整消费的候选。
即使最后只剩八个 CM 标签，也只证明有理点只能落在这些原盘，
仍须另证盘内唯一性，不能写作 Serre 或 p47 点分类已经完成。
