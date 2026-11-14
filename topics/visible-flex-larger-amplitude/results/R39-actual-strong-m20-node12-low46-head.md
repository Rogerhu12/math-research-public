# R39：实际强M20节点高度的真实46模头部与低深图反馈

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**已证明。** 将已完成的新有理深g、M20、depth12/far225实际求解
在node12保存的**全部20个高度Q**按准确binary实数解释，作为
下述真实参考边界；其余26个低窗浅高度选0。对R26的同一真实
源，在node225到node12的213个胞元上，完整mean点态源的低46
投影方程配R18真实深图的低斜率条件，有一个显式盒内唯一解。
全46个深端低高度都允许校正，且

$$L_{\rm total}<0.271654,\qquad\max_nU_n<1.099248,$$
$$\boxed{|z|_{38}<2^{-2224.09023699}<2^{-2224}.}
\tag{39.1}$$

真实非线性低深图反馈消耗的盒余量比例小于 $2^{-232}$，新增
Lipschitz常数小于 $2^{-238}$。本结果不再使用q003的小幅高度
作为实际参考；重用的仅是已独立认证的同一源线性列和Green核。

**数据来源与范围。** 外端完整20H来自root的 **q085成功M20**
原度量实际响应，经新有理深g重新求解后取得node12数据；
不是同时另行计算的q095 M24。本结论认证的是这些明确node12
高度上的真实辅助边值问题，不把外0..11的保存浮点轨道当作
精确实轨道。完整头部高频、mean接缝、外头到强前缀的匹配和
全时闭面几何仍须继续支付。

## 1. 两个算术对象与准确边界定义

新有限求解使用首160个冻结浅层参数和冻结binary全局warp，
深处 $n\ge160$ 改用准确 $\alpha_n=65/64$。它对同一完整20H
重新求解；旧g的成功响应仅作warm起点。该作业14656正式exit0，
完整响应为

`notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz`，

SHA256为

`528fd51921f7cad71445d76669b44e60279c0fc31cddf9041f8ea5b1f7477962`。

其有限求解残差 $1.0904156886053144\cdot10^{-10}$、有限audit
和保存的Pi/Xi只用于记录所选候选；以下定理不以该残差充当
严格实轨道误差。

设该文件 `response.endpointCanonicalTrace.Q[j-1]` 的准确binary
值为 $q_j^*$，$1\le j\le20$。例如

$$q_1^*=-3.7342413529625106\cdot10^{-40}\quad\text{的准确binary值}.$$

其余数由上述完整文件及SHA唯一指定，而非由本文显示小数另行
四舍五入。定义全部46个浅端条件

$$Q_{2j}(b)=q_j^*\quad(1\le j\le20),\qquad
Q_{2j}(b)=0\quad(21\le j\le46),
\tag{39.2}$$

其中 $b$ 是R26**真实积分源**的node12半径。把数值Q用于
(39.2)是定义一个准确边界坐标，不是宣称数值节点半径恰等于b。
R26的真实外半径与名义binary0.3的已证差仍保留。

数值状态Q已经是常规cosine系数；root内部L使用正交
$\sqrt2\cos(m\theta)$。保存的

$$\Xi_j=\frac{\sqrt2 r^4w^2}{\sqrt{12}\mu}\,L_j$$

已将L转回R23的常规cosine canonical坐标。参考重建只使用Q，
不会将checkpoint的非线性connection momentum Pi直接当作Xi，
也不会再额外乘一个 $\sqrt2$。

## 2. 同一真实源的复用守卫

实际参考入口 `closure_rebase_actual_reference.py` 从头核对：

- 定义、固定source revision及source hashes、深源起点、深alpha、
  准确源常数、冻结warp和head fingerprint逐项相同；
- 全部物理几何参数及完整160行浅层
  $(n,\delta,R,c,\mathrm{lengthScale},\alpha_n)$ 表逐项相同；
- 原ready的SHA属于已付真实列输入；六个真实列组SHA都未改变；
- 新完整响应属于所给ready，确实有20个完整请求H、20个Q和
  20个canonical Xi，physical depth12、far225、spacing2均相符。

这里只复用相同公式及参数所定义的真实实函数。点缓存和冻结
校准的复用不更换函数，也没有用指纹点相等代替完整参数相等。
该核对使R26/R29真实流、全部46个非零浅高度图及Green核能
用于新参考；不需重新积分相同线性系数。

令 $\phi_m$ 为R29从R18实际线性深子空间出发的列，
$G_m=\phi_{Q,m}(b)\ne0$。新真实线性参考为

$$Y_m^0(r)=\frac{q_{m/2}^*}{G_m}\phi_m(r)
\quad(m\le40),\qquad Y_m^0=0\quad(42\le m\le92).
\tag{39.3}$$

每个比值使用保留符号的独立上下端点，不对包零幅度区间作
不合法除法。参考为0的26项仍有完整真实列；非线性校正会
改变其far低高度，未将这些参数删除。

