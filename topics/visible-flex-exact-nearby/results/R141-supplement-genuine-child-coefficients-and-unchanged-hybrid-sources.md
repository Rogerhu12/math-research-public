# R141：真正 child 系数包围与不变 hybrid 源

2026-11-20，visible-exact-astra-ac637-20261120。

**纯数学结论和待接入接口；没有执行科学数值。** 本篇不改活跃 R141 的 owner、原153个 coefficient parent、155个 comparison panel、精确 dyadic 比较模型、任一已有目标或当前运行 pin。配套纯模块为 fourfold_codazzi_low_centre_child_coefficients.py，没有科学库导入、文件读写、运行入口或数值执行。

本篇处理 [R141 原定理](R141-low193-directed-green-and-complete-observation-certification.md) §2 已明确的缺口：缩小 Green 指数的时间区间，不会自动缩小 assembly 中按原 parent 保存的系数球。本篇从原已准入数据重新包围**新的子域函数值**；没有重做4650行的原 positive producer、旧 repair、旧 Z、Riccati 或任何已成范数目标。

## 1. 对象、数据和不能更换的参数范围

令原 moving 角为 $\varphi$。低坐标和返回源坐标仍为

$$
\mathcal L=((o,1),\ldots,(o,96),(e,0),(e,1),\ldots,(e,96)),\quad
\mathcal H_0=((o,97),\ldots,(o,160),(e,97),\ldots,(e,160)).
\tag{CC.1}
$$

归一化实 Fourier 基、ordinary $dr$、独立 even mean、真正 root 和原 transmission 不变。记

$$
A_L^c(r)=\Pi_L A_c(r)\Pi_L,\qquad C_{HL}^c(r)=\Pi_L A_c(r)\Pi_{\mathcal H_0}.
\tag{CC.2}
$$

这里 $A_c$ 始终是原 **WVC hybrid**：lower coefficients 使用同一 repaired degree32 centre，principal speed 使用原全族的

$$
\eta_\delta(r)=-\gamma(r)m_\delta(r),\qquad
m_\delta(r)=m_c(r)+\delta Z_m(r).
\tag{CC.3}
$$

原 admitted real $\delta$ 半径为 $10^{-8}$，且其余 intrinsic、selected parameter、compact-control 和 root 范围均保持原 admission 的完整限定。不得把本篇改称 $DF(Q^{\rm repair})$，也不得把 $m_\delta$ 填入只属于 centre 的 lower mean 行。

最小实现仅消费已经在 W2C/R141 准入的对象：

1. 原4650个完整 closed rows 及其原 candidate piece；
2. 同一 candidate index 和全部五个原 shard，exact binary64 值作为有理系数解释；
3. 原 repair 全对象中的65个 coefficient suprema；root piece 另用原已存的65个有符号 exact offsets；
4. 每行原 intrinsic 球、完整 family mean/speed 球及 independent_mean_variation_bound；
5. 原完整 root germ、root family budget 和 collar execution；
6. 原 context 的 exact reference、权 $S_i$、原 reciprocal 记录导出的 $\sqrt2$、root interval 与全部资格。

这一步**不需要**恢复 Z trial 的新 shard：原 mean 变动上界已经足够保留 (CC.3)。它也不宣称这项上界会随 child 长度缩小。

## 2. parent、child、原 row 是三种不同分割

原 assembly 在153个 coefficient parent 上先对所有原 row 交段的 $u_c,v_c,\beta,K,\gamma,\eta_\delta$ 分别取 hull，再构造 packet。随后155个 comparison panel 仅增加 cutoff joins。当前 packet_at 只读 parent 索引，不读 box 的左右坐标。

令 evaluation-domain box 为 $B=(i,a,b)$。它可以位于原155个 panel 或其准确 refined domain。要求显式 map $B\mapsto B_{\rm old}$ 给出同一个原 comparison panel 内的 affine box，并逐有理数核对两个 exact_physical_cover 相等。若原 root panel 右端为 $c$，则覆盖为

$$
\left[(1-a)r_-+ac,\ (1-b)r_++bc\right],
\quad r_-\le r_*\le r_+,
\tag{CC.4}
$$

其中 $a,b$ 应先用 refine map 转回原 panel 的归一化坐标。它覆盖所有真实 $r=(1-t)r_*+tc$、$a\le t\le b$，**不是**把 $r_*$ 换成 $r_-$。

body 的 cover 是确切有理端点 $J=[l,r]$。枚举其与全部原 row $I_\nu$ 的非空 closed intersections $J_\nu$。实现也保留在原 row 边界上的零长度交段，因此点 box 和原一侧 piece 资格不会被遗漏。逐段原覆盖保证

