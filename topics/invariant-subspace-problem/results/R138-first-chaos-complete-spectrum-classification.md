# R138：任意平方可和第一阶闭乘子的完整谱分类

日期：2026-11-12。作者：l2_moments，独占稿；完整结果 R138。
状态：完整证明。相位缺陷判据的反向、乘积态误差及实际低头 carry 已由根代理和 critical_kernel 独立核验。本文分类的是固定实际算子的第一阶闭乘子族，不是整个 Hilbert 不变子空间问题的解答。

## 1. 分类定理

给定
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
令 $X=X_u$ 为 R125 的真实闭乘子。记
$$
\mathcal D(a,\theta)
=\sum_{j\ge0}\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)
\in[0,\infty].
\tag{1.1}
$$
每一项非负。则恰有下列三类。

**有界类。** 若 $a\in\ell^1$，则
$$
X\in\mathcal A,\qquad
\sigma(X)=\left\{a_*+\sum_j a_j\right\}.
\tag{1.2}
$$
当 $a\ne0$ 时，这唯一谱点是连续谱点：算子差单射、值域稠密而不满。若 $a=0$，则 $X=a_*I$，唯一谱点为标量点谱；这包括零标量。

**空谱类。** 若 $a\notin\ell^1$，且存在 $\theta$ 使
$\mathcal D(a,\theta)<\infty$，则
$$
\boxed{\sigma(X)=\varnothing.}
\tag{1.3}
$$
每个 $(X-\lambda I)^{-1}$ 都是有界交换子。这样的角 $\theta$ 在模 $2\pi$ 意义下唯一。

**全平面连续谱类。** 若 $a\notin\ell^1$，且对每个 $\theta$ 都有
$\mathcal D(a,\theta)=\infty$，则
$$
\boxed{\sigma(X)=\sigma_{\mathrm{ap}}(X)=\mathbb C.}
\tag{1.4}
$$
每个 $\lambda$ 都属于连续谱。更准确地，对每个 $\lambda$ 可以选有限柱单位向量 $x_m$，使
$$
x_m\rightharpoonup0,\qquad
\|(X-\lambda I)x_m\|\longrightarrow0.
\tag{1.5}
$$
因此这是关于实际定义域的显式近似谱结论。

这里“连续谱”使用单射、稠密但不满值域的通常闭算子定义；“近似谱”指存在定义域内单位向量使残差趋零。空谱对无界闭算子并不矛盾。

## 2. 已有实际接口与有界情形

R125 给出：

- $X^*=CXC$；
- 有限柱为 $X$ 及 $X^*$ 的图核心；
- 有限部分 $X_n=a_*I+\sum_{j<n}a_jV_j$ 在有限次数输入上强收敛到 $X$；
- 所有有界交换子保持 $\operatorname{Dom}X$ 并与 $X$ 域交换；
- 若第一阶向量非常数，则对每个 $\lambda$，
  $$
  \ker(X-\lambda I)=0,\qquad
  \overline{\operatorname{Ran}(X-\lambda I)}=H.
  \tag{2.1}
  $$

最后一条也直接由 R125 的每个非零第一 chaos 向量循环及 $C$ 自伴性得到。

若 $a\in\ell^1$，因 $\sup_j\|V_j\|\le6$，有限部分在算子范数中收敛，故 $X$ 是其有界极限，并属于
$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。R32 的唯一特征取 $V_j$ 为 $1$，所以 $\mathcal A$ 内谱只有
$c=a_*+\sum_j a_j$。在 $\mathcal B(H)$ 中谱包含于该单点，且有界算子的谱非空，故恰为 $\{c\}$。

若 $a\ne0$，(2.1) 给 $X-cI$ 单射、稠密值域。它不能满射，否则其逆由有界逆定理有界，与 $c$ 为谱点矛盾。若 $a=0$，直接得到纯标量情形。

反过来，R88 的精确第一阶有界乘子判据也说明：当 $a\notin\ell^1$ 时，这个闭乘子确实无界。以下两类都属于真正的无界算子。

## 3. 可和相位缺陷的空谱方向

这是 R134 §2 的结论；为使分类独立可核，重述全部关键步骤。

