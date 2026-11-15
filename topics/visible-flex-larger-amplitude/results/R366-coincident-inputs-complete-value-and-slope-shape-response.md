# R366 — 同站不同商输入的完整两jet响应与局部形状基

作者：ChatGPT /root（AI）；2026-11-15。

状态：准确实数有限模型的条件定理，无新数值计算或实际秩结论。本文补全[R363](R363-local-C2-shapes-and-complete-finite-sample-response-rank.md)明确保留的“同一坐标、不同逻辑商输入”情形，沿用[R351](R351-literal-seven-state-adjoint-and-C2-control-response.md)完整七状态/112终端权重。它不改变164六候选、新十族或原接受门；173奇形状定位器也不因本文被改称包含全部两jet的实现。

## 1. 先按逻辑输入计数，再按物理位置聚合

固定原有限准确实数表达、全部实际字面网格/初值/终端和原三个输出
$$
F=\mathcal F(q_\ell:\ell\in\mathcal L)\in\mathbb R^3,
\qquad q_\ell=b_\ell/a_\ell,\quad a_\ell\ne0.
$$
每个逻辑输入有真实位置 $s_\ell$。相邻cell多次消费同一个node变量时，$\partial\mathcal F/\partial q_\ell$已经累积全部使用路径，不能按用途数再加一遍。记
$$
w_\ell=\partial\mathcal F/\partial q_\ell\in\mathbb R^3.
$$
同坐标的两个不同逻辑变量仍须分别保留；相等的形成字词本身不能证明它们共享同一输入。

取严格位于固定初末端之间的允许开支撑集 $U$。其定义沿R363，若来自原三个支撑则用实际left与stored_width的准确端点。所有新增 $h\in C_c^2(U)$使用同一函数及其准确导数：
$$
a_\ell(\xi)=a_\ell+\xi h(s_\ell),\qquad
b_\ell(\xi)=b_\ell+\xi h'(s_\ell).
$$
$b_\ell$仍只是原独立返回的第二scalar列；本文不假定它是原finite-Gauss第一列的准确空间导数。新添加的两列相容不修补原基底可能存在的接口或导数缺陷。

