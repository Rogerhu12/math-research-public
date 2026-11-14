# R230 附录：复指数尾右滤子、共同次数相位锥与完整 Gram

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下定理和完整 Gram 公式均已证明。** 本文处理真实右因子
$G_m(z)=\exp(zU_m)$，统一允许 $|z|\le q^6$、$q=2^m$，
并证明它们不能给相位消元主理想测试一个非消失的归一化真空矩。
复指数允许任意相位；结论不是只把实正指数代入旧正锥。
纯模型中结论对所有复参数成立，实际提升明确支付全部 carry。
本文也给不同指数参数、不同有限 Walsh 输入之间的完整 Gram，
用于后续具有真实相消的线性组合。
一般右因子、密度专属证书及普通 ISP 仍未解决。

## 1. 实际对象及已经证明的输入

固定 $S=S_N$ 或 $S=S_Y$，相应统一取 $X_j=N_j$ 或 $X_j=Y_j$。
在原 Haar 物理尾空间中令
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_{j\ge0}a_j<2,
\qquad q=2^m,\quad m\ge1,
$$
$$
U_m=\sum_{j\ge m}a_jX_j\in\mathcal B_m\subset A',
\qquad
D_m=\sum_{j\ge m}a_jE_j,\qquad E_j=e_{10}^{(j)}.
\tag{1.1}
$$
两者均为范数收敛级数。$D_m$ 只作纯比较，
没有把 $D_m$ 当成实际交换子。

R253 的真实相位消元给
$$
P_m=\prod_{\zeta^q=1}\gamma_\zeta(S)
=I_{<m}\otimes Q_m\in S\mathcal A,\qquad Q_m\in\mathcal B_m.
\tag{1.2}
$$
尾真空记 $\Omega=\Omega_{\ge m}$，其态为 $\omega_m$。
沿用
$$
h_m=\omega_m(D_m^q)>0,\qquad h_m\ge(8eq)^{-q},
$$
$$
\|Q_m-D_m^q\|\le e_m,\qquad
e_m=13a_\Sigma q(3a_\Sigma)^{q-1}
       \exp\!\left(-\frac{770}{16}q^4\right).
\tag{1.3}
$$
这正是 R235 使用的误差，主负指数为
$770\,16^{m-1}=(770/16)q^4$。

实际递推和局部差为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
N_j^2=\eta_jN_{j+1},\quad \|N_j\|\le1,\quad
0<\eta_j\le e^{-770\,16^j}.
\tag{1.4}
$$
又 $Y_j=N_j(I+N_j)^{-1}$。由于
$$
(I+N_j)^{-1}=(I-N_j)(I-N_j^2)^{-1},
$$
且 $\eta_j<1/3$，有 $\|(I+N_j)^{-1}\|\le3$，故
$$
\|Y_j-E_j\|
\le \|N_j-E_j\|+\|N_j^2(I+N_j)^{-1}\|
\le4\eta_j.
$$
因此两个固定模型都有
$$
\boxed{\quad
\zeta_m:=\|U_m-D_m\|
 \le4a_\Sigma e^{-770q^4}.
\quad}
\tag{1.5}
$$

令
$$
G_m(z)=e^{zU_m},\qquad
R_m(z)=Q_mG_m(z),\qquad
A_{m,k}(z)=D_m^k e^{zD_m}\quad(k\ge0).
\tag{1.6}
$$
$G_m(z)$ 和 $R_m(z)$ 是真实有界尾算子；
$I_{<m}\otimes R_m(z)\in S\mathcal A$ 对每个 $z$ 精确成立。

记
$$
L_m=\left\lfloor q^{2/3}/4\right\rfloor,\qquad
\beta=1+1/\sqrt2.
\tag{1.7}
$$

## 2. 纯指数相位的范数恒等式

**引理 2.1。** 对每个 $m,k$ 和每个 $z\in\mathbb C$，
$$
\boxed{\quad
\|D_m^k e^{zD_m}\|
=\|D_m^k e^{|z|D_m}\|.
\quad}
\tag{2.1}
$$
同时
$$
\boxed{\quad
|\omega_m(D_m^k e^{zD_m})|
\le\omega_m(D_m^k e^{|z|D_m}).
\quad}
\tag{2.2}
$$

