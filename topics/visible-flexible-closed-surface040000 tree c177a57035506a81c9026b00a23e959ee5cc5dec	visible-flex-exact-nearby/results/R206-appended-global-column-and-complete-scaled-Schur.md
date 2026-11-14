# R206：新增全局列与完整缩放 Schur 求解

**状态：已证明。** 本结果只把已经完整组装的真实有限normal扩展到一个新增全局参数。当前用途是保留原cut高度列，再添加R205平环弯曲幅度列；它不代替该列的真实链式求导，不代替完整非线性试探，也不声称新的曲面已经合格。

## 1. 完整normal与布局

设原完整参数$x\in\mathbb R^n$包含所有局部角、高度、半径参数及一个全局cut高度，新增参数记$A$。假定完整实际残差$F(x,A)$及全部列都已计算，写
\[
 J=(J_x,j_A),\qquad
 H=J^TJ=\begin{pmatrix}H_0&h\\h^T&d\end{pmatrix},
 \quad
 g=J^TF=\binom{g_0}{g_A}.
\]
其中$h=J_x^Tj_A,d=j_A^Tj_A,g_A=j_A^TF$必须来自同一实际$x,A,F$，不能把旧normal补零冒成新增列的normal。每个参数的列平方范数是同一完整$H$的对角。

对$H_{ii}>0$取$s_i=H_{ii}^{-1/2}$，零列取$s_i=1$。新增列也独立取$s_A=d^{-1/2}$，$d=0$时取$s_A=1$。令
\[
 D=\operatorname{diag}(s_1,\ldots,s_n),\qquad
 \widehat D=\operatorname{diag}(D,s_A).
\]
原有限布局保持原字节顺序，新增$A$只追加到index $n$。原cut的一个border仍留在原块中，新增幅度是第二个global border；绝不能把它伪放进一个局部径向块。

给定明确$\lambda>0$，完整LM方程为
\[
 (\widehat D H\widehat D+\lambda I)v=-\widehat Dg,
 \qquad \Delta(x,A)=\widehat Dv.
\]
因为$H=J^TJ$半正定且缩放为正，阻尼矩阵严格正定。零列也得到明确的$\lambda$，没有隐藏对角修正。

## 2. 只利用原完整求解器的公式

写
\[
 P=DH_0D+\lambda I,\quad b=Dhs_A,\quad
 c=s_A^2d+\lambda,\quad q=Dg_0,\quad q_A=s_Ag_A.
\]
$P$包含全部原参数，包括原cut border。用原R195型完整求解器分别解
\[
 Pv_0=-q,\qquad Pw=-b.
\]
这两个右端只是同一线性方程的右端；第二个不是新的物理残差，也不是另一次非线性目标求值。由于$P$严格正定，两解唯一。

定义
\[
 \sigma=c+b^Tw,\qquad
 v_A=\frac{-q_A-b^Tv_0}{\sigma},\qquad
 v_x=v_0+w\,v_A.
\]
因为$w=-P^{-1}b$，有
\[
 \sigma=c-b^TP^{-1}b>0,
\]
最后一个不等式是完整正定阻尼矩阵的Schur补性质。直接代入可得
\[
 Pv_x+bv_A=-q,\qquad b^Tv_x+cv_A=-q_A.
\]
所以该算法恰好解完整原LM方程，没有省去任何交叉项。原实现可各做一次完整band+cut求解，得到两右端的解；未来缓存同一因子只影响工程成本，不改变数学。

真实物理步为
\[
 \Delta x=Dv_x,\qquad \Delta A=s_Av_A.
\]
这里必须先完成原有完整列缩放，再计算新增列的缩放。不能直接使用未缩放$A$方向，不能使用旧normal的对角，也不能把不同幅度处的$J_x$和$j_A$混在一起。

## 3. 支撑与原检查保持

若原局部列按径向支撑组成固定宽度的band，新增幅度影响所有径向位置，但它只产生一个全局列以及与原块的完整交叉向量$h$。原$H_0$的局部band结构不变，原cut高度仍按原border处理。

因此可直接复用原求解器对$H_0$的全部维度、参数布局、有限性、原带外项和缩放检查。所有非零带外项仍必须保留或报错，不得因新增幅度而截断。源码以显式
\[
 \texttt{baseProvider},\quad\texttt{dimension}=n+1,\quad
 \texttt{globalIndex}=n
\]
标识新表示；旧读取器不得把它当旧$n$维实体。

浮点实现与原R195一样区分工作对称矩阵和输入原矩阵。原块仍由原函数给出；新增交叉项工作值取两方向的平均，原两方向分别保留用于完整原方程残差。给原求解器构造辅助右端时的浮点乘除舍入也显式记录。$\sigma$不正或出现非有限值就返回实际求解失败，交由明确LM阻尼策略处理，不偷偷加jitter。

返回的完整方向还要重新计算
\[
 g^T\Delta z,\qquad v^T(\widehat D H\widehat D)v,
\]
及完整工作/原缩放方程残差；不能只检查原$n$维子方程。算法报告的预测值只是线性模型。接受仍由同一完整新目标在真实试探$(x+\alpha\Delta x,A+\alpha\Delta A)$上决定，保持原Armijo与域检查。

## 4. 与真实平环幅度的接口

对R205冻结参考，已有完整角参考的$A,sA,ssA,uA$导数以及mean-height correction的$A,sA,ssA$导数。若把$A$升级为参数，必须将这些变化穿过完整单位切向量、物理primitive、半径乘法、位置两jet、真实Gram/II及全部几何残差，形成真正$j_A$。

如果使用R201无反射mean-phase，还必须包括$\beta_A,\beta_{sA},\beta_{ssA}$，并使用full-half primitive；不能把固定幅度的phase或outercut截面平均高误当innercuff高度。半径设计列仍保留；中央$A_q$与新增tail幅度$A$不是同一变量。

这些字段导数不是由本线性算法自动生成的。只有完整新列和新$H/g/\operatorname{diag}/\|F\|^2$已经真实完成，才可把此算法接入实际LM。幅度区间、正图域、固定cuff高度窗和所有几何条件仍由真实provider逐次验证，不投影试探参数。

## 5. 已完成的实际线性核及其范围

首次测试调用遗漏R196所要求的明确rational knots，被原provider在normal组装前拒绝；未称任何OS退出或数学求解完成。修正调用只补准确uniformKnots(3)，没有放宽原输入检查。

随后在一个真实R203位置目标上组装19维完整normal，包含metric、真实曲率和全部位置几何行。追加两种实际导数方向$j_A=J_xb$：

1. $b$只选原cut高度，因此新增列与一个原列完全重合，测试真实秩亏normal上的显式阻尼；
2. $b$混合全部原角、高度、cut和半径列，得到具有全局支撑的新列。

每种分别取$\lambda=10^{-2},10^{-3},10^{-5}$。六个20维系统的方向与独立全dense Cholesky比较，相对差不超过$3.102\cdot10^{-12}$；完整原缩放方程相对残差不超过$4.612\cdot10^{-16}$。辅助缩放右端最大舍入差不超过$2.776\cdot10^{-17}$。全部在纯V8实际执行，未创建OS子进程，不能写作Node exit0。

该核使用真实完整位置normal，但新增列是说明的$J_xb$，不是已完成的R205幅度列。实际tail-$A$ normal、非线性接受和最终全域metric/reach仍须单独完成；本结论不给这些未做事项补结果。