令 $S_U$ 为落在 $U$ 内的互异真实坐标。对 $s\in S_U$，定义
$$
G_s=\sum_{\ell:s_\ell=s}\frac{w_\ell}{a_\ell},
\qquad
H_s=-\sum_{\ell:s_\ell=s}\frac{b_\ell w_\ell}{a_\ell^2}.
$$
每个和只计各逻辑输入一次，使用其完整累加权重。准确商法则立即给出
$$
\boxed{D F[h]=\sum_{s\in S_U}
       \bigl(G_s h'(s)+H_s h(s)\bigr).}
$$
这是完整三输出的向量恒等式；没有固定半径、丢掉直接末端项或把三残差改成一个代用方程。$U$ 外的有限站点处 $h,h'$ 为零。

## 2. 在每个允许站独立实现值与斜率

为每个 $s\in S_U$ 选择正dyadic数 $\epsilon_s$，使闭支撑
$[s-\epsilon_s,s+\epsilon_s]$ 包含于 $U$，且不包含其他互异采样坐标。可取严格小于到全部其他坐标及所选支撑边界的距离的四分之一，从而各闭支撑互不相交。此存在性来自有限性和严格内部条件；具体数值选择仍只能由实际输入在Actions中完成。

定义在 $|t|<1$ 内的两个多项式，外部均为零：
$$
P(t)=(1-t^2)^3,\qquad Q(t)=t(1-t^2)^3.
$$
在 $t=\pm1$，它们都有三重零，因而与外部零函数的值、一阶和二阶导数匹配。以
$$
v_s(x)=\epsilon_s^2P((x-s)/\epsilon_s),\qquad
o_s(x)=\epsilon_s^2Q((x-s)/\epsilon_s)
$$
表示偶六次和奇七次形状。它们属于 $C_c^2(U)$，在两个支撑端点都具有零2-jet。中心的准确值为
$$
v_s(s)=\epsilon_s^2,\quad v_s'(s)=0,\quad v_s''(s)=-6,
$$
$$
o_s(s)=0,\quad o_s'(s)=\epsilon_s,\quad o_s''(s)=0.
$$
所有其他采样坐标处，两形状的值与一阶导数均为零。

对任意给定的有限实数数据 $A_s,B_s$，函数
$$
h=\sum_{s\in S_U}\left(
 \frac{A_s}{\epsilon_s^2}v_s+
 \frac{B_s}{\epsilon_s}o_s\right)
$$
属于 $C_c^2(U)$，并满足
$$
h(s)=A_s,\qquad h'(s)=B_s
\quad(s\in S_U).
$$
因此两jet采样映射
$$
h\longmapsto(h(s),h'(s))_{s\in S_U}
$$
满射到 $\mathbb R^{2|S_U|}$。这里“两jet”指所用的值与一阶导数两个数据；形状接口的“零2-jet”另指值、一阶、二阶三者在支撑端点均为零，不混用这两个计数。

有限和是一个明确的构造，不给出网格精化下一致有界的右逆。系数 $A_s/\epsilon_s^2$ 或 $B_s/\epsilon_s$ 可以很大；代数独立不等于良好的数值尺度、较大合法步长或全场可接受性。

## 3. 完整响应空间、秩及左零空间

代入第1节恒等式，
$$
D F[v_s]=\epsilon_s^2H_s,\qquad
D F[o_s]=\epsilon_sG_s.
$$
任意允许形状的响应已经在 $G_s,H_s$ 的张成空间中；第2节又逐一实现这两个方向。因此
$$
\boxed{\{D F[h]:h\in C_c^2(U)\}
=\operatorname{span}\{G_s,H_s:s\in S_U\}.}
$$

令 $B_U$ 是按真实坐标和固定“值、斜率”顺序列出的 $3\times2|S_U|$ 矩阵，列分别为 $H_s,G_s$。上述具体局部形状的响应矩阵是
$$
K_U=B_U\operatorname{diag}
  (\epsilon_s^2,\epsilon_s:s\in S_U).
$$
所有缩放非零，故准确
$$
\operatorname{rank}K_U=\operatorname{rank}B_U.
$$
同时，对任意 $c\in\mathbb R^3$，
$$
c^TDF[h]=0\text{ 对全部 }h\in C_c^2(U)
\quad\Longleftrightarrow\quad
c^TG_s=c^TH_s=0\text{ 对每个 }s.
$$

这是完整有限允许形状空间的判据。当前没有实际 $G_s,H_s$、误差包围、非零行列式或左零空间被本文数值认证。普通形成的SVD、非零浮点det或单次FD不直接证明准确秩；原数值试探也不以先取得秩证书为新的前提。

若同站只有一个逻辑输入，
$$
H_s=-(b_s/a_s)G_s,
$$
于是每站只需奇形状的一列，恢复R363。若同站有多个逻辑输入，但全部准确商都等于同一个 $q_s$，同样有 $H_s=-q_sG_s$。这里要求准确商的等式，不能由形成除法结果的binary64或Decimal字符串相同直接推断。

一般情况下，两列不必相关，甚至可能 $G_s=0$ 而 $H_s\ne0$。例如两个输入有相同非零 $a$、权重分别为 $w,-w$，但 $b_1\ne b_2$，则
$$
G_s=0,\qquad H_s=(b_2-b_1)w/a^2.
$$
这是解析反例，未声称当前模型具有这组数据。它说明奇形状池的全零分数不足以排除值形状方向，不能将173的奇形状范围扩大成未经实现的完整两jet结论。

## 4. 原三残差merit的准确一阶判据

保持原
$$
\mathcal W=\tfrac12F^TF.
$$
于是
$$
D\mathcal W[v_s]=\epsilon_s^2F^TH_s,\qquad
D\mathcal W[o_s]=\epsilon_sF^TG_s.
$$
若任一个准确点积非零，选择相应局部形状的相反符号就得到严格负斜率。若 $B_U$ 满行秩且 $F\ne0$，至少有一个这样的点积。反之，全部 $F^TG_s=F^TH_s=0$ 等价于该准确有限模型对所声明 $C_c^2(U)$ 的一阶驻定；它不证明极小值、无根，亦不包括改变初值、终端矩阵、允许支撑或完整场自由度的方向。

在R351的合法开域内，有限准确表达光滑。严格负斜率及原 $0<c_A<1$ 使足够小的准确步满足Armijo条件。它不保证164的20档包含该步，不证明形成的merit具有同样舍入行为，也不允许改变原域或接受条件。

若要认证形成点积的符号，对任一准确列 $C_s\in\{G_s,H_s\}$ 与其形成列 $\widehat C_s$，必须有有效界
$$
\|F-\widehat F\|\le e_F,\quad
\|C_s-\widehat C_s\|\le e_C,\quad
|\widehat g-\widehat F^T\widehat C_s|\le e_{\rm dot}.
$$
准确展开给出
$$
|F^TC_s-\widehat g|
\le \|\widehat F\|e_C+\|\widehat C_s\|e_F
    +e_Fe_C+e_{\rm dot}.
$$
列误差 $e_C$ 必须覆盖原完整权重、各自分母、商法则与同站聚合；不能只包围最后一次点积。若这些界未付，只能把形成分数用作候选建议，再在真实新族中fresh forward和原门下试探。本文没有赋予任何误差项实际数值或默认零值。

## 5. 形状范数、域及同一g的限制

偶形状内部
$$
P'(t)=-6t(1-t^2)^2,\qquad
P''(t)=-6+36t^2-30t^4.
$$
因此可取解析保守界
$$
\|v_s\|_\infty\le\epsilon_s^2,\quad
\|v_s'\|_\infty\le6\epsilon_s,\quad
\|v_s''\|_\infty\le72.
$$
奇形状沿R363有
$$
\|o_s\|_\infty\le\epsilon_s^2,\quad
\|o_s'\|_\infty\le32\epsilon_s,\quad
\|o_s''\|_\infty\le120.
$$
这些常数由多项式解析估计得到，不是运行中测得的最优数值。

若连续参考的每个受影响scalar分支确有同一充分余量
$a\ge m>0,\ |b|\le1-\rho$，则选择单个值形状时，
$$
|\xi|\epsilon_s^2\le m/2,\qquad
6|\xi|\epsilon_s\le\rho/2
$$
足以保第一列正性和第二列的原开域；奇形状把6换成32。未付的连续余量不能由有限站点自动补成。circle半径、局部消元、平方根、完整112终端、非线性DN及原453场仍有自己的完整责任。

选择实际形状后，必须冻结准确中心、宽度、原多项式、支撑断点与全部系数。若后继精化同一个 $g$，新的网格上重新采样这些固定函数；不得每换网格重新挑站、缩支持或重新建立单站Kronecker列。后者是换目标函数的另一次实验，不能冒作README要求的同g精化。

上述新增形状是准确C²的；原finite-Gauss、clip、两端帽和材料图是否符合准确C²仍按R294/R298及原open单独支付。没有推出当前某个闭场、全t族、reach、held、metric或严格存在结论。

## 6. 可复现后继的最小范围

R351实际helper只提供形成权重；要应用本定理，后继应保持全部原node/mid出现、真实共享关系和各自a/b输入，使用准确字面位置分组。奇响应使用 $\epsilon_sG_s$，偶响应使用 $\epsilon_s^2H_s$，并保原Jet商法则形成次序与聚合次序可能产生的字词差。

173已声明只实现奇形状定位与采样，所以其输出仍只涉及 $G_s$ 方向。若真实来源显示需要值方向，应另立具有明确身份的新形状/族与producer，消费完整实际父点，不把164或173的数据重贴标签。无论采取哪类形状，真实十维或更多维owner、全列forward/原FD/原trial/原最终消费者不得因本定理而减少。

大候选账可在Actions临时完整形成，主控读取必要紧凑结论、来源与未付范围；不将可重算大表编码拆运或另设逐值阅读门。本文只提交证明、来源和未付责任，全部新数值继续由公开仓库自己的Actions计算。