证明。先令 $D_{m,M}=\sum_{m\le j<M}a_jE_j$。
若 $z=r e^{i\theta}$，对这有限组物理位作对角酉共轭，
可把每个 $E_j$ 同时送到 $e^{-i\theta}E_j$。
因而 $D_{m,M}^k e^{zD_{m,M}}$ 被送到
$e^{-ik\theta}D_{m,M}^k e^{rD_{m,M}}$，证明有限式。
由于 $D_{m,M}\to D_m$ 于算子范数，固定 $k,z$ 的多项式乘指数
亦在算子范数中收敛，得到 (2.1)。

这里没有定义或使用在当前 Haar 不完全张量积上同时旋转无限多位的酉算子。
只使用有限张量酉及随后合法的算子范数极限。

$D_m$ 保持物理函数非负锥，且 $\Omega=1$ 非负。
指数幂级数在算子范数中绝对收敛，
$$
\omega_m(D_m^k e^{zD_m})
=\sum_{n=0}^\infty \frac{z^n}{n!}\omega_m(D_m^{k+n}),
\qquad \omega_m(D_m^{k+n})\ge0.
$$
逐项取绝对值得 (2.2)。证毕。

## 3. 纯正锥在这里没有支撑预算

下面说明所用 R237 纯结论的准确范围，而不把实际锥的支撑上限带到纯步骤。

设
$$
W_0=\sum_{B\subset[m,\infty)\ {\rm finite}}c_BE_B,
\qquad c_B\ge0,\qquad0<\sum_Bc_B<\infty.
\tag{3.1}
$$
此处不限制 $|B|$，也不限制最大物理位。
级数按算子范数绝对收敛。

对固定 $B$，
$$
D_m^qE_B
=q!\sum_{\substack{|F|=q\\F\cap B=\varnothing}}a_FE_{F\cup B}.
\tag{3.2}
$$
按其正真空矩归一化后，$F$ 是在未排除的指标中按权 $a_F$
选取的固定基数 $q$ 子集。R237 正右因子附录 §§3--4 已证明：

1. 排除固定的其他指标不会降低一个未排除指标的入选率；
2. 对未排除模型的 $p_j=\mathbb P(j\in F)$，
   $1-p_j\le4(j+1)^2/q^2$；
3. 因而对 $J_m=\{m,\ldots,m+L_m-1\}$，充分大的 $m$ 有
   $\mathbb P(J_m\subset F\cup B)\ge3/4$，一致于任意有限 $B$。

为看清第三点，若 $j\in B$ 它已经入选；否则用前两点，再作并集界：
$$
\mathbb P(J_m\nsubseteq F\cup B)
\le\frac4{q^2}\sum_{j=m}^{m+L_m-1}(j+1)^2
\le\frac{16L_m^3}{q^2}\le\frac14
$$
（最终 $m\le L_m$）。这些界与 $|B|$ 无关。

在每个 $j\in J_m$ 上取单位向量
$$
u_j=\cos(\pi/8)e_0+\sin(\pi/8)e_1,\quad
v_j=\sin(\pi/8)e_0+\cos(\pi/8)e_1,
$$
其他位取 Haar 真空。所得 $u,v$ 是原尾空间中的单位向量。
所有 $\langle E_Gu,v\rangle\ge0$，而 $J_m\subset G$ 时
$$
\langle E_Gu,v\rangle=\beta^{L_m}\omega_m(E_G).
$$
按 (3.2) 的正真空矩再对 $B$ 作概率混合，得到
$$
\boxed{\quad
\|D_m^qW_0\|
\ge\frac34\beta^{L_m}\omega_m(D_m^qW_0).
\quad}
\tag{3.3}
$$
可数和由绝对范数收敛通过。
R237 对实际右因子所加的 $|B|\le b_m$ 预算，只用于其后统一的
绝对 carry 除以真空下界；不出现在 (3.3) 中。

