# R847：原五个比较函数在同一 CM 点的一阶导数实际均非零

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际完成。** 对原 $p=41$、原 $f=f_4$、原五个 $g_j=(1+T^j)f$，在同一原点 $c_1$ 和原参数 $z=a-1$ 下，五个
$$
D_j=\frac{\mathcal R_j'}{\mathcal R_j}(c_1),\qquad j=1,\ldots,5,
\tag{847.1}
$$
均非零。更准确地，在已指定的原分支 $L\hookrightarrow\mathbf Q_\ell$、$\ell=1000000753$ 下，实际五个严格球证书均给
$$
v_\ell(D_j)=0,\qquad\text{绝对精度}=518.
\tag{847.2}
$$
由 [R844](R844-certified-original-five-Hom-word-points-and-comparison-values.md) 已证的 $\mathcal R_j(c_1)\ne0$，得到原五个 $\mathcal R_j'(c_1)\ne0$。
这里的单位是辅助素数 $\ell$ 处的单位；本项不声称原 $p=41$ 处的单位或高度非零。

实际公开运行 [43789012126](https://github.com/Rogerhu12/math-research-public/actions/runs/43789012126)，job **133043052846**，source **f699023d15daacb7d7e176f52da41899d69ae26c**，于 **2026-11-16T01:55:24.160999+00:00** 结束，exit0、error=null。核心总用时 **3.1661501240000014 秒**；最终数学证书计时 **3.1658617049999975 秒**。两者只是计时边界不同。

## 1. 原对象与已成来源

本项直接消费 [R846](R846-certified-original-Hom-coordinate-and-comparison-first-jets.md) 的 **733节点**准确程序，包含 R844 原529节点。原十二个整数 Hom、实际 $T^7=[\zeta^2]$、七个 $\sigma$ 运输及切向规范均来自 [R791](R791-certified-original-Hom-descent-and-eta-inputs.md)。原点本身的非挠性和所有非零原 Hom 的值分离来自 [R843](R843-certified-original-CM-point-nontorsion-and-Hom-value-separation.md)。

原比值、参数和五个方向保持不变。记原既约比值为
$$
r_j=\frac{a_j}{b_j}
=\frac{31}{67},\ -\frac{41}{67},\ -\frac{34}{67},\
\frac{34}{67},\ \frac{103}{134},\qquad b_j>0.
\tag{847.3}
$$
R846 已证明并生成准确节点
$$
D_j=b_j\sum_{k=0}^6\sigma^k\!\left(\frac{6y_{g_j}h_{g_j}}{x_{g_j}}\right)(c_1)
 -(2b_j+a_j)\sum_{k=0}^6\sigma^k\!\left(\frac{6y_fh_f}{x_f}\right)(c_1).
\tag{847.4}
$$
本次仅给这些既有准确节点的严格有限精度非零见证，没有重新生成 Hom 点、一阶公式或原范数常数。

输入由已完成载体保留270件：CM165、R7919、R841 DAG11、R843非挠66、R844原点程序10、R846一阶程序9。全部旧 manifest、原配置和父子来源已按真实字节绑定。原 CM 四响应是准确单位解表达式的518位像；没有读取短有理重构候选来替代准确叶。

## 2. 有限精度见证为何证明准确值非零

本项执行方法为 [原比较函数对数一阶项的有限精度见证](../notes/R792-original-comparison-log-jet-padic-witness-method.md)，SHA-256 **d55f377e2bb3532bfe6d5b18ecfdc26f74f1c6451507fefea5f3ea0b6a09fbf2**。其严格球算术直接复用 R843 已冻结的实现。

### 2.1 每个球包含哪一个准确值

对原节点 $n$ 和 $0\le k<7$，消费器的含义始终是
$$
\operatorname{eval}(n,k)\supseteq\iota_0\bigl(\sigma^k(\operatorname{value}(n))\bigr),
\tag{847.5}
$$
其中 $\iota_0$ 为原辅助素数分支0。遇到原 $\sigma$ 节点，消费者移动整个输入上下文；实际原 $b,\rho$、切向、四响应和全部常数随之运输。没有只替换外层坐标而遗留错误的单位解叶。

原分支0的 $b,x,y,h_0,y'$ 球及原根提升逐字读取 R843 完成阶段。其余六个嵌入由已认证的原 $\sigma(b)$ 和原固定 $\zeta$ 得到。四响应在各嵌入中按原 $B=\lambda b$、$s=1+2\zeta$ 的十四坐标求值；没有再次求解2420维单位图，没有增加 Hensel 或 Dixon 位数。

球的加、乘和逆都保绝对误差界。逆只在已知有限赋值时执行；分母球含零时只产生“精度不足”，不能据此断言准确分母为零。准确分母本身已由 R843、R844、R846 的原 Hom 与非挠证明保证。故沿准确 DAG 的归纳给 (847.5)。

### 2.2 本次五个实际出口

完成阶段对每个 $j$ 均给 `evaluation_available=true`、`known_nonzero=true`，以及 (847.2)。也就是说，准确 $D_j$ 落在一个赋值0、误差属于 $\ell^{518}\mathbf Z_\ell$ 的球内。该球不含零，所以 $D_j\ne0$。这里仅消费已完成阶段的赋值、精度与证明标志；本地没有重新约化球中心或执行节点算术。

| $j$ | 原 $r_j$ | 实际 $v_\ell(D_j)$ | 绝对精度 | 完成决定的 SHA-256 |
|---:|---:|---:|---:|---|
| 1 | $31/67$ | 0 | 518 | aa85b485f00e3493bb25b33de848b06d44413b133a2e79dd8860570f22be6d82 |
| 2 | $-41/67$ | 0 | 518 | e55a900bcc3e343ffb957d4d258faa29077f715468028154507660c21f62dd79 |
| 3 | $-34/67$ | 0 | 518 | 55a6919b153dd2ab4e8faa445e26d05cc7d40a44f3717a13222a41db76992a2d |
| 4 | $34/67$ | 0 | 518 | a90d0a9f45f773260af62af38f244f44134e0a2ab1d3b0cc69fb0a7fa2bfe7a6 |
| 5 | $103/134$ | 0 | 518 | 4babd9d3d6db14fa562eb361a8e43831fc1fb20eb329acef605cf44efdbf88de |

对应文件依次为 `R792-log-jet-padic-comparison-j.json.gz`，$j=1,\ldots,5$，字节数为5787、5790、5780、5778、5766。它们各自绑定原 R846 程序、原 $D_j$ 根节点及完整节点球来源，没有把五个不同计算对象仅以序号混同。

最后应用准确恒等式
$$
\mathcal R_j'(c_1)=\mathcal R_j(c_1)D_j.
\tag{847.6}
$$
R844 的原七因子范数给 $\mathcal R_j(c_1)\ne0$，所以五个一阶导数均非零。这一步保留原比较函数值及其全部非零常数，未换成另一归一化函数。证明完成。

## 3. 实际产物与不可变身份

数学配置 SHA-256 为 **7b2a243eb552a619e8c65ab626cfa4adcb1e6e0e560193a99063efe9ca66dade**。结果名为 `R792-original-comparison-log-jet-padic-witness`；最终文件为 `p41-original-comparison-log-jet-padic-witness-certificate.json`。

入口：[公开请求](../notes/R792-log-jet-padic-witness-public-request.json)、[数学核心](../scripts/R792_original_comparison_log_jet_padic_witness.py)、[标准库 IO 包装器](../scripts/R792_public_original_comparison_log_jet_padic_witness.py)。工作流 `.github/workflows/serre-R792-log-jet-padic-witness.yml` 仅在本公开仓库执行。

| 项目 | 字节数 | SHA-256 |
|---|---:|---|
| 数学核心 | 28219 | a3d04929db13d1c73414807f0a7c73b18c0e0e4e749d2349e3a44fdafc160335 |
| 标准库 IO 包装器 | 35253 | ea579ada26e837b01250d670be7620f114066967e2ef62dd783aa8cd48dda187 |
| 最终证书 | 7794 | 39f3d05fcc6dcc9f4972f3bfcb16f2bab3e3623b6a73646d809e49007d60359d |
| 原来源审计阶段 | 3631 | 7130b7cf087e4c254d259bcbbcd57ed55b0978c40d831f01db66d2534d55c9af |
| 数学阶段 manifest | 86610 | 23cbd8a749a5fc556421d9ea596189d93b8908032e7f5cdd64da8e7c41e5f856 |
| 全输出 manifest | 290468 | 9bd3169295d20c87ab72c2c7ed149438db7a257e1197072b2d3bbb992fb3185c |
| 原270件输入载体 | 2078830 | a7ccfe9b61d59233e622505afd0a664e18be8d1384a093b446b8b02bf7b9ddb1 |
| 输入 receipt | 62201 | 15df56028a3d35a43d8e37a4dcd74a004d30e7b6a8651e710db715c8ca9ad21e |
| public-actions-input | 63307 | 0fa9fe17bbad584a07356618ceb9a7b1a7780048f2745dfdd14c29b9f1e5d603 |
| core receipt | 5925 | fea53327a7a9125e3165694533b09ae256fd152dd778cdf5853b92de73739e1b |
| run receipt | 405 | e2c582cd863e6b7e60a534980fa04dcfb0a56ae78f74b940d8f0e54d362df179 |

实际请求 SHA-256 为 **69e1ae86c03d8314691357fd465fce304fdb5e664315f13ea0f236f35126d3d4**。原球算术模块 SHA-256 为 **dd3f06a2ed34d31d4d9cc7000eeb5ca763b3fa26b238b418de3e2a47e8dca9c0**，原 DAG 模块为 **afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b**。实际来源审计同时核了这些冻结模块与原字段规范。

本次数学 manifest 登记 **1413个完成阶段**；全输出 manifest 有 **1421项**。实际 artifact **14191283725**，名 `serre-global-R792-log-jet-padic-witness-43789012126-1`，ZIP **11198983字节**，SHA-256 **1737c833763f617e192447f1656d6793cd6d7eb6b78dfdbac0e4d8a9192aac98**。根会话实际读取并重哈希完整 ZIP，核全部 manifest 项、证书和来源；这个复核只有 IO，没有本地数学重算。

机器球中心、节点表、证书及载体仅在一日 active artifact 中续传。Git只保存脚本、参数、纸面证明和本简明运行/SHA登记。

## 4. 直接含义与保留边界

五个原函数在 $c_1$ 的准确局部展开均有非零一次项：
$$
\mathcal R_j(z)=\mathcal R_j(c_1)\bigl(1+D_jz+O(z^2)\bigr).
\tag{847.7}
$$
因此本项关闭 R846 留下的五个具体 $D_j$ 非零缺口。任何另已证明合法的非零常数倍归一化都保持对数导数 $D_j$，但本项未实施或认证原 $c_0$ 刚性化。

五个单独非零不表示五个一阶数线性独立，也不给任意线性组合非零。原高度的一阶项还含其原 Picard、Poincaré、周期或框架比较项；这些项可能发生的相消不由 (847.2) 排除。

本次没有新增 Hensel/Dixon 位数，没有重做旧 CM、Hom、点加法、非挠或原733节点，没有使用候选数组。准确展开坐标与原单值接受条件 A.1、抽象 $A$ 的同源核前像、$\eta_h$ 的标准 Jacobian 坐标、原高度及全 $p$ 结论均仍各按其真实未完成接口推进。
