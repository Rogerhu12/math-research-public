# R138 补篇：保持同一个v的四顶点体Gram包围

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇给出与[SG.12](R138-supplement-complementary-Gram-spectral-body-energy.md)
不同的完整closed-box上界。SG先分别放大 $M$、缩小 $\kappa$与分母；这里始终让
同一个 $r=|v|$同时出现在 $\kappa=Kr^2$、两个对角项和整个分母。
所用原格、真实mean、修补、support、两个梯度和source全不变。
本篇尚未赋予新majorant任何数值，也不重算已成SG的5个目标。

## 1. 原谱算子在v变量中的准确矩阵

沿SG取 $\eta=-\gamma m>0$、$r=|v|>0$、$\sigma>0$，同一未加权
$p=1,q=K$梯度的pointwise Gram准确为

$$
\mathcal G(\eta,r,u,K,\sigma)=\frac1\sigma
\begin{pmatrix}
\eta(1+u^2)/r+\eta^{-1}Kr&-(\eta-\eta^{-1})u\sqrt K\\
-(\eta-\eta^{-1})u\sqrt K&\eta Kr+\eta^{-1}(1+u^2)/r
\end{pmatrix}.
\tag{CV.1}
$$

它就是 SG.2 的 $(\eta A+\eta^{-1}B)/(\sigma|v|)$，没有加权修改原能量、
没有改变原frame或引入新的角/径向导数。

令原同一修补闭行的完整包围为

$$
|u|\le U,\quad r_-\le r\le r_+,\quad 0\le K\le K_+,
\quad t_-\le\eta\le t_+,\quad \sigma\ge\sigma_-=2/5,
\tag{CV.2}
$$

其中 $r_-$是完整inverse-angle gap减修补，$r_+=V$是完整 $v$的Wiener界加修补；
$t_\pm=\gamma_\pm m_\pm$保留独立moving mean，不以 $v$的非均值替代它。
允许把实际相关的 $\eta,r$放大成该rectangle，但不允许把同一个 $r$的不同
出现再分别选互不相容的端点。

## 2. 四个角点已经包住整个原box

**引理。** 在(CV.2)上，最大的pointwise特征值由 $u=U,K=K_+$以及
$(\eta,r)\in\{t_-,t_+\}\times\{r_-,r_+\}$的四个值支配。
它实际上是这个独立closed box的最大值；不声称是实际背景的最优常数。

**证明。** 先固定 $r,u,K$。原 $A,B$是半正定矩阵，故
$\eta\mapsto\eta A+\eta^{-1}B$是Loewner凸的。
对任一中间 $\eta$，凸组合的矩阵上界支配它，所以最大特征值至多是两个
eta端点的最大值。此步不分别最大化两个不相容的eta表达式。

再固定一个eta端点和 $r$。改变第二个基向量符号，可把(CV.1)的off-diagonal
写成 $|\eta-\eta^{-1}|\,|u|\sqrt K$；两个对角项均非负。
这个对称 $2\times2$非负矩阵的最大特征值随各项非减：对角增加是半正定增量，
off-diagonal的结论直接由

$$
\lambda_{max}\begin{pmatrix}p&q\\q&s\end{pmatrix}
=\frac{p+s+\sqrt{(p-s)^2+4q^2}}2,\qquad q\ge0,
\tag{CV.3}
$$

得到。因此可以把 $|u|,K$同时提高到 $U,K_+$。
这里**没有**声称矩阵对 $u$或 $K$本身Loewner单调；其off-diagonal导数
通常不半正定。符号变换只用于pointwise谱，不作为新的几何frame或角坐标。

最后固定这个eta端点与 $U,K_+$。令

$$
D_-=(1+U^2)\operatorname{diag}(\eta,\eta^{-1}),\qquad
D_+=K_+\operatorname{diag}(\eta^{-1},\eta),
$$
$$
C=\begin{pmatrix}0&-(\eta-\eta^{-1})U\sqrt{K_+}\\
-(\eta-\eta^{-1})U\sqrt{K_+}&0\end{pmatrix}.
$$

