# R42 共同strip的完整有向四核Green界及强M20重标

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）。日期：2026-11-12。

可信度：已证明的真实线性核证书与条件重标定定理。

本文件给出已完成的真实线性/材料证书，以及一个不需要重新积分的严格
幅度重标定定理。它不宣称尚未运行的联合不动点门已经通过。

## 0. 定理、量词和Green核的完整证明

固定 [R26](R26-real-head-source-interval-and-port-coordinates.md) 定义的实
有理深源、[R18](R18-computable-exact-tail-trace-and-robin-envelope.md) 的
真实线性far图、[R38](R38-shallow-plateau-strip-and-nonlinear-low-head.md)
的辅助低解盒，以及 [R33](R33-full-head-forcing-on-a-variable-analytic-strip.md)
的连续 $\tau(r)$、$B_n$、$V(r)$。这里的参考是q003，不是原stored-g的
数值截断解。以下所有范数、边界和材料均指这些固定的实对象。

**定理42.1（完整有限头部四核）。** 下述输出文件中的四个矩阵
$\Gamma_{\rm main},\Gamma_{\rm corr},\Gamma_{\rm base},\Gamma_{\rm rem}$
以及四个far行，分别是 R33 §16.7 四种固定频谱质量源族的严格上界。
范围是全部213个源胞元、全部213个目标胞元和全部46个低Fourier模。
所有矩阵项按文件中向上dyadic值解释。它们同时给出完整均值/逆分母
方程低修正的正映射上界：令 $t_n$ 为该胞元全部非均值变化的物理强范数，
则

$$
\begin{aligned}
\|T_{{\rm low},k}\|\le{}&
\sum_n\left[(\Gamma_{{\rm main},kn}+3\Gamma_{{\rm corr},kn})t_n
 +\frac32\Gamma_{{\rm base},kn}t_n^2\right.\\
&\left.\hspace{20mm}+216\Gamma_{{\rm rem},kn}
 (t_n+t_n^2+t_n^3/3)\right]
 +B_{{\rm low},k}\|D_{\rm low}(z)-D_{\rm low}(z_{\rm aux})\|.
\end{aligned}
$$

该式作用于完整源的低频输出投影，不是有限Taylor源或角网格别名源。
它没有给高浅端高度强加零条件。高场和独立 $z$ 方程必须继续联立；
本定理本身不是整面存在结论。

**证明。** 对每个 $m=2,4,\ldots,92$，记真实线性头部状态为
$y_m=(Q_m,\Xi_m)$。使用 R29 的 gauge

$$
Q=(r/r_c)^{m^2-4}q,\qquad
\Xi=(r_c/r)^{m^2-4}\xi.
$$

以该胞元的源坐标 $x$ 微分，精确方程为
$q_x=a\xi,\ \xi_x=-bq$，其中 $a,b\ge0$。
其精确流行列式为一。所用 Peano–Baker 区间同时包围完整流、所有正向
子区间及反向子区间的绝对流。跨胞元的 $\Xi$ 乘数明确为
$\rho^{\pm1}$，$\rho=2^{11/4}$，未把不同 $\mu_n$ 规范互换。

令 $\phi$ 为真实far-admissible列，$\psi$ 为
$Q_{\rm cut}=0,\ \Xi_{12,\rm cut}=1$ 的真实列。所有46个真实
$\phi_Q({\rm cut})$ 已由 R29 的完整列包围证明非零。
精确归一化列是
$\Phi=\phi/\phi_Q({\rm cut})$；计算只在取绝对上界时使用该分母的
正绝对下界，并不把这个下界当作精确分母。于是物理Wronskian满足

$$
\mu_n(\Phi_Q\psi_\Xi-\psi_Q\Phi_\Xi)=\mu_{12}.
$$

对第 $n$ 胞元的canonical源 $N_\Xi$，零浅高度、零线性far缺陷的
Green列，忽略不影响绝对估计的符号，在 inner 目标使用

$$
\frac{\mu_n}{\mu_{12}}\Phi(r)\psi_Q(s),
$$

在 outer 目标使用

$$
\frac{\mu_n}{\mu_{12}}\psi(r)\Phi_Q(s).
$$

