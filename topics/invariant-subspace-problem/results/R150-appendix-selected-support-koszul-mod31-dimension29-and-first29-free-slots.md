# R150 附录：原无穷远 Koszul 族的所选支撑交，模 31 维数 29

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

本条记录一次已完成的有限域计算及其严格特征零推论。它不把模 31 的新方向提升为有理核，也不重做原正常形或增加 Dixon 精度。

## 1. 同一原来源与支撑

使用已固定的原整数矩阵 $A_\infty\in\mathbb Z^{4367\times6188}$、4354 个所选原来源 $J$，以及原 36 个规范自由来源。17 个原多项式记为 $f_0,\ldots,f_{16}$。原来源逐个为次数至多 3 的单项式乘一个原方程；方程、单项式及原行号均沿实际模型保存。

按 $i<j$ 的字典序，再按 $1,m_0,\ldots,m_{10}$ 的顺序，定义 1632 列
$$
\Phi_{ij,a}=a(f_j e_i-f_i e_j).
$$
因此 $A_\infty\Phi=0$ 是原整数多项式恒等式。此前 187 列线性倍二次头的非零子式已证明 $\Phi$ 在 $\mathbb Q$ 和 $\mathbb F_{31}$ 上均单射；见 [187 与 1632 单射证明](R150-appendix-physical-infinity-linear-multiples187-and-koszul1632-injection.md)。

令
$$
O=\Phi_{J^c,*},\qquad G=\Phi_{\mathrm{free},*}.
$$
这里 $O$ 保留全部 1834 个未选来源，$G$ 保留完整 36 个自由来源。所选支撑的标准 Koszul 空间准确为 $\Phi(\ker O)$；不能把原输出的某个商空间代替这一来源支撑条件。

## 2. 实际执行及完整身份

同一公开仓库 Actions 会话的实际执行为：

- run：43679903558；
- step：koszul-selected-support-f31；
- 执行源提交：72a9ac524b51a3f99c8217e29d28d3e494d96e2b；
- 数学计时：1.575719778 秒；进程总计时：1.667543354999907 秒；
- exitCode：0；status：completed。

小回执为 [实际执行记录](../notes/r150-infinity-remote-session-789f/43679903558-koszul-selected-support-f31.json)。临时完整回执为 22081 B，SHA256 为
$0ea2d7e85aef6d6adc037a26ce0947d8db02a6a5ca4c9a690076fba0a8a3ff3b$。
执行代码为 [原支撑计算源码](../notes/2026-11-15-r150-infinity-koszul-selected-support-789f.py)，SHA256 为
$fb8045033c74de29c2d8842d13457bcde370c8de7926ea3cc39897b65a771d4d$。

本次由原整数模型直接生成 $\bar O,\bar G$，计算完整 RREF，并构造具有全部 29 个自由列的核矩阵 $Z$。实际验证了
$$
\operatorname{rank}_{\mathbb F_{31}}\bar O=1603,\qquad
\bar O Z=0\quad\text{（全部 1834 行）},
$$
以及
$$
\dim\ker\bar O=29,\qquad
\operatorname{rank}_{\mathbb F_{31}}(\bar G Z)=29.
$$
此处 $Z$ 的所有列均保留完整 1632 个 Koszul 系数；没有只验一个标量投影。

所有大数组仅保留于本次运行的临时工作目录；仓库长期保存源码、参数、运行号、小回执及哈希。

## 3. 29 维像准确是前 29 个自由坐标

实际回执保存了完整 $36\times29$ 自由像矩阵。它的最后七行全零，而前 29 行秩为 29。主代理另以该已保存的小矩阵作 V8 精确模 31 核对；这只是读取同一结果，未另运行 Actions 数学。

从而
$$
\bar G(\ker\bar O)=
\operatorname{span}_{\mathbb F_{31}}\{e_0,\ldots,e_{28}\}.
$$
此前 23 条真有理核的规范自由槽为
$$
\{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22,23,24,25\}.
$$
将这些 23 个坐标轴并入本次像后，秩仍为 29。因此在自由坐标层面，新增的六个模 31 方向准确是
$$
e_{17},e_{18},e_{19},e_{26},e_{27},e_{28}.
$$
这不证明旧 23 条有理核在特征零属于标准 Koszul 族：本次比较使用的是它们已知的规范自由坐标。

## 4. 严格的特征零范围

整数矩阵的一个模 31 非零子式在 $\mathbb Q$ 上仍非零，故
$$
\operatorname{rank}_{\mathbb Q}O\ge1603,\qquad
\dim_{\mathbb Q}\Phi(\ker O)\le29.
$$
不能反向由模 31 核维数得到 29 条有理核。特征零的额外约束可能在模 31 消失；本次也没有证明该支撑交可与模 31 基变换交换。

特别地，本次不改变此前所选原矩阵的严格界
$$
4318\le\operatorname{rank}_{\mathbb Q}B_0
\le\operatorname{rank}_{\mathbb Q}C_0\le4331.
$$
要降低右端，必须构造真实有理来源并付原整数完整乘回及自由坐标独立性。

还有一个有用的条件性非成员判据。令 $D=\mathbb Z_{(31)}$。已付的 [原来源左逆](R150-appendix-standard-koszul-original-source-left-inverse-and-membership.md) 给出 $\Gamma\Phi=I$，其中 $\Gamma$ 在 $D$ 上有定义。因此若未来得到一个 $D$ 整来源 $v$，支撑于 $J$、满足原核身份，且其完整自由坐标恰为 $e_j$，$29\le j\le35$，则
$$
v\notin\operatorname{im}_{\mathbb Q}\Phi.
$$
否则 $v=\Phi c$，由 $c=\Gamma v\in D^{1632}$ 可约化模 31；其外支撑仍零，而自由坐标为 $e_j$，与本节前述最后七行恒零矛盾。这里没有断言这七个规范真有理核已经存在，亦未对其余不满足这些条件的来源作非成员判定。

## 5. 下一精确接口

本次 1603 个模 31 枢轴可以用来选取原整数 $O$ 的一个真正可逆有理子块。解该原整数子块后仍须核全部 1834 条外支撑方程；若出现剩余约束，应在完整 29 个待定方向上精确求其核。每条保留的有理方向最终须回到全部 6188 原来源，核所有 4367 个原整数输出，并以完整 36 个自由坐标与旧 23 条核比较有理秩。只有这些原身份完成后，才可登记特征零新增维数。
