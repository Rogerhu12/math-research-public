# R1026 — 扩展原长窗口、真实十三处二次 Frobenius 饱和与完整 flat contiguous 家族

日期：2026-11-27 UTC。**已证明。** 本篇将 R1022 的同一
特征零39支返回扩至 $H\le p-6$，并重新支付完整 Newton 尾、
全部 double 边界、实际字和 sigma 折回。§2 先证明显示的 $p^{K(H)}$ 精度；新增 §9 再用原第二半径
将同一来源的完整比较提高到 $p^{H+1}$，保留质量和两个 Gaussian。

在一整段连续参数中，原十三处权模 $p$ 准确饱和为
$v_\pi^{p^2}$，所以经过第二 Cartier 后是同一个固定
$v_\pi$ 乘子。三处权仍是原 $W_q$；其相邻差及两级
特征零原权的完整相邻差一并给出。
这些是真实 flat 返回的家族，不是额外假设的独立 canonical 零。

## 1. 全部参数与原特征零输入

仍取原
$$
E:y^2=x^3+1,\quad X=x^3,\quad
p=6s-1>13^4,\quad \alpha=\delta\pi.
$$
令
$$
3\le q\le s-2,\qquad H=6q+5\le p-6,\qquad
N=H(p+1),\quad k=N/6=Hs.
\tag{1}
$$
保持 R1022 的原
$R_\pi,\mathsf A_\pi,R_\alpha=x\mathsf A_\pi R_\pi$，
以及两个完整特征零权
$$
V_\pi=v_\pi^{N+1}B_{N+1,k}(v_\pi),\quad
v_\pi=\frac{R_\pi}{(X+1)^2},\qquad
V_\delta=v_\delta^{2k+1}B_{2k+1,k}(v_\delta),\quad
v_\delta=\frac X{X+1}.
\tag{2}
$$
允许两种原顺序
$$
V_\alpha=V_\pi(P)V_\delta(\pi P),\qquad
V_\alpha^{\rm alt}=V_\delta(P)V_\pi(\delta P).
$$
每一种都按其整个原式分别消费；没有在特征零交换两个权。

R1022 的未平均 trace、绝对 $\alpha^{-10}$、全部39支
Miller 相位及原点前缀证明逐式成立：
$$
A_{10,\alpha}(f)=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
 \left(V_\alpha\frac{R_f}{R_\alpha^{10}}\right),\qquad
h_{10,\alpha}(f)(\alpha z)-f(z)=O(z^{N+1}).
\tag{3}
$$
两个顺序都具有同一整基帽
$$
M_\alpha=\frac{17N}{6}+3,\qquad
A_{10,\alpha}=\frac{x^2P(X)}{(X+1)^{M_\alpha}},
\quad\deg P\le M_\alpha+1
\tag{4}
$$
在 principal 输入上成立；整个 $S_{390}$ 的两族整基
仍为 R1022(55)。
增大 $H$ 不改变有限 étale trace 的整性、
所有核点的实际零阶或与 $M_\alpha$ 无关的 Hurwitz 范数。

## 2. 重新支付全部尾：准确精度 K(H)

原整窗口是 $w<s(p-1)$。
因 $H\le p-6$，在 $H<\ell\le p-2$ 的每一个导数项中，
$\ell s<s(p-1)$，原整基及全部 Gaussian 卷积都整；
所用 $j!\,(j\le\ell<p)$ 都是单位。
故这些项的赋值至少为 $\ell$。

对全部 $\ell\ge p-1$，使用 R1016 的原完整 Hurwitz 界：
$$
v_p(\text{第 }\ell\text{ 项})
\ge\ell-v_p((\ell s)!)+v_p((\ell-1)!)
\ge\frac{\ell(5p-7)}{6(p-1)}
\ge5s-2.
\tag{5}
$$
于是准确的共同深度是
$$
\boxed{K(H)=\min(H+1,5s-2).}
\tag{6}
$$
保持原 $q_\alpha=\alpha^{p+1}/39=q_\delta q_\pi$，
两种完整 trace 都满足
$$
\boxed{
j_f-j_{10,h_{10,\alpha}(f)}
-m_0(f)\log_pq_\alpha\in p^{K(H)}\mathcal O.
}
\tag{7}
$$
质量及全部固定 frame 单位仍与 R1022 相同。
这不是把所有低 Newton 项仅约化模 $p$；
它们的特征零前缀由 (3) 同时支付。