这由常数Wronskian的变参数公式直接得到，避免了相减两个巨大Cauchy
传播子。在同胞元，按 $s\ge r$ 与 $s\le r$ 分别积分；$p$ 和 $\kappa$
分量各自取径向sup后相加。父面板内包含两种顺序时把该面板计入两次，
仍为正上界。跨胞元的顺序没有歧义。具体有序和见本课题notes中的
`2026-11-12-closure-common-strip-panel-green.md`。

从canonical状态到物理强变量的精确关系为

$$
p_m=imr^3Q_m,\qquad
\kappa_m=m^2r^3Q_m+\frac{\sqrt{12}\mu_n}{r^4w}\Xi_m.
$$

令 $a_n\ge1+2B_n/9$ 为密度表中已固定的 `Q_coefficient`
（实际取向上dyadic值），并写

$$
V=\overline X_n\left(a_nr^3+
 \frac{\sqrt{12}\bar\mu_n}{r^4w}\right),\quad
T=\frac{a_nr^7w}{a_nr^7w+\sqrt{12}\bar\mu_n}.
$$

于是

$$
\frac{r^3}{V}=\frac{T}{\overline X_na_n},\qquad
\frac{\sqrt{12}\mu_n}{r^4wV}
 =\frac{\mu_n}{\bar\mu_n}\frac{1-T}{\overline X_n}.
$$

这些正比值直接围住两个物理分量，不把 $V$ 的两个正项分别除后相加。
源变换恰为 $N_\Xi=r^4wf/(\sqrt{12}\mu_n)$。因此每片的canonical正材料是

$$
\int\frac{r^4V^2}{\sqrt{12}\mu_n}\,d\log r,
\qquad
\int\frac{r^4V^2}{\sqrt{12}\mu_n}\,|d\log w|.
$$

R26的真实源值和半径包围给出这些积分上界。新半径子片的严格性在§2证明。
代码未使用独立浮点 $r$、$r'$ 去冒充一个实函数。

现在将真实辅助中心写成 $L_2+R$。每胞元的 $R$ 包含全部非m2线性模和
整个非线性辅助修正盒；令其canonical逐模质量为 $c_l$，总量上界为
$\mathcal R_n$。物理转换与 $|l|\ge2$ 给出

$$
\text{第 }l\text{ 模的共同物理帽}
 \le\frac{c_l}{\mathcal R_n}\,
 \epsilon_n(r),\qquad
\epsilon_n(r)=\frac{\mathcal R_n}{\overline X_n}
 e^{-2(\tau_{{\rm ref},n}-\tau(r))}.
$$

质量 $c_l$ 先取该胞元径向sup，故不依赖 $r$。R33 §16.7 的卷积论证
使 $DQ(R)$ 的源频谱由固定质量 $\eta*\delta$ 支配，得到外乘 $3$ 的
`corr` 核；不能把仅有点态 $\ell^1$ 小性直接替换此论证。

$L_2$ 只有固定的两个signed频率。其源频谱由
$\nu_m=(\delta_{m-2}+\delta_{m+2})/2$ 支配，总质量至多为输入范数，
仍与 $r$ 无关。R33的二材料恒等式及精确
$C_m=\sqrt{12}\mu_n\Xi_m/(r^4wV)$ 给出 R33 (33.101)
的 $g_1,g_\lambda$；其完整表达式与实幅/复半幅约定均在该式保留。
其因子 $2$ 已包含在 `main` 内。其余变化的二次项有系数 $3/2$，完整
均值及点态逆分母的余项有导数界 $216(V/w)X^2$，分别给出 `base` 和
`remainder`。这些是完整余式上界，不是Taylor多项式替代。

因此每一个源族都有固定、非负、总质量不超过输入范数的 Fourier
序列。先积分真实有序核，再对46个输出块取最大值，即得到 $\ell^1$
算子范数。既无需乘46，也没有交换径向sup与频谱求和。

所列程序在cells12..23执行全部552个真实有序模/胞元计算；其余201胞元
使用已付真实整胞元核。装配遍历每一个 $k,n,m$，对独立有效上界可取较小
者，对所有模式取较大者。所有标量运算向外包围，最后向上压成dyadic。
§1的已完成输出及固定源哈希因此支付所宣称的全部矩阵项。

