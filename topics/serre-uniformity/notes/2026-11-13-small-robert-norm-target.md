# 2026-11-13：同一实际 Norm 目标的 44 次普通单位模型

**已证明的计算归约；$\mathcal L$ 仍未计算。**
固定 R171/R201 的 $p=43,q$、CM 实点和 Weil 标记。
以下把 Robert 的普通 Norm 目标写成一个 $44$ 次域生成元的简单函数，
用于后续 $43$ 维相对 Norm 方程。
它不是另一个有限素数窗口，也没有把 R204 的 $24$ 当成 $\mathcal L$。

## 1. 四挠点上的精确 Robert 函数

任意带阶 $4$ 点的曲线可写成 Tate normal form
$$
y^2+xy-b y=x^3-bx^2,\qquad P_4=(0,0).
$$
其 $\Delta=b^4(1+16b)$。除法多项式递推在该点给
$$
\psi_2=-b,\quad\psi_3=-b^3,\quad\psi_4=0,\quad
\psi_5=b^9,\quad\psi_6=b^{13},\quad\psi_7=-b^{18},
\quad\psi_{11}=-b^{45}.
$$
所以 R198 的同一函数为
$$
\mathcal F(P_4)=\frac{\Delta^{10}}{\psi_{11}(P_4)}
 =-\left(\frac{(1+16b)^2}{b}\right)^5.
\tag{1}
$$
这些是一般 Weierstrass division-polynomial 恒等式；
改变 Weierstrass 模型时分子、分母的权重均为 $120$，比值不变。

把 $2P_4$ 平移到原点，写
$$
E:y^2=x^3+a x^2+r^2x,\qquad x(P_4)=r.
$$
缩放到 Tate 模型给 $b=-r/[4(a+2r)]$，故
$$
\mathcal F(P_4)
 =4^5\left(\frac{(a-2r)^2}{r(a+2r)}\right)^5.
\tag{2}
$$
原 $A:y^2=x^3-x$ 的 $P_2=(i,1-i)$ 有 $a=0,r=i$，
因此 $\mathcal F_A(P_2)=8^5=32768$。

## 2. 同一个 $44$ 次域中的 $z$

令 $H=\langle P\rangle$、$\phi:A\to E_H=A/H$，
并记 $e_0,e_1,e_{-1}$ 为 $(0,0),(1,0),(-1,0)$ 在商曲线中的
$x$ 坐标。置
$$
r=x(\phi P_2)-e_0,\quad
e=e_1-e_0,\quad f=e_{-1}-e_0,\quad
z=-i\,r/f.
\tag{3}
$$
四挠点公式给 $r^2=ef$，所以 $\lambda=e/f=-z^2$。

沿用 R171 的指定二同源 $A\to B=A/\langle(1,0)\rangle$。
商 $B/\langle\phi_2P\rangle$ 的指定对偶二挠点产生 Hauptmodul
$$
\delta=256\lambda(\lambda-1)=256z^2(z^2+1).
\tag{4}
$$
这是带标记公式：把源 $E_H$ 的核点 $e$ 平移到原点，
二同源商有 $a_2'=-2(2e-f),a_4'=f^2$，
代入 R171 的 $\delta=16(a_2'^2-4a_4')/a_4'$ 即得 (4)。

$E_H$ 和三个二挠点在 R171 的实固定域
$H_0=F^{\langle\tau\rangle}$ 中。$\tau P_2=iP_2$，
并且这两个四挠点的 $x$ 坐标相对 $e_0$ 分别为 $r,-r$；
因此 $\tau(r)=-r$、$\tau(i)=-i$，故 $\tau z=z$。
有理标量 Cartan 子群固定 $H$ 及所有标记，所以 $z\in H_0$。

## 3. $44$ 次多项式的确切证书

R171 的 $W(t)$ 是 $44$ 次首一多项式，$t^3=\delta$。
把
$$
W(t)=W_0(t^3)+tW_1(t^3)+t^2W_2(t^3)
$$
代入，得到 $\delta$ 的精确多项式
$$
G(d)=W_0(d)^3+dW_1(d)^3+d^2W_2(d)^3
      -3dW_0(d)W_1(d)W_2(d).
\tag{5}
$$
$[H_0:\mathbb Q]=44$。R171 §4.2 的指定实嵌入取 $t$ 为 $\delta$ 的实立方根，因此 $\mathbb Q(t^3)\subset\mathbb R$。若 $X^3-\delta$ 在该基域上可约，则它的线性根只能是唯一实根 $t$；所以 $[\mathbb Q(t):\mathbb Q(t^3)]$ 只可能为 $1$ 或 $3$。它又整除 $44$，故只能为 $1$。因此 $G$ 的 $44$ 次因子确生成同一域。

程序对 $G(256z^2(z^2+1))$ 作整数因式分解，
保存次数 $44,44,88$ 的三个因子和全部整内容。
核验器不信任分解软件：它逐整数重乘所有因子，
并独立重算 (5) 与代入式。

