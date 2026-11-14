# R321：固定六挠 U frame 的三原 primitive、真实六线与完整中央转置

日期：2026-11-13。**状态：本文的五维原降阶、三个规范 primitive、固定六挠 Miller 对数、全部六条原 odd CM 分量，以及普通和惰性处的完整中央转置均已证明。普通式保留全部 p-core、输入环带和单位相加 carry；惰性式保留 Gaussian、移位和解析全尾。R324 的首坏分母是本文同一个 primitive 的分母，不另计为新的中央非零条件。主目标仍未完成。**

## 1. 固定原来源与五维降阶

采用 R297、R307、R316 的同一规范。令 $b=17$，并在恒等式中暂允许一般非零 $b$：
$$
E_b:y^2=x^3+b,\qquad dz=\frac{dx}{2y},\qquad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad \sigma=z+\cdots.
$$
置 $X=x^3$、$\Theta=x\sigma^2$、$F=\Theta^{17}$。三个**实际**来源为
$$
H_i=\sigma^{34}x^2P_i(X),\qquad i=1,3,5,
\tag{1}
$$
其中
$$
\begin{aligned}
P_1={}&X^4-\frac{53b}{7}X^3-\frac{12b^2}{7}X^2
              -\frac{80b^3}{7}X-\frac{128b^4}{7},\\
P_3={}&X^5-208bX^4+400b^2X^3+8128b^3X^2+12032b^4X-2048b^5,\\
P_5={}&X^5+272bX^4-272b^2X^3-14912b^3X^2-6784b^4X+1024b^5.
\end{aligned}
\tag{2}
$$
它们分别来自 $E_{17}$、$E_{17^3}$、$E_{17^5}$；$H_1=z^6+\cdots$，
$H_3(0)=H_5(0)=1$。只有第一条是本有限池的秩二来源。

固定真实五因子参考
$$
\boxed{U=\Theta(z)\Theta(2z)^4
 =\sigma^{34}x^5(X-8b)^4
 =\frac{-336bH_1+5H_3+4H_5}{9}.}
\tag{3}
$$
这里用了真实倍点式 $\Theta(2z)=x(X-8b)\sigma^8$，且 $U(0)=1$。
因此
$$
\frac UF=\left(\frac{X-8b}{X}\right)^4,\qquad
q_U-q_F=\frac{192b\,y}{x(X-8b)},\qquad q_G=G'/G.
\tag{4}
$$
所有 $P_i$ 均被 $X-8b$ 整除。故三个 $H_i/U$ 都属于真实空间
$$
\mathcal V=\operatorname{span}\left\{
1,\frac1X,\frac1{X-8b},\frac1{(X-8b)^2},\frac1{(X-8b)^3}\right\}.
\tag{5}
$$
其极只在 $x=0$ 的两个三挠点和 $X=8b$ 的六个六挠点，阶至多三。
这正是 R320 的固定五维空间。

以下 $D_i$ 是新的 **U-frame** 伴随，不与 R307 的 F-frame $C_{13},C_{15}$ 混同。置
$$
D_i=\sigma^{34}x^3y(X-8b)^2B_i(X)=Ug_i,\qquad
g_i=\frac{yB_i(X)}{x^2(X-8b)^2}.
\tag{6}
$$
全部系数如下：

| $i$ | $B_i(X)$ | $a_i$ | $\gamma_i$ |
|---|---|---|---|
| $1$ | $-3X^2/(448b)-X/28+b/14$ | $-3/(448b)$ | $-3/112$ |
| $3$ | $-X^2/4+28bX+8b^2$ | $3/4$ | $-9b$ |
| $5$ | $-X^2/4-38bX-4b^2$ | $3/4$ | $9b$ |

它们给出完整恒等式
$$
\boxed{\frac{H_i}{U}=g_i'+a_i+\frac{\gamma_i}{X-8b},\qquad
H_i=\nabla_U D_i+a_iU+\gamma_iV_6,}
\tag{7}
$$
其中 $\nabla_U=\partial_z-q_U$，
$V_6=U/(X-8b)=\sigma^{34}x^5(X-8b)^3=z^6+\cdots$。

**精确证明及整性。** 对 $\deg B\le2$，直接求导得
$$
\left(\frac{yB(X)}{x^2(X-8b)^2}\right)'
=\frac{\mathcal N(B)}{X(X-8b)^3},
$$
$$
\mathcal N(B)=6X(X+b)(X-8b)B'
                    -(13X^2+8bX-32b^2)B.
