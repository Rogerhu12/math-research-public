# R71 — 同一真实度量上的两侧内部高度重心化

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

**状态：已证明，含完整实际区间扫描。**

本文件说明 `closure_outer_internal_height_recentre.py` 的完整构造与
源差账本。它保留实际强 M20 参考的真实 $g$、所有外端非均值数据及
相位范围，只改内部 node 11 的一个候选高度系数。实际计算范围是
cell 11 和 cell 10 的原 10793 个材料面板；完整外解存在性不由此推出。

**精确补充：** R63 §5.1 显式补回辅助中心自身的非线性 far 提升。
旧 primary 的新 centre raw 区间须分别加
$[-E_{11,m},E_{11,m}]$，其中模式2小于 $5.663072\times10^{-2367}$、
模式4小于 $1.629825\times10^{-2368}$。真正完整的新端点见
`notes/2026-11-12-closure-r63-far-boundary-completion-r1.json` 的
`corrected_R71_rows`；所有正文显示宽界仍严格成立。以下已经选定的
准确 dyadic 候选、全部两侧源差和 mean 高度积分不变。选取中点只是
定义固定候选，旧选择式未含该项并不改变候选构造的合法性。

## 1. 一次明确选择，不是逐点评价的自由参数

记 node 12、11、10 的真实半径为 $b<c<d$。取 R70 的真实背景高度图
$S_{0,2}(c)$ 和已包围的候选中心残差 $e_2$。程序作一个明确的 dyadic
选择

$$
Q_2^{\rm new}(c)=\operatorname{mid}\!\left(
Q_2^{\rm old}(c)+\operatorname{mid}(S_{0,2})
                         \operatorname{mid}(e_2)\right),
\qquad \Delta Q=Q_2^{\rm new}(c)-Q_2^{\rm old}(c).
\tag{71.1}
$$

所有 `mid` 只用于选取新的**固定候选系数**，不表示把任何真实解、
背景函数或区间输入改成中点。选出的整数尾数与二进制指数完整保存。
物理高度变化是同一真实半径上的准确函数

$$
\Delta H=c^4\Delta Q.
\tag{71.2}
$$

它没有额外的 $w$ 因子。其他 19 个非均值模式与另外 12 个原端口的
非均值高度不变。node 11 的原物理 $h_r,h_{rr}$ 保留；因此把它重新
写成原连接动量坐标时，内部 $L$ 会随 $Q$ 改变，不能同时声称原 $L$
逐位不变。完整候选不是一次新的有限 ODE 求解。

## 2. 两侧真实正权 bubble

在每个 cell 使用原 R48 的同一归一 source 长度 $u\in[0,1]$，
不是把九个不等长 source 段简单拼成 $j+x$。令

$$
b_4(u)=u^2(1-u)^2,\qquad
I_n=\int_{\mathrm{cell}\ n} w(r)b_4(u(r))\,dr>0,
\qquad J_n(r)=\int_{r_{\rm inner}}^r w(t)b_4(u(t))\,dt.
\tag{71.3}
$$

$I_n,J_n$ 均为原已付五正积分中同一个 `b` 分量；没有重选各评价点的
积分常数，也没有重新定义一个近似半径函数。

两侧只有 $m=2$ 的完整实余弦幅改变：

$$
\begin{array}{lll}
\mathrm{cell}\ 11:&
\delta\overline K_2=\dfrac{\Delta H}{I_{11}}b_4(u),&
\delta H_2(r)=\Delta H\dfrac{J_{11}(r)}{I_{11}},\\[4pt]
\mathrm{cell}\ 10:&
\delta\overline K_2=-\dfrac{\Delta H}{I_{10}}b_4(u),&
\delta H_2(r)=\Delta H\left(1-\dfrac{J_{10}(r)}{I_{10}}\right).
\end{array}
\tag{71.4}
$$

其中 $\overline K=h_{\perp,r}/w$。所以第一行兼容恒等成立。因为
$b_4=b_4'=0$ 在两端，两个 cell 在外端都具有零高度变化和零物理
一、二阶导数变化；在共享 node 11，两侧高度变化同为 $\Delta H$，
且物理一、二阶导数变化均为 0。于是非均值高度仍为一个 $C^2$ 函数。

