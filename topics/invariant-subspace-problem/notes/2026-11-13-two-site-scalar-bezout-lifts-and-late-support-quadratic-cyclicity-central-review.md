# 二位标量 Bézout 提升：二次偏离的双池平均与迟首位慢幂排核

日期：2026-11-13（UTC）。作者：central_review。
状态：本文给完整实际证明，供主会话独立核验后登记。
核心输入是在同一反射下使用两位线性组合，
把未知核上的 first 项消成非零标量行列式。
一般 Hilbert 不变子空间问题仍未完成。

## 1. 二次目标与双池条件

取任意复
$$
a,b\in\ell^2,\qquad a_*,b_*\in\mathbb C,\qquad c\in\ell^1.
$$
令
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,
$$
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2.
\tag{1.1}
$$
对任意固定 $\lambda\in\mathbb C$，取原自然闭算子
$$
T_\lambda=X^2+Y-B-\lambda I,\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^2.
\tag{1.2}
$$
R176 给完整 $C$ 自伴性、全部自然幂域和真实图核心，
并有
$$
T_\lambda e^w
=
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)-\lambda
\right]e^w.
\tag{1.3}
$$

设沿某个无穷整数子序列 $N$，
存在两个不交的真实物理位池
$$
I_N,\ J_N,\qquad |I_N|=|J_N|=N,
$$
以及固定常数 $\mu,C_a>0$，使
$$
\boxed{
\min(I_N\cup J_N)\ge\mu N,\qquad
\max_{j\in I_N\cup J_N}|a_j|\le C_aN^{-1/2}.
}
\tag{1.4}
$$
定义跨池行列式
$$
\Delta_{jk}=a_kc_j-a_jc_k
\qquad(j\in I_N,\ k\in J_N),
$$
$$
d_N=\min_{j\in I_N,\ k\in J_N}|\Delta_{jk}|.
$$
要求
$$
\boxed{
d_N>0,\qquad
\ell_N:=1+\log^+d_N^{-1}=O(N^{3/2}).
}
\tag{1.5}
$$
不要求同一池内的行列式非零。
$c$ 在两个池以外可为任意 $\ell^1$ 行。

**定理 1（双池标量消元）。**
在 (1.4)–(1.5) 下，对每个 $\lambda\in\mathbb C$，
$$
\boxed{
\ker T_\lambda=0,\qquad
\overline{\operatorname{Ran}T_\lambda}=H,
}
\tag{1.6}
$$
因而 (1.3) 非零且循环。

本稿没有使用主 first 的全空间预解式，
也不要求核内 $X$ 拟幂零。
$\lambda\ne0$ 时通常只知其核内谱包含 $\{\pm\sqrt\lambda\}$；
以下标量消元对任意有界 $X_M$ 都成立。

## 2. 同一个真实闭核与合法输入

固定 $\lambda$，反设
$$
M=\ker T_\lambda\ne0.
$$
R176 的实际最大图给
$$
\boxed{
M\subset\mathcal D_\infty(X),\qquad
X_M:=X|_M\in B(M).
}
\tag{2.1}
$$
所有 $\mathcal A$ 元素保持 $M$，
与 $X$ 完整域交换并保持全部自然幂域。
这里不从某个全空间算子的单射或稠密像外推限制性质。

对选中的物理位，记
$$
u_j=t_jN_j,\qquad
L_j=8a_jX_M+4c_jI_M.
\tag{2.2}
$$
对跨池一对 $(j,k)$，定义全空间有界 $\mathcal A$ 元素
$$
\boxed{
P_{jk}
=
\frac{a_k u_k-a_j u_j}{4\Delta_{jk}}.
}
\tag{2.3}
$$
分母是非零复标量，不是算子分母。
即使 $a_j$ 或 $a_k$ 为零，(2.3) 仍按原公式合法。

$P_{jk}$ 保持 $M$。
因此对 $f\in M$，
$$
P_{jk}f\in M\subset\mathcal D_\infty(X),
\qquad
X^nP_{jk}f=X_M^nP_{jk}f.
$$
后面任意有限个不交对的乘积也具有同样性质。
所有输入均已在同一个真实闭核内，
没有先反射再试图使用核内公式。

