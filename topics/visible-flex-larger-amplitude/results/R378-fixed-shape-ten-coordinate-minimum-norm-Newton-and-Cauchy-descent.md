# R378：固定新增形状后完整十维最小范数 Newton、径向截取与 Cauchy 回退的条件下降

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 1. 问题、有限对象与不能混同的范围

[R373](R373-actual164-r3-six-shapes-and-twenty-full-merit-rejections.md)实际付清了独立十族的完整三响应、六候选选择和20档真实试探。所选支撑1/k4形状给出负形成斜率，但只沿ξ的二十档全部因完整三残差 Armijo 拒绝。新增十列投影的数值奇异值为后继提供动机，不能当作准确秩或准确导数证书。

这里证明一个不同的、完整联合十坐标方向的**条件代数结论**。固定同一个已选形状，不重选六候选；固定旧九个形状表、全部原三残差和原112末端责任。参数
$p=(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi)$
是真正的十坐标向量。令 $F(p)\in\mathbb R^3$ 是合法域内同一有限实表达的三残差，
$W(p)=\tfrac12F(p)^TF(p)$。
本证明中用 $J=DF(p)$ 表示该准确实表达的导数；实际 Decimal50 forward、输入binary64字面表与投影描述只是它的数值实现和观察，没有因此得到准确导数或含舍入程序可微性证书。

原接受系数是准确的binary64字面lift
$$
c_A=0.200000000000000011102230246251565404236316680908203125,
$$
满足 $0<c_A<1/2$，不是把它替换为数学 $1/5$。实际路径为直线 $p+\alpha d$；本方案没有normal弯曲恢复，也没有把ambient线性模型当成另一曲线路径的模型。

## 2. 固定坐标尺度与新实验策略

取真实actual157九个持久参数作为数值初猜，ξ初值为0。旧父relative radius 0.0000390625仅是历史来源；本次不声称继承它。显式新尺度为
$$
S_{jj}=0.01\max(1,|p^{157}_j|),\quad 1\leq j\leq9,
\qquad S_{10,10}=0.01 .
$$
$S$在整个实验中固定，不在接受点或FD扰动后重算。这里的0.01是新策略的明确Decimal字面；实现会记录实际形成的十个正尺度。原三残差没有乘行权。缩放信赖域为 $\|z\|_2\leq1$，物理方向 $d=Sz$，因此约束的是同一固定椭球 $\|S^{-1}d\|_2\leq1$。

这些尺度不声称有唯一最优性，也不是从函数幅度或root半径推导出的收敛保证。它们清楚区分旧九物理系数的相对尺度与新ξ的绝对尺度。以下全部代数对任意固定正对角 $S$成立。

定义
$$
A=JS\in\mathbb R^{3\times10}.
$$
完整十列、完整三行都保留；没有按奇异值截断，没有丢掉大响应行，也没有改成单ξ标量方向。

## 3. 列pivot约定、Householder顺序与三角回代

对 $A^T\in\mathbb R^{10\times3}$ 作完整列pivot QR：
$$
A^T\Pi=Q_3R,\qquad Q_3^TQ_3=I_3,
$$
其中 $\Pi$ 为3×3置换阵，$R$ 为3×3上三角阵，$Q_3$ 是完整10×10正交 $Q$ 的前三列。这里pivot的是转置矩阵的三列，也就是**原三方程**；不是重新排列十个物理参数。

设程序返回pivot[j]表示变换后第j列来自原第pivot[j]列，则
$$
\Pi_{i,j}=1\quad\Longleftrightarrow\quad i=\operatorname{pivot}[j],
\qquad
(\Pi^TF)_j=F_{\operatorname{pivot}[j]}.
$$
由转置得到
$$
\Pi^TA=R^TQ_3^T .
$$

原433d Householder程序维护 $Q\leftarrow QH_j$，并对当前矩阵作 $H_j$ 左乘。若实际反射序列为 $H_0,H_1,H_2$，准确算术下上三角化给
$R_{\rm full}=H_2H_1H_0A^T\Pi$，返回
$Q=H_0H_1H_2$；故 $A^T\Pi=QR_{\rm full}$。不能把返回Q误当成Q的转置，亦不能把Q列回代方向反过来。