完整 source-$x$ 导数实际为

$$
\delta\overline K_{2,x}
 =\pm\frac{\Delta H}{I_n}b_4'(u)u_x,
\quad
\delta h_{2,r}=w\delta\overline K_2,
\quad
\delta h_{2,rr}=\frac w{r_x}
   (\delta\overline K_{2,x}+\ell\delta\overline K_2),
\qquad \ell=w_x/w.
\tag{71.5}
$$

实际扫描对每个原面板使用其真实 $u,u_x,r,r_x,w,\ell$ 包围，而非从
有限 ODE 右端取代新候选导数。高度同时从正 prefix 和 suffix 表达式
相交，并使用 $0\le J_n/I_n\le1$、$0\le b_4\le1/16$。

## 3. 完整 mean 与一个全局高度常数

在 $\mathcal A_{\sigma,1}$ 中，记原非均值状态范数为
$R_o=\|P_o\|_1+\|\overline K_o\|_1$，变化范数为
$\delta R=\|\delta P\|_1+\|\delta\overline K\|_1$。
程序使用的是**连接线段的统一包络**

$$
R_*=R_o+\delta R<1/64,
\tag{71.6}
$$

不是一个可能更小的新端范数。R33 的完整 mean 小根及其导数给

$$
|c_o|\le4R_o^2,\quad |c_n|\le4R_*^2,
\quad |\delta c|\le16R_*\delta R.
\tag{71.7}
$$

相邻 cell 使用相同非均值物理两 jet 和背景，所以 R44 的唯一 mean
根及其径向导数在 node 11 一致。由一个高度积分常数重建的完整高度
因此仍 $C^2$。

改变 mean 根一般会改变 mean 高度积分，程序真实支付

$$
\left|\Delta h_0(d)-\Delta h_0(b)\right|
\le\sum_{n=10,11}\sum_{p\subset n}
 \Delta r_p\,\sup_p w\,16R_{*,p}\delta R_p.
\tag{71.8}
$$

每个 $\Delta r_p$ 来自原真实正宽积分。选择一个常数使外 node 10
的 mean 高度不变，则更外 node 0 的 mean 高度也不变，而内 node 12
及自由放置的 cuff 承受式 (71.8) 所包围的高度位移。没有独立重置两个
cell 的 mean，也没有同时暗定两端绝对高度。固定新形状作纯相位旋转
时，角平均不变，所以这个常数相位无关。一般形状参数族仍按 R61
第 8 节允许它依形状参数而变。

## 4. 完整非线性源差

记 $E=1+w^2$、$s=r_x/r$，并令

$$
T=P_\theta,\quad U=\overline K_\theta-P,\quad
L_{\rm nm}=\overline K+ET,
$$

$$
Q=EsU^2+\ell\left[(\overline K+T)^2+
 w^2(2\overline KT+T^2-P^2)\right],
\quad A=\ell(2cL_{\rm nm}+c^2),
\quad l=c+L_{\rm nm}.
\tag{71.9}
$$

完整源为 $N=(Q+A)/(1+l)$，最后取非均值投影。对于指定的非零 Fourier
模式，投影不改变其系数；全部 mean 与逆分母生成的频率仍包含。

令 $R=N-Q$，下标 $o,n$ 表示原、新候选。精确代数恒等式为

$$
\delta R=
\frac{\delta A-l_n\delta Q}{1+l_n}
-\frac{(Q_o+A_o)\delta l}{(1+l_n)(1+l_o)}.
\tag{71.10}
$$

因此只要两个完整 Wiener 域 $L_o=\|l_o\|_1<1$、
$L_n=\|l_n\|_1<1$ 已付，便有

$$
\|\delta R\|_1\le
\frac{\|\delta A\|_1+L_n\|\delta Q\|_1}{1-L_n}
+\frac{(\|Q_o\|_1+\|A_o\|_1)\|\delta l\|_1}
 {(1-L_n)(1-L_o)}.
\tag{71.11}
$$

这里使用完整 mean 根差 (71.7)，并用

