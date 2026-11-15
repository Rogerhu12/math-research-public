# R150 补篇：原正常九维 pencil 的非幂零性与有限几何级数消元的准确边界

日期：2026-11-15。作者：Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 结论与量词

保持原六模矩阵 $K$、原 Hankel 空间、原两个 Gram 矩阵 $J_2,J_3$ 以及原物理投影 $\Pi$。令
$$
y=v(s)=(1,s,\ldots,s^5)^{\mathsf T},\qquad Y=yy^{\mathsf T},
$$
并定义
$$
\mathcal L_y=J_3^{-1}B_{Ky}J_2,\qquad
A_yM=(\mathcal L_yM)_{Ky},\qquad
R_YZ=\Pi(YKZ+ZKY).
\tag{1.1}
$$
这里 $B_{Ky}$ 是乘以原极线多项式的矩阵；$\Pi$ 始终是原 $J_2$ 度量对应的 Hankel 投影。

本次在原参数 $s=4,3,5$ 上分别进行了完整九维有理数运算。三个点的正常算子 $A_y$ 均可逆，而诱导算子
$$
X_s=(A_y|_{\mathrm{normal}})^{-1}R_Y|_{\mathrm{normal}}
\tag{1.2}
$$
均不幂零。只用 $s=4$ 的精确值已经足够：
$$
\boxed{
\operatorname{tr}X_4=
-\frac{
173426385394976878339490215263179048478569283
}{
1316444161047835023954502818828451840000000
}\ne0.}
\tag{1.3}
$$

因此，“在原线性中心算子可逆的局部，$A_y^{-1}R_Y$ 在整个正常空间幂零，从而可用有限几何级数消去全部正常变量”这一普适断言不成立。包含 $A_y^{-1}R_Y$ 的整个算子族也不可能联合幂零。

这不否定原九个平方目标的成员性，不排除保留全部 $\Gamma$ 方程和完整来源 Schur 的特殊消元，也不说明原参数 $s=2$ 的目标局部费用。结论没有外推到普通不变子空间问题。

## 2. 使用真实正常商，而不是删去方程后的矩阵

令 $u=v'(s)$、$T=yu^{\mathsf T}+uy^{\mathsf T}$。原恒等式给出
$$
A_yY=A_yT=0,\qquad y^{\mathsf T}Ky=y^{\mathsf T}Ku=0.
\tag{2.1}
$$
后两个等式还直接给出
$$
R_YY=R_YT=0.
\tag{2.2}
$$
所以 $R_Y$ 对切向平面取商后有确定的作用。

取原二项式 moment 变换
$$
m_i=\sum_{j=0}^i\binom ij s^{\,i-j}z_j.
\tag{2.3}
$$
其矩阵 $\mathcal T(s)$ 行列式为一，前两列准确是 $Y,T$ 的 Hankel 坐标。令
$$
N(s)=\mathcal T(s)[:,2,\ldots,10].
$$
这是九维正常商的一个完整代表空间，不是改换原物理度量。定义
$$
H_s=N(s)^{\mathsf T}J_2A_yN(s),\qquad
P_s=J_2R_YN(s).
\tag{2.4}
$$

计算分别核对了 $H_s$ 的非零行列式及全部两个原切向行
$$
[Y,T]^{\mathsf T}P_s=0.
\tag{2.5}
$$
由于 $A_y$ 在原 $J_2$ 配对下自伴，且其核恰为这两条切向方向，式 (2.5) 将 $R_YN(s)$ 放回同一个真实 $\operatorname{im}A_y$。因此
$$
X_s=H_s^{-1}N(s)^{\mathsf T}P_s
\tag{2.6}
$$
是真实商作用。它满足两个完整乘回：
$$
H_sX_s=N(s)^{\mathsf T}P_s,
\tag{2.7}
$$
$$
A_yN(s)X_s=J_2^{-1}P_s=R_YN(s).
\tag{2.8}
$$
本次逐点核对 (2.7) 的全部 $81$ 个坐标和 (2.8) 的全部 $99$ 个坐标。特别地，没有仅在九条投影行上解方程后，漏掉两个切向反馈行。