far评估是同一个Green公式在 $r_{225}$ 上的 $Q$ 分量，再乘
$e^{38m}/S_F$。真实far线性列的该 $Q$ 初值为一，故代码保留
$\mu_n/(\mu_{12}|\phi_Q({\rm cut})|)$ 的完整因子。边界提升由同一个
$\psi$ 列得到，低far参数的 $S_Fe^{-38m}$ 与评估中的因子恰相消。
因此§3的far行与 $E B_{\rm low}$ 不来自物理窄范数的免费升宽。
全部断言得证。$\square$

**定理42.2（同实度规的强参考重标）。** §4–5中的所有缩放关系成立。
它们要求保留同一个连续 $\tau(r)$，以及同一真实源与完整辅助盒输入；
不允许用另一度规或另一角宽函数的数据直接替换。证明见§4–5。

## 1. 完成的对象

`closure_panel_centred_low_green_v2.py` 的作业52401已正式 exit $0$：
wall $968.043374$ 秒，峰 RSS $123424$ KiB。它完成了
cells $12,\ldots,23$ 上全部 $46$ 个真实低频，分别保存十二个完整胞元包。
每一模完成后另存恢复行；完整胞元包和最终 summary 才声明全窗口覆盖。

`closure_assemble_centred_green.py` 的作业22069也已正式 exit $0$：
wall $44.186756$ 秒，峰 RSS $133788$ KiB。其输出
`2026-11-12-closure-centred-four-green.json.gz` 为 $1521122$ 字节，SHA256：

```
d33768666cda08a4991d48911f276135b67aab4354b3d7bc6e83b491da655456
```

该包包含四个完整 $213\times213$ 正核矩阵、四条真实 far-$z$ 源行、
每胞元 $B_{\rm low}$、以及 $E B_{\rm low}$。所有频率
$m=2,4,\ldots,92$ 均实际计算；没有用 M8 零填充支付高列。

cells12..23 使用真实有序面板及逐面板角宽/物理材料，cells24..224 使用
此前已证的真实整胞元基本列、$\mu_n$ 端口变换和明确的材料上界。
包中的每一源胞元、每一目标胞元都被覆盖。其作用域为 node12 到真实 R18
深尾接口；outer cells0..11、全前缀及整面几何仍是独立工作。

四核的语义、频谱质量及完整均值/逆分母余项见 R33 §16–17，以及
`2026-11-12-closure-common-strip-panel-green.md`。`main` 已含 $DQ$ 的
导数常数；`corr` 外乘 $3$；`base` 的二次映射系数为 $3/2$；
`remainder` 已含逐点 $V/w$，完整余项导数外乘 $216X^2$，不得再乘一次
胞元 $A_\ast$。

## 2. 同一真实源上收紧PB子片半径

旧面板程序把父源面板的半径范围交给其所有 PB 子片。该操作是有效的
上界，但会积累严重的 gauge 区间依赖，并在部分中模丢失投影图。
完整输出使用独立 `closure_weighted_panel_flow_v4.py`。

对固定父面板的真实两端半径 $r_-,r_+$ 和任意内部源坐标 $x$，它分别围住

$$
r_-+\Delta r(x_-,x),\qquad r_+-\Delta r(x,x_+),
$$

并取交。其中在这里的cells12..23，冻结源恰满足

$$
\Delta r(a,b)=\frac18\operatorname{TV}_{[a,b]}
\left(\frac{w}{\sqrt{1+w^2}}\right)
 +\alpha\int_a^b\frac{dr_o}{1+w^2}.
$$

所有 $w$ 临界点均保留。第一项由真实源值给出；第二项由正的
$r_o(b)-r_o(a)$ 和同片 $w$ 上下界给出上下包围。两端锚点来自原真实源包，
故交集仍包含同一个实半径。新的 PB 子片仅把这个更小的真实半径区间代入
原正核，Peano–Baker公式、$AB<2^{-20}$ 门、冻结全局warp和全部数学边界
不变。

在此修正后，全部12胞元、全部46模的投影图均实际保持非零。
最坏对角矩阵项为

| 核 | 所有213胞元对角的统一上界 |
|---|---:|
| `main` | $2^{-41}$ |
| `corr` | $2^{-35}$ |
| `base` | $2^{-20}$ |
| `remainder` | $2^{-74}$ |