对任何 $r\ge0$，
$$
e^{rD_m}=\prod_{j\ge m}(I+ra_jE_j)
=\sum_B r^{|B|}a_BE_B,
\tag{3.4}
$$
且
$\sum_Br^{|B|}a_B=\prod_{j\ge m}(1+ra_j)<\infty$。
所以 (3.3) 对 $W_0=e^{rD_m}$ 适用，不需截断指数的次数。

由 (2.1)--(2.2) 得到以下纯全平面结论：
$$
\boxed{\quad
\frac{|\omega_m(A_{m,q}(z))|}{\|A_{m,q}(z)\|}
\le\frac43\beta^{-L_m}
\qquad(z\in\mathbb C).
\quad}
\tag{3.5}
$$
此外分母始终有独立于相位的下界
$$
\boxed{\quad
\|A_{m,q}(z)\|
=\|D_m^qe^{|z|D_m}\|
\ge \omega_m(D_m^qe^{|z|D_m})\ge h_m.
\quad}
\tag{3.6}
$$
最后一个界使用指数的常数项为 $I$ 及正系数。
绝不以可能因复相消而为零的 $|\omega_m(A_{m,q}(z))|$ 作分母下界。

## 4. 全复参数的实际指数与 Duhamel 预算

R215/R218 已证明：逐位任意 $N/Y$ 选择和任意系数相位，
模长 $a_j$ 的全慢和 $V$ 满足
$$
\|e^{zV}\|\le e^{16\sqrt{|z|}}.
\tag{4.1}
$$
同一上界适用于 $U_m$。确切理由是，把低于 $m$ 的有限个系数
看作各自闭圆盘 $|c_j|\le a_j$ 中的变量；
对每个单位向量对应用标量多变量最大模原理。
边界上是 (4.1) 的全相位模型，令这有限个变量为零即可。
这不新增或改变 R218 的精确半群型结论。

纯因子的奇异值和张量范数给
$$
\log\|e^{zD_m}\|
=\sum_{j\ge m}\operatorname{arsinh}\frac{|z|a_j}{2}
\le\sum_{n=1}^\infty\log(1+|z|/n^2)
\le\pi\sqrt{|z|}.
\tag{4.2}
$$
最后一步由递减函数的积分比较及
$\int_0^\infty\log(1+r/x^2)\,dx=\pi\sqrt r$ 得到。

Duhamel 恒等式不要求 $D_m$ 与 $U_m$ 交换。由 (1.5)、(4.1)--(4.2)，
$$
\begin{aligned}
\|e^{zU_m}-e^{zD_m}\|
&\le |z|\zeta_m\int_0^1
 e^{16\sqrt{(1-t)|z|}+\pi\sqrt{t|z|}}\,dt\\
&\le |z|\zeta_m e^{17\sqrt{|z|}},
\end{aligned}
\tag{4.3}
$$
因为 $16\sqrt{1-t}+\pi\sqrt t\le\sqrt{256+\pi^2}<17$。

因此令 $r=|z|$，有完整算子范数比较
$$
\boxed{\quad
\|R_m(z)-A_{m,q}(z)\|
\le\Delta_m(r):=
 e_m e^{16\sqrt r}
 +a_\Sigma^q\,r\zeta_m e^{17\sqrt r}.
\quad}
\tag{4.4}
$$
这同时比较了所有输入向量，不是只比较真空或某个次数。

当 $0\le r\le q^6$ 时，
$$
\frac{\Delta_m(r)}{h_m}\le t_m,
$$
其中可取
$$
\begin{aligned}
t_m={}&13a_\Sigma q(3a_\Sigma)^{q-1}(8eq)^q
 \exp\!\left(-\frac{770}{16}q^4+16q^3\right)\\
&+4a_\Sigma^{q+1}q^6(8eq)^q
 \exp(-770q^4+17q^3).
