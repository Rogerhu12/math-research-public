# R230 附录：实际平方选择器与正密度矩的稀疏 Walsh 质量逃逸

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c017065；主会话全文复核，central_review 独立核一次80界及实际不交块增生构造。状态：以下各命题为完整证明；普通 ISP、一般正常正湮灭者及一般交叠高次矩仍未解决。

本稿加强 [一次可观测性与规范正头矩](R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)。
新估计直接使用实际增生算子，不先把测试换成纯模型。
对任意向量 $v$，一次层的平方范数至多是 $80\|v\|$ 乘对应泛函范数。
因此真正正湮灭态的规范头矩归一化以后，整个一次层趋于零；旧 $1/73$ 高次比例是其较弱推论。

同一优化可用于任意互不相交、大小有统一上界的 Walsh 单项族，继而用于具有给定相交着色数的任意族。
本稿不把这一范围扩大为所有交叠次数层：完整 $k$ 次层仍有明确组合费用。

## 1. 同时适用于实际模型与有限头的记号

在原 Haar 空间 $H$ 上，$\Omega=1$，Walsh 基为 $\chi_F$。
内积对第一变量线性，并令
$$
C\chi_F=(-1)^{|F|}\chi_F,\qquad
B(u,v)=\langle u,Cv\rangle.
\tag{1.1}
$$
$C$ 对标量共轭。
实际算子
$$
N_j=E_j+\eta_j E_j^*N_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j},
\qquad
V_j=(I-N_j)(I+N_j)^{-1}
\tag{1.2}
$$
属于 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$，两两交换且 $C$ 对称。
其准确真空列为
$$
V_F\Omega=\chi_F
\quad(F\text{ 有限}).
\tag{1.3}
$$

也可固定有限头 $[0,m)$，令 $N_m^{[m]}=0$，向下使用同一递推定义 $N_j^{[m]}$、$V_j^{[m]}$。
此时用 $\mathcal A_m=\mathbb C[A_{<m}]$ 及该有限头的空间、反射共轭、真空替代相应对象，且只取 $j<m$。
本稿的选择器证明在这两个模型中逐式相同。
为免重复，在选择器各节把上标 $[m]$ 暂时省去。

对于 $v$ 定义
$$
\Phi_v(R)=\langle Rv,\Omega\rangle,\qquad
K(v)=\sup_{\substack{R\in\mathcal A\\\|R\|\le1}}
|\Phi_v(R)|,\qquad V=\|v\|.
\tag{1.4}
$$
有限头使用同一定义但把 $\mathcal A$ 换成 $\mathcal A_m$。
当然 $0\le K(v)\le V$。
共同 $C$ 对称性准确给
$$
\Phi_v(R)=B(v,R\Omega).
\tag{1.5}
$$
若 $\widehat v(F)=\langle v,\chi_F\rangle$，则
$$
B(v,a\chi_F)=(-1)^{|F|}a\,\widehat v(F).
\tag{1.6}
$$
这里没有多加复共轭。

## 2. 实际增生性、局部共同真空与收缩测试

### 2.1 单个位的准确块矩阵

在第 $j$ 位的 Walsh 基 $(\Omega_j,\chi_j)$ 中，令 $n_j$ 为投影到 $\chi_j$ 的局部数目投影。
由 (1.2) 直接计算
$$
V_j=
\begin{pmatrix}
0&-I\\
I&2K_j
\end{pmatrix},
\qquad
K_j=(I+\eta_jN_{j+1})(I-\eta_jN_{j+1})^{-1}.
\tag{2.1}
$$
低于 $j$ 的位上为恒等。
有限头同式成立，尾端使用 $N_m^{[m]}=0$。

因为 $\|N_{j+1}\|\le1$，
$$
\operatorname{Re}K_j
=(I-\eta_jN_{j+1}^*)^{-1}
(I-\eta_j^2N_{j+1}^*N_{j+1})
(I-\eta_jN_{j+1})^{-1}
\ge\frac{1-\eta_j}{1+\eta_j}I.
\tag{2.2}
$$
于是
$$
\operatorname{Re}V_j
\ge2\frac{1-\eta_j}{1+\eta_j}n_j
\ge n_j\ge0.
\tag{2.3}
$$
同时，纯矩阵 $D_j=\begin{pmatrix}0&-1\\1&2\end{pmatrix}$ 的范数为 $1+\sqrt2$。
由
$\|K_j-I\|\le2\eta_j/(1-\eta_j)$ 及 $\eta_j<1/16$，
$$
\|V_j\|\le1+\sqrt2+\frac{4\eta_j}{1-\eta_j}<3.
\tag{2.4}
$$