旋转后先令 $\theta=0$，置
$$
\delta_j=|a_j|-\operatorname{Re}a_j,\qquad
c_m=\sum_{j\ge m}(\delta_j+8|a_j|\eta_j).
$$
$\sum\delta_j<\infty$，且 $\sum|a_j|\eta_j<\infty$，故 $c_m\to0$。
物理单坐标矩阵 $S_j=I-2E_j$ 满足
$$
\operatorname{Re}(a_jS_j)\ge-\delta_jI.
$$
实际差 $\|V_j-S_j\|\le8\eta_j$ 于是给尾闭乘子
$T_m=X_{\sum_{j\ge m}a_j\chi_j}$ 的下界
$$
\operatorname{Re}\langle T_mx,x\rangle\ge-c_m\|x\|^2.
$$
有限柱图核心与 $T_m^*=CT_mC$ 将同一下界传到完整域和通常伴随。故当 $\operatorname{Re}z>c_m$ 时，$T_m+zI$ 有界可逆；证明是下界使像闭、伴随同一下界使其稠密。

写
$$
X=T_m+\beta_mI+K_m,
$$
其中
$$
\beta_m=a_*+\sum_{j<m}a_j,\qquad
K_m=\sum_{j<m}a_j(V_j-I)\in\mathcal A.
$$
$K_m$ 的常数特征为零，故拟幂零。又
$$
\operatorname{Re}\beta_m
=\operatorname{Re}a_*+\sum_{j<m}|a_j|-\sum_{j<m}\delta_j
\longrightarrow+\infty.
$$
对给定 $\lambda$ 选 $m$ 使 $\operatorname{Re}(\beta_m-\lambda)>c_m$。
置 $R=(T_m+(\beta_m-\lambda)I)^{-1}$。$R$ 属于交换子代数，与 $K_m$ 交换，故 $K_mR$ 拟幂零。于是
$$
(X-\lambda I)^{-1}=R(I+K_mR)^{-1}
$$
有界且属于 $\{A\}'$。一般 $\theta$ 对旋转算子应用同样证明。

角的唯一性也很直接。若两个不同方向 $\theta_1,\theta_2$ 的缺陷都可和，则逐项有
$$
\begin{aligned}
&\bigl(|a_j|-\operatorname{Re}(e^{-i\theta_1}a_j)\bigr)
+\bigl(|a_j|-\operatorname{Re}(e^{-i\theta_2}a_j)\bigr)\\
&\quad\ge
\left(2-\left|e^{-i\theta_1}+e^{-i\theta_2}\right|\right)|a_j|.
\end{aligned}
$$
模 $2\pi$ 不同使括号严格为正，求和与 $a\notin\ell^1$ 矛盾。

## 4. 无可和方向时的尾圆盘耗尽引理

以下为反向的几何核心。固定尾起点 $m$，定义
$$
L_{m,n}=\sum_{m\le j<n}|a_j|,
\qquad S_{m,n}=\sum_{m\le j<n}a_j,
\qquad d_{m,n}=L_{m,n}-|S_{m,n}|.
\tag{4.1}
$$
三角不等式给 $d_{m,n+1}\ge d_{m,n}$。

**引理。** 若不存在可和相位缺陷方向，则对每个固定 $m$，
$$
d_{m,n}\longrightarrow+\infty.
\tag{4.2}
$$
因此圆盘
$$
D(S_{m,n},L_{m,n})
$$
随 $n$ 最终包含任意给定复数，甚至包含任意预先指定的闭圆盘。

**证明。** 若 $d_{m,n}$ 有有界子列，则其单调性使它一直有界于某个 $C$。因为 $L_{m,n}\to\infty$，最终 $S_{m,n}\ne0$。选一个
$\theta_n=\arg S_{m,n}$ 的收敛子列，极限为 $\theta$。对每个固定 $k>m$，当 $n\ge k$ 时，
$$
\begin{aligned}
\sum_{m\le j<k}
\bigl(|a_j|-\operatorname{Re}(e^{-i\theta_n}a_j)\bigr)
&\le
\sum_{m\le j<n}
\bigl(|a_j|-\operatorname{Re}(e^{-i\theta_n}a_j)\bigr)\\
&=L_{m,n}-|S_{m,n}|\le C.
\end{aligned}
$$
先沿该子列令 $n\to\infty$，再令 $k\to\infty$，非负项单调求和得同一个方向的尾总缺陷不超过 $C$。加回有限头，得到可和方向，矛盾。故 (4.2) 成立。