## 3. 二位恒等式及全部跨位二次项

先在仅作为记账的交换多项式商
$$
\mathbb C[u_j,u_k]/(u_j^2,u_k^2)
$$
中计算。
系数允许为与这些变量交换的有界 $X_M$ 多项式。

准确有
$$
a_kL_j-a_jL_k
=
4(a_kc_j-a_jc_k)I_M
=
4\Delta_{jk}I_M.
\tag{3.1}
$$
故
$$
\begin{aligned}
(u_jL_j+u_kL_k)P_{jk}
&\equiv
\frac{u_ju_k(a_kL_j-a_jL_k)}{4\Delta_{jk}}\\
&=u_ju_kI_M.
\end{aligned}
\tag{3.2}
$$

以下明确核对反射差并没有遗漏跨位项。
对有限选位集 $F$，只在 $F$ 中把
$R_j=V(t_jN_j)$ 换成 $V(-t_jN_j)$，
得到 $\widehat X,\widehat Y,\widehat B$。
其一阶部分为
$$
\widehat X-X=4\sum_{j\in F}a_ju_j+\text{真实重复位余项},
$$
$$
\widehat Y-Y=4\sum_{j\in F}c_ju_j+\text{真实重复位余项}.
$$
准确符号差
$$
\widehat B-B
=
\sum_{j\in F}
16a_j^2u_j^3(I-u_j^2)^{-2}
\tag{3.3}
$$
从三次开始。

因此 $\widehat T_\lambda-T_\lambda$ 的平方零主多项式为
$$
\boxed{
A_F
=
\sum_{j\in F}u_jL_j
+
16\left(\sum_{j\in F}a_ju_j\right)^2.
}
\tag{3.4}
$$
第二项完整包含跨位
$$
32\sum_{j<k,\ j,k\in F}a_ja_k u_ju_k.
\tag{3.5}
$$
不能把 (3.4) 只写成一次和；
本稿保留 (3.5)，随后靠总次数准确排除其贡献。
标量 $\lambda$ 在反射差中完全相消。

## 4. r 对不交配对的准确 r! 系数

固定小参数 $\theta>0$，置
$$
r=\lceil\sqrt{N/\theta}\rceil.
\tag{4.1}
$$
充分大 $N$ 时 $r\le N$。

对每个
$$
I\subset I_N,\quad J\subset J_N,\qquad |I|=|J|=r,
$$
只选一个确定的双射配对。
例如分别按物理位递增排序后逐项配对。
记这些对为 $(j_s,k_s)$、$1\le s\le r$，
$$
F=I\cup J,\qquad |F|=2r,
$$
$$
P_{I,J}=\prod_{s=1}^rP_{j_sk_s}.
\tag{4.2}
$$
没有对全部 $r!$ 种双射再求和。

在商
$$
\mathbb C[u_j:j\in F]/(u_j^2:j\in F)
$$
中，$P_{I,J}$ 的总次数为 $r$。
$A_F$ 无零次项。
若 $A_F^r$ 的某个词选过至少一个二次项，
乘 $P_{I,J}$ 后总次数至少 $2r+1$；
只有 $2r$ 个变量，所以该词必含某个平方并为零。
这同时排除了全部 (3.5) 的跨位二次项。

剩余项只能来自 $(\sum_Fu_jL_j)^rP_{I,J}$。
输入每对选一个变量；
为避免重复，一次和必须在每对中恰选剩余的另一个变量。
$r$ 个线性因子的排列数恰为 $r!$。
每一对的两种输入选择由 (3.1) 相消成 $4\Delta_{jk}$，
准确取消 (2.3) 的标量分母。
因此
$$
\boxed{
A_F^rP_{I,J}
\equiv r!\prod_{j\in F}u_j\,I_M
=
r!t_FN_FI_M
\pmod{(N_j^2:j\in F)}.
}
\tag{4.3}
$$
这里 $t_F=\prod_Ft_j$、$N_F=\prod_FN_j$。
$2r$ 个输出位对应的系数仍是 $r!$，
不是 $(2r)!$，也没有额外的配对 $r!$。

## 5. 系数预算、真实进位及深域 jets