更重要的是，(2.1) 对任意其余位向量 $h$ 给
$$
V_j(\Omega_j\otimes h)=\chi_j\otimes h,\qquad
V_j^*(\Omega_j\otimes h)=-\chi_j\otimes h.
\tag{2.5}
$$
不是只在全空间真空上成立。

### 2.2 有限块的准确增生修正

令 $B$ 是任意有限位集，$b=|B|\ge2$。
用 $P_B^0$ 表示这些位全为 Walsh 真空的投影，其余位不受限制。
依次使用 (2.5)，得到
$$
V_B(\Omega_B\otimes h)=\chi_B\otimes h,\qquad
V_B^*(\Omega_B\otimes h)=(-1)^b\chi_B\otimes h.
\tag{2.6}
$$
这些公式不要求 $B$ 连续。

置
$$
\sigma_B=
\begin{cases}
1,&b\text{ 为奇数},\\
i,&b\text{ 为偶数}.
\end{cases}
\tag{2.7}
$$
自伴算子 $H_B=\operatorname{Re}(\sigma_B V_B)$ 准确杀掉 $\operatorname{Ran}P_B^0$。
所以
$$
H_B=(I-P_B^0)H_B(I-P_B^0),\qquad
\|H_B\|\le3^b.
\tag{2.8}
$$

固定整数 $d\ge2$，取
$$
\epsilon_d=\frac1{2\,3^d},\qquad 2\le |B|\le d,\qquad
L_B^\pm=\sum_{j\in B}V_j\ \pm\epsilon_d\sigma_BV_B.
\tag{2.9}
$$
由于 $\sum_{j\in B}n_j\ge I-P_B^0$，(2.3) 与 (2.8) 给
$$
\boxed{\operatorname{Re}L_B^\pm
\ge(1-\epsilon_d3^b)(I-P_B^0)
\ge\frac12(I-P_B^0)\ge0.}
\tag{2.10}
$$
此外
$$
\|L_B^\pm\|\le3d+1,\qquad
q_B^\pm:=L_B^\pm\Omega
=\sum_{j\in B}\chi_j\pm\epsilon_d\sigma_B\chi_B,
\tag{2.11}
$$
$$
\langle q_B^\pm,\Omega\rangle=0,\qquad
\|q_B^\pm\|^2=b+\epsilon_d^2\le d+1.
\tag{2.12}
$$
$b\ge2$ 保证目标单项不与一次项重合。

### 2.3 实际收缩及准确二阶余项

若 $L\in\mathcal A$ 有界增生，$t>0$，则
$$
R_t=(I-tL)(I+tL)^{-1},\qquad
T_t=\frac{I-R_t}{2}=tL(I+tL)^{-1}
\tag{2.13}
$$
都是范数至多 $1$ 的算子。
其中 $\|(I+tL)^{-1}\|\le1$，而
$$
I-R_t^*R_t
=4t(I+tL^*)^{-1}\operatorname{Re}L(I+tL)^{-1}\ge0.
$$
$T_t$ 的范数界也由 $(I-R_t)/2$ 直接得到。

这里的逆仍在 $\mathcal A$ 内。确切地，
$$
(I+tL)^{-1}=\int_0^\infty e^{-s}e^{-stL}\,ds;
\tag{2.14}
$$
增生性给 $\|e^{-stL}\|\le1$，积分在算子范数中收敛，每个指数都在 $\mathcal A$。
有限头同理。
不需要额外假设该代数对所有有界逆都封闭。

准确恒等式为
$$
T_t\Omega=tL\Omega-t^2(I+tL)^{-1}L^2\Omega.
\tag{2.15}
$$
因而
$$
|\Phi_v(T_t)-tB(v,L\Omega)|
\le t^2V\,\|L^2\Omega\|.
\tag{2.16}
$$

## 3. 一次层的平方估计

令 $J$ 为任意有限位集，并记
$$
b_j=\widehat v(\{j\}),\qquad B_1^2=\sum_{j\in J}|b_j|^2.
$$
若 $B_1=0$ 则结论显然。
从 $(\operatorname{Re}b_j)_+$、
$(-\operatorname{Re}b_j)_+$、
$(\operatorname{Im}b_j)_+$、
$(-\operatorname{Im}b_j)_+$ 四个非负向量中，选择平方范数最大的一个，记为 $w$。
令 $W^2=\sum_jw_j^2$，则
$$
W\ge\frac{B_1}{2},\qquad
\left|\sum_j b_jw_j\right|\ge W^2.
\tag{3.1}
$$

