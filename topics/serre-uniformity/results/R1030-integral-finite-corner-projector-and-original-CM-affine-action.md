# R1030：原最低型的整有限角投影及其 CM 仿射作用

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
global_route / root，有限群与分支接口另经 o2_high_coefficient 审核。

**已证明：R1029 的原最低惯性型投影可由一个明确的整有限群双陪集幂等元实现。**
在同一个 full-$p$ 模型、保留全部 Weil 配对分支后，该算子固定
$d(x^{2g-1}y)$，并杀掉 $A_{\rm tail}x^{2g-1}dx/y$。
后者的 $A_{\rm tail}$ 随分支变化；它没有被当成一个可从投影中提出的常数。

本文计算的是这两个实际仿射微分的投影。
原底 Hodge 向量传播到 CM 尾时，在第一个微分前的完整线性泛函
仍须从真实节点过渡求出；本文不把它规范成一，也未据此宣称原 CM jet 已是单位。

## 1. 原对象和有限角代数

全篇保持 R1018、R1021、R1028、R1029：
$$
p=12g-1>37,\quad m=(p-1)/2,\quad e_0=m(p+1),\quad
\pi_0^{e_0}=p,\quad \varepsilon=\pi_0^m .
\tag{1030.1}
$$
原曲线仍为 $X_1$，原六层仍为 $H_6$，原下降仍为
$\kappa_4$；没有换成一个只有相同 $p$-处类型的独立 CM 商。

在 full-$p$ 图上同时保留全部配对分支。
因原中央角色平凡，可在
$$
G=\operatorname{PGL}_2(\mathbf F_p),\qquad
N=N_{\rm ns}/\mathbf F_p^\times,\qquad |N|=2(p+1)
$$
中工作。置
$$
e_N=\frac1{|N|}\sum_{n\in N}n\in\mathbf Z_p[G].
\tag{1030.2}
$$
令 $V=V_{\theta_1}$ 是 R1029 的最低尖点型：
$$
\theta_1=\widetilde\omega_2^{p-1},\qquad \dim V=p-1 .
$$
使用 $\theta_1^{-1}$ 给同一个有限表示。
其 $N$-固定线为一维；奇偶号已在 R1029 完整计算。

## 2. 从 R434 的本原格得到真正整的幂等元

R434 §§1–3 对这个有限表示给出了一个 $G$-稳定未分歧整格
$\Lambda$，以及 $G$-不变满射
$$
\lambda:\Lambda/p\Lambda\longrightarrow k .
$$
并且可在 $\Lambda^N$ 中取本原生成元 $v$，使
$\lambda(\bar v)=1$。
此处只消费 R434 独立有效的有限群部分；
不恢复该文开头及 R575 已撤回的全局 CM 商识别。

记 $\rho$ 为 $V$ 的表示，定义 spherical coefficient
$$
\phi(g)=\operatorname{Tr}\!\bigl(\rho(e_N)\rho(g)\bigr).
\tag{1030.3}
$$
因为 $e_N$ 是投到 $\mathcal O v$ 的秩一整幂等元，
$$
e_N\rho(g)v=\phi(g)v .
$$
故 $\phi(g)$ 是整数。
施加 $\lambda$ 后，
$$
\overline{\phi(g)}
=\lambda(e_N\rho(g)\bar v)
=\lambda(\bar v)=1.
\tag{1030.4}
$$
$\phi(g)$ 实际属于 $\mathbf Z_p$：它是
$|N|^{-1}\sum_n\chi_V(ng)$，而 $\chi_V$ 的全部值在
$\mathbf Q_p$ 中。
对 nonsplit 元，这些值是
$-z^a-z^{-a}$，其中 $z^{p+1}=1$；未分歧 Frobenius
将 $z$ 送到 $z^{-1}$，所以这个和固定。
其余类别的 character 值本来就是整数。

在 $\mathbf Q_p[G]$ 中令 $e_{\rm triv},e_{\theta_1}$
为相应中央幂等元。定义
$$
E=(e_{\rm triv}+e_{\theta_1})e_N .
$$
用完整 character 幂等公式，得到准确的系数表达式
$$
\boxed{\quad
E=\frac1{|G|}
  \sum_{g\in G}\bigl(1+(p-1)\phi(g^{-1})\bigr)g .
\quad}
\tag{1030.5}
$$
确切地，$e_{\theta_1}e_N$ 的 $g$-系数为
$(p-1)|G|^{-1}\operatorname{Tr}(\rho(g^{-1})\rho(e_N))$；
没有丢掉 $e_N$ 的归一化分母。