## 3. 新参考的强范数与实际Green矩阵

使用R38平顶角宽

$$\tau_n=\max\{2,1+(n-12)\log2/4\},\quad12\le n\le224,$$
$$X_n(Y)=\sum_{m\ne0}e^{\tau_n|m|}
\left[(1+|m|)^3\sup_n|Q_m|+(1+|m|)\sup_n|\Xi_m|\right].
\tag{39.4}$$

两分量sup分开取。由 (39.3) 和全部真实列重新算得上界x：

$$x_{12}<1.110109914589\cdot10^{-35},\qquad
x_{224}<2.496723356849\cdot10^{-1043}.$$

完整213行x、R23源/mean界和far转换保存在
`closure-newg-strong-m20-real-reference.json`。参考全部R23半径比
小于 $3.623089\cdot10^{-9}$。

R23完整mean根上的源估计仍是

$$\|N(Y)\|_{L^1\mathcal W_{\tau_n}}
\le B_nX_n(Y)^2,\qquad
B_n=2^{12}r_c^3/(\epsilon\delta_n^{19/4}),$$
$$\|N(Y)-N(\widetilde Y)\|
\le2B_n\{X_n(Y)+X_n(\widetilde Y)\}X_n(Y-\widetilde Y),$$
$$r_n=2^{-23}\epsilon\delta_n^{19/4}/r_c^3.
\tag{39.5}$$

R38实际全46角宽Green核给

$$X_k(Gf)\le\sum_n\gamma_{kn}
\|f\|_{L^1\mathcal W_{\tau_n}(n)}.
\tag{39.6}$$

cells12/13使用R35有序真实核及分量sup，其余采用原真实列。
程序再次核对并读取全部46块，乘正确的源/目标角权，然后取
对角Fourier算子范数的最大值。新Green包的统一参考响应为

$$\eta<0.096207783.$$

包内默认的1%统一相对球门因此失败。这个失败如实保留；程序
正常退出仅表示上界计算完成。本结果使用下面另行支付的非等
盒，不将该默认门写成成功。

## 4. 完整46模非等盒的四项严格门

定义

$$A_{kn}=\gamma_{kn}B_nx_n^2/x_k,$$
$$\mathcal B=\{V:X_n(V)\le(U_n-1)x_n\},\qquad
d(V,\widetilde V)=\max_n X_n(V-\widetilde V)/(W_nx_n).
\tag{39.7}$$

全部U,W由普通浮点提出后固定成准确dyadic数；再由真实源和
外舍入Arb从头检查，普通提议的误差不参与证明。完整数据在
`closure-newg-strong-m20-real-box.json`。逐行得到

$$s_k=U_k-1-\sum_nA_{kn}U_n^2>0,
\qquad\min_k s_k/W_k>8.0482410\cdot10^{-10},$$
$$L=\max_k\frac{\sum_n4A_{kn}U_nW_n}{W_k}
<0.271653516,$$
$$U_nx_n<r_n\qquad(12\le n\le224).
\tag{39.8}$$

部分数据为：

| cell | $U_n$ | $W_n$ |
| --- | ---: | ---: |
| 12 | 1.01567651596193 | 1.08970165339532 |
| 13 | 1.09924784504310 | 1.56790074156367 |
| 14 | 1.00076426533423 | 1.00410187030941 |
| 224 | 1.00000030250297 | 1.00000172563245 |

实际证明用文件中准确端点，表格只是显示。最大U在cell13，
小于1.099248。盒的半径与收缩距离权是独立的两组正数。

第四项门是全46深参数的定义域。令

$$S_F=\epsilon\delta_{224}^{11/2}/r_c^3,\qquad
C_F=\max_{m=2,4,\ldots,92}
\frac{e^{(38-\tau_{224})m}}{(1+m)^3}.$$

最坏转换模仍是m92，全部26个参考零项均参加这个最大值。
参考far参数满足 $\log_2Z_0<-2228.16008766$，整个盒有

$$|z|_{38}\le Z_0+(U_{224}-1)x_{224}C_F/S_F,$$
$$\log_2|z|_{38}<-2224.09023699363.
\tag{39.9}$$

因此取 $Z_*=2^{-2224}$，同时满足R18和R34所有低输入域条件。
相对 $2^{-2200}$ 工作门，实际余量超过24.0902比特。

## 5. 用当前far高度评价完整真实深图

设 $\mathcal D=\Gamma-\Gamma^{\rm lin}$ 是R18的完整全频深图差。
已证复球估计给

$$\|\mathcal D(z)\|\le C_D|z|^2,qquad
\|D\mathcal D(z)\|\le4C_DZ_*,\qquad C_D=2^{1967}.
\tag{39.10}$$

