# R250：射线长度二的准确群结构与非平凡 Γ 作用

**状态：已证明的结构加强；射线长度、实际 Norm 原像和 $\mathcal L$ 仍未计算。**

沿用 R210 的同一 $p=43$、$q$、$F/K$、$L/F$、$\Gamma=\langle\gamma\rangle$、
$\Delta=\langle\sigma\rangle=C_{44}$、$\mathcal O=\mathbf Z_{43}[i]$ 和
$k=\mathcal O/43$。仍有 $\chi(\sigma)\bmod43=\omega=8+25i$。
设 $\mathfrak Q$ 为 $L$ 中全部 $q$ 素点的平方自由乘积。

R210 已证明普通 $\chi$ 类群为 $k$ 且 $\Gamma$ 作用平凡，射线类群
长度为一或二；长度二恰对应规范剩余量
$\rho=\mathcal L+3=0$。
本条进一步证明
$$
 \begin{array}{c|c|c}
 \rho & \operatorname{Cl}_{\mathfrak Q}(L)_\chi
       & \gamma\text{ 的作用}\\ \hline
 \rho\ne0 & k & 1\\
 \rho=0 & \mathcal O/43^2 & 1-86i.
 \end{array}
 \tag{250.1}
$$
特别地，长度二时不可能是 $k\oplus k$，$\Gamma$ 的作用也不可能平凡。
本条没有测得哪一行实际发生。第 6 节用同一已标记 $q$ 一致化元与
R171 的主化元，实际确定固定 $\gamma$ 下的系数为 $a=-2i$；
这仍不决定 $\rho$。

## 1. 使用可实现为类域 Galois 群的整角色

为了谈论真正的扩张而不把系数扩张后的单个投影误当成一个
$\mathbf F_{43}$ 商，令 $e_W\in\mathbf Z_{43}[\Delta]$ 是
$\chi,\chi^{-1}$ 对应的二维不可约整幂等元，置
$$
 A=e_W\bigl(\operatorname{Cl}_{\mathfrak Q}(L)\otimes\mathbf Z_{43}\bigr).
 \tag{250.2}
$$
它自然是 $\mathcal O$ 模，$\sigma$ 按 Teichmüller 单位 $\widehat\omega$
相乘。把系数扩到 $\mathcal O$ 再取 $\chi$ 后，就得到 R210 的
$\operatorname{Cl}_{\mathfrak Q}(L)_\chi$；两者的 $\mathcal O$ 长度相同。
特别地，$k$ 在这里作为实际有限阿贝尔群有 $43^2$ 个元素。

射线类域论给出一个实际扩张 $E/L$，其 Galois 群是 $A$。
该商在 $\Delta,\Gamma,\tau$ 下稳定，所以 $E/K$、$E/F$ 及 $E/\mathbf Q$
均为 Galois 扩张。令
$$
 G=\operatorname{Gal}(E/F).
$$
则有
$$
 1\longrightarrow A\longrightarrow G\longrightarrow\Gamma\longrightarrow1.
 \tag{250.3}
$$
这里 $A$ 用加法记号。$\Gamma$ 对 $A$ 的共轭作用就是对射线类群
的自然作用，且与 $\mathcal O$ 作用交换。

R210 的射线正合列给
$$
 E_{L,\chi}\longrightarrow k\longrightarrow A
 \longrightarrow k\longrightarrow0.
 \tag{250.4}
$$
当 $\rho=0$ 时，左边单位映射为零。记其后 $k$ 的像为 $B$，则
$$
 0\longrightarrow B\simeq k\longrightarrow A
 \longrightarrow k\longrightarrow0.
 \tag{250.5}
$$
$B$ 由各个 $q$ 素点的惯性生成；$\Gamma$ 在 $B$ 与 $A/B$ 上都平凡。
各个单独素点的 $43$ 惯性群为阶 $43$ 的循环群，而不是阶 $43^2$ 的 $k$。
$B\simeq k$ 是全部共轭惯性线合在一起的 $\Delta$ 不可约分量。