这些是对角项，不是整个矩阵的算子范数。跨胞元增益必须保留：例如目标
cell14的 `corr` 行和约为 $2^{-7.323}$，主源仍是cell12。因此后续联合检查
采用完整正矩阵和独立距离权，不把小对角线当作收缩结论。

## 3. 数值表示与深端规范

矩阵每一项以 `[mantissa,binary_exponent]` 保存，表示精确的向上dyadic数
$\mathrm{mantissa}\,2^{\mathrm{binary\_exponent}}$。舍入保留24位有效整数，
相对放大量不超过 $2^{-23}$；它不是二进制浮点近似的裸展示值。

far行实际计算的是

$$
z_m=e^{38m}Q_m(r_{225})/S_F,
\qquad
S_F=\frac{\varepsilon}{r_c^3}\delta_{224}^{11/2}.
$$

其中 $Q$ 是 height 系数，$\Xi$ 是 canonical momentum，不与物理 $\Pi$
互换。这里 $z_m$ 已吸收角宽权重，其 $\ell^1$ 范数等于前文报告记作
$|z|_{38}$ 的物理参数规范；不能再给这些加权坐标重复乘 $e^{38m}$。
输出 $E B_{\rm low}<0.015870698936$。

四条 far 源行的行和上界分别满足

$$
\log_2 F_{\rm main}<-2211.82,\quad
\log_2 F_{\rm corr}<-2205.59,\quad
\log_2 F_{\rm base}<-2190.96,\quad
\log_2 F_{\rm rem}<-2244.78.
$$

这些量仍需乘对应源范数/非线性常数，不能直接称为参数误差。
辅助中心的真实 $|z|_{38}\le2^{-2231}$ 来自 R38 的已付非线性低边界，
后续独立参数球可取 $2^{-2200}$ 并显式检查两者的差。

## 4. 同一真实度规下的幅度重标定定理

以下是完整的条件工具；它不改度规，也不把旧stored-g改称新有理g。
设 $q$ 是本次参考，$s$ 是另一组在同一实度规上已付的完整46低模辅助盒，
两者使用同一 $B_n,a_n$ 和同一胞元常值宽度 $\tau_{{\rm ref},n}$。
**定义新证明空间继续使用本次 $q$ 的同一个函数 $\tau(r)$**，不是把另一
份强参考账本原有的 $\tau$ 自动认作同一函数。

令

$$
\sigma_n=\frac{\overline X_n^s}{\overline X_n^q}>0,
\qquad V_s(r)=\sigma_nV_q(r)\quad(r\in I_n),
$$

并令 $\mathcal R_n^q,\mathcal R_n^s$ 为相应“完整辅助修正盒 + 线性非m2模”
的 canonical 质量上界。假定这些正的上界已明确计算。
再定义

$$
\eta=\frac{|Q_{2,\rm cut}^s|}{|Q_{2,\rm cut}^q|}.
$$

由于真实基本列、$w,r,\mu_n$ 和 $S_F$ 完全不变，已有四核可严格重标为

$$
\Gamma^s_{{\rm main},kn}
 \le\frac{\sigma_n\eta}{\sigma_k}\Gamma^q_{{\rm main},kn},
$$

$$
\Gamma^s_{{\rm corr},kn}
 \le\frac{\sigma_n}{\sigma_k}
   \frac{\mathcal R_n^s}{\mathcal R_n^q}
   \Gamma^q_{{\rm corr},kn},
$$

$$
\Gamma^s_{{\rm base},kn}
 \le\frac{\sigma_n^2}{\sigma_k}\Gamma^q_{{\rm base},kn},
\qquad
\Gamma^s_{{\rm rem},kn}
 \le\frac{\sigma_n^3}{\sigma_k}\Gamma^q_{{\rm rem},kn}.
$$

**证明。** 新状态范数在目标胞元除以 $\sigma_k$。$d_s=\sigma_n^2d_q$，
故 `base` 有所列的平方缩放；`remainder` 还含
$V_s/w=\sigma_nV_q/w$，多一个 $\sigma_n$。
主m2场的每个归一化帽按 $\eta/\sigma_n$ 缩放，与
$d_s/d_q=\sigma_n^2$ 相乘即得 `main`。
剩余中心的形状

