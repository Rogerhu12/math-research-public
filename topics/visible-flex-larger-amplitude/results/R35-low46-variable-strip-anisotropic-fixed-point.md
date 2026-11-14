# R35：真实头部46模的变角宽非等半径固定点

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**已证明。** 对 R26 同一真实固定有理深源，在 physical node225
至 node12 的213个胞元上，以下明确的**辅助46模边值问题**有解，
并且在本文指定盒中唯一：非线性向量场先使用完整点态 mean 根，
然后只在输出处投影到物理频率 $m=2,4,\ldots,92$；node12 固定
下述全部46个参考高度；node225 取 R18 的**真实线性**深子空间。

该解处于逐胞元角宽

$$\tau_n=1+(n-12)\log2/4$$

的显式非等半径盒内。其全部46个深端低高度参数满足

$$\boxed{|z|_{38}<2^{-2203.2158}<2^{-2200}.}\tag{35.1}$$

所以 R34 的真实完整高深迹接口对整个指定盒有效。盒的 Banach
收缩常数不超过 $0.749997628<4/5$。

**范围。** 本结论没有将有限投影方程当作完整 Darboux 方程，也
没有将真实线性深子空间当作 R18 的非线性深图。头部自产高频、
非线性深端低斜率差、高深迹、mean 高度规范以及外0..11胞元和
实际强前缀仍须接入。这是对完整46维低窗的实际存在结论，仍是
原闭曲面任务的中间进展。

## 1. 固定参考与准确边值问题

参考是 `closure-real-linear-q003-low46-recovered` 的真实线性场。
node12 的前八个高度取已保存 q003 包中的准确 binary 实数，
其余38个参考高度选为0。对每个 $m=2j$，使用 R18 的实际线性
深斜率，而非理想斜率等号。真实浅端高度增益严格非零，全部46列
都已经实际包围；没有用八列加零代替高38列。

用 $Y=(Q,\Xi)$ 表示 canonical 非均值变量，$\mathcal L$ 为
R29 的准确线性算子，$N(Y)$ 为 R23 在完整 mean 根上求出的
非线性源。辅助方程是

$$\mathcal L Y=\Pi_{46}N(Y),\tag{35.2}$$

这里投影只作用于完整源的输出。mean 根仍使用完整角函数求解，
并非将 mean 设0；产生的高频源在此辅助问题中不进入微分方程。
浅端为上述46个准确高度，深端为46个实际线性子空间。

令 $Y^0$ 为同边界的真实线性参考。两端 Green 算子 $G$ 给出
准确等价的固定点方程

$$V=G\Pi_{46}N(Y^0+V),\qquad V=Y-Y^0.$$

这里 $V$ 满足齐次浅高度和齐次实际线性深条件。物理动量
$\mu_n\Xi_n$ 在所有胞元接口连续；canonical $\Xi$ 的已知
$\rho$ 转换始终保留。

## 2. 全胞元范数与最初粗界

对 cell n 取 R23 范数

$$
X_n(Y)=\sum_{m\ne0}e^{\tau_n|m|}
 \left[(1+|m|)^3\sup_n|Q_m|
 +(1+|m|)\sup_n|\Xi_m|\right].
\tag{35.3}
$$

两个分量的 supremum 各自取，不能假设同时实现。令 $x_n>0$
为真实参考 $X_n(Y^0)$ 的已存外舍入上界。R23 给

$$\|N(Y)\|_{L^1_r\mathcal W_{\tau_n}(n)}\le B_nX_n(Y)^2,$$
$$
\|N(Y)-N(\widetilde Y)\|
\le2B_n\{X_n(Y)+X_n(\widetilde Y)\}X_n(Y-\widetilde Y),
$$
$$B_n=\frac{2^{12}r_c^3}{\epsilon\delta_n^{19/4}},\qquad
r_n=\frac{2^{-23}\epsilon}{r_c^3}\delta_n^{19/4}.
\tag{35.4}
$$

以上在 $X_n\le r_n$ 的完整 mean 分支内成立。

最初整cell正逆盒给统一角宽1的 $\eta\le263601.2549$；最坏是
cell12到自身的核 $2^{64}$，由物理m86列主导。cell13自身为
$2^{61}$。这些是合法但过粗的上界，不是线性图退化，也不是
无解结论。后面仅在这两个cell内保留真实径向次序来消去粗界。

## 3. 有序的同胞元 Green 核

对单模令 $\phi$ 为深端可容许列，$\psi$ 为浅端
$Q=0,\Xi_{12}=1$ 的列。物理 Wronskian 为

$$W=\mu_{12}\phi_Q(\mathrm{cut}).$$

把 $\phi$ 除以浅高度增益后记为 $\widehat\phi$，则同一cell n
上的 Green 分量绝对值受以下有序积控制，统一再乘
$\mu_n/\mu_{12}$：

