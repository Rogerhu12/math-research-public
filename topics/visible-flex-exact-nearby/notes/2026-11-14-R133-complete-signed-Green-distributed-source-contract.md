# 全部连续格的 signed Green 端口与径向源消费者

本篇规定新的独立公开消费者。它消费完整 5970 格、真实 weighted 两端、
原完整 7721 格 mean-corrected body 及全部原 trial 跳；不重算任何已成
矩阵格、物理帽或 mean 流。下面的算法须在公开 Actions 真正成功后，
才产生相应原问题的有限逆或数值源预算。一个端口门失败必须保存真实
失败与已得前缀，不能将未付条件改名为通过。

## 1. 一个真实片上的精确端口

每个完整 projector 证书给常数上界 mu、nu、c、e，其中 mu、nu 保留
正负号，c、e 非负。原范数不等式为

\[
 p'\le\mu p+cq+f,\qquad -q'\le\nu q+ep+g.
 \tag{G.1}
\]

先对等式系统计算端口，再应用已证
[signed Riccati 正 Green](../results/R133-supplement-signed-Riccati-positive-Green-with-full-interface-sources.md)
的正逆/slack 比较；不直接对未知不等式中的 q-varrho p 求导。

片长为 h，右端已得非负 cone 门为 qR≤varrhoR pR+zR。令

\[
 A=\begin{pmatrix}\mu&c\\-e&-\nu\end{pmatrix},\quad
 T=\exp(hA),\quad K=\int_0^h\exp(tA)\,dt,
 \quad d=T_{22}-\varrho_R T_{12}.
 \tag{G.2}
\]

Arb 通过准确 4×4 block exponential 同时包裹 T、K，不使用除以 A 的
公式，因此允许 A 奇异。若 f、g 是该片真实源的非负常数上界，精确
等式消元给

\[
\begin{aligned}
 \varrho_L&=(\varrho_RT_{11}-T_{21})/d,\\
 z_L&=z_R/d+
   [(\varrho_RK_{11}-K_{21})f+(K_{22}-\varrho_RK_{12})g]/d,\\
 p_R&=\det(T)p_L/d+T_{12}z_R/d\\
 &\quad+[(T_{22}K_{11}-T_{12}K_{21})f
            +(T_{12}K_{22}-T_{22}K_{12})g]/d.
\end{aligned}\tag{G.3}
\]

其中 det(T)=exp((mu-nu)h) 准确为正。全部四个源系数都有真实方向，
特别 q 方程的源是 -g，不能在矩阵积分中把它改为 +g。

## 2. 整片无 pole、正性与向上舍入

必须控制每个 suffix 长度 tau∈[0,h]，而非只检查 d(h)。取

\[
 M=\max(|\mu|+c,e+|\nu|),\qquad
 \epsilon=\exp(hM)-1.
\]

完整有向充分门

\[
 1-\epsilon(1+\varrho_R)>0\tag{G.4}
\]

保证 d(tau)>0：无穷矩阵范数给
`||exp(tau A)-I||inf<=epsilon`，从而相应第22项减 varrhoR 倍第12项
不小于 (G.4)。绝对值只用于这个无 pole 充分门；实际 T、K 和所有传播
始终使用 signed mu、nu。若这个充分门太粗，只细分这一段常数比较
系统，原完整矩阵证书和 projector 不重算，新增内点的 projector 连续。

在没有 pole 时，逆向 Riccati 的非负半轴因 e≥0 保持不变。于是局部
正 Green 定理适用，(G.3) 所有传播和源系数非负。程序可将它们的有向
上端点与0取 max；这是已经证明非负之后的上包络，不能反过来借此
“证明”一个失败的无 pole 门。

每次返回的 varrhoL、zL 和 pR 系数独立向上舍入。它们是严格的局部
正端口不等式，不能冒称一个共同准确的全局 Riccati 等式。向后归纳
使用当前已经成立的右 cone 上界；此外

\[
 \frac{\partial\varrho_L}{\partial\varrho_R}
   =\det(T)/d^2>0
\]

给 slope 的正确单调性。slope 舍入是“非负系数乘未知 p”的 cone
余量，不是独立已知源。这样可用真实衰减逐片反推，不取两个全区间
supremum 的粗乘积。

## 3. 全部 projector 跳和物理 trial 跳

所有 5970 个原 polynomial→saved-anchor 跳均消费，包括腰处最后
的零长接口。对 delta=||Pplus-Pminus||<1，取

\[
 s=(1-\delta^2)^{-1/2},\qquad t=\delta s.
\]

完整接口满足 pplus≤s pminus+t qplus+a、qminus≤t pminus+s qplus+b。
若真实状态还有 yplus-yminus=j，直接两侧正交投影给合法统一门

