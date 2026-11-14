# R337：原 Hadamard 域运输、十二条线管与深度条件的真实中央传播

日期：2026-11-13。**状态：已证明。** 同一原八 sigma 二次核的四变量 Riemann 身份给出一个真正的联合测度分解：保留原相加输出，同时取两个 Hadamard 辅助坐标，经过已付且不改变输出的平均后，准确得到 $\nu_S\otimes\rho\otimes\rho$，其中 $\rho=x\nu_\sigma/\Omega_p$ 是质量一、core 为 $t_p[\kappa]_*\rho$ 的原测度。因此辅助坐标的深度、环带条件确实把原完整中央零传播到相应的实际输入域。另一条真实 CM 对合把 R333 两个二次核的差局限到十二条明确的线管；其整个负矩族和全部尾均保留。两种结论作用的域并不相同，本篇不删去其交叠或补域，也不由单个子域的非零推断原总中央非零。

## 1. 同一来源、原测度和两种相加输出

固定 R297、R316、R333 的
$$
E_{17}:y^2=x^3+17,\qquad
\delta^2=-3,\qquad
\omega=\frac{\delta-1}{2},\qquad
\gamma=\frac{5+\delta}{2}.
$$
普通素数始终满足 $p>7$、$p\equiv1\pmod3$。选定同一原普通嵌入与周期
$\Omega=\Omega_p$。令
$$
\nu=\nu_{\sigma,17},\qquad
\lambda=\frac{\varepsilon^3}{\bar\pi},\qquad
\kappa=\frac p{\bar\pi^2},\qquad
t_p=\lambda\kappa=\frac{\varepsilon^3p}{\bar\pi^3}.
\tag{1}
$$
R316 的整个原测度身份为
$$
\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu,\qquad
\int d\nu=0,\qquad
\int x\,d\nu=\Omega,\qquad
[\zeta]_*\nu=\zeta\nu\quad(\zeta\in\mu_6).
\tag{2}
$$
$\Omega,\lambda,\bar\pi$ 为单位，$v_p(t_p)=v_p(\kappa)=1$。
本文所有乘积均为原有界测度的加法卷积，不把 Mellin 函数拆成乘积。

把八个相同输入分为共同四变量 $\boldsymbol r=(r_1,\ldots,r_4)$ 和
二次权四变量 $\boldsymbol x=(x_1,\ldots,x_4)$。定义
$$
\begin{aligned}
\boldsymbol a&=(1,2,\delta,2\delta),\\
\boldsymbol c_A&=(2,2,\delta,\delta),\\
\boldsymbol c_B&=(5/2,5/2,\delta/2,\delta/2),\\
W(\boldsymbol x)&=(x_1-x_2)^2-(x_3-x_4)^2,\\
y_L(\boldsymbol r,\boldsymbol x)
 &=\boldsymbol a\boldsymbol r+\boldsymbol c_L\boldsymbol x
 \qquad(L=A,B).
\end{aligned}
\tag{3}
$$
R333 已由真正 sigma 加法和 CM7 相位证明
$$
\boxed{\nu_S=-\frac1{168\Omega^2}(y_L)_*
                   \bigl(\nu^{\otimes4}\otimes W\nu^{\otimes4}\bigr),
       \qquad L=A,B,}
\tag{4}
$$
其中 $S$ 是固定秩二曲线的原来源
$$
S=-\frac1{84}\sigma(z)\sigma(2z)\sigma(\delta z)
           \sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z).
\tag{5}
$$
两种 (4) 的输出单位条件各施加于自身的 $y_L$。

对共同变量的开闭域 $R$、二次权变量的开闭域 $D$，记原输出测度
$$
\mathcal K_L(R,D)=
-\frac1{168\Omega^2}(y_L)_*
 \left(\mathbf1_R(\boldsymbol r)\mathbf1_D(\boldsymbol x)
                  \nu^{\otimes4}\otimes W\nu^{\otimes4}\right).