设
$$
m_N=\lfloor\mu N\rfloor.
$$
由 (1.4)，对上述每个 $F$，
$$
\sum_F|a_j|
\le2C_ar/\sqrt N=O_\theta(1),
$$
$$
\sum_F|a_j|^2=O_\theta(N^{-1/2}),
\qquad
\sum_F|c_j|
\le\sum_{j\ge m_N}|c_j|\longrightarrow0.
\tag{5.1}
$$
$c$ 的尾只须有界，没有速度要求。

记 $L_t=\max(1,\sup_j|t_j|)$。
用 (2.3) 的有限标量系数定义绝对系数预算
$$
H_{I,J}
=
\prod_{s=1}^r
\frac{|a_{k_s}||t_{k_s}|+|a_{j_s}||t_{j_s}|}
{4|\Delta_{j_sk_s}|}.
\tag{5.2}
$$
因为 $\|N_j\|=1$，
$$
\|P_{I,J}\|\le H_{I,J}.
$$
由 (1.4)–(1.5)，
$$
H_{I,J}\le
\left(\frac{C_aL_t}{2\sqrt N\,d_N}\right)^r.
$$
可取统一预算
$$
H_N=
\max\left\{1,\
\left(\frac{C_aL_t}{2\sqrt N\,d_N}\right)^r
\right\},
$$
满足
$$
\boxed{\log H_N\le r\ell_N+C r.}
\tag{5.3}
$$
后续使用的是这一绝对系数预算，
不只依赖可能因相消而更小的 $\|P_{I,J}\|$。

R260 的任意跨度真实壳层给
$$
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\|\delta_X^s(\gamma_FY-\widehat Y)\|
+\|\delta_X^s(\gamma_FB-\widehat B)\|
\le s!\epsilon_N,
$$
$$
\epsilon_N\le C e^{-38516^{m_N-1}}.
\tag{5.4}
$$
这里 $\gamma_F=\operatorname{Ad}J_F$、
$J_F=\prod_{j\in F}M_{\chi_j}$。
该已证估计只使用 $a\in\ell^2$、$a^2,c\in\ell^1$，
不要求选中位最大物理位置受控。

所有 $J_F$ 双向保持 $\mathcal D_\infty(X)$。
对
$$
f_{I,J}=P_{I,J}f\in M
$$
先有
$$
\|X^nf_{I,J}\|\le\|X_M\|^n\|f_{I,J}\|.
$$
结合 (5.1)、(5.4) 的有限词正规排序，
存在固定 $R_{M,\theta}$ 使
$$
\|X^nJ_Ff_{I,J}\|
\le2R_{M,\theta}^n\|f_{I,J}\|
\qquad(0\le n\le4r).
\tag{5.5}
$$
全部实际反射误差被
$\epsilon_N e^{C_\theta r\log(r+2)}H_N$
控制。

再把 (4.3) 搬回真实算子：
每个被商掉的单项式至少重复一个选中位，
而
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j=d_{j+1}/d_j^2\le e^{-38516^j}.
\tag{5.6}
$$
在 $M$ 上，(3.4) 的全部系数绝对范数和由 (5.1) 一致控制；
乘上输入的绝对系数预算 (5.2)，
所有重复位项的总范数至多
$$
\eta_{m_N}C_{M,\theta}^rH_N.
\tag{5.7}
$$
这是真实重复位误差，不把 $N_j^2$ 宣称为零。

由于 $P_{I,J}M\subset M$，正确顺序为
$$
\boxed{
T_\lambda^rJ_FP_{I,J}f
=
J_F(\gamma_FT_\lambda)^rP_{I,J}f.
}
\tag{5.8}
$$
先在同一个 $M$ 上用 (4.3)，随后才作用最左侧的反射。
没有声称 $J_FM\subset M$。

又由实际
$$
\left\|N_F-\prod_{j\in F}E_j\right\|
\le C(2r)\eta_{m_N},
\qquad
J_FE_F=(-1)^{2r}E_F=E_F,
$$
得到
$$
\boxed{
T_\lambda^rJ_FP_{I,J}f
=
r!t_FE_Ff+\mathcal E_{I,J}f,
}
\tag{5.9}
$$
其中
$$
\|\mathcal E_{I,J}f\|
\le
\epsilon_N e^{C_\theta r\log(r+2)}H_N\|f\|
+
C r!|t_F|\,r\eta_{m_N}\|f\|.
\tag{5.10}
$$
调整固定常数后，(5.7) 已并入第一项。
全部系数、自然域和重复位项均在同一实际 Haar 模型中支付。