\end{aligned}
\tag{4.5}
$$
从而
$$
t_m=
\exp\!\left(-\frac{770}{16}q^4+16q^3+O(q\log q)\right),
\qquad
t_m\beta^{L_m}\longrightarrow0.
\tag{4.6}
$$
这里 (4.5) 是使用明确上界定义的数列；(4.6) 是该数列的渐近式。
特别保留了主项中的 $16q^3$，没有把它改成未支付的常数。

## 5. 实际全复指数过滤定理

**定理 5.1。** 存在 $m_0$，使两个固定慢符号中，
对所有 $m\ge m_0$ 和所有 $|z|\le q^6$，
$R_m(z)\ne0$，且
$$
\boxed{\quad
\frac{|\omega_m(Q_m e^{zU_m})|}
     {\|Q_m e^{zU_m}\|}
\le3\beta^{-L_m}.
\quad}
\tag{5.1}
$$
因而任何随 $m$ 改变的此类复参数，都不能使该实际主理想测试
的归一化真空矩保持非消失下界。

证明。置 $B_m(z)=\|A_{m,q}(z)\|\ge h_m$。
由 (3.5)、(4.4)，
$$
|\omega_m(R_m(z))|
\le\frac43\beta^{-L_m}B_m(z)+\Delta_m(|z|),
$$
$$
\|R_m(z)\|\ge B_m(z)-\Delta_m(|z|).
$$
由 (4.6)，充分大的 $m$ 有
$t_m\le\min(1/4,\beta^{-L_m}/4)$。
除以 $B_m(z)$，分母为正，而且
$$
\frac{|\omega_m(R_m(z))|}{\|R_m(z)\|}
\le
\frac{(4/3)\beta^{-L_m}+t_m}{1-t_m}
\le3\beta^{-L_m}.
$$
所有估计一致于参数，证明完成。

特别，常见负实过滤 $e^{-tU_m}$ 及振荡过滤 $e^{itU_m}$
（$0\le t\le q^6$）都在结论中。
这里所排除的是指定真空比，不是断言这些算子对任意真密度的
全部右矩只有这一行为，也不是一个完整 $q_m$ 上界。

## 6. 不同参数和全部有限 Walsh 列的精确 Gram

本节不作鞍点下界推断；提供完整的解析核，保留全部交叉项。
所有无穷积在每个参数紧集上一致收敛，因为 $\sum a_j<\infty$、
$\sum a_j^2<\infty$。

先定义两个独立复变量的整函数
$$
\mathcal K_m(\xi,\eta)
=\prod_{j\ge m}
 \left(1+\frac{a_j}{2}(\xi+\eta)
          +\frac{a_j^2}{2}\xi\eta\right).
\tag{6.1}
$$
局部直接计算给
$$
\mathcal K_m(\xi,\eta)
=\langle e^{\xi D_m}\Omega,e^{\overline\eta D_m}\Omega\rangle.
$$
内积线性于第一个变量，因此第二个参数在此写成 $\overline\eta$；
右边作为 $\xi,\eta$ 的函数是整函数。

对任意非负整数 $k,\ell$，
$$
\boxed{\quad
\langle A_{m,k}(z)\Omega,A_{m,\ell}(w)\Omega\rangle
=
\left.
 \partial_\xi^k\partial_\eta^\ell\mathcal K_m(\xi,\eta)
\right|_{\xi=z,\ \eta=\overline w}.
\quad}
\tag{6.2}
$$
等价的精确系数式是
$$
k!\ell!\,[u^k v^\ell]\,
\mathcal K_m(z+u,\overline w+v).
$$
它包括 $z\ne w$、不同阶数及全部复相位。

令
$$
\mathcal P_m(s)=\prod_{j\ge m}(1+a_js).
\tag{6.3}
$$
真空振幅准确为
$$
\boxed{\quad
H_{m,k}(z):=\omega_m(A_{m,k}(z))
=\partial_z^k\mathcal P_m(z/2)
=k![u^k]\mathcal P_m((z+u)/2).
\quad}
\tag{6.4}
$$
这里 $\partial_z^k$ 包含链式法则中的 $2^{-k}$。