\tag{6}
$$
省略 $R$ 表示 $R=\mathbf Z_p^4$。对任何有界连续测试 $\phi$，
$\mathcal K_L(R,D;\phi)$ 表示相应积分。特别可以完整取
$$
\phi_{\ell,u}(z)=\mathbf1_{\mathbf Z_p^\times}(z)
                    \tau(z)^\ell\langle z\rangle^{(p-1)u}.
\tag{7}
$$
以下测度等式同时给全部 tame、全部原输出环带以及 principal 中央导数。
没有在变换前删除非单位输出。

## 2. 真正四 sigma 身份及其带权联合式

引入两个真实四变量矩阵
$$
B=\frac12
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},\qquad
C=\frac12
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\tag{8}
$$
二者对称，$B^2=C^2=1$，行列式均为 $-1$，所以对所有本篇素数都是
原 $\mathbf Z_p^4$ 的自同构。

### 2.1 不丢 Gaussian 的 sigma 证明

原 reduced sigma 满足
$$
\begin{aligned}
&\sigma(x+u)\sigma(x-u)\sigma(y+v)\sigma(y-v)\\
&\quad-\sigma(x+v)\sigma(x-v)\sigma(y+u)\sigma(y-u)\\
&=\sigma(x+y)\sigma(x-y)\sigma(u+v)\sigma(u-v).
\end{aligned}
\tag{9}
$$
这可直接由两变量加法证明。除以
$\sigma(x)^2\sigma(u)^2\sigma(y)^2\sigma(v)^2$ 后，设
$X=\wp(x),U=\wp(u),Y=\wp(y),V=\wp(v)$，所需式恰为
$$
(U-X)(V-Y)-(V-X)(U-Y)=(Y-X)(V-U).
$$
在无极开集成立后即为整个 sigma 身份。因而这不是一个仅比较首项的
候选公式，也没有另换 theta frame。

代入
$(z_1,z_2,z_3,z_4)=(x+u,x-u,y+v,y-v)$，(9) 准确成为
$$
\prod_{i=1}^4\sigma(z_i)=
       \prod_{i=1}^4\sigma((B\boldsymbol z)_i)
      +\prod_{i=1}^4\sigma((C\boldsymbol z)_i).
\tag{10}
$$
把 $z_i$ 换成原 $\Omega\log(1+T_i)$。由于 $B,C$ 对称，
多变量 Amice 变换的单射性给真正有界测度等式
$$
\boxed{\mu=B_*\mu+C_*\mu,\qquad \mu=\nu^{\otimes4}.}
\tag{11}
$$
所有 $\Omega$ 都来自同一个 E17 原测度；矩阵分母只有二。

### 2.2 实际二次权的精确变换

直接乘法给
$$
W(B\boldsymbol x)=-W(\boldsymbol x),\qquad
W(C\boldsymbol x)=4x_3x_4,
\tag{12}
$$
以及对任意 $(u,u,v,v)$，
$$
B^t(u,u,v,v)^t=(u,u,v,v)^t,\qquad
C^t(u,u,v,v)^t=(u+v,u-v,0,0)^t.
\tag{13}
$$
将 (11) 乘 $W$，并正确把乘子拉回每条支，得到
$$
\boxed{(1+B_*)(W\mu)=4C_*(x_3x_4\mu).}
\tag{14}
$$
特别 $B$ 固定两种实际相加输出，而 $C$ 准确产生两个不再进入输出的
辅助变量。式 (14) 保留了二次权的全部交叉项。

## 3. 两个真实二次参数之间的 CM 域运输