## 6. 双池平均的完整归一化

定义
$$
\boxed{
\mathcal V_N
=
r!\left(\frac2N\right)^{2r}
\sum_{\substack{I\subset I_N,\ J\subset J_N\\|I|=|J|=r}}
t_{I\cup J}^{-1}J_{I\cup J}P_{I,J}.
}
\tag{6.1}
$$
对每个 $(I,J)$ 只用 §4 固定的一个配对。
总项数准确为 $\binom Nr^2$。

置 $L_b=\max(1,\sup_j|t_j|^{-1})$。
组合数上界给
$$
\|\mathcal V_N\|
\le
r!\left(\frac4{N^2}\right)^r
\binom Nr^2L_b^{2r}H_N
\le
\frac{(4L_b^2)^r}{r!}H_N.
$$
记右边为 $A_N$，必要时增大到1，
则
$$
\boxed{
\log A_N\le r\ell_N+C'r.
}
\tag{6.2}
$$
没有 $N^2$ 级的全空间预解成本。

令
$$
C_{I_N}=\frac2N\sum_{j\in I_N}E_j,\qquad
C_{J_N}=\frac2N\sum_{k\in J_N}E_k.
$$
两个池不交，纯位算子严格交换；
每个 $E_j^2=0$。
因此
$$
C_{I_N}^rC_{J_N}^r
=
(r!)^2\left(\frac2N\right)^{2r}
\sum_{\substack{I\subset I_N,\ J\subset J_N\\|I|=|J|=r}}
E_{I\cup J}.
\tag{6.3}
$$
(6.1) 中的 $r!$，与 (5.9) 再产生的 $r!$，
恰好给 (6.3) 的 $(r!)^2$。
这是选择 (6.1) 归一化的原因。

将 (5.10) 求和，
$$
\boxed{
\left\|
T_\lambda^r\mathcal V_Nf
-C_{I_N}^rC_{J_N}^rf
\right\|
\le
\left[
\epsilon_Ne^{C_\theta r\log(r+2)}A_N
+C4^r r\eta_{m_N}
\right]\|f\|
\longrightarrow0.
}
\tag{6.4}
$$
$m_N\asymp N$，所以实际双指数 carry 压过
$O(r\ell_N+r\log(r+2))=O(N^2)$ 的全部成本。

精确纯位范数给
$$
\|C_{I_N}^rC_{J_N}^r\|
\le(1+1/N)^{2r},
$$
故一致有界。
在两个固定有限柱之间，
矩阵元系数恰为
$$
\left[\frac{(N)_r}{N^r}\right]^2.
$$
由 $r\sim\sqrt{N/\theta}$，
$$
\log\left[\frac{(N)_r}{N^r}\right]^2
=
-\frac{r(r-1)}N+O(r^3/N^2)
\longrightarrow-\frac1\theta.
$$
于是
$$
\boxed{
T_\lambda^r\mathcal V_Nf
\rightharpoonup e^{-1/\theta}f.
}
\tag{6.5}
$$
这是有界的非零弱极限，
没有取 $r\gg\sqrt N$ 后重称强近单位。

## 7. 局部四次估计与完整 C 配对