$$
\begin{aligned}
\|\delta l\|_1&\le|\delta c|+\|\delta L_{\rm nm}\|_1,\\
\|\delta A\|_1&\le|\ell|\left[
2|\delta c|\|L_{{\rm nm},o}\|_1
+2|c_n|\|\delta L_{\rm nm}\|_1
+(|c_n|+|c_o|)|\delta c|\right].
\end{aligned}
\tag{71.12}
$$

二次部分 $\delta Q$ 对原全部 20 模与新 $\pm2$ 变化作**准确有限卷积**。
每个乘积以

$$
\delta(FG)=F_o\delta G+\delta F G_o+\delta F\delta G
\tag{71.13}
$$

计算。这保留 $m=2$ 等模式的真实卷积支撑，避免把一个主要处于
$m=4$ 的二次范数无区别倒入 $m=2$。Wiener 代数范数中的所有乘积
常数为 1，因为权 $(1+|m|)e^{\sigma|m|}$ 次乘性成立。

如果 $(\delta Q)_m^{\cos}$ 为完整实余弦系数，则

$$
(\delta N)_m^{\cos}\in(\delta Q)_m^{\cos}
+\left[-\frac{\|\delta R\|_1}{(1+m)e^{\sigma m}},
         \frac{\|\delta R\|_1}{(1+m)e^{\sigma m}}\right].
\tag{71.14}
$$

程序以真实角权的严格**下界**作分母，不以用于上界输入范数的向上
舍入权作分母。复 Fourier 半幅与实余弦幅的 2 因子在代码中明确。

## 5. 不重做 ODE 的真实功能转移

R70 原 source 面板 $p$ 保存包含同一真实 $N_{o,m}$ 的区间
$[a_{p,m},b_{p,m}]$。令

$$
C_{p,m}=\max(|a_{p,m}|,|b_{p,m}|).
\tag{71.15}
$$

这是一个由保存 dyadic 端点定义的非负**确定常数**，不是要求
$|N_{o,m}(x)|$ 有正下界。若 $C_{p,m}>0$，从 (71.14) 支付

$$
|\delta N_m(x)|\le\kappa_{p,m}C_{p,m}
\quad(x\in p),\qquad
\kappa_m=\max_p\kappa_{p,m}.
\tag{71.16}
$$

若 $C_{p,m}=0$，程序只在新源差界也为 0 时继续，否则明确失败。
从未使用 signed 区间中点作分母。

R70 的独立绝对功能上界 $A_m^{70}$ 是逐面板、逐子位置以一个
不小于 $C_{p,m}$ 的源帽乘真实 adjoint 几何权后累加得到的。因此

$$
|\mathcal I_m(N_n)-\mathcal I_m(N_o)|
\le\kappa_m A_m^{70}.
\tag{71.17}
$$

此证明不需要保存每个几何核的新积分，也没有把有符号核的积分错误地
与一个变化源区间相乘。所有径向源位置由原 R70 证书和本次逐原面板
源差共同覆盖。

于是 cell 11 新候选中心的完整两模残差包含于

$$
e_{n,m}\in e_{o,m}-\frac{\Delta Q_m}{S_{0,m}(c)}
+[-\kappa_mA_m^{70},\kappa_mA_m^{70}],
\qquad \Delta Q_2=\Delta Q,\quad\Delta Q_4=0.
\tag{71.18}
$$

原真实内头的低动量/mean/高反馈仍保持在 $e_{o,m}$ 中，没有借新候选
把它们重置为有限 worker 数据。

## 6. 这个构造不改变更外端的完整线性残差

对整个 $[b,d]$，本次非均值候选变化及其一阶导数在两端均为 0。
真实变参数恒等式给

$$
\int_b^d\Phi(d,r)\,\mathcal L\delta Y(r)\,dr
=\delta Y(d)-\Phi(d,b)\delta Y(b)=0.
\tag{71.19}
$$

内部 node 11 处 $C^1$ 接合，所以没有漏掉一个内部跳跃项。
因此 node 10 及更外端的**全部线性边界残差不因内部重心化改善**。
改变的是候选的连续形状及完整非线性源 $N_n-N_o$；它必须继续进入
更外侧的有源 Green/Schur 账本。

