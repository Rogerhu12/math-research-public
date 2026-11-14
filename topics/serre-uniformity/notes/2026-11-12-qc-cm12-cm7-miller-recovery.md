# 两条真正 based CM 点的 Miller 链：恢复及评价池变更

日期：2026-11-12。状态：实际初始点和每个已保存群运算均完成；304位全链仍在运行，尚未把中间截面或坐标称为高度。长链源文件按自身 SHA 绑定，恢复时禁止静默修改源。

## 1. 实际初始除子

使用 R160 已发布的 p41_cm_based_points47_checkpoint.json.gz。
令 $b=P_{-3}$，$P=P_{-12}$ 或 $P_{-7}$，$h=f_b/f_0$。
证书中的真实有效除子为 $E_P=\operatorname{div}(f_b)-b+P$，所以

$$A_P=E_P-D_0=P-b+\operatorname{div}(h).$$

完整199×73点空间和 Frobenius 均来自真实点值条件，不能用 Hecke 坐标等式代替这里的主函数。两条链都保留初始 $f_b$ 的固定73基系数、实际负点的199×1二次截面、每一步325×1三次截面和随机状态。

令 $s_-=q_P/f_0^2$，其除子为 $A_P+A_{-P}$。
$F_{-1}=s_-^{-1}$，而 AddFlip $R=-(U+V)$ 使用
$\operatorname{div}(s_{U,V})=A_U+A_V+A_R$，故
$F_R=(F_UF_Vs_{U,V})^{-1}$。
符号、幅度和304位整数 $m=\#J(\mathbf F_{47})$ 均随实际步骤保存；$m\bmod47=9$。

初始 $E_P$ 包含真实 $P$，因此在 $P$ 的剩余盘上 $W_{\rm init}=t$，不能误套原 $B_{-4}$ 的 $W_{\rm init}=1$。
一般局部式是

$$F_n=V_n\,W_{\rm init}^{\,n}/W_n.$$

每一步只对整单位求逆，实际端点因子必须继续保留。原始 $h$ 在 $b$ 的碰撞也须按 R148 相同线丛生成元处理。

## 2. CM12：原820点评价池

源文件 p41_cm_slp47.py，SHA256：

~~~
f3fb1acbc335b7560ddb00f31f1566be3a6eae06fdb69e47fbf6dc996df0348b
~~~

本文件的有效运行参数是 --discriminant12（实际命令中选项和值之间留空格）。
初始点在原820点评价池上允许群运算所需的单位截面。负点和后续 AddFlip 使用原模型基，不改 Frobenius 规范。

固定恢复点 p41_cm12_slp47_30_fixed.json.gz：

- 30位，45个 AddFlip，470961字节；
- SHA256 9dae214770d230ff87e783b351ca62ae3fe7aa32832cbc5a32fd35b21d2d15e9；
- 当前真实点 SHA256 b1e4f42c286760dde5775ba8a84a04264c9491d299af9afcdf1af91d40b56b58。

恢复时把固定文件复制到独立 rolling 路径，然后从该 checkpoint 续算。
不要把原 $B$ 链或另一条 CM 链的随机状态、负点或符号混用。

~~~
python -B scripts/p41_cm_slp47.py --script-dir scripts --discriminant 12 --checkpoint /tmp/p41_cm12_slp47_rolling.json.gz
~~~

## 3. CM7：819点评价池及准确原基转换

原820池的第254行在模47等于实际 $P_{-7}$，而初始 $E_{P_{-7}}$ 包含该点。
因此所有初始理想截面在这一行都非单位；继续尝试随机截面不能修复它。
最早的通用驱动尝试在初始化阶段退出，没有生成任何已完成链步，随后用新文件修复。

源文件 p41_cm7_slp47.py，SHA256：

~~~
54e31db47d6ffc8bed7c1ee5b5a859f904a0737e023046269006c370fad97aa4
~~~

删掉第254行；它是 Frobenius 固定行，所以余819行仍稳定。
所有群运算中清分母后的截面次数最多 $5\deg\mathcal L=630$，
而819个剩余点互异，故这些截面在剩余池上的评价仍忠实。
原 $V_2,V_3$ 分别保留整秩199、325；程序用单位子式重新规范得到

$$V_2'=V_2 C_2,\qquad V_3'=V_3 C_3.$$

$C_2,C_3$ 在模47为可逆矩阵。若原 Frobenius 系数矩阵为 $\mathcal A_i$，新矩阵严格为

$$\mathcal A_i'=C_i^{-1}\mathcal A_i\overline{C_i}.$$