为进一步保留整个有限列 Gram，置局部 Walsh 基 $e_0=\Omega_+$、
$e_1=\chi$。若 $u=a_j\xi$、$v=a_j\eta$，局部核矩阵为
$$
\mathcal L_j(\xi,\eta)=
\begin{pmatrix}
1+(u+v)/2+uv/2 &(v-u)/2+uv/2\\
(u-v)/2+uv/2 &1-(u+v)/2+uv/2
\end{pmatrix}.
\tag{6.5}
$$
行指标是第一个输入，列指标是第二个输入。此式来自
$$
E_j\Omega_+=E_j\chi=(\Omega_+-\chi)/2
$$
逐项计算，不丢弃混合的线性符号。

对有限 $F,G\subset[m,\infty)$，令
$$
\mathcal K_m^{F,G}(\xi,\eta)
=\prod_{j\ge m}
 [\mathcal L_j(\xi,\eta)]_{\mathbf1_F(j),\mathbf1_G(j)}.
\tag{6.6}
$$
只有有限多个因子不是 $(0,0)$ 项，因此仍是明确的整函数。
准确有
$$
\boxed{\quad
\langle A_{m,k}(z)\chi_F,A_{m,\ell}(w)\chi_G\rangle
=
\left.
\partial_\xi^k\partial_\eta^\ell
 \mathcal K_m^{F,G}(\xi,\eta)
\right|_{\xi=z,\ \eta=\overline w}.
\quad}
\tag{6.7}
$$
有限 Walsh 线性组合的全部 Gram 由该式作有限双线性求和。
没有只保留某一对角列或某一次数层。

### 6.1 一变量闭式和双变量因式分解

Euler 双曲正弦乘积（NIST DLMF 4.36.1）给
$$
\mathcal P_m(s)=
\frac{\sinh(\pi\sqrt s)}{\pi\sqrt s}
\prod_{n=1}^{m}(1+s/n^2)^{-1}.
\tag{6.8}
$$
根号表达式以其整函数幂级数解释，有限分母处的表面奇点全部可去；
不选取某个不连续的平方根支作为定义。

若 $b_+,b_-$ 是
$$
b_++b_-=(\xi+\eta)/2,\qquad b_+b_-=\xi\eta/2
$$
的两个根，则
$$
\mathcal K_m(\xi,\eta)
=\mathcal P_m(b_+)\mathcal P_m(b_-).
\tag{6.9}
$$
右边对两个根对称，因而不依赖其编号或局部分支。
(6.8)--(6.9) 可供后续精确系数、鞍点或数值计算；
不能单凭正实轴最大模把带复相消的导数下界宣布为已证。