最后，$D(S,L)$ 包含以零为中心、半径 $L-|S|$ 的圆盘，故第二结论立即成立。证毕。

这里不能只对每个有限段单独选择一个方向并忽略其随段变化；上述紧子列是在固定每个有限 $k$ 之后取极限，才产生同一全序列方向。

## 5. 纯尾乘积态：期望任取而残差由尾 ℓ² 控制

在物理单坐标上，
$$
S=I-2E=\begin{pmatrix}1&0\\-2&1\end{pmatrix}
$$
的数值域恰为 $D(1,1)$。事实上，对单位向量
$z=(\cos t,e^{i\phi}\sin t)$，
$\langle Ez,z\rangle$ 遍历 $D(0,1/2)$，所以
$\langle Sz,z\rangle$ 遍历该圆盘。另有 $\|S\|\le3$。

给定有限区间 $[m,n)$ 和目标
$$
z\in D(S_{m,n},L_{m,n}),
$$
可以选 $v_j\in D(1,1)$，使
$$
\sum_{m\le j<n}a_jv_j=z.
\tag{5.1}
$$
若 $L_{m,n}>0$，一个明确选择是
$$
w=\frac{z-S_{m,n}}{L_{m,n}},\qquad
v_j=1+\frac{|a_j|}{a_j}w
\quad(a_j\ne0),
$$
零系数处任意选。$|w|\le1$ 保证每个 $v_j$ 可作为某单位局部向量 $z_j$ 的期望 $\langle S_jz_j,z_j\rangle$。

取有限乘积态
$$
z_{m,n}=\bigotimes_{m\le j<n}z_j
$$
并在 $j\ge n$ 的每个位张量参考常数 $1$。参考常数满足
$S_j1=\chi_j$，因此期望为零。对每个位定义中心化残差
$$
r_j=(S_j-v_j)z_j\quad(m\le j<n),\qquad
r_j=\chi_j\quad(j\ge n).
$$
它与对应的原局部向量正交。不同位的中心化残差张量因子也因此两两正交；复系数不改变这个正交性。于是整个无限纯尾有严格估计
$$
\begin{aligned}
\left\|
\left(\sum_{j\ge m}a_jS_j-zI\right)
\left(z_{m,n}\otimes1_{\ge n}\right)
\right\|^2
&=
\sum_{m\le j<n}|a_j|^2
\bigl(\|S_jz_j\|^2-|v_j|^2\bigr)
+\sum_{j\ge n}|a_j|^2\\
&\le9\sum_{j\ge m}|a_j|^2.
\end{aligned}
\tag{5.2}
$$
所以残差不取决于圆盘半径或所选有限区间长度，只由起点之后的 $\ell^2$ 尾控制。无限参考尾已经包含在 (5.2)，没有被丢弃。

## 6. 物理全一头使真实低位进位消失

令 $p_m$ 为前 $m$ 位全部为物理 $1$ 的归一化柱向量：
$$
p_m=2^{m/2}1_{\{y\bmod 2^m=2^m-1\}}.
$$
记 $P_m$ 为到该头向量张量任意尾的正交投影。若 $j<m$，实际递归
$$
N_j=E_j+\eta_jE_j^*N_{j+1}
$$
在这些全部为 $1$ 的输入位上没有 $E_j$ 项，必须连续进位至 $m$。所以
$$
N_jP_m
=\frac{\alpha_m}{\alpha_j}
\left(E_j^*E_{j+1}^*\cdots E_{m-1}^*\right)N_mP_m,
$$
其范数为 $\alpha_m/\alpha_j$。这里低于 $j$ 的位保持不变，等式只用于上述头子空间。

