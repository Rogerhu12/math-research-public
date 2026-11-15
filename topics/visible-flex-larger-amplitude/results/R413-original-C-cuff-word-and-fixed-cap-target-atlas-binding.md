# R413：原 C 的 cuff 字词、固定帽目标与实际同场绑定

作者：geometry agent（AI）。日期：2026-11-15。

## 413.1 结论与范围

本项支付一个具体来源缺口：把 [R409 完整 current-C 径向／shared-B 构造](R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md) 的 `plan.cuff` 固定到**同一个当前十参数目标所携带的原 `physical_parameters.rCuff` 字词**。由该原半径、原模型 C 的深端定理及原固定帽定义，得到两 cuff 的同目标 $C^2$ 张量衔接。它没有把几何背景 $B$ 的导数变成目标斜率，没有重选全局 warp，没有移动原 cut 或 natural $R_{\rm out}$，也没有把整个目标定义为 $F_0^*e$。

这不是新的深尾极限定理。[R286](R286-original-stored-continuous-integral-and-metric-bridge.md) 第286.9—286.10节已证明原允许深根族在原内 cuff 的端点性质；[R294](R294-nine450-exact-C2-seams-and-target-atlas.md) 第294.8.2、294.9.1节已给出它与固定平帽目标的兼容。这里补的是这两个定理与当前准确连续十族、真450 checkpoint、R409 closing plan 之间的实际字段连接，并给出无需开方舍入的帽内平坦环带。

本轮没有真实非零 current-C 十族的 accepted450 输入，也没有执行本源。所有结论按下列实际来源条件陈述；没有数值 $E$、metric 阈值、曲率、reach、held、全像或最终闭面成功证书。旧有限 Gauss 十族的实际185／189结果不能成为本源的 current-C accepted 父。[R298](R298-original-finite-Gauss-clip-seam-and-same-target.md) 的旧有限对象与连续模型之分仍保持。

## 413.2 原半径的完整来源

当前连续 C v3 源是

`geometry_20261115_stored_continuous_E_cover_v3.py`

其 SHA256 为 `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`。

该源 `bind_inputs` 先把可选 `ready` 外层剥除，然后从

```text
ledger.rationalDeepModel.physicalParameters.rCuff
```

读取原数值。它把 `rCuff`、`oldCut`、`epsilonScale`、`prefixRByCell` 列在 `DERIVED_KEYS`，逐原 IEEE 数值字词与

```text
stored.storedMetricAdapter.physicalParameters
```

中的同名项比较。原输入版本为 `869436630c99aa5a68afb55bd8877c826034d117`；原三输入、160个有限浅 cell 参数、原全局正 warp、全部相关源码均由该 binding 绑定。`rCuff` 不是按照当前 BVP、当前采样的最内节点或新背景 $B$ 重新拟合的量。

在 [R400](R400-current-continuous-ten-frozen450-and-complete-prefix-metric-binding.md) 的连续十族链中，原对象继续沿下表进入真450：

| 层 | 准确字段／约束 |
|---|---|
| 连续十族准确 definition | `continuous_tail.actual_input_binding.physical_parameters.rCuff` |
| 同一 current target identity | `original_complete_C_input_binding.physical_parameters.rCuff` |
| 真450 checkpoint | `current_target_identity.original_complete_C_input_binding.physical_parameters.rCuff` |
| R413 输出计划 | `cuff` 为上项原数值的逐字复制；另外记录原 little-endian binary64 word 和准确有理值 |
| 冻结 R409 原入口 | `checked_plan` 继续读取这个计划，并独立保其原 `cuff < rFar < cut-W < cut` 全布局检查 |

R413 读取 checkpoint 的原 manifest、原 factory result、原准确 definition，并核它们的完整文件 SHA 和相互 descriptor。当前十个原 word、准确 dyadic 表、目标身份、原 C binding、原 factory source 及原 cut 均必须对应。**不**把 factory 初始参数强行等同当前 BVP 的末参数；当前点仍由 R400 的完整十词身份给出，factory 定义保同一个准确参数族。

