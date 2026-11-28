# 原 Haar 根图的统一中位间隙、迹类物理极化与真实两坐标

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本稿在[全部有限头根图](R12-appendix-all-finite-haar-head-root-graphs-half-weak-limit-and-strong-zero.md)的完整原权与全部分支上，支付此前未付的整块算子范数估计。它使用真实 $8^L$ 次项，而不从主项的无原子分布推出最小行间隙。由此得到全部 Walsh 直和根图与同一个明确物理投影之间的迹类差，以及真实注入、稠值的两坐标。原进位仍完整保留；不构造完整 $C$ 的闭根。

## 1. 原权和精确中心行

固定原 Haar 尾 $C=A^{(m)}$，$m\ge0$，写 $a_j=\alpha_{m+j}$。沿用[全 Walsh 块](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md)：
$$
\mu_L=(a_L+\mu_{L+1})/2,\qquad a_L/2\le\mu_L<a_L,
$$
$$
N=2^L,\qquad
\beta_{L,k}=\prod_{\ell=1}^{k}a_{v_2(\ell)},\qquad
r_L=(\mu_L\beta_{L,N-1})^{1/N}.
$$
原正闭合有限头 $C_L$ 的 companion 图平衡权及其中心为
$$
w_{2k+\varepsilon}=\beta_{L,k}r_L^{-k-\varepsilon/2},\qquad
h_L=\tfrac12\log(\sqrt{r_L}/\mu_L),\qquad \varepsilon\in\{0,1\}.
\tag{1}
$$
令
$$
A=100\,16^m,\quad B=105\,8^m,\quad H_0=150\,2^m,\quad
c_m=-\tfrac{20}{3}16^m+15\,8^m-\tfrac{850}{3},
$$
$$
d_j=-\log(a_j\beta_{j,2^j-1}),\qquad
\delta_L=\log(a_L/\mu_L)\in(0,\log2).
$$
直接对原权的四项作有限几何和，准确得到
$$
d_j=A16^j-B8^j+H_0(j+2)2^j+c_m2^j,\qquad
\lambda_L:=-\log r_L=(d_L+\delta_L)/2^L.
\tag{2}
$$
若 $k=\sum_{j<L}b_j2^j$，原前缀分块为
$-\log\beta_{L,k}=\sum_{j<L}b_jd_j$，并且
$\sum_{j<L}d_j=d_L+\log a_L$。所以中心行准确为
$$
\ell_{L,k,\varepsilon}:=\log w_{2k+\varepsilon}-h_L
=\sum_{j<L}(b_j-\tfrac12)(2^j\lambda_L-d_j)
+\frac{2\varepsilon-1}{4}\lambda_L.
\tag{3}
$$
中心偏移及两物理分量都没有省略。

对 $u=k/2^L$ 取以零结尾的二进制展开 $u=.b_{L-1}\cdots b_0$，定义
$$
f_b(u)=\sum_{\nu\ge1}\operatorname{bit}_\nu(u)b^{-\nu},
\qquad h_b(u)=u-f_b(u),\qquad b=8,16.
$$
令
$$
t_\varepsilon=(2\varepsilon+1)/4,\qquad
c=B/A=\frac{21}{20\,2^m}.
$$
由 (2)–(3) 得
$$
\boxed{\quad
\frac{\ell_{L,k,\varepsilon}}{A8^L}
=2^L\bigl(h_{16}(u)-7/15\bigr)
+t_\varepsilon-c\bigl(h_8(u)-3/7\bigr)+e_{L,k,\varepsilon},
\quad |e_{L,k,\varepsilon}|\le4\,2^{-L}.
\quad}
\tag{4}
$$
这里的界对 $m\ge0,k,\varepsilon$ 一致。为核实常数：除两主幂外，(3) 的余项绝对值不超过
$H_0 2^L+|c_m|/4+\log2$；除以 $A8^L$ 后，再计入有限几何和的端项，其界为
$$
(1/30+c/14)8^{-L}+(3c/4)2^{-L}
+(H_0/A)4^{-L}+(|c_m|/4+\log2)/(A8^L).
$$
使用 $c\le21/20$、$H_0/A\le3/2$、
$|c_m|/(4A)\le61/80$、$\log2/A<1/100$，
$8^{-L}$ 的总系数小于一，故该式不超过 (4) 的界。

