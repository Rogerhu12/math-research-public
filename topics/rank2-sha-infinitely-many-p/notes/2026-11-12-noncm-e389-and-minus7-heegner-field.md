# 非 CM 固定曲线 E389 与负七 Heegner 域的严格证书

日期：2026-11-12。**已证明。** 本文支付一个新的固定算术输入，
不声称它已经解决无穷素数上的 Sha 有限性。

## 1. 原曲线及非 CM 性

取 R2 的固定曲线
$$
 E:y^2+y=x^3+x^2-2x.
\tag{1}
$$
R2 已以完整有限域群证书证明 $E(\mathbb Q)_{\rm tors}=0$
及 $(0,0),(1,0)$ 线性无关；所以其有理秩至少二。
直接计算给
$$
 c_4=112,\qquad c_6=-856,\qquad \Delta=389.
\tag{2}
$$
该整模型最小，只有 $389$ 处坏约化，且为 $I_1$。
$-c_6\equiv95^2\pmod {389}$，所以该节点分裂，
$a_{389}=1$、局部根数为 $-1$。故
$$
                   N_E=389,\qquad w(E)=+1.
\tag{3}
$$
其 $j=112^3/389$ 非整数，而 CM 曲线的 $j$ 是代数整数。
因此 (1) **不是 CM 曲线**；这没有使用数据库标签或大像假设。

## 2. 明确负扭曲、导子和非挠点

令 $d=-7$。对应整二次扭曲可以直接写成
$$
 E^{(-7)}:y^2+y=x^3-7x^2-98x-86.
\tag{4}
$$
确切地，将 (1) 完成平方后，对任意 $d\equiv1\pmod4$ 的扭曲为
$$
 (2y_d+1)^2=4x_d^3+4dx_d^2-8d^2x_d+d^3,
$$
在 $\mathbb Q(\sqrt d)$ 上的同构为
$$
 x=x_d/d,\qquad 2y+1=(2y_d+1)/(d\sqrt d).
\tag{5}
$$
于是 (4) 的不变量为
$$
 c_4=112\cdot7^2,\qquad c_6=293608=-856(-7)^3,
 \qquad \Delta=389\cdot7^6=45765461.
\tag{6}
$$
所有判别式赋值小于 $12$，所以整模型已最小。准确的局部表为

| 位 | $v(c_4),v(c_6),v(\Delta)$ | 型 | 导子指数 | 根数 |
|---:|---|---|---:|---:|
| $7$ | $(3,3,6)$ | $I_0^*$ | $2$ | $(-1/7)=-1$ |
| $389$ | $(0,0,1)$ | split $I_1$ | $1$ | $-1$ |
| 其他有限位 | $v(\Delta)=0$ | good | $0$ | $+1$ |

在 $7$ 处，除去 $2,3$ 分母作短模型后，
$v(a_4)\ge2,v(a_6)\ge3,v(\Delta)=6$，Tate 算法给 $I_0^*$；
剩余三次式可分，因为 $\Delta/7^6$ 是单位。
注意 $112$ 自身含一个 $7$，故表中 $v_7(c_4)$ 是 $3$。
在 $389$ 处，$-7\equiv185^2$，所以扭曲不改变 split 类型。
无穷位根数为 $-1$，从而
$$
             N_{E^{(-7)}}=389\cdot49=19061,
             \qquad w(E^{(-7)})=-1.
\tag{7}
$$

点
$$
                            R=(16,25)
\tag{8}
$$
满足 (4)，两边均为 $650$。逐个有限域计数给
$\#E^{(-7)}(\mathbb F_5)=3$、
$\#E^{(-7)}(\mathbb F_{11})=16$。
若有素数阶挠点且其阶不是 $5$，在 $5$ 约化迫其阶为 $3$，
而在 $11$ 约化不允许 $3$；若其阶是 $5$，在 $11$ 约化也不允许。
故 $E^{(-7)}(\mathbb Q)_{\rm tors}=0$，(8) 非挠。
经 (5) 得到原曲线上的实际负点
$$
 R_-=
 \left(-\frac{16}{7},\frac{-49+51\sqrt{-7}}{98}\right),
 \qquad cR_-=-R_-.
\tag{9}
$$

## 3. 严格的解析秩一证书

写 (4) 的 $L$ 级数为 $L(s)=\sum a_n n^{-s}$，并置
$$
 A=\frac{\sqrt{19061}}{2\pi},\qquad
 E_1(x)=\int_x^\infty e^{-t}\frac{dt}{t}=-\operatorname{Ei}(-x).
