# R34：二次无理数对完整低阶相位的全频除数门

2026-11-12，independent-audit。

**状态：已证明的中间结论。** 本文处理已经准确化到 Fourier 对角的
**完整相位**，而不只处理主特征返回角。对二次无理旋转数，
$1/j$ 相位系数只须避开一个明确的离散危险集合，就得到真正的
$|1+D_j|\ge c/j$ 高频下界；全部未覆盖的模明确落入一个有限集合。
还给出同一 continued-fraction cylinder 内判别式 $5$ 与 $8$ 的
双目标选择门，包含两目标真实 $1/j$ 系数的连续性费用。

本文没有证明当前候选已有这样的真实对角正常形，没有确定其
Maslov 常相位、完整 $1/j$ 系数或余项常数，也没有把有限低模、固定帽、
source 或完整 PDE 逆省去。它是 R32 的真实边界算子在完成相应
正常形后可使用的一项算术输入。

## 1. 相位、频率与常相位的准确约定

角变量取周期 $2\pi$，正 Fourier 模标为 $j=1,2,\ldots$。
设某个已证的真实对角模型满足
$$
D_j=e^{i\Theta_j},\qquad
\Theta_j=2\pi\alpha j+\frac{\beta}{j}+r_j,\qquad
|r_j|\le \frac{C}{j^{1+\eta}}\quad(j\ge J_0),
\tag{1.1}
$$
其中 $\Theta_j$ 是相容选定的**实相位提升**，
$\beta$ 的单位是弧度，$\eta>0$，$C\ge0$，$J_0\ge1$。
本节先取待逆缺陷为 $1+D_j$；因此主共振是
$j\alpha\in\mathbb Z+\tfrac12$。

式 (1.1) 已经假定完整常相位为 $0$ 模 $2\pi$。
如果实际模型是
$$
e^{i(2\pi\alpha j+\chi_0+\beta/j+r_j)},
$$
必须先证明 $\chi_0$ 的值；不能把未知的 $\chi_0$ 归入
$O(j^{-1})$。常相位为 $\pi$ 时是整数共振，其明确修改见第 7 节；
一般有理常相位也可处理。没有证明为有理的常相位不在本文的
简单整数范数门内。

实际原模型也不能被抹掉。例如若已证的准确正常形是
$$
D_j=Q_{0,j}\,
 e^{\,2\pi i(\alpha-\alpha_0)j}
 \exp i\left[
 \frac{c_1-c_{1,0}}{j}+\frac{c_2-c_{2,0}}{j^2}\right],
\tag{1.2}
$$
并且实际 $Q_{0,j}$ 具有已证相位展开
$$
\arg Q_{0,j}
=2\pi\alpha_0j+\chi_0+\frac{c_{1,0}}j
+\frac{c_{2,0}}{j^2}+r_{0,j},
$$
那么合成后的 $\beta$ 是 **$c_1$**，而非只取
$c_1-c_{1,0}$；余项包含 $c_2/j^2+r_{0,j}$。
若 $|r_{0,j}|\le Rj^{-3}$，可在 (1.1) 取
$\eta=1$、$C=|c_2|+R$。若没有该真实展开及余项界，
(1.2) 本身不支付 (1.1)。

本课题四重角的换算也必须固定。若物理频率 $n=4j$ 的相位写成
$$
2Jn+\frac{\beta_{\rm ph}}n+\frac{\gamma_{\rm ph}}{n^2}+\cdots,
$$
则 (1.1) 中
$$
\alpha=\frac{4J}{\pi},\qquad
\beta=\frac{\beta_{\rm ph}}4,\qquad
\gamma=\frac{\gamma_{\rm ph}}{16}.
\tag{1.3}
$$
这里 $J$ 只在实际已经证明径向或等价的情况下表示真实主作用量。
任意近似非径向图的径向均值作用量不是自动可用的 $\alpha$。

## 2. 整数范数恒等式及危险集合

令 $\alpha$ 为实二次无理数，取其 primitive 整系数方程
$$
A\alpha^2+B\alpha+C_0=0,\qquad A>0,\qquad
\mathfrak d=B^2-4AC_0>0
\tag{2.1}
$$
（$\mathfrak d$ 不是完全平方）。写
$$
\alpha=\frac{-B+s\sqrt{\mathfrak d}}{2A},\qquad s\in\{+1,-1\},
$$
并以 $\alpha'$ 表示另一个根。