## 2. 两个固定字及其全部移位尾

考虑
$$
u-f_{16}(u)=7/15.
\tag{5}
$$
因为 $7/15=.7777\ldots$（十六进制），
$7/15+f_{16}(u)$ 的十六进制数字恰为 $7+\operatorname{bit}_\nu(u)$；
没有进位。写成二进制，就是替换
$$
\varphi(0)=0111,\qquad \varphi(1)=1000.
\tag{6}
$$
因此 (5) 的解恰为两个互补的无限固定字 $u_-,u_+=1-u_-$，
分别以 $0,1$ 开头。确实，(6) 的第 $n>1$ 位只依赖不超过
$\lceil n/4\rceil<n$ 的位；给定首位后所有位唯一。
这些固定字没有二进制端点歧义。

令 $\mathcal K$ 为十六进制数字只取 $7,8$ 的紧集。首个十六进制数字给
$$
\mathcal K\subset
[7/15,113/240]\ \cup\ [127/240,8/15].
\tag{7}
$$
对任意 $L$，$\{2^Lu_\pm\}$ 属于下列四种相位尾的并 $\mathcal T$：
$$
\mathcal K,\qquad
\frac{\{0,7\}+\mathcal K}{8},\qquad
\frac{\{0,3\}+\mathcal K}{4},\qquad
\frac{\{0,1\}+\mathcal K}{2}.
\tag{8}
$$
这是在一个 $0111$ 或 $1000$ 块中分别删去 $0,1,2,3$ 位的准确式。

因为 $u_-$ 以 $0111$ 开头，(7) 及八进位尾和给
$$
7/15\le u_-\le113/240,\qquad
73/4096\le f_8(u_-)\le1/56.
$$
因此
$$
q:=h_8(u_-)-3/7
\in[17/840,10511/430080],
\qquad h_8(u_+)-3/7=-q.
\tag{9}
$$

下面是需要保留的数值间隙，全部是有理比较：
$$
\boxed{\quad
\operatorname{dist}\bigl(t_\varepsilon\pm c q,\ \mathbb Z+\mathcal T\bigr)
\ge1/600,\qquad m\ge0,\quad\varepsilon=0,1.
\quad}
\tag{10}
$$
具体地，$m=0$ 时
$$
17/800\le c q\le10511/409600<1/20.
$$
靠近 $1/4,3/4$ 的 (8) 只能来自最后一种相位。
它分别落在距相应 quarter 至多 $1/60$ 的外带内；
故这时距离至少
$17/800-1/60=11/2400>1/600$。
其他三个相位的距离更大。

$m\ge1$ 时，$cq\le10511/819200$。
由 (7)，最后一种相位在每个 quarter 两侧留下半宽 $7/480$ 的开间隙。
所以距离至少
$$
7/480-10511/819200
=4307/2457600>1/600.
$$
其他相位仍不进入该间隙。所有目标都位于 $(1/5,4/5)$；
模整数取距离没有产生更近的端点。

## 3. 近零行必须跟随同一个固定字

这一节把无限固定字的间隙返回原有限行，不假设点态函数连续于所有二进制端点。

若某行满足
$$
|\ell_{L,k,\varepsilon}|<A8^L/1200,\qquad L\ge20,
\tag{11}
$$
由 (4)、$|h_8(u)-3/7|\le3/7$ 得
$$
|u-(7/15+f_{16}(u))|\le3\,2^{-L}.
\tag{12}
$$
取 $r=\lfloor L/4\rfloor-1$。
数 $v=7/15+f_{16}(u)$ 属于 $\mathcal K$，
所以它到任一 $16^{-r}$ 网格端点的距离至少
$(7/15)16^{-r}>3\,2^{-L}$。
由 (12)，$u,v$ 的前 $4r$ 个二进制位相同。
$v$ 的这些位又是对 $u$ 的前 $r$ 位应用 (6)，
故递归唯一性使 $u$ 的前 $4r\ge L-7$ 位
与同一个 $u_-$ 或 $u_+$ 完全一致。