所选因子是证书 `factors[0]`，其系数按升幂存储，
首尾均为 $1$，中间最大系数 $52$ 位。
它以
~~~text
1, -53954989986262285086541658420,
6129319325615296236460006939945138, ...
~~~
开头，并且是倒数多项式。
另一个 $44$ 次因子为把 $z$ 改成 $-z$；其余次数为 $88$。

为何选第一个因子而非任意有限根：
对 R171 的同一个全局几何 $z$，(5) 与 (4) 证明三个因子的
乘积全局为零。在已固定的 $q$ 素点，核验器直接从
$\phi_jP_2,e_{0,j},e_{\pm1,j}$ 算出全部 $44$ 个 $z_j$；
恰第一个因子为零，另外两个均不为零。
所有这些元素在该处可约减，因此全局为零的因子只能是第一个。
$44$ 个 $z_j$ 的剩余值互异，故其全局 Cartan 共轭也互异；
$[K(z):K]=44$，再由 $z\in H_0$ 得
$$
\mathbb Q(z)=H_0,\qquad F=\mathbb Q(z,i).
\tag{6}
$$
这也证明所选 $44$ 次因子不可约，不需另相信数值辨认。

## 4. 普通单位与恰当投影

定义
$$
u=\frac{z-i}{z+i},\qquad
w=u^2=\frac{a-2r}{a+2r}.
\tag{7}
$$
由 (2) 和 R198 的精确 isogeny Norm，
$$
u_0=\frac{\mathcal F_{E_H}(\phi P_2)}{\mathcal F_A(P_2)}
 =\left(\frac{(a-2r)^2}{2r(a+2r)}\right)^5
 =\left(\frac{2u^4}{1-u^2}\right)^5.
\tag{8}
$$
这里 $u_0$ 正是 R201 的原始 scalar Norm 单位，未重新缩放它。

Cartan 元素 $i$ 把 $H$ 送到 $iH$，
其诱导同构交换 $e_1,e_{-1}$ 并把 $x$ 乘 $-1$。
代入 (3) 得
$$
\sigma_i z=1/z,\qquad
\sigma_i u=-u^{-1},\qquad
\sigma_i u_0=-u_0u^{-30}.
\tag{9}
$$
最后的 $-1$ 必须保留；有限域复算也直接验证这个符号。
$\tau z=z$ 还给 $\tau u=u^{-1}$。

在 R185/R201 的 $\chi$-投影中 $\chi(i)=-1$，
而 $\mu_2$ 在奇数 $p$ 的单位完成中为零。
因此对同一投影 $\Pi_\chi$，
$$
-2\Pi_\chi[u_0]=-30\Pi_\chi[u],\qquad
\boxed{\Pi_\chi[u_0]=15\Pi_\chi[u].}
\tag{10}
$$
这个等式在 Teichmüller $p$ 进完成中成立，
不只是一个任意模 $p$ 的替换；$15$ 在 $43$ 可逆。
$u_0$ 及其共轭在 $\{2,p\}$ 外为单位，(9) 迫使 $u$
在同一支撑外也是单位。

故 R201 的两个普通目标可在
$F=\mathbb Q[z,i]$ 中由 (7) 的简单函数与 (10) 构造，
不必先构造 $1848$ 次 torsion 域或保留全部 division polynomial。
仍须保留原有模 $p^2$ Kummer-zero 规范；
(10) 提供准确的全 $p$ 进比例，不能忽略其整数提升。

## 5. 实际检查与边界

独立标准库程序重新算全部 $44$ 条曲线及 $1848$ 个 $\psi_{11}$ 值，
逐条验证 (3)、(7)、(8)、(9)，检查所有 $z_j$ 互异，
并验证完整整数因式分解。
程序和证书为：

- [verify_small_robert_norm_target.js](../scripts/verify_small_robert_norm_target.js)
- [small_robert_norm_target_certificate.json](small_robert_norm_target_certificate.json)

~~~sh
node scripts/verify_small_robert_norm_target.js notes/small_robert_norm_target_certificate.json
~~~

全部 $44$ 行的标准 JSON SHA256 为
`e42b85b60bfc9f9f1fadf3af2429de9c6e66bd468cbbd910a8ebdaf7c13d73d1`；
源可重新生成，不提交冗长中间行。
实际输出保留 `actual_L_computed:false`。

此处不存在一个仅依赖有理式 $u=(z-i)/(z+i)$ 的通用 Norm 恒等式：
把 $z$ 当不定元，对非平凡 constant cyclic $L_q/K$，
$z=i$ 处延拓惰性剩余次数为 $43$，而 $u$ 的赋值为 $1$，
所以 $u$ 在 $L_q(z)/K(z)$ 并非 Norm。
实际存在性使用 $44$ 次 CM 多项式、正确角色投影及 R201 的全局条件。
后续必须真正利用这些关系或 R191 的主化元素；本笔记没有求出 $\mathcal L$。