$$
J=\bigcup_\nu J_\nu .
\tag{CC.5}
$$

真正 $h_i$ 仍由原 domain.full_length 给出；不得用 (CC.4) 的 padded cover 宽度代替真正积分长度或 defect 中的分母。

## 3. body child 的同一 centre 与 family speed

在 $J_\nu$ 所属的原 cubic piece 上，令 $p_j(r)$、$j=0,\ldots,64$ 是原有理 cubic，$\alpha$ 是原 exact amplitude，$E_j$ 是原 repair coefficient supremum。原定义保证

$$
y_j^c(r)=\alpha p_j(r)+e_{j,\mathrm{piece}},
\qquad |e_{j,\mathrm{piece}}|\le E_j .
\tag{CC.6}
$$

其中 mean 还加上 $s(r)=1/C_{\rm ref}(r)$。用同一 cubic reader 在新的完整 $J_\nu$ 上作 Horner interval evaluation，保留65项及原 $C_{\rm ref}$ 球，即得 $[u_c]_{J_\nu},[v_c]_{J_\nu}$。这是 assembly._body_centre_fields 已具有的接口；它没有调用旧 producer。

原 intrinsic 球 $[\beta]_\nu,[K]_\nu,[\gamma]_\nu,[C_{\rm ref}]_\nu$ 在 child 上仍是有效包围。**它们原样限制到子域，不乘 child/parent 长度比。** 正 body 的 $K>0,\gamma>0,\eta_\delta>0$ 仍须使用原完整有效资格；不把这个 $K$ 下界搬到 root collar。

令 $\epsilon_{m,\nu}$ 是原 independent_mean_variation_bound 记录的有向 upper，$[m_\delta]_\nu,[\eta_\delta]_\nu$ 为原 complete_delta_bounds 中的完整球。定义

$$
[\widetilde m_\delta]_{J_\nu}
 =\bigl([m_c]_{J_\nu}+[-\epsilon_{m,\nu},\epsilon_{m,\nu}]\bigr)
    \cap[m_\delta]_\nu,
\tag{CC.7}
$$
$$
[\widetilde\eta_\delta]_{J_\nu}
 =\bigl(-[\gamma]_\nu[\widetilde m_\delta]_{J_\nu}\bigr)
    \cap[\eta_\delta]_\nu.
\tag{CC.8}
$$

**包含命题。** 对每个原准入参数值和每个 $r\in J_\nu$，真实 $m_\delta(r),\eta_\delta(r)$ 分别属于 (CC.7)、(CC.8)。

证明：原 Z/whole-family 结果已给 $|\delta Z_m(r)|\le\epsilon_{m,\nu}$，(CC.6) 给同一个 repaired $m_c$，故两个待交集合均包含同一真实 mean。再用 (CC.3) 和原完整 speed 记录，两个待交 speed 集合也包含同一真实值。逐有向端点相交仍包含真实值；空交说明新计算尚未成立，必须失败保存，不能通过删除某个因子解除。证毕。

这里没有将 $\epsilon_{m,\nu}$ 除以细分数，没有把 interval 取 midpoint 当作函数，也没有假设 family 参数可以随 $r$ 改变。对固定真参数的包含逐点成立，因而统一覆盖原完整参数域。

## 4. root child

原 collar.complete_true_collar_packet 已接受 radial_interval。把 (CC.4) 的 exact cover 传入即可重新包围同一 cubic 的子域；原 complex germ 的 real intrinsic 球、193个完整 response upper、原 exact offsets 和全参数族费用仍保留。

该函数已经以 centre mean 与原 signed mean 记录交，且以 centre mean 加完整 response mean 与原 family mean gap 交。故可进一步作

$$
[\widetilde\eta_\delta]_B
 =\bigl(-[\gamma]_{\rm germ}[m_\delta]_B\bigr)
    \cap[\eta_\delta]_{\rm old\ collar}.
\tag{CC.9}
$$

这仍是 (CC.3) 的交包围。K 使用原 germ 的完整 signed real 球，不能假定 padded cover 全部位于真根右侧。原 packet 的 $m_c$ 和 family increment 三个 ordered primitive words 均不更改；仅 centre packet 的两个同义 speed 字段 eta/actual_eta 同步更新。

## 5. 每个交段先完整 signed assembly，再作 hull

对每个 packet 原样调用 assembly._complete_signed_centre_matrix。它先计算 local signed terms，再保留整个

$$
-2\,a\,I_\varphi\Pi_{\ne0}\,b
\tag{CC.10}
$$