对 $H$ 较大时，(7) 的初始精度可能严格小于 $H+1$。
以下 §§3–8 的原论证均使用 (6)，不以旧符号隐去这个损失；
新增 §9 另用原第二半径支付同一来源的 $H+1$ 位加强。

## 3. 原有限模型的完整 double 边界与唯一 primitive

对全部 $0\le b<p$，仍取原
$$
\eta_b=Z^{-b-1}P_{10}A_{10,\alpha}(f)\omega_E.
$$
其原点极至多 $b+1\le p$；
原 $Z^p$ 因子仍消去其它 $Z=0$ 点补极。
在三个非零二挠点的完整帽为
$$
d_b=p^3-p^2+(8-b)p+\frac{17H(p+1)}3+7
<2p^3.
\tag{8}
$$
因为 $H\le p-6$，最坏值不超过
$p^3+(14p^2-61p)/3-27<2p^3$。

第一次和第二次 Cartier 的形式帽可取
$$
d_1=p^2-p+9-b+
 \left\lfloor\frac{17H(p+1)/3+6}{p}\right\rfloor
\le p^2+\frac{14p-61}{3},
\qquad
d_2=\left\lceil\frac{d_1}{p}\right\rceil\le p+5.
\tag{9}
$$
原点留数仍准确是 $\alpha^{-b}c_b(f)$。
先按 R1020/R1024 去掉该留数后，第三次 Cartier 的整个余项
属于 $\Omega_E(2\mathcal D_2)$，在原点正则。

### 3.1 全六维边界的明确基

这个六维空间的完整基可取
$$
\boxed{
\omega_E,\quad \frac{\omega_E}{y},\quad
\frac{x\omega_E}{y},\quad
d(1/y),\quad d(x/y),\quad
\varphi=-\frac{3x}{c_p(X+1)}\omega_E.
}
\tag{10}
$$
在 $Q_e=(e,0)$，$e^3=-1$，三个 double 主部依次由
$d(1/y),d(x/y),\varphi$ 给出与
$1,e,e^2$ 成比例的三个独立向量。
两个 simple 留数向量由 $\omega_E/y,x\omega_E/y$ 给出，
全纯项是 $\omega_E$。这支付全部六维，而非只保某一角型。

其完整 Cartier 作用是
$$
\begin{aligned}
C\omega_E&=0,& C\,d(1/y)&=0,&C\,d(x/y)&=0,\\
C(\omega_E/y)&=-x\omega_E/y,&
C(x\omega_E/y)&=-\omega_E/y,&
C\varphi&=\omega_E.
\end{aligned}
\tag{11}
$$
所有标量按真实 $p$ 次根处理。
前两条 simple 符号可直接从
$e^p=-e^2$ 的留数检查；
CM 型排除额外全纯项。
最后一条仍是 R529/R1020 的原 section，不是另选的横向值。

### 3.2 两 exact 与平坦 section 的完整帽

R1020 的 $S_0$ 第一 primitive 可用
$$
\operatorname{pole}_{\mathcal D_2}U_0
\le p^2+5p+1.
$$
对同一个 $\varphi_H$，仍只积分指数 $<H$；
由于 $H\le p-6$，全部分母是 $p$ 单位，
且 $\operatorname{ord}_O\varphi_H\ge H+5$。
其第二 section 和唯一第一 primitive 的完整帽可取
$$
\boxed{
L_H\le p(p+H+4),\qquad
\operatorname{pole}_{\mathcal D_2}U_H\le p(p+H+4)-1.
}
\tag{12}
$$
所有原 $aZ$ 和 $-\rho_b r_0\omega_E$ 的原点留数修正保留。
低窗 $0<r\le H<p$ 中的 primitive 系数仍在模 $F^p$ 类上有定义。