$$
符号 $-1$ 的 Mellin 变换在 $s=1$ 给收敛恒等式
$$
                 L'(1)=2\sum_{n\ge1}\frac{a_n}{n}E_1(n/A).
\tag{10}
$$
完整推导为
$$
 A^s\Gamma(s)L(s)
  =\int_1^\infty f(it/\sqrt{19061})
       \bigl(t^{s-1}-t^{1-s}\bigr)\,dt;
$$
求导并用 $L(1)=0$，再对每个指数项分部积分即得 (10)。

Hasse 界与 Euler 因子给 $|a_n|\le d(n)\sqrt n\le2n$，
包括 additive 的 $7$ 和 multiplicative 的 $389$。
所以对每个 $B\ge1$，
$$
 \left|L'(1)-2\sum_{n=1}^B\frac{a_n}{n}E_1(n/A)\right|
 \le \frac{4A}{B+1}
       \frac{e^{-(B+1)/A}}{1-e^{-1/A}}.
\tag{11}
$$

[完整整数与球算术脚本](../scripts/check-e389-minus7-heegner-field.py)
取 $B=2000$、192-bit Arb，使用两套独立的系数生成器逐项比较：

1. 直接数 (4) 的点：对奇好素数及 $389$ 用完成平方后的
   三次式判别式求和，$7$ 用已证明的 additive 因子。
2. 对 (1) 枚举 $y^2+y$ 的值及每个 $x$ 的纤维，得到原 $a_q$，
   再乘原始字符 $\chi_{-7}(q)=(q/7)$；$q=7$ 置零。

两者随后分别作乘法/Euler 递推；好位
$a_{q^k}=a_qa_{q^{k-1}}-q a_{q^{k-2}}$，坏位为各自局部因子。
得到
$$
\begin{aligned}
 S_{2000}&=4.42329194407789135903503891063808498790293992897631097
                  \quad(\text{球半径}<3\cdot10^{-54}),\\
 T_{2000}&<2.788\cdot10^{-40},\\
 L'(1)&\in4.423291944077891359035038910638084987903
                         \ \pm\ 3.39\cdot10^{-40}.
