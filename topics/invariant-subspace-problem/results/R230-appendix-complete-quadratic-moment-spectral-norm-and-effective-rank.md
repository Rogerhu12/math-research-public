# R230 附录：完整实际二次矩的谱范数与正头矩的有效秩增长

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_complex；AI 辅助：GPT-6 Astra Pro。状态：以下估计和推论完整证明；一般正常湮灭者与普通 ISP 仍未解决。

本稿接续 [实际 Cayley 选择器与稀疏 Walsh 逃逸](R230-appendix-actual-cayley-selectors-and-sparse-walsh-escape.md)。
此前的块选择器保留了整个次数层的相交组合费用。
这里直接控制所有二次系数组成的复对称矩阵的算子范数，允许全部指标相交与任意复相位。
它没有给完整二次系数平方和一个无维数费用的上界。

对真正正密度的规范头代表 $v_m$，结论为
$$
\|B_m\|_{\rm op}\le690\,\tau^{1/3}\|v_m\|^{2/3}.
$$
因此 $\|B_m\|_{\rm op}/\|v_m\|\to0$。
如果二次层仍有固定正比例，其有效秩至少按
$(\|v_m\|/\tau)^{2/3}$ 发散。
这里的秩是二次系数矩阵的秩，与原正密度的有限秩没有自动关系。

## 1. 实际设置与统一记号

在原 Haar 空间，$\Omega=1$，$\chi_F$ 为 Walsh 基，
内积对第一变量线性，
$$
C\chi_F=(-1)^{|F|}\chi_F,\qquad
B(u,v)=\langle u,Cv\rangle.
\tag{1.1}
$$
$C$ 对标量共轭。
使用实际交换算子
$$
V_j=(I-N_j)(I+N_j)^{-1}\in\mathcal A,
\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$
所需的准确性质为
$$
\operatorname{Re}V_j\ge0,\qquad
\|V_j\|<3,\qquad
V_F\Omega=\chi_F,\qquad
V_j\text{ 共同 }C\text{ 对称}.
\tag{1.2}
$$
上一完整稿已从实际 Walsh 块矩阵
$V_j=\begin{pmatrix}0&-I\\I&2K_j\end{pmatrix}$
逐式证明这些性质。

固定有限头 $[0,m)$ 时，同一证明适用于
$V_j^{[m]}\in\mathcal A_m=\mathbb C[A_{<m}]$；
下文省去上标。
纯模型不是任何估计的中间输入。

给定 $v\in H$，记
$$
V=\|v\|,\qquad
\Phi_v(R)=\langle Rv,\Omega\rangle,\qquad
K=\|\Phi_v|_{\mathcal A}\|.
\tag{1.3}
$$
有限头将代数换成 $\mathcal A_m$。
总有 $0\le K\le V$，且
$$
\Phi_v(R)=B(v,R\Omega),\qquad
B(v,\chi_F)=(-1)^{|F|}\widehat v(F).
\tag{1.4}
$$

对有限指标集 $J$ 定义复对称零对角矩阵
$$
(B_J)_{ij}=
\begin{cases}
\widehat v(\{i,j\}),&i\ne j,\\
0,&i=j.
\end{cases}
\tag{1.5}
$$
它不是 Hermitian Gram 矩阵，也不假设它半正定。

## 2. 三次实际真空列的无维数估计

令 $w_j\ge0$、$j\in J$，并令
$$
W^2=\sum_{j\in J}w_j^2,\qquad L=\sum_{j\in J}w_jV_j.
\tag{2.1}
$$
$L$ 是实际有界增生算子。
尽管其算子范数可以依赖 $\sum_jw_j$，
其前三阶真空列只需 $\ell^2$ 权。

一次列是 $L\Omega=\sum_jw_j\chi_j$。
上一稿已证明
$$
\|L^2\Omega\|\le(3+\sqrt2)W^2<5W^2.
\tag{2.2}
$$
这里单独证明本稿需要的三次估计。
按下标重数准确展开，
$$
L^3\Omega
=\sum_jw_j^3V_j^3\Omega
+3\sum_jw_j^2V_j^2
       \left(\sum_{k\ne j}w_kV_k\Omega\right)
+6\sum_{i<j<k}w_iw_jw_k\chi_{\{i,j,k\}}.
\tag{2.3}
$$
所有实际 $V_j$ 交换，所以此重排合法；没有交换实际和纯因子。

第一项满足
$$
\left\|\sum_jw_j^3V_j^3\Omega\right\|
\le9\sum_jw_j^3\le9W^3,
\tag{2.4}
$$
因为 $V_j^3\Omega=V_j^2\chi_j$。
第二项先固定重复下标 $j$，使用
$$
\left\|\sum_{k\ne j}w_kV_k\Omega\right\|
=\left(\sum_{k\ne j}w_k^2\right)^{1/2}\le W
$$
以及 $\|V_j^2\|\le9$，得到上界 $27W^3$。
这一步对不同 $j$ 只用三角不等式。

