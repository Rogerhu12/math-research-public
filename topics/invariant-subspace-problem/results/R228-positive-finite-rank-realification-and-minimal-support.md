# R228：正有限秩见证的 C 实化、配对降秩与最小支撑约束

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：完整有限维结构引理与一个精确的轨道变形障碍。没有把任意秩见证降到秩一，没有把共轭 $C$ 作用于某个未知零子商后仍属该子商作为假设。

## 1. C 对称上的正泛函实化

沿用本题的共轭 $C$；每个 $F\in\mathfrak C=\{A\}'$ 都满足
$$F^*=CFC.$$
内积对第一变量线性。设 $\rho\ge0$ 为有限秩算子，定义
$$
\rho^C=C\rho C,\qquad
\tau=\frac{\rho+\rho^C}{2}.
\tag{1.1}
$$
二者都正，且 $C\tau C=\tau$、$\operatorname{Tr}\tau=\operatorname{Tr}\rho$。

**引理1.1。** 对任意有界 $C$ 对称算子 $F$，
$$
\boxed{\operatorname{Tr}(\rho^C F)=\operatorname{Tr}(\rho F),
\qquad \operatorname{Tr}(\tau F)=\operatorname{Tr}(\rho F).}
\tag{1.2}
$$

证明写出共轭步骤。若 $\rho=\sum_j x_j\otimes x_j$，则
$\rho^C=\sum_j Cx_j\otimes Cx_j$。由 $FC=CF^*$ 以及
$\langle Cu,Cv\rangle=\langle v,u\rangle$，
$$
\langle FCx_j,Cx_j\rangle
=\langle CF^*x_j,Cx_j\rangle
=\langle x_j,F^*x_j\rangle
=\langle Fx_j,x_j\rangle.
$$
相加即得 (1.2)。没有把反线性 $C$ 当成线性算子在迹里无解释地循环移动。

特别，若 $\operatorname{Tr}\rho=1$ 且
$$
\operatorname{Tr}(\rho SF)=0\quad(F\in\mathcal A),
\tag{1.3}
$$
其中 $S\in\mathfrak C$，则 $SF\in\mathfrak C$ 仍为 $C$ 对称，故 $\tau$ 是同一条件的正常正见证。

## 2. 两个 C 实谱向量合并成一个正向量泛函

因为 $\tau$ 为有限秩正算子且 $C\tau C=\tau$，其每个非零特征空间都被 $C$ 保持。可以选一个 $C$ 实正交归一谱基，写成
$$
\tau=\sum_{j=1}^r\lambda_j u_j\otimes u_j,
\qquad \lambda_j>0,\quad Cu_j=u_j.
\tag{2.1}
$$
若 $F$ 为 $C$ 对称，则对 $C$ 实 $u,v$ 有
$$\langle Fu,v\rangle=\langle Fv,u\rangle.$$
这是 $F$ 对双线性对称配对 $\langle\cdot,C\cdot\rangle$ 的对称性。

对两个谱项，置
$$
x=\sqrt\lambda\,u+i\sqrt\mu\,v.
$$
直接展开正向量泛函，交叉项准确抵消：
$$
\begin{aligned}
\langle Fx,x\rangle
&=\lambda\langle Fu,u\rangle+\mu\langle Fv,v\rangle\\
&\quad+i\sqrt{\lambda\mu}
\bigl(\langle Fv,u\rangle-\langle Fu,v\rangle\bigr)\\
&=\lambda\langle Fu,u\rangle+\mu\langle Fv,v\rangle.
\end{aligned}
\tag{2.2}
$$

把 (2.1) 的相邻谱项两两配对，若 $r$ 为奇数就保留最后一个实向量。得到正有限秩算子 $\sigma$，使
$$
\boxed{
\operatorname{rank}\sigma\le\lceil r/2\rceil,
\quad \operatorname{Tr}\sigma=\operatorname{Tr}\rho,
\quad \operatorname{Tr}(\sigma F)=\operatorname{Tr}(\rho F)
}
\tag{2.3}
$$
对全部 $C$ 对称 $F$ 成立。

这不是无限迭代地把任意秩降到1：实化可能先把秩 $d$ 增至 $2d$，(2.3) 随后只把它降回 $d$。

## 3. 最小正见证的支撑与 C 支撑至多交一维

假设满足 (1.3)、迹为1的正有限秩见证存在，选其中秩最小者 $\rho$，记
$$d=\operatorname{rank}\rho,\qquad W=\operatorname{Ran}\rho.$$
由于 $\rho,\rho^C$ 均为正，
$$
\ker(\rho+\rho^C)=\ker\rho\cap\ker\rho^C.
$$
有限维正交补给
$$
\operatorname{Ran}\tau=W+CW,
\qquad
r=\operatorname{rank}\tau
=2d-\dim(W\cap CW).
\tag{3.1}
$$

