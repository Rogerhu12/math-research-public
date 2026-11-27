# TQC：完整 OT 到真正 low96 Theta 方阵的首次实际目标

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**已证明的实际计算合同；尚无本目标的实际数值。** 数学接
[TQ](../results/R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md)
和 [TQL](../results/R149-supplement-exact-low-model-isometry-and-Theta-square-error.md)。
只有整个 OT 实际成功后，generator 才能形成 manifest/workflow。
没有原实际 result 时不预填 run、carrier SHA 或 gate outcome。

## TQC.1 完整输入与两个原空间

输入是 OT 的整 manifest、actual、execution 和原全部 current/native
闭包：IR、ASR 的所有完整前件、selected member、真正角变换、原
reflection phase、两 physical mean、原 CYA high scope 全保留。
ASR 的原失败记录也作为其完整闭包继承，不能用成功的几个标量替代
任何 whole 结果。所有外层 metadata 先调用各原 owner 的完整准入，
再调用原 worker 的整输出 validator，并核实际结束与返回码。

原空间和归一实基保持

$$
 v_n^a(x)=\sqrt2\cos(4nx-2na),\qquad
 u_n^b(x)=\sqrt2\cos(4nx-2nb-\pi/4),
 \quad a=2\mathcal H(0),\quad b=a+\Omega.
$$

输入坐标为前96个 $v_n^a$，输出为原完整 $V_Q$ 的96个 source/root
坐标；不是 SC physical/incoming matrix 的换名。

$$
 T=\Theta E_{96}^a=V_Q\overline G E_{96}^a,
 \qquad \overline G E_{96}^a=E_{96}^b,
 \qquad \|E_{96}^b\|=1.
 \tag{TQC.1}
$$

该精确 low model reference 只来自原定义；不假定真正 physical low
PDE inverse。完整原 moving mean 和 high Cayley 参数继续留在 OT
整模型与其资格中，不能因此消除两独立 mean slots。

## TQC.2 必要恢复全部原载体，不重复旧范数

原 OT 大载体仅在 runner，新的 consumer 必须重物化原有限 witnesses。
先在独立子进程中调用原 carrier-only IR/ASR 恢复：前者固定 Haswell，
后者保持 `OPENBLAS_CORETYPE` 未设，全部六线程变量为1；原 immutable
Python 容器、320-bit arithmetic、原每个完整 SHA 要求不变。
原 SN 端点、ASR raw192/grid/alpha2048、IR grid/trial 的 whole SHA
全部核对后，才恢复 OT 本身的完整 finite rows。

`fourfold_codazzi_original_Theta_trial_restore.py` 从整个已准入 OT owner
提取两个原字面代码段：完整两个原 finite trials 的读取；完整 DT
同号 row action、model multipliers、model balls 与 dyadic rows 的形成。
这两段的 SHA 分别为

`b8477204bcc9678a7660a3d5200af97d3a84d52d0c7a8fb71e54e893dfd8dba0`，

`58a8d2914eeb5d9275b0120206a60b16067381875a1d47d317e4f18f4b41510e`。

中间旧 TP norm/error 段及末尾旧 TM rounding/error 段不进入程序。
这些纯旧 norm 函数不改变 carrier 输入或 arithmetic context；省去它们
不改变原 finite carrier recurrence。helper 还禁用全部这些完成目标
的函数，并静态拒绝恢复段中的相关调用。后继只接受**四份完整**
原 receipt 的逐字段相等：DT rows、model multipliers、所有 model balls、
全部 $96\times2240$ exact dyadics。真实模型输入记录也必须与原 actual
相同。局部矩阵、几个行、norm 或新舍入中心不能替代整 SHA。

由原算法同输入、同算术顺序和同完整字节 identity，这只恢复原有限
witness，不再执行旧科学误差/norm 目标。所有科学运算仅在公开 Actions；
本地只读 source、bytes、AST 和 metadata。

## TQC.3 新的完整 low model 误差与两个 whole 候选

令 $\widehat T$ 是原完整 exact-dyadic matrix 的前96列；其原始
binary64 bytes 直接按完整行截取，不重选中心。对原 model balls
$\mathbb T_{jn}$，形成全部9216个新半径的联合界