记这个固定字为 $u_\sigma$。于是
$$
2^L|f_{16}(u)-f_{16}(u_\sigma)|
\le2^{-3L+28}/15,
$$
$$
|h_8(u)-h_8(u_\sigma)|
\le2^{-L+7}+8^{-L+7}/7.
\tag{13}
$$
把 (13) 代回 (4)，原左边与
$$
k-2^Lu_\sigma+t_\varepsilon
-c\bigl(h_8(u_\sigma)-3/7\bigr)
\tag{14}
$$
的差不超过
$$
4\,2^{-L}+2^{-3L+28}/15
+\frac{21}{20}\bigl(2^{-L+7}+8^{-L+7}/7\bigr)
\le140\,2^{-L}<1/1200
\tag{15}
$$
（$L\ge20$）。但由 (8)–(10)，(14) 的模至少 $1/600$；
这与 (11)、(15) 矛盾。

所以得到整块、全部来源行的显式统一结论：
$$
\boxed{\quad
|\log w_j-h_L|\ge \frac{16^m}{12}\,8^L
\quad(0\le j<2^{L+1},\ L\ge20).
\quad}
\tag{16}
$$
特别，从这一高度起中位没有相等权。前缀反转的对称性保证中位两侧各恰有 $N$ 行。

## 4. 全部分支的整块图范数与迹范数估计

令 $F_L^{\rm fin}$ 为有限 companion 空间中 $N$ 个最大物理平衡权行的正交投影。
它只依赖原物理权，不依赖根分支。

已刊[全部有限头根图](R12-appendix-all-finite-haar-head-root-graphs-half-weak-limit-and-strong-zero.md) §2
给任意根分支、任意 $N$ 行的真正 Fourier 逆费用
$$
C_N=N^{(N^2+3)/2}.
$$
按高低权行写图，有限图斜率的范数因此不超过
$$
C_N\exp\!\left[-2\frac{16^m}{12}8^L\right].
$$
对 $L\ge20$，$\log C_N\le L4^L\le(16^m/12)8^L$，
故任意 $S_L^2=C_L$ 的真实有限图投影满足
$$
\boxed{\quad
\|\Pi_{S_L}-F_L^{\rm fin}\|
\le\exp[-(16^m/12)8^L],\qquad
\|\Pi_{S_L}-F_L^{\rm fin}\|_1
\le2^{L+1}\exp[-(16^m/12)8^L].
\quad}
\tag{17}
$$
所有范数在完整 $2N$ 维 companion 空间取。
若将二者在其正交补上同时延零，(17) 不变；
不能把有限秩 $\Pi_{S_L}$ 与全空间柱乘法投影直接作算子范数比较。

负闭合 Walsh 块的同一结论也成立：
乘前文的对角相位把负闭合块转成正闭合块，根图相应的两坐标酉因子
与 $F_L^{\rm fin}$ 精确交换。因此 (16)–(17) 不改变，
没有仅核一个主平方根。

## 5. 同一个物理投影与全部直和闭根

沿用原 Walsh 正交块 $Q_{-1},Q_0,Q_1,\ldots$。
在每个 $Q_LH\oplus Q_LH$ 上取上节的中位行投影 $F_L$；
有限个初始块任取前缀反转配对下的一半行。
常数块取一维坐标投影。置
$$
F=F^{(0)}\oplus F^{(1)}
$$
为这些原物理行投影的正交和。这里 $F^{(i)}$ 是 $H$ 上的投影；
两分量均使用原 Walsh 块及实际列，不把它们认作某个单高位事件。