外部恒等式来源：
[NIST DLMF 4.36.1](https://dlmf.nist.gov/4.36.E1)。
本节其余核等式均由局部二维矩阵及范数收敛直接推导。

## 7. 实际完整 Gram 的统一误差

对所有单位输入 $u,v$，(4.4) 给
$$
\begin{aligned}
&|\langle R_m(z)u,R_m(w)v\rangle
 -\langle A_{m,q}(z)u,A_{m,q}(w)v\rangle|\\
&\quad\le
 \Delta_m(|z|)\|A_{m,q}(w)\|
 +\Delta_m(|w|)\|A_{m,q}(z)\|
 +\Delta_m(|z|)\Delta_m(|w|).
\end{aligned}
\tag{7.1}
$$
右侧不含 Walsh 支撑的大小或最大位。
又由 (4.2)，
$$
\|A_{m,q}(z)\|\le a_\Sigma^q e^{\pi q^3}
\quad (|z|\le q^6).
$$
故 (7.1) 除以 $h_m^2$ 后，一致有
$$
\boxed{\quad
\frac{\text{(7.1) 左端}}{h_m^2}
\le
2t_m a_\Sigma^q(8eq)^q e^{\pi q^3}+t_m^2
\longrightarrow0.
\quad}
\tag{7.2}
$$
它保留全部实际 Gram，且没有用“定位误差乘完整矩常数”的失败路径。

更一般，给有限复 Borel 测度 $\sigma$，支撑在 $|z|\le q^6$，
Bochner 积分
$$
G_{m,\sigma}=\int e^{zU_m}\,d\sigma(z)\in\mathcal B_m,\qquad
A_{m,\sigma}=\int A_{m,q}(z)\,d\sigma(z)
\tag{7.3}
$$
存在，并有
$$
\|G_{m,\sigma}\|\le e^{16q^3}\|\sigma\|_{\rm TV},\qquad
\|Q_mG_{m,\sigma}-A_{m,\sigma}\|
\le h_m t_m\|\sigma\|_{\rm TV}.
\tag{7.4}
$$
其纯源 Gram 就是 (6.7) 对 $d\sigma(z)d\overline{\sigma}(w)$
的双重积分；紧参数集上的一致有界性保证 Fubini 和有限列极限。

若 $\rho\ge0$ 真正湮灭 $S\mathcal A$，$\lambda=\operatorname{Tr}\rho$，
R235 的全部实际右测试准确给
$$
\left|\frac{\operatorname{Tr}(\rho T_mG_{m,\sigma})}{h_m}\right|
\le
\lambda\epsilon_m e^{16q^3}\|\sigma\|_{\rm TV},
\qquad \epsilon_m=e_m/h_m.
\tag{7.5}
$$
这是对真实 $G_{m,\sigma}\in A'$ 的约束。
本文没有把这个泛函换成仅由某个局部正密度决定的矩向量。

## 8. 一般复混合必须真正利用相消

(5.1) 不能逐项推广到任意复线性组合，因为组合的算子范数可能远小于
各项范数之和。这个剩余可能性可精确量化。

对 §7 中任意有限复测度 $\sigma$，若 $A_{m,\sigma}\ne0$，由 (3.5)
和三角不等式，
$$
\frac{|\omega_m(A_{m,\sigma})|}{\|A_{m,\sigma}\|}
\le
\frac43\beta^{-L_m}
 \frac{\int\|A_{m,q}(z)\|\,d|\sigma|(z)}
      {\|A_{m,\sigma}\|}.
\tag{8.1}
$$
所以若左边至少为某个固定 $\kappa>0$，则必有
$$
\boxed{\quad
\frac{\int\|A_{m,q}(z)\|\,d|\sigma|(z)}
     {\|A_{m,\sigma}\|}
\ge\frac{3\kappa}{4}\beta^{L_m}.
\quad}
\tag{8.2}
$$
这是组合中必须发生的算子范数相消量；不是不可能性结论。
其指数为 $O(q^{2/3})$，仍远小于实际 $q^4$ carry 预算。
因此不能以 (8.2) 排除真正依赖 $\rho$ 的复杂相位组合。

纯 $D_m$ 的核是否为零不参与任何步骤。
下一未闭合问题仍是从真密度及全 $G$ 湮灭关系构造有效的复杂组合，
或构造其他全空间理想内证书；本稿不把指数族失败外推为完整理想范数衰减。


## 9. 原实际支撑预算内的共同次数相位锥

本节的实际单项式明确使用 $N_B=\prod_{j\in B}N_j$，
不将它替换为 $Y_B$。左因子 $Q_m$ 仍可来自 $S_N$ 或 $S_Y$。
因此使用的是 R237 已付过的 $\|N_j\|\le1$ 及
$\|N_B-E_B\|\le |B|e^{-770q^4}$；不另外宣称 $Y_B$ 有同一预算。

固定一个可以随 $m$ 改变的实数 $\theta$，令
$$
W_\theta=\sum_{|B|\le b_m}d_B e^{i\theta|B|}N_B,
\qquad d_B\ge0,\qquad0<\sum_Bd_B<\infty.
\tag{9.1}
$$
允许可数项和任意高位。假设
$$
\limsup_m b_m/q^4<\frac{770}{16\log2}.
\tag{9.2}
$$
包括 $b_m\le q^4$ 及 $b_m=o(q^4)$。
则一致于 $\theta$、系数和所有支撑位置，充分大的 $m$ 有
$$
\boxed{\quad
Q_mW_\theta\ne0,\qquad
\frac{|\omega_m(Q_mW_\theta)|}{\|Q_mW_\theta\|}
\le3\beta^{-L_m}.
\quad}
\tag{9.3}
$$

证明。按齐次性令 $\sum_Bd_B=1$，并设
$$
W_\theta^0=\sum_{|B|\le b_m}d_Be^{i\theta|B|}E_B,\qquad
W_+^0=\sum_{|B|\le b_m}d_BE_B.
$$
先对有限指标子集作统一物理相位酉，随后对绝对范数收敛级数取极限，
准确有
$$
\|D_m^qW_\theta^0\|=\|D_m^qW_+^0\|.
\tag{9.4}
$$
原因是共轭把 $D_m$ 送到 $e^{-i\theta}D_m$，
同时把 $W_\theta^0$ 送到 $W_+^0$；只留下全局标量
$e^{-iq\theta}$。
它不声称任何对应的无限酉在 Haar 表示中存在，也不声称实际 $N_j$
可同时作这个相位共轭。

逐项绝对值和纯正锥 (3.3) 又给
$$
|\omega_m(D_m^qW_\theta^0)|
\le k_m,\qquad
\|D_m^qW_\theta^0\|\ge(3/4)\beta^{L_m}k_m,
$$
其中 $k_m=\omega_m(D_m^qW_+^0)>0$。
R237 §5 的逐项下界原封不动适用：
$$
k_m\ge H_m
:=q!2^{-q-b_m}(m+b_m+q)^{-2q}.
\tag{9.5}
$$
确切地，每个 $B$ 从前 $b_m+q$ 个尾指标中最多排除 $b_m$ 个，
故还可保留 $q$ 个指标的单项式；再用 $\sum_Bd_B=1$。

因为相位不影响绝对系数和，
$$
\|W_\theta\|\le1,\qquad
\|W_\theta-W_\theta^0\|\le b_m e^{-770q^4},
$$
所以
$$
\|Q_mW_\theta-D_m^qW_\theta^0\|
\le \widehat\Delta_m
:=e_m+a_\Sigma^q b_m e^{-770q^4}.
\tag{9.6}
$$
由 (9.2)、$q!\ge(q/e)^q$，
$$
\log(\widehat\Delta_m/H_m)
\le-\frac{770}{16}q^4+b_m\log2+O(q\log q)\longrightarrow-\infty.
\tag{9.7}
$$
令 $s_m=\widehat\Delta_m/H_m\le1/4$。实际比值至多
$$
\frac{1+s_m}{(3/4)\beta^{L_m}-s_m}
\le3\beta^{-L_m},
$$
且分母严格正，证明 (9.3)。

这覆盖的是所有系数相位随次数线性变化的锥，
不要求不同支撑具有同样的大小或同样的正振幅。
例如，有限坐标乘积
$\prod_{j\in J}(I+e^{i\theta}t_jN_j)$、$t_j\ge0$，
只要 $|J|\le b_m$，就在其中。
因此仅把所有局部正参数同时改为负数或同一复射线，
不能绕开原正锥障碍。
不同坐标的独立相位、非线性次数相位和一般复线性组合仍不由本节排除。

## 已证依赖与范围

- R253 及其第三附录：真实 $P_m=I\otimes Q_m$、$h_m$、$e_m$。
- R237 正右因子附录 §§3--4：纯固定基数占据和共同偏转矩阵元。
  本稿 §3 明确使用其中没有支撑预算的纯步骤。
- R215/R218：任意相位慢和的全空间半群上界；
  未把全空间精确型当成真空或未知不变子商的下界。
- R235 真湮灭全部右测试：只作用于本稿实际 $G\in A'$。
- 本稿新步骤：有限相位酉后的范数极限、全复指数比较、
  $q^6$ 参数盘的实际统一 carry、全部有限列 Gram、复混合相消成本，
  以及原真实支撑预算内的共同次数相位锥。


完整工作源：[复指数与相位锥推导](../notes/2026-11-13-complex-exponential-tail-right-filters-and-complete-source-gram-normal-complex.md)。