定义
$$
P=
\begin{pmatrix}
0&-\omega&0&0\\
-\omega^2&0&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},\qquad
H=CPC=
\frac14
\begin{pmatrix}
3&-1&\delta&\delta\\
-1&3&\delta&\delta\\
-\delta&-\delta&1&-3\\
-\delta&-\delta&-3&1
\end{pmatrix}.
\tag{15}
$$
$P$ 只交换前两个相同 sigma 输入并乘两个原 $\mu_6$ 相位；
$(-\omega)(-\omega^2)=1$。由 (2)，
$$
P_*\mu=\mu,\qquad
P_*(x_3x_4\mu)=x_3x_4\mu.
\tag{16}
$$
准确矩阵计算又给
$$
H^2=1,\qquad HB=BH,\qquad W\circ H=W,\qquad
H^t\boldsymbol c_A^t=\boldsymbol c_B^t.
\tag{17}
$$
因此 $H$ 是由原 Riemann 和真实 CM 相位得到的变换；并未假设
$H_*\mu=\mu$。真正不变的是 (14) 左端的带权平均：
$$
\boxed{H_*\{(1+B_*)(W\mu)\}=(1+B_*)(W\mu).}
\tag{18}
$$

**域运输命题。** 若 $BD=D$，则对任何共同域 $R$、任何完整测试 $\phi$，
$$
\boxed{\mathcal K_A(R,D;\phi)=\mathcal K_B(R,HD;\phi).}
\tag{19}
$$
若还 $HD=D$，两份原输出测度在该域相等。

证明：$B$ 固定 $y_L$，又保持 $D$，故 (6) 可将 $W\mu$ 换成
$\frac12(1+B_*)(W\mu)$。对这个实际平均使用 (18)，并用
$y_A(\boldsymbol r,H\boldsymbol x)=y_B(\boldsymbol r,\boldsymbol x)$。
由于 $H$ 与 $B$ 交换，$HD$ 仍为 $B$ 不变域，故可把右端平均再去掉。
$R$ 完全不受这些变换作用。这证明整个测度身份，包含 (7) 中原输出单位条件。

## 4. 十二条真实线管精确承载 R333 的差域

对每个整数 $N\ge1$，令
$$
E_N=\coprod_{j=1}^4
 \{x_j\in\mathbf Z_p^\times,\ x_i\in p^N\mathbf Z_p\ (i\ne j)\}.
\tag{20}
$$
这四个原开闭管各约化到一条坐标直线。再定义
$$
F_N=E_N\ \coprod\ BE_N\ \coprod\ HE_N\ \coprod\ BHE_N,
\qquad
T_N=BE_N\ \coprod\ HE_N\ \coprod\ BHE_N.
\tag{21}
$$
下面说明这确为不交并，而不是以点数代替交叠计算。

$B$ 的每个元素均为单位；$H$ 的元素只有
$\pm1/4,\pm3/4,\pm\delta/4$，也都是当前素数处单位。另有准确矩阵
$$
BH=\frac14
\begin{pmatrix}
1&1&\delta+2&\delta-2\\
1&1&\delta-2&\delta+2\\
2-\delta&-\delta-2&-1&-1\\
-\delta-2&2-\delta&-1&-1
\end{pmatrix}.
\tag{22}
$$
其所有元素均为单位，因为 $N_{K/\mathbf Q}(2\pm\delta)=7$。
因此 $BE_N,HE_N,BHE_N$ 的点均有四个单位坐标，不能落在 $E_N$。
由 $B,H$ 是交换对合，把其余任意两个集合的交拉回 $E_N$ 与上述三者的交，
也为空。每一个像内部的四管因矩阵可逆而不交。这付清全部十六管的交叠。

$F_N$ 对 $B,H$ 都不变，故由 (19)，
$$
\mathcal K_A(R,F_N)=\mathcal K_B(R,F_N).
$$
减去 $E_N$，准确得
$$
\boxed{
\mathcal K_A(R,T_N)-\mathcal K_B(R,T_N)
=\mathcal K_B(R,E_N)-\mathcal K_A(R,E_N).
}
\tag{23}
$$
这里十二条像管都是原四单位输入域；输出单位条件仍分别由 $y_A,y_B$ 决定。