## 2. 一个强制分裂的初等群论引理

### 引理

在 (250.3) 中，$\Gamma$ 有一个阶为 $43$ 的提升，故
$$
 G\simeq A\rtimes\Gamma.
 \tag{250.6}
$$

**证明。** 在 $\operatorname{Gal}(E/K)$ 中任选 $\sigma$ 的提升 $s$。
由于 $\sigma$ 在 $L/K$ 中阶为 $44$，有 $s^{44}\in A$。
它被 $s$ 固定，而 $s$ 对 $A$ 的作用是乘 $\widehat\omega$。
$\widehat\omega-1$ 是 $\mathcal O$ 的单位，所以 $A^s=0$，从而
$s^{44}=1$。

任选 $g\in G$ 映到 $\gamma$。由于 $\Delta$ 与 $\Gamma$ 在 $L/K$
中交换，存在 $b\in A$ 使 $sgs^{-1}=bg$。
取唯一 $c\in A$ 满足
$$
 (\widehat\omega-1)c=-b.
$$
则 $g'=cg$ 被 $s$ 固定。又 $(g')^{43}\in A$ 也被 $s$ 固定，
所以 $(g')^{43}=1$。$g'$ 映到阶 $43$ 的 $\gamma$，故其阶恰为 $43$。
这直接证明分裂，不使用“同为 $43$ 群所以自动分裂”的错误推断。
相对于选定的 $s$，这个与 $s$ 交换的 $\gamma$ 提升还是唯一的。
证毕。

## 3. 温和惯性排除 $k\oplus k$

现在假设 $\rho=0$。$A$ 是 $\mathcal O$ 长度二的有限模，故只有
$\mathcal O/43^2$ 和 $k\oplus k$ 两种同构类型。

假如 $A\simeq k\oplus k$，记 $T$ 为 $\gamma$ 的作用。
由 $T^{43}=1$ 及特征 $43$，$T$ 是幺幂矩阵；其维数为二，故
$(T-1)^2=0$。写 $s_0=T-1$，于是
$$
 N_\Gamma=1+T+\cdots+T^{42}
 =43+\frac{43\cdot42}{2}s_0=0
 \quad\text{在 }A\text{ 上}.
 \tag{250.7}
$$
由 (250.6)，每个 $(a,\gamma)$ 的 $43$ 次幂为 $N_\Gamma a=0$；
对 $\gamma^j$ 同理，$j\ne0$ 时它还是 $\Gamma$ 的生成元。
所以整个 $G$ 的指数为 $43$。

另一方面，$B\ne0$ 保证至少一个 $q$ 素点在 $E/L$ 中有非平凡惯性。
$\Delta$ 传递地排列这些素点，所以每个都有惯性阶 $43$。
而 $L/F$ 在每个 $q$ 位置全分歧，分歧指数也为 $43$。
因此 $E/F$ 的该局部惯性阶恰为 $43^2$。

所有这些扩张的分歧指数都是 $43$ 的幂，且 $q\ne43$，所以它们是
温和分歧。有限 Galois 温和惯性群是循环群，故 $G$ 含有阶 $43^2$
的元素，矛盾。因此
$$
 \boxed{\rho=0\Longrightarrow A\simeq\mathcal O/43^2.}
 \tag{250.8}
$$
在此情形，(250.5) 的 $B$ 就是 $43A$。

## 4. Γ 必须作用为非平凡的一阶主单位

由于 $A\simeq\mathcal O/43^2$，每个 $\mathcal O$ 线性自同构都是乘
一个单位。它在 $A/43A\simeq k$ 上平凡，故
$$
 \gamma\bigm|_A=1+43a\qquad(a\in k).
 \tag{250.9}
$$
若 $a=0$，(250.6) 说明 $G$ 为阿贝尔群。取上节的局部惯性生成元 $t$，
其阶为 $43^2$；底域 $F_\lambda$ 的剩余域为 $\mathbf F_{q^2}$。
温和局部 Galois 群的算术 Frobenius 关系为
$$
 \varphi t\varphi^{-1}=t^{q^2}.
 \tag{250.10}
$$
若 $G$ 阿贝尔，必有 $t^{q^2-1}=1$。但 R191/R210 的同一素数满足
$v_{43}(q^2-1)=1$，不能杀掉阶 $43^2$ 的 $t$，矛盾。因此 $a\ne0$。

$\tau\sigma\tau^{-1}=\sigma^{-1}$ 说明 $\tau$ 对 $A$ 的 $\mathcal O$
结构是半线性的，其系数作用是 $i\mapsto-i$。
同时 $\tau$ 反转 $\Gamma$。即使选定的提升在 $G$ 中多出一个 $A$ 元素，
该元素对阿贝尔核 $A$ 的内共轭也平凡，故在 $A$ 上仍有
$$
 \tau(1+43a)\tau^{-1}=(1+43a)^{-1}.
$$
约化模 $43^2$ 给 $\bar a=-a$。在 $k=\mathbf F_{43}[i]$ 中这正是
$$
 \boxed{a\in i\mathbf F_{43}^{\times}.}
 \tag{250.11}
$$
这证明 (250.1) 的长度二一行。若 $\rho\ne0$，(250.4) 直接给
$A\simeq k$，它等于普通类群分量，所以 $\Gamma$ 平凡；另一行也已证明。

## 5. 等价判据和实际 Galois 群

结合 R210，在当前固定标记下，下列命题等价：
$$
 \rho=0;\quad \mathcal L=40;\quad
 \operatorname{length}_{\mathcal O}A=2;\quad
 \operatorname{exp}(A)=43^2;\quad
 \Gamma\text{ 在 }A\text{ 上非平凡}.
 \tag{250.12}
$$
它们一旦被实际认证，都给 $\Omega_2^\epsilon=13\epsilon\ne0$。
本条本身只证明等价性，没有认证其中一个为真。

长度二时，(250.6)、(250.9)、(250.11) 还给
$$
 |G|=43^5,\qquad [G,G]=Z(G)=43A\simeq k,\qquad
 G/[G,G]\simeq (\mathbf Z/43)^3.
 \tag{250.13}
$$
其中 $[G,G]=(\gamma-1)A=43aA=43A$；$a\ne0$ 保证中心不含任何
非平凡 $\Gamma$ 分量，故中心也为 $43A$。
此外 $N_\Gamma=43$ 在 $A$ 上成立，所以 $G$ 的所有 $43$ 次幂生成的
子群也是 $43A$，整个群的指数为 $43^2$，幂零类为二。

长度一时则 $G\simeq(\mathbf Z/43)^3$。
因此，当前未知量的零性也等价于这个实际射线扩张 $E/F$ 是否非阿贝尔。
第 6 节进一步给出固定 $\gamma$ 下的非零系数 $a$。
这个群作用的准确值仍不能替代同一规范下 $\mathcal L$ 的精确读数。

本条没有新增枚举或数值假设，没有依赖条件类数，亦未构造混合
Norm-one 单位。它只使用 R210 的准确长度与单位剩余判据，以及
有限群的上述显式计算和温和局部 Frobenius 关系。

为固定最后这个局部关系的方向，可取上域一致化元 $\pi$，对惯性元
$t$ 考察 $c(t)=\overline{t(\pi)/\pi}$。它与一致化元选择无关；
其核的高阶单位滤过商都是剩余特征 $q$ 的群，故在当前 $43$ 群中核为零。
于是惯性嵌入有限剩余域的乘法群，因而循环。对算术 Frobenius 提升
$\varphi$，用 $\varphi^{-1}\pi$ 替换一致化元，立即得到
$c(\varphi t\varphi^{-1})=c(t)^{q^2}$；由单射性就是 (250.10)。
这也直接说明为何本条不能把算术 Frobenius 的指数换成几何 Frobenius 的逆数。

## 6. 同一主化元与一致化元给出准确系数 $a=-2i$

### 6.1 两个输入确在同一个局部素点

R171 取 $\alpha=89460y+1\in H$，并已证明
$(\alpha)=\mathfrak q$ 是 $H$ 中指定的一次 $q$ 素理想。
延拓到 $F$ 后仍为唯一的 $\lambda_0$，赋值为一。
这个素点由同一实际 CM 点 $P$ 确定；全部 $\sigma^j\alpha$ 的标签
也是由 $\beta=-1+2i$ 在该点上的 CM 作用确定，不是任意排列。
记 $Q_0$ 为 $L$ 中其上的唯一素点。

另一方面，R191 的 $\mathcal B=K(\zeta_{43})$ 中指定 $q$ 素点是
唯一使 $g(r_Q)=0$ 的已给根。该证书逐坐标核对
$$
 \zeta_{43}=\frac{S_{44}(r_Q)-ir_Q}{2}=e_A(P,iP)=\zeta,
 \qquad S_0=2,\ S_1=X,\ S_n=XS_{n-1}-S_{n-2}.
 \tag{250.14}
$$
因此两边的局部嵌入在 Weil 根上相容，也与同一个 $i$ 相容；
它们来自包含 $F$ 与 $\mathcal B$ 的 $K(A[43])$ 的同一嵌入。
这里并未假定 $F\cap\mathcal B=K$：其二次交域已经由这个共同
Weil 配对标记匹配。

在这个 $\mathcal B$ 素点，R191 的 $h=g(r)(2-r)^{22}$ 赋值为一，
其余 $\sigma_{\mathcal B}^j h$ 均为单位。
R207 把原中心权换成正代表 $E_j\in\{1,\ldots,42\}$，其中 $E_0=1$，
并取
$$
 \alpha_+^{43}=\prod_{j=0}^{41}(\sigma_{\mathcal B}^j h)^{E_j},
 \qquad
 \theta=\sum_{j=0}^{41}\widetilde\sigma_{\mathcal B}^{\,j}\alpha_+.
 \tag{250.15}
$$
R207 的 42 个被加数在同一个局部点的赋值依次遍历
$1/43,\ldots,42/43$，唯一最小项是 $j=0$ 的 $\alpha_+$。
其 $\gamma$ 作用是原 R191 的
$\gamma\alpha_+=\zeta\alpha_+$，所以
$$
 v_{Q_0}(\theta)=1,\qquad
 \overline{\gamma\theta/\theta}=\zeta.
 \tag{250.16}
$$
这就是 R207 (207.7) 的实际一致化元朝向，不是单凭两个文稿都用了
$\gamma$ 这个字母而认定的相容性。
在 $L$ 的全部 $q$ 素点，$\theta$ 都有赋值一；
$\Delta$ 固定 $\theta$，而 $\tau\theta=\theta$。

### 6.2 一个明确的避开模的理想类

令
$$
 \beta=\theta+\alpha,\qquad
 D_0=Q_0-\operatorname{div}(\beta).
 \tag{250.17}
$$
这里除子写成加法，允许负的素理想系数。
在 $Q_0$，$\alpha$ 的赋值是 $43$，$\theta$ 的赋值是一，
所以 $\beta$ 的赋值是一；
在其他 $q$ 素点，$\alpha$ 为单位而 $\theta$ 赋值为一，
所以 $\beta$ 为单位。因此 $D_0$ 的支撑确实避开整个 $\mathfrak Q$，
定义合法的射线类。

由于 $\lambda_0\mathcal O_L=Q_0^{43}$ 且 $(\alpha)=\lambda_0$，得到
两个精确的除子恒等式
$$
 43D_0=\operatorname{div}\!\left(\frac{\alpha}{\beta^{43}}\right),
 \qquad
 (\gamma-1)D_0
   =\operatorname{div}\!\left(\frac{\beta}{\gamma\beta}\right).
 \tag{250.18}
$$
两个括号内的元素都在全部 $q$ 素点为单位。
它们在 $q$ 之外可以有支撑；(250.18) 只是射线正合列中的主理想关系，
没有把它们冒当成普通单位或所需 Norm 原像。

### 6.3 两个完整 Fourier 剩余值

记 $m=(q^2-1)/43$，并仍取
$\ell(u)=\log_\zeta(u^m)$。实际 $m=21\bmod43$。
以下在扩标后的 $\chi$ 分量使用
$$
 e_\chi=\frac1{44}\sum_{j=0}^{43}\widehat\omega^{-j}\sigma^j.
 \tag{250.19}
$$
在剩余群中 $44=1\bmod43$；权的方向固定为 $\omega^{-j}$。

设 $v=\alpha/\beta^{43}$。
当 $j\ne0$ 时，$\sigma^j\alpha$ 在 $Q_0$ 为单位，故
$$
 \overline{\sigma^j v}
 =\overline{\sigma^j\alpha}^{\,1-43},
 \qquad
 \ell(\sigma^jv)=\ell(\sigma^j\alpha).
 \tag{250.20}
$$
当 $j=0$ 时，$v$ 为 $Q_0$ 单位并被 $\tau$ 固定，所以其剩余值在
$\mathbf F_q^\times$，$43$ 次剩余符号为一，$\ell(v)=0$。
这一步没有计算或选择某个未知的 $q$ 进高阶单位根。

R171 给出的同一主化元的 $21$ 个前半符号为
~~~text
37,15,6,41,27,24,1,38,34,33,5,39,28,19,10,42,14,4,8,27,38.
~~~
中央符号为零，其余由 $\ell(\sigma^{-j}\alpha)=-\ell(\sigma^j\alpha)$ 得到。
所以
$$
 r:=\ell(e_\chi v)
 =\frac1{44}\sum_{j=1}^{43}\omega^{-j}\ell(\sigma^j\alpha)
 =-2i\lambda_q=-32i=11i.
 \tag{250.21}
$$
此处 $\ell(e_\chi v)$ 是单位完成模的线性剩余映射记号，
不把非整数幂的形式元素声称为一个普通代数数。

再设 $w=\beta/(\gamma\beta)$。由 (250.16)，当 $j=0$ 时
$\bar w=\zeta^{-1}$；当 $j\ne0$ 时，分子与分母的剩余值都为
$\overline{\sigma^j\alpha}$，所以 $\overline{\sigma^j w}=1$。
从而
$$
 s:=\ell(e_\chi w)=-m/44=-21=22.
 \tag{250.22}
$$
注意 $\ell(\zeta^{-1})=-m$，不是 $-1$。
这保留了幂剩余对数与直接根指数之间的区别。

### 6.4 射线群上的准确关系

在射线正合列中，记剩余线 $k$ 中坐标一的射线像为 $b_0$；
这个定义在单位像非零时允许 $b_0=0$。
令 $d=e_\chi[D_0]$。由 (250.18)–(250.22)，使用两边同一主理想映射，
$$
 43d=(11i)b_0,\qquad
 (\gamma-1)d=22b_0.
 \tag{250.23}
$$
若选相反的射线 Artin 同构，两式同改号，下面比值不变。
因为 $11i\ne0$，得到对两种长度都成立的关系
$$
 (\gamma-1)d=-2i\,(43d).
 \tag{250.24}
$$
$d$ 在普通类群上的像是 $e_\chi[Q_0]$，它生成 R210 的 $k$：
所有 $q$ 素点由 $\Delta$ 传递排列，且它们生成整个非零普通分量。
当 $\rho=0$ 时，(250.23) 还直接说明 $43d$ 生成 $B$，所以 $d$ 生成
整个长度二的 $A$；当 $\rho\ne0$ 时，它也生成长度一的 $A$。
因此关系 (250.24) 在全部 $A$ 上成立，准确为
$$
 \boxed{\gamma|_A=1-86i\pmod{43^2}.}
 \tag{250.25}
$$
长度一时右边约化为一；长度二时其阶恰为 $43$。
这独立再证长度二不能是 $k\oplus k$，并使 (250.11) 的系数唯一化为
$a=-2i$。它与 $\bar a=-a$ 也完全相容。

这条明确的射线关系不决定单位剩余映射是否为零：
$b_0=0$ 与 $b_0\ne0$ 分别对应 (250.1) 的两行，现有关系在两行都成立。
所以本条没有借由已知 $\lambda_q$ 循环论证 $\rho$ 的实际值。

## 7. 标记与数值的实际复算

`verify_r250_ray_module_constants.py` 只用 Python 标准库，读取原
R171、R191、R207 三个证书。它重新核对同一 $q$ 与同一 Weil 根，
从 $r_Q$ 的 Chebyshev 式重新生成该根，检查 $g$ 的唯一零分支，
检查正权给出的 42 个 trace 赋值和唯一最小项；
它还直接检查原完整 $P_\theta$ 在 $q$ Eisenstein。
这里复用 R207 的既有精确多项式证明，不重跑其 1325 个 CRT 素数。

随后程序从 R171 完整 $y$ 根、同一标签以及 $\alpha=89460y+1$
重新求出全部 $43$ 个非坏共轭的幂剩余符号，而不是只把
$\lambda_q=16$ 当输入代入。其实际结果为
$$
 \lambda_q=16,\quad m=21,\quad
 (r,s,a)=(11i,22,-2i).
 \tag{250.26}
$$
对应证书为 `r250_ray_module_constants_certificate.json`，
含三个输入的 SHA-256、完整重算符号和 42 个赋值分子。
复现命令（在 `notes/` 中）为
~~~bash
python verify_r250_ray_module_constants.py \
  r171_principal_norm_selflocal_certificate.json \
  r191_eta_ray_certificate.json \
  r207_gaussian_trace_degree43_certificate.json \
  --check r250_ray_module_constants_certificate.json
~~~
本次实际执行返回 `PASS`。这不重新证明原始 CM 标号或素性，
而是沿已证输入重连同一个局部素点并复算本条需要的所有新标量。
证书明确保留
`ray_length_computed:false`、
`actual_norm_preimage_computed:false`、
`actual_L_computed:false`。

## 依赖与出处

- R191：固定 $q$、$L_q/K$、完整实/正 Artin 标记和局部分歧。
- R171：实际主化元 $\alpha$、44 个 CM/Artin 标签、21 个有限符号及
  $\lambda_q=16$。
- R207 §2，(207.6)–(207.8)：同一选定 $q$ 素点的实际
  $\theta$、唯一最小项和 $\gamma\theta/\theta\equiv\zeta$。
- R200、R201：规范 $\mathcal L$ 及 $\Omega_2^\epsilon=\epsilon(10-\mathcal L)$。
- R210：普通类群 $k$、射线正合列、$\rho=\mathcal L+3$ 及长度判据。
- J.-P. Serre, *Local Fields*, Springer, 1979, Chapter IV, §2：温和惯性
  的循环性与剩余 Frobenius 对惯性的作用。此处使用算术 Frobenius
  $x\mapsto x^{q^2}$，故指数为 $q^2$。
- B. Conrad, *Math 676*, Homework 12, Exercise 4(ii)–(iii)，原课程讲义：
  <https://math.stanford.edu/~conrad/676Page/homework/hmwk12.pdf>。
  其中把温和惯性识别为剩余域根单位的逆极限，并要求在该识别下核对
  剩余 Galois 的共轭作用；与上面的直接证明相同。
