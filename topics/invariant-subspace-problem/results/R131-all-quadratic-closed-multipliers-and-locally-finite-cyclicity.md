# R131：全部二阶闭乘子及局部有限二阶循环性

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：本稿的实际二阶闭乘子定理已完整证明。实际 carry 估计由 critical_kernel 的独立稿 R130 提供，且已逐节交叉核验。父代理预留 R131 登记本稿。一般二阶 gauge 同域与核排除仍未证明。

**主结论。** 对任意
$$
f=a_*+\sum_j a_j\chi_j+\sum_{i<j}b_{ij}\chi_i\chi_j,
\qquad a\in\ell^2,\quad b\in\ell^2(\{i<j\}),
$$
真实有限系数乘子在 $\mathscr D=\bigcup_pH_{\le p}$ 上逐点收敛，所得算子可闭，其闭包 $X_f$ 满足
$$
X_f^*=CX_fC.
$$
有限柱是 $X_f$ 的图核。每个 $T\in\{A\}'$ 保持 $\operatorname{Dom}X_f$，并在该域上满足 $X_fT=TX_f$。此外
$$
\overline{\operatorname{Ran}X_f}=\operatorname{cyc}_A(f).
$$
因而一般二阶循环性精确归结为这个已确定闭乘子的核是否为零。本稿没有把核排除包含在结论中。

## 1. 一个自含的次数对易子引理

设 $\mathscr H=\bigoplus_{q\ge0}\mathscr H_q$，$\Lambda|_{\mathscr H_q}=(q+1)I$，$\mathscr D$ 为有限次数向量的并。设 $D$ 在 $\mathscr D$ 上对称，并满足
$$
\|Dx\|\le a\|\Lambda x\|,
\tag{1.1}
$$
以及形式对易子界
$$
|c(x,y)|
:=|\langle Dx,\Lambda y\rangle-\langle\Lambda x,Dy\rangle|
\le b\|\Lambda^{1/2}x\|\|\Lambda^{1/2}y\|.
\tag{1.2}
$$
则 $D$ 本质自伴。

**证明。** (1.1) 使 $D$ 从 $\mathscr D$ 连续延拓到
$\operatorname{Dom}\Lambda$ 的图范数，且该延拓包含在 $\overline D$ 中，因为有限次数截断是 $\Lambda$ 的图核。以下仍记这个延拓为 $D$。(1.2) 亦延拓到该域。

令
$$
J_\varepsilon=(I+\varepsilon\Lambda)^{-1},
\qquad B_\varepsilon=DJ_\varepsilon.
$$
$B_\varepsilon$ 为全空间有界算子。对 $x,y\in\mathscr H$，置
$u=J_\varepsilon x,v=J_\varepsilon y$，利用
$x=u+\varepsilon\Lambda u$、$y=v+\varepsilon\Lambda v$，得到
$$
\langle B_\varepsilon x,y\rangle
-\langle x,B_\varepsilon y\rangle
=\varepsilon c(J_\varepsilon x,J_\varepsilon y).
\tag{1.3}
$$
所以 $B_\varepsilon-B_\varepsilon^*$ 是由右侧有界形式给出的算子。

若 $\xi\in\ker(D^*-i)$（另一符号相同），则
$$
B_\varepsilon^*\xi=J_\varepsilon D^*\xi=iJ_\varepsilon\xi.
$$
因此
$$
DJ_\varepsilon\xi
=iJ_\varepsilon\xi+(B_\varepsilon-B_\varepsilon^*)\xi.
$$
左侧与 $J_\varepsilon\xi$ 的内积为实数，因为该向量位于
$\operatorname{Dom}\Lambda\subseteq\operatorname{Dom}\overline D$。取虚部，(1.2)—(1.3) 给
$$
\|J_\varepsilon\xi\|^2
\le b\varepsilon
\|\Lambda^{1/2}J_\varepsilon\xi\|
\|\Lambda^{1/2}J_\varepsilon^2\xi\|
\le b\varepsilon\|\Lambda^{1/2}J_\varepsilon\xi\|^2.
\tag{1.4}
$$
谱演算及支配收敛给
$$
\varepsilon\|\Lambda^{1/2}J_\varepsilon\xi\|^2
=\int\frac{\varepsilon\lambda}{(1+\varepsilon\lambda)^2}\,
d\mu_\xi(\lambda)\longrightarrow0,
$$
因为被积函数不超过 $1/4$ 且逐点趋零。$J_\varepsilon\xi\to\xi$，故
$\xi=0$。两缺陷空间均为零，从而 $\overline D$ 自伴。若要避免使用缺陷空间判据，闭对称算子 $\overline D\pm i$ 的值域由
$\|(\overline D\pm i)x\|^2=\|\overline Dx\|^2+\|x\|^2$ 闭，缺陷空间零又使它稠密，故满射；这等价于自伴。证毕。