### 4.1 与真正恰一单位域的全权身份

令 $D_{L,N}(u)$ 表示 (4) 中八个输入恰有一个为单位、其余七个在
$p^N\mathbf Z_p$ 的 principal 完整函数。共同四变量恰一单位、二次权变量
全部在 $p^N$ 的部分，在 $A,B$ 下准确相等：因为
$p^N\mathbf Z_p^4$ 对 $B,H$ 都不变，可直接用 (19)。

所以取 $R_N=p^N\mathbf Z_p^4$，(23) 给出整个新局限式
$$
\boxed{
\mathcal K_A(R_N,T_N;\phi_{0,u})
-\mathcal K_B(R_N,T_N;\phi_{0,u})
=D_{B,N}(u)-D_{A,N}(u).
}
\tag{24}
$$
$N=1$ 的右端正是 R333 的 $D_B-D_A$。因此原多单位域的全部差
可以精确局限到十二条指定线管，而非扩大到任意有限环境。

R333(17) 对深度 $N$ 的完整式只须将
$\lambda^7\kappa^{\sum r_i}$ 换成
$\lambda^{7N}\kappa^{N\sum r_i}$。特别
$$
\boxed{
D_{B,N}'(0)-D_{A,N}'(0)
=d\,t_p^{7N}\sum_{K\ge0}
                 \kappa^{6NK}\mathfrak b_{K,p}I_{-5-6K},
\quad d=p-1,
}
\tag{25}
$$
其中 $\mathfrak b_{K,p}$ 与 $N$ 无关，由 R333(17) 的真实平方和交叉项
全部相加给出，且
$$
\mathfrak b_{0,p}=\Omega^5\eta,\qquad
\eta=\frac{6267982}{3125}
=\frac{2\cdot7^3\cdot9137}{5^5}.
\tag{26}
$$
$9137$ 是惰性素数，所以 $\eta$ 对本篇全部普通 $p>7$ 为单位。
$K\ge1$ 的全函数尾在 $p^{13N}\mathcal O\langle u\rangle$ 内；
逐项估计为
$$
N(7+6K)-\sum_{i\ne j}v_p((r_i-e_i)!)
\ge N(7+6K)-\left\lfloor\frac{6K}{p-1}\right\rfloor.
\tag{27}
$$
$K=1$ 的阶乘均为单位，$K\ge2$ 的右端至少 $13N$ 并随 $K$ 趋于无穷。
故 (25) 是完整收敛式，所有非单位深度已由原 core 付清。
其中每项在中心由正阶 falling factorial 求导，只留下负矩的值，
没有负矩导数、$\log$ 尺度质量或参考斜率。

若将来能合法地令 (24) 对每个 $N$ 的中央导数都为零，则除以
$d\,t_p^{7N}$ 后令 $N\to\infty$，(25) 已足以迫 $I_{-5}=0$。
更高系数也可依次读出 $\mathfrak b_{K,p}I_{-5-6K}$。
这里没有预设各 $\mathfrak b_{K,p}$ 非零，更没有把这一将来的域控制
当成本篇已得结论。

## 5. 真实质量一辅助测度和整个联合分解

定义同一原 sigma 的带一次权测度
$$
\boxed{\rho=\frac{x}{\Omega}\nu.}
\tag{28}
$$
它是有界整测度；并非把 $\nu$ 的零质量改成一个任意参考。
由 (2) 准确有
$$
\boxed{
\rho(\mathbf Z_p)=1,\qquad
\rho|_{p\mathbf Z_p}=t_p[\kappa]_*\rho,\qquad
[\zeta]_*\rho=\rho\quad(\zeta\in\mu_6).
}
\tag{29}
$$
后一式中的一次权抵消了 $\nu$ 的 $\zeta$ 相位。特别 $\rho$ 是偶测度。