$$
K_Q(r,s)=\widehat\phi_Q(\min(r,s))\psi_Q(\max(r,s)),
$$
$$
K_\Xi(r,s)=
\begin{cases}
\widehat\phi_\Xi(r)\psi_Q(s),&r\le s,\\
\psi_\Xi(r)\widehat\phi_Q(s),&r\ge s.
\end{cases}
\tag{35.5}
$$

旧界把整个cell的两个最大值无序相乘，允许实际径向次序不相容
的位置对。现将cells12、13按 R29 的真实材料面板划分，分别有
4240、2077个面板。正向 $\phi$、反向 $\psi$ 都使用有符号
Peano–Baker 面板矩阵及正的局部部分流 majorant；反向流用
行列式1的余子式，未除一个包零的区间行列式。

将面板按半径从内至外编号 i，记其中两个列的分量上界为
$\Phi_{Q,i},\Phi_{\Xi,i},\Psi_{Q,i},\Psi_{\Xi,i}$。则

$$K_Q^*\le\max_j\Psi_{Q,j}\max_{i\le j}\Phi_{Q,i},$$
$$K_\Xi^*\le\max_j\max\left\{
\Psi_{Q,j}\max_{i\le j}\Phi_{\Xi,i},\ 
\Psi_{\Xi,j}\max_{i\le j}\Phi_{Q,i}\right\}.
\tag{35.6}
$$

同一面板内仍允许两个分量在不同位置取值，所以 (35.6) 只是
保守上界，没有漏掉面板内部。乘 $\mu_n/\mu_{12}$，再取
$(1+m)^3K_Q^*+(1+m)K_\Xi^*$，得到所需的分量sup之和范数。

这把两个对角核分别收紧至 $2^{33}$、$2^{32}$。
同一次真实面板传播也给出整个cell的 $\phi,\psi$ 分量sup；v2
用这些更小的合法上界收紧所有涉及source12/13的非对角核。
其它胞元的已付真实列仍原样使用。全部46个浅端高度条件未改。

## 4. 变角宽 Green 矩阵

R29 每对胞元的单模 Green 上界乘

$$e^{(\tau_k-\tau_n)m}=2^{m(k-n)/4}.$$

取46个独立 Fourier 块的最大值，而非和，得到

$$X_k(Gf)\le\sum_n\gamma_{kn}
 \|f\|_{L^1_r\mathcal W_{\tau_n}(n)}.
\tag{35.7}
$$

每个 $\gamma_{kn}$ 用精确 $2^{g_{kn}}$ 上界保存；半整数权指数
向上舍入最多再损半比特。全部213×213矩阵在
`closure-variable-green-low46-v2.json.gz` 中。

即使收紧这两个cell，统一相对半径的充分界仍有
$\eta\le280.84196$，主导为source12到target13。最后cell224的
相对响应只有约0.083735。这个差别说明按同一个参考幅度倍数
限制每层过紧，不能据统一球失败否定实际小性。

## 5. 非等半径盒与独立的距离权

定义一个完全显式的正矩阵

$$A_{kn}=\gamma_{kn}B_nx_n^2/x_k.$$

取文件中保存为精确dyadic数的 $U_n>1$ 与 $W_n>0$。定义闭盒

$$\mathcal B=\{V:X_n(V)\le(U_n-1)x_n\text{ 对所有 }n\},
\tag{35.8}
$$

而用于收缩的距离取

$$d(V,\widetilde V)=\max_n
 \frac{X_n(V-\widetilde V)}{W_nx_n}.
\tag{35.9}
$$

盒的半径与距离权是两组独立正数。无需让 $W_n=U_n-1$；二者
混同会制造额外的失败门。

对 $V\in\mathcal B$，由参考上界和 (35.4)–(35.7)，

$$X_k(G\Pi_{46}N(Y^0+V))
\le x_k\sum_n A_{kn}U_n^2.$$

因此以下有限个不等式足以保证盒不变：

$$\boxed{1+\sum_nA_{kn}U_n^2<U_k\quad(\forall k).}\tag{35.10}$$

又由 (35.4)，同一盒中两输入的源差给

$$d(TV,T\widetilde V)
\le L\,d(V,\widetilde V),\qquad
L=\max_k\frac{\sum_n4A_{kn}U_nW_n}{W_k}.
\tag{35.11}
$$

最后需同时核销 $U_nx_n<r_n$，这样完整mean根和源界在整个盒
有效。这里的源来自完整点态方程，投影的 $\ell^1$ 范数至多1。

## 6. 数值只提议盒，严格算术支付全部门

程序先用普通浮点正迭代提议 $u\approx1+Au^2$，再以
$4A\operatorname{diag}(u)/(3/4)$ 的正迭代提议 w。随后将

$$U_n=u_n+2^{-30}w_n,\qquad W_n=w_n$$

的最终binary值固定成**精确dyadic输入**。
这一步不构成证明，也不需要相信普通浮点迭代误差。

程序重新从真实源定义的 $B_n,r_n$、真实参考上端 $x_n$ 和完整
dyadic Green矩阵建立外舍入 Arb 矩阵 A。然后逐行检查
(35.10)、(35.11)及 $U_nx_n<r_n$。全部门得到