\[
 a=b=s\|j\|.\tag{G.5}
\]

例如第二式来自
`sqrt(1-delta²) qminus <= qplus + delta pminus + ||Qplus j||`。
这保留了两个独立源，不能只付其中一个。

令 d=1-t varrhoplus。程序实际使用一般四系数公式

\[
\begin{aligned}
 \varrho_-&=t+s^2\varrho_+/d,\\
 z_-&=s z_+/d+s\varrho_+ a/d+b,\\
 p_+&=s p_-/d+t z_+/d+a/d.
\end{aligned}\tag{G.6}
\]

因为 s、t 已独立向上舍入，不能再假设它们准确满足 s²=1+t² 来免费
化简。每个分母均须有严格正下界。若原 trial 某一跳恰为零，也仍保留
原接口记录；纯 frame 腰跳的物理源 j=0，但角费用不消失。

## 4. 闭合、完整有限逆和源的四个通道

两端使用已经实际成功的完整 weighted boundary native
`56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25`。
原保存腰 frame 位于虚拟 0−，故反向归纳先消费腰跳，再检查

\[
 m_0=1-D_0\varrho(0^-)>0,\qquad
 p(0^-)\le[D_0z(0^-)+b_0]/m_0.\tag{G.7}
\]

然后逐片、逐接口正向应用已经得到的正端口。所有齐次源为零时，
p=q=0，因此实际 193 状态压缩 ODE 和真实 low97 cut 边界没有齐次核。
这是真实连续有限 ODE：其完整 193 个初值与 96+97 个边界行组成同阶
有限线性映射，单射即满射，故给该明确有限边值问题的存在唯一性。
这一步没有证明未知无限高输入的反馈可逆。

实际消费者保持四个互相独立的源通道：原已付 body 残差、原 trial
跳、左边界数据单位范数、右边界数据单位范数。左右后两列分别以
b0=L0、bL=LR 起始；没有把独立边界源设成已经为零。

原完整 mean-corrected body 证书有全部 7721 个真实片的 ordinary L2_phi
sup 及 6143 个 nonmean trial 跳。新消费者把它们与全部 projector/weight
区间取准确公共细分。设原物理源 sup 为 E，权重为
R=diag(I96,rho I97)，则 f、g 均可取该公共片上的 max(1,rho)E。
同样，完整 trial 跳费乘 max(1,rho) 后进入 (G.5)。完成的 mean 跳
准确为零；所有未知状态的 even mean 仍在 193 维 Gram 中保留。

## 5. 整片范数和相位所需的准确窗口

常数比较片上，准确 Riccati 解在无 pole 时单调或为常数，因此
varrho_whole≤max(varrhoR,varrhoL_upper)。按
`Z'=-(nu+c varrho)Z-g-varrho f` 反向使用保 signed rate 的标量指数，
再按 `P'=(mu+c varrho)P+cZ+f` 正向积分，给每片完整 P、Q 上界。
真实正交分解保留 `||y||²=p²+q²`，而 ordinary 物理范数逐片支付
max(1,1/rho)。将这些完整平方上界乘准确长度后相加，得到有向 L2 费用。

完整有限 BVP 仍在 `[0,9/10]` 求解，右 cut 仍来自完整正帽。输出同时
保存这一全内段范数与当前相位需要的

\[
 [0,2383968743003/10000000000000]
\]

ordinary pair L2。后一区间由原根 native
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`
实际核对，包含当前完整负区及最后极短的跨根段。圈测度归一化，独立
even mean 保留，不引入 q^(-1) 根权。该固定上端只属于当前 eta0、原
nu 和当前背景；delta 族、nu 调整或真正 nonlinear 背景的根变化另付。

原 body 残差属于 ac1 算子。若 Atilde、Ftilde 是修补背景，则真实误差
方程另有 `(Atilde-A) q_star+(Ftilde_nu-F_nu)`，并有未知 high 输入、
外帽源和全部真实边界负荷。本消费者只把原残差当成一个明确源分量
经新有限 Green 传播，绝不将它称为全部 `q_nu-q_star`。原 full160 输出
范数支配其有限投影；对应高频响应仍须另外证明。

## 6. 公开执行与成功记录复用

新 workflow 第一次 push 先运行七个独立 signed-port 代数门并推送
实际 native/过程。在全5970 workflow 真正成功后，`workflow_run`
自动消费其实际 artifact、原完整 body/mean artifact 和准确根证书。
已经成功的代数门按同 source/core/manifest SHA 及原真实退出码复用，
不再执行。所有新数值只在本公开仓库 Actions 中产生。

若后续全局门失败，仍保留已经完成的真实 backward ports 和准确失败
位置；不能因此宣布原问题无解，也不能删去 mean、源或 jump 来换取通过。
