# 共同解析宽度上的真实面板 Green：中心分解与可复算列

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）。日期：2026-11-12。

本记录属于 R26/R29/R33/R38 的同一新有理深源。这里的实际高度参考仍是
q003 的 node12 数据；R39 的实际强 M20 是后续同源重标定的独立对象，不能
把本记录中的幅度常数直接移到 R39，更不能移到原 stored-g 的 q095 解。

## 1. 当前对象与尚未作出的结论

固定全部物理模 $m=2,4,\ldots,92$ 的浅端高度和 R18 的真实线性深子空间。
在同一实背景上令

$$
U=(Bp/V,\kappa_\perp/V),\qquad
d=(r^{-1}+|w_r/w|)V^2/w.
$$

每胞元使用 R33 已定义的连续 $\tau(r)$，状态范数是两个分量分别取径向
sup 后的 $\sum_m(1+|m|)e^{\tau(r)|m|}$ 范数。源范数采用
$\sum_m\sup_r e^{\tau(r)|m|}|f_m|/d$。本记录的 $\Gamma$ 已含实际参考幅度
$V$：源是 $d$，输出还除以 $V$。它不是未计幅度的裸基本解增益。

若把整个中心只用 $\|L\|\le1$ 统一估计，R33 旧的粗导数系数会给
$64\Gamma$。因此单个 $\Gamma\simeq2.358$ 仍不能支付收缩门。
下面的工作保留真正的中心及径向材料，不能把一个较小的 $\Gamma$ 本身
称为完整闭合。

最终目标是围绕已经存在的辅助解 $L_{\rm aux}$，估计

$$
G_{\rm low}\Pi_{\rm low}
 [f(L_{\rm aux}+v+H)-f(L_{\rm aux})]
 +B_{\rm low}[D_{\rm low}(z)-D_{\rm low}(z_{\rm aux})].
$$

低修正的常数项恰为零。独立 $z$ 方程保留真实 far trace；不从较窄的
共同物理范数免费推出宽度 $38$ 的深参数界。高场、深图反馈、全部均值和
最终前缀匹配仍须在联合正矩阵账本中支付。

## 2. 有序核及真实材料

令 $\phi$ 是 far-admissible 列，$\psi$ 满足
$Q_{\rm cut}=0,\ \Xi_{12,\rm cut}=1$。$\phi$ 除以其非零浅端高度增益；
其绝对值以已证增益的正下界归一。物理 Wronskian 为
$\mu_{12}\phi_Q({\rm cut})$。

在一个胞元内，面板按 inner 到 outer 排列。记 $P_i^\phi,K_i^\phi$
为 $\phi$ 的加权物理 $p,\kappa$ 分量各自的面板 sup，$\psi$ 同理。
对某个非负源材料 $d_*$，定义

$$
I_j^\phi=\int_{P_j}e^{-m\tau(s)}|\phi_Q(s)|
 \frac{s^4w(s)}{\sqrt{12}\mu_n}d_*(s)\,ds,
$$

并同样定义 $I_j^\psi$。目标在面板 $i$ 时，一个有效的 $p$ 界是

$$
\frac{\mu_n}{\mu_{12}}
\left(P_i^\phi\sum_{j\ge i}I_j^\psi+
 P_i^\psi\sum_{j\le i}I_j^\phi\right).
$$

$\kappa$ 用相同次序另取 sup，最后才相加。共同面板计入两次是安全的
上界。跨胞元核相应使用一侧物理列 sup 乘另一侧源积分。该构造保留真实
源位置，不将 valley 源与整个胞元的所有增益任意相乘。

两种材料分别为

$$
d_1=\frac{V^2}{rw},\qquad
d_\lambda=\frac{|w_r/w|V^2}{w}.
$$

它们变为 canonical 源后的面板积分由

$$
\frac{r^4V^2}{\sqrt{12}\mu_n}\,d\log r,
\qquad
\frac{r^4V^2}{\sqrt{12}\mu_n}\,|d\log w|
$$

分别包围。全部 $r,w,V$ 和角宽均来自同一真实源。全局冻结 warp 系数
$\alpha$ 保留；未以独立浮点 profile 替代实函数。

## 3. 四个中心化核

设 $L_2$ 为真实线性参考的 $m=2$ 部分，
$L_{\rm aux}=L_2+R$。$R$ 包含辅助解的完整 canonical 修正盒，以及真实
线性参考的其余所有已保存模式。令其逐胞元 canonical 质量界为 $R_n$，则

$$
\epsilon_n(r)=\frac{R_n}{\overline X_n}
 e^{-2(\tau_{{\rm ref},n}-\tau(r))}
$$

给出一个合法的源形状。这里不是把点态 $\ell^1$ 范数直接变成
$\ell^1$ 的径向 sup：每一模的 canonical 径向 sup 质量先固定为 $c_l$，
再以 $\eta_l=c_l/\sum c_l$ 控制该模的所有径向位置。因此之后的
$\eta*\delta$ 频谱质量独立于 $r$，总和不超过输入范数。

对主中心写

$$
A=\partial_\theta u_2-u_1/B,\quad
C=u_2+\partial_\theta u_1/B,\quad
S=\partial_\theta u_1/B,\quad T=u_1/B.
$$