现在
$$
|G|=p(p^2-1),\qquad
1+(p-1)\phi(g^{-1})\equiv0\pmod p
$$
由 (1030.4) 对每个 $g$ 成立。因此
$$
\boxed{\quad
E\in e_N\mathbf Z_p[G]e_N,\qquad E^2=E .
\quad}
\tag{1030.6}
$$
这证明一个真正整的角代数投影，不是声称
$e_{\theta_1}$ 单独为整的中央幂等元。
在特征零中，$E$ 在 trivial 与 $V_{\theta_1}$ 的
$N$-固定线上为一，在其余有限型上为零；它的 augmentation 为一。

## 3. 与原 $e_1$ 的实际识别

从 full-$p$ 图到原正规化子商的 pull–push 只需除以
$|N|$，是 $p$ 单位。全 $p$ 换基与原 full-six 换基
逐点交换，所以 (1030.6) 与 $H_6$ 平均及原 deck $\delta$
交换，并沿原 $\kappa_4$ 下降。

完整 canonical spectrum 已由 R1029 §§2–3 核过。
有限 trivial 部分若出现在原 holomorphic differentials 中，
就来自
$$
S_2(H_6)=H^0(\mathbf P^1,\Omega^1)=0 .
$$
Steinberg 及二次退化也已按原正规化子条件排除。
因此 $E$ 在原 generic Hodge 空间上的作用，准确等于只取
$\tau_1$ 的 R1029 幂等元 $e_1$。

两边都是实际整端环的 $p$-进元素；特征零微分表示忠实，
且原整格无挠，故其作用在整 Hodge 格及实际 $p$-可除群上相同：
$$
\boxed{\quad E|_{\mathcal J[p^\infty]}=e_1 .\quad}
\tag{1030.7}
$$
这里可以先在 $\operatorname{End}(J)\otimes\mathbf Q_p$ 中比较，
再在各 $p^n$-torsion 及其相容极限中读这个等式。
它没有将一个特殊纤维的局部表示直接冒成泛纤维商。

## 4. 全配对分支上的原多项式

在一个原 CM supersingular 来源的 full-$p$ 仿射图中，
取 Cartan eigenvariables $A,B$，使
$$
c=A^{p+1}-B^{p+1},\qquad
U=(A^{p+1}+B^{p+1})/2,\qquad V=AB .
$$
它们正是 R1018 原坐标的共轭本征线版本；
可取 $A=\beta+s\alpha,B=\beta-s\alpha$，$s^2=-3$。
在 $(\alpha,\beta)\in\mathbf F_p^2$ 上，$A^p=B$。

置
$$
A_{\rm tail}=c^2/4,\qquad
U^2=V^{p+1}+A_{\rm tail},\qquad
x=V^6,\quad y=UV^3 .
\tag{1030.8}
$$
于是
$$
y^2=x(x^{2g}+A_{\rm tail})
$$
是同一个 $e_s=3$ 商尾。
不能把各个 $c$ 分支在进行有限群运算前合并成一个固定的 $A_{\rm tail}$。

考虑齐次多项式
$$
F=UV^{p-2}
 =\frac{A^{2p-1}B^{p-2}+A^{p-2}B^{2p-1}}2
 =x^{2g-1}y .
\tag{1030.9}
$$
其次数是 $3p-3$，故标量 $\mathbf F_p^\times$ 作用平凡。
因此 $W=\operatorname{Sym}^{3p-3}(k^2)$ 是 $G$-模。

设 Cartan 元对应 $\lambda\in\mathbf F_{p^2}^\times$，作用为
$A\mapsto\lambda A,B\mapsto\lambda^pB$。
单项式 $A^iB^{3p-3-i}$ 固定，当且仅当
$$
i+p(3p-3-i)\equiv0\pmod{p^2-1},
$$
即 $i\equiv-3\bmod p+1$。
在所需范围内恰有
$$
i=p-2,\qquad i=2p-1 .
$$
normalizer 的 Frobenius 元交换这两个单项式，因而
$$
W^N=kF .
\tag{1030.10}
$$

