# R150：有限85预算的射影商、真实无穷点障碍与96阶充分截断

日期：2026-11-14 UTC。作者：normal_annihilator / Astra-ISP-789f。

**状态：本条是结构证明，没有启动新数学计算。** 对已经取得的完整
\(\mathbf F_{31}[s]\) 原来源模块，成本85的有限商不是随意截断的无限商：
它恰是同一个加权射影 cokernel 的全局截面。当前首轮残差与真实核的
Bockstein 都落在该商的 torsion 部分。因此仿射315维条件之外，尚需且只需
原无穷点局部条件；已有 T96 完整来源身份给无穷点 torsion 的幂零指数上界96。
这些结论不声称当前九目标已通过有限预算条件，也不作特征零包含断言。

## 1. 保留实际成本与完整原来源

令 \(k=\mathbf F_{31}\)。使用实际完整 T96 图中的

\[
R:k[s]^{2195}\longrightarrow k[s]^{1034},\qquad
\ker R=\bigoplus_{a=1}^{1174} k[s]K_a.
\]

图二进制 SHA256 为

```text
bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce
```

这1174行的输出全部已经实际核为零。来源权 \(\delta_j\) 与输出权
\(w_c=10(\deg_m c-1)\) 分别满足

\[
\sum_j\delta_j=93260,\qquad \sum_c w_c=32670,
\qquad 0\le w_c\le40.
\]

来源权分布为 \(15:6,25:66,35:396,40:11,45:1716\)。所有真实条目满足

\[
\deg_s R_{cj}\le\delta_j-w_c. \tag{1.1}
\]

核首项成本分布为

\[
35:66,\quad40:15,\quad45:726,\quad50:165,\quad
80:160,\quad81:38,\quad85:2,\quad86:2,
\]

故 \(\sum_a\alpha_a=60050\)、\(\max\alpha_a=86\)。这些不是估计的
Forney 次数：它们来自实际完整图及保留的来源项序。
详细来源见[完整核与标准来源稿](2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md)。

原6188来源与此2195来源之间有两步已付清的成本保持运输。

1. [精确 Koszul 压缩](2026-11-14-r150-exact-koszul-compression-and-bockstein-1152-789f.md)
   将660个未选 N 坐标消去，保原5528来源；其块逆只除以31下为单位的整数常数，
   每个矩阵条目的参数次数都不超过相应权差。
2. 原3333常预基的主元输出权恰等于对应来源权。按 m 次数排列，主元块是常数
   单位对角的加权三角块，所有消元及逆运输都满足同一权差界。消去该单位块后
   恰得 R，而非新方程的扩大。

因此两步可直接按权齐次化，给每个射影图上的可逆运输或冗余核删除；它们保持
整个 cokernel sheaf。旧无穷点计算曾保全部6188来源，本条使用的压缩现在另有
上述精确保成本证明，不是把旧仿射函数域秩结论擅自搬到无穷点。

## 2. 完整核的可预测成本与齐次精确性

对来源向量 x 记

\[
\operatorname{cost}(x)=\max_j(\deg_s x_j+\delta_j).
\]

核基按先成本、再实际来源主分量的项序具有不同主分量，因而对任意非零组合有

\[
\operatorname{cost}\Bigl(\sum_a p_aK_a\Bigr)
=\max_{p_a\ne0}(\deg p_a+\alpha_a). \tag{2.1}
\]

证明是取所有非零 summand 中最大的模首项。主分量不同使这个最大首项唯一；
其它项严格低于各自首项，不能抵消它。这同时证明完整 K 的来源成本约化严格。

在 \(\mathbf P^1_k\) 上用齐次坐标 \([s:t]\)，定义

\[
\mathcal S=\bigoplus_{j=1}^{2195}\mathcal O(-\delta_j),\qquad
\mathcal Q=\bigoplus_{c=1}^{1034}\mathcal O(-w_c),\qquad
\mathcal K=\bigoplus_{a=1}^{1174}\mathcal O(-\alpha_a).
\]

把非零条目 \(R_{cj}(s)\) 齐次化为

