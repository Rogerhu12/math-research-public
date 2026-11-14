# 当前修补 M32 背景上的已知高频源：只消费完整方向的第 33–96 模

这是公开 Actions 的新有向消费者合同。它读取已完成的原 40 份、7,721 格连续标量证书、原完整 193 态三次多项式、准确连续方向 $Z$ 及其全区修补费；不重算目标函数、原残差、均值流或 trial。实际通过前不登记新数值结论。

## H.1 同一科学对象与范围

背景固定为原候选 ac1d5b98… 的准确连续 M32 修补，definition
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
物理参数为原 $\eta_0,\nu$，仿射偏移为零。不是物理 $\eta=0$。

方向是完整 193 态物理 trial ed42a71d… 的连续修补 $Z$，
definition
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。
其原生修补证书为
`87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88`。
它保留全部 even mean；不能改称均值完成的 $q^*$，也不能改称真正 PDE 响应。

当前 $Q=(u,v)$ 的准确角支撑为 $|j|\le32$，$Z$ 为 $|j|\le96$，
角频率为 $4j$。本文只适用于系数家族 $\delta=0$。$\delta\ne0$ 后背景含第
96 模，以下支撑相消必须另外付费；未知无限高输入也不属于本合同。

令

$$
h=P_{33\le |j|\le96} Z,\qquad Q_0=\|Q\|_{A^0},\quad
Q_1=\|Q_\varphi\|_{A^0},\quad
H_0=\|h\|_{A^0},\quad H_1=\|h_\varphi\|_{A^0}.
\tag{H.1}
$$

pair $A^0$ 取两分量 Fourier 绝对系数和，支配归一化圆周上的 pair $L^2$。
原反射类实正弦/余弦振幅的绝对和恰给相同费用，不再加 $\sqrt2$。

## H.2 精确相消后只有三个已知高源

原完整 moving 算子记 $D=\partial_r-A$。设
$S=u^2+Kv^2$、$d=-\beta I_\varphi S$，则其角主项为
$d h_\varphi+\gamma m J_Kh_\varphi$。反应矩阵可写成
$\beta\operatorname{diag}(-1,1)$ 加三次系数的零阶部分；非局部项为

$$
-2\beta Q_\varphi I_\varphi(uh_1+Kvh_2)
+\gamma\langle h_2\rangle J_KQ_\varphi .
\tag{H.2}
$$

这与原 `fourfold_codazzi_nu_full_adjoint_kernel.py` 的完整两行一致；
这里没有投掉原独立均值方程。

对于 $P_{\le32}Z$，二次系数带宽 64 及两次 M32 卷积均最多产生第 96 模。
$I_\varphi$ 只删均值，不扩支撑。原参数源 $F_\nu$ 的完整角支撑也至多为 96，
包括其误差余项，因为它来自同一准确有限三次公式。

对于 $h$，$h_r$、$\gamma mJ_Kh_\varphi$ 和
$\beta\operatorname{diag}(-1,1)h$ 都仍至多第 96 模；其 even mean 准确为零，
故 (H.2) 的 mean rank 项准确消失。因此

$$
P_{\ge97}(DZ-F_\nu)=-P_{\ge97}Ah ,
\qquad \operatorname{supp}P_{\ge97}Ah\subset\{97,\ldots,160\}.
\tag{H.3}
$$

这里是作用于已知 $Z$ 的准确支撑恒等式。它不说明未知高解为零，也不改变
任何 low193 或 mean 残差。

令 $K_*=\max(1,|K|)$。四倍频 primitive 的范数为 $1/4$，由 pair Wiener
乘法与投影收缩得

$$
\begin{aligned}
E_d&=\frac{|\beta|K_*}{4}Q_0^2H_1,\\
E_{\rm loc}&=3|\beta|K_*Q_0^2H_0,\\
E_I&=\frac{|\beta|K_*}{2}Q_0Q_1H_0,\\
\|P_{\ge97}(DZ-F_\nu)\|_{L^2_\varphi}
&\le E_d+E_{\rm loc}+E_I=:E_H .
\end{aligned}
\tag{H.4}
$$

常数 3 分别来自 $S$ 乘单位阵和 $2Q(u,Kv)$；非局部项的系数
$2\times(1/4)=1/2$。完整 $K,\beta$ 和背景均值已保留在这些系数及 $Q_0$ 中。

## H.3 从原存储字节得到全格费用

