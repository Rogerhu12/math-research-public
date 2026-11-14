# R98：真实外头的三档材料核与低—中—高联立条件

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

**已证明的条件工具。** 本文把原 R74 域的同一真实两胞元、R96 的低46中心和 R93 的无限高响应放在一个固定 Banach 问题中。低中频采用原 local-$V$ 范数，高频保留实际 balanced 范数；不以 $V_{\min}$ 把高球强行改成 local-$V$ 球。完整 mean 与商的导数、有限输出角权、变条带到常条带的费用都显式保留。

实际新算术只支付 §5 的十个标量域门，V8 BigInt 约8毫秒。三档实际有限核与最终 Schur 门仍是明确输入，尚无新的 m94/96 Arb/ODE 运行。本文没有将这个条件工具称作外头全频方程已经完成。

## 1. 固定真实背景、参数与三个空间

背景固定为 R26/R87 的 node12 至 node10、胞元11和10。沿原 source 坐标 $x$ 记
$$
 s=r_x/r>0,\qquad \ell=w_x/w,\qquad
 \mathfrak c=s+|\ell|,\qquad E=1+w^2\le5/4.
 \tag{98.1}
$$
所有源是 source-$x$ 单位，不再次乘 $r_x$。令
$$P=h_\theta/(rw),\qquad K=h_{\perp,r}/w.$$
$K$ 是非均值场，完整均值小根记为 $c$。

原10793叶上的固定正 dyadic 包络仍为 $V(x)=V_I$，并有
$$0<V\le V_0=2^{-40}.$$
常宽 $\tau_*=18/125$。真实变宽 $\tau(x)$ 恰为 R93(93.16) 的同一函数，含全部 frame 接口跳变，且
$$
 \frac1{64}<\tau(x)\le\tau_*.
 \tag{98.2}
$$
低块为正负偶模 $2\le|m|\le92$；完整中块为 $94\le|m|\le5758$；高块为 $|m|\ge5760$。奇模的零子空间由乘积与原方程保持。

令 $C=C_L(a)$ 为 R91 已存在的低46投影解，参数 $a$ 限原实 R74 族及共同相位。R96 对这个同一个中心证明
$$
 \|C\|_{X_V}\le C_0:=10,\qquad
 \|Z\|_{X_V}=
 \sum_{m\ne0}(1+|m|)e^{\tau_*|m|}
 \left(\sup_x\frac{|P_m|}{V}
       +\sup_x\frac{|K_m|}{V}\right).
 \tag{98.3}
$$
它不是给任意高场除以 $V_0$ 得出的界。

低校正记为 $u$，中校正为 $v$，二者用对应频率限制的 $X_V$。高场 $H$ 用 R93 的固定空间
$$
 \|H\|_{X_H}=
 \sum_{|m|\ge5760}(1+|m|)
 \sup_x e^{\tau(x)|m|}
       |(P_m,K_m/b_i)|_2.
 \tag{98.4}
$$
接口两侧均计入 supremum，物理场仍连续。真实 frame 范围给
$$
 \|H\|_{\mathrm{ph},\tau}<B\|H\|_{X_H},
 \qquad B=18555.
 \tag{98.5}
$$
这里 $B$ 支付两物理分量分别取sup的完整代价，不能改成未经证明的点态欧氏因子。

## 2. 完整非线性及径向量词

令 $T=P_\theta$。完整 source 保持
$$
 N=\Pi_\perp\frac{Q+B_c}{1+l},\qquad l=c+K+ET,
$$
$$
 Q=Es(K_\theta-P)^2+
 \ell\{E(K+T)^2-w^2(K^2+P^2)\},
 \qquad B_c=\ell\{2c(K+ET)+c^2\}.
 \tag{98.6}
$$
减号、全部 mean 项及无限逆分母不删。R89/R91 已付同一个完整小根的
$$|c|\le4R^2,\qquad |Dc[\delta Z]|\le16R\,\delta R$$
于强域 $R\le1/64$。

为完整列明商的常数，由非均值最小频率2，
$$
 \|P\|_0+\|K\|_0\le R/3,\quad
 \|K_\theta-P\|_0,\|K+T\|_0\le R,\quad
 \|K+ET\|_0\le5R/4.