令 $\rho^\times=\rho|_{\mathbf Z_p^\times}$。由于 $v_p(t_p)=1$，
(29) 给真正 Banach 范数收敛的重构
$$
\rho=\sum_{n\ge0}t_p^n[\kappa^n]_*\rho^\times,
\qquad
\left\|\rho-\sum_{n=0}^Mt_p^n[\kappa^n]_*\rho^\times\right\|
\le p^{-(M+1)}.
\tag{30}
$$
这里 $\rho$ 的整范数至多一。因此
$$
\rho(p^m\mathbf Z_p)=t_p^m,\qquad
\rho(p^m\mathbf Z_p^\times)=t_p^m(1-t_p).
\tag{31}
$$
这些是完整原深度质量；没有遗漏 $p$ 内更深环带。

把原八变量带权测度及其实际 $B$ 平均记为
$$
\mathfrak e=-\frac1{168\Omega^2}\nu^{\otimes4}\otimes W\mu,
\qquad
\mathfrak e^{\mathrm{av}}=\frac{\mathfrak e+B_*\mathfrak e}{2},
\tag{32}
$$
其中 $B$ 只作用最后四输入。令 $\boldsymbol q=C\boldsymbol x$，定义
$$
\mathscr T_L(\boldsymbol r,\boldsymbol x)
             =(y_L(\boldsymbol r,\boldsymbol x),q_3,q_4).
$$

**联合测度定理。**
$$
\boxed{(\mathscr T_L)_*\mathfrak e^{\mathrm{av}}
                 =\nu_S\otimes\rho\otimes\rho,\qquad L=A,B.}
\tag{33}
$$

证明：由 (14)，
$$
\mathfrak e^{\mathrm{av}}
=-\frac1{84\Omega^2}
    (1\otimes C)_*(\nu^{\otimes4}\otimes x_3x_4\mu).
$$
换到 $\boldsymbol q$ 后，(13) 表明输出为
$$
\boldsymbol a\boldsymbol r+(u_L+v_L)q_1+(u_L-v_L)q_2,
$$
与 $q_3,q_4$ 无关。$B$ 型的两条 active 尺度恰为 $\gamma,\bar\gamma$；
$A$ 型则满足
$$
2-\delta=-\omega\gamma,\qquad
2+\delta=-\omega^2\bar\gamma.
\tag{34}
$$
两个原 $\mu_6$ 相位乘积为一，所以两型的 active 六输入都准确给 (5)，
系数都是 $-1/84$。余下 $q_3\nu,q_4\nu$ 的 $\Omega^2$ 正好抵消分母，
得到 (33)。这是整个三变量有界测度身份，绝非只读输出的若干矩。

## 6. 原中央零真正传播到哪些输入条件

要把 (33) 用回未平均的原核，必须检查实际域的 $B$ 不变性。准确有
$$
\boxed{CBC=\operatorname{diag}(1,1,1,-1).}
\tag{35}
$$
故在 $q$ 坐标中，$B$ 只改变 $q_4$ 的符号。对任何有界连续
$h(q_3,q_4)$ 满足
$$h(q_3,-q_4)=h(q_3,q_4),$$
测试 $h(q_3,q_4)\phi(y_L)$ 对 $B$ 不变。由 (33) 可去掉平均，得
$$
\boxed{
(y_L)_*\{h(q_3,q_4)\mathfrak e\}
 =\left(\int h\,d(\rho\otimes\rho)\right)\nu_S.
}
\tag{36}
$$
对任意 $h$，同式在 $\mathfrak e^{\mathrm{av}}$ 上成立；
未平均原核只使用上面已证明的偶条件。

### 6.1 深度与环带给准确非零标量

