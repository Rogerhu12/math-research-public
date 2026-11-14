# R230 附录：所有固定阶实际矩张量与注入范数

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。central_review 与 normal_complex 独立核查真空列、有限差分、极化及去重复步骤。
状态：以下固定阶界已证明；一般正常湮灭者、完整高次平方和与普通 ISP 仍开。

本稿接续[实际平方选择器](R230-appendix-actual-cayley-selectors-and-sparse-walsh-escape.md)和[完整二次矩谱范数](R230-appendix-complete-quadratic-moment-spectral-norm-and-effective-rank.md)。
新增的是任意固定阶、允许全部指标交叠的实际矩多线性界。它控制与单位纯张量的全部配对，不把这个范数换成完整系数平方和。

## 1. 实际代数、转置和张量范数

在原 Haar 空间取真空 $\Omega$ 和 Walsh 基 $\chi_F$。
内积对第一变量线性，$C$ 为原共轭，
$$
C\Omega=\Omega,\qquad C\chi_F=(-1)^{|F|}\chi_F.
$$
对标量 $C$ 是反线性的。记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
V_j=(I-N_j)(I+N_j)^{-1}\in\mathcal A.
$$
前稿由准确实际 Walsh 块矩阵已证明
$$
\operatorname{Re}V_j\ge0,\qquad \|V_j\|\le3,\qquad
V_F\Omega=\chi_F\quad(F\text{ 无重复}),\qquad
CV_j^*C=V_j.
\tag{1.1}
$$
全部 $V_j$ 交换。有限头 $V_j^{[m]}$、$\mathcal A_m=\mathbb C[A_{<m}]$ 也有同样性质；以下两种情形使用同一证明。

固定 $v\in H$，置
$$
V=\|v\|,\qquad
\Phi_v(R)=\langle Rv,\Omega\rangle,\qquad
K=\|\Phi_v|_{\mathcal A}\|\le V.
\tag{1.2}
$$
有限头时用 $\mathcal A_m$。因为每个 $R\in\mathcal A$ 都是 $C$ 对称，
$$
\Phi_v(R)=B(v,R\Omega),\qquad
B(u,z)=\langle u,Cz\rangle.
\tag{1.3}
$$
这正是以下真空列误差能与 $v$ 配对的依据。特别，
$$
\Phi_v(V_F)=(-1)^{|F|}\widehat v(F).
\tag{1.4}
$$

对有限指标集 $J$ 和 $k\ge1$，定义有序 $k$ 阶张量
$$
(T_{k,J}(v))_{i_1,\ldots,i_k}=
\begin{cases}
\widehat v(\{i_1,\ldots,i_k\}),&i_1,\ldots,i_k\text{ 两两不同},\\
0,&\text{否则}.
\end{cases}
\tag{1.5}
$$
使用注入范数
$$
\|T\|_\varepsilon=
\sup_{\|w_1\|_2,\ldots,\|w_k\|_2\le1}
\left|\sum_{i_1,\ldots,i_k}T_{i_1,\ldots,i_k}
                 \prod_{\nu=1}^k w_\nu(i_\nu)\right|.
\tag{1.6}
$$
这里允许任意复 $w_\nu$；将配对改成 Hilbert 内积只会对这些测试向量取共轭，范数不变。

**主结论。** 对每个固定 $k$，有下面明确给出的有限常数 $\Lambda_k$，与 $J$ 的大小、位置及复相位无关，使
$$
\boxed{\|T_{k,J}(v)\|_\varepsilon
\le\Lambda_k K^{1/(k+1)}V^{k/(k+1)}.}
\tag{1.7}
$$
所有证明只构造有限和 $L$，不把一般 $\ell^2$ 系数的无限算子和当成有界算子。

## 2. 任意固定阶实际真空列

令 $w_j$ 为有限支撑复数，$\sum_j|w_j|^2\le1$，并置
$$
L(w)=\sum_jw_jV_j.
$$
本节不需 $L(w)$ 增生。记
$$
c_0=1,\qquad c_n=3^{n+1}n!\quad(n\ge1).
$$

**引理 2.1。**
$$
\boxed{\|L(w)^n\Omega\|\le c_n.}
\tag{2.1}
$$