的中间 Fourier 正频率求和，最后用完整 centre mean row 覆盖 mean 输出。对 degree32 centre，给定输出 $(o/e,k)$ 与输入 $(o/e,j)$，全部允许的中间频率满足

$$
\max(1,k-32,j-32)\le m\le \min(k+32,j+32),
\qquad I_\varphi\text{ 的因子为 }(4m)^{-1}.
\tag{CC.11}
$$

使用全矩阵共有的较大中间集合，只增加确定为零的项；不能用固定输入截断替代 (CC.11)。原 normalized real 基的 $\sqrt2$ 与 sine/cosine signs 保持。

特别是 mean 输出仍为

$$
(A_c)_{00}=\beta(1-S_0-2Km_c^2),
\quad (A_c)_{0,(o,j)}=2\sqrt2\,\beta m_c\,u_j,
\quad (A_c)_{0,(e,j)}=-2\sqrt2\,\beta m_c K\,v_j.
\tag{CC.12}
$$

式中的 $u_j$ 采用原 ui 编码约定，含其原符号。mean 输入的非 mean rank 项也由原 local_signed_entry 保留，不能因 (CC.12) 单列而遗漏。

设 $\mathbb A_\nu$ 是交段 $J_\nu$ 上得到的完整 signed 矩阵。最终取

$$
\mathbb A_B
 =\operatorname{hull}_{\nu}\mathbb A_\nu
       \cap\mathbb A_{\rm old\ parent},
\tag{CC.13}
$$

两个运算均按矩阵 entry 的 signed 实区间进行。

**完整 child 包围定理。** 对全部原参数及所有实际 $r\in B$，
$A_L^c(r)\in\mathbb A_B^{LL}$、
$C_{HL}^c(r)\in\mathbb A_B^{LH}$。

证明：在 body 上由 (CC.5) 选取包含 $r$ 的一个交段，(CC.6)–(CC.8) 给完整同对象 packet，原 ordered assembly 给全部矩阵项。root 用 §4。hull 因而包围整个 child，原 parent 包围同一真实值，所以相交仍包含。所有乘法和 primitive 求和发生在 hull 之前，不混合不同 row 的系数而制造本可避免的交叉项。最后使用有向 interval 存储，球半径量化也须向外。证毕。

式(CC.13)在数学区间层面不比原 parent entry 范围更大；具体 Arb 球的向外半径量化可能在边界多一个舍入量。这里不由 entrywise 范围包含直接声称不同 midpoint PSD majorant 之间有 Loewner 单调性。

## 6. CHL 的三个精确支持事实

在 $C_{HL}^c$ 中，输入 $j\ge97$、输出 $k\le96$：

1. principal speed 只在 $j=k\ne0$ 的 cross component 出现，故此块不依赖 $\eta_\delta$；
2. gamma mean-rank 只在输入 $j=0$ 出现，故此块不依赖这项；
3. mean 输出 (CC.12) 只读 centre $u_j,v_j$，其支持不超过32，故完整 mean 输出行准确为零。

这三个结论在**保留完整193行和全部128列之后**得到。实现仍返回 $193\times128$ 矩阵并检查 retained mean row 为 exact zero。CHL 的 child 改善只需要 $\beta,K,u_c,v_c$；无需为这个块另恢复 Z，也不能将该事实扩大到 AL、全部 actual-family 差或 full CFB。

## 7. 原五种源的单位保持

配套 provider 的 source_matrix 接受原 model 和完整 box，明确返回

$$
W_{\rm raw}=I_{193},\quad W_{\rm tr}=S_i^{-1},\quad
W_\Delta=(A_L^c-H_i/h_i)S_i^{-1},
\tag{CC.14}
$$
$$
W_{\rm second}=(A_L^c-D_i)S_i^{-1},\qquad
W_{\rm return}=C_{HL}^c.
\tag{CC.15}
$$

原 $D_i$、$S_i$、selected diagonals、mean normalizer 和 model.generators 不变。对准确 refined cell，
$(H_{\rm parent}/n)/(h_{\rm parent}/n)=H_{\rm parent}/h_{\rm parent}$；
真实 root $h_i$ 及其不确定性始终保留。两种 constant source 不调用新 child assembly。

该函数不改变两侧 Green triangles、root97/outer96 BC、193观察 atoms、normalizer、right sides 或 Neumann identity。它只替换三个 varying source 的**包围来源**，不更换真实源。

与 [GM exact moments](R141-supplement-exact-cell-Green-moments-and-shared-output-covariances.md) 相接时，对每个完整 child $W(s)\in\mathbb W_B$，仍须先建立