\end{aligned}
\tag{12}
$$
最简可复核结论为
$$
                         \boxed{4<L'(E^{(-7)},1)<5.}
\tag{13}
$$
$a_1,\ldots,a_{2000}$ 逗号连接 ASCII 的 SHA256 为
`93c2fada5a30865f0134e7fa3eb9bba60d80a09f8e750695eb30d54f94022524`。
这是有限球区间加完整解析尾界，未使用浮点零阈值。
(7)、(13) 证明解析秩恰一；Gross–Zagier–Kolyvagin 给
$$
 \operatorname{rank}E^{(-7)}(\mathbb Q)=1,
 \qquad \Sha(E^{(-7)}/\mathbb Q)\text{ 有限}.
\tag{14}
$$

## 4. 固定 Heegner 域、基层点及固定 q

取
$$
                         F=\mathbb Q(\sqrt{-7}).
$$
Minkowski 界 $(2/\pi)\sqrt7<2$ 说明每个理想类有范数 $1$ 的
整理想，所以 $h_F=1$。$389\equiv4\pmod7$（也可用
$185^2\equiv-7\pmod {389}$）给 Heegner hypothesis。

原曲线秩至少二，由解析秩零定理的逆否命题有 $L(E,1)=0$；
结合 $w(E)=+1$，其解析消失阶至少二。故
$L'(E/F,1)=0$。Gross–Zagier 使基层 Heegner 点的高度为零。
事实上 $E(F)_{\rm tors}=0$：若 $T$ 是挠点，则 $T+cT$
为有理挠点而为零；$T-cT$ 属于 (4) 的有理挠点像而也为零，
从而 $cT=T$、$T\in E(\mathbb Q)_{\rm tors}=0$。
所以在 $\pi(\infty)=O$ 的规范下，**原基层 Heegner 点就是 $O$**。
这里类数一不需要另作固定 $3$-同源类群和。

固定 $q$ 可取
$$
  q=29=N_{F/\mathbb Q}(1+2\sqrt{-7}),\qquad
  \#E(\mathbb F_{29})=36,\quad a_{29}=-6.
\tag{15}
$$
因此 $q$ 在源 $F$ 分裂，目标 $E$ 在 $q$ ordinary，且
$q\nmid\#E(\mathbb F_q)$。这支付固定 Serre–Tate/Mellin
方法需要的一个明确普通、非异常输入；本文未把固定 $q$
非零性改称变化中的 $p$ 整原始性。

## 5. 新分支中仍须保留的额外 delta

即使基层点为 $O$，一般高层 Heegner 点的关系仍为
$N_\Gamma Y_n=a_\ell P_n$，$P_n$ 不必为零。
非 CM 曲线的 $a_\ell$ 也不恒零。因此不能照搬 CM 原分支
“所有 $Y_n$ 本身在 norm-one 群中”的除 $\delta$ 步骤。
安全构造是先用 $(\tau-1)Y_n$；它的 leading point 为
$\delta Q$，保留相应一层指数成本。本文没有证明或使用
一个尚未支付的 $\operatorname{length}\Sha(A)\le2a$ 泛化，
也没有由 (13) 宣称主曲线的无穷素数结论。

## 6. 指定基层 CM 源点的一阶 jet 确实非零

令
$$
             \tau_0=\frac{-185+\sqrt{-7}}{778}.
\tag{16}
$$
二次型 $(389,185,22)$ 的判别式为 $-7$，故对应曲线的
endomorphism order 是 $\mathcal O_F$。标准循环子群
$\langle1/389\rangle$ 的商格在乘以 $389$ 后为
$\langle1,389\tau_0\rangle$；而
$389\tau_0=(-185+\sqrt{-7})/2$ 也给最大阶。
因此 (16) 代表所需的真实 $389$-Heegner 点 $x_0$，
不是另一个未匹配的复 CM 特化。共轭方向同样可用。

令 $f=\sum a_n(E)q^n$ 为原曲线的归一 weight-two newform。
模参数化满足
$$
                  \pi^*\omega_E=c\,f(\tau)\,2\pi i\,d\tau,
                  \qquad c\in\mathbb Q^\times.
\tag{17}
$$
因而证明 $f(\tau_0)\ne0$ 就严格证明 $\pi$ 在 $x_0$ 不分歧；
不需先知道 Manin 常数 $c$ 的具体数值。

同一脚本对原曲线生成 $2500$ 个整数 Fourier 系数，
以 Acb 分别计算每个 $a_n\exp(2\pi i n\tau_0)$。
设 $r=\exp(-2\pi\operatorname{Im}\tau_0)<1$，则完整尾界为
$$
 \left|f(\tau_0)-\sum_{n=1}^B a_n e^{2\pi i n\tau_0}\right|
 \le2\sum_{n>B}nr^n
 =2r^{B+1}\left(\frac{B+1}{1-r}+\frac r{(1-r)^2}\right).
\tag{18}
$$
$B=2500$、192-bit 球算术给
$$
\begin{aligned}
 f(\tau_0)&=-18.5566721785180562871\ldots
             -66.6307467972063741128\ldots\,i
             \quad(\text{两坐标误差各}<1.492\cdot10^{-18}),\\
 -19&<\operatorname{Re}f(\tau_0)<-18,
 \qquad -67<\operatorname{Im}f(\tau_0)<-66.
\end{aligned}
\tag{19}
$$
这是固定源点的严格一阶 jet 输入。由于 $\pi$ 和 $x_0$ 都是
代数对象，在固定代数局部坐标与微分框架中该非零一阶系数
是固定数域的非零代数数；排去固定有限多个素位后仍为单位。
本结论**不推出**实际 torus $C_p$ 覆盖在该 CM 纤维上的
$\mathcal D_2$ 行非零。特别地，一般 étale 覆盖中函数可以
在整个纤维为零，而其范数迹沿基底的一阶导数非零。

## 来源

- R2 给 (1) 的完全有限域秩二下界及 torsion 证明。
- J. Cremona，*Algorithms for Modular Elliptic Curves*，
  [作者全文](https://johncremona.github.io/book/fulltext/index.html)，
  Chapter 3 的 Tate 算法/导子；本文已列出所有局部输入。
- J. Desjardins，*Root number of twists of an elliptic curve*，
  J. Théor. Nombres Bordeaux **32** (2020)，
  [出版全文](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1112.pdf)，
  Proposition 3.1 给 $p\ge5$ 的局部根数，特别是 $I_0^*$。
- Arb/FLINT 的[特殊函数球算术](https://flintlib.org/doc/algorithms/special-functions/overview.html)
  与[指数积分](https://arblib.org/arb_hypgeom.html)。
- Gross–Zagier（1986）、Kolyvagin（1990）的解析秩至多一结论，
  同课题 README/R103 的既有输入。本文只将其用于 (4)，
  没有对秩至少二的 (1) 宣称同一结论。