给 $j\ge1$ 和任意奇整数 $t$，令
$\varepsilon=j\alpha-t/2$。则
$$
\begin{aligned}
N&=A(2j\alpha-t)(2j\alpha'-t)\\
 &=A t^2+2Bjt+4C_0j^2
 =4A\varepsilon^2-4s\sqrt{\mathfrak d}\,j\varepsilon .
\end{aligned}
\tag{2.2}
$$
特别，
$$
\boxed{\quad
N\in\mathbb Z\setminus\{0\},\quad N\equiv A\pmod2,\qquad
2\pi j\varepsilon
=-\frac{s\pi N}{2\sqrt{\mathfrak d}}
+\frac{2\pi sA}{\sqrt{\mathfrak d}}\varepsilon^2 .
\quad}
\tag{2.3}
$$
$N\ne0$ 不能删去：若范数乘积为零，就会使某个无理根等于有理数
$t/(2j)$，矛盾。这同时解释了 $\beta=0$ 不自动是危险值。

因此一个可直接使用的危险集合为
$$
\Lambda
=\left\{\frac{s\pi n}{2\sqrt{\mathfrak d}}:
 n\in\mathbb Z\setminus\{0\},\ n\equiv A\pmod2\right\}.
\tag{2.4}
$$
可以进一步加入 (2.2) 的任何已证整同余限制，以缩小该集合；
但不能任意删掉没有被排除的范数值。集合 (2.4) 已足够证明下文。
它是一个明确离散集，即使 $A$ 为偶数，也必须排除其中的 $n=0$。

## 3. 带明确有限 cutoff 的完整相位定理

### 定理 3.1

假设 (1.1)--(2.1)，并且已证明
$$
d_\beta:=\operatorname{dist}(\beta,\Lambda)>0.
$$
任取一个已知下界 $0<d\le d_\beta$，定义
$$
\kappa=\min\{1,d/2\},\qquad
H=\frac{\kappa+|\beta|+C}{2\pi},
\tag{3.1}
$$
以及明确整数
$$
\boxed{\quad
N_*=\left\lceil
\max\left\{
J_0,1,\left(\frac{4C}{d}\right)^{1/\eta},
\sqrt{\frac{8\pi A H^2}{\sqrt{\mathfrak d}\,d}}
\right\}\right\rceil .
\quad}
\tag{3.2}
$$
则全部 $j\ge N_*$ 满足
$$
\boxed{\qquad
|1+D_j|\ge \frac{2\kappa}{\pi j}.
\qquad}
\tag{3.3}
$$
若对 $\beta,C$ 只有区间上界，可在 $H$ 和 (3.2) 中代入统一上界；
$d$ 则必须是该区间到危险集合的真实距离下界。

**证明。** 对每个 $j$，取奇整数 $t$ 使
$$
\delta_j=\Theta_j-\pi t\in[-\pi,\pi].
$$
若 $|\delta_j|\ge\kappa/j$ 已有目标相位下界。
反设 $|\delta_j|<\kappa/j$，则
$$
\varepsilon=j\alpha-t/2
=\frac{\delta_j-\beta/j-r_j}{2\pi},
\qquad |\varepsilon|<H/j.
\tag{3.4}
$$
用 (2.3) 写出准确恒等式
$$
j\delta_j
=\beta-\frac{s\pi N}{2\sqrt{\mathfrak d}}
+\frac{2\pi sA}{\sqrt{\mathfrak d}}\varepsilon^2+jr_j .
\tag{3.5}
$$
其中 $s\pi N/(2\sqrt{\mathfrak d})\in\Lambda$。于是对
$j\ge N_*$，
$$
\begin{aligned}
d
&\le\left|\beta-\frac{s\pi N}{2\sqrt{\mathfrak d}}\right|\\
&\le |j\delta_j|
 +\frac{2\pi A}{\sqrt{\mathfrak d}}|\varepsilon|^2+j|r_j|\\
&<\kappa+\frac d4+\frac d4\le d,
\end{aligned}
$$
矛盾。故 $|\delta_j|\ge\kappa/j$。
最后
$$
|1+D_j|=2\sin(|\delta_j|/2)
\ge \frac{2}{\pi}|\delta_j|
$$
给 (3.3)。证毕。

### 有限低模和真正的一阶损失

若 $1\le j<N_*$ 的实际模型亦已核实没有未处理零点，置
$$
c_{\rm all}=\min\left\{
\frac{2\kappa}{\pi},
\min_{1\le j<N_*}j|1+D_j|
\right\}>0.
\tag{3.6}
$$
则 $|1+D_j|\ge c_{\rm all}/j$ 对全部正模成立，准确对角逆满足
$$
\|(I+D)^{-1}f\|_{H^s}
\le c_{\rm all}^{-1}\|f\|_{H^{s+1}}.
\tag{3.7}
$$
零模、负 Fourier cone、额外有限维核和幅度/均值增广均须按其实际
模型保留。若负 cone 是正 cone 的真共轭，(3.3) 同时覆盖它；
否则应对其自身相位分别核实本文的前提。

定理没有用一个主 Diophantine 常数减去任意大的 $|\beta|$。
它允许 $\beta$ 很大，只要它与完整危险集合仍有明确正距离；
代价会如 (3.2) 所示进入有限 cutoff。

## 4. 判别式 5：所有 golden-tail 目标都给奇整数格

取任何合法有限 continued-fraction prefix
$[a_0;a_1,\ldots,a_k]$，令其连续两个收敛分数为
$p/q$、$p_-/q_-$，其中 $q>0$。
对 $\tau>1$ 置
$$
\alpha(\tau)=\frac{p\tau+p_-}{q\tau+q_-}.
\tag{4.1}
$$
若 $\tau$ 满足 $\tau^2-a\tau-1=0$，则 $\alpha$ 满足
$$
(q_-\alpha-p_-)^2
+a(q_-\alpha-p_-)(q\alpha-p)
-(q\alpha-p)^2=0.
\tag{4.2}
$$
此整系数方程的判别式为
$$
(a^2+4)(pq_--p_-q)^2=a^2+4.
\tag{4.3}
$$
系数仍 primitive，因为该变量替换的整矩阵行列式为 $\pm1$；
其逆也是整矩阵，若新三系数有公因子，就会给原
$(1,-a,-1)$ 同一公因子。必要时整体乘 $-1$ 使 $A>0$。

对 golden tail
$$\tau_5=(1+\sqrt5)/2=[1;1,1,\ldots],$$
判别式恰为 $5$。此时 $B$ 为奇数；由
$B^2-4AC_0\equiv5\pmod8$ 得 $AC_0$ 为奇数，因此 $A,C_0$ 都为奇数。
所以 (2.2) 中 **$N$ 必为奇数且非零**，统一危险集合为
$$
\boxed{\quad
\Lambda_5=\frac{\pi}{2\sqrt5}(2\mathbb Z+1).
\quad}
\tag{4.4}
$$
它不随 prefix 的大小改变。prefix 改变会改变 $A$，
从而影响 cutoff (3.2)，但不会把危险格的间隔压小。

### R30 的明确例子

R30 所列
$$
\alpha_\sharp=\frac{8165-\sqrt5}{13918}
=[0;1,1,2,2,1,1,3,\overline1]
$$
的 primitive 方程为
$$
6959\alpha_\sharp^2-8165\alpha_\sharp+2395=0,
\qquad \mathfrak d=5,\quad s=-1.
\tag{4.5}
$$
所以完整相位只须检查
$\operatorname{dist}(\beta,\Lambda_5)$。
例如若真实相位证书给出
$$
|\beta|\le\tfrac12,\qquad |r_j|\le j^{-2}\quad(j\ge J_0),
\tag{4.6}
$$
则
$$
d_\beta\ge \frac{\pi}{2\sqrt5}-\frac12>\frac15.
$$
最后一个严格不等式可用 $\pi>157/50$、$\sqrt5<56/25$ 的有理界核实。
在定理 3.1 取 $d=1/5,\kappa=1/10,C=1,\eta=1$。
因为 $H\le4/15$、$\pi<22/7$、$\sqrt5>2$，(3.2) 的平方根小于 $180$，
其另一项是 $20$。因此得到一个无需隐藏常数的门：
$$
\boxed{\quad
j\ge\max(J_0,180)\quad\Longrightarrow\quad
|1+D_j|\ge\frac{1}{5\pi j}.
\quad}
\tag{4.7}
$$
这一例的 $180$ 和 $5\pi$ 是充分常数，不声称最优。
(4.6) 仍须从实际完整正常形证出；本文没有把它赋给当前数值图。

## 5. 判别式 8 及两个危险格的定量分离

在**同一个** prefix (4.1) 内，另取 silver tail
$$\tau_8=1+\sqrt2=[2;2,2,\ldots].$$
式 (4.2)--(4.3) 给 primitive 方程判别式 $8$。
$B$ 必为偶数；$A$ 不可能被 $4$ 整除，因为否则
$B^2-4AC_0$ 模 $16$ 只能为 $0$ 或 $4$，不可能为 $8$。
故 $A\bmod4\in\{1,2,3\}$。

对半整数共振的奇数 $t$，(2.2) 精确给
$$N\equiv A\pmod4.$$
因此比 (2.4) 更准确的危险集合是
$$
\boxed{\quad
\Lambda_8
=\frac{s\pi}{2\sqrt8}(A+4\mathbb Z).
\quad}
\tag{5.1}
$$
其中同样没有零。为核实其 cutoff，只须在定理 3.1 用
$d\le\operatorname{dist}(\beta,\Lambda_8)$；证明没有变化。

两个场的危险集合没有共同点。否则存在非零整数 $n,m$ 使
$$
\frac{\pi n}{2\sqrt5}=\frac{\pi m}{2\sqrt8},
\qquad 8n^2=5m^2,
$$
这会使 $\sqrt{8/5}$ 为有理数，矛盾。
尤其对一个**相同**的实数 $\beta$，它不可能同时精确落入两格；
$\beta=0$ 还分别与两格有正距离。

本题真正需要的是不同目标下的 $\beta_5,\beta_8$，它们不能被
无根据地当成同一个数。下面给出保留该变化的定量门。

### 命题 5.1：双目标实际系数门

设两个已经实际实现的目标模型满足
$$
|\beta_5|,|\beta_8|\le B_*,\qquad
|\beta_5-\beta_8|\le\frac{\Delta_*}{2},\qquad
\Delta_*=\frac{\pi^2}{320(B_*+2)}.
\tag{5.2}
$$
则至少一个目标满足
$$
\boxed{\quad
\operatorname{dist}(\beta_i,\Lambda_i)
\ge\frac{\Delta_*}{4}
=\frac{\pi^2}{1280(B_*+2)},\qquad i\in\{5,8\}.
\quad}
\tag{5.3}
$$

**证明。** 各取一个最近格点 $\lambda_i$。$\Lambda_5$ 的半间距为
$\pi/(2\sqrt5)<1$，$\Lambda_8$ 的半间距为 $\pi/\sqrt8<2$。
因此 $|\lambda_i|\le W:=B_*+2$。
写 $\lambda_5=\pi n/(2\sqrt5)$、
$\lambda_8=\pi m/(2\sqrt8)$，其中 $n,m$ 为非零整数。
则
$$
|\lambda_5^2-\lambda_8^2|
=\frac{\pi^2}{160}|8n^2-5m^2|
\ge\frac{\pi^2}{160}.
$$
由 $|\lambda_5+\lambda_8|\le2W$，
$$
|\lambda_5-\lambda_8|\ge\frac{\pi^2}{320W}=\Delta_*.
$$
三角不等式给
$$
\Delta_*
\le\operatorname{dist}(\beta_5,\Lambda_5)
 +|\beta_5-\beta_8|
 +\operatorname{dist}(\beta_8,\Lambda_8),
$$
结合 (5.2) 即得 (5.3)。证毕。

两个 prefix 目标的距离还具有准确公式
$$
\boxed{\quad
|\alpha(\tau_5)-\alpha(\tau_8)|
=\frac{\tau_8-\tau_5}
{(q\tau_5+q_-)(q\tau_8+q_-)}
<\frac1{q^2}.
\quad}
\tag{5.4}
$$
所以若已证明实际相位参数化中的统一 Lipschitz 界
$|\beta(\alpha_1)-\beta(\alpha_2)|\le L|\alpha_1-\alpha_2|$，
并且两目标均在已实现的真实参数区间内，则例如
$L/q^2\le\Delta_*/2$ 支付 (5.2) 的差条件。
若只知实际外参数 $a$ 的导数界，应使用已证的
$|\beta(a_5)-\beta(a_8)|\le L_a|a_5-a_8|$，连同真实目标参数距离，
而非将 $a$ 与 $\alpha$ 混同。

任一非空开区间内都可选一个足够深的 continued-fraction cylinder：
取区间内无理数，其有限 prefix cylinder 长度至多 $1/q^2$，
收敛分母趋于无穷，故最终 cylinder 的闭包含在该区间。
随后同一 prefix 的两个无理 tail 都在其中。
这只是一条算术可选性事实；实际返回图目标区间、参数 twist、
共轭和 $\beta$ 连续性仍须由实际方程支付。

## 6. 与 smoothing 余项、有限 Schur 块的准确接口

设真实边界算子在已证的正常形中是
$$
\mathscr B=I+D+\mathscr R,
\tag{6.1}
$$
其中对角模型在 $|j|\ge N_*$ 有 (3.3)。
置 $c_\infty=2\kappa/\pi$，令 $\Pi_N$ 为 $|j|\ge N$ 的投影。
若预选 Sobolev 档上已证明
$$
\|\mathscr R u\|_{H^{s+1+\varepsilon}}
\le M_s\|u\|_{H^s},\qquad \varepsilon>0,
\tag{6.2}
$$
则
$$
\|(I+D)^{-1}\Pi_N\mathscr R\Pi_N\|_{H^s\to H^s}
\le c_\infty^{-1}M_s\langle N\rangle^{-\varepsilon}.
\tag{6.3}
$$
取 $N\ge N_*$ 且右边至多 $1/2$，真实高角块由 Neumann 逆出，
并保留 $H^{s+1}\to H^s$ 的一阶损失和至多
$2c_\infty^{-1}$ 的常数。
所有高低 cross 随后必须进入同一个有限角 Schur 增广块，
不能在此处丢掉。

若余项只有恰好一个角导的 gain，增大 cutoff 不会自动改善
(6.3)；这时须直接支付相对范数小于一，或继续正常形消去更低阶项。
因此“有一个一阶小除数逆”与“任意 order $-1$ 余项都可吸收”
不是同一个命题。

本节的有限 Schur 块仅指已经压到边界角空间后的有限角数据。
它不把尚未完成的连续径向 cap/source 问题偷偷换成有限矩阵。

## 7. 整数及一般有理常相位

若完整常相位使共振位置为
$$j\alpha\in\mathbb Z+\omega,\qquad
\omega=r/q\in\mathbb Q,\quad q\ge1,$$
其中 $r,q$ 互素且 $0\le r<q$，则取整数
$t=qk+r$，$\varepsilon=j\alpha-t/q$。
准确整数范数改为
$$
\begin{aligned}
N
&=A(qj\alpha-t)(qj\alpha'-t)\\
&=A t^2+qBjt+q^2C_0j^2\\
&=Aq^2\varepsilon^2-sq^2\sqrt{\mathfrak d}\,j\varepsilon.
\end{aligned}
\tag{7.1}
$$
仍有 $N\ne0$，且 $N\equiv Ar^2\pmod q$。
完整危险集合可取
$$
\boxed{\quad
\Lambda_{q,r}
=\left\{\frac{s\,2\pi n}{q^2\sqrt{\mathfrak d}}:
n\in\mathbb Z\setminus\{0\},\
n\equiv Ar^2\pmod q\right\}.
\quad}
\tag{7.2}
$$
其余恒等式为
$$
2\pi j\varepsilon
=-\frac{s\,2\pi N}{q^2\sqrt{\mathfrak d}}
+\frac{2\pi sA}{\sqrt{\mathfrak d}}\varepsilon^2,
$$
所以定理 3.1 的 cutoff 和证明原样成立，只把 $\Lambda$ 换成
(7.2)。半整数情形是 $q=2,r=1$，整数情形是 $q=1,r=0$。
在待逆缺陷为 $1+D_j$ 时，实际常相位应满足
$\chi_0\equiv\pi-2\pi\omega\pmod{2\pi}$。

本节没有容许未知常相位。尤其不能仅因为两个转折通常产生某个
Maslov 符号，就不检查当前真实端口、共轭、原 $Q_{0,j}$ 和有限
frame 所给的符号。只有完成这个识别，才知道应使用半整数、
整数或另一个有理格。

## 8. 这项门实际减少了什么

对一个已证的全相位正常形，本文把“无限多个完整 target 除数”
变成：

1. 一个真实二次无理主旋转目标及准确常相位识别；
2. 一个真实 $1/j$ 系数到明确离散格的距离证书；
3. 一个高阶相位余项证书和 (3.2) 的明确有限 cutoff；
4. cutoff 以下的实际有限角块，以及实际 smoothing 余项的
   相对范数门。

判别式 $5/8$ 双目标进一步给第 2 项的一个可选择性充分门，
但其 (5.2) 诚实保留两个实际目标间的系数变化。
它不要求把真实返回图共轭到一个有理旋转，也没有从主返回旋转数
直接声称完整 PDE 可逆。应用到当前课题前，仍须把 R32 的真实
两通道算子、固定帽与强源域接到这个准确正常形。


## 9. PT 基点：在一个明确真实端口中的完整相位校准

本节只校准 R25 的实际 Pöschl--Teller 全轴算子与其衰减尾域，
不把结果直接授给修帽后的算子或当前非径向正常形。
设
$$
\mu=\frac{484}{89},\quad \nu=\frac{495}{89},\quad n=4j,\qquad
L_n=-\partial_x^2+n^2\mu^2-n^2\nu^2\operatorname{sech}^2x.
$$
置
$$
k_n=\mu n,\quad
\ell_n=\sqrt{\nu^2n^2+\tfrac14}-\tfrac12,\quad
a_n=\frac{\ell_n-k_n}{2},\quad b_n=\frac{\ell_n+k_n}{2}.
\tag{9.1}
$$
因 $\nu^2-\mu^2=\mu/4$，$n\ge4$ 时 $a_n\ge0$，
而 $b_n>0$。令 $f_n$ 为右半轴的非零衰减解。

### 9.1 半轴完整 Cauchy 线及正 impedance

可选
$$f_n(x)=\mathsf P_{\ell_n}^{-k_n}(\tanh x),$$
其中 $\mathsf P$ 是实区间上的 Ferrers 函数。
其超几何表示给
$f_n(x)\sim e^{-k_nx}/\Gamma(1+k_n)$，所以它是同一真实衰减支；
将 $t=\tanh x$ 代入其二阶方程也直接给 $L_nf_n=0$。
所用标准特殊函数恒等式见
[DLMF 14.3.1](https://dlmf.nist.gov/14.3.E1)、
[14.5.1--14.5.2](https://dlmf.nist.gov/14.5)。
在 $x=0$，
$$
f_n(0)=
\frac{2^{-k_n}\sqrt\pi}
{\Gamma(\tfrac12-a_n)\Gamma(1+b_n)},\qquad
f_n'(0)=
-\frac{2^{1-k_n}\sqrt\pi}
{\Gamma(-a_n)\Gamma(\tfrac12+b_n)}.
\tag{9.2}
$$
这里 $d(\tanh x)/dx=1$ 在零点，没有遗漏坐标导数。
用 [Gamma 反射公式 DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3)，得
$$
\frac{f_n'(0)}{f_n(0)}
=\mathcal K_n\tan(\pi a_n),\qquad
\mathcal K_n=
2\frac{\Gamma(1+a_n)\Gamma(1+b_n)}
{\Gamma(\tfrac12+a_n)\Gamma(\tfrac12+b_n)}>0
\tag{9.3}
$$
（商有极点时按完整 Cauchy 线解释）。

$\mathcal K_n$ 是一个真实的正 Fourier impedance，且在四重模上有
充分的明确椭圆界
$$
\boxed{\quad \frac n2<\mathcal K_n<3n,\qquad n=4,8,\ldots.\quad}
\tag{9.4}
$$
证明只需 Gamma 积分的 Hölder 不等式所给对数凸性：
$$
\sqrt x\le\frac{\Gamma(x+1)}{\Gamma(x+\tfrac12)}
\le\sqrt{x+\tfrac12}\quad(x>0),
\qquad
\frac{\Gamma(1)}{\Gamma(\tfrac12)}=\pi^{-1/2}.
$$
对 $n\ge8$，由 $\nu-\mu>3/25$、$\nu+\mu=11$ 得
$a_n/n>1/50$、$b_n/n>5$，所以
$\mathcal K_n>2n/\sqrt{10}>n/2$。
又 $\sqrt{\nu^2n^2+1/4}\le\nu n+1/(8\nu n)$、
$\nu-\mu<1/8$、$\nu>5$ 给
$a_n+1/2<n/4$、$b_n+1/2<6n$，故上界甚至小于 $\sqrt6\,n$。
$n=4$ 时 $a_n=0,b_n=4\mu$；用 $4<\mu<6$、$1<\pi<4$
在同一 Gamma 界中直接得到 (9.4)。

在中心用 R32 的完整端口，取 $K=\mathcal K_n$、$p=u'$。
右半轴衰减线的准确反射为
$$
r_n=
\frac{\mathcal K_nf_n(0)+if_n'(0)}
{\mathcal K_nf_n(0)-if_n'(0)}
=e^{2\pi i a_n}.
\tag{9.5}
$$
分母不为零，因为实数 $f_n(0),f_n'(0)$ 不会同时为零。
所以该式在 $f_n(0)=0$ 的 Dirichlet 极点也完全有意义，
并非先假设一个处处有界的半轴 DN。
左半轴为 $f_n(-x)$，其对中心 incoming/outgoing 的反射同为 $r_n$。

### 9.2 完整中心反馈及 $1/j$ 系数

将两个真实半轴在中心接合，准确条件是
$(1-r_n^2)z^+=0$。若把待逆缺陷写成 $1+D_j$，就必须取
$$
\boxed{\quad
D_j=-r_{4j}^2
=\exp\left\{2\pi i
\left[\sqrt{(4\nu j)^2+\tfrac14}-4\mu j\right]\right\}.
\quad}
\tag{9.6}
$$
因此在这个明确选择的真实正端口 frame 中，谱量确实就是完整
反馈相位；这一步不只是比较其零点集合。

展开仍可给全 $j\ge1$ 的真实余项界：
$$
\boxed{\begin{aligned}
\Theta_j^{\rm PT}
 &=2\pi\left[4(\nu-\mu)\right]j
   +\frac{\pi}{16\nu j}+r_j^{\rm PT},\\
-\frac{\pi}{4096\nu^3j^3}
 &\le r_j^{\rm PT}\le0 .
\end{aligned}}
\tag{9.7}
$$
事实上对 $x\ge0$，
$$
0\le1+\frac x2-\sqrt{1+x}
=\frac{x^2}{2(1+\sqrt{1+x})^2}\le\frac{x^2}{8};
$$
取 $x=(64\nu^2j^2)^{-1}$ 即得 (9.7)。故准确基点系数为
$$
\alpha_{\rm PT}=\frac{44}{89},\qquad
\boxed{\quad \beta_{\rm PT}=\frac{89\pi}{7920}<\frac1{28}.\quad}
\tag{9.8}
$$
基点主旋转数是有理数；其实际径向逆已经由 R25 另证。
本文二次无理门不是用来重新证明这个有理基点。

假如后续真实正常形始终采用已经与本节 frame 识别的相位规范，
并且某个实际判别式 $5$ 的目标已证明
$$
|\beta-\beta_{\rm PT}|\le\frac35,
\tag{9.9}
$$
则
$$
\operatorname{dist}(\beta,\Lambda_5)
>\frac7{10}-\frac35-\frac1{28}
=\frac9{140}>\frac1{16}.
\tag{9.10}
$$
可以在定理 3.1 直接取 $d=1/16$。
这是一项带显式裕量的**条件校准**：要使用 (9.9)，仍须证明当前
真实正常形与此基点的 frame/phase 识别及完整系数增量；
从原 PT 谱量、主射线返回图或一个任意的新端口定义，都不能免费
推出该增量。修改尾、固定帽和非径向扰动也都须计入。