此证明没有把仅有正半径的解析向量幂级数当成整个实轴上的指数群。

## 2. 二阶纯乘子的各次数块

令
$$
f=a_*+\sum_ja_j\chi_j+\sum_{i<j}b_{ij}\chi_i\chi_j,
\qquad a\in\ell^2,\quad b\in\ell^2(\{i<j\}).
$$
设
$$
V_j^0=I-2E_j=c_j-c_j^*+2P_j,
$$
其中 $c_j$ 是不重复创建，$P_j=c_jc_j^*$。定义纯乘子
$$
S_f^0=a_*I+\sum_ja_jV_j^0+\sum_{i<j}b_{ij}V_i^0V_j^0
$$
于 $\mathscr D=\bigcup_pH_{\le p}$。

以下给出不使用指数次数常数的二阶界。记对称零对角矩阵
$B_{ij}=b_{ij}$（$i<j$）、$B_{ji}=b_{ij}$，则
$\|B\|_{\rm HS}=\sqrt2\|b\|_2$。

二阶部分分成以下五种次数位移：

- $+2$：$C_b=\sum_{i<j}b_{ij}c_ic_j$；
- $-2$：$\sum_{i<j}b_{ij}c_i^*c_j^*$；
- $0$：$-\sum_{i\ne j}B_{ij}c_ic_j^*+4\sum_{i<j}b_{ij}P_iP_j$；
- $+1$：$2\sum_{i\ne j}B_{ij}c_iP_j$；
- $-1$：$-2\sum_{i\ne j}B_{ij}c_i^*P_j$。

在纯 $q$ 阶上有：

$$
\|C_b\|\le\sqrt{\binom{q+2}{2}}\|b\|_2,
\qquad
\|\text{删除二阶}\|\le\sqrt{\binom q2}\|b\|_2.
\tag{2.1}
$$
前者由对输出 $q+2$ 元集合按其中的二元子集作 Cauchy–Schwarz 得到，后者取伴随。

交换项满足
$$
\left\|\sum_{i\ne j}B_{ij}c_ic_j^*\right\|_{H_{=q}}
\le q\|B\|_{\rm op}\le\sqrt2q\|b\|_2.
\tag{2.2}
$$
可将无重复 $q$ 元集合的标准基等距嵌入归一化对称 $q$ 重张量基；该算子恰为
$\sum_{\ell=1}^qB^{(\ell)}$ 在无重复子空间的压缩。替换后产生重复指标的张量由压缩丢弃，其余转移系数正为 $B_{ij}$。

对创建加占据项，输出集合 $G$、$|G|=q+1$ 的系数为
$$
\sum_{i\in G}\left(\sum_{j\in G\setminus\{i\}}B_{ij}\right)
x_{G\setminus\{i\}}.
$$
先对 $i$ 作 Cauchy–Schwarz，再按输入 $F$ 求和，得到
$$
\left\|\sum_{i\ne j}B_{ij}c_iP_j\right\|
\le\sqrt{q(q+1)}\|B\|_{\rm HS}.
\tag{2.3}
$$
其伴随给删除加占据项同样的线性次数界。最后
$$
\left\|\sum_{i<j}b_{ij}P_iP_j\right\|_{H_{=q}}
\le\sqrt{\binom q2}\|b\|_2.
\tag{2.4}
$$