当三个准确对角均非零时，按下三角系统正向回代
$$
R^Ty=-\Pi^TF,\qquad
y_j=\frac{-F_{\operatorname{pivot}[j]}-\sum_{i<j}R_{ij}y_i}{R_{jj}},
$$
再取
$$
z_N=Q_3y.
$$
完整十个物理坐标由 $d_N=Sz_N$ 恢复。实现直接用原完整Householder核；不形成 $AA^T$，也不使用正规方程或SVD阈值。

## 4. 条件最小范数定理

**命题。** 若 $A$ 满行秩，且本节运算指准确实算术，则上述 $z_N$ 满足 $Az_N=-F$，并且是该完整线性系统的唯一最小欧氏范数解。因此 $d_N$ 是 $Jd=-F$ 的唯一最小 $\|S^{-1}d\|_2$ 解。

**证明。** 从上一节
$$
\Pi^TAz_N=R^TQ_3^TQ_3y=R^Ty=-\Pi^TF,
$$
所以 $Az_N=-F$。任一其他解 $z$ 都可写为
$z=z_N+n$，其中 $An=0$。满行秩及QR等式给
$\operatorname{range}(Q_3)=\operatorname{range}(A^T)$，
从而该空间与 $\ker A$ 正交。于是
$$
\|z\|_2^2=\|z_N\|_2^2+\|n\|_2^2.
$$
最小值仅在 $n=0$取得。物理尺度结论由可逆映射 $d=Sz$立即得到。证毕。

该结论不是由某个浮点最小奇异值超过阈值触发。实际形成R出现准确零字面或非有限运算时，程序保留完整异常，进入下一节的完整Cauchy提议；它不悄悄删除对应行、不用“数值秩二”代替原三方程，也不将失败宣称为数学秩亏。

## 5. 径向截取及原全三线性merit

对 $F\ne0$ 且满行秩情形，令
$$
\vartheta=\min(1,1/\|z_N\|_2),\qquad z=\vartheta z_N,\qquad d=Sz.
$$
准确算术下 $\vartheta>0$、$\|z\|_2\leq1$，并且
$$
Jd=-\vartheta F,\qquad
F^TJd=-\vartheta\|F\|_2^2<0.
$$
完整三残差的线性模型沿任意 $\alpha\in(0,1]$ 为
$$
F+\alpha Jd=(1-\alpha\vartheta)F,
\qquad
W_{\rm lin}(\alpha d)=(1-\alpha\vartheta)^2W.
$$
与原Armijo界比较：
$$
W_{\rm lin}(\alpha d)-[W+c_A\alpha F^TJd]
=\alpha\vartheta[\alpha\vartheta-2(1-c_A)]W<0,
$$
因为 $\alpha\vartheta\leq1<2(1-c_A)$。

这里径向截取不宣称解了完整非线性trust子问题，也不宣称它是有界线性最小二乘的精确最优解；它保留完整Newton响应的方向关系。R373只沿新ξ单列的提议没有这一 $Jd=-\vartheta F$ 结构；联合方向是在准确条件下避免把第二、第三分量独立推大的一个明确机制。

实际Decimal50形成的Q并非区间认证正交阵，三角残差未被证明为零，径向范数也不当作准确外包。程序因此保留原Q/R/pivot、未截取方向、三角残差、完整 $Az_N+F$、截取因子、形成 $Jd+\vartheta F$、实际形成范数与原斜率，不把上述准确条件结论当成实际通过标志。

## 6. 无rank阈值的完整缩放Cauchy回退