本适配器只读取上述元数据与表达定义，未重读完整450数组、完整338×112响应或原所有接受记录正文。它不凭 manifest 的成功标记重新认证 accepted。实际 field 的完整认证仍由原 R400 checkpoint／SavedPrefix 和 R409 loader 执行；这里没有增加第二套 BVP 门，也没有替换任何原门。

## 413.3 为什么原端点可以直接使用

记原输入给出的准确 dyadic 半径为 $c>0$。对每个原允许的准确深根序列，在 R286 的声明 C 中，原深段以

$$
r_o(s)=c\exp(s/\sqrt{12})
$$

定义，从 $r=c$ 向外。原 $d_0,c_0,\epsilon_{\rm phys}$ 和所有 root 条件保留；特别是 R286 已使用的 $0<d_0\le1/10$、$0<c_0\le1/16$、$R_n=64$、$n\ge160$ 及原根盒 $[1/2,2]$。R413 不选一个中点根，也不把某次包围盒任意点指定为共同准确 C。

R286 给出了覆盖全部深 cell 和原根族的界，使

$$
E_C(c)=1,\qquad (E_C)_r(c)=0,\qquad
(E_C)_{rr}(c)=0. \tag{413.1}
$$

这些是连续端点迹，不是有限节点的近似值。深端的 $w$ 只需相应的 $C^1$ 控制；$E_C=1+w^2$ 的额外衰减支付二阶平端。R413 引用该既有证明，不重算无限深尾。

局部 cuff 结论只使用靠近 $c$ 的完整深段定义和上述统一界；整个有限头与深段的保护接口、1440片完整径向覆盖以及 cut 是否落在 natural 定义域中，仍是其原本独立责任。没有把“局部端点已定义”提升为“完整有限头已算完”。

自然外端与此相反：R294第294.9.2节证明原正数据下 $E_C(R_{\rm out})>1$，并给出非零一、二阶迹。这里不把 natural 外端平延拓，不把它重名为原 binary cut，也不把任何未付源后缀填成平面。

## 413.4 固定帽和明确的平坦内环带

采用 R409 已冻结的完整帽定义。在同一 Cartesian 材料图 $X=(x,y)$ 上，两帽分别为

$$
F_+(X)=(X,H+b_+(X)),\qquad
F_-(X)=(X,-H-b_-(X)), \tag{413.2}
$$

其中

$$
b_\pm(X)=\sum_{i\in I_\pm}
A_i\left(\max\left\{0,1-\frac{|X-z_i|^2}{\rho_i^2}\right\}\right)^4. \tag{413.3}
$$

原 `upper` 字段区分两侧；同侧全部 marker，包括重叠者，先求和，再形成度量。$H$ 可为任意有限原值，不是这个目标衔接所需的正性条件。$\rho_i>0$ 和支撑严格在半径 $c$ 的盘内是冻结 R409 已有的构造条件。

由于 $t\mapsto (\max\{0,t\})^4$ 为 $C^3$，有限和 $b_\pm$ 至少为 $C^3$。两帽的既定目标均为

$$
g_{{\rm cap},\pm}=I+Db_\pm\otimes Db_\pm. \tag{413.4}
$$

下帽的整体反射与法向取向不改变该张量。$H$ 的导数为零，亦不进入它。

实际计划使用原有限字词作为准确 dyadic。R413 对每个 marker 记录

$$
D_i=(c-\rho_i)^2-|z_i|^2>0,\qquad
\delta_i=\frac{D_i}{4(c-\rho_i)}>0. \tag{413.5}
$$

它不通过浮点平方根估算支撑距离。由

$$
c-\rho_i-|z_i|
=\frac{D_i}{c-\rho_i+|z_i|}
>\frac{D_i}{2(c-\rho_i)}=2\delta_i
$$

得到全部 marker 都严格离开 $r\ge c-2\delta_i$ 的区域。令

$$
\delta=\min\left(\frac c4,\min_i\delta_i\right)>0, \tag{413.6}
$$

无 marker 时取 $\delta=c/4$。于是两帽在完整闭内环带

$$
c-\delta\le |X|\le c
$$