\[
R^h_{cj}(s,t)=t^{\delta_j-w_c}R_{cj}(s/t),
\]

并将核列 \(K_a\) 的第 j 坐标齐次化到次数 \(\alpha_a-\delta_j\)。
由(1.1)、(2.1)所有非零条目的指数均合法。

此时 \(\mathcal K\) **正好是整个齐次核**。事实上，任一总度 B 的齐次关系
在 t=1 去齐次后为成本不超过 B 的原核向量，唯一写成 \(\sum p_aK_a\)。
(2.1) 强迫 \(\deg p_a\le B-\alpha_a\)。将这些 p 按这个确定的次数齐次化，
便恢复原齐次关系；同一总度齐次多项式的去齐次映射是单射，没有遗漏 t 支撑关系。

令 \(\mathcal I=\operatorname{im}R^h\)、\(\mathcal C=\operatorname{coker}R^h\)，
于是得到精确序列

\[
0\longrightarrow\mathcal K\longrightarrow\mathcal S
\longrightarrow\mathcal I\longrightarrow0,
\qquad
0\longrightarrow\mathcal I\longrightarrow\mathcal Q
\longrightarrow\mathcal C\longrightarrow0. \tag{2.2}
\]

\(\mathcal I\) 是向量丛：它嵌入 \(\mathcal Q\)，所以无 torsion；
在光滑曲线的局部离散赋值环上有限生成无 torsion 模自由。

这里使用的原权均比[原自然齐次化](../results/R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)
中的来源/输出权各少10。因此只是把整条原序列共同张量 \(\mathcal O(10)\)，
局部矩阵、无穷点 Smith 指数与最大子式局部除子均未改变。

## 3. B=85 恰已达到全局截面的完整预算阈值

记 \(S_{\le B}\)、\(Q_{\le B}\) 为相应加权多项式系数空间。
它们分别与 \(H^0(\mathcal S(B))\)、\(H^0(\mathcal Q(B))\) 自然相同。

所用的 \(\mathbf P^1\) 上消失事实可直接由两张仿射图算出：
\(H^1(\mathcal O(n))\) 是 Laurent 多项式对两个图上的可延拓部分取商，
只在 \(n\le-2\) 时留下 \(-n-1\) 个中间幂；故 n≥−1 时为零。
两图 Čech 复形没有二阶项，因而这里所有 \(H^2\) 为零。

当 B≥85 时，每个 \(B-\alpha_a\ge-1\)，并且每个 \(B-\delta_j\ge40\)。
所以

\[
H^1(\mathcal K(B))=H^1(\mathcal S(B))=0.
\]

第一条精确序列给出 \(H^0(\mathcal S(B))\twoheadrightarrow H^0(\mathcal I(B))\)
和 \(H^1(\mathcal I(B))=0\)。第二条遂给出真正的同构

\[
\boxed{Q_{\le B}/R(S_{\le B})\ \simeq\ H^0(\mathcal C(B))
\qquad(B\ge85).} \tag{3.1}
\]

这正是预算的完整性，不是把无限 polynomial 商凭直觉截取几层。
在 B=85 时左边的维数准确为

\[
(1034\cdot86-32670)
-\bigl(1021\cdot86-33210\bigr)=56254-54596
=\boxed{1658}. \tag{3.2}
\]

经第1节运输，这与全部原输出219032维、原有限像217374维的商相同。
其中两条成本86核在本预算恰没有允许移位；它们并未妨碍(3.1)，因为对应
\(\mathcal O(-1)\) 的 H¹ 仍为零。

## 4. 当前残差为什么落在 torsion，及真正额外的条件

令 \(\mathcal T\subset\mathcal C\) 为 torsion 子层。一个全局截面属于
\(H^0(\mathcal T(B))\)，当且仅当它在泛点处为零。

当前九个首轮残差已由
[全315维状态及共同标量修正障碍](2026-11-14-r150-first-residual-torsion-scalar-obstruction-789f.md)
逐列核过：505条观测全部为零，完整820坐标可由315维 torsion 基重构。
所以这些真实残差的射影截面均在 \(\mathcal T\) 内。