因此 R1020 的全部 $n=rp+b$ 读者、原 sigma/$P_{10}$/$Z$
下三角折回及 R1022 的全部外部 torsion pullback 继续成立。
(10) 的非exact double 方向不被宣称为零，
也没有从 (12) 把原第二 section 在整个曲线上删除。

## 4. 原十三处权的真实二次 Frobenius 饱和

写
$$
k=qp+t,\qquad t=q+5s\le p-1.
$$
置
$$
q_c=\left\lceil\frac{s-7}{7}\right\rceil.
$$
当 $q\ge q_c$ 时，原 $N+1=Hp+H+1$ 与 $k$ 的最低位
发生实际 carry。完整多项式因而是一个 $p$ 次幂。
其根在 $v=0$ 零至少 $H+1$，在 $v=1$ 与1的差零至少
$q+1$，次数至多 $H+q+1$。
两点 Hermite 唯一性准确给
$$
\boxed{
\bar V_\pi=W_{\pi,q}^{\,p},\qquad
W_{\pi,q}=v_\pi^{H+1}B_{H+1,q}(v_\pi).
}
\tag{13}
$$
这个证明不要求 $\binom{H+q}{q}$ 是单位。
原 R1016 在小范围中的单位断言不能无证延长至本篇全部参数。

若进一步
$$
q\ge q_{\rm sat}:=\left\lceil\frac{p-6}{7}\right\rceil,
$$
则 $H+q+1=7q+6\ge p$。
此时 $H+1<p$、$q<p$、$p\le H+q+1<2p$，
所以 $W_{\pi,q}$ 的完整导数系数
$(H+1)\binom{H+q+1}{q}$ 被 $p$ 整除。
又其次数小于 $2p$，$W_{\pi,q}(0)=0$、$W_{\pi,q}(1)=1$。
由此严格得到
$$
\boxed{
W_{\pi,q}=v_\pi^p,\qquad
\bar V_\pi=v_\pi^{p^2}.
}
\tag{14}
$$
没有丢掉一个余带或引入自由系数。

对任何完整 source 微分 $\eta$，因此有
$$
\boxed{
C^2(v_\pi^{p^2}\eta)=v_\pi C^2\eta.
}
\tag{15}
$$
第二 Cartier 与未平均十三支 trace 交织。
故整段 $q_{\rm sat}\le q\le s-2$ 的十三部分在该层
是同一个固定乘子 $v_\pi$。
它的位置仍是原 source 点，不能跨 torsion 平移或几何投影。
这个共同性不删除第一 primitive 或 (10) 的完整边界。

## 5. 三处根、一个真正的整除 p 步和单位 holomorphic 核

整个参数范围 (1) 内，原三处仍满足
$$
\boxed{
\bar V_\delta=W_q^p,\qquad
W_q=v_\delta^{2q+2}B_{2q+2,q}(v_\delta).
}
\tag{16}
$$
证明同 R1022，但这里另外核全部上界：
$2k+1=(2q+1)p+a_0$，$a_0=2q+4s+2<p$；
$a_0+t$ 在 $[p,2p)$ 中，而高位 $3q+2<p$。
只有这一次低位 carry。
根的次数 $3q+2<p$，其零阶和原点规范仍唯一确定 (16)。

令
$$
c_q=12(q+1)\binom{3q+2}{q}\in\mathbf F_p^\times,\qquad
d_q=\frac{6(2k+1)}p\binom{3k+1}{k}\in\mathbf Z_p^\times.
$$
第二个数先在特征零真除 $p$；
其单位性正由刚核定的唯一 carry 和 $2k+1\not\equiv0$ 给出。
整个特征零导数是
$$
\boxed{
dV_\delta
=6(2k+1)\binom{3k+1}{k}
 \frac{(x/y)^{N+2}}{y}\,\omega_E.
}
\tag{17}
$$
所以在同一个整模型中
$$
\overline{\frac{dV_\delta}{p}}
=\bar d_q\,((x/y)^H)^p
 \frac{(x/y)^{H+2}}y\,\omega_E.
\tag{18}
$$
这是实际的第一整除 $p$ 步，不是从模 $p$ 恒等式猜一个提升。