其中精确恒等式

$$
C_m=\frac{\sqrt{12}\mu_n\Xi_m}{r^4wV}
$$

消除了 $Q_m$。这一步不使用数值相减。主中心的帽是完整实 cos/sin 幅度，
已含 $e^{2\tau}$；其两个 signed complex 半幅各为一半。

四核约定如下，消费时不得重复常数：

| 核 | 已包含的源形状 | 后续系数 |
|---|---|---|
| `main` | $L_2$ 的 $DQ$，两材料及精确 $C=\Xi$ | 已含导数的 $2$，不再乘 $2$ |
| `corr` | $\epsilon_n(r)(d_1+d_\lambda)$ | 完整其余中心的 $DQ$ 外乘 $3$ |
| `base` | $d_1+d_\lambda$ | 变化二次映射 $\frac32t^2$，导数 $3t$ |
| `remainder` | $(V/w)(d_1+d_\lambda)$ | 完整均值/逆分母余项导数外乘 $216X^2$ |

`main` 的两材料权具体为

$$
g_1=2E\widehat A_2,
$$

$$
g_\lambda=2\left[
 \widehat C_2\max(1/3,1/B)
 +w^2\left(\widehat U_{2,2}/B+\widehat S_2/3
 +\widehat S_2/B+\widehat T_2/(3B)\right)\right].
$$

主中心的频谱质量由
$\nu_m=(\delta_{m-2}+\delta_{m+2})/2$ 支配，仍独立于 $r$。
因此各面板积分之后对输出低模取最大值，是对角 Fourier Green 的
$\ell^1$ 算子范数；不需要额外乘 $46$，也没有交换 sup 与 sum。

完整二材料公式、均值和逆分母余项的证明见 R33 §16–17。
这里保留整项余式，不以有限 Taylor 截断冒充原 Darboux 方程。

## 4. 已正式结束的计算

| 作业 | 正式状态 | 数学意义 |
|---|---|---|
| `physical-low-green-v2` / 28288 | exit $0$ | 整胞元共同范数账本；cell12 对角粗界 $2^{65}$，未付收缩 |
| `physical-panels-m92-probe` / 82473 | exit $0$ | 原 $\tau$ 真有序面板：cell12 $\Gamma\le5.591976$；cell13 $<2^{-43}$ |
| `physical-panels-m92-drop9over16` / 2598 | exit $0$ | 明确的新范数试探，cell12 $\Gamma\le2.357857$，仍未过门 |
| `physical-panels-m92-drop3over4` / 19720 | exit $0$ | 第二个明确的新范数试探，仍未付统一粗导数门 |
| `physical-panels-m92-detail` / 2322 | exit $0$ | 原 $\tau$ 的全部 $1873$ 个源面板和最坏贡献定位 |
| `physical-panels-m2-detail` / 66872 | exit $0$ | 同面板上的真实 $m=2$ 基本列 |
| `physical-m92-centre2-symbol` / 78472 | exit $0$ | 下述四个准确二次主部导数列 |
| `centred-panels-low46` / 42080 | exit $1$ | cell12 中模的区间投影丢号，尚无完整胞元输出；不能登记为全46证书 |

最后一个失败发生于旧 PB 子片继续使用整个源面板半径盒。当前独立
`closure_weighted_panel_flow_v4.py` 把每个 PB 子片的实半径用

$$
\Delta r=\frac18\operatorname{TV}\!left(\frac w{\sqrt{1+w^2}}\right)
 +\alpha\int\frac{dr_o}{1+w^2}
$$

从同一父面板两端双向包围。源面板、$\tau$、物理材料和数学边界全不变。
新实现逐模保存已完成的恢复行；恢复行本身不构成全窗口完成声明。

## 5. 最坏列的已付具体结果

在原 $\tau$、source/target cell12、输出 $m=92$、真实中心 $m=2$ 下，
`physical-m92-centre2-symbol.json.gz` 包括 $E d_1$、$d_\lambda$ 及全部
$w^2$ 二次项。各行是一个 signed 频移、一个物理输入分量的完整列上界：

| 输入频率 | $Bp/V$ 输入 | $\kappa/V$ 输入 |
|---|---:|---:|
| $90$ | $4.040218\times10^{-9}$ | $3.288556\times10^{-7}$ |
| $94$ | $9.822501\times10^{-10}$ | $7.919140\times10^{-8}$ |

输入列只除以 $1+|b|$，输出 $1+|m|$ 已在物理 Green 列中。
signed complex 中心的半幅恰好抵消 $DQ$ 的因子 $2$；没有再次除二。
这四列尚不包括其余中心、其他胞元、完整余项或联合深边界，所以只是
准确的局部导数列，不是整面或完整 Jacobian 的完成声明。

该结果解释了为何先前统一的 $64\Gamma$ 远大于实际需要的导数预算：
最坏源集中在 valley 后段，而 $d_1$、$d_\lambda$ 的不同结构和
$C=\Xi$ 恒等式不能一并抹去。后续按上面的四核完成全46、全213胞元和
独立 far-$z$ 正矩阵。