上准确满足 $b_\pm=0$，因而 $g_{{\rm cap},\pm}=I$，其所有一阶、二阶 Cartesian 导数为零。这个环带在**帽内侧**；没有声称原 C 在 $r>c$ 的邻域恒等于1，也没有添加一个新的径向目标环带。

## 413.5 同一目标的 cuff 公共图

取原材料角 $\theta$，在 cuff 邻域用

$$
X=(r\cos\theta,r\sin\theta),\qquad r>0. \tag{413.7}
$$

这不是把原物理角 $\phi$ 改名为 $\theta$。R409 的活动片已用完整同场材料映射复合；在 cuff，完整非平凡 Fourier 系数的012迹为零，留下同一个材料圆。该共同材料身份由 R409 原 full-112／mean／registration 合同承担，R413 不另造角参数或旋转旧静态 pair。

原尾目标在(413.7)中为

$$
g_T(X)=I+\bigl(E_C(|X|)-1\bigr)
\frac{X\otimes X}{|X|^2}. \tag{413.8}
$$

$c>0$ 使径向单位张量在整个 cuff 邻域光滑。由(413.1)，(413.8)从尾侧的值、所有一阶和二阶 Cartesian 迹分别为 $I,0,0$。帽侧由(413.6)有相同迹。故两个原张量在这一个公共图上定义 $C^2$ 正定目标张量。

正定性来自尾侧 $E_C=1+w^2\ge1$ 和帽侧 $I+Db_\pm\otimes Db_\pm\ge I$。它没有使用几何 Hermite 背景 $B'$，也没有用有限场的近似 metric 残差代替准确目标。帽的相对误差恒零只指同一固定帽定义(413.2)与其已选目标(413.4)；它不自动支付活动 collar 上的误差。

本构造精确保留原尾上 $E_C(r)dr^2+r^2d\theta^2$、原前缀完整十族目标以及原两帽既定目标。它只是把此前独立给出的两侧连接到它们共同的正确原半径，未改变任何一侧的张量。

## 413.6 为什么不能任意挪 cuff 再说“只是换坐标”

这一段只说明当前选择的必要性边界，不作为新的数值接受门。

对一般半径 $c_1>0$ 的原圆周，在

$$
g=E(r)dr^2+r^2d\theta^2
$$

中其单位切向为 $T=c_1^{-1}\partial_\theta$。直接由 Christoffel 公式得到

$$
\nabla_TT=-\frac1{c_1E(c_1)}\partial_r,\qquad
|k_g|=\frac1{c_1\sqrt{E(c_1)}}. \tag{413.9}
$$

固定平帽的相应边界圆有 $|k_g|=1/c_1$。如果 $E(c_1)>1$，两侧的边界测地曲率大小不同。一个保持原边界弧长身份的 $C^1$ 度量拼接必须给出相同的这一内蕴量（两侧外法向采用相反符号），因此不能仅通过重新命名横向坐标消除该冲突。

这不声称任意非原半径都不可能关闭，也不排除另一个明确的新构造。它只禁止把“旧固定平帽＋原尾截断在任意 $c_1$”未经证明重标为同一个光滑目标。本源直接选原 $c$，因此不需要测试未来 $E(c_1)$ 是否碰巧满足某条件。

R294 允许原内端的合法平坦延拓，但本源没有选它作为额外计划，也不把 $r<c$ 的 v3 域外查询称为已付。生成的 `cuff` 始终是原 `rCuff`，不增加自由度。

## 413.7 与完整闭面 atlas 的准确分工

局部 cuff 支付后，完整闭合目标仍须在所有原拼接处使用同一个 atlas。至少以下责任保持：

1. 当前同一准确十族半径、原 core 与所有内部段真实为所声明的正、$C^2$ 对象；不能从数值 compiler 的 `ap/app` 标签推出这一点。
2. 中央反射处原目标的真实一阶迹匹配，原 R249 几何投影不改变目标。
3. 原 C 有限头、深段保护接口和整个所用径向域确为同一个准确族；原 cut $R$ 必须在它的真实 natural 定义域内。
4. prefix↔tail 的几何图与准确目标图必须一致，不能为几何采用一组数值 $v,b$，为目标偷偷采用另一组准确 $v,b$。
5. 同一原材料角、完整相位、反射和固定帽身份沿全部片保持；完整空间／相位覆盖与几何估计另付。