$$\min_k\frac{U_k-1-\sum_nA_{kn}U_n^2}{W_k}
>5.82077\cdot10^{-10},$$
$$L\le0.749997627237571<4/5,$$
$$U_nx_n<r_n\qquad(12\le n\le224).
\tag{35.12}
$$

盒的若干量级为

$$U_{13}\approx281.9111,\quad
\max_nU_n=U_{14}<6691.597,\quad
U_{224}<11.098524.$$

这些大的**相对参考倍数**没有突破实际源的小球：参考沿头部极快
衰减，真实物理幅度仍由上述逐层 $r_n$ 门控制。
推理实际用完整JSON中的dyadic数，显示的小数不反向作为输入。

## 7. Banach定理与正则性

取213个胞元上满足物理接口连续性的有限46模连续场空间，并用
(35.9)赋范。有限胞元、有限角模及所有正权保证这是完整空间；
canonical规范在接口的已知变换是有界线性变换。盒 (35.8)
为其中包含0的闭集。

固定点算子使用准确两端 Green，自动满足齐次边界和接口条件。
在盒内，完整mean隐式根及源连续，且 (35.4) 给 Lipschitz。
(35.10)使算子将盒映入自身，(35.11)–(35.12)使其在完整距离下
严格收缩。Banach固定点定理给唯一 V，从而给 (35.2) 的解。

固定点先是连续场；其方程右侧连续，故canonical变量按实际线性
系统为一阶可微。再由同一真实 $w,r$ 的源正则性和高度的准确
canonical转换得到有限头部高度的两阶正则性。这里不借数值
quintic的独立导数，也不声称未投影的高频Darboux残差为0。
mean slope 由同一个完整根确定，mean高度可沿头积分并指定一次
平移规范；与 R18 深mean的实际高度规范匹配仍未在本定理施加。

## 8. 整个盒的46参数真实深图定义域

R34 已给

$$S_F=\epsilon\delta_{224}^{11/2}/r_c^3,\qquad
Z_0=|z(Y^0)|_{38}<2^{-2232.1897},$$

及全部46模的转换范数

$$C_F=\max_{m=2,4,\ldots,92}
 \frac{e^{(38-\tau_{224})m}}{(1+m)^3}
<40804.559661132.$$

其最坏模是m92。对本定理整个盒，由 (35.8) 的最后一层Q分量，

$$|z|_{38}\le Z_0+
 \frac{(U_{224}-1)x_{224}}{S_F}C_F.
\tag{35.13}
$$

将本定理准确dyadic $U_{224}$ 代入，外舍入结果为

$$\log_2|z|_{38}<-2203.21585677454.$$

这保留全部46个可能改变的低参数和最后一次角宽转换，支付
(35.1)，对 R34 的门仍有3.21585比特余量。没有将参考中恰为0的
38项当作修正后为0，也没有只用M8标签通过far门。

## 9. 可重算入口与源版本

所有数学检查使用 python-flint 0.9.0 / Arb 192位精度，binary输入
精确转有理数。每个输出记录输入哈希和源哈希，执行wrapper用
wait4将真实退出码、资源和完整命令落盘。

核心稳定文件为：

- `computations/closure_ordered_cell_green_enclosure.py`：同cell有序核v1。
- `computations/closure_ordered_cell_green_v2.py`：额外导出真正逐面板
  $\phi,\psi$ 全cell分量sup，供非对角核使用；旧v1不改。
- `computations/closure_variable_strip_green_enclosure.py` 及独立v2：
  保留第一次统一盒失败，再在v2消费真实全cell分量sup。
- `computations/closure_anisotropic_low46_box.py`：精确提议输入后的
  四组严格门，使用完整213×213实际Green。

最终命令（在课题目录执行）：

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-anisotropic-low46-box-resource.json -- \
  python computations/closure_anisotropic_low46_box.py \
  --green notes/2026-11-12-closure-variable-green-low46-v2.json.gz \
  --reference notes/2026-11-12-closure-variable-reference-farball.json \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out notes/2026-11-12-closure-anisotropic-low46-box.json
```

实际会话3058正式 exit0；wait4文件也记录 exitcode0、1.94774秒、
峰 RSS 44640 KiB。输入Green v2会话18956和有序列v2会话48762
均已正式 exit0。最初有序v1的固定角宽投影球也已通过，但本文
用的是额外支付变角宽、非等半径和真实far域的最终版本。

## 10. 下一完整接口的准确缺项

辅助解的far边界仍是实际线性子空间。应在同一盒的余量内加入
R18相同低高度下的非线性低斜率差，并允许其完整高模高度和斜率
成为头部的边界输入。R34只支付高深迹的线性传播。

头部自产无限高频要使用 R33 的逐模径向密度和连续角宽预算，
不能把本定理对46块取最大值的矩阵当作无穷频率界，也不能给
未表示高模再加任意零Dirichlet条件。完成这个联合反馈、mean
高度及外头/前缀之后，才可调用 R32 的完整Darboux闭合结论。