令每个 $A_m$ 为 $p^m\mathbf Z_p$ 或 $p^m\mathbf Z_p^\times$，
每个 $A_n$ 同样选取，$m,n\ge0$。这些集合都对负号不变。
设 $e$ 为两个集合中选择环带的个数。由 (31)、(36)，
$$
\boxed{
\mathcal K_L
 \bigl(\{q_3\in A_m,\ q_4\in A_n\}\bigr)
 =t_p^{m+n}(1-t_p)^e\,\nu_S.
}
\tag{37}
$$
所以相应的整个 tame Mellin 函数是原函数乘同一个常标量。principal 中央为
$$
\boxed{
J_{L;m,n,e}'(0)=t_p^{m+n}(1-t_p)^e J_S'(0).
}
\tag{38}
$$
系数非零，赋值准确为 $m+n$；$m=n=0$ 的双方辅助单位域系数
$(1-t_p)^2$ 为单位。因而这里得到真正的原中央零等价和准确赋值传播，
而不是从有限矩阵可逆推得新零。

(36)–(38) 都先给完整输出测度。若随后取原输出单位、任一更深环带
或任一 tame，仍是相同真实返回；没有把条件与输出 carry 交换而省略边界。
标量不依赖 Mellin 变量，所以这里也没有隐去的 $\log$ 质量项。

### 6.2 共同四输入不能附加条件

**式 (33)、(36)–(38) 中共同四变量 $\boldsymbol r$ 必须取整个
$\mathbf Z_p^4$。** 若另加 $R$，联合身份准确变成
$$
(\mathscr T_L)_*
       \bigl(\mathbf1_R(\boldsymbol r)\mathfrak e^{\mathrm{av}}\bigr)
 =\nu_{L,R}^{(6)}\otimes\rho\otimes\rho,
\tag{39}
$$
其中
$$
\nu_{L,R}^{(6)}
=-\frac1{84}
 \bigl(\boldsymbol a\boldsymbol r+(u_L+v_L)q_1+(u_L-v_L)q_2\bigr)_*
             \bigl(\mathbf1_R\nu^{\otimes4}\otimes\nu^{\otimes2}\bigr).
$$
这是一个真正的受限 active 六输入来源；通常不是 $\nu_S$ 的标量倍数。
例如 $R=p^N\mathbf Z_p^4$ 时，只有前四个尺度被 $\kappa^N$ 改变，
其原 core 系数为 $\lambda^{4N}$，后两个 active 尺度没有同时改变。
不能用原整体 CM 缩放把它误认成 (5)。

因此 (24) 的十二线差域带有 $R_N$，尚不在 (38) 的原零传播断言之内。
这个限制是实际来源公式 (39) 的一部分。

## 7. 十二线管与可控辅助域的精确交叠

由 (8)，每个 $Ce_j$ 的第三、第四坐标都是 $\pm1/2$，且二者相等或相反。
另由 (15)、(35)，
$$
CH=PC,\qquad CB=\operatorname{diag}(1,1,1,-1)C.
\tag{40}
$$
$P$ 保持后两个坐标。因此对 (21) 的每一条实际线管都有
$$
\boxed{
F_N\subset Z_N:=
\{q_3,q_4\in\mathbf Z_p^\times,\
       q_3-q_4\in p^N\mathbf Z_p
       \text{ 或 }q_3+q_4\in p^N\mathbf Z_p\}.
}
\tag{41}
$$
在双方单位条件下，后面两支互不相交，因为 $p$ 为奇数。
特别
$$
F_N\subset Z:=\{q_3,q_4\in\mathbf Z_p^\times\}.
\tag{42}
$$
任一个辅助变量的正深度条件 $q_3\in p\mathbf Z_p$ 或
$q_4\in p\mathbf Z_p$，均与全部十六条线管不相交。
所以不能以 (38) 的任意深度传播直接覆盖 (24) 的非齐次线域。