由 $V_j-I=-2N_j(I+N_j)^{-1}$、$N_j$ 与该逆交换，且逆范数小于 $3$，
$$
\boxed{\|(V_j-I)P_m\|\le6\frac{\alpha_m}{\alpha_j}.}
\tag{6.1}
$$
因此，均匀地对所有该头下的单位尾向量，
$$
\begin{aligned}
\left\|\sum_{j<m}a_j(V_j-I)P_m\right\|
&\le6\sum_{j<m}|a_j|\frac{\alpha_m}{\alpha_j}\\
&\le6\sqrt m\,\|a\|_2\,\eta_{m-1}
\longrightarrow0.
\end{aligned}
\tag{6.2}
$$
最后用到 $\alpha_j\ge\alpha_{m-1}$（$j<m$）和本题超快下降的
$\eta_{m-1}=\alpha_m/\alpha_{m-1}$。这一步是实际低头的统一估计，不假设尾乘积态的最大位受到控制。

真实尾与纯尾之差同样是全空间有界的小量：
$$
\left\|\sum_{j\ge m}a_j(V_j-S_j)\right\|
\le8\sum_{j\ge m}|a_j|\eta_j
\le8\|a_{\ge m}\|_2\|\eta_{\ge m}\|_2.
\tag{6.3}
$$
该级数按算子范数收敛。

## 7. 每个复数的实际有限柱奇异序列

固定 $\lambda\in\mathbb C$。记
$$
\beta_m=a_*+\sum_{j<m}a_j.
$$
对每个 $m$，§4 允许选择某个有限 $n=n(m,\lambda)>m$，使
$$
\lambda-\beta_m\in D(S_{m,n},L_{m,n}).
$$
按 §5 选择相应尾乘积态，并令
$$
x_m=p_m\otimes z_{m,n}\otimes1_{\ge n}.
$$
这是有限柱单位向量，故属于 $X$ 的真实定义域。纯尾期望精确抵消
$\lambda-\beta_m$，所以 (5.2)、(6.2)、(6.3) 给
$$
\boxed{
\|(X-\lambda I)x_m\|
\le
6\sqrt m\,\|a\|_2\eta_{m-1}
+\bigl(3+8\|\eta_{\ge m}\|_2\bigr)\|a_{\ge m}\|_2
\longrightarrow0.
}
\tag{7.1}
$$
右端与 $\lambda$ 无关；仅有限尾区间的选择依赖 $\lambda$。

这些向量的支撑位于柱
$$
C_m=\{y:y\bmod2^m=2^m-1\},
\qquad \mu(C_m)=2^{-m}.
$$
因此对任意固定 $h\in H$，
$$
|\langle x_m,h\rangle|
\le\|1_{C_m}h\|\longrightarrow0.
$$
这证明 $x_m\rightharpoonup0$。

于是每个 $\lambda$ 都属于实际近似谱，故 $\sigma(X)=\mathbb C$。
由 R125 的 (2.1)，所有差 $X-\lambda I$ 单射且值域稠密。如果其中某个差满射，闭图定理会使其处处定义的逆有界，与 (7.1) 矛盾。因此值域处处都真小于 $H$，全部是连续谱点。

附带地，对任意有界紧算子 $K$，有 $Kx_m\to0$，所以同一个序列证明
$\sigma_{\mathrm{ap}}(X+K)=\mathbb C$。这只是一条由实际弱零序列直接得到的谱稳定性结论，没有要求 $K$ 与 $A$ 交换。

## 8. 三种情况的具体例子与使用边界

- 若 $a\in\ell^1$ 非零，例如 $a_j=2^{-j-1}$，则谱是唯一谱值
  $a_*+\sum_j a_j$，但该点不是特征向量意义的点谱，而是连续谱。
- 若 $a_j=(j+1)^{-1}$，则唯一可和缺陷方向为 $0$，闭乘子空谱。R134 给此模式任意非零点态多项式循环。
- 若 $a_j=(-1)^j/(j+1)$，则两个相反方向都具有不可和总质量，任何固定方向的缺陷都发散；故谱为整个复平面，全部连续。其系数的条件收敛和不能被当作这个无界算子的单一谱值或 $\mathcal A$ 特征。

第一阶向量本身在三种非零情况下都已由 R125 循环。谱分类的作用是确定何时存在可用于闭算子多项式的有界逆，以及何时这种方法必须失败。特别地，第三类的全平面连续谱不能被“第一阶均循环”改写为空谱。

本条没有从全平面连续谱推出非平凡闭不变子空间，也没有解决这些模式的任意点态高次多项式或一般无限秩二阶向量的循环性。