$$
W(s)W(s)^T\preceq \overline V_B
\tag{CC.16}
$$

的逐点 PSD majorant。不得把 $\mathbb W_B$ 当作一个 constant unknown matrix 后直接积分。GM 的 $H/Q$ 模板、A/B/K/J 完整 output covariances仍可共享；本篇不产生额外观测或原子。

## 8. 明确接口与缓存限制

纯模块公开 WholeChildSignedCoefficientProvider。构造参数是 api、km、green、assembly、collar、admitted、original_context、evaluation_context 及 to_original_box。现有 refined domain 提供最后一个函数。原上下文和 model 均不被修改；未来 owner 显式调用 provider.source_matrix 或 provider.centre_matrix。

每次 centre_matrix：

1. 核 parent/child exact cover 相同，取所有原 row 的 closed intersections；
2. 一次只持有一个交段 packet，先完整 signed assembly；
3. 流式 hull 全部交段，并与同 parent 的既有矩阵包围相交；
4. 保存当前一个 child 的 AL/CHL 两矩阵缓存，旧 child 缓存立即释放。

parent 缓存只保存同原 panel 的 AL/CHL 两个包围，用于 (CC.13)。它不存储新 child 值。全部 row 原数据仅读，没有全历史 child 矩阵缓存。

**不得将新 provider 放入旧 ParentMomentProvider 的 parent-source 缓存而不改 key。** 原 parent-cached adapter 的数学前提正是 source ball 在同 parent 不变；本篇使这个前提不再成立。新的 varying source covariance/moments 必须按完整 child box 缓存。$H/Q$ 模板仍按原 parent/细分数共享。一次 source pass 的 private memory 可以保持一个 child，但 dense source moment 求值次数可能增加；本篇不承诺更快。

root/outer carriers、两批 source 调用次序、point-observation 阶段以及 shared private_storage_prefix 的释放规则均沿 GM 原合同。不需要增加新的公开 source 数组。

## 9. 剩余的真实限制与可选后继

最小 provider 去掉的是两个确定的包围损失：全 parent 的 radial hull，以及先混合不同原 row 再做二次/primitive 组合。它不会免费消除：

- 原 row intrinsic 球的宽度；
- 原 repair 的非零包围费；
- 原 $\epsilon_{m,\nu}$ 的 whole-family 范围；
- 同一个 child 内仍使用 interval algebra 的依赖损失；
- 原 piecewise-constant comparison 模型与真实 varying centre 的真实差；
- Hilbert–Schmidt 上界与 operator norm 之间的差。

只有已保存的 value 球时，不能从其数值宽度反推一个径向 Lipschitz 常数，也不能据细分比例缩小该球。若以后确有需要，下面是**不同的新输入/新子域目标**，并非本最小实现已经取得的资格：

1. 读取原 Z trial 全部 shard 和原 exact continuous-direction repair 全对象，只对真正 mean component96 的同一 cubic 求新子域值，以原 exact mean repair supremum支付偏移，再与原 $\epsilon_{m,\nu}$ 交。因为本 hybrid 的 Z 只通过 (CC.3) 入 principal，评 mean 在此足够；不能据此替代193维 actual-family lower 差。
2. 对 intrinsic 真定义做子域限制，必须拥有该域有效的旧 Taylor/jet 恒等式或执行新的完整 intrinsic 子域包围。旧 negative-side Taylor cover不能未经域检查延拓到整个 positive body。不得重新运行旧 producer 然后把旧目标改名为新结论。
3. 若采用精确 piece repair offsets，须从原已存原件得到同一 offset 定义和完整身份；本最小接口刻意只用原65 suprema，不重新生成原6143接缝 repair 目标。

当前活跃 R141 未结束前，这些纯定义不会启动任何重叠科学。活跃结果若已完成某个 scalar 目标，则它保持冻结；未来运行须声明新的完整 enclosure/比较目标及所复用的已成对象。更小的 child 球只是改进收缩证书的一条具体途径，不能提前登记 $\epsilon<1$、全部源已成、full inverse、7 ports 或两个原 RHS 已闭合。


## 10. 显式GM接线

[child moment provider](../scripts/fourfold_codazzi_low_centre_child_moment_provider.py)通过普通局部子类接原ParentMomentProvider，未patch旧module或model。两种constant源沿parent/count缓存；三种varying源以同一private template token加完整child box key缓存，每次经GM逐点PSD majorant。signed两三角、每格独立carrier、true h及完整mean公式继承原GI，原shared对象必须等point阶段结束才释放。它仅给新的明确source包围，不给数值收缩或运行时保证；全常量模板次数不因缓存复用冒作新增成功目标。