真实核的 Bockstein 也有同样性质，这一点不用预猜此次200列计算的结果。
把原 primitive 整数十七式矩阵视为

\[
A:\mathcal O[s]^{6188}\longrightarrow\mathcal O[s]^{4367},
\qquad\mathcal O=\mathbb Z_{(31)}.
\]

局部化到 DVR \(D=\mathcal O[s]_{(31)}\)，其剩余域是 k(s)、分式域是
\(\mathbb Q(s)\)。原矩阵在两域的秩同为4354；特征零部分来自
[原泛参数秩定理](../results/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)第5节，
模31部分来自同一真实完整模块。
取一个4354阶的 D 单位子式，作可逆块消元；其余 Schur 块在分式域为零，
故在 D 中也为零。因此 \(\operatorname{im}A_D\) 是 \(D^{4367}\) 的直和项。

若 \(\bar\kappa\in\ker\bar A\)，取任一整数多项式提升 \(\widehat\kappa\)，
则 \(A\widehat\kappa\) 被31整除。在 D 中，直和项性质给

\[
\operatorname{im}A_D\cap31D^{4367}=31\operatorname{im}A_D.
\]

所以 \(A\widehat\kappa/31\) 在 k(s) 的原 cokernel 中为零。
原常预基正常形运输保这个结论。故每个真实 β 列及其允许 s 移位的
预算85截面也都在 \(\mathcal T\) 内。

将 torsion 按支撑分为有限图部分与无穷点部分：

\[
\mathcal T=\mathcal T_{\mathrm{aff}}\oplus\mathcal T_\infty.
\]

已完成的仿射 torsion 长度为315。因此对任何当前残差与 β 的线性组合 v，

\[
\boxed{
v\in R(S_{\le85})
\iff
\begin{cases}
\text{仿射315维类为零},\\
\text{原无穷点局部类为零}.
\end{cases}} \tag{4.1}
\]

在这个量词下，没有第三类来自 free 部分的隐蔽预算障碍；但第二行仍是必须支付的
真实条件。特别是，仅解此次315×1152系统不能把 `finite_budget_verified` 改为 true。

## 5. 完整 T96 图给无穷点幂零指数上界96

把图的1021条输出主元行写成 \((G_i,V_i)\)，其中 \(RV_i=G_i\)，
令 \(d_i=\deg_sG_i\)。T96 使用来源移位 \(\delta_j-96\)，而这些行以输出为首项，
所以实际图逐行给

\[
\operatorname{cost}(V_i)\le d_i+96. \tag{5.1}
\]

这是原来源身份，不是用一个未知多项式逆估计。G 主分量不同，且是实际完整的
度数优先 image GB。对任一 \(v\in\operatorname{im}_{k[s]}R\)，按 G 正常形约化，
若 \(D=\max_c\deg v_c\)，每个商系数满足

\[
v=\sum_iq_iG_i,\qquad\deg q_i\le D-d_i.
\]

原因是每次约化都严格降低模首项而不增整行次数。于是(5.1)给实际来源

\[
v=R\sum_iq_iV_i,\qquad
\operatorname{cost}\Bigl(\sum_iq_iV_i\Bigr)\le D+96. \tag{5.2}
\]

若 v 的输出成本至多 B，则 w≥0 使 D≤B，故来源成本至多 B+96。

现在任取 \(\mathcal T_\infty\) 的局部元素，视为
\(H^0(\mathcal T_\infty(85))\) 中的截面。(3.1) 给它一个实际
\(v\in Q_{\le85}\) 的代表。它在有限图为零，所以 v 在整个 k[s] 的像内；
(5.2) 使它在预算181中已经为零。预算85到181的自然嵌入，在齐次表达中是乘 t⁹⁶，
在无穷点图 \(u=t/s\) 中正是乘 u⁹⁶。因此

\[
\boxed{u^{96}\mathcal T_\infty=0.} \tag{5.3}
\]

这不声称真实最大指数为96，也没有重做无穷点 Smith 计算。
它是由已经取得的真实来源图付出的统一有限上界。