第三项的完整 Walsh 列彼此正交，故其范数至多
$$
6\left(\sum_{i<j<k}w_i^2w_j^2w_k^2\right)^{1/2}
\le\sqrt6\,W^3.
\tag{2.5}
$$
合并即得
$$
\boxed{\|L^3\Omega\|\le(36+\sqrt6)W^3<40W^3.}
\tag{2.6}
$$
允许重复下标列携带任意实际尾项；估计已经使用完整 $H$ 范数。

## 3. 两个实际收缩消去一次项

对 $t>0$ 定义
$$
E_t=(I+tL)^{-1},\qquad
T_t=tL(I+tL)^{-1}=I-E_t.
\tag{3.1}
$$
增生性给 $\|E_t\|\le1$。
Cayley 变换 $(I-tL)(I+tL)^{-1}$ 是收缩，因此
$\|T_t\|\le1$。
此外
$$
E_t=\int_0^\infty e^{-s}e^{-stL}\,ds\in\mathcal A;
$$
这里积分在算子范数中收敛。
有限头中也成立。

准确到三阶的恒等式为
$$
T_t\Omega
=tL\Omega-t^2L^2\Omega+t^3E_tL^3\Omega.
\tag{3.2}
$$
置
$$
U_t=T_t-2T_{t/2},\qquad \|U_t\|\le3.
\tag{3.3}
$$
于是
$$
U_t\Omega
=-\frac{t^2}{2}L^2\Omega
+t^3\left(E_t-\frac14E_{t/2}\right)L^3\Omega.
\tag{3.4}
$$
以下将 $W$ 归一化为 $1$。
由 (2.6)，余项范数至多 $50t^3$。
用 (1.4) 配对并保留全部其他次数，
$$
\frac{t^2}{2}|\Phi_v(L^2)|
\le3K+50t^3V.
\tag{3.5}
$$
因此
$$
|\Phi_v(L^2)|\le\frac{6K}{t^2}+100tV.
\tag{3.6}
$$

若 $K>0$，取 $t=(K/V)^{1/3}$，得到
$$
\boxed{|\Phi_v(L^2)|\le106\,K^{1/3}V^{2/3}.}
\tag{3.7}
$$
若 $K=0$，该结论直接由 $\Phi_v|_{\mathcal A}=0$ 成立。
$v=0$ 也无需另行选取 $t$。

## 4. 保留全部二次系数与准确对角扣除

真实列恒等式为
$$
L^2\Omega
=\sum_jw_j^2V_j^2\Omega+
2\sum_{i<j}w_iw_j\chi_{\{i,j\}}.
$$
所以
$$
w^\top B_Jw
=\Phi_v(L^2)-\sum_jw_j^2\Phi_v(V_j^2).
\tag{4.1}
$$
第二项的绝对值至多 $9K$，因为
$\sum_jw_j^2=1$、$\|V_j^2\|\le9$。
由 $K\le V$，(3.7) 给
$$
\boxed{
|w^\top B_Jw|
\le115\,K^{1/3}V^{2/3}
\quad(w\ge0,\ \|w\|_2=1).}
\tag{4.2}
$$
这不是用纯 $D_j^2$ 代替 $V_j^2$；
实际重复下标的对角项由 $\Phi_v$ 的真实算子范数界直接支付。
因此没有丢失 carry，也没有需要趋零的比较误差。

## 5. 从正权到整个复对称矩阵

设一个复对称矩阵 $B$ 满足
$$
|w^\top Bw|\le M\|w\|_2^2\quad(w\text{ 为非负实向量}).
\tag{5.1}
$$
任意实向量 $x=x_+-x_-$，其中 $x_+,x_-$ 非负且正交。
令 $q(x)=x^\top Bx$，则
$$
q(x)=2q(x_+)+2q(x_-)-q(x_++x_-).
$$
故
$$
|x^\top Bx|\le3M\|x\|_2^2.
\tag{5.2}
$$

把 $B=B_{\rm r}+iB_{\rm i}$ 写成两个实对称矩阵。
(5.2) 分别控制二者的实二次型，有限维自伴谱定理给
$$
\|B_{\rm r}\|_{\rm op}\le3M,\qquad
\|B_{\rm i}\|_{\rm op}\le3M.
$$
因此
$$
\|B\|_{\rm op}\le6M.
\tag{5.3}
$$
没有要求所有系数属于同一个象限。

将 (4.2) 代入，
$$
\boxed{\|B_J\|_{\rm op}\le690\,K^{1/3}\|v\|^{2/3}.}
\tag{5.4}
$$
常数与 $J$ 的大小、位置及全部复相位无关。
这覆盖该指标集上完整的二次矩阵，允许每一对指标都出现。

若希望保留实际对角矩，定义
$$
(M_J)_{ij}=\Phi_v(V_iV_j).
$$
其非对角恰为 $B_J$，对角绝对值至多 $9K$。
所以还得到
$$
\boxed{\|M_J\|_{\rm op}\le699\,K^{1/3}\|v\|^{2/3}.}
\tag{5.5}
$$
不过 $M_J$ 的对角 Hilbert--Schmidt 范数不代表二次 Walsh 层；
下节的有效秩始终用于零对角 $B_J$。