固定任意物理有限头的局部全矩阵 $D$。
与原统一提升、固定盘及辅助圆稿相同，
对 (5.5) 的真实输入 jets，
每次局部交换提取一个固定有限头的实际 $A$ 因子。
R109 的四次幂界给
$$
\boxed{
\|(\operatorname{ad}_{T_\lambda}^rD)\mathcal V_Nf\|
\le
2\|D\|A_N C_{D,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
}
\tag{7.1}
$$
$\operatorname{ad}_{T_\lambda}=\operatorname{ad}_{T_0}$，
标量位移没有额外交换子成本。
(7.1) 只断言在所需自然域向量上的估计，
不把无界多项式交换子当作全空间有界算子，
也不把整个慢 $Y$ 有界除以 $A$。

由 (1.5)、(6.2)，若 $\ell_N\le C_\ell N^{3/2}$，
则
$$
\limsup\frac{\log A_N}{r^4}
\le C_\ell\theta^{3/2}.
$$
固定足够小的 $\theta$，使此数小于 $1/4$。
该选择与 $D$ 无关；
所有固定局部常数的 $r$ 次成本除以 $r^4$ 后趋零。
因此 (7.1) 趋零。

对 $f,g\in M$，全部向量有足够自然幂域，
完整双线性 Leibniz 恒等式为
$$
\mathcal B(DT_\lambda^r\mathcal V_Nf,g)
=
(-1)^r
\mathcal B((\operatorname{ad}_{T_\lambda}^rD)\mathcal V_Nf,g).
$$
由 (6.5)、(7.1)，
$$
\mathcal B(Df,g)=0
$$
对全部局部全矩阵成立。
这些矩阵在原 Haar 无限张量表示中不可约；
若 $f\ne0$，其局部矩阵轨道张成稠密，
取 $g=f$ 将迫 $Cf=0$，矛盾。
故 $M=0$。

由 $T_\lambda=CT_\lambda^*C$ 得稠密像，
再由 (1.3) 的真实循环图核心，
目标非零且循环。
定理 1 得证。

## 8. 任意物理排列的规则幂行：迟首位纯高阶偏离关闭

令主行非零幅度的非增重排为 $\rho_n$。
假设
$$
A_-n^{-\sigma}\le\rho_n\le A_+n^{-\sigma},
\qquad \sigma>\frac12,\quad A_\pm>0.
\tag{8.1}
$$
物理排列和主相位任意。

假设 $c\in\ell^1$，且存在 $\kappa>1$、$c_\pm>0$，
使对所有充分高的非零主物理位，
$$
\boxed{
c_-|a_j|^\kappa
\le|c_j|\le c_+|a_j|^\kappa.
}
\tag{8.2}
$$
有限物理头任意，包括主首位有 $a_{j_a}\ne0$ 而 $c_{j_a}=0$。
主零位上的辅助也可任意，只须整个 $c\in\ell^1$。
对于由 (8.2) 定义的可和辅助，自然要求 $\kappa\sigma>1$；
原高阶近共振 $\kappa>2$ 自动满足。

**推论 2。** 在 (8.1)–(8.2) 下，
(1.3) 对每个 $\lambda\in\mathbb C$ 非零且循环。

证明写出不依赖物理排列的双池。
固定非零主位的排序枚举 $j(n)$，并选择足够大的整数 $K\ge4$。
先取秩带
$$
U_N=\{j(n):N<n\le3N\},
$$
$$
W_N=\{j(n):KN<n\le(K+2)N\}.
$$
每带有 $2N$ 项，且互不相交。
分别删去物理位小于 $N$ 的项；
每带至多删 $N$ 项，所以各可取剩余 $N$ 项为 $I_N,J_N$。
充分大 $N$ 同时删掉 (8.2) 的全部有限物理例外。

对 $j\in I_N$，
$$
|a_j|\ge A_-3^{-\sigma}N^{-\sigma},
$$
而对 $k\in J_N$，
$$
|a_k|\le A_+K^{-\sigma}N^{-\sigma}.
$$
所以
$$
|c_j/a_j|
\ge c_-A_-^{\kappa-1}3^{-\sigma(\kappa-1)}
N^{-\sigma(\kappa-1)},
$$
$$
|c_k/a_k|
\le c_+A_+^{\kappa-1}K^{-\sigma(\kappa-1)}
N^{-\sigma(\kappa-1)}.
$$
增大固定 $K$，使后一常数至多为前一常数的一半。
由反三角不等式，不论复相位如何，
$$
|c_j/a_j-c_k/a_k|
\ge C_0N^{-\sigma(\kappa-1)}
\tag{8.3}
$$
对全部跨池对成立。

又两带都有
$$
|a_j a_k|
\ge
A_-^2[3(K+2)]^{-\sigma}N^{-2\sigma}.
$$
因此
$$
\boxed{
|\Delta_{jk}|
=
|a_ja_k|\,|c_j/a_j-c_k/a_k|
\ge C_1N^{-\sigma(\kappa+1)}.
}
\tag{8.4}
$$
于是 $\ell_N=O(\log N)$。
同时物理最小位至少为 $N$，
最大主幅度不超过 $A_+N^{-\sigma}\le A_+N^{-1/2}$。
定理 1 的全部条件满足，推论得证。

特别，
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad \frac12<\sigma<1,
$$
$$
c_0=0,\qquad
c_j=\beta|a_j|^\kappa\omega_j\quad(j\ge1),
\qquad
\kappa>2,\quad \beta\ne0,\quad|\omega_j|=1
\tag{8.5}
$$
现在满足推论。
它的零标量位移正是此前首支撑与共同圆方法保留的规则慢幂候选。
本稿由二位标量消元处理该值，同时处理全部其他固定 $\lambda$。
任意复 $\ell^2$ 指数权与任意 $a_*$ 均允许。

## 9. 规则伸缩指数主行至 α=3/2

同一判据还有如下独立充分范围。
设对某个 $0<\alpha\le3/2$，
$$
A_-e^{-\beta_+n^\alpha}
\le\rho_n
\le A_+e^{-\beta_-n^\alpha}
\quad(n\ge1),
\tag{9.1}
$$
其中 $0<\beta_-\le\beta_+$。
仍取 (8.2) 的任意 $\kappa>1$ 及 $c\in\ell^1$，
允许全部有限物理头例外。

使用相同的两个秩带。
选固定 $K$ 足够大，使
$$
\beta_-K^\alpha>\beta_+3^\alpha.
$$
则充分大 $N$ 时，第二带的 $|c_k/a_k|$ 上界
至多是第一带下界的一半。
由各带的下界和反三角不等式，
$$
d_N\ge C e^{-C'N^\alpha}.
$$
故
$$
\ell_N=O(N^\alpha)=O(N^{3/2}).
$$
所有主位在高秩上自动满足 $|a_j|\le\|a\|_2/\sqrt N$；
删除物理低位后，定理 1 适用。
$\alpha=3/2$ 的端点仍由固定小 $\theta$ 支付。

所以 (1.3) 在 (9.1)–(8.2) 下对全部 $\lambda$ 循环。
本节要求明确的两侧全局排序界；
没有从只有一个稀疏下界子序列擅自推出两个秩带的幅度分离。

## 10. 边界与没有自动覆盖的情况

定理 1 的核心是两个增长位池之间的行列式下界。
如果辅助与主行在所选尾部严格成同一线性比例，
跨池行列式可能全为零，
本稿不能使用该配对输入；
这类情形可另外检查既有固定盘核内逆定理。

对于一般极不规则排序，
或者在所有可取双池上行列式下降过快而使
$\ell_N=O(N^{3/2})$ 失败，
本稿没有给无条件结论。
特别不把“主、辅助两行形式上线性独立”
直接当成 (1.4)–(1.5) 的定量双池条件。

本稿处理的是二次多项式。
更高阶反射差的线性系数含 $X_M^{p-1}$，
混合低阶修正也需要重新计算；
不能把二位公式未经证明复制为全阶标量消元。

已闭的 (8.5) 不再应登记为开放的规则慢幂纯高阶偏离。
整个课题仍须继续检查其他未闭类及一般 Hilbert ISP 的完成标准。

## 11. 来源与新增步骤

- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  真实自然域、核内有界 first、完整 $C$ 自伴与图循环。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意物理跨度的实际壳、全部导数和有限词正常排序。
- [近共振统一准则](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)：
  真实三次 $B$ 余项、固定局部四次交换子及完整配对。
- [固定盘逆](../results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)：
  独立 $a,c$ 行的真实 jets 输入范围。
- R109 的原四次幂界与实际纯位范数：
  (6.4)–(7.1) 的预算。

新的实质步骤是 (2.3) 的二位标量 Bézout 输入、
(4.3) 的 $r$ 对总次数消去、
(6.1)–(6.3) 的双池精确归一化，
以及 (8.3)–(8.4) 对任意相位、任意物理排列的双池构造。