本构造的用途是为真实局部匹配和连续残差提供更准确、兼容的中心。
它不取代完整外边值解的存在证明，也不把未通过的旧参数轴自动放大。

## 7. 完整执行范围与实际数值

[主包](../notes/2026-11-12-closure-internal-node11-height-recentre-r1.json)
与两个完成 cell 包保存同一候选的所有定义、严格端点、源差及 mean
高度账本。会话 39026 的工具与 wait4 均正式退出 0，wall 84.212198 秒，
峰值 34568 KiB；全部 **10793** 个原材料面板扫描完成，12 项门全部为真。
没有新的 ODE 或背景积分。

准确的新 canonical 系数是

$$
Q_2^{\rm new}(c)=
61855255778698022751261341340716513357862518611450126526807318921804056001615
\cdot2^{-367},
\tag{71.20}
$$

其变化为

$$
\Delta Q=
-1598959110399621790192415988000725501205652905956050061049338769015729
\cdot2^{-367}.
\tag{71.21}
$$

因此 $\Delta Q\approx-5.31898724836\cdot10^{-42}$，并有

$$|\Delta H|<3.340350\cdot10^{-47}.$$

以下总 mean 预算、状态范数、功能变化和 $m=2$ 残差的严格十进制界由
[准确分数账本](../notes/2026-11-12-closure-r71-fraction-bounds-r1.json)
从保存 dyadic 端点核销；该程序也已正式退出 0。

| 项目 | cell 11 | cell 10 |
|---|---:|---:|
| 完整连接线段状态范数 $R_*$ | $<3.429795\cdot10^{-18}$ | $<1.118059\cdot10^{-13}$ |
| 完整非均值状态变化 $\delta R$ | $<1.565127\cdot10^{-28}$ | $<1.320659\cdot10^{-30}$ |
| mean 高度积分变化的上界展示 | $1.405763\cdot10^{-66}$ | $1.005267\cdot10^{-62}$ |

总 mean 高度变化严格满足

$$\left|\Delta h_0(d)-\Delta h_0(b)\right|<1.005408\cdot10^{-62}.
\tag{71.22}$$

这不是把 mean 设为 0，而是把两个真实完整 mean 根之差沿同一背景
正宽积分后得到的上界。按第 3 节选择外高度常数时，它给 cuff 与内切口
的实际位置变化预算。

对 cell 11，式 (71.17) 的功能变化实际给出

$$
|\delta\mathcal I_2|<1.542922\cdot10^{-65},\qquad
|\delta\mathcal I_4|<3.457076\cdot10^{-61}.
\tag{71.23}
$$

新 $m=2$ 完整候选中心包满足

$$\boxed{|e_{n,2}|<1.088656\cdot10^{-56}.}\tag{71.24}$$

相对于 R70 严格正的原中心偏移，这改善超过 29 bit，但不声称超过
30 bit。新上界仍约为原 R59 的 $2^{-193}$ 轴的 136.672 倍，**没有
宣布原固定中心参数盒已经容纳了完整外修正**。$m=4$ 的当前宽区间仍
约为 $[-1.058,1.410]\cdot10^{-52}$，没有在本次把它认作精确小残差。

最后，第 6 节的相消量词仍适用：node 10 与更外端的完整线性边界残差
没有因这次内部候选调整而变化。更外侧的完整源响应、参数族与 Schur
问题继续由同一真实方程支付。

## 8. 可重现性与范围

执行入口为
[closure_outer_internal_height_recentre.py](../computations/closure_outer_internal_height_recentre.py)，
它记录全部真实度规、原正权积分、原候选及 R70 功能的输入 SHA，
并在每个完整 cell 后保存恢复包。所有执行命令见
[resource](../notes/2026-11-12-closure-internal-node11-height-recentre-r1-resource.json)。

源码 SHA-256 为
`de1f64511d94d76810f084f3b7fd472d9c27258d91e8a0942901c5f8e394cc8a`。
本结果的有限改动明确只是内部候选改进，未改变外cut的全部20H、g、
时间/相位范围，也未把完整外部精确解或闭面几何当作已完成。
