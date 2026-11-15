# R788 后续：首修正带的单位源与六截面微分闭合的限制

日期：2026-11-15。状态：**下述有限恒等式和不闭合断言已证明；原本原同标签共同非零仍未证明。**

本记录接 R788，不重做其完整跨 $p$ 修正式。所需原函数、规范和
系数全部沿用 R770/R784/R788；尤其 $\kappa=6B$ 是原 Cartier
单位，不能改 Gaussian 或把一个一般六阶递推当成原函数的递推。
本记录没有新增正式计算或素数窗口。

## 1. 六个零行在第一条修正带上的准确方程

写 $p=6N+5\ge41$，并置
$$
R(z,t)=P(z+t)Q(z-t),\qquad K=(1+\Phi_p)R
\quad\text{于 }R_p=\mathbf F_p[z,t]/(z^p,t^p),
$$
其中 $P,Q,\Phi_p$ 恰是 R788 (788.3)、(788.5)，不是新选的多项式。
记
$$
(1+X)^4(1-X)=\sum_{j=0}^5 k_jX^j,\qquad
(k_0,\ldots,k_5)=(1,3,2,-2,-3,-1).
\tag{Z1}
$$
$R$ 的最低齐次项是 $(z+t)^4(z-t)$，总次数五；
$\Phi_p$ 总次数 $p+1$。故 $K$ 的总次数 $p+6$ 部分准确为
$$
\sum_{i=1}^N f_i g_{N+1-i}
(z+t)^{6i+4}(z-t)^{p+2-6i}
+\Phi_p(z,t)(z+t)^4(z-t).
\tag{Z2}
$$
和式端点为 $1\le i\le N$，因为 $P,Q$ 都只保留指标至 $N$；
原非整端点 $f_{N+1},g_{N+1}$ 已准确包含在 $\Phi_p$ 中，不能再加入。

对 $12\le b\le17$，定义
$$
C_b=\sum_{\substack{0\le j\le5\\b-j\ {\rm even}}}
\frac{k_j}{(b-j)(b-j-1)}\in\mathbf F_p.
\tag{Z3}
$$
此处 $7\le b-j\le17<p$，显示分母均为单位。由 R788 已经合法
除 $p$ 的表达式，(Z2) 的对应系数是
$$
\boxed{
M_{p+6-b,b}=
\sum_{i=1}^N
[X^b](1+X)^{6i+4}(1-X)^{p+2-6i}
f_i g_{N+1-i}
-2\kappa C_b.
}
\tag{Z4}
$$
这条式子在原数据上无条件成立。

若另外假设**全部未筛** critical 乘积
$f_i g_{N-1-i}$（$0\le i<N$）皆为零，R788 (788.22) 给
$p-11,\ldots,p-6$ 六个完整零行。因
$p+6-b$ 正好遍历这六个行指标，(Z4) 遂给六条方程
$$
\sum_{i=1}^N
[X^b](1+X)^{6i+4}(1-X)^{p+2-6i}
f_i g_{N+1-i}=2\kappa C_b,
\qquad12\le b\le17.
\tag{Z5}
$$
所以这六个零行确实接到了同一个原 Cartier 源，且不含未知高阶
有限部。但右侧非零并不意味着左侧必须零：左侧仍是总指标
$N+1$ 的原整高带，而假设只涉及总指标 $N-1$。

### 1.1 六条源项不会同时消失

第十二项正好对应此前十二阶下降记录中的整数 $659$：
$$
C_{12}=\frac1{132}+\frac1{45}-\frac3{56}
=-\frac{659}{27720}.
\tag{Z6}
$$
因此只看这一条会在允许素数 $p=659$ 丢失源项。
第十三项则为
$$
\begin{aligned}
C_{13}
&=\frac3{12\cdot11}-\frac2{10\cdot9}-\frac1{8\cdot7}\\
&=\frac1{44}-\frac1{45}-\frac1{56}
=-\frac{481}{27720}
=-\frac{13\cdot37}{2^3 3^2 5\cdot7\cdot11}.
\end{aligned}
\tag{Z7}
$$
全部允许素数均至少为 $41$，故 $C_{13}$ 始终是单位。
因 $\kappa\ne0$，(Z5) 的六维源向量始终非零。
这排除了六条源在某个允许素数一起退化的可能，
但没有消去 (Z5) 的整高带。

## 2. 同一修正的有限微分表达

普通偏导在 $R_p$ 上合法，因为 $\partial_z(z^p)=0$、
$\partial_t(t^p)=0$。直接对 R788 的多项式求导，得
$$
\boxed{
(\partial_z^2-\partial_t^2)\Phi_p
=2\kappa(z^{p-1}-t^{p-1}).
}
\tag{Z8}
$$
逐项核对如下：$z$ 两次求导的乘数模 $p$ 是
$(p+1-r)(p-r)=r(r-1)$，所以给
$$
-2\kappa\sum_{\substack{2\le r\le p-1\\r\ {\rm even}}}
z^{p-1-r}t^r.
$$
负的 $t$ 两次求导在换指标 $r-2=s$ 后给
$$
2\kappa\sum_{\substack{0\le s\le p-3\\s\ {\rm even}}}
z^{p-1-s}t^s.
$$
中间项逐项抵消，仅留下 (Z8) 两个端点。