一般地，若整函数 $V$ 满足 $\bar V=W^p$，
选任一整提升 $\widetilde W$，
则
$dV/p=\widetilde W^{p-1}d\widetilde W+
d((V-\widetilde W^p)/p)$。
由 Cartier 对 exact 的作用，准确得到
$$
C(\overline{dV/p})=dW.
\tag{19}
$$
结合 (18) 和原 $dW_q=c_q(x/y)^H\omega_E$，本篇得到
一个真实单位 holomorphic 返回。

它也有完全显示的闭式：
$$
\boxed{
C\left(\frac{(x/y)^{H+2}}y\,\omega_E\right)
=
\binom{3(s-q)-5}{\,2(s-q)-3\,}\omega_E
=\frac{c_q}{\bar d_q}\omega_E\ne0.
}
\tag{20}
$$
直接证明前一等号：
$(x/y)^{H+2}/y=x^{6q+7}/(X+1)^{3q+4}$。
hyperelliptic Cartier 公式把整个输入化为
$$
\frac1{2y}\,
C_x\left(
x^{6q+7}(x^3+1)^{3(s-q)-5}\,dx\right).
$$
其次数小于 $2p-1$，唯一可读槽是 $x^{p-1}$，
对应 $2(s-q)-3$。
因 $2\le s-q$，该二项式上下标均在 $[0,p)$，
且下标不超过上标，故是单位。
(19) 同时支付后一比值的绝对规范。

本节没有将 (19) 继续当作任意模 $p^K$ 提升；
高精度比较仍只使用 (7) 的原特征零输入。

## 6. 完整相邻 flat 权及高精度差

### 6.1 实际三处根的二次 contiguous 式

令 $u=x/y$、$v=v_\delta$、
$B_q=\binom{3q+2}{q}$。
全部有限项准确给
$$
\boxed{
W_{q+1}-W_q
=-\frac{B_q}{2q+3}\,
u^{6q+6}
\{(2q+3)+3(q+1)v-3(3q+4)v^2\}.
}
\tag{21}
$$
可对两边完整微分，并用 $W_q(0)=0,W_q(1)=1$
固定常数。等价的多项式形式是
$v^{2q+2}(1-v)^{q+1}$ 乘一个显示二次式，
所以没有选择一个可自由调整的差权。

特别乘原 $U_B=xy$ 后，差严格为
$$
\boxed{
(W_{q+1}-W_q)U_B
=B_q u^H x^2\,
\frac{2X^2-\dfrac{7q+9}{2q+3}X-1}{(X+1)^2}.
}
\tag{22}
$$
这是与原两条 $x^2$ 旧方向比较时的真实乘子；
整个 $P_{10}$、Miller 和十三字符仍保留。

### 6.2 特征零差也全部显示，不能删十三处的 p 倍项

为在 (7) 的精度使用相邻 $q$，还须保原 $V$ 的特征零差。
对 $c=2$ 或 $6$ 定义
$$
F_{c,k}(v)=v^{ck+1}B_{ck+1,k}(v).
$$
令 $a=ck+1,b=k+1$，
$C_{c,k}=a\binom{a+k}{k}$。
存在一个完全指定的整多项式 $P_{c,k}$，次数至多 $c$，使
$$
\boxed{
F_{c,k+1}-F_{c,k}
=v^a(1-v)^bP_{c,k}(v).
}
\tag{23}
$$
整性由两个原整多项式之差在 $0$、$1$ 的显示零阶给出；
$v$、$1-v$ 的 resultant 为一。
其全部系数也由
$$
v(1-v)P'+[a-(a+b)v]P
=C_{c,k+1}v^c(1-v)-C_{c,k}
\tag{24}
$$
及 $P(0)=-\binom{a+k}{k}$ 唯一确定。
例如 $0\le j<c$ 时
$$
[P]_j=-\binom{a+k}{k}
 \frac{(a+b)_j}{(a+1)_j},\qquad
[P]_c=\frac{C_{c,k+1}}{a+b+c}.
$$
这些比值作为特征零恒等式使用；
不把其中某个非单位分母单独反演后约化。