定义纯代数的 evaluation functional
$$
\Lambda_{\rm ev}(f)
 =\sum_{(\alpha,\beta)\in\mathbf F_p^2} f(\alpha,\beta).
\tag{1030.11}
$$
这是 $G$-不变的线性泛函：换基置换全部 $\mathbf F_p^2$；
标量不影响本次次数的值。
对非零 $(\alpha,\beta)$，有 $A^p=B$、$AB\ne0$，从而
$$
F=(AB)^{p-1}=1 .
$$
零向量的值为零，所以
$$
\Lambda_{\rm ev}(F)=p^2-1=-1\ne0\quad\text{于 }k.
\tag{1030.12}
$$
这只是完整有限域恒等式的纸面证明，不是执行一个求和程序。

由 $E$ 的 augmentation 为一，
$\Lambda_{\rm ev}(EF)=\Lambda_{\rm ev}(F)$。
又 $EF\in W^N$，(1030.10)–(1030.12) 给
$$
\boxed{\quad EF=F,\qquad E(dF)=dF .\quad}
\tag{1030.13}
$$
第二式使用有限群换基与相对微分交换。

也记录完整的原第二类微分恒等式。置
$$
\mu=x^{4g-1}\frac{dx}{y},\qquad
\nu=x^{2g-1}\frac{dx}{y}.
$$
直接微分 (1030.9) 给
$$
dF=\frac{6g-1}{2}\mu+\frac{4g-1}{2}A_{\rm tail}\nu
   =-\frac14\mu-\frac13A_{\rm tail}\nu\quad\text{于 }k.
\tag{1030.13a}
$$
结合下文 (1030.17)，准确得到
$$
E\mu=\mu+\frac43 A_{\rm tail}\nu=-4dF.
\tag{1030.13b}
$$
$\mu$ 的 norm 角色为 $d^{2p-2}=1$；本式仍在全部分支并上使用。
它只计算这个明确源，不提前识别原全局 Hodge 向量的系数。

## 5. 模 $p$ 常线性作用与 normal 层

R1021 已在整个非约化 $\mathcal O/(p)$ 上给出实际 full-$p$
仿射图及其 level 作用：各个 $c$ 分支的并由原
$C=\alpha^p\beta-\alpha\beta^p$ 的常值方程给出，
所有换基都是常系数线性变换。
本篇只使用这个已证明的仿射范围，不把它扩张成未知节点的高精度模型。

有限群换基固定底环及 $\pi_0$，在全部 $c$ 分支间作用，
并固定下面的原六标记 supersingular 来源。
因此它不把当前 CM 尾送到另一 supersingular 来源，
且保持每个 $\pi_0$-adic normal 层。
整 $E$ 的作用可以逐层约化；没有含 $p$ 分母的系数，
也没有更早层经变换回灌到当前层的问题。
在归一化、商及正则化模型上，所用作用是原几何 deck 作用的延伸；
各仿射图上可直接由 R1021 读它。

## 6. 真正被杀掉的是 $A_{\rm tail}\nu$

记
$$
\nu=x^{2g-1}\frac{dx}{y}.
$$
R1028 的实际中心 Hodge 提升 $\Omega_I$ 具有完整惯性权
$e_0-p-1$，并令
$$
\Delta\Omega=\pi_0^{3m+2}\Omega_I .
$$
在每个原 CM 尾上，其所有早于 $4m$ 的 normal 层为零，
而第 $4m$ 层为
$$
\kappa_c\,\nu,\qquad \kappa_c\ne0 ,
\tag{1030.14}
$$
其中原节点厚度三、节点单位与中心首系数均已由 R1028 (1028.20)
保留。这里只把那些已经确定的单位合记为 $\kappa_c$，不另改尺度。