实际算子 $L=\sum_jw_jV_j$ 增生，且 $L\Omega=\sum_jw_j\chi_j$。
其二次列展开为
$$
L^2\Omega=\sum_jw_j^2V_j^2\Omega+
2\sum_{j<k}w_jw_k\chi_{\{j,k\}}.
\tag{3.2}
$$
第一项用 $\|V_j^2\Omega\|=\|V_j\chi_j\|\le3$；第二项使用完整正交 Walsh 列。因此
$$
\|L^2\Omega\|
\le3W^2+
2\left(\sum_{j<k}w_j^2w_k^2\right)^{1/2}
\le(3+\sqrt2)W^2<5W^2.
\tag{3.3}
$$
没有把不同位的对角 carry 项说成正交。

若 $V>0$，取 $t=(10V)^{-1}$。
由 (1.6)、(3.1)、(2.16) 及 $\|T_t\|\le1$，
$$
tW^2\le K(v)+5t^2VW^2.
$$
故
$$
\boxed{\sum_{j\in J}|\widehat v(\{j\})|^2
\le80K(v)\|v\|.}
\tag{3.4}
$$
全空间中令有限 $J$ 递增即可得到
$$
\boxed{\|P_1v\|^2\le80K(v)\|v\|.}
\tag{3.5}
$$
$V=0$ 时结论也成立。
这是对任意 $v$ 的估计，不要求它的其他次数系数为零。

## 4. 任意不交有界大小块的平方估计

令 $\mathcal B$ 是有限的两两不交位集族，且
$2\le |B|\le d$。
记
$$
B_{\mathcal B}^2=\sum_{B\in\mathcal B}|\widehat v(B)|^2,
\qquad
c_B=(-1)^{|B|}\sigma_B\widehat v(B).
\tag{4.1}
$$
对 $c_B$ 作与 (3.1) 相同的四象限选择，得到 $w_B\ge0$，
$$
W^2=\sum_Bw_B^2\ge B_{\mathcal B}^2/4,\qquad
\left|\sum_Bw_Bc_B\right|\ge W^2.
\tag{4.2}
$$

定义两个实际增生算子
$$
L^\pm=\sum_{B\in\mathcal B}w_BL_B^\pm.
\tag{4.3}
$$
若 $B\ne D$，两个 Walsh 指标集不交，(1.3) 给准确恒等式；这里并不把带实际 carry 的算子当成局部矩阵：
$$
L_B^\pm L_D^\pm\Omega=q_B^\pm q_D^\pm.
\tag{4.4}
$$
右侧为普通有限 Walsh 多项式乘积；每个展开项在 $B$、$D$ 中均非空。
不同无序块对的这些列两两正交。
因此
$$
\begin{aligned}
\|(L^\pm)^2\Omega\|
&\le\sum_Bw_B^2\|L_B^\pm q_B^\pm\|
 +2\left(\sum_{B<D}w_B^2w_D^2
       \|q_B^\pm\|^2\|q_D^\pm\|^2\right)^{1/2}\\
&\le\bigl[(3d+1)\sqrt{d+1}+\sqrt2(d+1)\bigr]W^2\\
&\le M_dW^2,\qquad M_d=4(d+1)^{3/2}.
\end{aligned}
\tag{4.5}
$$
第一项仍仅用三角不等式，允许无限实际 carry。

设
$$
u=\sum_Bw_B\sum_{j\in B}\chi_j,\qquad
z=\sum_Bw_B\sigma_B\chi_B.
$$
则 $L^\pm\Omega=u\pm\epsilon_d z$。
无论 $v$ 的一次系数怎样，
$$
\max\{|B(v,u+\epsilon_dz)|,\ |B(v,u-\epsilon_dz)|\}
\ge\epsilon_d|B(v,z)|\ge\epsilon_d W^2.
\tag{4.6}
$$
这一步是消除一次污染的两个实际测试，不把污染设为零。

选择达到该下界的符号，并取
$$
t=\frac{\epsilon_d}{2M_dV}.
\tag{4.7}
$$
(2.16)、(4.5) 给
$$
K(v)\ge
t\epsilon_dW^2-t^2VM_dW^2
=\frac{\epsilon_d^2W^2}{4M_dV}.
$$
故
$$
\boxed{
\sum_{B\in\mathcal B}|\widehat v(B)|^2
\le A_dK(v)\|v\|,
\qquad
A_d=\frac{16M_d}{\epsilon_d^2}
=256\,9^d(d+1)^{3/2}.}
\tag{4.8}
$$
常数只依赖大小上界 $d$，与块数、位置、间隔、系数相位及其他次数无关。
无限不交族由有限子族取极限。
允许同一族混合奇偶大小，因为 (4.1) 已准确处理相应相位。