$$
因此
$$
 \|Q\|_0\le\tfrac{23}{18}\mathfrak c R^2,\qquad
 \|B_c\|_0\le\mathfrak c(10R^3+16R^4),\qquad
 \|l\|_0\le5R/4+4R^2.
$$
其完整导数分别由
$$
 \|DQ[\delta Z]\|_0\le\tfrac{23}{9}\mathfrak c R\delta R,\quad
 \|DB_c[\delta Z]\|_0\le
 \mathfrak c(50R^2+128R^3)\delta R,\quad
 \|Dl[\delta Z]\|_0\le(5/4+16R)\delta R
$$
控制。商法则给正系数函数，在 $R=1/64$ 的两个严格有理门为
$$
 \frac{13252}{9027}<\frac32,\qquad
 \frac{31451168}{9054081}<4.
$$
遂在整个域内
$$
 \|N(Z)\|_{\tau,0}\le\tfrac32\mathfrak c R^2,\qquad
 \|DN(Z)[\delta Z]\|_{\tau,0}
       \le4\mathfrak c R\delta R.
 \tag{98.7}
$$

这里每个径向 Fourier 质量先固定再作正卷积。变条带满足
$e^{\tau(x)|j+k|}\le e^{\tau(x)|j|}e^{\tau(x)|k|}$，正标量 $V(x)$、$\mathfrak c(x)$ 不依赖角度。把每个因子先取相应的逐模径向sup，以上证明给真正的 sum-of-sup 算子界；未把点态和的上界直接搬到较强空间。

特别地，若 $\|u\|_{X_V}\le r_L$、$\|v\|_{X_V}\le r_M$、
$\|H\|_{X_H}\le r_H$，置
$$
 t=r_L+r_M,\qquad h=B r_H.
$$
沿两段连线先加 $X=u+v$、再加 $H$，(98.7) 的完整积分给
$$
 N(C+X)-N(C):
 \quad (4C_0t+2t^2)\mathfrak c V^2,
$$
$$
 N(C+X+H)-N(C+X):
 \quad 4(C_0+t)h\,\mathfrak c V+2h^2\mathfrak c .
 \tag{98.8}
$$
第一行在常宽 $\tau_*$，第二行在实际 $\tau(x)$。
这些“密度系数”指固定模态质量总和的充分界，保留完整 mean/商。它们不是仅二次主部的近似。

后文对低中方向求导时，还必须控制完整导数随高场的改变，不能直接微分一个仅已知的上界。R33 §2(33.11)–(33.14) 已在非均值复 Wiener 输入 $R\le1/32$ 的整个球上证明相同完整小根全纯且 $|c|\le4R^2$。上面的绝对代数也在复 $R\le1/64$ 球成立。

对任何物理强范数不超过 $2^{-34}<1/256$ 的基点 $Y$，以及两个单位方向 $U,W$，函数
$N(Y+zU+\zeta W)/\mathfrak c$ 在
$|z|,|\zeta|<1/256$ 上全纯，整个输入半径至多 $3/256<1/64$。双变量 Cauchy 因而给
$
 \|D^2N(Y)[U,W]\|_{\tau,0}
 \le \frac32(3/256)^2(256)^2\mathfrak c
 =\frac{27}{2}\mathfrak c<16\mathfrak c.
 \tag{98.8a}
$
混合系数就是 $D^2N[U,W]$，没有额外因子2。此证明在相同固定径向质量的 Banach 空间成立。特别地，$N$ 径向逐点作用，故一个方向中的标量 $V(x)$ 可准确提出 $D^2N$，不会付 $V_{\min}^{-1}$。

于是沿完整连线
$
 \|[DN(C+X+H)-DN(C+X)][\delta X]\|_{\tau,0}
 \le16\mathfrak c\,hV\,\|\delta X\|_{X_V}.
 \tag{98.8b}
$
这项在变条带；$DN(C+X)$ 本身仍在常宽。下面严格用16控制这一交叉导数，而不以(98.8)的形式微分暗取4。

## 3. 三档位置核及真实条带转换

定义
$$
 d_p(x)=\mathfrak c(x)V(x)^p,\qquad p=2,1,0.
 \tag{98.9}