需要在全部配对分支同时运输 (1030.14)。
对 norm 为 $d\in\mathbf F_p^\times$ 的 Cartan 元，
$$
c\mapsto dc,\quad U\mapsto dU,\quad V\mapsto dV,\quad
x\mapsto d^6x,\quad y\mapsto d^4y.
$$
所以
$$
A_{\rm tail}\mapsto d^2A_{\rm tail},\qquad
\nu\mapsto d^{p-3}\nu=d^{-2}\nu .
\tag{1030.15}
$$
原 $\Delta\Omega$ 是正规化子商上的微分；
其 full-$p$ 拉回 $N$-不变。
又 $c$ 分支是 norm 群的单一非零轨道，因此 (1030.14)
在分支并上准确为
$$
\kappa\,A_{\rm tail}\nu,\qquad \kappa\in k^\times
\tag{1030.16}
$$
（对不同六标记 CM 来源可有各自的 $\kappa$）。
Frobenius normalizer 元将 $c$ 送到 $-c$，不改变 $A_{\rm tail}$，
同样相容。

另一方面，R1029 (1029.20) 和 (1030.7) 给
$$
E\Delta\Omega=e_1\Delta\Omega\in p\,e_1\omega_{\mathcal J}.
$$
由于 $4m<e_0$，其第 $4m$ normal 层为零。
以 §5 的逐层相容性应用于 (1030.16)，得到
$$
\boxed{\quad E(A_{\rm tail}\nu)=0 .\quad}
\tag{1030.17}
$$
本式是在全部配对分支并上的微分恒等式。
它没有把 $A_{\rm tail}$ 提到 $E$ 外，也未声称固定单一分支后
仍能不经运输地计算 $E\nu$。

## 7. 对原 CM jet 还需要什么

若从某个指定原底 Hodge 向量的真实过渡已经求得其首 normal
微分为
$$
a\,d(x^{2g-1}y)+b\,A_{\rm tail}x^{2g-1}\frac{dx}{y},
$$
并且这里的 $a,b$ 是在同一来源的全部配对分支上准确运输的
常数，那么 (1030.13)、(1030.17) 给它的实际类型投影为
$$
a\,d(x^{2g-1}y).
\tag{1030.18}
$$
在原 $Q=(0,0)$ 取 $t=\sqrt x$，有
$$
x^{2g-1}y
 =\sqrt{A_{\rm tail}}\,t^{4g-1}
      \sqrt{1+t^{4g}/A_{\rm tail}},
$$
故 (1030.18) 的首项是
$$
a(4g-1)\sqrt{A_{\rm tail}}\,
     t^{4g-2}\,dt.
\tag{1030.19}
$$
$4g-1=(p-2)/3$ 是 $p$ 单位，节点及分支尺度亦为单位。
但是 $a$ 必须由原底向量计算：不能把一个形式形状相同的参考微分
除以 $a$，再据规范后的单位反推原 jet 单位。

接下来须求这个实际线性泛函 $a$，并与 R1023/R1026/R1029
的完整首 log 向量比较；还须控制原有理简单商的相对整格和尾项。
本文不宣称这些比较已完成，更不取消 O0 的全局覆盖条件。

## 来源与审核

- [R434](R434-primitive-cartan-trace-and-scalar-invariant-cm-logarithm.md)，
  §§1–3：真正有限群整格、全纤维求和的独立证明、
  $G$-不变 $\lambda$ 和本原正规化子线；只用其未被 R575 撤回的范围。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)，
  §§2、5、7：原 Cartan 坐标、完整惯性及同一 $e_s=3$ 尾。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)，
  §§2–3：真实 full-$p$ 仿射图在完整 $\mathcal O/(p)$ 上的常线性 level 作用。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)，
  §§4–6：同一个中心提升、原厚度三节点及准确第 $4m$ 层修正。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)，
  §§2、4–5、7：全部原类型、实际整投影与 (1029.20)。

global_route 与 root 对整系数公式、所有分支、
多项式固定空间、evaluation functional、逐 normal 层作用和
$A_{\rm tail}$ 的 determinant 运输作纸面审核。
没有执行数学程序或重扫已有窗口。
Serre 主目标仍 OPEN。


## R1032 接续：原前因子已确定

[R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)
已保中心自身变形及全部 normal 层，求得原底向量 $L$ 的
实际前因子为 $a(L)=\kappa_1(2/m)\sum_sL_s\theta_s/(1-s)^2$。
因此本篇 §7 的来源比较现已完成；原 $p$-单位 $\kappa_1$
和整 Serre 配对保留。仍须另证真实 MW 饱和空间的横截性、
更高 normal 层的低 Taylor 项与统一原盘半径。