只取低46斜率投影 $\mathcal D_{\rm lo}$，范数常数不增。没有
把图内高频或mean设0；只是它们尚未全部作为头部边界数据安装。

R36的准确Wronskian边界提升仍为

$$\mathcal B_m d_m^{\rm phys}(r)
=\frac{\mu_{224}}{\mu_{12}\phi_{Q,m}(b)}\psi_m(r)d_m^{\rm phys},$$
$$\psi_Q(b)=0,\quad\psi_{\Xi,12}(b)=1,qquad
d_m^{\rm phys}=S_Fe^{-38m}d_m.
\tag{39.11}$$

这准确施加far低斜率缺陷，保留跨胞元动量规范。设该提升在
cell k的真实范数上界为Kk，定义

$$b_D=\max_kK_k/(W_kx_k),\qquad
e_D=W_{224}x_{224}C_F/S_F.$$

新入口从同一真实列和实际强参考盒重新计算，不沿用q003的
归一常数。得到

$$\log_2b_D<2218.902535,qquad
\log_2e_D<-2202.5222579,$$
$$\log_2(4b_DC_DZ_*e_D)<-238.6197230,$$
$$\log_2\max_k\frac{K_kC_DZ_*^2}{x_ks_k}<-232.0974640.
\tag{39.12}$$

所以真实低深图反馈严格小于原盒每一行的余量，新增Lipschitz
小于 $2^{-238}$。全mean的far界同时按相同 $Z_*$ 保存为

$$|\kappa_0(a)|\le2^{99}\epsilon\delta_{224}^{33/4}Z_*^2,$$
$$|\overline v(a)-\overline v(r_c)|
\le r_c2^{853}\epsilon\delta_{224}^{25/4}Z_*^2.
\tag{39.13}$$

这些量未被设为0；投影头与完整深图的mean接缝尚不从低斜率
等式单独推出。

## 6. 存在性、唯一性及正则性

取满足物理接口连续性和齐次浅高度的有限46模连续场完整空间，
用 (39.7) 赋范；不向迭代输入预施加线性far条件。定义

$$T(V)=G\Pi_{46}N(Y^0+V)
+\mathcal B\mathcal D_{\rm lo}(z^0+\mathcal EV),
\tag{39.14}$$

其中 $\mathcal E$ 是准确far低高度评估。第一项用完整mean根
计算源后投影，第二项每次在**当前全部46高度**求完整真实深图。

(39.8) 和 (39.12) 使T把闭盒映入自身，且

$$\operatorname{Lip}(T)<0.271653516+2^{-238}<0.271654<1.$$

Banach定理给唯一固定点。准确Green与Wronskian提升分别施加
齐次线性far条件和其非线性低斜率差，故固定点满足

$$\mathcal LY=\Pi_{46}N(Y),\qquad Q_m(b)=Q_m^*(b),$$
$$\Xi_{2j}(a)=S_Fe^{-38(2j)}\Gamma_{\Xi,j}(z(Y)),\quad1\le j\le46.
\tag{39.15}$$

源在整个盒内连续且Lipschitz，固定点由真实一阶系统得到一阶
canonical正则性，并由准确高度转换和完整mean根得到有限头部
高度的两阶正则性。投影外Darboux方程尚未施加，因此该C²
辅助高度不能冒充完整头与深尾已经C²接合。

## 7. 完整复算链与已付范围

所有界使用python-flint0.9.0、192位Arb和准确binary输入。
以下作业均已工具formal exit0，且持久化resource的wait4
exitcode也为0：

| 作业 | 会话 | 数学作用 |
| --- | ---: | --- |
| 新g完整20H有限重解 | 14656 | 给出明确候选node12数据；587.14秒，峰408364KiB |
| 新真实参考 | 28746 | 同源守卫、全部20高度、完整46列、全胞元源界 |
| 新加权Green | 18719 | 完整213×213核；默认1%球失败如实保留 |
| 新非等盒 | 28024 | 四组严格门全部成功 |
| 真实低深图反馈 | 42208 | 新盒不变与完整低边界反馈成功 |

入口及包分别是 `closure_rebase_actual_reference.py`、
`closure_plateau2_green.py`、未改的 `closure_anisotropic_low46_box.py`
和 `closure_rebased_nonlinear_low_far_lift.py`。
最后一个入口显式接受并核销 $Z_*=2^{-2224}$，不硬编码旧q003球。
文件前缀为 `2026-11-12-closure-newg-strong-m20-real-`，每包记录
全部输入和源SHA，resource记录完整命令，可直接逐项重算。

R39支付了实际强候选进入真实深头的低窗存在块。完整高深迹、
头部自产中高频及其对低窗的反馈必须由R33联合固定点处理。
全非均值匹配后，mean小根的唯一性和一次统一高度积分可用于
真正的完整接缝；在此之前不把有限投影结果提升为完整Darboux
解。外头和强前缀仍要在同一真实g上匹配，并保留R26外cut规范。