若 $\dim(W\cap CW)\ge2$，则 $r\le2d-2$，(2.3) 给同一正见证且秩至多 $d-1$，矛盾。因此
$$
\boxed{\dim(W\cap CW)\le1.}
\tag{3.2}
$$

特别，最小秩见证若支撑本身被 $C$ 保持，就只能为秩一。一般最小见证的支撑可以与其 $C$ 像完全不交；(3.2) 没有否定 $d>1$。

这里 $W$ 只是有限秩密度的支撑，没有假设它对 $A$ 不变，也没有假设某个实现 (1.3) 的未知不变子商被 $C$ 保持。

## 4. 最小支撑上的压缩理想必须占满一个实超平面

还有一个不依赖 $C$ 的必要条件。令
$$
\mathcal J=S\mathcal A,
\quad
\mathcal V_W=\operatorname{span}_{\mathbb R}
\{\operatorname{Re}(P_WJ|_W),\operatorname{Im}(P_WJ|_W):J\in\mathcal J\}.
$$
这是 $W$ 上 Hermitian 矩阵实空间的子空间。$\rho|_W$ 正定，且 (1.3) 给
$$
\mathcal V_W\subseteq\{K=K^*: \operatorname{Tr}(\rho K)=0\}.
\tag{4.1}
$$

**引理4.1。** 若 $\rho$ 为最小秩正见证，则 (4.1) 事实上是等号，故
$$\dim_{\mathbb R}\mathcal V_W=d^2-1.$$

证明。若维数更小，以 Hilbert–Schmidt 实内积配对的正交补至少二维，且包含 $\rho$。可取不与 $\rho$ 成比例的 Hermitian 矩阵 $H$，使
$\operatorname{Tr}(HK)=0$ 对全部 $K\in\mathcal V_W$。替换为
$$H_0=H-(\operatorname{Tr}H)\rho$$
后仍非零、仍正交于 $\mathcal V_W$，且 $\operatorname{Tr}H_0=0$。

$\rho+tH_0$ 在足够小的实 $t$ 下正定。因为非零 Hermitian $H_0$ 迹为0，它有正、负特征值；沿某一实方向增大 $|t|$ 可到达正半定锥的有限边界。于是存在 $t_0\ne0$，使
$$\rho+t_0H_0\ge0,\quad \operatorname{Tr}(\rho+t_0H_0)=1,$$
且其秩小于 $d$。它仍湮灭 $\mathcal J$ 的实部和虚部，因而仍满足 (1.3)，矛盾。证毕。

这给最小见证一个具体而强的有限矩阵条件：其全部压缩理想的 Hermitian 实线性张成必须恰好是由 $\rho$ 切出的超平面。仅证明这些压缩矩阵不同时对角化仍不足够。

## 5. 为何不能直接用解析轨道移动正见证

一个自然尝试是取 $T\in\mathcal A$，将 $\rho$ 变成
$$\rho_T=T\rho T^*,$$
希望移动 $W$，再用 (3.2) 排除它。然而
$$
\operatorname{Tr}(\rho_TJ)
=\operatorname{Tr}(\rho T^*JT)
=\operatorname{Tr}(\rho T^*T J),
$$
其中第二步只用 $JT=TJ$。$T^*T$ 一般不属于 $\mathcal A$，所以 (1.3) 并不消去最后一项。

这个缺口有有限维的精确反例。取物理二维前移
$$
Ae_0=e_1,\qquad Ae_1=0,\qquad S=A,
\quad \rho=e_0\otimes e_0.
$$
则 $\rho$ 的正泛函湮灭 $S\mathbb C[I,A]$。但对 $T=I+A$，
$$
\rho_T=(e_0+e_1)\otimes(e_0+e_1),\qquad
\operatorname{Tr}(\rho_TA)=1.
$$
即使归一化迹也不恢复湮灭。这个有限维例子只否定上述一般逻辑步骤，不是本题原 Haar 算子的反例。

对应的非正变化 $T\rho$ 的确仍给湮灭泛函，因为
$\operatorname{Tr}(T\rho J)=\operatorname{Tr}(\rho JT)=0$；但它一般不是正算子，故不能直接重用 (3.2) 的正见证降秩论证。

因此，若要利用解析轨道迫最小支撑与其 $C$ 像出现更大交，还必须构造一种**确实保持正性及原主理想湮灭**的变形。普通共轭 $T\rho T^*$ 尚不具备这一步。

## 6. 剩余的有限秩问题

本文给出两条准确必要条件：

- 最小正见证支撑满足 $\dim(W\cap CW)\le1$；
- 压缩理想的 Hermitian 张成在该支撑上必须占满 $d^2-1$ 维。

这两条可以同时成立，当前没有从实际慢符号结构推出矛盾。未知零子商的 $C$ 不变性、正见证轨道的封闭性、一般 rank-one 因子分解都未在本文获得。普通 Hilbert ISP 的完成标准未改变。