\tag{8}
$$
于是 (7) 等价于五次以下的原多项式恒等式
$$
\frac{P_i}{X-8b}
=\mathcal N(B_i)+a_iX(X-8b)^3+\gamma_iX(X-8b)^2.
\tag{9}
$$
以 $B=1,X,X^2,a,\gamma$ 为五列、次数 $0,\ldots,4$ 为五行，
该原系数矩阵的行列式为
$$-2^{14}3^6b^6.\tag{10}$$
所以这是一份唯一的五维降阶，且在 $p>7$、$p\nmid b$ 时整。
各 $D_i$ 全局全纯，属于同一 degree $34$ 的原 odd 空间。其原点边界为
$$
D_1'(0)=\frac3{448b},\qquad D_3'(0)=D_5'(0)=\frac14,
\qquad D_i'(0)+a_i=H_i(0).
\tag{11}
$$

## 2. 实际六挠 Miller 对数与原点归一

固定 $\theta^6=b$、$\omega^2+\omega+1=0$。令
$$
P_j=(2\theta^2\omega^j,3\theta^3),\qquad
m_j=2\theta\omega^{2j},\qquad j=0,1,2.
$$
有 $2P_j=(0,\theta^3)$，所以 $P_j$ 恰为六挠点。取真实有理函数
$$
f_j=
\left(\frac{y-m_jx+\theta^3}{y+m_jx-\theta^3}\right)^3
\frac{y-\theta^3}{y+\theta^3}.
\tag{12}
$$
分子、分母中的斜线分别是 $P_j,-P_j$ 的切线；它们的第三交点是
$-2P_j,2P_j$。与后面的水平线相乘，得到
$$
\operatorname{div}(f_j)=6(P_j)-6(-P_j),\qquad
f_j(O)=1,\qquad f_j(-z)=f_j(z)^{-1}.
\tag{13}
$$
因此这里的对数可严格取原点值零的局部对数，没有未定乘法常数。
用 $x'=2y,y'=3x^2$ 化简得
$$
\boxed{(\log f_j)'=12\theta\omega^{2j}
                    +\frac{36\theta^3}{x-2\theta^2\omega^j}.}