证明中把出现至少两次的指标记为有序互异组 $j_1,\ldots,j_r$，重数为
$a_1,\ldots,a_r\ge2$。置 $A=a_1+\cdots+a_r$、$s=n-A$。
准确多项式展开为
$$
L(w)^n\Omega=
n!\sum_{\substack{r\ge0,\ a_\ell\ge2\\A\le n}}
\frac{1}{r!\prod_{\ell=1}^r a_\ell!}
\sum_{\substack{j_1,\ldots,j_r\\\text{互异}}}
\left(\prod_{\ell=1}^r w_{j_\ell}^{a_\ell}V_{j_\ell}^{a_\ell}\right)
\left(
\sum_{\substack{|F|=s\\F\cap\{j_1,\ldots,j_r\}=\varnothing}}
w_F\chi_F
\right).
\tag{2.2}
$$
$r=0$ 使用空积约定。$1/r!$ 准确消去重复指标组的排序；单次指标的所有排列已在 $n!$ 中，不能再加入一个 $s!$。

固定重复指标后，括号中的完整实际列由 (1.1) 准确等于 Walsh 和。其范数至多
$$
\left(\sum_{|F|=s}|w_F|^2\right)^{1/2}\le\frac1{\sqrt{s!}}.
\tag{2.3}
$$
而重复算子乘积范数至多 $3^A$。由于每个 $|w_j|\le1$，
$$
\sum_{\substack{j_1,\ldots,j_r\\\text{互异}}}
\prod_{\ell=1}^r|w_{j_\ell}|^{a_\ell}
\le\prod_{\ell=1}^r\sum_j|w_j|^{a_\ell}\le1.
\tag{2.4}
$$
于是
$$
\|L(w)^n\Omega\|
\le n!\sum_{\substack{r\ge0,\ a_\ell\ge2\\A\le n}}
\frac{3^A}{r!\prod_\ell a_\ell!\sqrt{(n-A)!}}.
\tag{2.5}
$$
用 $3^A\le3^n$ 和 $1/\sqrt{(n-A)!}\le1$ 后，延长正项级数给
$$
\frac{\text{右端}}{3^nn!}
\le
\sum_{r\ge0}\frac1{r!}
\left(\sum_{a\ge2}\frac1{a!}\right)^r
=\exp(e-2)<3.
$$
这证明 (2.1)。所有重复指标的真实 carry 已由完整算子范数支付；没有用纯局部模型代替 $V_j$。证毕。

## 3. 有限差分抽出第 k 阶矩

此节取 $w_j\ge0$、$\|w\|_2\le1$，故 $L=L(w)$ 是有界增生算子。
对 $t>0$ 置
$$
E_t=(I+tL)^{-1},\qquad T_t=tL(I+tL)^{-1}.
$$
增生性与 Cayley 变换给
$$
\|E_t\|\le1,\qquad \|T_t\|\le1.
\tag{3.1}
$$
并且
$$
E_t=\int_0^\infty e^{-u}e^{-utL}\,du\in\mathcal A
$$
为范数收敛积分。因此以下所有测试及余项属于实际代数。

对固定 $k\ge1$，有限代数恒等式为
$$
T_{jt}\Omega=
\sum_{a=1}^k(-1)^{a-1}(jt)^aL^a\Omega
+(-1)^k(jt)^{k+1}E_{jt}L^{k+1}\Omega.
\tag{3.2}
$$
定义
$$
\Delta_{k,t}=\sum_{j=1}^k(-1)^{k-j}\binom kjT_{jt}.
$$
则 $\|\Delta_{k,t}\|\le2^k-1$。有限差分恒等式
$$
\sum_{j=0}^k(-1)^{k-j}\binom kjj^a
=\begin{cases}0,&0\le a<k,\\k!,&a=k,\end{cases}
$$
给
$$
\Delta_{k,t}\Omega=(-1)^{k-1}k!t^kL^k\Omega+\mathcal R_{k,t},
$$
其中
$$
\|\mathcal R_{k,t}\|
\le a_kt^{k+1},\qquad
a_k=c_{k+1}\sum_{j=1}^k\binom kjj^{k+1}.
\tag{3.3}
$$
通过 (1.3) 配对，
$$
k!|\Phi_v(L^k)|
\le(2^k-1)Kt^{-k}+a_kVt.
\tag{3.4}
$$
若 $K,V>0$，取 $t=(K/V)^{1/(k+1)}$。定义
$$
\beta_k=\frac{2^k-1+a_k}{k!},
$$
得到
$$
\boxed{
|\Phi_v(L(w)^k)|
\le\beta_k K^{1/(k+1)}V^{k/(k+1)}
\quad(w\ge0,\ \|w\|_2\le1).
}
\tag{3.5}
$$
$K=0$ 时 $\Phi_v$ 在实际代数上为零，$V=0$ 时也平凡。一般非负 $w$ 的右边再乘 $\|w\|_2^k$。

## 4. 全部复混合矩的极化