任意逐块根 $R_L^2=D_L$ 的最大直和闭根 $R$
满足已有稳定域关系
$
\operatorname{Dom}(R^2)=\operatorname{Dom}R,\qquad
R^2x=Dx\quad(x\in\operatorname{Dom}R).
$
这里不把这个限制算子与定义于全 $H$ 的有界 $D$ 等同为同域算子。统一采用 companion 的图顺序
$
\Gamma R=\{(Rx,x):x\in\operatorname{Dom}R\}\subset H\oplus H.
$
由 (17)，
$$
\boxed{\quad P_{\Gamma R}-F\in\mathcal S_1.\quad}
\tag{18}
$$
其尾迹范数由
$$
\sum_{L\ge M}2^{L+1}\exp[-(16^m/12)8^L]
\tag{19}
$$
控制，$M\ge20$，对全部分支一致。
所以任何两个分支选择的图投影差亦为迹类。

还存在真实酉算子 $W_R$，满足
$$
W_R-I\in\mathcal S_1,\qquad W_R F W_R^*=P_{\Gamma R}.
\tag{20}
$$
对 $L\ge20$ 取两投影的标准直接旋转，
其距恒等的范数不超过 $\sqrt2\|\Pi_{R_L}-F_L\|$；
(19) 支付迹范数和。有限个初始块因两投影秩相等可直接选酉。
这构造了 (20)，不由一般紧扰动差偷补指标零。

对精确吸收前 $L$ 位的 $D^{[L]}$，令 $F^{[L]}$
为已吸收有限正闭合头的中位投影加未吸收 Walsh 中位投影。
全部相应直和根统一满足
$$
\|P_{\Gamma R^{[L]}}-F^{[L]}\|_1\longrightarrow0.
\tag{21}
$$
有限头项和尾和都由 (17)、(19) 控制。
$F^{[L]}$ 随 $L$ 改变，原半弱极限及强图零没有被撤回。

## 6. 实际两坐标与完整原进位

令 $E=\operatorname{Ran}F$，以 (20) 的同一个酉算子定义
$$
J_0=\pi_2W_R|_E,\qquad J_1=\pi_1W_R|_E.
$$
因为 $W_R E=\Gamma R$，两者均为真正的单射、稠值有界映射
$E\to H$，并且
$$
\operatorname{Ran}J_0=\operatorname{Dom}R,\qquad
J_1=RJ_0,\qquad
J_0^*J_0+J_1^*J_1=I_E.
\tag{22}
$$
单射、稠值来自原最大直和闭根及其每个可逆有限块，
不是从任意两个紧扰动坐标推得。
同时
$$
J_0-\pi_2|_E\in\mathcal S_1,\qquad
J_1-\pi_1|_E\in\mathcal S_1.
\tag{23}
$$
原对角 companion $\mathcal B_D=\begin{pmatrix}0&D\\I&0\end{pmatrix}$
在同一个 $E$ 上诱导有界 $T_R=W_R^*\mathcal B_DW_R|_E$，准确满足
$$
J_0T_R=J_1,\qquad J_1T_R=DJ_0.
\tag{24}
$$
(22)–(24) 是原参考根的实际注入与范围来源。

对完整原 $C=D+K$，没有删掉 carry。其漏出这个图的完整块是
$$
\boxed{\quad
(I-F)W_R^*\mathcal B_C W_RF
=(I-F)W_R^*
\begin{pmatrix}0&K\\0&0\end{pmatrix}W_RF\in\mathcal S_1.
\quad}
\tag{25}
$$
右端仍是同一个原 $K$；本稿没有证明它为零，
也没有证明存在另一个注入、稠值的两坐标同时消去它。
因此 (22) 给的是 $D$ 的真实闭根，
不是 $C$ 或未知原旗商的闭根。
绝对迹范数小不支付旧临界低块的相对非线性费用。

本稿新增的是实际中位行的统一算术间隙、全部分支的整块/迹范数估计、
以及其真实两坐标极化。完整原不变格与场外二次分子仍按原完成标准继续。