第一阶部分由 R125 的创建／删除／对角估计控制为 $O(\sqrt{q+1})$。因此存在
$$
K_f\le C\bigl(|a_*|+\|a\|_2+\|b\|_2\bigr)
$$
使每个次数块满足
$$
\boxed{
\|1_{H_{=q+\delta}}S_f^0|_{H_{=q}}\|
\le K_f(q+1),\qquad |\delta|\le2,
}
\tag{2.5}
$$
其他块为零。有限系数截断在这些界下收敛，故它们定义了完整的平方可和二阶符号算子，不要求有限秩。

## 3. 纯二阶 Dirac 的闭包

通常形式伴随为
$$
(S_f^0)^\dagger=CS_f^0C,
$$
因为不同位的 $V_j^0$ 交换，各自 $C$ 对称。构造
$$
\mathscr D_f^0=
\begin{pmatrix}
0&(S_f^0)^\dagger\\
S_f^0&0
\end{pmatrix}
$$
于 $\mathscr D\oplus\mathscr D$，并把
$\Lambda=N_{\rm Walsh}+1$ 对角作用于两个分量。

(2.5) 和有限带宽直接给
$$
\|\mathscr D_f^0x\|\le C_f\|\Lambda x\|.
\tag{3.1}
$$
对易子形式在 $q\to q+\delta$ 块上只增加因子 $\delta$。因为
$|\delta|\le2$，且
$$
q+1\le\sqrt3\sqrt{(q+1)(q+\delta+1)}
$$
对所有存在的块成立，逐个 $\delta$ 作 Cauchy–Schwarz 得
$$
|\langle\mathscr D_f^0x,\Lambda y\rangle
-\langle\Lambda x,\mathscr D_f^0y\rangle|
\le C_f\|\Lambda^{1/2}x\|\|\Lambda^{1/2}y\|.
\tag{3.2}
$$
所以 §1 引理适用，纯 Dirac 本质自伴。

如在 R125 中，块图范数分解给
$$
\boxed{
(\overline{S_f^0})^*=C\overline{S_f^0}C.
}
\tag{3.3}
$$
有限柱是图核：对固定次数输入作有限坐标条件期望，(2.5) 给同层图收敛，再利用初始域的图核定义即可。

## 4. 实际 carry 的已证接口

critical_kernel 的独立完整证明见
2026-11-12-quadratic-carry-number-weight-estimates-0c-agent.md（R130）。
该稿的局部字串、逆算子定义域、排序级数和无界扰动例均已由本稿作者独立核验。令
$$
R_f=S_f-S_f^0.
$$
在 $\mathscr D$ 上已经证明
$$
\|R_fx\|+\|[N_{\rm Walsh},R_f]x\|
\le C_f\|\Lambda^{1/2}x\|,
\tag{4.1}
$$
并对形式伴随 $CR_fC$ 同样成立。这里 $R_f\mathscr D\subseteq\operatorname{Dom}N_{\rm Walsh}$，对易子是该域上真实的算子对易子。一个可用常数是
$$
C_f=
2000\left(\sum_{j\ge0}(j+1)\eta_j^2\right)^{1/2}
(\|a\|_2+\|b\|_2).
$$

为明确本稿实际使用了什么，局部估计为
$$
\|V_j-V_j^0\|\le8\eta_j,\qquad
\|[N_{\rm Walsh},V_j-V_j^0]\|\le126\eta_j.
$$
它们由真实 carry 字串
$$
N_j-E_j=
\sum_{\ell\ge1}\frac{\alpha_{j+\ell}}{\alpha_j}
E_j^*E_{j+1}^*\cdots E_{j+\ell-1}^*E_{j+\ell}
$$
以及 $(I+N_j)^{-1}$ 的 Neumann 级数在次数图范数中的绝对收敛得到；没有把算子范数收敛本身当作定义域保持。