## 6. 明确的96阶局部测试及移位方向

在无穷点取 \(u=t/s\)。第1节原加权矩阵准确变为

\[
R^\infty_{cj}(u)=u^{\delta_j-w_c}R_{cj}(1/u). \tag{6.1}
\]

对预算 B=85 的右端 v，其对应局部代表是

\[
v_c^\infty(u)=u^{85-w_c}v_c(1/u). \tag{6.2}
\]

这些都是真多项式，由各自的成本界保证。无需把原 m 变量改成其它未记录来源。

因为局部 cokernel 是一个自由模与 \(\mathcal T_\infty\) 的直和，且后者被 u⁹⁶
消去，torsion 到该局部 cokernel 模 u⁹⁶ 的映射是单射。故对第4节限定的 v，
其无穷点类为零当且仅当

\[
\boxed{v^\infty\in\operatorname{im}
\bigl(R^\infty:(k[u]/u^{96})^{2195}
\longrightarrow(k[u]/u^{96})^{1034}\bigr).} \tag{6.3}
\]

因此(4.1)的第二行是一个明确有限的原来源测试，不需无限阶形式级数。

对成本 \(\alpha_j\) 的基础 β 列，先定义
\(b_{cj}^\infty=u^{\alpha_j-w_c}b_{cj}(1/u)\)。它的允许仿射移位
\(s^\ell b_j\)，\(0\le\ell\le85-\alpha_j\)，在**共同预算85**的无穷点图中是

\[
u^{85-\alpha_j-\ell}b_j^\infty. \tag{6.4}
\]

这是必须保留的反向移位。不能在无穷点仍把同一来源乘 u^ℓ，或忘记把成本80、81、85
的不同列补齐到同一总度85。

若此次仿射必要系统有一组解 λ₀，则完整解空间为 λ₀ 加该系统的核。
必须在这个**整个仿射解空间**上再施加(6.3)，而不是只检查一个任意 particular
solution 失败后就断言有限问题无解。原315×1152系统所保存的全系数RREF与列标签
已足以重建这个解空间；所需无穷点算术尚未执行。

## 7. 原全局除子的一个独立数值上界

由(2.2)的秩、次数可得

\[
\operatorname{rank}\mathcal C=13,\qquad
\deg\mathcal C=-32670-(-93260+60050)=540.
\]

令 \(\mathcal F=\mathcal C/\mathcal T\)，它是秩13向量丛。由于
\(\mathcal Q(40)\) 是非负次数线丛之和，故全局生成；其商
\(\mathcal F(40)\) 也全局生成。取最高外幂，\(\det\mathcal F(40)\)
有非零全局截面，所以其次数非负，亦即 \(\deg\mathcal F\ge-520\)。于是

\[
\operatorname{length}\mathcal T=540-\deg\mathcal F\le1060,
\qquad
\boxed{\operatorname{length}\mathcal T_\infty\le745}. \tag{7.1}
\]

这里不需要选 \(\mathcal F\) 的分裂型。结合
[全原无穷点一阶计算](../results/R150-appendix-original-infinity-jet-and-mod31-determinantal-thickness.md)，
恰有14个正局部指数，其中4个为1、其余10个至少为2；本条进一步给每个不超过96、
总和不超过745。因此已知范围是

\[
24\le v_\infty(\Delta_{31})\le745,
\qquad339\le\deg\Delta_{31}\le1060.
\]

这仍没有确定任何额外特征零根或局部厚度。

## 8. 计算与结论边界

本条没有执行96阶计算、没有给有限1658系统的新秩，也没有改动当前一次全200
Bockstein任务的程序或状态。当前任务的仿射结果必须按其真实回执另行登记。

若完整有限β条件最终通过，它给的是原预算85模型的 mod961 整数提升；
仍须恢复原十七式全系数身份，后续精度与有理重构也须独立支付。
有限β条件失败则排除该预算的相应整数首步提升，不能无条件排除带31分母的
特征零来源。R150 全复参数余集与主 ISP 均未由本条关闭。