由此得到不需要除 $P,Q$ 或 $K$ 的多项式恒等式
$$
\boxed{
K(K_{zz}-K_{tt})-K_z^2+K_t^2
=2\kappa(z^{p-1}-t^{p-1})K^2
\quad\text{于 }R_p.
}
\tag{Z9}
$$
证明时先注意 $R=P(z+t)Q(z-t)$ 满足
$$
R(R_{zz}-R_{tt})-R_z^2+R_t^2=0,
$$
因为 $\partial_z^2-\partial_t^2=4\partial_u\partial_v$
于 $u=z+t,v=z-t$。然后代入 $K=(1+\Phi_p)R$。
两个 $\Phi_p$ 一阶导数的乘积以及 $\Phi_p$ 乘其二阶导数，
总次数均为 $2p>2p-2$，在有限方框中为零。
剩余项就是 $(\Phi_{p,zz}-\Phi_{p,tt})R^2$。
将 $R^2$ 换成 $K^2$ 所增加的项同样超出总次数上界，
再用 (Z8) 即得 (Z9)。整个证明没有使用 $\log K$；
$K$ 的最低次数为五，它不是这个有限环中的单位。

(Z9) 的右侧确实不为零：其 $z^{p-1}t^{10}$ 系数是
$2\kappa$，因为 $K(0,t)=-t^5+O(t^{11})$，而 $p-1>10$。
这个微分源再次保留了原 Cartier 单位。
但其左侧相应系数是两个核齐次层总指标为 $N+1$ 的混合，
不是仅由 critical 的 $f_i g_{N-1-i}$ 组成。
因此不能由 (Z9) 把同标签共同零问题宣布为已解。

## 3. 原六截面不形成一个闭合的常系数微分系统

去掉原公共因子 $\sigma^{12}$，R784 的六个有理函数是
$$
-x^2y,\quad (x^3-4)^2,\quad
-2y(x^3+2),\quad x^2(x^3-4),\quad
3xy(x^3-4),\quad x^4.
\tag{Z10}
$$
它们在 $O$ 的极阶依次为 $7,12,9,10,11,8$，没有其他极点。
令它们的常数域线性张成为 $V$。对所有允许 $p$，
$$
D\bigl((x^3-4)^2\bigr)=12yx^2(x^3-4)
\tag{Z11}
$$
有恰好十三阶极点，其首系数 $-12$ 非零。
因此 $DV\not\subset V$。

更强地，不存在有理函数 $a\in\overline{\mathbf F}_p(E_0)$
使得 $(D+a)V\subset V$。事实上，(Z10) 中
$(x^3-4)^2$ 与 $x^4$ 没有共同有限零点。
若 $a$ 在某有限点有极点，至少一个 $aq_j$ 在该点有极点；
$Dq_j$ 仍正则，故 $(D+a)q_j$ 不可能属于 $V$。
所以 $a$ 只能在 $O$ 有极点。
若其极阶至少二，则 $a(x^3-4)^2$ 的极阶至少十四，
不能与 (Z11) 的十三阶项相消。故其极阶至多一。
亏格一曲线上不存在只有一个至多一阶极点的非常数函数，
所以 $a$ 为常数；这又无法消去 (Z11) 的十三阶项。

这是一条精确的闭合限制，而不是否认可以构造一般亚纯连接。
原截面求导必须保留
$$
D(q_j\sigma^{12})=\sigma^{12}(Dq_j+12\zeta q_j).
\tag{Z12}
$$
公共 $\zeta$ 项不能扔掉；它也不是一个在 $E_0$ 上全局单值的
有理函数。任意写出的可变矩阵连接还必须说明其原几何来源、
允许极点、规范和实际 $p$-curvature，才能约束本题的 Taylor 零支撑。
低六阶 Wronskian 可逆只说明六个低阶 jet 独立，
不能据此断言 $p-11,\ldots,p-6$ 的六个高阶泛函不同时为零。

## 4. 已有 Cartier 输入与仍缺的步骤

R601 §3 已经完整给出原有理原函数
$$
q=-B^{-1}D^{p-2}x,\qquad Dq=1,\qquad
q=z-B^{-1}z^{-p}+O(z^{5p}).
\tag{Z13}
$$
本记录不把它重新注册成新结果。R601 §5 的
$D^p=B\partial_E$ 作用于明确加入 completed-zeta 变量
$DE=-x$ 的代数；它不是 (Z10) 六维空间上的一个现成封闭矩阵。
R702 的高普通导数与首 pole 公式已经由这个输入得到；
单凭这些向前移位关系，不限制第一 $p$ 阶中的任意两条零支撑。

本次后续尚未证明：

- (Z5) 的全部原整高带能够被原连接或六秩 Schur 关系消去；
- R788 的真实联立系统与未筛 critical 全零不相容；
- 原筛选集合
  $\{i:(6i+7,p+1)=1,\ P_{6i+6}(1/s)\ne0\}$
  必与 $\{i:f_i g_{N-1-i}\ne0\}$ 相交。

最后一项的失败假设只给一部分单项为零，不能升级为 (Z5) 的
未筛全零假设。因而本记录不给 R770 所需的共同非零，
更不提供真正高度排根或 Serre 一致性的完成证明。

## 依赖

- [R601](../results/R601-c1-first-and-third-block-Cartier-cancellations.md)，§§3、5：原有理 primitive 与原扩展代数上的 $D^p$。
- [R702](../results/R702-first-pole-block-and-uniform-shifted-units.md)：原首 pole 范围及普通导数移位。
- [R770](../results/R770-same-primitive-label-square-and-finite-bilinear-pairing.md)：真正同标签目标与原本原筛。
- [R784](../results/R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md)：原六截面、规范和全部三通道。
- [R788](../results/R788-original-cross-p-Cartier-correction-and-rank-six-coupling.md)：合法跨 $p$ 修正式、秩六、Schur 约束和未筛六零行后果。