先令 $w_1,\ldots,w_k$ 为非负实向量，$\|w_\nu\|_2\le1$。
交换性给准确极化恒等式
$$
k!\,\Phi_v\!\left(\prod_{\nu=1}^kL(w_\nu)\right)
=
\sum_{I\subset\{1,\ldots,k\}}(-1)^{k-|I|}
\Phi_v\!\left(L\left(\sum_{\nu\in I}w_\nu\right)^k\right).
\tag{4.1}
$$
$\|\sum_{\nu\in I}w_\nu\|_2\le|I|$，所以 (3.5) 给右边的统一界。

对一般复向量 $w$ 写
$$
w=(\operatorname{Re}w)_+-(\operatorname{Re}w)_-
+i(\operatorname{Im}w)_+-i(\operatorname{Im}w)_-.
$$
这四个非负部分的 $\ell^2$ 范数之和至多 $2\|w\|_2$。
逐变量展开 (4.1) 的多线性型，因此定义
$$
\gamma_0=1,\qquad
\gamma_k=
\frac{2^k\beta_k}{k!}\sum_{j=1}^k\binom kjj^k
\quad(k\ge1)
\tag{4.2}
$$
后有
$$
\boxed{
\left|\Phi_v\!\left(\prod_{\nu=1}^kL(w_\nu)\right)\right|
\le\gamma_k K^{1/(k+1)}V^{k/(k+1)}
\prod_{\nu=1}^k\|w_\nu\|_2.
}
\tag{4.3}
$$
这里重复指标的矩也在内。$k=0$ 的解释为 $|\Phi_v(I)|\le K$。

## 5. 去掉重复指标而不付维数费用

令 $\Pi_k$ 为 $\{1,\ldots,k\}$ 的集合分割族。对 $\pi\in\Pi_k$ 记
$$
\mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!,
\qquad
s(\pi)=\#\{B\in\pi:|B|=1\}.
\tag{5.1}
$$
有准确的有限组合恒等式
$$
\mathbf1_{\{i_1,\ldots,i_k\ {\rm 两两不同}\}}
=
\sum_{\substack{\pi\in\Pi_k\\
 i_\nu\text{ 在每一块 }B\text{ 上相等}}}\mu(\pi).
\tag{5.2}
$$
可逐个相等指标组验证：一个大小 $r$ 的组贡献
$\sum_{\pi\in\Pi_r}\mu(\pi)$，它是首一多项式
$x(x-1)\cdots(x-r+1)$ 在 $x=1$ 的值；$r=1$ 为 $1$，$r>1$ 为 $0$。这也直接证明 (5.2)。

固定一个分割 $\pi$，以及 $\|w_\nu\|_2\le1$。
每个非单块 $B$ 产生系数列
$$
b_B(i)=\prod_{\nu\in B}w_\nu(i),\qquad
\sum_i|b_B(i)|\le\prod_{\nu\in B}\|w_\nu\|_{|B|}
\le1.
\tag{5.3}
$$
第一步为 Hölder，第二步用 $|B|\ge2$。

把所有非单块的指标固定，令
$$
R=\prod_{\substack{B\in\pi\\|B|\ge2}}V_{i_B}^{|B|}.
$$
不同块的 $i_B$ 允许相同，且
$$
R\in\mathcal A,\qquad\|R\|\le3^{k-s(\pi)}.
$$
交换性使
$$
\Phi_v(RT)=\Phi_{Rv}(T).
$$
因此，对向量 $Rv$ 的真实泛函范数和 Hilbert 范数分别有
$$
K_R\le3^{k-s(\pi)}K,\qquad
V_R\le3^{k-s(\pi)}V.
\tag{5.4}
$$
对余下 $s=s(\pi)$ 个单块使用 (4.3)，再以 (5.3) 对非单块求和，得到该分割的贡献不超过
$$
3^{k-s}\gamma_s K^{1/(s+1)}V^{s/(s+1)}.
\tag{5.5}
$$
$s=0$ 时就是实际算子范数对 $\Phi_v(R)$ 的直接界，不需新的零阶算子。
因为 $K\le V$、$s\le k$，
$$
K^{1/(s+1)}V^{s/(s+1)}
\le K^{1/(k+1)}V^{k/(k+1)}.
\tag{5.6}
$$

定义有限常数
$$
\boxed{
\Lambda_k=
\sum_{\pi\in\Pi_k}|\mu(\pi)|\,3^{k-s(\pi)}\gamma_{s(\pi)}.
}
\tag{5.7}
$$
将 (5.2)--(5.6) 代入全部矩的和，再用 (1.4) 消去共同符号 $(-1)^k$，即得 (1.7)。