相邻 $q$ 对应 $H$ 增六、$k$ 增 $p+1$。
因此整个特征零差是有限的
$$
\boxed{
F_{c,k+p+1}-F_{c,k}
=\sum_{j=0}^{p}
 v^{c(k+j)+1}(1-v)^{k+j+1}P_{c,k+j}(v).
}
\tag{25}
$$
$c=2$ 是三处，$c=6$ 是十三处。
完整两级权的差按普通乘积差展开，并逐项保 (25)。

高 $q$ 时，十三处原权虽在模 $p$ 都等于
$v_\pi^{p^2}$，它们的特征零差一般只是被 $p$ 整除，
不能从模 $p$ 饱和式把它从整个 $p^{K(H)}$ 比较中删除。

对同一原 canonical 来源 $f$，相邻两完整返回的质量
Gaussian 相同，故 (7) 真正给
$$
j_{10,h_{q+1}(f)}-j_{10,h_q(f)}
\in p^{\min(K(H+6),K(H))}\mathcal O.
\tag{26}
$$
在坏 canonical 假设下，每个原 mass0 返回也各自满足相应深零。
(21) 描述的是其实际模 $p$ first-Cartier 权差；
其高精度来源是 (25)–(26)，并非另加一个非canonical零。

## 7. 原实际非零系数仍在这个完整精度内

R1025 §11 的同一个特征零输入 $Z^9F_H\omega_E$，
在每个原二挠点的 selected coefficient 是
$\widetilde\rho_p^{\,8}T_H(p)$，其中
$$
T_H(p)=\sum_{j=0}^{A}(-1)^j\binom Aj
 \frac{(2/3)_{N_0-j}}{(N_0-j)!\,[p+2(N_0-j)+1]},
\quad N_0=3q+1,\quad A=2q+2.
\tag{27}
$$
这里 $N_0$ 不是 (1) 的长前缀 $N$。
原正矩证明给 $0<T_H(p)<1$，
$\widetilde\rho_p$ 是原有理 Beta 值且在目标 $p$ 为单位。

完整分母整除
$$
D'=3^{N_0}N_0!
 \prod_{n=q-1}^{N_0}(p+2n+1),