$$
\epsilon_n^s(r)=
\frac{\mathcal R_n^s}{\sigma_n\overline X_n^q}
 e^{-2(\tau_{{\rm ref},n}-\tau(r))}
$$

相对于 $\epsilon_n^q$ 缩放为
$(\mathcal R_n^s/\mathcal R_n^q)/\sigma_n$；再次乘源的平方缩放即得
`corr`。上述因子每胞元为常数，可从所有有序积分、分量sup和Fourier算子
范数提出。所有关系保留全部46低模。证毕。

far四行没有目标物理范数 $1/V$，故只去掉上述 $1/\sigma_k$。
$B_{{\rm low},k}$ 除以 $\sigma_k$；$E B_{\rm low}$ 不变。
真实R18映射本身及 $C_D=2^{1967}$ 不变，辅助中心和其参数球必须另外选择
并核验，不能沿用小幅度中心的 $2^{-2231}$。

## 5. 中频、无限高频和纯低残差的同域重标

有限中频的源到状态核同样满足

$$
\Gamma^s_{{\rm mid},kn}
 \le\frac{\sigma_n^2}{\sigma_k}\Gamma^q_{{\rm mid},kn}.
$$

记 $\sigma_-\le\sigma_n\le\sigma_+$。整个头部的无限高频范数满足
$\|H\|_s\le\sigma_-^{-1}\|H\|_q$，源范数满足
$\|f\|_{Y_q}\le\sigma_+^2\|f\|_{Y_s}$。因此无须重新积分即可取

$$
\Gamma^s_\infty\le
 \frac{\sigma_+^2}{\sigma_-}\Gamma^q_\infty.
$$

这是直接的范数比较，不要求误认两个连续角宽定义。若要使用R33的更紧
无穷窗公式，也可取 $k_s\ge\sigma_+k_q$；因
$\chi_s=(cV_s/w)/k_s\le\chi_q$，原 $\tau$ 的导数门仍成立，$B$ 和
胞元内 $\partial_r\log V$ 不变。胞元接口及强参考的完整小球门仍需逐项
确认。

已有纯低高频残差只使用完整 $\overline X_n$ 盒、共同宽度
$\tau_{{\rm ref},n}$ 和通用全源解析界，不使用 q003 的具体高频谱。
该事实已由尾代理逐源核对。因此有限目标胞元可取

$$
b^s_{{\rm pure},k}\le
 \frac{\sigma_+^2}{\sigma_k}b^q_{{\rm pure},k},
$$

无穷块可取 $\sigma_+^2/\sigma_-$ 倍。固定同一个独立 R18 参数球时，
纯深边界只除以目标 $\sigma_k$，无穷块除以 $\sigma_-$。
全部均值和逆分母仍使用新的 $A_n^s=\sigma_nA_n^q$，不能复用旧幅度值。

## 6. 实际强M20的接口范围

R39的实际强M20来自 q085 已成功M20端口在新有理深g上的完整重求，响应
SHA256为

```
528fd51921f7cad71445d76669b44e60279c0fc31cddf9041f8ea5b1f7477962
```

它不是当前原stored-g的 q095 M24。其所有20个实际高度以及其余26个独立
低频方向都必须保留。现有输入的数值定位为
$\sigma_n\simeq16.33245\text{--}17.85330$；这些近似值不是重标矩阵
使用的舍入规则，最终矩阵必须使用逐胞元向外包围的比值。
R39已付真实辅助参数球为 $2^{-2224}$。

强M20重标后仍须直接复核完整联合映射和带权Lipschitz行。
本文件给出了不会更换度规或漏掉高模的可执行变换，尚不将这些待执行门
登记为成功。

## 7. 复算与固定依赖

完整数值包和执行入口的列表在
[已完成 Green 清单](../notes/2026-11-12-closure-centred-green-stable-manifest.json)。
该清单保留了两项正式退出码、全部十二个完整胞元包、恢复记录及依赖哈希。
本证明和该清单的固定版本由
[R42 清单](../notes/2026-11-12-closure-r42-stable-manifest.json) 记录。
准备中的联合正盒程序不属于这份完成清单，其是否成功须由实际运行输出决定。
