# R569：R566 固定振荡尾的非零全平角频二无穷小等距场

日期：2026-11-26。**完整定量纸证。root 已逐项核对权变换、单谷逆、DtN 符号、递推、全平导数和完整线性度量。给出实际非零 $C^\infty$ 无穷小等距场，准确固定开平帽；未执行科学数值，不把线性场当成有限弯曲或课题完成。**

背景是 [R566](R566-flat-oscillatory-cap-tail-and-graph-reach.md) 的同一固定函数，未为获得核而另换度量：
$$
r_c=\frac{11}{50},\quad \ell=\frac15,\quad A=\frac1{10},\quad
\delta=\frac{r-r_c}{\ell},\quad
w(r)=A e^{-(2-\sin(\delta^{-2}))/\delta},\quad h'=-w.
$$
令 $w=0,\ h=h(r_c)$ 于 $r\le r_c$。讨论 $r_c<r\le3/10$。

原始文献 Boyang Hu, *Smooth isometric bending of a closed sphere*, 2026，[原文](https://hexagonmath.org/2611.00534v1) §3.2（PDF第19页，命题3.2前及其陈述）给出径向图的线性角模方程。下面独立构造该方程的实际非零解，并最后直接核验全向量场，不依赖其论文存在性结论。

## 1. 要证明的准确命题

存在非零 $f\in C^\infty([r_c,3/10])$，在 $r_c$ 所有阶导数为零，且
$$
(wf')'-4\frac{w'}r f=0\qquad(r_c<r\le3/10). \tag{1}
$$
取
$$
a(r)=\frac{w(r)(4f(r)-rf'(r))}{3},\qquad b(r)=-\frac{a(r)}2,
$$
则对背景 $X_0(r,\theta)=r e_r+h(r)e_z$，向量场
$$
V=a(r)\cos(2\theta)e_r+b(r)\sin(2\theta)e_\theta
       +f(r)\cos(2\theta)e_z \tag{2}
$$
准确满足 $2\operatorname{sym}\langle dX_0,dV\rangle=0$。把 $V=0$ 延拓到整个 $r\le r_c$ 的平盘后，它是一个非零 $C^\infty$ 无穷小等距场，固定一个真正开二维区。

以下给出 $f$ 的规范构造：所有参数固定，剩余无限极限有明确收敛界，无任意未指定的控制数列。

## 2. 化为正权 Sturm–Liouville 方程

置 $f=r^4y$。直接展开 (1) 得
$$
(wr^8 y_r)' +12wr^6y=0. \tag{3}
$$
令
$$
u=\delta^{-2},\qquad r(u)=\frac{11}{50}+\frac1{5\sqrt u}.
$$
向平帽靠近对应 $u\to\infty$。因 $r_u=-\ell/(2u^{3/2})$，(3) 化为
$$
(p(u)y_u)'+\varepsilon(u)p(u)y=0, \tag{4}
$$
其中本组参数恰有 $2A/\ell=1$，故
$$
p(u)=u^{3/2}r(u)^8 e^{-\sqrt u(2-\sin u)},\qquad
\varepsilon(u)=\frac{0.12}{r(u)^2u^3}>0. \tag{5}
$$
这一步保留了 $r(u)$ 的全部变化，没有把半径冻结为常数。

## 3. 精确单谷 cell 和统一初始阈值

在 $u\ge1000$，
$$
(\log p)'=\sqrt u(\cos u-\eta(u)),
$$
$$
\eta(u)=\frac{2-\sin u}{2u}-\frac3{2u^{3/2}}
                    +\frac{0.8}{r(u)u^2}.
$$
有
$$
0<\eta(u)<0.002,\qquad |\eta'(u)|<0.001. \tag{6}
$$
第一式用 $r\ge0.22,\sqrt u>30$ 即得；第二式由逐项微分估计
$$
|\eta'|\le\frac1{2u}+\frac3{2u^2}
 +\frac9{4u^{5/2}}+\frac{0.08}{0.22^2u^{7/2}}
 +\frac{1.6}{0.22u^3}<0.001.
$$

对每个 $n\ge160$，记 $q_n=\pi/2+2\pi n$。存在唯一最大值点
$$
\alpha_n\in(q_n-0.003,q_n)
$$
和唯一最小值点
$$
\gamma_n\in(3\pi/2+2\pi n,\ 3\pi/2+2\pi n+0.003).
$$
证明：零点须满足 $0<\cos u<0.002$，故只可能在上述小窗；在最大值窗内 $-\sin u-\eta'(u)<0$，在最小值窗内它 $>0$，而两端符号相反。其他位置没有零。

于是
$$
I_n=[\alpha_n,\alpha_{n+1}],\qquad 6<|I_n|<7
$$
是一个准确单谷 cell：$p$ 先降至 $\gamma_n$，再升。并且 $\alpha_{160}>1000$。根的唯一性给出有限、可复现的 bracket 定义；无需选择一条未知相位数列。

## 4. 与 contrast 无关的 Dirichlet 逆

先对任意单谷正权 $p$ 在 $I=[a,b]$ 上证明一个引理，长度 $b-a<7$，谷点 $c$。设
$$
R(x)=\int_a^x\frac{dt}{p(t)},\quad R_*=R(b),\quad K=1/R_*,
$$
$$
H_L=1-R/R_*,\qquad H_R=R/R_*.
$$
它们是零势 Dirichlet 插值解。令 $L_0 z=-(pz')'$，使用零 Dirichlet 边界。

### 4.1 无共振

若 $z(a)=z(b)=0$，在左半区 $p$ 单调下降，Cauchy–Schwarz 给
$$
p(x)|z(x)|^2
\le p(x)\left(\int_a^x p|z'|^2\right)
           \left(\int_a^x p^{-1}\right)
\le (x-a)\int_a^c p|z'|^2.
$$
在右半区反向使用 $z(b)=0$ 得对应估计。因此
$$
\int_a^b p|z|^2
 \le \frac{\max((c-a)^2,(b-c)^2)}2\int_a^b p|z'|^2
 < C_0\int_a^b p|z'|^2,\qquad C_0=\frac{49}{2}. \tag{7}
$$
该常数完全不含 $\max p/\min p$。

若 $0\le\varepsilon\le\varepsilon_{\max}$ 且 $\varepsilon_{\max}C_0<1$，则
$L_0-\varepsilon p$ 的零 Dirichlet 二次型严格正定，所以不存在 Dirichlet 共振。

### 4.2 正 Green 核与端点插值界

令 $G$ 为 $L_0^{-1}$ 后再乘权 $p$ 的算子，其核写成
$$
Gz(x)=\int_a^b
 \frac{R(\min(x,t))(R_*-R(\max(x,t)))}{R_*}\,p(t)z(t)\,dt.
$$
直接分 $t\le x$ 和 $t\ge x$ 得
$$
0\le GH_i\le C H_i,\quad i=L,R,
$$
$$
C=\int_a^b p(t)\frac{R(t)(R_*-R(t))}{R_*}\,dt\le C_0. \tag{8}
$$
最后一个不等式在左半使用 $p(t)R(t)\le t-a$，右半使用
$p(t)(R_*-R(t))\le b-t$。

含势 $\varepsilon(u)$ 的准确插值解 $H_i^\varepsilon$ 满足
$$
H_i^\varepsilon=H_i+G(\varepsilon H_i^\varepsilon).
$$
由正 Neumann 级数及 (8)，
$$
H_i\le H_i^\varepsilon
 \le\frac{H_i}{1-\varepsilon_{\max}C_0}. \tag{9}
$$
存在性可由该级数构造，唯一性由 (7) 支付；这里没有假设一个未证明的统一 resolvent。

## 5. 准确 DtN 矩阵及其量级

按外向通量 $(-py'(a),py'(b))$ 定义 $2\times2$ Dirichlet-to-Neumann 矩阵 $D^\varepsilon$。Green 恒等式给
$$
D^\varepsilon_{ij}
 =D^0_{ij}-\int_a^b\varepsilon pH_iH_j^\varepsilon,\qquad
D^0=K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}. \tag{10}
$$
矩阵对称。若 $\varepsilon_{\max}C_0\le1/2$，由 (8)–(9) 得
$$
K\le -D^\varepsilon_{LR}\le2K, \tag{11}
$$
$$
D^\varepsilon_{ii}\le K-\varepsilon_{\min}\int_a^b pH_i^2. \tag{12}
$$
(11) 的相对误差没有付出指数 contrast：因为
$\int pH_LH_R=K C\le K C_0$。

现在取 $I_n$，写 $a=\alpha_n,\ \beta=\sqrt a,\ C_a=r_c^8a^{3/2}$。
在整个 cell 上 $a\le u<a+7$，且 $0.22<r(u)<0.227$，从 (5) 可得
$$
\frac12 C_a e^{-\beta(2-\sin u)}
 \le p(u)\le2C_a e^{-\beta(2-\sin u)}, \tag{13}
$$
$$
a^{-3}\le\varepsilon(u)\le3a^{-3}. \tag{14}
$$
为核对 (13)：幂因子与 $C_a$ 的比在 $1$ 和 $2$ 之间；
$\sqrt u-\sqrt a<1/8$，所以指数额外因子至少 $e^{-3/8}>1/2$。

左右各长 $1/2$ 的端窗内 $\sin u\ge3/4$；以
$3\pi/2+2\pi n$ 为中心的长 $1$ 谷窗内 $\sin u\le-3/4$。故
$$
R_*\ge\frac1{2C_a}e^{11\beta/4},\qquad K\le2C_a e^{-11\beta/4}. \tag{15}
$$
在左端窗 $R(x)/R_*\le2e^{-3\beta/2}<1/2$，右端窗同理，所以
$$
\int pH_L^2,\ \int pH_R^2
 \ge\frac{C_a}{16}e^{-5\beta/4}. \tag{16}
$$
又有
$$
\varepsilon_{\max}C_0\le\frac{73.5}{a^3}<\frac12.
$$
由 (12)、(15)–(16)，因 $32a^3e^{-3\sqrt a/2}<1/2$ 于 $a\ge1000$，
$$
D^\varepsilon_{LL},D^\varepsilon_{RR}
 \le-\frac{C_a}{32a^3}e^{-5\beta/4}<0. \tag{17}
$$
这里的 $a^3e^{-3\sqrt a/2}$ 于 $a>16$ 递减，故统一阈值 $1000$ 足够。

## 6. 无穷 cell 的通量匹配成为对角占优递推

令 $k_n=-D_{n,LR}^\varepsilon>0$，并在内部端点 $\alpha_n$ 置
$$
V_n=-(D_{n-1,RR}^\varepsilon+D_{n,LL}^\varepsilon)>0.
$$
通量匹配准确等价于
$$
k_{n-1}y_{n-1}+V_n y_n+k_ny_{n+1}=0. \tag{18}
$$
前一 cell 的 $C_{\alpha_{n-1}}\le C_{\alpha_n}$，且
$\sqrt{\alpha_n}-\sqrt{\alpha_{n-1}}<1/8$。由 (11)、(15)、(17)，
$$
\frac{k_{n-1}}{V_n}\le256\alpha_n^3e^{-3\sqrt{\alpha_n}/2},
\qquad
\frac{k_n}{V_n}\le128\alpha_n^3e^{-3\sqrt{\alpha_n}/2}.
$$
为留余量，统一记
$$
\mathcal R(a)=512a^3e^{-3\sqrt a/2}<\frac1{64}\qquad(a\ge1000). \tag{19}
$$
最后的纯数值不等式可不用浮点核查：$\sqrt{1000}>30,\ e>2$，故
$$
\mathcal R(1000)
 <512\cdot10^9\cdot2^{-45}<1/64;
$$
再用单调性即可。

置 $y_n=(-1)^{n-160}x_n$。取 $x_{160}=1$，并用正比值
$$
\rho_n=\frac{x_n}{x_{n-1}}
 =T_n(\rho_{n+1}),\qquad
T_n(t)=\frac{k_{n-1}}{V_n-k_nt},\quad n\ge161. \tag{20}
$$
每个 $T_n$ 将 $[0,1/32]$ 映入自身，且
$$
0<T_n(t)\le2\mathcal R(\alpha_n),\qquad
|T_n'(t)|\le
 \frac{(1/64)^2}{(1-1/2048)^2}<10^{-3}. \tag{21}
$$

先令有限末端 $\rho_{M+1}=0$，从后向前算 (20)，再令 $M\to\infty$。
对每个固定 $n$，它是一致 Cauchy 序列，并有明确误差界
$$
|\rho_n-\rho_n^{(M)}|
 \le\frac1{32}\,10^{-3(M-n+1)}. \tag{22}
$$
此界以 cell 的准确 DtN 为输入；实际浮点计算仍须另包围 DtN 误差。

所得 $\rho_n>0$，从而 $x_n=\prod_{k=161}^n\rho_k>0$。
在每个 cell 中，以端值 $y_n,y_{n+1}$ 用
$$
y(u)=y_n H_L^\varepsilon(u)+y_{n+1}H_R^\varepsilon(u) \tag{23}
$$
构造准确解。(18) 保证接口通量匹配。因 $p>0$ 且系数光滑，$y,y'$ 匹配，ODE 再推出全部高阶导数匹配。于是 (23) 是整个 $u\ge\alpha_{160}$ 上的真实非零光滑解，并非离散模型代用品。

## 7. 全平端的导数证明

由 (21)，
$$
\rho_n\le1024\alpha_n^3e^{-3\sqrt{\alpha_n}/2}.
$$
当 $a\ge10000$ 时
$\log1024+3\log a\le\sqrt a/2$，故 $\rho_n\le e^{-\sqrt{\alpha_n}}$。
因 cell 长小于 $7$，
$$
\sum_{k=m+1}^n\sqrt{\alpha_k}
 \ge\frac17\int_{\alpha_m}^{\alpha_n}\sqrt t\,dt
 =\frac2{21}(\alpha_n^{3/2}-\alpha_m^{3/2}).
$$
所以存在常数 $C$ 使
$$
|y_n|\le C e^{-2\alpha_n^{3/2}/21}. \tag{24}
$$
由 (9)、(23)，cell 内 $|y(u)|\le4|y_n|$，因此
$$
|y(u)|\le C'e^{-u^{3/2}/21}
$$
在充分大 $u$ 成立。

这也控制全部导数。将 (4) 写成
$$
y''+(\log p)'y'+\varepsilon y=0.
$$
在长度小于 $7$ 的 cell 上，$(\log p)'$ 及每个固定阶导数只按 $u$ 的某个幂增长。由均值定理可在 cell 内取一点，使
$|y'|\le |y_{n+1}-y_n|/|I_n|$。然后对二阶 ODE 的一阶系统在该 cell 双向使用 Gronwall，至多损失 $e^{C\sqrt u}$；再微分 ODE 即得每个固定阶导数的多项式损失。这些都被 (24) 的 $e^{-c u^{3/2}}$ 压过。

因 $d/dr=-2u^{3/2}\ell^{-1}d/du$，每个固定 $r$ 导数也只增加多项式因子。因此对各固定 $k$，存在 $C_k,c_k>0$：
$$
\left|\frac{d^k}{dr^k}(r^4y)\right|
 \le C_k e^{-c_k/\delta^3}\longrightarrow0. \tag{25}
$$
取 $f=r^4y$，在 $r=r_c$ 零延拓，得到真正 $C^\infty$ 全平解。

## 8. 延伸到整个尾与开平帽

在有限闭区间 $u\in[25/4,\alpha_{160}]$，$p>0$ 且所有系数光滑，故由
$y(\alpha_{160})=1$ 和 (23) 给出的 $y'(\alpha_{160})$，普通 ODE 唯一延伸到 $u=25/4$，即 $r=3/10$。这一步没有宣称其外端 jets 自动匹配任意指定核心；外端实际值和导数由这个规范解决定。

最后核验 (2)。由 (1)，
$$
a'=wf',\qquad a+2b=0,\qquad
-2a-b+2wf+rb'=0.
$$
而背景 $X_{0,r}=e_r-we_z,\ X_{0,\theta}=r e_\theta$，于是
$$
\langle X_{0,r},V_r\rangle=(a'-wf')\cos2\theta=0,
$$
$$
\langle X_{0,\theta},V_\theta\rangle
 =r(a+2b)\cos2\theta=0,
$$
$$
\langle X_{0,r},V_\theta\rangle+
\langle X_{0,\theta},V_r\rangle
 =(-2a-b+2wf+rb')\sin2\theta=0.
$$
所以它是准确无穷小等距场。由 (25) 及 R566 对 $w$ 的全平估计，$a,b,f$ 全部全平；故 $V=0$ 延拓于整个 $r\le r_c$ 时 $C^\infty$，准确固定开平盘。又 $y(\alpha_{160})=1$，所以 $V\ne0$。非零环境刚体无穷小运动不能在开二维盘上恒为零，因此该场非刚性。

## 9. 对下一实际模型的意义和未付款项

这比“无限次 K 变号”更强：同一个 R566 固定函数有一个规范、真实、非零、全平的角频二模式及完整向量无穷小等距场。种子由唯一 bracket 根、无共振有限 cell ODE 和带 (22) 误差界的递推极限定义，没有任意未指定的 sigma 序列。可在公共 Actions 中据此生成带传递误差预算的种子数据，再作为新的逆设计初始化或端部基函数。

它仍不提供有限等距族。直接置 $X_t=X_0+tV$ 会得到
$$
I_{X_t}=I_{X_0}+t^2\langle dV,dV\rangle,
$$
所以二阶及后续非线性修正仍须求解。本文也没有支付外端连接到非圆核心、闭面嵌入、跨块 reach、宏观 hold 幅度或固定 g 的 1e-6 精化。

当前 soft-weight v2 的坏候选不能因这个线性核被重解释为成功；新 R566 Model 和动态硬几何 solver 是另一个明确身份。应继续做它的非线性返回和连续空间门，不在本线性结果处停下。