程序逐行检查 $V_i'\mathcal A_i'=\overline{V_i'[\tau]}$。
原73维权二基不改，原平方/立方基也不在已保存数据中替换。
内部点坐标 $K'$ 每次保存为 $C_2K'$，内部三次截面 $f'$ 保存为 $C_3f'$。
负点二次截面直接由原点矩阵和实际选取系数形成。
因此所有 checkpoint 的点、主截面及后续局部评价仍可直接使用 R102/R110 原基。

换基数据的规范 JSON 哈希：

- $C_2$: 060604d6cdc93a92c83ed1c89e9c74176c55c56db2ed993772ba41904f966ca3；
- $C_3$: 8101d4f7d08d7fa1675730bb92bb3877d042a4cd79b51e8abb8813957dbc6955。

完整换基可由固定模型和遗漏行唯一重建，不另存大矩阵。
内部每步点哈希和转换后的原基点哈希同时保存，不能混同。

固定恢复点 p41_cm7_slp47_15_fixed.json.gz：

- 15位，22个 AddFlip，411435字节；
- SHA256 befa90b5a28e825a459aef82b596c1c9e8c5c3692802042c716beffc5066142f；
- 原基当前真实点 SHA256 5e95251f8934a4ca291c6518d80dd8bad83b3ef56c2fe9e8fbe6a6ddde915c35。

~~~
python -B scripts/p41_cm7_slp47.py --script-dir scripts --checkpoint /tmp/p41_cm7_slp47_rolling.json.gz
~~~

不要再用通用 p41_cm_slp47.py 的 discriminant7 路径，它不处理这一评价池相交。

## 4. 完成后的真正比较及剩余工作

两驱动最终都检查304位、正号、整数幅度恰为 $m$，并对完整除子理想进行模47零类检查。
这还不等于完整的实际形式端点运输。

R167 已保存两 CM 点在同一 R141 family0 上的 $m$ 倍形式端点：
p41_cm_formal_endpoints47_checkpoint.json.gz，
SHA256 05a194c9d7e4dc0e8a28266b18aa351a635f70be0d8d311556cff3b2e9eea0b9。
其字段为 targets[x12或x7].targets.m.exponentials[0]。
完成长链后必须实际构造当前有效除子与该形式端点间的主函数、核验完整理想，并保存该函数的固定基系数及碰撞单位。
不得仅比较 Lie 向量或把尚未求出的范数指定为1。

每步主截面保存允许之后在任意实际 CM 支撑、典范代数或 Hecke 推前代数上重放范数，无需再次执行304位群运算。
但新评价点若出现47非单位，仍须使用 R159/R160 的整盘因子相消，禁止先除47再宣称保留四位精度。

上述30/15位固定文件保留作前缀证书输入；现行恢复入口如下。B主链已由R151完整完成，勿重跑。



## 5. 现行恢复入口：180位与140位

2026-11-13 更新两个现行安全点；30/15固定证书及先前145/120固定字节均保留。

| 链 | 现行文件 | 位数/步数 | 字节 | SHA256 |
|---|---|---:|---:|---|
| CM12 | scripts/data/p41_cm12_slp47_saved.json.gz |180/271|1058436|2b94fcd501fd1b0ccfd5ba7d519cabe6be8a4fb196c285e549f07ebd219a0396|
| CM7 | scripts/data/p41_cm7_slp47_saved.json.gz |140/211|905168|4c3d3e99fb8f301312101c4f3a16f56bafad50a8fe2a514e069e22041759e30e|

复制各saved到独立rolling后续跑，CM12仍用§2原驱动；CM7使用 `p41_cm7_slp47_finish.py`，SHA `0e9b640f58efe798c3001c1e30e90498e11f05c85f40ac0bd496fc48e199ad6f`。它只释放不再使用的大输入，全部算术、RNG和原基不变，driver_history记录旧源。不要从30/15位重做。

CM7曾在120/180后因共享内存退出，已由finisher正确恢复至本次140/211；原边界在 `p41_cm7_slp47_120_fixed.json.gz`，823740B，SHA `51c5644f205934c91ecb0292c77169a326d7dcae0046212cd61258a67a07e617`。CM12先前145/217另存 `p41_cm12_slp47_145_fixed.json.gz`，918081B，SHA `1baad5a4cddcc63de6fec5570c8dbf613bbd9a7d197903b8226a7e252d4c57d6`。

两CM混合形式值见[实际混合形式值与整盘恢复](2026-11-12-qc-cm-mixed-formal-and-local-unit-work.md)，t到j的首单位见[CM参数单位](2026-11-12-qc-cm-j-parameter-and-collision-units.md)。终态完整碰撞范数仍待全链。

R178共同短组合24/24已完成，完整初始hD两范数也已核准；共同m链另用宽5有符号窗口，见[共同窗口恢复](2026-11-13-common-window-recovery.md)。R179的新S图、两CM T2主函数和六个共同正负端点已完成；不要重跑GP或形式指数。三个矩阵作业并行时，不再同时解码完整大T2 JSON；按单分支顺序读取。