\qquad p\nmid D'.
$$
下面重新支付本篇较大 $q$ 的严格常数。
$N_0<p/2$，各后因子小于 $2p$。
由
$N_0!\le eN_0(N_0/e)^{N_0}$，得到
$$
\frac{D'}{p^{5q+4}}
<12(3q+1)\left(\frac{27}{2e^3}\right)^q
<12(3q+1)(3/4)^q.
$$
当 $q=32$，$(3/4)^8<1/8$ 且 $12\cdot97<4096$；
之后相邻比严格小于一。
对 $3\le q<32$，原 $p>13^4$ 已保证 $p\ge6H$，
直接用 R1025 原较小参数的分母界。
所以整个 (1) 内都有
$$
\boxed{
v_p(T_H(p))<5q+4<
\min(6q+6,5s-2)=K(H).
}
\tag{28}
$$
末参数 $q=s-2$ 仍有 $5q+4=5s-6<5s-2$ 的严格余量。

(28) 是同一个实际有理输入系数的深度，
不是为模 $p$ Cartier 自选提升。
它不删除 R1025/R1024 的完整 $GP_{10}$ 项；
要导出 canonical 坏条件的不相容，
仍须在 (26) 的同一个全精度读者中消去该项。

## 8. 继续联立的准确共同对象

在饱和区间 $q_{\rm sat}\le q\le s-2$，
原十三处在第二 Cartier 后是同一个固定 $v_\pi$，
三处变化由 (21) 和特征零 (25) 完整给出。
全部六维边界、第一 primitive、原点留数、
真实外部 $\tau$ 位置和 sigma 折回都仍在。
R1024 的 weighted primitive 恒等可以直接对这些共同输入使用，
不能只保第三 Cartier 或把 $v_\pi$ 移出不相容的 source 点。

本篇不把连续多个 flat 返回称为多个独立的算术来源。
新的实际输入是一个完整高精度家族、
其确定的邻差、已付第一整除 $p$ 步，
以及在同一精度内严格非零的原 selected coefficient。
全部结论为手证，未执行本地数学或新增素数扫描。


## 9. 末六权的原特征零比较实际达到 H+1 位

追加日期：2026-11-28 UTC。这里把 R1034 §5、§11.3 已付的
真实整展开和第二半径用于本篇原来的两个特征零 trace 顺序。
结论加强 (6)–(7) 的尾精度；不改动 flat 权、原来源、
任何一个外部 pull 或物理读者。

### 9.1 包含非零质量的同一个整展开

取本篇原 principal 来源
$f=\sigma^{390}R_f(X)$，$\deg R_f\le65$、$R_f\in\mathcal O[X]$。
$\mathcal O$ 是原好位的非分歧系数环，$v_p(p)=1$。
对 (2) 的任一种完整顺序，(4) 的实际返回在
$u=x^{-1/2}$ 中具有
$$
A_{10,\alpha}(f)=u^{-10}\sum_{j\ge0}a_ju^{6j},
\qquad a_j\in\mathcal O,\qquad a_0=m_0(f).
$$
记 $w=z^6$、$W_0=z^2x$、
$U_\sigma=(\sigma/z)e^{-cz^{p+1}}$，则整个 target Gaussian 是
$$
\boxed{
G_{10,h}(z)=
\sum_{j\ge0}a_jw^jU_\sigma^{10}W_0^{\,5-3j}.
}
\tag{29}
$$
这正是 R1034 §5 的展开，但本节保留 $j=0$。
所有负整数幂都是同一个常数一单位的真逆；
每个给定系数只读有限多个 $a_j$。
因此增长的极帽、增长的分子以及两种 trace 顺序
都不会增加一个依赖 $H$ 的垂直分母。

原 source 也有同一形式：
把 $R_f=u^{-390}\sum_{j=0}^{65}b_ju^{6j}$ 代入，
其 Gaussian 为
$\sum b_jw^jU_\sigma^{390}W_0^{195-3j}$。
R614 (9) 于是直接给两者在全部 $w$ 指标 $<L=s(p-1)$ 的整性。
这里没有使用质量零才成立的 $hs-1$ 指标，
也没有把 $n<2L$ 的端点扩到 $n=2L$。

保原
$$
q_\alpha=\frac{\alpha^{p+1}}{39}=q_\delta q_\pi,\qquad
\gamma_\alpha=10c(\alpha^{p+1}-39)\in\mathcal O.
$$
用于长前缀比较的两个实际 charge390 Gaussian 是
$$
\boxed{
G_f=e^{-390cz^{p+1}}f,\qquad
G_\alpha=e^{-390cz^{p+1}}h(\alpha z)
=e^{\gamma_\alpha z^{p+1}}G_{10,h}(\alpha z).
}
\tag{30}
$$
$\alpha$ 为单位。在 $w$ 指标 $<L$ 内，
额外指数只使用 $k<p-1$ 的 $k!$，故仍整。
所以 (30) 的每一个中央系数
$g_h=[w^{hs}]G$ 在 $1\le h\le p-2$ 都整。
两个 Gaussian 没有被认作相同的函数。

### 9.2 全无限尾及其准确端点

使用 R618 的同一第二半径
$$
\tau_2=\frac{2p-1}{p(p^2-1)},\qquad
R_2=p^{-\tau_2},\qquad
\eta_p=1-(p+1)\tau_2>0.
$$
在每个严格内闭盘 $R<R_2$ 上，
$U_\sigma,W_0,W_0^{-1}$ 及 $u/z$ 都有范数一；
(29) 中 $|u|=R<1$，故整个级数的范数至多一。
源端有限和也满足同一界。
这里保非零质量，所以不使用质量零时额外的 $R^6$ 收益。

又 $(p+1)\tau_2>1/(p-1)$，
所以 (30) 中的整指数及其逆在这些盘上同样为范数一的单位。
由严格内盘趋向 $R_2$ 得到系数界，
不宣称 $U_\sigma$ 在临界闭盘是 Tate 元。

对 (30) 的任一 Gaussian，令
$$
T_h=(-1)^{h-1}(h-1)!(390c)^{-h}g_h.
$$
原 $v_p(390c)=-1$，故完整的有限窗和无限尾分别满足
$$
\boxed{
v_p(T_h)\ge h\quad(1\le h\le p-2),\qquad
v_p(T_h)\ge\lceil h\eta_p\rceil+v_p((h-1)!)
\quad(h\ge1).
}
\tag{31}
$$
第二式是 R618 (25) 去掉质量零的 $6\tau_2$ 后的同一证明；
它也直接由上述范数界和整数赋值给出。

在 $h=p-1$，
$(p-1)\eta_p=p-3+1/p$，所以第二式至少为 $p-2$。
右侧随后不减并趋于无穷。
于是对本篇全部 $H\le p-6$，
$H<h\le p-2$ 的项至少有 $H+1$ 位，
而整个 $h\ge p-1$ 尾至少有 $p-2\ge H+1$ 位。
严格得到
$$
\boxed{
\sum_{h>H}T_h\in p^{H+1}\mathcal O.
}
\tag{32}
$$
这一次覆盖了全部无限尾，包括非零质量的首坏带；
不需要单独删除 $h=p$ 或借用任何坏 canonical 假设。

### 9.3 原质量 log 与两种 trace 顺序

由 (3)，(30) 的前 $H$ 个中央系数在特征零中准确相同。
将 (32) 用于二者之差，得
$j_f-j_{390,h(\alpha z)}\in p^{H+1}\mathcal O$。
R1022 (20) 的完整 Tate 恒等式仍是
$J_{390,h(\alpha z)}(v)=q_\alpha^vJ_{10,h}(v)$；
原质量由长前缀保留。
因此
$$
\boxed{
j_f-j_{10,h_{10,\alpha}(f)}
-m_0(f)\log_pq_\alpha
\in p^{H+1}\mathcal O
\qquad(3\le q\le s-2,\ H=6q+5).
}
\tag{33}
$$
若按两步写，质量项分别是
$m_0(f)\log_pq_\pi$ 与 $m_0(f)\log_pq_\delta$；
其和才是 (33)。
(33) 对两个实际顺序分别成立，
未在特征零交换原权、未除去未平均 trace 的39支或任何 Miller 相位。

特别，R1028 的末六权
$H_t=p-6t$、$1\le t\le6$ 分别有精度
$$
\boxed{
K_t^{\rm new}=H_t+1=p-6t+1.
}
\tag{34}
$$
六权共同精度可取 $p^{p-35}$；
末两权 $t=1,2$ 的共同精度可取 $p^{p-11}$，
各自精度为 $p^{p-5}$、$p^{p-11}$。
本篇 (6)–(7)、(26) 的原较粗界仍然正确，
而在这里的原来源和全部参数上可用 (33) 加强。

对同一个 $f$，两个返回的质量 log 相消，故
$$
\boxed{
j_{10,h_t(f)}-j_{10,h_{t'}(f)}
\in p^{\min(H_t,H_{t'})+1}\mathcal O.
}
\tag{35}
$$
若原质量零 canonical 还满足 $j_f=0$，
(33) 才分别给各个实际返回的相应深零；
这些始终是同一来源的完整 Newton 必要行。

### 9.4 新精度没有改写模 p primitive 的支持

(33)–(35) 只加强特征零长前缀的误差。
R1028 (10) 的完整余项
$c_pu^{p^2}T_t^p$、十三处权的特征零 $p$ 倍差，
以及完整 $GP_{10}$、$\chi_8$、Miller、cut、留数、
两个 exact 和 $\varphi$ 修正均保留。
不能把 $V_{\delta,t}$ 全函数换为 $W_\infty^p$。

同样，本节不把 R1028 (18) 的原低窗结论
自动延长到 (34) 的全部指标，也不宣称终端 $T_t$ 差新增独立行。
是否可见必须逐项满足实际 native 支持
$n=rp+b\le(p+1)H_t$，再经同一 physical $M$、
原 Gaussian 卷积及完整 Newton 和式读取。
提高 $p$ 精度本身不把一个中央零拆成逐系数零。

本附节只使用 R614、R618、R1022 和 R1034 已付的全系数结论，
未执行数学计算，也未改变原两条 canonical 的授权范围。