每个原闭格 $I_i$ 读取原 `intrinsic_whole_third_jets` 中的 $\beta,K$，
取完整区间绝对上界；这些证书覆盖固定 $\eta_0$。

已完成 repair-source native

`05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4`

的逐格字段 `original_background_pair_A0` 和
`original_background_angular_derivative_pair_A0` 是原背景完整 Bernstein
界。分别加其 `exact_centre_repair_bounds.A0`、`angular_A0` 后得到 (H.1)
的修补背景全格 $Q_0,Q_1$。该原 native 的科学源 SHA 是
`6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad`。

原完整 physical trial 顺序为 odd $j=1,\ldots,96$，even mean，然后
even $j=1,\ldots,96$。新消费者在原三次系数副本中准确置零 odd 前 32 槽、
even mean 及 even 前 32 槽，只保留两组 $33\ldots96$。原
`cubic_pair_norms` 的完整三次 Bernstein 算法给全格 $H_{0,\rm raw}$、
$H_{1,\rm raw}$，不取径向采样。

$Z-\mathrm{raw}$ 在每个原 piece 内是准确常量，其全区
`direction_repair_full_interval_joint_derivative_norms["1/64"][0,1]`
分别控制两项角费用。降到 $A^0$ 并投影收缩后，

$$
H_0\le H_{0,\rm raw}+E_{Z,0},\qquad
H_1\le H_{1,\rm raw}+E_{Z,1}.
\tag{H.5}
$$

不需要新的径向 target jets，也不把有限数组 midpoint 当作完整余项。
mean 槽的准确置零在原系数层检查；浮点区间算法对零产生的包络仍留在范数中。

## H.4 与原完整界混合及真实径向积分

已完成 mixed-Z native

`365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e`

给每格原高源的 sup 和径向 $L^2$ 上界。新全格界分别为
$E_{H,i}$ 与 $\sqrt{|I_i|}E_{H,i}$。只在各自独立合法的标量上界间取 min，
不把该 min 回写进某个方向多项式的 uniform remainder。

对完整区间先逐格平方和再开方。对跨固定相位端点的最后一格使用真实截断长度
乘该格完整 sup；不按整格 $L^2$ 比例猜测局部积分。完整 7,721 格仍核到
$25/8$，即使某个所报告窗口在更早位置结束。

分别报告 $[0,25/8]$、$[0,9/10]$ 与

$$
[0,2383968743003/10000000000000].
\tag{H.6}
$$

最后一个端点只是当前背景负区功能的安全上端，不转移到其他 $\delta$ 或未知
非线性背景。已知高源实际支撑至 $|4j|\le640$，因此这条有限源还可收

$$
\|f_H\|_{H^{1/3}_\varphi}
\le(1+640^2)^{1/6}\|f_H\|_{L^2_\varphi}.
\tag{H.7}
$$

这个有限源权重不能授给未知无限 Fourier tail。

## H.5 公开执行、恢复与失败记录

输入的 40 份原 closed rows 必须同时逐 SHA 匹配 repair-source 与 mixed-Z
native 的原 receipts；原候选与原 trial 的 index、每个分片、6144 piece
及完整 65/193 槽由原 input-only restore 审计。原 repaired centre 和 $Z$
的 definition、区间、mean 与全部门另行核验。

原 artifact process 的准确 SHA 分别是

- repair：`16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a`；
- mixed：`56c84147351d56b262a17ae0cbf96e18c6525083d72bd51e2f590620dc6e5168`。

这些是 artifact 快照，不冒充后续仓库 process 的同一 SHA。新 worker 保留全部
失败与完成 prefix，按 native 的准确逻辑路径与 SHA 恢复原字节，包含 lossless
分片。已完成的数学 native 即使后来发布失败也可复用，前提完整门与真实
child returncode 0 均成立；部分 prefix 只复用逐行准确完成记录。

新源每 128 行保存一次；wrapper 每 10 分钟真实 pull 并检查两份 README。
新 summary 在写出前检查不超过 60,000 UTF-8 字节，大 native 由原 reviewed
发布器原字节分片。所有数值运算均在此公开仓库 Actions 内执行。

实际成功只证明同一 fixed repaired M32 背景上这条已知高源的完整界。真正
无限高逆、low/high 反馈、非零 $\delta$ 转授、全系统响应误差和非线性闭合仍需各自
支付，不随这个源证书自动通过。
