# 实际 canonical v0 的完整谱预算与共同根余项

2026-11-12。对象始终是 R57/R97 的准确 affine
$\delta_5\pm10^{-9}$ 族，不是重新取整的物化 NPZ。
$\delta_5=-7789843107295549/4611686018427387904$。
本记录只补实际根端比较；不声称全反馈或非线性零解已经完成。

## 1. 源、真重算与失败记录

实际几何/原函数来源是
[actual-root-Fourier-fit-and-H-primitive](2026-11-12-actual-root-Fourier-fit-and-H-primitive.json.gz)，
SHA256
$1b9aa765803c8a12bd300a568e04dd93cd60f5ffd142bbcc18369ba4fb8bef1c$；
名义角参考来自
[actual-to-nominal-root-shear](2026-11-12-actual-to-nominal-root-shear.json)，
SHA256
$6b8c1fcc5e7cc3211c33401798a722e0831dde93c365dfad15ce926836c71143$。
脚本逐项核源 SHA、完整标志及准确对象身份。
这些有限多项式是带严格误差的计算参考，实际曲面没有被它们替换。

新源
[fourfold_phase_canonical_v0_wiener_ci.py](../scripts/fourfold_phase_canonical_v0_wiener_ci.py)
SHA256
$197fd0ad59c00e8cd56909728a270b371d64f6f17cb3337a180303e13ebb5a29$。
初次 run 43303990088 中，保存物理字段的字典变量名被后面的
逆角残差区间覆盖，程序在输出完整报告之前抛异常。
修复仅将该字典改名为 physical_fit；失败任务没有生成可转授的证书。
run **43304292862** 从真实输入重新计算成功，随后通过终端 Git 保存，
不是从失联执行器的摘要拼回结果。
运行环境为 Python 3.12.16、NumPy 2.3.5、SciPy 1.17.0、
python-flint 0.9.0，Arb 精度320位。

[完整报告](2026-11-12-ci-canonical-v0-scaled-Wiener.json)
SHA256
$3709417eec2b87e21f81f83c05dc83e113fd881984ea2e7de6678cbafe85db68$；
[小报告](2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json)
SHA256
$66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8$；
准确 binary64 参考系数 NPZ SHA256
$890b7d6296a62711bc0aabe76a4cc5a1864e06a263729863a9b17f487a63935f$。
[运行 manifest](2026-11-12-ci-canonical-v0-manifest.json) 同时保存三个原件。

## 2. 角、常数项及完整误差

记真实归一化角为 $\psi=H(\theta)=qY_0(\theta)$，
周期为物理四分之一周期 $\pi/2$。
其实际 Fourier 频率是 $4k$，真实 canonical 物理频率仍为
$\lambda_k=4q|k|$。不遗漏这个 $q$，也不把物理 $\theta$ 系数
直接当成 canonical 系数。

真实物理余项 $r=v_0-5050$ 的已认证有限参考为 $P$，
名义角为准确有限多项式 $H_0$。
先在16384个物理格上以16阶 Taylor 和完整指数余项评价
$H_0-\theta,H'_0,P$。每个实际求逆候选可以由普通浮点 Newton
给出，但随后使用真实区间残差和已证 $H'_0\ge m_0>0$，
付
$$
 |\theta_*-\theta_{\rm trial}|
 \le |H_0(\theta_{\rm trial})-\psi|/m_0.
$$
由完整 $P'$ 模支付其余项值的变化。没有把 Newton 浮点收敛
当成准确逆角的证明。

16384个 canonical 节点使用对称性还原完整圆。
节点中点均定义为准确 binary64 数，节点球的全部离散 RMS
进入系数误差。Arb 完整 DFT 后保留 $|k|\le4096$，
完整解析 alias 为每个保留模的双侧几何和。
只向零系数加入准确5050，再支付最终系数中点舍入。
所以矩0包括真实均值，矩1的常数项准确为零。