实际二阶差的排序恒等式为
$$
\sum_{i<j}b_{ij}
\bigl[(V_i-V_i^0)V_j^0+V_i(V_j-V_j^0)\bigr].
\tag{4.2}
$$
第一部分按 $i$ 聚合后是小误差算子乘纯第一阶行，给
$O(\sum_i\eta_i\|\mathrm{row}_i\|_2)\|\Lambda^{1/2}x\|$。
第二部分对固定 $j$ 只有 $j$ 个更低位，给
$O(\sum_j\sqrt j\,\eta_j\|\mathrm{col}_j\|_2)\|x\|$。
上述局部差及其次数对易子都是 $O(\eta_j)$，故相同排序对对易子成立。由 Cauchy–Schwarz，两和均由平方可和的二阶核控制。任意有限系数逼近都在
$\mathcal B(\operatorname{Dom}\Lambda^{1/2},H)$ 中收敛；对易子也如此。若 $x\in\mathscr D$，有限部分的
$$
N_{\rm Walsh}R_{\rm fin}x
=R_{\rm fin}N_{\rm Walsh}x+[N_{\rm Walsh},R_{\rm fin}]x
$$
两端收敛，$N_{\rm Walsh}$ 的闭性给上述真实定义域结论。

注意实际误差一般不是全空间有界：固定低位的 $O(\eta_i)$ 误差仍可能乘一个无界第一阶行。正确接口是 (4.1)。

## 5. 实际二阶闭乘子的完整定理

### 5.1 初始算子、通常形式伴随与 Dirac

令 $f_n$ 为任意有限系数逼近，$T_n$ 为对应有限实际乘子：
$$
T_n=a_*I+\sum_{j\in I_n}a_jV_j
+\sum_{(i,j)\in J_n}b_{ij}V_iV_j.
$$
由 §2、§4，对每个 $x\in\mathscr D$，$T_nx$ 收敛；极限记为 $S_fx$。同样
$T_n^*x=CT_nCx$ 收敛到 $S_f^\dagger x=CS_fCx$。有限部分满足通常伴随配对恒等式，取极限得
$$
\langle S_fx,y\rangle=\langle x,S_f^\dagger y\rangle
\qquad(x,y\in\mathscr D).
$$
故二者都可闭，且实际 Dirac
$$
\mathscr D_f=
\begin{pmatrix}0&S_f^\dagger\\S_f&0\end{pmatrix},
\qquad
\operatorname{Dom}\mathscr D_f=\mathscr D\oplus\mathscr D,
$$
为稠密定义的对称算子。

其纯部分满足 (3.1)—(3.2)。误差块
$$
\mathscr R_f=\begin{pmatrix}0&CR_fC\\R_f&0\end{pmatrix}
$$
由 (4.1) 满足 $\|\mathscr R_fx\|\le C_f\|\Lambda^{1/2}x\|$，且像在
$\operatorname{Dom}\Lambda$ 中。对初始域上的 $x,y$，
$$
\begin{aligned}
&\langle\mathscr R_fx,\Lambda y\rangle
-\langle\Lambda x,\mathscr R_fy\rangle\\
&\qquad=\langle[\Lambda,\mathscr R_f]x,y\rangle,
\end{aligned}
$$
其绝对值不超过
$C_f\|\Lambda^{1/2}x\|\|\Lambda^{1/2}y\|$。
所以实际 Dirac 也满足 §1 的两个假设，因而本质自伴。这里没有假设实际误差保有限次数，也没有把它说成相对纯 Dirac 的有界扰动。

### 5.2 C 自伴性与有限柱图核

置 $X_f=\overline{S_f}$。由于
$$
\|\mathscr D_f(x,y)\|^2
=\|S_fx\|^2+\|S_f^\dagger y\|^2,
$$
Dirac 的图闭包按两个分量分开，等于
$$
\overline{\mathscr D_f}
=
\begin{pmatrix}
0&\overline{S_f^\dagger}\\
X_f&0
\end{pmatrix}
$$
于 $\operatorname{Dom}X_f\oplus\operatorname{Dom}\overline{S_f^\dagger}$。
该块算子自伴，故
$$
\boxed{X_f^*=\overline{S_f^\dagger}=CX_fC.}
\tag{5.1}
$$