$Z_N$ 对 $q_4\mapsto-q_4$ 不变，故它本身确是 (36) 的合法域。记
$$
a_{p,N}=
\int_{\mathbf Z_p^\times\times\mathbf Z_p^\times}
\mathbf1_{\{s-t\in p^N\mathbf Z_p\ \text{或}\ s+t\in p^N\mathbf Z_p\}}
                                      \,d\rho(s)d\rho(t).
\tag{43}
$$
则准确有
$$
\boxed{
\mathcal K_L(Z_N)=a_{p,N}\nu_S,\qquad
\mathcal K_L(Z)=(1-t_p)^2\nu_S.
}
\tag{44}
$$
(43) 保留两个原单位输入的全部相加 carry；本篇没有假定 $a_{p,N}$ 为单位，
也没有通过残域点数替代这个带权测度质量。

包含 (41) 严格，且补域可能仍满足真实输出单位条件。
例如取原二次权坐标
$$
\boldsymbol x=(1,2,0,0),\qquad
C\boldsymbol x=(3/2,3/2,-1/2,-1/2).
\tag{45}
$$
它属于所有 $Z_N$，却不属于任何 $F_N$：它有恰两个单位坐标，
而 $F_N$ 的点只有恰一个或四个单位坐标。其原权 $W=1$，
两个 active 输出分别为 $6$ 和 $15/2$，对本篇素数都为单位。
故即使共同四输入在 $p^N$ 内，补域也不能靠“输出非单位”删除。
这里仅确认一个实际开闭域存在，不把有符号测度的非空域等同于非零质量。

完整分解必须写成
$$
\mathcal K_L(F_N)+\mathcal K_L(Z_N\setminus F_N)=a_{p,N}\nu_S
\tag{46}
$$
或在 $Z$ 中保留相应补域。$F_N$ 对两个对合都不变，所以两型的第一项相等；
这仍不使任何一项的中央导数分别为零。若再加 $R_N$，右端须换成 (39)
的 $\nu_{L,R_N}^{(6)}$，不能继续写 $a_{p,N}\nu_S$。

## 8. 本篇实际增加的控制及后续准确接口

本篇的正向结论是两个不同但可相接的原身份：

1. (33)–(38) 给完整联合测度和真正原零传播，涵盖两个 Hadamard
   辅助变量的任意独立深度、环带及更一般的偶测试。特别深度零的双方单位域
   以单位 $(1-t_p)^2$ 无损返回原 $J_S'$。
2. (24)–(27) 将两真实二次核的非齐次差局限为十二条原线管，给任意深度
   $N$ 的完整负矩族，保所有高尾和原相加输出单位边界。
3. (39)、(41)–(46) 精确记录两份控制之间尚未消除的条件：
   十二线差带共同四输入的深度限制，并且它位于辅助变量双方单位的对角管内；
   原已控的正深度域不覆盖它，深度零域仍有真实补域。

R339 的 norm3 链已给同一个 $S$ 的真实独立深度子域非零。
将来若用三变量或四变量联合运输把那一族子域准确纳入原中央控制，
可以把这些非零输入用于主目标。仅使用 (38) 自身或有限群的四个域像，
还没有实现这一覆盖。本篇不把该未付桥梁写成完成。

## 9. 精确证书及来源

生产脚本 check-jzero-original-hadamard-domain-transport.py 与同名 JSON
核定原 $B,C,P,H$、两个二次权拉回、两种实际输出运输、$CBC$ 的符号、
全部 CM7 相位、$BH$ 的每个线代表及其唯一坏素数 $2,3,7$，
并保联合分解的准确系数。有限证书不扫描目标素数。
sigma 身份、测度单射、全部域和收敛证明均在正文，不由数值恒等式替代。

- [R297：实际来源和 CM7 乘积](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R316：原 sigma 的完整 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R327：原单 sigma 二次核与收缩重构](R327-original-single-sigma-quadratic-kernel-and-contracting-reconstruction.md)。
- [R333：六核、两二次核与完整负矩族](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)。
- [R339：同一来源的 norm3 独立深度单位系数](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。

