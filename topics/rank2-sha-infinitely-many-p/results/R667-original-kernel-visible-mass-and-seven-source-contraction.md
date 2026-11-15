# R667 — 原十一维 carry 核的真实可见方向、七条 A 来源与完整 S5 消元

日期：2026-11-15。**状态：已证明。**

本篇保持已经固定的 R594 测试 $q_N$，另构造同一家族中的一个
差测试 $\delta q_N$。它的整个 $\pi_4$ 推前严格为零，并同时保持
原九条补偿约束；然而它在 R664/R665 的共同四输入门上改变
真实条件 A 来源，且其二阶质量具有准确单位尺度。

随后对两个 S 共同域作完整 S5 矩消元，给出含全部七条条件 A
来源的有限公式。原 T 观察仍保全部混合单位 cut。
调用 R665 的同一个负一接口，得到这个算术零差测试的实际
L 深支非零，以及浅域和原 T 外部必须支付的准确补偿。
本篇没有从这些恒等零总行或非零子域推出原中央非零。

## 1. 固定测试之外的真实十一维整核

保持 R594/R659/R664/R665 的全部原规范，
$$
b=17,\quad\omega^2+\omega+1=0,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega\in\mathcal O^\times,
\qquad N\in4\mathbf Z_{\ge1}.
$$
原来源是
$$
\mu_0=\nu_4\otimes\nu_{\rm pair},\qquad
\nu_4=-\mathcal P_{6,C}\nu_\sigma^{\otimes4}/84,
\qquad
\nu_{\rm pair}\longleftrightarrow
\sigma(q+2l)\sigma(2q-l).
\tag{1}
$$
其物理 pair 坐标为 $Q=c+2d,L=2c-d$。
这里 $q,l$ 是生成变量，不是 carry 测试。

R594 的二十个中性列按原次序为
$$
\phi_{ij}=C^iF^jG^{6-i-j},
\qquad1\le i\le5,\quad0\le j\le6-i .
$$
令 $A_p$ 是原九条**完整**约束
$$
(\mathcal M_0,\ldots,\mathcal M_5,L_4,a_{600},\mathcal L_B)
$$
对二十列的矩阵。它保所有 $\lambda,\kappa$ 和
$u_j=(1+\lambda\kappa^j)^{-1}$，不是只取模 $p$。
沿用已付的固定矩阵
$$
A(\tau)=A_++\tau A_0,\qquad
B(\tau)=\frac{B_0+\tau B_1}{\tau-1},\qquad
\tau=(1+\lambda)^{-1},
\qquad A(\tau)B(\tau)=I_9 .
\tag{2}
$$
R594 已证明 $A_pB(\tau)\equiv I_9\bmod p$，且其整逆存在。
定义实际整右逆及核投影
$$
R_p=B(\tau)(A_pB(\tau))^{-1},\qquad
\Pi_p=I_{20}-R_pA_p .
\tag{3}
$$
于是 $A_pR_p=I_9$、$A_p\Pi_p=0$、$\Pi_p^2=\Pi_p$。
因此 $\ker A_p$ 是秩十一的整直和项；这里没有用列数猜秩。

取原零起编号为一的列
$$
e=e_{C F G^4},\qquad
\boxed{v_p=\Pi_pe\in\ker A_p.}
\tag{4}
$$
定义**单独的差多项式**
$$
\delta\widetilde Q_p=\sum(v_p)_{ij}\phi_{ij},\qquad
\delta P_p(D,E,G)=
\delta\widetilde Q_p((E-D)/14,(E+13D)/14,G),
$$
并按原 E 单位逆逐项置
$$
\delta\widehat P_p=\sum_{a+j+k=6}
\frac{[\delta P_p]_{a,j,k}}{1+\lambda\kappa^j}D^aE^jG^k .
\tag{5}
$$
原 $-C^6/8$ 项没有加入差多项式，原 $q_N$ 的系数也未修改。

在 (1) 上可用实际正分支
$$
\delta q_N=
\frac{1_{\{D\in p^N,E\ {\rm unit}\}}}{b\Omega^6}
\delta\widehat P_p(D/\kappa^N,E,G).
\tag{6}
$$
在未平均的原六 sigma 上则使用 R594(25) 的完整六支平均，
只是把其多项式换成 (5)。两个定义按原 C 平均准确对应。