$\mathscr D$ 按定义为 $X_f$ 的图核。若 $x\in H_{\le p}$，以有限坐标条件期望 $x_m$ 逼近，则 $x_m\in H_{\le p}$，$x_m\to x$，而
$$
\|S_f(x_m-x)\|\le C_f'(p+1)\|x_m-x\|\longrightarrow0
$$
由纯部分的 (2.5) 及进位的 (4.1) 得到。每个 $x_m$ 是有限柱。因此有限柱也是 $X_f$ 的图核。

### 5.3 所有有界交换算子的真实域交换

取任意 $T\in\{A\}'$。每个 $T_n$ 是 $A$ 的有界解析函数，故与 $T$ 交换。又 $T_n$ 对双线性型
$B(u,v)=\langle u,Cv\rangle$ 对称。对于 $x,z\in\mathscr D$，
$$
B(Tx,T_nz)=B(T_nTx,z)=B(TT_nx,z).
$$
令 $n\to\infty$，得到
$$
B(Tx,S_fz)=B(TS_fx,z).
\tag{5.2}
$$
此处没有要求 $Tx$ 先已在 $\mathscr D$ 或 $\operatorname{Dom}X_f$。

因为 $\mathscr D$ 是图核，(5.2) 延拓到所有 $z\in\operatorname{Dom}X_f$。由 (5.1)，它正是双线性伴随的定义域判据，因此
$$
Tx\in\operatorname{Dom}X_f,\qquad X_fTx=TS_fx
\qquad(x\in\mathscr D).
$$
再对一般 $x\in\operatorname{Dom}X_f$ 取 $\mathscr D$ 中的图逼近。$T$ 有界且 $X_f$ 闭，故
$$
\boxed{
T\operatorname{Dom}X_f\subseteq\operatorname{Dom}X_f,\qquad
X_fTx=TX_fx.
}
\tag{5.3}
$$
这尤其给 $A$ 的域不变与真交换；逆向包含只有在 $T$ 有可交换的有界逆时才随之成立。

### 5.4 闭值域等于循环空间

$1\in\mathscr D$，且 $T_n1=f_n\to f$，所以 $X_f1=f$。由 (5.3)，对任意多项式 $p$，
$$
X_fp(A)1=p(A)f.
$$
因此 $\operatorname{cyc}_A(f)\subseteq\overline{\operatorname{Ran}X_f}$。

反过来，若 $u$ 为有限柱，则其有界乘子 $X_u\in\mathcal A$ 满足
$X_u1=u$。有限乘子交换给
$$
T_nu=X_uT_n1=X_uf_n\longrightarrow X_uf.
$$
因此 $X_fu=X_uf\in\operatorname{cyc}_A(f)$。有限柱是图核，故所有 $X_fx$ 都在该闭循环空间中。结论是
$$
\boxed{
\overline{\operatorname{Ran}X_f}
=\operatorname{cyc}_A(f).
}
\tag{5.4}
$$

### 5.5 准确的未决对象

若 $f\ne0$，$M=\ker X_f$ 是闭的、$A$ 不变的子空间，并由 (5.1)、(5.4) 得
$$
\operatorname{cyc}_A(f)=H
\quad\Longleftrightarrow\quad
\ker X_f=\{0\}.
$$
R101 的有限次数双端矩分离还给 $M\cap\mathscr D=\{0\}$：若
$u\in M\cap\mathscr D$，则
$$
B(A^nf,u)=B(X_fA^n1,u)=B(A^n1,X_fu)=0
$$
对所有 $n$ 成立，故 $u=0$。这条相交为零结论不把未知的闭子空间 $M$ 排除；稠密域可以与非零闭子空间只有零交。

## 6. Gauge 差的真正域障碍

二阶符号在 dyadic 旋转下的差只涉及有限低位及其无限第一阶行，因此它通常是有限个有界解析因子与无界第一阶闭乘子的组合。它不是 R125 中的有界解析差。

虽然 $U_\zeta\mathscr D=\mathscr D$，且初始域上可写出
$$
U_\zeta S_fU_\zeta^*-S_f=\text{第一阶行的实际组合},
$$
仍不能据此推出
$$
U_\zeta\operatorname{Dom}X_f=\operatorname{Dom}X_f.
$$
R125 的这一步依赖差是有界算子；当前下阶项未被证明相对 $X_f$ 的图范数有界。控制它相对次数算子 $\Lambda$，不足以控制它相对一个可能退化的二阶乘子。