$$
 e_{\mathrm{low,model}}=
 \operatorname{up}\sqrt{\sum_{j,n=1}^{96}
          \sup_{t\in\mathbb T_{jn}}|t-\widehat T_{jn}|^2}.
 \tag{TQC.2}
$$

原 DT evaluation、真实 $b$ phase ball 和 model arithmetic 的费用都在
这些完整 balls 内。读 OT 的整个 $e_V$ record，由 (TQC.1) 和 TQL 得

$$
 \xi_{\rm low}=e_V+e_{\mathrm{low,model}},\qquad
 \|T-\widehat T\|_2\le\xi_{\rm low}.
 \tag{TQC.3}
$$

该 $e_V$ 已付原全部无限 source/IR/model 误差，限制输入不删除任何
其中的 tail，也没有另乘 $\sqrt{96}$ 或 high model 常数512。
原 OT 最后一个完整 $e_\Theta$ 作为 verbatim copied global 候选保留。
整个新 $\xi_{\rm low}$ 与整个旧 $\xi_{\rm global}=e_\Theta$ 均保存、
读回后，才选择 $\xi=\min(\xi_{\rm low},\xi_{\rm global})$。没有从
旧全局 upper 中扣减局部 upper。

## TQC.4 真 signed 方阵及严格门

公开 owner 对完整 $\widehat T$ 形成一次 binary64 inverse proposal，
把其全部 $96\times96$ entries 保存成 exact-dyadic matrix $B$。
proposal 不作任何证明。若浮点 inverse 非有限或报 singular，选择
完整 $B=0$ 并明确登记 proposal outcome；后面的严格门照常形成。

对任意这个 exact $B$，先形成每一 signed entry

$$
 R_0=I-B\widehat T,
 \qquad b\ge\|B\|_2,\quad r_0\ge\|R_0\|_2.
 \tag{TQC.4}
$$

每个乘积保全96个 signed summands，之后才取绝对值。对 $B$ 和 $R_0$
分别保存完整 row-sum upper、column-sum upper、其 Schur 二范数候选
以及完整 Frobenius 候选。两个全矩阵 norm 候选均保存、读回后才选
整 upper；不逐行或逐项混取不同分解。全部 signed residual entries
也保存其完整 private receipt。

由 (TQC.3--4)，

$$
 \|I-BT\|_2\le\rho:=r_0+b\xi.
 \qquad
 \rho<1\Longrightarrow
 T^{-1}\text{ 存在},\quad
 \|T^{-1}\|_2\le\frac{b}{1-\rho}.
 \tag{TQC.5}
$$

这是有限同维空间上的 Neumann 论证。整个 $\rho$ 先保存读回，严格
比较其上端点与1；通过才输出完整 inverse upper。若充分门不通过，
完成对象保存 `finite_coordinate_inverse_proved=false`，inverse record
为 null；这不证明 $T$ 奇异。特别 $B=0$ 时 $R_0=I$，故任何合法
上界均有 $\rho\ge1$，不会因 proposal fallback 获得假阳性。

十一条固定新目标依次是 low model radius、low square error、$B$ 的
四个完整 norm records、$R_0$ 的四个完整 norm records、最后完整
$\rho$。严格门及条件 inverse upper 另存为不可省略的整个 conclusion。
`complete=true` 只表示全部这些实际目标与门 outcome 已完成，不能
单凭它冒称门通过。

## TQC.5 后续义务与唯一实际入口

新增 source 是 `fourfold_codazzi_original_Theta_trial_restore.py`、
`fourfold_codazzi_original_Theta_low_square_inputs.py`、
`fourfold_codazzi_original_Theta_low_square_owner.py`、
`fourfold_codazzi_original_Theta_low_square_public_worker.py` 和
`make_original_Theta_low_square_manifest.py`。generator 的唯一运行输入
是已完成的 `--OT-run`；不存在成功 whole actual 时不输出 manifest。
后者一旦齐全，不再增加独立复核门，直接生成首次公开入口。

只有真正 $\rho<1$ 的 outcome 才能进入 TQ 的 exact constraint chart。
该 chart 随后造成的 finite-rank high feedback 仍按 TQ 的完整公式支付。
本目标既不构成 physical PDE inverse，也不完成真实 high solve、
两 physical means、true $\nu$/phase、整张 full Schur 或非线性闭曲面
嵌入族。大载体仅保存原配方与整 SHA，不提交或上传 artifact/Release。