## 5. 明确支付交叠：着色与完整次数层

### 5.1 给定相交着色数的任意族

若有限单项族 $\mathcal F$ 满足 $2\le|F|\le d$，并能分成 $h$ 个两两不交族，则由 (4.8) 相加，
$$
\boxed{\|P_{\mathcal F}v\|^2
\le hA_dK(v)\|v\|.}
\tag{5.1}
$$
这不要求周期、等间隔或相同块大小。

若每个位属于至多 $\Delta$ 个集合，则每个集合与至多
$d(\Delta-1)$ 个其他集合相交。
按任意次序贪心着色，至多
$$
h=d(\Delta-1)+1
\tag{5.2}
$$
种颜色足够。故 (5.1) 在这个明确费用下成立。

### 5.2 全部 $k$ 次系数的组合费用

固定有限头的 $m$ 个位与 $2\le k\le m$。
随机均匀排列这些位，按顺序取前 $\lfloor m/k\rfloor$ 个完整 $k$ 位块。
每次得到一个不交族；由对称性，每个 $k$ 元集合被选中的概率准确是
$$
\frac{\lfloor m/k\rfloor}{\binom mk}.
$$
对 (4.8) 取平均得到
$$
\boxed{
\|P_kv\|^2
\le A_k\,\frac{\binom mk}{\lfloor m/k\rfloor}\,
K(v)\|v\|.}
\tag{5.3}
$$
若 $m\ge2k$，组合因子至多
$2\binom{m-1}{k-1}$。
这是实际完整次数层的费用；本稿不删除它。

## 6. 真正正密度的规范头矩

令 $\rho\ge0$ 为迹类，$\tau=\operatorname{Tr}\rho>0$，
$\varphi(R)=\operatorname{Tr}(\rho R)$。
定义准确有限头代表
$$
v_m=\sum_{F\subset[0,m)}
(-1)^{|F|}\varphi(V_F^{[m]})\chi_F.
\tag{6.1}
$$
有限头的 $A_{<m}$ 是全部相邻权非零的一个 $2^m$ 阶幂零 Jordan 链，故 $\dim\mathcal A_m=2^m$。
$V_F^{[m]}\Omega=\chi_F$ 说明这些 $2^m$ 个算子线性无关，因而构成其基。
由 (1.6) 与 (6.1) 先在这一基上直接核对，再线性延拓，得到
$$
\langle Rv_m,\Omega\rangle=\varphi(R)
\quad(R\in\mathcal A_m),\qquad
\langle v_m,\Omega\rangle=\tau,\qquad
K_m(v_m)=\tau.
\tag{6.2}
$$
最后一式只用 $\varphi$ 在整个 $B(H)$ 上的正性及 $I\in\mathcal A_m$；
有限头测试不必属于实际交换子代数。