$$
三个档分别支付 local-field×local-field、local-field×physical-field 和 physical-field×physical-field。每档还分开保存
$sV^p$、$|\ell|V^p$ 两种真实材料。

对有限输出块 $B_f=L$ 或 $M$，记背景源逆为 $\mathcal G_{B_f}$。低逆是 R90 的完整两端 Wronskian Green；中逆是带两个真实初迹的 Volterra 算子去掉其初迹 lift 后的源部分。设其物理分量核为 $G_{m,i}(x,y)$。必须按真实 Green 的方向和源支撑积分，不把晚源搬到早目标。

对常宽源定义逐模行
$$
 \gamma_{m,p}=(1+|m|)\sum_{i=1}^2\sup_x
 \int \frac{|G_{m,i}(x,y)|\,d_p(y)}{V(x)}\,dy.
 \tag{98.10}
$$
对变宽源到常宽输出，真正需要
$$
 \gamma_{m,p}^{\Delta}=(1+|m|)\sum_{i=1}^2\sup_x
 \int \frac{|G_{m,i}(x,y)|\,d_p(y)}{V(x)}
       e^{|m|(\tau_*-\tau(y))}\,dy.
 \tag{98.11}
$$
输出角权已在两式中，不能再重复乘一次。没有把变宽高球原样置入常宽低中空间。

若初步仅有常宽核，R93 的精确总费用 $\Delta_*<0.128327283$ 给合法的保守接法
$$\gamma_{m,p}^{\Delta}\le e^{|m|\Delta_*}\gamma_{m,p}.\tag{98.12}$$
实际消费须用原完整有理 $\Delta_*$ 和向上的指数包围；显示小数不参与门。此界可能很粗，未称它在全部中频已经足够。

置
$$
 \Gamma_{B_f,2}=\sup_{m\in B_f}\gamma_{m,2},\qquad
 \Gamma_{B_f,p}^\Delta=\sup_{m\in B_f}\gamma_{m,p}^\Delta
 \quad(p=1,0).
 \tag{98.13}
$$
固定 source 质量先求和的量词证明相应算子范数由这些sup控制。与此不同，R96 保存的是独立逐模纯中心源帽 $b_m$；其实际中响应应付
$$
 R_M=\sum_{m=94,96,\ldots,5758}\gamma_{m,2}b_m,
 \tag{98.14}
$$
不得无故换成一个max。$b_m$ 已是正负成对质量，(98.14) 不另乘2。

### 实际中流的同源实现

置 $F=\sqrt{rw^3}$，$Y_m=F(P_{\sin,m},K_{\cos,m})^T$。固定的真矩阵为
$$
 Y_{m,x}=
 \begin{pmatrix}(\ell-s)/2&-ms\\-m\ell&-(\ell-s)/2\end{pmatrix}Y_m
       +e_2 F N_m.
 \tag{98.15}
$$
其迹为0，真实行列式准确为1。每个原source段的局部基本矩阵 $A(a)=I$，于是
$$
 A(y)^{-1}e_2=(-A_{01}(y),A_{00}(y))^T.
$$
对任意一档正材料 $d_{p,\alpha}$，累计
$$
 I_0(x)=\int_a^x|A_{00}(y)|F(y)d_{p,\alpha}(y)\,dy,\quad
 I_1(x)=\int_a^x|A_{01}(y)|F(y)d_{p,\alpha}(y)\,dy.
$$
段内完整响应由
$$
 |A_{i0}(x)|I_1(x)+|A_{i1}(x)|I_0(x)
 \tag{98.16}
$$
及 $|A(x)|$ 乘上一段的源端盒控制。实际计算在子片中先把该片完整正积分计入，再取全部目标位置的矩阵盒；这是保守多付，且包含所有有序位置。18个原段的真 signed 端矩阵推进既有不确定性，原两条全局初迹列全程不重置。没有发明 $m>92$ 的头斜率或零高 Dirichlet 条件。

独立新入口只把同一 $A,F,V$ 中的正材料从两列扩成六列；真 Taylor/root transitions、精度、原真实 source、所有余项与旧 $V^2$ 列均保留。它不靠新增 ODE 支付不同背景。低 Green 的对应两档也可从已付原有序几何重新按源位置加权，而非除以全局 $V_{\min}$。