若真实物理余项误差为 $\epsilon_P$，
真实角误差为 $\epsilon_H$，$H'\ge m_H$、$|H'|\le M_H$，
则归一化 Fourier $\ell^2$ 的完整比较费为
$$
 \sqrt{M_H}\,\epsilon_P
       +\|P'\|_\infty\epsilon_H/m_H.
$$
第一项由真实换元的 Jacobian 给出；第二项用两个真实逆角的距离。
再加节点 RMS、DFT 中点舍入和完整 alias，
得到实际投影系数总误差
$$
 \epsilon<0.00001872673.
$$
它是保留系数的整体 $\ell^2$ 费用，不能在每一个高模上独立重复收费。

真实余项在 canonical 条带上的模小于467.112549，
条带宽度大于0.0018609264148。
对 $p=0,\ldots,4$、$\nu=0,1$，用 R98(98.27)求全部矩。
有限部分精确求和；误差部分用 Cauchy–Schwarz；
无穷部分用二项式和 Stirling 数展开的几何矩。
每个候选分割 $J$ 都包含全部 $|k|>J$，优化选择最小者合法。

## 3. 实际改善及准确根端算术

实际 $K=256$ 得 $M_{v_0}(3)<5192$、$L_{v_0}(3)<4520$。
先前仅凭复模得到的 $L_{v_0}(3)<54936011898$ 虽然正确，
但不适合作为实际高频余项费用。新界没有改变主算子；
它支付的是同一完整函数的更精细 Fourier 预算。

R98第9节给出完整波空间的准确恒等式
$$
 (\mathscr T F_A)^{-1}\mathscr T_{\rm app}F_A
   =\operatorname{diag}(A,A)+\mathcal R_h+UV.
$$
$\mathscr T$ 是准确保通量的共同 frame；
$A=(I+D)^{1/2}$ 是两侧共有的正振幅；
$\mathcal R_h$ 是同一 canonical $L^2\oplus L^2$ 上的高块；
$UV$ 保留有限输入/输出方向及其无限高输出尾。
这不是把低列截成物理 Fourier 方阵。

[fourfold_phase_common_root_budget.py](../scripts/fourfold_phase_common_root_budget.py)
检查本篇小表和 R99 的完整小表 SHA，一并检查准确 family、$q$、
$v_0$ 矩、$v_1/3$ 矩和 $m_0,m_4$。
脚本用 Python Fraction 将每个显示的 Arb 球解析成有理区间，
再以准确平方和立方不等式支付所有平方根/三次根。
所有最终范数与小量比较均为有理数运算。
实际结果保存在
[actual-common-root-high-remainder](2026-11-12-actual-common-root-high-remainder.json)。
首次两行 run 43306123080 成功；加入更低的 $K=64$ 行后，
run 43306719256 重新执行全部检查成功。
三行报告 SHA256 为
$e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253$，
准确有理源 SHA256 为
$6c6aab056672046df9b8e130dd60797022c1269f858de40bf039cc15663a528b$。

|$K$|$\|\mathcal R_h\|_{L^2\to\mathcal H^{7/3}}$|$\|\mathcal R_h\|_{L^2\to L^2}$|根比较高块逆|
|---:|---:|---:|---:|
|64|$<77000000$|$<0.88$|$<16$|
|128|$<8700000$|$<0.021$|$<1.04$|
|256|$<2100000$|$<0.001$|$<1.006$|

这给出了可按有限增广成本选择的真实根端高块，而不是强迫全物理
PDE 使用同一个角截断。每个标量槽低维数为 $2K+1$，
比较有限项秩不超过 $4(2K+1)$；若正帽 trial 均值取零，
另附真实均值差列。regular 端口的均值与通量也保留。

## 4. 尚未转授的部分

此处没有证明有限矩阵 $I+V\mathcal L_0^{-1}U$ 的实际可逆性，
也没有把 R96 的正帽 scalar/weak-flux 大源费自动变小。
实际全帽和负区传播、普通源、外端 Wronskian 匹配、
全部有限 Schur 及非线性迭代仍须在完整空间中接通。
根端小余项使这一接线少了一项已识别的大费用，
但它本身不是完整强反馈逆。