即便已在某个 $M=\ker X_f$ 上得到了差的作用，也不能取消其中的平滑因子 $A^r$，断言 $M\subseteq\operatorname{Dom}X_g$。闭包
$\overline{A^rX_g}$ 可能比 $X_g$ 具有更大定义域。

进一步，即使域问题解决，已知第一阶 $X_g$ 在整个 $H$ 单射且值域稠密，也不自动给它在任意未知闭 $A$ 不变子空间上的像包含或稠密像。Fourier 核论证需要的是指定 $M$ 上的稠密像，这一点必须另证。

因此下一层不能仅把“第一阶均循环”代入原来的有界旋转差证明。当前可确认的是二阶闭乘子与循环空间的对应；一般另一端仍可能位于其未知核中。


## 7. 完整循环性推论：局部有限二阶支撑与任意第一阶项

设二阶支撑逐位局部有限，即对每个固定 $i$，
$$
\#\{j\ne i:b_{\min(i,j),\max(i,j)}\ne0\}<\infty.
\tag{7.1}
$$
第一阶系数仍是任意复 $\ell^2$ 序列，不要求 $\ell^1$；二阶系数也只要求平方可和。则
$$
\boxed{f\ne0\quad\Longrightarrow\quad f\text{ 对 }A\text{ 循环}.}
\tag{7.2}
$$
若 $f$ 非常数，还对每个 $\lambda\in\mathbb C$ 有
$$
\ker(X_f-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H,
\qquad f-\lambda\text{ 对 }A\text{ 循环}.
\tag{7.3}
$$

**证明。** 设 $\zeta$ 的阶整除 $2^m$。对 $j\ge m$，
$\gamma_\zeta(N_j)=N_j$，故 $\gamma_\zeta(V_j)=V_j$。二阶单项只有在至少一个指标小于 $m$ 时才可能改变；由 (7.1)，这类非零单项只有有限个。第一阶被改变的单项同样只有有限个。因此有限系数逼近取足够大后，其 gauge 差稳定为一个固定的有限有理解析芽：
$$
\gamma_\zeta(T_n)-T_n=F_\zeta(A).
\tag{7.4}
$$
这里每个局部因子是
$$
v_j(z)=\frac{1-z^{2^j}/d_j}{1+z^{2^j}/d_j},
$$
所以 $F_\zeta$ 是有限个 $v_i(\zeta z)-v_i(z)$ 和
$v_i(\zeta z)v_j(\zeta z)-v_i(z)v_j(z)$ 的线性组合，确在零点邻域收敛。不是从形式幂级数直接推得解析性。

$U_\zeta$ 是有限柱函数的点乘，故 $U_\zeta\mathscr D=\mathscr D$。
在 (7.4) 中对该域上的向量取极限，得到
$$
U_\zeta S_fU_\zeta^*=S_f+F_\zeta(A)
\quad\text{于 }\mathscr D.
$$
左侧的闭包为 $U_\zeta X_fU_\zeta^*$；右侧因 $F_\zeta(A)$ 有界，且
$\mathscr D$ 是 $X_f$ 的图核，其闭包恰为 $X_f+F_\zeta(A)$。因此
$$
U_\zeta X_fU_\zeta^*=X_f+F_\zeta(A)
\tag{7.5}
$$
是包含定义域的等式。

§5 已给出 $C$ 自伴、有限柱图核和全部有界交换子的域交换，故 R125 §9 的闭加性 cocycle 定理全部假设成立。该定理对非标量 $X_f$ 排除所有参数的核并给稠密值域；再用 (5.4) 得循环性。$X_f$ 为标量当且仅当 $f=X_f1$ 为常数，此时非零结论由 $1$ 循环直接给出。证毕。

这个推论去掉了 R123 在本二阶类上的有界乘子假设。它没有去掉 (7.1)：若某个固定低位与无限多个高位相连，(7.4) 的差可成为真正无界的一阶行，前面的闭包步骤便不能照用。