## 4. 真实头、中心消去及联立映射

固定同一真实参数 $a$。低中心 $C$ 已解其完整低投影问题，故低校正的纯中心残差准确为0。低边界仍为原线性关系加规定真实 $\beta(a)$；固定 $a$ 时校正用齐次边界。中高则保留真实头给出的两个初迹，分别记 $M_{\rm bd}(a)$、$H_{\rm bd}(a)$。

联立式为
$$
 u=\mathcal G_L P_L\{N(C+u+v+H)-N(C)\},
$$
$$
 v=M_{\rm bd}(a)+\mathcal G_M P_M N(C+u+v+H),
$$
$$
 H=H_{\rm bd}(a)+\mathcal G_H P_H N(C+u+v+H).
 \tag{98.17}
$$
这保留真实非零高浅迹。参数 $a$ 的 head 与当前外解切口是否一致仍是另外的切口方程；没有由 (98.17) 擅自删去它们。

令 $\mathsf B_M\ge\|M_{\rm bd}(a)\|_{X_V}$ 为实际两初迹传播界。由 (98.8)–(98.14)，有限输出 $i=L,M$ 的共同变化帽为
$$
 \mathcal A_i(t,h)=
 (4C_0t+2t^2)\Gamma_{i,2}
 +4(C_0+t)h\Gamma_{i,1}^\Delta
 +2h^2\Gamma_{i,0}^\Delta.
 \tag{98.18}
$$
故前两自映行分别是
$$
 \mathcal A_L(t,h)<r_L,\qquad
 \mathsf B_M+R_M+\mathcal A_M(t,h)<r_M.
 \tag{98.19}
$$
全部 $r,\Gamma$ 必须来自同一对象、同一 $V$、同一 source-$x$ 单位和正确频率范围。有限或失败的核包不替代完整中范围。

## 5. 已实际支付的混合域与高行

R93 证明
$$
 G_H=\frac{11798528}{45},\qquad
 q_H=G_H\,4\cdot257\cdot2^{-34}
     =\frac{1480577}{94371840}<\frac1{60}.
 \tag{98.20}
$$
对给定有限物理变化，除以 $b_i$ 的费用至多256，故用相同 $q_H$ 保守控制；低中 local-$V$ 单位方向转物理只需 $V_0$。高→高方向用的是已付的257，不把18555重复塞入该高行。

保持原实际高半径，取
$$
 t=r_L+r_M\le1/8,\qquad
 r_H=2^{-149}+2^{-43}/50.
 \tag{98.21}
$$
则 $V_0t\le2^{-43}$，正好进入 R93 原已付中频物理域，而非宣称高球处于 local-$V$ 半径1。新精确标量账本逐项证明
$$
 10V_0+2^{-43}+18555r_H
 <5.139781934\times10^{-11}<2^{-34}<1/64,
 \tag{98.22}
$$
以及完整 leading 商小于1。

纯低中心高源仍可使用 R93 的完整 Neumann 尾 $2^{-2053}$，真实高初迹仍小于 $2^{-152}$。所以高自映行由
$$
 2^{-152}+2^{-2053}+q_H(V_0t+r_H)<r_H
 \tag{98.23}
$$
支付。在最坏 $t=1/8$ 上，实际向上显示 image
$<1.819277440\times10^{-15}$。这个新十门 BigInt 账本只核 (98.20)–(98.23)，未检查任何尚无实际输入的有限 $\Gamma$。

## 6. 完整三行导数与可执行 Schur 条件

在以上全域内，写
$$
 a_i=4(C_0+t)\Gamma_{i,2}
                  +16h\Gamma_{i,1}^\Delta,
$$
$$
 b_i=4B\{(C_0+t)\Gamma_{i,1}^\Delta
                         +h\Gamma_{i,0}^\Delta\},
 \qquad i=L,M.
 \tag{98.24}
$$
完整固定点导数由正矩阵
$$
 J=
 \begin{pmatrix}
 a_L&a_L&b_L\\
 a_M&a_M&b_M\\
 q_HV_0&q_HV_0&q_H
 \end{pmatrix}
 \tag{98.25}