对任意 $A$，设完整缩放梯度
$$
g=A^TF.
$$
若 $g\ne0$，则 $Ag\ne0$：若 $Ag=0$，有
$\|g\|_2^2=g^TA^TF=(Ag)^TF=0$，矛盾。因此
$$
\gamma=\|g\|_2^2>0,\qquad
\beta=\|Ag\|_2^2>0 .
$$
取
$$
\tau=\min(1/\|g\|_2,\gamma/\beta),\qquad
z_C=-\tau g,\qquad d_C=Sz_C .
$$
则 $\|z_C\|_2\leq1$，原完整merit斜率为
$$
F^TJd_C=-\tau\gamma<0.
$$
完整线性模型满足
$$
W_{\rm lin}(d_C)-W
=-\tau\gamma+\tfrac12\tau^2\beta
\leq-\tfrac12\tau\gamma.
$$
更一般地，$0<\alpha\leq1$ 时
$$
W_{\rm lin}(\alpha d_C)-W
\leq-\tfrac12\alpha\tau\gamma
<c_A\alpha F^TJd_C ,
$$
其中最后一个比较应理解为
$-\tfrac12\alpha\tau\gamma<-c_A\alpha\tau\gamma$，
使用的是同一个准确字面 $c_A<1/2$。

回退只在实际Newton三角算术失败、非有限或形成原斜率非负时使用；原失败与traceback保留。若实际形成的 $g$ 为零、非有限，或回退形成斜率仍非负，记录“无本次有限严格下降提议”并停止，不推准确驻点。有限形成 $\beta=0$ 时可用信赖域边界长度作明确数值提议，但它没有上面准确 $\beta>0$的证书；最后仍需原strict slope与真实试探。任何新阈值、截奇值或行删减都不属于本方案。

## 7. 原非线性merit、有限方向误差与二十档范围

设原准确有限表达合法，给定任一物理方向d，写
$$
E(\alpha)=F(p+\alpha d)-F(p)-\alpha Jd.
$$
准确恒等式为
$$
W(p+\alpha d)-W(p)
=\alpha F^TJd+\tfrac12\alpha^2\|Jd\|_2^2
 +(F+\alpha Jd)^TE(\alpha)+\tfrac12\|E(\alpha)\|_2^2.
$$
因此线性模型全部满足Armijo，不等于实际非线性步满足Armijo。若F在该点可微、真实方向有负准确斜率且附近合法，则存在充分小步满足原Armijo；这仍不保证预设的 $\alpha=1,\ldots,2^{-19}$ 必含该步。有限域失败也可以先于该邻域被触发。

若实际形成方向与理想Newton关系有缺陷
$r=Jd+\vartheta F$，则
$$
F^TJd=-\vartheta\|F\|_2^2+F^Tr.
$$
对准确残差和准确误差的充分界
$\|r\|_2<\vartheta\|F\|_2$可保证负斜率；**本方案不把该界新增为接受门，也未用普通Decimal残差声称已付该界**。所有形成误差只作记录，最终科学行动仍按当前完整原full3 slope、实际原primal域、未加权W及同 $c_A$ 的Armijo。

完整原三方程没有改为分量归一化、重权目标或法向精度门。当前Hessian、连续目标误差、native响应都没有由这些QR读数自动获得。

## 8. 独立Request178的执行责任

源策略固定如下：

- 从真实actual157九p50加ξ=0独立重建原输入与完整十族。R373只绑定固定支撑1/k4的选择证据；不读取已删164 raw，也不把164失败当作接受父。
- 原09240 family与8cb835十model直接复用。形状公式/支撑/列身份全过程固定；全部十坐标可移动，新族不冒旧九参数。
- 固定S及缩放半径1；每个实际接受后重新形成完整当前十列，最多8个完整方向，每方向原20档真实线搜。完整拒绝或无有限严格负斜率即按真实原因停止，不在同点无限机械重复。
- 原初末120 FD检查、160bit/depth14标量域、453圆参考、完整112 residual和投影边界全部保留；native/full nonlinear field/finalJ/audit仍按实际范围记录，不伪称通过。
- 所有科学运算只在公开Actions。完整原模型、QR、提议与实际试探在本次临时目录记录；小摘要保真实标量、必要小阵及覆盖/身份，原大表不入Git/Release/新artifact。
- 8×20只是明确本次预算，不是课题终点。实际出现接受后可据新完整原记录继续；本证明不预填未来父点或run。

本定理证明的是完整联合方向在准确条件下的结构与下降，不是当前有限程序的准确性证书、全局收敛定理或新非零完整场存在结论。