为使本稿的真湮灭接口完整，重述其必要预算。
设 $S\in\mathcal A$ 在全 $H$ 单射，且
$$
\varphi(SR)=0\quad(R\in\{A\}').
\tag{6.3}
$$
实际头差为
$$
\|A-A_{<m}\|\le a_m^{\rm car}
=d_0\prod_{j<m}\eta_j
\le d_0\exp[-(770/15)(16^m-1)].
\tag{6.4}
$$
同时 $\|v_m\|\le10^{m/2}\tau$。
因此对每个固定多项式 $p$，
$$
|\varphi(p(A))-\langle p(A)v_m,\Omega\rangle|
\le L_p\,a_m^{\rm car}(\tau+\|v_m\|)\longrightarrow0,
\tag{6.5}
$$
其中 $L_p$ 为固定多项式的通常望远镜常数。

若 $(v_m)$ 有有界子列，则取弱极限 $v$。
(6.5) 先在固定多项式上给
$\varphi(p(A))=\langle p(A)v,\Omega\rangle$，
再由范数连续性扩展到 $\mathcal A$。
使用 (6.3) 的 $R=A^n$、$S\in\mathcal A$、共同 $C$ 对称性与 $\Omega$ 循环，得到 $Sv=0$。
单射性给 $v=0$，却与 $\langle v,\Omega\rangle=\tau$ 矛盾。
于是
$$
\|v_m\|\longrightarrow\infty.
\tag{6.6}
$$
同一固定多项式配对及 (6.5) 除以 $\|v_m\|$ 给
$v_m/\|v_m\|\rightharpoonup0$。
这里先固定多项式，未给 $S$ 本身假造快速有限头误差。

### 6.1 一次层全部消失

把 (3.5) 用于真实正头代表，
$$
\boxed{\|P_1v_m\|^2\le80\tau\|v_m\|.}
\tag{6.7}
$$
结合真空锚与 (6.6)，
$$
\boxed{
\frac{\|P_{\le1}v_m\|^2}{\|v_m\|^2}
\le\frac{\tau^2}{\|v_m\|^2}
+\frac{80\tau}{\|v_m\|}
\longrightarrow0.}
\tag{6.8}
$$
所以
$$
\frac{\|P_{\ge2}v_m\|}{\|v_m\|}\longrightarrow1.
\tag{6.9}
$$
这加强了先前的固定 $1/73$ 下界。

### 6.2 任意变化不交块族与稀疏族

任意选择 $\mathcal B_m\subset 2^{[0,m)}$，
只要每个 $\mathcal B_m$ 两两不交且 $2\le |B|\le d$，同一个常数给
$$
\boxed{
\frac{\|P_{\mathcal B_m}v_m\|^2}{\|v_m\|^2}
\le\frac{A_d\tau}{\|v_m\|}\longrightarrow0.}
\tag{6.10}
$$
族可依赖 $\rho$、$v_m$ 与 $m$。
因此固定大小的不交高次块也不能承载归一化头矩的固定正比例。

若族能分成 $h_m$ 个不交子族，则右侧改为
$A_dh_m\tau/\|v_m\|$。
特别，若相交次数有统一上界，结论仍成立；
更一般地，只要
$$
A_{d_m}h_m\tau=o(\|v_m\|),
\tag{6.11}
$$
也可让块大小与颜色数随 $m$ 增长。

这也给一个必要的集中费用：
若某族上的投影至少为 $\delta\|v_m\|$，则
$$
h_m\ge\frac{\delta^2\|v_m\|}{A_d\tau}.
\tag{6.12}
$$
不是说所有高次质量必须处于单一高次数，而是它不能继续集中在费用有界的这些族内。

### 6.3 完整低次数的准确条件

由 (5.3)，对固定 $d$，
$$
\|P_{\le d}v_m\|^2
\le\tau^2+
\tau\|v_m\|
\left[80+\sum_{k=2}^d
A_k\frac{\binom mk}{\lfloor m/k\rfloor}\right]
\quad(m\ge d).
\tag{6.13}
$$
方括号为 $O_d(m^{d-1})$。
因此若另有
$$
\|v_m\|/m^{d-1}\longrightarrow\infty,
\tag{6.14}
$$
则整个不超过 $d$ 的次数部分归一化后消失。
本稿没有证明 (6.14)，也不把单纯的 (6.6) 替换为它。

## 7. 与实际全行擦除代表的接合

对有限秩正见证 $\rho=\sum_{i=1}^rf_i\otimes f_i$，
[纯远尾源擦除](R230-appendix-pure-tail-source-erasure-and-carry-controlled-aggregate-growth.md)
与先前头矩稿给出了明确实际代表
$$
\widetilde v_m=\sum_{F\subset[0,m)}\sum_{i=1}^r
V_F W_{F,i}f_i,
\tag{7.1}
$$
其中 $Cf_i=\sum_F\chi_F\otimes z_{F,i}$，
$$
W_{F,i}
=I_{<m}\otimes
|\Omega_{\ge m}\rangle\langle C_{\ge m}z_{F,i}|.
$$
准确有限头替换是 $v_m$，且已支付
$$
\|\widetilde v_m-v_m\|
\le6m\,\eta_{m-1}\,10^{m/2}\tau\longrightarrow0.
\tag{7.2}
$$
因此 (6.8)、(6.10)、满足 (6.11) 时的结论，也适用于
$\widetilde v_m/\|\widetilde v_m\|$。
理由只需各 Walsh 投影范数为 $1$，所以即使投影族随 $m$ 变化，(7.2) 的误差仍统一趋零。
不把实际 $\widetilde v_m$ 说成严格有限柱。

## 8. 范围与剩余接口

本稿的测试全部是实际 $\mathcal A$ 中的收缩，或者有限头代数中的准确收缩。
增生性、两种奇偶相位、所有二次列及实际 carry 均保留。
选择器的观测用真正正密度的范数 $\tau$；没有以一个固定非湮灭态代替当前见证。

新结论迫使规范正头矩完全离开一次层，并离开任意有界大小、有界相交费用的 Walsh 单项族。
一般密集交叠的高次矩仍受 (5.3) 的组合费用约束。
它没有给 $v_m$ 的多项式以上增长率，也没有给见证专属 $S$ 理想内强单位、原共同域上界或秩一分解。
普通 ISP 的完成标准仍未达到。