更换正常商基只使 $X_s$ 相似变换。因此 (1.3) 是真实商算子的性质，不是某个非正交补空间的偶然矩阵迹。

## 3. 对有限多项式消元的严格后果

原 $N$ 方程沿 $M=cY$ 的正常线性部分是
$$
6A_y+4cR_Y.
\tag{3.1}
$$
在同一个正常商上，式 (2.8) 给出
$$
(6A_y+4cR_Y)N
=
6A_yN\left(I+\frac23cX_s\right).
\tag{3.2}
$$
由于
$$
\left.\frac{d}{dc}\det\left(I+\frac23cX_4\right)\right|_{c=0}
=\frac23\operatorname{tr}X_4\ne0,
\tag{3.3}
$$
该行列式是非常数多项式。因此 $I+\frac23cX_4$ 在 $\mathbb Q[c]$ 上没有多项式矩阵逆。特别地，任何固定截断的几何级数
$$
I-\frac23cX_4+\cdots+\left(-\frac23cX_4\right)^r
$$
都不能给出对所有 $c$ 成立的逆。

这里并未把 (3.1) 当作全部原十七式。原 $\Gamma$ 的六个方程、正常二次项、来源乘子和更高正常层可以在完整问题中共同补偿。因此 (3.3) 仅排除了“先独立取整个正常线性块的有限多项式逆”的捷径，不能替代原来源成员性判断。

## 4. 实际计算与可重建证据

入口为[原九维 pencil 小探针](../notes/2026-11-15-r150-original-normal-ay-inverse-ry-pencil-probe-789f.py)，调用已冻结的[原式生成器](../notes/2026-11-15-r150-original-transverse-first-connection-789f.py)。原式生成器 SHA256 为
2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186。

实际执行的探针为 $8875$ 字节，SHA256 为
b9d0fd1f44f07b8e1017ea80b28066afcc9e4113bbb364005d649bf083646485。
它只重新构造固定的 $K,J_2,J_3$、三个九维正常块与完整十一维乘回，没有重算原 $6188\times4367$ Macaulay 矩阵。

实际 run 为 43731613530，step 为 original-normal-ay-inverse-ry-pencil-three-points，执行来源提交为
bf04a6ac4f8316b341c82327706cc4233d3fecab。
入口参数为 --points 4 3 5、共享数学时限 $30$ 秒、内存限额 $512$ MiB。实际数学用时约 $0.049385118$ 秒，退出码为零。

[实际小回执](../notes/r150-local-projection-session-789f/43731613530-original-normal-ay-inverse-ry-pencil-three-points.json)保留：

1. 三个非零正常行列式、两个切向行恒等式和全部 $81+99$ 个真实乘回；
2. 每个 $X_s$ 的完整特征多项式，$X_s^1,\ldots,X_s^9$ 的精确迹、逻辑哈希及首个非零坐标；
3. 三个完整 $81$ 坐标 Cayley–Hamilton 乘回，以及 $X_s^9=0$ 与特征多项式等于 $x^9$ 的一致性核对；
4. 原 $K,J_2,J_3$、moment 变换和原物理 $R_Y$ 的哈希。

原始回执为 $35520$ 字节，SHA256 为
60bbc79fe49f7eb5683aef2cf70c39a69a44495c6e41766fc1a374a35c83d64e。

在 $s=4$，关键逻辑哈希是
$$
H_4:\quad
\text{c17e235fdd279f6b4ab458f9d21986b3f5d21816d5f264fc61cbbd9818f42320},
$$
$$
X_4:\quad
\text{84c2fee86dc99ba728d8be48a20e459aa82b9306caaf9707d59401ffb72b0a31}.
$$
非零迹 (1.3) 已经是一条独立可读的精确非幂零证书。其余两个合法点及九次幂是同次有界执行的核对，不用于扩大结论的量词。

下一步仍须在原 $s=2$ 参数和原平方目标上支付完整来源反馈，或控制未知有限参数处的真实来源分母；不再重复尝试这个已被原点证书排除的全正常幂零断言。