## 6. 真正正密度头矩的应用

令 $\rho\ge0$ 为迹类，$\tau=\operatorname{Tr}\rho>0$，
$\varphi(R)=\operatorname{Tr}(\rho R)$。
准确规范头代表为
$$
v_m=\sum_{F\subset[0,m)}
(-1)^{|F|}\varphi(V_F^{[m]})\chi_F.
\tag{6.1}
$$
[规范头矩完整证明](R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)
及上一选择器稿已证明
$$
\Phi_{v_m}(R)=\varphi(R)\ (R\in\mathcal A_m),\qquad
K_m(v_m)=\tau,\qquad
\langle v_m,\Omega\rangle=\tau.
\tag{6.2}
$$
正性在整个 $B(H)$ 上付清 $K_m(v_m)=\tau$。
不把有限头算子冒充实际交换子以使用湮灭条件。

若 $S\in\mathcal A$ 在全 $H$ 单射，并且
$\varphi(S\{A\}')=0$，上述完整结果已支付
$$
\|A-A_{<m}\|\le d_0\prod_{j<m}\eta_j,\qquad
\|v_m\|\le10^{m/2}\tau,
$$
故固定多项式配对误差趋零。
由固定真空分解与 $S$ 单射性，遂有
$$
V_m:=\|v_m\|\longrightarrow\infty,\qquad
v_m/V_m\rightharpoonup0.
\tag{6.3}
$$
这里只引用这项已有实际域与 carry 结论，不假设任何更快的增长率。

令 $B_m$ 是 (1.5) 的完整 $m$ 阶矩阵。
从 (5.4) 得
$$
\boxed{
\frac{\|B_m\|_{\rm op}}{V_m}
\le690\left(\frac{\tau}{V_m}\right)^{1/3}
\longrightarrow0.}
\tag{6.4}
$$
实际全二阶矩 $M_m$ 也满足同一极限，由 (5.5) 即得。

### 6.1 所有低秩矩阵部分的统一消失

对任意秩至多 $r_m$ 的正交投影 $Q_m$，即使它随 $\rho$ 与 $m$ 变化，
$$
\|Q_mB_m\|_{\rm HS}^2
\le r_m\|B_m\|_{\rm op}^2
\le690^2r_m\tau^{2/3}V_m^{4/3}.
\tag{6.5}
$$
因此只要
$$
r_m=o((V_m/\tau)^{2/3}),
\tag{6.6}
$$
就有 $\|Q_mB_m\|_{\rm HS}/V_m\to0$。
右乘正交投影同理。
特别，固定秩的密集二次部分不能承载归一化头矩的固定正比例。

### 6.2 若二次层保留比例，其有效秩必须增长

准确有
$$
\|B_m\|_{\rm HS}^2=2\|P_2v_m\|^2.
\tag{6.7}
$$
当 $B_m\ne0$ 时定义有效秩
$$
r_{\rm eff}(B_m)=
\frac{\|B_m\|_{\rm HS}^2}{\|B_m\|_{\rm op}^2}.
$$
若某些 $m$ 上
$\|P_2v_m\|\ge\delta V_m$，$\delta>0$ 固定，则
$$
\boxed{
r_{\rm eff}(B_m)
\ge
\frac{2\delta^2}{690^2}
\left(\frac{V_m}{\tau}\right)^{2/3}.}
\tag{6.8}
$$
由于 $r_{\rm eff}(B_m)\le\operatorname{rank}B_m\le m$，
也得到这一集中情形下的必要上界
$$
V_m/\tau\le
\left(\frac{690^2m}{2\delta^2}\right)^{3/2}.
\tag{6.9}
$$
(6.9) 的增长上界本身弱于上一稿用完整二次组合费用得到的对应线性上界；
本稿新增的是完整矩阵的谱范数以及 (6.5)--(6.8) 的秩结构。

原 $\rho$ 具有有限秩，不会自动给出 $\operatorname{rank}B_m$ 的统一上界。
矩阵条目仍由随 $j$ 变化的 $H$ 中向量 $V_jf_i$ 与 $V_j^*f_i$ 配对产生，
这些向量的张成维数可随 $m$ 增长。
因此 (6.8) 还不是对有限秩正常湮灭者的矛盾。

## 7. 尚未消去的密集高秩部分

本稿用两个实际 Cayley 收缩消去一次项，以完整三次真空列支付余项。
它没有把算子范数误当 Hilbert--Schmidt 范数，也没有把原密度秩替换为二次矩阵秩。

结合上一稿，真实正头矩必须离开一次层、所有有界大小且相交费用受控的单项族，
以及本稿刻画的低秩二次矩阵部分。
仍可能保留的二次部分必须既具有越来越高的相交复杂度，又具有越来越高的有效秩；
一般更高次数的重叠部分也未关闭。

还需要利用原正密度、真 $S$ 湮灭关系或共同域结构给出新的预算。
本稿没有证明一般正常正湮灭者不存在，也没有达到普通 ISP 的完成标准。