特别地，设准确前缀弧长变量为 $s$、数值存储变量为 $s_{\rm num}$，令 $\kappa=L_{\rm true}/L_{\rm num}>0$。前缀目标为

$$
\kappa^2ds_{\rm num}^2+
a_{\rm true}(\kappa s_{\rm num};p_{10})^2d\theta^2.
$$

若尾的同一 cut 图记为 $r=\gamma(s_{\rm num})$，准确弧长选择给出的 cut 迹应为

$$
\begin{aligned}
\gamma'&=-\kappa E_0^{-1/2},\\
\gamma''&=-\kappa^2\frac{E_1}{2E_0^2},\\
\gamma'''&=\kappa^3\left(\frac{E_2}{2E_0^{5/2}}
-\frac{E_1^2}{E_0^{7/2}}\right).
\end{aligned} \tag{413.10}
$$

这是 R294(294.26)按同一坐标缩放的直接推论，没有重新选择原目标。冻结 R409 的几何补丁目前使用它明确声明的有限 `ap/app` 字词；R413 没有证明它们等于(413.10)，没有修改其补丁，也没有把这种未付写成已有 $C^2$ 全目标 atlas。

两个盘与中间完整环带按照原边界身份相粘，可取得连通无边界的抽象域 $S^2$；R409已说明对应几何映射的完整条件和强 $C^2$ 相位连续性。抽象拓扑闭合不证明映射浸入、单射、reach 或 held。当前 cuff 结论亦不支付 README 的 $\delta E$、$D$、$0.2D$、$0.03D$ 或 $10^{-6}$ 任何实际数值条件。

## 413.8 独立源码与实际执行边界

源码为 [geometry_20261115_current_C_original_cuff_target_atlas.py](../computations/geometry_20261115_current_C_original_cuff_target_atlas.py)，29060 B，SHA256 `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2`。

它只用 Python 标准库，且实际入口要求 `GITHUB_ACTIONS=true` 与正确 repository。依赖的科学源只读 bytes/SHA，不 import。输入是实际真450 checkpoint 及其原两个 factory 文件，加一份小 construction 参数；输出是可直接交给冻结 R409 的计划、独立 cuff target atlas 和必要结果。

`checkpoint_metadata` 逐原 descriptor 读取三件元数据，保存完整当前十词与原 C 身份。`construction_plan` 只派生原 cuff，保完整帽参数并给(413.5)—(413.6)。`atlas_definition` 明确写下同一个原目标及所有尚未付责任。`bind_loaded_shared_bundle` 接已有完整 R409 七元组，重新从该真实 target 中核原 cuff，并返回**单独**的 target attachment；它不修改 tuple、loader guard 或旧记录中的 whole-atlas 未付标志。

当前不存在真实输入或实际 run。没有本地执行、import、AST、编译、数值 fixture 或新请求。后续科学运行依原公开 Actions 规则安排，本项不是193／194的前置接受门。可重算的原字段、atlas和临时构造只在实际 job 的自有目录；永久保存源码、计划参数、run及必要输出身份。

## 413.9 与既有工作的区别

| 既有结果 | 已付内容 | R413新增的最小责任 |
|---|---|---|
| R286 | 原约定 C 的完整定义、六 primitive、深根族与 cuff 极限 | 不重复；逐实际字段绑定其原 cuff |
| R294 | 几何／目标两jet的条件、内 cuff 可平接、外端不可平接 | 不重复；把正确原端点接到实际当前 closing plan |
| R298 | 旧有限 Gauss／clip 实表达与连续目标的区别 | 不解除该旧对象问题，不将旧finite父重标current-C |
| R400 | 独立连续十族、真正453／450来源及完整prefix metric合同 | 保当前十词、准确DAG与原C来源，不重新求解或删除三行 |
| R409 | 完整新径向 Hermite/shared-B、几何两jet与七元组 | 不改两个冻结源；给原目标的 cuff 子责任与生成计划 |

本项可以作为源码／结构结论独立登记。它不等待未来 accepted 场才成立，也不能冒充未来场、完整相对 metric 或题目最终完成。
