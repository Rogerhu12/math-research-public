# 完整高频源到低46的第一份实际反馈上界

2026-11-12，exact_closure。

入口 `closure_high_to_low_density_enclosure.py` 已完整执行，97656
formal exit0，resource也记录exitcode0；17.9975秒、峰102820KiB。
它计算的是一个有效但**未通过原低盒余量门**的充分上界，不能
把程序退出0写成联合闭合成功。

## 准确输入和规范

低窗使用R38的原q003 plateau2完整46盒，实际参考x、距离权W
与盒半径U均未改变。高窗使用tail已经支付的全部 $m\ge94$
联合盒，包括213个中频半径和真正无限窗口半径。源g、完整
160浅表、R26真实半径及全mean小根均保持相同；程序核对所有
原始输入SHA及高/低盒共同的物理密度包。

低距离为 $\max_n X_n(\Delta Y)/(W_nx_n)$；W字段是无量纲
倍数。高窗口的中频和无限频距离权分别按其包的实际定义读取，
没有把半径自动等同于距离权。

## 支付的完整源界

记物理幅度包络为

$$V(r)=\overline X_n\left[a_n r^3+
\frac{\sqrt{12}\overline\mu_n}{r^4w(r)}\right],$$

以及 $c=1/r+|w_r/w|$。R33物理source为 $f=w\mathscr H_\perp$，
其canonical source准确转换为

$$N_\Xi=\frac{r^4w}{\sqrt{12}\mu_n}f.$$

因此所需积分密度是

$$J_n=\int_{I_n}\frac{r^4c(r)V(r)^2}{\sqrt{12}\mu_n}\,dr.$$

本版保守地用 $r_c\le r\le(257/256)r_c$、已付w下界与
$\int c\le L_n+5(n+9)$ 包围J。没有将source的点值或端点值
充作积分，也未漏掉warp导致的实际对数导数。

低场在其常数角宽 $\tau_n^{\rm lo}$ 上的归一强范数至多1；
设完整高场在同一cell的连续角宽 $\tau(r)$ 上范数至多
$R_n=r_n^{\rm mid}+h_\infty$。R33完整差界给

$$\|f(L+H)-f(L)\|_{\mathcal Y_n}
\le64R_n(1+R_n).$$

这个界包含完整mean与所有乘法逆的无限级数，未截成二次
多项式。它尚未利用输入的具体频带支撑。

## 所有46输出模、源位置和角宽

对每个 $m=2,4,\ldots,92$、每对目标/源胞元k,n，以原真实
Wronskian列和有序同cell核计算 $\gamma^{\rm raw}_{knm}$。
目标角宽取低窗实际角宽，源连续角宽用该cell外端的严格下界。
程序完整计算

$$\widehat\gamma_{kn}\ge\max_m
\gamma^{\rm raw}_{knm}
e^{m\tau_k^{\rm lo}-m\tau_n^{\rm out}}.$$

于是

$$X_k(\Delta T_{\rm high})
\le\sum_n64\widehat\gamma_{kn}J_nR_n(1+R_n).$$

取max后乘整个源的Fourier总质量，不额外乘46。每个源胞元
仍独立保留，没有用统一全头角宽损失替代实际矩阵。相应
high→low的两个距离Lipschitz列也保留各自单位。

## 实际结果和下一收紧位置

原R38盒的最坏余量消耗比上界满足

$$\log_2(\text{所算比值上界})\approx210.46115547.$$

最坏项来自source12到target13、输出m92；target12同source和
同模的对数约206.85798。完整213×213 dyadic核与主导模在
`closure-high-to-low-density-v1.json.gz` 中。

这没有给实际反馈的下界，也不是无解结论。明确的过粗位置是：
先对完整高源取R33总范数，再把窄strip限制到有限低输出的较宽
strip，丢失了频率卷积定位和纯low残差本来更宽的解析性；J还
使用了整cell的w下界。后续首先消费tail保留宽low残差得到的
更小高频谱盒，再保留低×高的具体频率选择；完整高阶和mean
余项仍必须包围。此v1源码及输出冻结，改进使用新文件。

完整命令记录在同prefix的resource文件，所有输入、源和列组
SHA在主包中，可直接重算。当前没有新增数学result编号。