$$
逐行控制。每个 $b_i$ 中的 $B$ 是从 balanced 高距离转到物理方向的明确一次费用；完整 mean/逆包含在各个常数中。$a_i$ 的高交叉项以 (98.8b) 的16及 (98.11)支付；$b_i$ 直接由完整一阶导数的4支付。两者都没有免费升宽。

可以直接给正权 $W_L,W_M,W_H$ 与 $q<1$ 并核 $JW\le qW$。也可只核二维正比较
$$
 A=a_L+a_M,\quad B'=b_L+b_M,\quad
 C'=q_HV_0,\quad D=q_H.
$$
若
$$
 A<1,\quad D<1,\quad
 (1-A)(1-D)>B'C',
 \tag{98.26}
$$
则有严格正的三行权。

**证明。** 若 $B'>0$，取
$$
 \frac{C'}{1-D}<W_H<\frac{1-A}{B'},\qquad W_T=1.
$$
区间非空恰由 (98.26)。置
$$
 \epsilon=1-A-B'W_H>0,
$$
$$
 W_L=a_L+b_LW_H+\epsilon/2,\qquad
 W_M=a_M+b_MW_H+\epsilon/2.
$$
则 $W_L+W_M=1$，前两行的 $JW$ 各严格小于相应权，第三行由所取下界严格小于 $W_H$。若 $B'=0$，任取 $W_H>C'/(1-D)$ 并用同样的 $\epsilon=1-A$。取三个严格行比的最大值就是某个 $q<1$。证毕。

这不是把原三个数学门换成谱诊断；它精确构造原三行的距离权，也不需要浮点逆矩阵。

**条件定理98.1。** 若完整实际有限核支付 (98.10)–(98.13)、全部真实初迹与 R96 纯源行支付 $\mathsf B_M,R_M$，并存在正半径满足 (98.19)、(98.21) 和 (98.26)，则 (98.17) 在该乘积闭球中有唯一解，完整 mean/leading 域保持，且对同一 R74 参数族连续依赖。若中块实际覆盖所有94至5758，则全部非均值偶频方程同时满足；结合相同完整 mean 根与第一行兼容性，R44/R75 给该两胞元内的完整 Darboux 方程。

**证明。** (98.19)、(98.23) 给自映；(98.22) 给所有连接线段的完整非线性域；(98.24)–(98.26) 给同一固定空间中的严格收缩。Banach 不动点定理完成。每个源逆来自同一真实方程，物理跨段连接和相应下窄条带的径向正则性由 Duhamel/Green 式传递。参数连续性来自统一严格收缩与原真实 trace 的连续性。完整 mean 方程使用同一根，不能另外独立指定其径向高度积分常数。证毕。

该定理仍未付所有切口、外0至9、嵌入性、reach或闭面大幅度。若只计算 m94/96，结论仅适用于其余中频被给定的相应投影问题，不是完整中块已付。

## 7. 源码、实际门与剩余数值

- 原入口 $\mathtt{closure\_outer\_middle\_volterra\_recovered\_v1.py}$ 保持冻结。
- 新准备入口 $\mathtt{closure\_outer\_middle\_mixed\_density\_v2.py}$ 增加 $V^1,V^0$ 两档、共四个材料列。它保留原 $V^2$ 两列与原八项 enclosure 守卫；新增线性核不自动支付 (98.11)、完整 mixed-domain 或 (98.19)/(98.26)。
- 原 argv、真实 ready、R87 anchors、全部 source groups、R78 两初迹与 R91 身份不变，输出使用全新前缀。观察 RSS 门仍为98304 KiB，不声称它是OS限制。
- $\mathtt{closure\_outer\_mixed\_density\_domain\_ledger.js}$ 已实际 V8 BigInt 执行十门，全真；没有 Arb、ODE 或新的源求值。
- 当前 Python 新入口只作唯一文字锚点变换与公式核对；执行器不可用，未声称 Python AST 通过或新数值运行。

因此下一实际义务十分具体：先跑 m94/96 真有序核，再以其 $V^2$ 行消费 R96 的完整纯源；用新增 $V^1,V^0$ 行及实际条带费用支付高反作用；逐步补全中范围，最后核原三行自映与 Schur。不允许只因纯中心源极小就宣称这些未知场反馈已经完成。