每个 $\phi_{ij}$ 的 $1\le i\le5$ 都被完整 $B_C$ 纤维矩杀掉。
所以 R594 §5 的全域证明逐项给
$$
\boxed{(\pi_4)_*(\delta q_N\mu_0)=0,\qquad
       \pi_4=(Y,W,W',G).}
\tag{7}
$$
同一六支定义在原未平均来源上也给完整零推前。
这是整个四输出的测度恒等式，因而保任意完整 $\pi_4$ 测试。

(4) 另支付原九行的全部差为零，特别原六条网格质量、
$L_4$、$a_{600}$ 和 B 首项均不变。
如果形式上考虑 $q_N+s\delta q_N$，这些已付结论对任意
$s\in\mathcal O$ 都保持。但本文不选择 s、不替换旧测试，
也不把 (7) 推成任意子域的差积分为零。

## 2. 完整核方向与实际二阶质量的精确定标

先给固定特征零证书。令
$$
v(\tau)=e-B(\tau)A(\tau)e
=\frac{v_0+\tau v_1+\tau^2v_2}{\tau-1},
$$
$$
\begin{aligned}
v_0&=-e-B_0A_+e,\\
v_1&=e-B_0A_0e-B_1A_+e,\\
v_2&=-B_1A_0e .
\end{aligned}
\tag{8}
$$
附脚本直接用已发表 R594 两矩阵，精确核对全部四个系数
$$
A_+v_0=0,\quad A_+v_1+A_0v_0=0,\quad
A_+v_2+A_0v_1=0,\quad A_0v_2=0 .
\tag{9}
$$
它没有重算或改写旧右逆。实际 (4) 满足 $v_p\equiv v(\tau)\bmod p$。

保 R665 的
$$
D_*=D_4-aA,\quad a=-(5+6\omega)/29,\quad
H=C+D_*,\quad g=3-2\omega,\quad \ell_0=-3\omega/5,
$$
$$
\mathcal H_N=\{C\ {\rm unit},D_*\in p^N\}.
$$
特别 $\langle D_*,C\rangle=-1$，仍使用 R665 的完整
$(87D_*,429C^\perp,A,R)$ 四轴和实际 $\eta=\pm1$，
不删 C 单位减深域项。

将 (5) 代入 R664(27)，定义
$$
\delta p_N(s)=
\frac{\delta\widehat P_p(D_*/\kappa^N+s/\kappa^N,\,
 H+13C+s,\,13H_1+gH+gs)}{b\Omega^6}
=\sum_{k=0}^6s^k\delta p_{k,N}.
$$
这是在真实 $\mathcal H_N$ 上的准确有限多项式。
其条件来源和二阶系数为
$$
\boxed{
\delta\Lambda_{k,N}
=A_*(1_{\mathcal H_N}\delta p_{k,N}\nu_4),\qquad
\delta J_N=\ell_0^2\,
              \delta\Lambda_{2,N}(\mathbf Z_p).
}
\tag{10}
$$
所有 $p$、N 依赖都按原式保留。定义归一质量
$$
\mathfrak j_{N,p}(v_p)
=2b\Omega^2\lambda^{-N}\kappa^{2N}
       \delta\Lambda_{2,N}(\mathbf Z_p)
=\frac{2b\Omega^2}{\ell_0^2}
       \lambda^{-N}\kappa^{2N}\delta J_N .
\tag{11}
$$
R665(21) 的 whole 四轴返回对任何列都线性成立。
其模 $p$ 值可直接在原四次生成函数上计算。

准确地，对原第 i 列 $P_i(D,E,G)$，置
$$
\begin{aligned}
a_i&=\mathfrak M_4((\partial_D^2P_i)(D_*,E_\perp,G_\perp)),\\
a_i^0&=\mathfrak M_4((\partial_D^2P_i)(D_*,0,G_\perp)),\\
b_i&=\mathfrak M_4((\partial_D^2P_i)(D_*,0,G_{00})),
\end{aligned}
$$
其中 $\mathfrak M_4=\Omega^{-4}\int\nu_4$，
$E_\perp,G_\perp,G_{00}$ 就是 R665(20) 的完整三行。
全部二十组三个矩均保在附 JSON。E 单位逆给
$P_i+(\tau-1)P_i(D,0,G)$；C 单位补项给
$-\eta\lambda\tau b_i$。因 $\lambda\tau=1-\tau$，
完整实际行准确为
$$
\boxed{
j_{\eta,i}(\tau)
=(a_i-a_i^0-\eta b_i)+\tau(a_i^0+\eta b_i).
}
\tag{12}
$$
所以
$$
\mathfrak j_{N,p}(v_p)\equiv
f_\eta(\tau):=j_\eta(\tau)v(\tau)\pmod p .
\tag{13}
$$
此式保两个符号及完整 C 单位补偿，且对全部 N 同时成立。

精确计算给出一个较小的完整结果：
$$
\boxed{
f_+(\tau)=\frac{-c_*+d_+\tau}{\tau-1},\qquad
f_-(\tau)=\frac{c_*+d_-\tau}{\tau-1},
\qquad
c_*=\frac{125125741+70916963\omega}{571536}\ne0 ,
}
\tag{14}
$$
$$
\begin{aligned}
d_+={}&\frac{107829908776938359583443}{192436526439512475120}
 +\frac{827607929906298733481}{2499175668045616560}\omega,\\
d_-={}&\frac{23570079243155395332253}{192436526439512475120}
 +\frac{207405708589386861271}{2499175668045616560}\omega .
\end{aligned}
\tag{15}
$$
原可能的二、三次分子系数准确为零。
这是完整特征零身份；形式参数 $\tau=2$ 的额外记录只是证书内
核对，不能当成任何普通素数的采样。

(8) 的固定分母为
$$
D_{\rm ker}=170084070436718391174838625821679160.
$$
全部附证书有理系数分母的一个公倍数为
$$
D_{667}=
705385329656222448034090561283719092460166564747586106792330496171668594263203434560 .
\tag{16}
$$
保原 $D_{594}$、$D_{665}$ 与所有旧坏集，再删 (16) 的有限素因子。
原 R410 已付 $1+\lambda$ 与 $\tau-1$ 单位，故 (3)–(5) 全部整。

将 (14) 代 $\tau=T/(T-1)$ 并清固定分母，两个分子都是
固定非零 $K[T]$ 多项式。对它们的乘积使用
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)，
在原固定 ray 再删 $O(\sqrt X\log X)$ 个素数后，
两个实际 $f_\eta(\tau)$ 同时为单位。
与 R659/R665 已用的相对密度一子族相交仍为相对密度一。
由 (13) 得到
$$
\boxed{
\mathfrak j_{N,p}(v_p)\in\mathcal O^\times,\qquad
v_p(\delta J_N)=-2N
\quad\text{对所有 }N\in4\mathbf Z_{\ge1}\text{ 同时成立}.
}
\tag{17}
$$
因此原十一维核到这个归一二阶质量的实际整映射满射且饱和：
(4) 就给一个单位像。它不是整个七来源空间的满射断言，
也没有给任意条件 A 测试赋值。

## 3. 七条完整条件来源与两个 S 共同域

R664 已付，(10) 中每条来源仍在真实 whole
$\mathcal S_{29}^{\rm odd}$，角型为 $k-2\bmod6$，并满足
$$
\delta\Lambda_{k,N}|_{A\in p^r}
=(\eta_A\lambda)^r[\kappa^r]_*\delta\Lambda_{k,N},
\qquad \eta_A=\chi_{29,p}\in\{\pm1\}.
\tag{18}
$$
$\kappa^{kN}\delta\Lambda_{k,N}$ 整有界。
其完整质量准确为
$$
\delta\Lambda_{k,N}(\mathbf Z_p)=0\ (k\ne2),\qquad
\delta\Lambda_{2,N}(\mathbf Z_p)=\delta J_N/\ell_0^2 .
\tag{19}
$$
带 A 观察时仍须保七条完整测度；(19) 不能替代它们。

保 R664 的两个真实 S 轴和共同轴：
$$
Y_0=A+Q,\quad Y_1=A+L,\quad
\mathcal E=5A-29(Q+L),
$$
$$
R=Y_0+Y_1,\quad D_{10}=Y_0-Y_1,\quad
B_n=P_{R,\kappa^n}P_{D_{10},\kappa^n}.
$$
$\Gamma_n=\{Y_0,Y_1\in p^n\}$ 的完整核为
$\lambda^{2n}(B_n)_*\mu_0$。
原两个 q 门在 $n\ge N$ 后是
$$
\mathcal G_i=\{C\ {\rm unit},D_*+e_i\mathcal E\in p^N\},
$$
$$
e_0=-(170+117\omega)/9135,\quad
e_1=-(170+291\omega)/9135 .
$$
其共同部分严格为 $\mathcal H_N\cap\{\mathcal E\in p^N\}$，
独占浅支是 $\mathcal G_i\cap\{\mathcal E\notin p^N\}$；
保全部 $0\le v_p(\mathcal E)<N$，不只单位层。

令
$$
h_0=-5-9\omega,\quad h_1=-5-3\omega,\quad t=\kappa^n,
$$
$$
v_0=h_0(34Y_1-29Y_0)/315,\qquad
v_1=h_1(34Y_0-29Y_1)/315.
$$
用 R664(32) 的整个共同 E 深返回，
以 $\delta\mathcal C_{i,n}^S(u)$ 表示差测试的 S 共同行，则
$$
\delta\mathcal C_{i,n}^S(u)
=\lambda^{2n}(\eta_A\lambda)^N
\sum_{k=0}^6\int
(e_i\kappa^N\mathcal E+t v_i)^k
1_{\{Y_i\ {\rm unit}\}}\langle Y_i\rangle^{d_pu}\,
d(\delta\Lambda_{k,N}\otimes\nu_{\rm pair}).
\tag{20}
$$
原 $(-1)^nY_i$ 只在 principal 观察中去掉根单位。
没有改变其它坐标，也没有用一个边际质量替换 (20)。

## 4. 完整 S5 七矩与有限 n 的准确两行消元

在完整 S5 pair 中，对所有 Q 测试，总 L 矩给以下**全来源**：
$$
B_\ell(Q):=(Q)_*(L^\ell\nu_{\rm pair}),\qquad0\le\ell\le6 .
$$

| $\ell$ | $B_\ell$ |
|---:|---|
| 0 | $\nu_{F_{12}}$ |
| 1 | $3\Omega\,\nu_{Z_5}$ |
| 2 | $-4\Omega^2\,\nu_{D_5}$ |
| 3 | $36b\Omega^3\,\nu_{\Sigma_5}$ |
| 4 | $0$ |
| 5 | $720b\Omega^5\,\nu_{X_5}$ |
| 6 | $120b\Omega^6\,\nu_{F_{12}}$ |

这里
$D_5=-xy\sigma^5,\ Z_5=x^2\sigma^5,\ X_5=x\sigma^5$、
$F_{12}=\sigma(z)\sigma(2z)$、$\Sigma_5=\sigma^5$ 全按原规范。

**证明。** R653 的整个 pair 分解是
$$
F_{12}\otimes D_5-D_5\otimes F_{12}
+3Z_5\otimes Z_5
+6b(X_5\otimes\Sigma_5+\Sigma_5\otimes X_5).
$$
各一维角型为 $0,1,2,3,5$；完整 S5 没有型四。
用
$$
D_5=1+(b/6)z^6+\cdots,\quad F_{12}=2z^2+\cdots,\quad
Z_5=z+\cdots,\quad X_5=z^3+\cdots,\quad\Sigma_5=z^5+\cdots
$$
及真实总矩 $\int X^j\nu_F=j!\Omega^j[z^j]F$，
逐项得到表中全部七行。特别第六行的 $120b$ 来自 D5 六阶，
不能遗漏。相反，对总 Q 矩再看 L 来源，表中每行乘
$(-1)^{\ell+1}$；这也由原整数旋转 $\mathsf J_*\mu_0=-\mu_0$
直接给出。证毕。

这些是**总矩**，没有加 L 单位或额外 Euler 因子。
因此它们可用于 (20)，因为对应 S 权不依赖被消去的另一轴。

置
$$
\mathcal H(A,q)=5A-29q,\qquad
\alpha_i=e_i\kappa^N+h_i\kappa^n/315,\qquad
\gamma_i=-29e_i\kappa^N+34h_i\kappa^n/315 .
\tag{21}
$$
对 $i=0$，实际多项式参数为
$\alpha_0\mathcal H(A,Q)+\gamma_0L$；
对 $i=1$，则为
$\alpha_1\mathcal H(A,L)+\gamma_1Q$。
定义有限测度核
$$
\mathscr K_k(\alpha,\gamma;A,dq)
=\sum_{\ell=0}^k
 {k\choose\ell}\alpha^{k-\ell}\gamma^\ell
 \mathcal H(A,q)^{k-\ell}\,dB_\ell(q).
\tag{22}
$$
于是两个 S 共同域的准确消元是
$$
\boxed{
\begin{aligned}
\delta\mathcal C_{0,n}^S(u)
={}&c_{n,N}\sum_{k=0}^6
 \int 1_{\{A+q\ {\rm unit}\}}\langle A+q\rangle^{d_pu}
\,d\delta\Lambda_{k,N}(A)\,
 \mathscr K_k(\alpha_0,\gamma_0;A,dq),\\
-\delta\mathcal C_{1,n}^S(u)
={}&c_{n,N}\sum_{k=0}^6
 \int 1_{\{A+q\ {\rm unit}\}}\langle A+q\rangle^{d_pu}
\,d\delta\Lambda_{k,N}(A)\,
 \mathscr K_k(\alpha_1,-\gamma_1;A,dq),
\end{aligned}
\quad c_{n,N}=\lambda^{2n}(\eta_A\lambda)^N .
}
\tag{23}
$$
第二行的全局负号是实际 $\mathsf J$ 来源号；
余下 $(-1)^\ell$ 才将 $\gamma_1$ 改为 $-\gamma_1$。
这是每个有限 $n\ge N$ 的全来源公式，不是先令 $\kappa^n=0$。

例如 $k=2$ 的两端核为
$$
\begin{aligned}
\mathscr K_2(1,-29)
 &=\mathcal H^2\nu_{F_{12}}-174\Omega\mathcal H\nu_{Z_5}
                      -3364\Omega^2\nu_{D_5},\\
\mathscr K_2(1,29)
 &=\mathcal H^2\nu_{F_{12}}+174\Omega\mathcal H\nu_{Z_5}
                      -3364\Omega^2\nu_{D_5}.
\end{aligned}
\tag{24}
$$
它们分别是 (23) 在 $\kappa^n\to0$ 时除去 $(e_i\kappa^N)^2$
后的二阶核。虽 (17) 已知 $\delta\Lambda_2$ 的非零质量，
(23)–(24) 的真实 A 混合单位权仍不能换成裸 Q 负矩或 log 矩。

T 的权则按 R664(33) 完整保持
$$
\zeta_{i,n}^T
=w_i\kappa^N\mathcal E
+t(W_i-w_i\mathcal E)+((-1)^n-t)b_YY_i ,
\tag{25}
$$
$$
w_0=(-8-18\omega)/315,\quad w_1=(-4+6\omega)/315,\quad
b_Y=(20+3\omega)/17 .
$$
它依赖被消去的另一个 pair 输入，故不得直接将上述总矩表用于
T 的混合单位 cut。其准确式仍是 (20) 换用 (25)，保原完整 pair。

## 5. 算术零差测试的全部共同域、浅域与外部

令 $\delta q_i=\delta q_N\circ\mathsf J^{-i}$。
用 R664(22) 的原 $Y_i$ 深词、相同逆观察和相同归一，
以差测试定义完整 $\delta\mathcal F_{i,n}^Z(u)$，
$Z=S,T$。由 (7) 及真实整数旋转，
$$
\boxed{\delta\mathcal F_{i,n}^Z(u)=0
       \quad(i=0,1;\ Z=S,T)}
\tag{26}
$$
是全 Mellin 函数身份，不需要先假设 $J'_S$ 或 $J'_T$ 为零。

仍令 $\delta\mathcal O_{i,n}^Z$ 为真实
$\{Y_i\in p^n,Y_{1-i}\notin p^n\}$ 外部，
$\delta\mathcal L_{i,n}^Z$ 为共同 $\Gamma_n$ 返回后
$\mathcal G_i\cap\{\mathcal E\notin p^N\}$ 的独占浅支。
则实际全域分区准确给
$$
\boxed{
\delta\mathcal O_{i,n}^Z+
\delta\mathcal L_{i,n}^Z+
\delta\mathcal C_{i,n}^Z=0 .
}
\tag{27}
$$
(23) 是其中 S 共同部分的有限七来源精确表达；
(25) 是 T 共同部分的全混合观察。
所有量使用同一个 $\delta q_i$，不能将两边不同的门或观察抵消。

这里新增的实质不是又多给原中央一个零：
(26) 本来就由原测试族的完整推前支付。
新增的是 (17) 表明该核在实际条件来源上非平凡且饱和，
而 (23)、(27) 把这种变化接到两个真实原算术词的完整补偿。

## 6. 同一负一深支的非消失与无条件补偿

R665 的完整证明对 carry 多项式线性成立。
用 (5) 的差多项式定义冻结权 $\delta p_{0,N}$、
同一混合观察 $\delta\Theta_\pm$，
并在同一真实 L 深域 $L\in p^n$ 取差
$\delta\Delta_{N,n}$。
所有原门和两个 $b_LL\pm b_YQ$ 单位 cut 不变。

原角型仍只留下 L 二阶项，其系数正是 (10)。
因此
$$
\boxed{
\delta\Delta_{N,n}
=2\beta^n\kappa^{2n}\delta J_N\,
              \mathscr H_p(\kappa^n),
}
\tag{28}
$$
其中 $\mathscr H_p$ 完全是 R665(11) 的同一负矩级数，
没有新加独立负矩来源。R655 已付原 $I_{\Sigma_5,-1}\ne0$；
R665 的完整统一尾界给
$$
\delta\Delta_{N,n}
=72b\Omega^3(b_L/b_Y)\,\delta J_N\beta^n\kappa^{3n}
 I_{\Sigma_5,-1}+\delta J_Np^{5n}\mathcal O .
\tag{29}
$$
故在 (17) 的同一无限子族，
$$
\boxed{
v_p(\delta\Delta_{N,n})
=3n-2N+v_p(I_{\Sigma_5,-1}),
\quad n\ge N,\quad 2n>v_p(I_{\Sigma_5,-1}).
}
\tag{30}
$$
密度引理只用于固定函数 (14)，没有套到 p 依赖的负一矩。

令 $\delta\mathcal R_{N,n}$ 为 R665(33) 的完整 L 浅补域，
仅把冻结权换为 $\delta p_{0,N}$；
令 $\delta\mathcal E_\pm$ 为 R662/R665 中同一个原 T 外部词的
正确归一 log 极限。由于差测试的整个 T 总行在 (26) 中恒为零，
此时无需假设原 $J'_T=0$，就有
$$
\boxed{
\delta\mathcal E_+-\delta\mathcal E_-+
\delta\mathcal R_{N,n}
=-\delta\Delta_{N,n}\ne0 .
}
\tag{31}
$$
(30) 给左边完整补偿和的准确赋值。
其中 $\delta\mathcal R$ 保原 L 不深域及两个不同混合单位 cut，
$\delta\mathcal E_\pm$ 保原 Y/A 外部、正确 $Q/p^m$ 尺度和
同一差测试；任何一项都没有单独赋零。

相邻 n 的浅域仍准确满足
$$
\delta\mathcal R_{N,n+1}-\delta\mathcal R_{N,n}
=\delta\Delta_{N,n}-\delta\Delta_{N,n+1},
\tag{32}
$$
其已付首项含真实单位 $1-\beta\kappa^3$。
这说明原十一维核可改变已知非零的真实深/浅补偿，
同时所有完整算术总行保持恒零。

接下来的缺口是 (27) 与 (31) 中这些实际补偿之间的附加关系。
不能由 (17)、(30) 或七条有限来源本身将它们删除。
原固定 $q_N$ 的 S/T 中央问题与所有原外部仍完整保留。

## 精确文件

- [check-r667-kernel-visible-mass-and-seven-source-contraction.js](../scripts/check-r667-kernel-visible-mass-and-seven-source-contraction.js)
- [check-r667-kernel-visible-mass-and-seven-source-contraction.json](../scripts/check-r667-kernel-visible-mass-and-seven-source-contraction.json)

脚本只读取已发表 R594 的二十列和固定右逆，
精确构造 (8)、核验 (9)、计算全部二十组三个四次矩及两个实际
$\eta$ 函数，并核完整 S5 矩表的原 sigma 系数。
实际 $\lambda,\kappa$ 整提升、所有 N 的单位量词、完整条件来源
和全部算术补域由正文支付。

主要依赖：
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md) 的原九行整右逆及六支来源；
[R653](R653-original-five-degree-kernel-and-native-rows.md) 的完整 S5 pair；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md) 的两个原 S 词与七条条件 A 来源；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md) 的原完整二阶系数、负一深支与全部浅补域。