则 $\sigma_-\mathcal G=r^{-1}D_-+rD_++C$，其中 $D_\pm\succeq0$。
它对 $r>0$是Loewner凸函数，最大特征值在 $[r_-,r_+]$上由两个端点支配。
最后用正的 $\sigma_-$支配原分母即得结论。四个顶点都属于独立box，故同时
给出该box真正最大值。证毕。

## 3. 稳定、完整且不除K的公式

对每个上述四角点设

$$
M_r=1+U^2+K_+r^2,\qquad
\Delta_r=(1+U^2-K_+r^2)^2+4U^2K_+r^2\ge0.
\tag{CV.4}
$$

其值可直接取

$$
\boxed{\displaystyle
C_i^{corr}=\max_{\substack{t\in\{t_-,t_+\}\\r\in\{r_-,r_+\}}}
\frac{M_r(t+t^{-1})+|t-t^{-1}|\sqrt{\Delta_r}}
                         {2\sigma_-r}.}
\tag{CV.5}
$$

$\Delta_r=M_r^2-4K_+r^2$；(CV.4)用非负和避免不必要的消差。
也可直接用(CV.1)的两个对角及off-diagonal代入(CV.3)。二者相同。
同一个 $r$与 $K_+$在每项中保留，不把最后分母另改为 $r_-$。

根germ的实际正侧允许 $K=0$，整个proof按连续极限有效；无 $1/K$。
germ仍以原完整real球的绝对upper作 $K_+$，实际 $K\ge0$只用于原真正正侧。
body无需使用 $K_-$：它已被谱的单调性消去，而非被错误丢弃。

对每个原格，(CV.5)不大于同一个精确box的SG.12数学majorant。
这只是两个明确包围公式的解析比较；已成SG数值的rounding仍按原整球保留，
不以此宣称一个未执行的新十进制上界。

## 4. 新完整目标及既成量的复用

新科学目标可以用同原positive4+germ1，仅从原完整4650行和首germ消费(CV.2)。
原SG的mean/sign/inverse-gap修补、全参数、全接口、full-angle及实际DF资格均保留。
对4651片逐片形成(CV.5)并取完整max；没有运行旧SG.12循环、旧CE、旧几何ODE或
任何旧A0/mean/primitive目标。

整4651片完成后，可与已完成SG的整个 `C_spectral_upper`取min形成新完整
$C_{corr}$，这时两个upper都已完整。旧SG5条结果及true body/necessary gates原样
仅读引用，不能因新预算不同而修改旧结论。

随后按已经证明的同一SG.14–SG.17，仅对变化的比较常数形成新的
$w_{E,corr},a_{EE,corr},a_{EB,corr}$，body三门真通过时另形成条件allowance。
原 $C_H,\Gamma,A_\Theta,h_E,h_B,w_B,a_{BB},r_E,r_B$均只读，不重复发布为新目标。
这是保留同一个 $v$之后得到的不同能量majorant，不是重新执行原5条数值结论。

新的完整保存球仍须先通过RN的实际根必要筛查。除
$C_{corr}<23,w_{E,corr}<22,a_{EE,corr}<23/30$之外，
RX的同一个正方向给更强的廉价测试：

$$
\mathcal Q_{test}
=2-a_{EE,corr}-\frac{37}{30}
 -\frac3{10}a_{EB,corr}
 +\frac9{100}(1-a_{BB}).
\tag{CV.6}
$$

若其完整upper不大于0，根实际EE费用严格大于 $37/30$使真正预算型在
$(1,3/10)$上严格负，仍不用构造新finite Gram。
upper必须使用已保存 $a_{EE,corr},a_{EB,corr},a_{BB}$的lower；
若没有排除，也只是该测试未排除，不授真正root容量或完整逆。
在执行前不承诺(CV.5)会降低多少或任何新门能够通过。