这一去重复步骤没有把对角删除当成某个免费收缩。所有对角碰撞都通过非单块的 $\ell^1$ 权、实际 $R$ 及低阶混合矩逐项支付。也没有要求 $Rv$ 正、有限次数或与未知核相关。

由于常数与 $J$ 无关，可以对有限支撑测试取极限，得到整个可数指标集上的有界 $k$ 线性型。这个延拓只发生在系数张量中，不引入一个未经定义的无限 $L(w)$。

## 6. 真正正密度头矩的后果

令 $\rho\ge0$ 为迹类、$\tau=\operatorname{Tr}\rho>0$，
$\varphi(R)=\operatorname{Tr}(\rho R)$，并取准确规范头代表
$$
v_m=\sum_{F\subset[0,m)}(-1)^{|F|}
             \varphi(V_F^{[m]})\chi_F.
\tag{6.1}
$$
[原正密度头矩证明](R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)已证明
$$
\Phi_{v_m}|_{\mathcal A_m}=\varphi|_{\mathcal A_m},\qquad
K_m(v_m)=\tau.
\tag{6.2}
$$
若实际单射 $S\in\mathcal A$ 满足
$\varphi(S\{A\}')=0$，同稿已利用准确前缀 carry、真空循环性和 $S$ 单射性证明
$$
V_m:=\|v_m\|\longrightarrow\infty,\qquad
v_m/V_m\rightharpoonup0.
\tag{6.3}
$$
这里不以头代数元素直接代入原湮灭条件，也不增加一个未证的增长率。

对每个固定 $k$，(1.7) 给
$$
\boxed{
\frac{\|T_{k,[0,m)}(v_m)\|_\varepsilon}{V_m}
\le\Lambda_k\left(\frac{\tau}{V_m}\right)^{1/(k+1)}
\longrightarrow0.
}
\tag{6.4}
$$
因此任意随 $m$ 变化的单位纯张量测试，其归一化配对都一致趋零。允许全部指标相交、任意复相位和随 $v_m$ 选择测试。

### 6.1 有预算的张量测试

对有限张量 $Z$ 定义射影范数
$$
\|Z\|_\pi=
\inf_{Z=\sum_\ell u_{\ell,1}\otimes\cdots\otimes u_{\ell,k}}
\sum_\ell\prod_{\nu=1}^k\|u_{\ell,\nu}\|_2.
$$
由定义，
$$
|\langle T_{k,[0,m)}(v_m),Z_m\rangle|
\le\Lambda_k\tau^{1/(k+1)}V_m^{k/(k+1)}\|Z_m\|_\pi.
\tag{6.5}
$$
所以当 $\|Z_m\|_\pi=o((V_m/\tau)^{1/(k+1)})$ 时，配对除以 $V_m$ 趋零。
这里保留真实分解预算，不用一个没有条件数控制的张量秩替代它。

### 6.2 正交纯张量方向

设 $\mathscr E_m$ 有 $r_m$ 个正交归一基向量，每个基向量是 $k$ 个单位向量的纯张量。逐个应用 (6.4) 并平方相加，
$$
\|P_{\mathscr E_m}T_{k,[0,m)}(v_m)\|_{\rm HS}^2
\le r_m\Lambda_k^2\tau^{2/(k+1)}V_m^{2k/(k+1)}.
\tag{6.6}
$$
若 $r_m=o((V_m/\tau)^{2/(k+1)})$，这个投影的 HS 范数除以 $V_m$ 趋零。
本条要求明确的正交纯张量基；不宣称任意有相同形式秩的张量都满足这种投影界。
二次情形的矩阵 SVD 允许更直接的低秩结论，且前稿的 $690$ 常数明显更好；本文不替换该锐一些的界。

## 7. 尚未支付的平方和

准确有
$$
\|T_{k,[0,m)}(v_m)\|_{\rm HS}^2=k!\,\|P_kv_m\|^2.
\tag{7.1}
$$
一般高维张量的注入范数远小于 HS 范数。
(6.4) 因此不推出 $\|P_kv_m\|/V_m\to0$，也不删除旧全部次数层的相交组合费用。

常数 $\Lambda_k$ 随 $k$ 增长；只凭 $V_m\to\infty$ 不能把“每个固定 $k$”改成一个任意增长的 $k_m$。
原密度 $\rho$ 的有限秩，也没有给所有这些系数张量一个统一的射影范数或正交纯张量维数上界。

下一实际问题仍是：能否结合原正密度和真正 $S$ 湮灭关系，控制完整密集高秩/高次部分的平方和或实际分解预算。本文没有证明一般正正规湮灭者不存在，也没有把固定阶矩约束当成普通 ISP 的完成。