\tag{14}
$$
注意 (14) 的常项不是零。由
$$
\sum_{j=0}^2\frac{\omega^j}{x-2\theta^2\omega^j}
=\frac{12\theta^4}{x^3-8b}
$$
得到准确规范
$$
\boxed{
L_6(z)=\frac1{432\theta^7}\sum_{j=0}^2\omega^j\log f_j(z)
                       -\frac z{12b},\qquad
L_6'=\frac1{X-8b},\quad L_6(0)=0.}
\tag{15}
$$
特别 $L_6=z^7/7+\cdots$。线性项 $-z/(12b)$ 是真实 Miller 常数的补偿，
不能因它本身的支撑在原点就删掉它乘 $U$ 后的中央贡献。
由导数及原点值的唯一性，$L_6\in\mathbf Q(b)[[z]]$；它在 $\mu_6$ 下
与 $z$ 同型，尽管 (15) 的各单项在更大固定数域中。

故三个规范局部 primitive 为
$$
\boxed{A_i=D_i+a_i zU+\gamma_iUL_6
       =U(g_i+a_iz+\gamma_iL_6),\qquad \nabla_UA_i=H_i.}
\tag{16}
$$
它们满足 $A_i(0)=0,A_i'(0)=H_i(0)$，特别 $A_1=z^7/7+\cdots$。
这给定了整个 primitive；$A_i$ 含真实对数，不被称作全局全纯 theta 截面。

若 $n$ 奇且 $n\equiv1\pmod6$，则真范数 $N_{[n]}f_j$ 与 $f_j$ 同除子。
在 $O$ 用 $Q,-Q$ 配对和 (13) 算出常数为一，所以 $N_{[n]}f_j=f_j$。
这与 R320 的微分迹不变行 $1/(X-8b)+1/(12b)$ 一致；它不是原 theta
中央泛函的等变性断言。

## 3. 三个 D_i 在全部六条真实 odd 来源中的精确坐标

采用 R311 的六条已支付全部局部角色、period 和 p-core 的实际来源 $Y_j$，
其归一为 $Y_j'(0)=1$。索引为
$$
\mathcal J_+=\{5,11,17\},\qquad \mathcal J_-=\{1,7,13\}.
$$
各组的 $T_j$ 是 R311 指定的 $T^3-3T-1=0$ 的三嵌入；保留该处的
角色标签，不能只把三根当作未标定集合。则
$$
\boxed{D_i=\sum_{j\in\mathcal J_+}d_{i,+}(T_j)Y_j
               +\sum_{j\in\mathcal J_-}d_{i,-}(T_j)Y_j,}
\tag{17}
$$
其中

| $i$ | $d_{i,+}(T)$ | $d_{i,-}(T)$ |
|---|---|---|
| $1$ | $-(5T^2-T-31)/(12096b)$ | $(T+1)^2/(6048b)$ |
| $3$ | $-(T^2-5T+1)/36$ | $(T+1)^2/18$ |
| $5$ | $-(2T-3)/12$ | $-(T+1)^2/18$ |

证明只需将 R311 的六个原多项式代入 (6)，并用
$\operatorname{Tr}(1,T,T^2,T^3,T^4)=(3,0,6,3,18)$ 化简。
证书逐系数验证全部恒等式，而不由数值特征向量识别来源。
每个 $d_{i,\pm}(T_j)$ 非零，因为相应二次以下多项式与不可约三次式互素。
因此三个 $D_i$ 各自确有全部六条来源；不能只保其中一个三维块。
(17) 的六个系数之和准确给 (11)。

有两条额外的真实消去：
$$
\boxed{-336bD_1+5D_3+4D_5=0,\qquad D_3+D_5=280bC_X,}
\tag{18}
$$
这里 $C_X$ 是 R311、R316 的同一纯倍点来源
$$
C_X=\frac{\Theta(z)\Theta(2z)^2\sigma(4z)}{2240b}
 =-\frac{\sigma^{34}x^3y(X-8b)^2(X^2+20bX-8b^2)}{560b}.
\tag{19}
$$
(18) 第二式的 minus 三线准确抵消；plus 系数为
$-(T^2+T-8)/36$，而不是把高权来源的非零质量当成原中央非零。

## 4. 同一四因子核的第二个完整 holomorphic 返回

(7)、(18) 给出
$$
\boxed{\begin{aligned}
\nabla_F C_X&=B_F=H_1+\frac{H_3}{336b}-\frac{H_5}{840b},\\
\nabla_U C_X&=B_U=\frac{H_1}{5}+\frac{H_3}{1680b}+\frac{H_5}{840b},\\
B_F-5B_U&=-\frac{H_5}{140b}.
\end{aligned}}
\tag{20}
$$
第二式也由 $H_3+H_5-3U/2=280b\nabla_UC_X$ 直接核定。
两式使用同一个 $C_X$ 和 (4) 的完整连接差。

普通处采用 Amice 规范
$G(\Omega_p\log(1+T))=\int(1+T)^x\,d\nu_G(x)$。
令
$$
\nu=\nu_\Theta\otimes\nu_\Theta\otimes\nu_\Theta\otimes\nu_\sigma,
\qquad y=x_1+2x_2+2x_3+4x_4.
$$
两条实际全测度式是
$$
\boxed{\nu_{B_F}=\frac1{2240b\Omega_p}y_*[w_F\nu],\qquad
\nu_{B_U}=\frac1{2240b\Omega_p}y_*[w_U\nu],}
\tag{21}
$$
$$
w_F=-16x_1+2x_2+2x_3+4x_4,\qquad
w_U=-2x_2-2x_3+4x_4.
\tag{22}
$$
确切地，$q_U=\Theta'/\Theta+8\Theta'(2z)/\Theta(2z)$。
后项平均放到两个相同的 $\Theta(2z)$ 因子，各读 $4x_2,4x_3$；
从原导数 $y$ 减去 $x_1+4x_2+4x_3$，正得 $w_U$。
这同时支付了第一变量的抵消和全部相加变量；没有使用乘法 Mellin。

两个权的 theta 平移异常均为零，即若 $w=\sum\alpha_jx_j$，则
$2\alpha_1+4\alpha_2+4\alpha_3+4\alpha_4=0$。
所以两条是原 holomorphic degree $34$ 返回，而非抽象核中的任意权。
任一 $u$ 的单位 Mellin 都必须在 (21) 中保留 $\mathbf1_{y\in\mathbf Z_p^\times}$。
将 $y=4\widetilde y$ 时，还必须保留
$4\langle4\rangle^{du}$；求导产生的 $d\log_p4$ 乘准确原质量。

## 5. 普通处的原 p-core、全部环带与 U 质量

设 $p>7,p\equiv1\pmod3$，并在同一 $E_{17}$ frame 置
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
v_p(\pi)=1,\quad d=p-1,\quad
\varkappa=p/\bar\pi^2,
$$
$$
\varepsilon=\frac{\psi_0(\mathfrak p)}{\psi_{17}(\mathfrak p)}\in\mu_6,
\qquad T_p=\bar\pi[\bar\pi^2]_*\psi_p.
\tag{23}
$$
R300、R308 的原 even 特征值为
$$
T_pH_i=e_iH_i,\qquad
e_1=1,\quad e_3=\varepsilon^{-2},\quad e_5=\varepsilon^{-4}=e_3^2.
\tag{24}
$$
这里 $\gamma_i$ 专指 (7) 的对数系数，$e_i$ 专指实际 core，相互不混用。

对每条 R311 的原 odd 来源，记 $c_j=\xi_j(\mathfrak p)$。
其完整测度式和 tame-one 行为
$$
\nu_{Y_j}|_{p\mathbf Z_p}=\frac{c_j}{\bar\pi}[\varkappa]_*\nu_{Y_j},
\qquad
\mathcal U_j(u)=\int_{\mathbf Z_p^\times}x\langle x\rangle^{du}\,d\nu_{Y_j}(x),
\tag{25}
$$
$$
\mathcal U_j(0)=\Omega_p\left(1-c_j\frac{\pi}{\bar\pi^2}\right).
\tag{26}
$$
将第 $n$ 环带变量除以 $p^n$ 后，准确有
$$
\mathcal U_j^{[n]}(u)=c_j^n\bar\pi^{-3n}
 \langle\bar\pi\rangle^{-2ndu}\mathcal U_j(u),
\tag{27}
$$
$$
(\mathcal U_j^{[n]})'(0)=c_j^n\bar\pi^{-3n}
\{\mathcal U_j'(0)-2nd\log_p\bar\pi\,\mathcal U_j(0)\}.
$$
故 (17) 给三个 $D_i$ 的整个 core 与全部环带，而不只是有限向量：
$$
\nu_{D_i}|_p=\bar\pi^{-1}[\varkappa]_*
       \sum_jd_{ij}c_j\nu_{Y_j}.
\tag{28}
$$
尤其 $\mathcal U_j'(0)$ 是 $x\log_p\langle x\rangle$ 观察，
不是 (26) 的非零一阶质量。

记 $J_G(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_G(x)$。
原三质量为
$$
m_1=0,\qquad m_3=1-e_3/\bar\pi,\qquad m_5=1-e_5/\bar\pi.
$$
于是
$$
\boxed{m_U=J_U(0)=\frac{5m_3+4m_5}{9}
          =1-\frac{C}{9\bar\pi},\qquad C=5e_3+4e_3^2.}
\tag{29}
$$
这个量永不为零，且对所有普通 $p>7000$ 为单位。证明如下：$e_3=1$ 时
$m_U=m_3$，R308 已证明 $p>7$ 时它是单位。否则 $N_{K/\mathbf Q}C=21$。
若 $m_U$ 非单位，则
$$
p\mid N(9\bar\pi-C)=81p+21-9\operatorname{Tr}(\bar\pi\overline C).
$$
而 $|21-9\operatorname{Tr}(\bar\pi\overline C)|\le21+18\sqrt{21p}<p$
对 $p>7000$ 成立，强迫 $9\operatorname{Tr}(\bar\pi\overline C)=21$，
与迹为整数矛盾。非零性更直接由 $N\bar\pi=p$ 与 $N(C/9)=7/27$ 得出。
有限小素数仍保留 (29) 的实际赋值，不预设其为单位。

### 5.1 四、五因子的全部相加 carry

R316 已支付同 frame 的两条低 degree core：
$$
\nu_\Theta|_p=\frac{\varepsilon}{\bar\pi}[\varkappa]_*\nu_\Theta,
\qquad
\nu_\sigma|_p=\frac{\varepsilon^3}{\bar\pi}[\varkappa]_*\nu_\sigma.
\tag{30}
$$
四输入全非单位部分的系数是 $\bar\pi^{-4}$；对 (22) 的线性权还需乘
$\varkappa$，所以准确系数是 $p/\bar\pi^6$。
在输入域 $\mathbf Z_p^4\setminus(p\mathbf Z_p)^4$、输出 $v_p(y)=n\ge1$
并将 $y$ 除以 $p^n$ 后，两条 $G=B_F,B_U$ 的 carry 均为
$$
\boxed{\bar\pi^{-n}[\bar\pi^{-2n}]_*
 \left((T_p^n-p\bar\pi^{-5}T_p^{n-1})\nu_G\right)^\times.}
\tag{31}
$$
证明是从整个输出第 $n$ 环带减去四输入全在 $p$ 内的第 $n-1$ 环带，
直接应用 (30)，与 R316 的同一证明完全相同。两条权均为一次，故没有
额外的未知 core。若 $G=\sum\alpha_iH_i$，其完整 Mellin 为
$$
\bar\pi^{-n}\langle\bar\pi\rangle^{-2ndu}
 \sum_i\alpha_i(e_i^n-p\bar\pi^{-5}e_i^{n-1})J_{H_i}(u).
\tag{32}
$$
求导保留 $-2nd\log_p\bar\pi$ 乘该层的全部质量。

五因子 $U$ 的相应公式是
$$
\boxed{\bar\pi^{-n}[\bar\pi^{-2n}]_*
 \left((T_p^n-\varepsilon^5\bar\pi^{-4}T_p^{n-1})\nu_U\right)^\times.}
\tag{33}
$$
其中五输入全非单位系数为 $\varepsilon^5/\bar\pi^5$。
原 $T_p^3$ 在这三条 even 来源上等于一；这使 (32)、(33) 留在同一三线，
但不把各 carry 的中央导数置零。

全部输入环带的收敛也不能从未中心化的质量一因子推定。明确置
$$
\eta_\Theta=\nu_\Theta^\times-(1-\varepsilon/\bar\pi)\delta_0,
\qquad \eta_\sigma=\nu_\sigma^\times.
$$
则两者质量为零，且
$$
\nu_\Theta=\delta_0+\sum_{n\ge0}(\varepsilon/\bar\pi)^n
 [\varkappa^n]_*\eta_\Theta,\qquad
\nu_\sigma=\sum_{n\ge0}(\varepsilon^3/\bar\pi)^n
 [\varkappa^n]_*\eta_\sigma.
\tag{34}
$$
R316 的混合有限差分估计给尾项至少 $\sum n_i$ 的赋值增长，故 (21)
及其所有 $u$ 导数可逐项读取。单位输出条件、相加 carry、原点质量均保留。

## 6. 普通处的完整中央式与规范 log distribution

因为 $U(0)=1$ 且其实际 Amice 系数整，$\nu_U$ 有有界的**加法卷积**逆。
原连接测度为
$$
\nu_{q_U}=\Omega_p^{-1}(x\nu_U)*\nu_U^{-1}.
\tag{35}
$$
令
$$
Z_i(u)=\sum_jd_{ij}\mathcal U_j(u),\qquad
Q_i(u)=\iint_{x+y\in\mathbf Z_p^\times}
  \langle x+y\rangle^{du}\,d\nu_{q_U}(x)d\nu_{D_i}(y).
$$
对 (7) 取同一个完整 Mellin，得
$$
\boxed{J_{H_i}(u)=a_iJ_U(u)+\gamma_iJ_{V_6}(u)
                          +\Omega_p^{-1}Z_i(u)-Q_i(u).}
\tag{36}
$$
这里普通处 $V_6(0)=0$ 不表示其单位质量 $J_{V_6}(0)=0$。
所有原点与非单位输入都先进入 (35)、$Q_i$ 的完整卷积后才取单位输出。

用非零的 (29) 定义
$$
\ell_U=J_U'(0)/m_U,\qquad
\mathcal C_U(G)=J_G'(0)-J_G(0)\ell_U.
$$
则三个原中央返回准确为
$$
\boxed{\begin{aligned}
\mathcal C_U(H_i)={}&\gamma_i\mathcal C_U(V_6)
 +\Omega_p^{-1}\{Z_i'(0)-\ell_U Z_i(0)\}\\
 &-\{Q_i'(0)-\ell_U Q_i(0)\}.
\end{aligned}}
\tag{37}
$$
常数项 $a_i$ 只在这份完整质量修正后抵消。
$J_{H_1}'(0)=\mathcal C_U(H_1)$，但另外两条的完整斜率仍在 (29)、(37) 中。
由 R311，$Z_i'(0)$ 还可以逐项写为
$$
\frac12\sum_j d_{ij}\mathcal U_j(0)
 \left(\frac{\mathscr L_j'(0)}{\mathscr L_j(0)}+d\log_p34\right),
\tag{38}
$$
其中 $\mathscr L_j$ 是那六条真实 tame-one Katz 支；其对数导数没有被认为已知。

### 6.1 原点归一 primitive 的实际 distribution

为使 (15)、(16) 中的对数和线性项也在同一完整接口中，设
$f_i=H_i/U$，$\nu_{f_i}=\nu_{H_i}*\nu_U^{-1}$。
对局部解析测试函数 $\varphi$ 定义
$$
\lambda_f(\varphi)=\Omega_p\int
 \frac{\varphi(x)-\varphi(0)}x\,d\nu_f(x),
\tag{39}
$$
在 $x=0$ 用连续值 $\varphi'(0)$。这是阶至多一的真实 distribution，
质量零，并且 $x\lambda_f=\Omega_p\nu_f$。它的 Amice 生成函数恰是
$\int_0^z f(v)dv$ 在 $z=\Omega_p\log(1+T)$ 的值。
故
$$
\nu_{A_i}=\nu_U*\lambda_{f_i},\qquad
\Omega_p^{-1}x\nu_{A_i}-\nu_{q_U}*\nu_{A_i}=\nu_{H_i}.
\tag{40}
$$
这没有将 $A_i$ 错称为有界测度。

对任意 tame 指数 $j$，令
$\varphi_{j,u}(x)=\mathbf1_{x\in\mathbf Z_p^\times}\tau(x)^j\langle x\rangle^{du}$。
完整输入式为
$$
\boxed{M_{A_i,j}(u)=\Omega_p\iint
 \frac{\varphi_{j,u}(x+y)-\varphi_{j,u}(y)}x
 \,d\nu_{f_i}(x)d\nu_U(y).}
\tag{41}
$$
因此原点导数、所有输入环带及跨单位边界的相加项都有明确位置。
没有先把积分分母 $x$ 逐环带丢弃再声称可求导。

取 $\delta_0'(\varphi)=\varphi'(0)$，则 (15) 在同一规范中为
$$
\nu_{L_6}=\frac1{432\theta^7}\sum_j\omega^j
       \lambda_{(\log f_j)'}-\frac{\Omega_p}{12b}\delta_0',
\qquad \nu_{UL_6}=\nu_U*\nu_{L_6}.
\tag{42}
$$
这里 $(\log f_j)'$ 的原 Amice 系数有界，因为其极是 prime-to-$p$
挠点，原点处有固定单位分母。式 (42) 也可直接由有理局部表达 (14) 证明。
原点 distribution 经卷积后有真实单位贡献。

一个直接边界核验是
$$
M_{zU,1}(u+1/d)=\Omega_p(du+1)J_U(u),\qquad
Q_{zU}(u)=duJ_U(u).
\tag{43}
$$
第一式来自对 $x\langle x\rangle^{du}$ 求导；第二式来自
$q_UzU=zU'$。它们完整相减后才得到 $\nabla_U(zU)=U$。
这支付了 (15) 的线性补偿和 (16) 的 $a_i zU$，不能只删其中一项。

## 7. 惰性处的同一 gauge、全尾与首坏分母

现在固定 $p=6s-1>7$、$p\ne17$，令
$$
d=p+1,\quad c_p=[z^d]\log(\sigma/z),\quad
\kappa=34c_p,\quad v_p(\kappa)=-1,
\quad \widehat G=e^{-\kappa z^d}G.
\tag{44}
$$
这是 R301 的真实 Gaussian 系数，所有 degree $34$ 来源使用同一个它。
记 $R=p^{-1/(2p)}$、$R'=p^{-1/(3p)}$。

R301 的证明在 $R'$ 上仍有效：其高尾下界变成
$p/3-3-1/(p^2-1)>1/(p-1)$（$p\ge11$），其余低带亦严格满足指数收敛界。
因此删去准确的 $c_pz^d$ 后，sigma 指数及其逆在 $R'$ 上真实解析、范数一。
又 $R'<p^{-1/(p^2-1)}$，真实高度二形式指数在该盘为等距同构。
从 (3)、(6) 的实际有理表达可得
$$
\|\widehat U\|_{R'}=\|\widehat U^{-1}\|_{R'}=1,\qquad
\|\widehat D_i\|_{R'}\le R'.
\tag{45}
$$
这里只将 $e^{-\kappa z^d}$ 用作形式去项记号；实际解析性由删项后的
sigma 表达给出，并不要求单独该指数在整个圆盘上收敛。

### 7.1 原六挠对数的完整 Gauss 界

每个 $f_j-1$ 在 $R'$ 上的范数至多 $R'$，故
$$
\|\log f_j\|_{R'}\le p^{2/3},\qquad \|L_6\|_{R'}\le p^{2/3}.
$$
这是由 $\sup_{n\ge1}p^{v_p(n)}(R')^n=p^{2/3}$ 得到的全尾界。
高度二指数的次数小于 $p^2$ 的前缀整；$L_6'$ 是原点处整有理函数，
所以这些积分系数只可能有积分分母。由于 $L_6$ 只含 $z^{6j+1}$，
第一个可能的 $p$ 分母在 $z^{5p}$。因此低于 $p^2$ 的尾在 $R$ 上
至多为 $\max\{R^7,pR^{5p}\}=R^7$。次数至少 $p^2$ 的部分则至多
$$p^{2/3}(R/R')^{p^2}=p^{2/3-p/6}<R^7.$$
加上 $[z^7]L_6=1/7$ 是单位，得到
$$
\boxed{\|L_6\|_R=R^7,\qquad \|\widehat U L_6\|_R=R^7.}
\tag{46}
$$

R324 已证明原 $\widehat U$ 及其逆在 $w=z^6$ 的 $w^p$ 以前整，
同一实际有理表达也给 $\widehat D_i$ 相应前缀整。
$\widehat D_1+a_1z\widehat U$ 的线性项由 (11) 消去；其前缀在 $R$ 上
范数至多 $R^7$，次数至少 $6p$ 的尾由 (45) 的较大盘界控制。
结合 (46)，完整规范 primitive 满足
$$
\boxed{\|\widehat A_1\|_R=R^7,\qquad
\|\widehat A_3\|_R,\|\widehat A_5\|_R\le R.}
\tag{47}
$$
故这里实际使用的带对数原来源也有全部 Gauss 尾，不只是一段截断。

### 7.2 与已发表 R324 的准确同一强迫行

R324 对 $u=x^{-1/2}$ 的原系数计算给
$$
p[z^{5p}]L_6\equiv\frac{b^{5s-2}}{10},\qquad
p[z^{5p}]\widehat A_1\equiv-\frac{3b^{5s-2}}{1120}\pmod p.
\tag{48}
$$
其几何卷积正是
$8^{(5s-2)-(3s-1)}9^{3s-1}=2^{p-2}=1/2$。
在次数小于 $6p$ 的窗口，全部负层可写成
$$
\frac{\gamma_1b^{5s-2}}{10p}\,z^{5p}\widehat U
+\text{整系数项}.
$$
但真实连接将该项准确变为
$$
\nabla_{\widehat U}
 \left(\frac{\gamma_1b^{5s-2}}{10p}z^{5p}\widehat U\right)
=\frac{\gamma_1b^{5s-2}}2z^{5p-1}\widehat U.
\tag{49}
$$
因此 $1/p$ 被原 $5p$ 特征值吸收。这个单位强迫行就是 R324 的同一个行，
不是额外非齐次中央方向；其进入五块除幂目标后的 $p^4$ 来源成本亦按 R324 保留。

## 8. 惰性处的完整 Newton 与中央移位式

对本文的实际 $\mu_6$ 不变局部来源 $G$，定义同一功能
$$
J_G(u)=\sum_{h\ge0}[z^{dh}]\widehat G\,\kappa^{-h}(u)_h,
\qquad (u)_h=u(u-1)\cdots(u-h+1).
\tag{50}
$$
若 $\|\widehat G\|_R\le R^r$，系数赋值至少
$$
\left\lceil\frac{h(p-1)+r}{2p}\right\rceil.
\tag{51}
$$
所以它在 $|u|_p<p^{(p-1)/(2p)}$ 上解析；$u=0,-1$ 及全部所需导数合法。
对整数 $k\ge0$，原有限卷积给
$J_G(k)=k!\kappa^{-k}[z^{dk}]G$，没有先对移权假设 Mellin 等变。
这里 $J_U(0)=1$，且 $J_U\in1+p\mathbf Z_p\langle u\rangle$。

令
$$
\widehat W=z\widehat U'/\widehat U,\qquad V_i=D_i/z,
\qquad r_i=V_i(0)=D_i'(0).
$$
$\widehat W$ 范数至多一、常数为零。它和 $V_i$ 的乘积使用原点正规
完整函数，全部尾由 (45)–(47) 控制。形式恒等式
$$
J_{z\partial_zG}(u)=duJ_G(u),\qquad
J_{z^dG}(u)=\kappa^{-1}uJ_G(u-1)
\tag{52}
$$
可在所有非负整数上直接核定，再由解析性延拓。
由于 $zq_U=\widehat W+d\kappa z^d$，(7) 的**完整**转置为
$$
\boxed{\begin{aligned}
J_{H_i}(u)={}&a_iJ_U(u)+\gamma_iJ_{V_6}(u)
 +(du+1)J_{V_i}(u)\\
 &-duJ_{V_i}(u-1)-J_{\widehat WV_i}(u).
\end{aligned}}
\tag{53}
$$
Gaussian 引起的 $-duJ_{V_i}(u-1)$ 与原连接乘法项同时保留。

现在用实际惯性质量定义
$$
\mathcal C_U(G)=J_G'(0)-G(0)J_U'(0).
$$
对 (53) 求导并减质量，准确得到
$$
\boxed{\begin{aligned}
\mathcal C_U(H_i)={}&\gamma_i\mathcal C_U(V_6)
 +J_{V_i}'(0)-r_iJ_U'(0)\\
 &+d\{r_i-J_{V_i}(-1)\}-J_{\widehat WV_i}'(0).
\end{aligned}}
\tag{54}
$$
这里 $V_6(0)=0$，所以在**惰性**规范中
$\mathcal C_U(V_6)=J_{V_6}'(0)$。这与普通式 (37) 中的真实单位质量不同。

若使用规范完整 primitive $A_i$，置 $\mathcal V_i=A_i/z$，则由 (16)
得到更直接但等价的整条式
$$
\boxed{J_{H_i}(u)=(du+1)J_{\mathcal V_i}(u)
 -duJ_{\mathcal V_i}(u-1)-J_{\widehat W\mathcal V_i}(u).}
\tag{55}
$$
此处 $\mathcal V_i(0)=H_i(0)$；特别目标 $\mathcal V_1(0)=0$。
式 (47) 付出了 (55) 的全部对数尾。

线性补偿的独立核验为
$$
J_{\widehat WU}(u)=du\{J_U(u)-J_U(u-1)\},
\tag{56}
$$
代回 $\nabla_U(zU)$ 的转置后才准确剩 $J_U$。
同样，置 $V_L=UL_6/z$，则 $V_L(0)=0$，并有
$$
J_{V_6}(u)=(du+1)J_{V_L}(u)-duJ_{V_L}(u-1)
                                  -J_{\widehat WV_L}(u).
\tag{57}
$$
这把固定六挠 dlog 放入了同一个完整中央功能，而没有将裸微分的迹特征值
直接当成原中央值。

## 9. 本篇支付的接口及仍需控制的同一项

(37)、(54) 是同一原三来源在两种素类下的完整返回。普通处 exact 部分读
六条真实 tame-one 的导数和原连接卷积；惰性处它读 $J_{V_i}'(0)$、
$J_{V_i}(-1)$ 与 $J_{\widehat WV_i}'(0)$。这些项没有由 $\gamma_1\ne0$
或 R320 的有限迹谱而消失。

确切地，R320 已有原 $p=23$ 的检验：$[z^{24}]U/X$ 和
$[z^{24}]U/(X-8b)$ 分别为 $7,5$ 模 $23$。前者属于 exact 微分的真实方向，
后者属于 dlog 方向；所以即使限于这个固定五维空间，原中央功能也不杀 exact。
本文的 (21)、(31)、(37)、(53) 始终保留这些实际行。

因此新第二四因子权及 U-frame 降阶给出可直接计算的完整来源关系；
它们尚未把 $H_1$ 的中央零传播成任一额外独立观察。
两条秩零参考 $H_3,H_5$ 的未知相对斜率也未被换成已知的常项非零。

## 10. 证书与依赖

`scripts/check-jzero-u-frame-original-primitives-and-transpose.py/.json`
给出 39 项精确恒等式检验：原五维行列式、三条完整降阶与首质量、真实 Miller
导数和原点线性补偿、全部六条实际来源的多项式坐标及非零嵌入、同一纯倍点
伴随的两种返回，以及第二四因子权。它没有扫描素数，也没有重复 R324 的证明。
普通全测度、canonical distribution、解析全尾和中央转置由本文正文证明。

- [R301：原高度二半因子与完整 Gauss 界](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)。
- [R307：原三来源与第一次连接](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
- [R308：实际秩零参考的 p-core 与质量](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)。
- [R311：原 odd 六线、tame-one 和纯倍点伴随](R311-jzero-original-odd-six-tame-one-core-and-pure-dyadic-companion.md)。
- [R316：低 degree 原 core 与全四因子 carry](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R320：固定六挠五维迹及完整中央矩阵](R320-fixed-six-torsion-five-dimensional-trace-and-full-central-matrix.md)。
- [R324：首强迫行与五块 Smith 成本](R324-original-u-connection-first-forced-row-and-five-block-smith.md)。
