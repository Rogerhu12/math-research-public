# R481 — 精确平端使五个真实 cap 门处处正则，及有限径向下降

本稿仅作纸面证明；没有执行程序、积分、符号化简、秩、profile、开发检查或旧研究。它消费 [R471](R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md) 的五个完整 cap 门和原密度，以及 [R475](R475-exact-four-column-cap-projection-and-one-real-mirror-condition.md) 的允许 cap 类。新的结论是：保留原精确 \(\psi _3\) 左平端后，**每一个允许 cap 的五门微分均已满秩**；不必先用高阶 jet 扰动选一个泛型 cap。该结论给出每个非零残差点的真实有限径向下降，但不把局部下降升级为全局零目标可达。

## 1. 固定数据和可变域

设左 cap 为 \(u=U(\eta)\)，\(\ell<\eta\le0\)，并记
\[
 p=U',\qquad r=U'',\qquad q=U''',\qquad A=6pq-2r^2 .
\]
采用 R475 的真实允许类：
\[
 U,p,r,q>0,\quad A>0\quad(\ell<\eta<0),\qquad
 A(0)=0,\quad A'(0)\ne0.                                      \tag{1}
\]
在左端，\(U\) 等于一个正倍数、正仿射输运的
\[
 \psi _3(y)=\exp[-3/(1-y^2)]
\]
的左平端 germ；在右端固定整个简单 \(A\) 根 germ。所有变动取真紧支于 \((\ell,0)\)，因此两端仍与原函数在某个邻域准确相同。这里“固定 germ”指函数在端点的某个邻域相同；不要求把整个预先指定的长尾区间冻结后再在该冻结区间内变动。

固定
\[
 r_*=r(0)>0,\qquad s=p(0)/r_*>0,\qquad h=U(0)/r_*>0 .
\]
R471 已给
\[
 h>\frac35s^2.                                                 \tag{2}
\]
端点 jets 不动，故 \(r_*,s,h\)、原四个端点多项式 \(k,j,m,R\) 及以下所有线性行均固定。

对完整 \(X_H\) cap self，R471 定义
\[
 {\cal H}(x)=r_*^{-5}\left\{
 P_H(x,U(0),p(0),r(0))+
 \int_\ell^0 L(x+\eta,U,p,r)\,d\eta\right\}.                     \tag{3}
\]
原积分没有删掉，仍是真单侧 cap primitive。令 \(\mathfrak r\) 为 R471 用 \(k,j,m\) 的 \(x^8,x^7,x^0\) pivot 所定义的真实线性消元，并写
\[
 \mathfrak r({\cal H})=\sum_{\nu=1}^6\beta_\nu x^\nu,\qquad
 R_5=-4s^3-34hs<0.
\]
五个原门为
\[
 F(U)=(\Delta_1,\Delta_2,\Delta_3,\Delta_4,\Delta_6),\qquad
 \Delta_\nu=R_5\beta_\nu-R_\nu\beta_5.                          \tag{4}
\]
其同时为零与该 cap 的完整 \(\mathfrak h\in\operatorname{span}\mathfrak y\) 等价，比例按 R471 唯一恢复。本稿不另换门、不删复余量，也不把单侧积分换成全母积分。

## 2. 五条固定线性行

在 \(\operatorname{Pol}_{\le8}\) 上定义
\[
 \lambda_\nu(P)=R_5[x^\nu]\mathfrak r(P)
               -R_\nu[x^5]\mathfrak r(P),
 \qquad \nu\in\{1,2,3,4,6\}.                                  \tag{5}
\]
它们满足
\[
 \lambda_\nu(k)=\lambda_\nu(j)=\lambda_\nu(m)
 =\lambda_\nu(R)=0.                                           \tag{6}
\]
这些五行线性独立。理由是 \(\mathfrak r\) 的像正是六维的
\(x,x^2,\ldots,x^6\) 空间，而 \(R_5\ne0\)；在这个空间，(5) 是消去同一非零向量 \(R\) 后的五条独立行。R470 的四列也因 R475 的四高系数 determinant 非零而独立。

对任意一条非零组合
\[
 \lambda=\sum_{\nu}b_\nu\lambda_\nu,\qquad b\ne0,
\]
令
\[
 P_k(\eta)=\lambda_x((x+\eta)^k),\quad 0\le k\le7.              \tag{7}
\]
则
\[
 P_k=\frac{k!}{7!}\frac{d^{\,7-k}}{d\eta^{\,7-k}}P_7.           \tag{8}
\]
而且
\[
 P_7\not\equiv0.                                               \tag{9}
\]
确实，若 \(P_7\equiv0\)，展开平移的七次幂就得到
\(\lambda(1)=\cdots=\lambda(x^7)=0\)。原 \(k\) 的最高项为
\(-3x^8\)，其余次数不超过七，故 \(\lambda(k)=0\) 再给
\(\lambda(x^8)=0\)。这将迫 \(\lambda=0\)，与五行独立及 \(b\ne0\) 矛盾。

注意 (9) 不要求 \(P_7(\ell)\ne0\)。本稿恰要保留它可能在左平端有有限阶零的情况。

## 3. 原密度的精确分级

R471 的完整密度为
\[
 L(X,U,p,r)=\sum_{k=0}^7X^k\ell_k(U,p,r),
\]
其中
\[
\begin{aligned}
\ell_0&=U^2p^3,&
\ell_1&=-Up^4,\\
\ell_2&=\tfrac32U^2pr^2+\tfrac3{10}p^5,&
\ell_3&=-\tfrac12U^2r^3-3Up^2r^2,\\
\ell_4&=\tfrac32Upr^3+\tfrac32p^3r^2,&
\ell_5&=-\tfrac14Ur^4-p^2r^3,\\
\ell_6&=\tfrac5{16}pr^4,&
\ell_7&=-\tfrac3{80}r^5.
\end{aligned}                                                  \tag{10}
\]
每个 \(\ell_k\) 中的单项式 \(U^a p^b r^c\) 都满足
\[
 a+b+c=5,\qquad b+2c=k+3.                                     \tag{11}
\]
这不是只保最高阶的替代密度；(10) 保留了全部十二项。

固定 \(\lambda\) 后，实际变分密度为
\[
 {\cal L}_\lambda(\eta,U,p,r)
   =\lambda_x L(x+\eta,U,p,r)
   =\sum_{k=0}^7P_k(\eta)\ell_k(U,p,r).                         \tag{12}
\]
其 Euler 表达式为
\[
 {\cal E}_\lambda=
 \partial_U{\cal L}_\lambda
 -D_\eta\partial_p{\cal L}_\lambda
 +D_\eta^2\partial_r{\cal L}_\lambda.                          \tag{13}
\]
因为扰动真紧，三次端项全部为零；因为右端 jets 固定，(3) 中的
\(P_H\) 不产生变分。因此
\[
 D\bigl(b\cdot F\bigr)_U[\varphi]
 =r_*^{-5}\int_\ell^0{\cal E}_\lambda(\eta)\varphi(\eta)\,d\eta,
 \qquad \varphi\in C_c^\infty(\ell,0).                         \tag{14}
\]
原 cap primitive 的变分全部在 (12)—(14) 中，没有由总 \(n_2=0\) 删除任何一项。

## 4. 包括有限阶零的平端渐近

写 \(z=\eta-\ell\downarrow0\)，并令
\[
 \kappa(\eta)=D_\eta\log U(\eta).
\]
精确 \(\psi_3\) 平端给出
\[
 \kappa=c z^{-2}(1+O(z)),\quad c>0,\qquad
 U^{(j)}=\kappa^jU(1+O(z))\quad(0\le j\le4).                   \tag{15}
\]
正仿射输运和正倍数不改变这些结论。以下常数只用于一条固定
\(\lambda\) 和一个固定 cap；不声称对全部单位 \(\lambda\) 同时具有同一渐近起点。

设非零 \(P_7\) 在 \(\ell\) 的零阶为 \(m\)，\(0\le m\le7\)。
在充分小的正 \(z\) 上 \(P_7\ne0\)，且对所有有限阶 \(d\)
\[
 \frac{P_7^{(d)}}{P_7}=O(z^{-d})                               \tag{16}
\]
（超出次数的导数为零）。由 (8)，每一个 Euler 项中落到系数上的
\(q\) 次导数满足
\[
 \frac{P_k^{(q)}}{P_7}=O(z^{-(7-k+q)}).                        \tag{17}
\]

对 (11) 的单项式作 Euler 微分，结果是四次齐次的 jet 多项式。
若有 \(q\) 次导数落到 \(P_k\)，剩余总导数权为 \(k+3-q\)。
由 (15)，该项除以 \(P_7\kappa^{10}U^4\) 后为
\[
 O\!\left(z^{-(7-k+q)}\kappa^{-(7-k+q)}\right)
 =O\!\left(z^{7-k+q}\right).                                 \tag{18}
\]
凡 \(k<7\)，或 \(q>0\)，均至少小一阶。这个估计也覆盖
\(P_7(\ell)=0\)：系数导数的可能增大已经在 (16)—(18) 计入。

唯一不小一阶的是 \(-3P_7r^5/80\) 中没有导数落到 \(P_7\) 的项。
它的 Euler 贡献准确是
\[
 -\frac3{16}P_7 D_\eta^2(r^4)
 =-\frac3{16}P_7(12r^2q^2+4r^3U^{(4)})
 =-3P_7\kappa^{10}U^4(1+O(z)).
\]
于是得到完整结论
\[
 \boxed{\displaystyle
 {\cal E}_\lambda(\eta)
 =-3P_7(\eta)\kappa(\eta)^{10}U(\eta)^4(1+O(\eta-\ell)).}       \tag{19}
\]
特别地，任何非零五门组合的 Euler 函数都不可能在整个左 germ 上恒零。

## 5. 任意解析尾开窗上的真实满秩

令 \(I\) 是原精确 \(\psi_3\) germ 在 \((\ell,0)\) 内的一个连通解析区间，
左端为 \(\ell\)。任取非空开窗
\[
 J\Subset I.                                                  \tag{20}
\]
在 \(I\) 内，五个 \({\cal E}_{\lambda_\nu}\) 都实解析。若它们在
\(J\) 上存在一个非零常系数关系，解析延拓将使同一关系在整个 \(I\)
上为零，与 (19) 矛盾。因此
\[
 \operatorname{span}\left\{
  ({\cal E}_{\lambda_\nu}(\eta))_\nu:\eta\in J
 \right\}=\mathbb R^5.                                       \tag{21}
\]
由此可选五个不同的实际点 \(\eta_i\in J\)，使相应五列 determinant
非零。这是有限求值引理的纸面应用，不是一次执行的秩或 profile 计算。

在这些点附近取两两不交的真紧支小窗，并取积分为一的光滑 bump
\(\varphi_i\)。支撑足够小时，(14) 的五乘五矩阵任意接近 (21)
的非奇异求值矩阵。一次固定有限支撑后即有
\[
 \det\bigl(D\Delta_\nu[\varphi_i]\bigr)\ne0.                   \tag{22}
\]
全部选择均有限。没有取零宽控制，也没有只把自由 jet 秩当作已构造的函数秩。

这给出主定理：

> 对每一个满足 (1)、具有原精确平端 germ 的允许 cap，在任意一个
> 严格内部的解析尾开窗 \(J\) 中，都存在五个两两分离支撑的真实
> \(C^\infty_c\) 方向，使完整五门的微分满秩。

选择 \(J\) 后，它与两端距离为正。小参数扰动在左端更小的 collar 和
整个右根 germ 上仍准确等于原函数。\(J\) 上的 \(U,p,r,q,A\) 各有正下界，
故参数足够小时保留 (1)。窗外整个 profile 不变；既有根、端 jets 及
简单根性质不变，也不会在 \(J\) 中新增 \(A\) 根。这一保持结论不要求
在平端声称 \(p\ge\delta>0\)。

## 6. 五门径向残差的有限下降

固定 (22) 的五个控制，置
\[
 U_\theta=U+\sum_{i=1}^5\theta_i\varphi_i.
\]
真实映射 \(\theta\mapsto F(U_\theta)\) 是 \(C^\infty\)，并在零参数
可逆。有限维隐函数定理给某个实际 \(\epsilon_0>0\) 及光滑参数
\(\theta(\epsilon)\)，使
\[
 F(U_{\theta(\epsilon)})=(1-\epsilon)F(U),
 \qquad |\epsilon|<\epsilon_0,\qquad \theta(0)=0.               \tag{23}
\]
若 \(F(U)\ne0\)，取任意有限的
\(0<\epsilon<\min(\epsilon_0,1)\)，五门欧氏残差严格下降。更一般，
对任意固定正定矩阵 \(G\)
\[
 {\cal J}(U)=\tfrac12F(U)^TGF(U)
\]
在任何非零残差 cap 都有允许的严格下降方向。因为
\[
 D{\cal J}[\varphi]=(GF)\cdot DF[\varphi],
\]
而 \(DF\) 满射，所以
\[
 D{\cal J}=0\text{ 对全部允许紧支扰动}
 \quad\Longleftrightarrow\quad F(U)=0.                        \tag{24}
\]
因此在这个保端 germ 的允许类中，不存在非零残差的内部局部极小点。
这比只在某个泛型 cap 取得开放像更强，但仍不是全局存在定理。

特别应保留下面的区别：\(\epsilon_0\) 可以依赖当前 cap，并可能在连续
下降过程中趋于零。本稿没有证明所有控制的正性余量、逆矩阵、导数界、
支撑位置或共同平端 collar 具有统一界。因此不能把 (23) 无条件迭代到
\(\epsilon=1\)，不能由“没有内部非零临界点”断言最小值在允许类中取得。

## 7. 与 \(\Delta_6=0\) 及全母安装的接口

若起点已经满足 \(\Delta_6=0\)，(22) 也使
\[
 F|_{\{\Delta_6=0\}}=(\Delta_1,\Delta_2,\Delta_3,\Delta_4)
\]
在该点满秩四。可直接在五个真实参数中用第六门的一个 normal 解出
一个参数，剩四参数给局部坐标。因此 (23) 可在
\(\Delta_6=0\) 内用于剩四门；不必先改 cap 为另一个泛型点。

R475/R477 的长微小公共尾仍有其已付作用：它们给出一个实际
\(\Delta_6=0\) cap 及整根 germ 的有限安装。本稿只说明，在这个 cap
及任何其他符合原平端条件的 cap 上，完整五门微分本来就已正则。
它不否定先前的构造，也不借其余四个未计算值猜零。

若需将这里选择的 cap 安装回原母库，必须在选择 cap 后使用原
R475/R455 的从起点构造，或在已付小邻域中使用 R474 的内外支撑分离、
四 normal 的实际 IFT，再重取原受限 \(F^\star\) 图册和有限二十目标根。
本稿不声称沿 (23) 移动后旧冻结 \(F^\star\) 数值自动不变；也不把单 cap
的五门控制当作同一个完整母/实际路径的全部 joint 控制。

## 8. 当前精确结论和剩余主问题

已付的是：

- 原精确平端上，任何非零五门组合都有 (19) 的非零 Euler 渐近，包括
  最高系数多项式在平端有有限阶零的全部情形；
- 每一个允许 cap、任一解析尾内开窗，都有五个实际分离紧支控制给出
  完整五门满秩；
- 在保 \(\Delta_6=0\) 的纤维中，剩四门处处局部开放；
- 每个非零残差点都能作一次有限、严格合法的完整五门径向下降；
- 任何非零残差的内部局部极小点均被排除。

尚未付的是：下降能否在同一允许类中以有限或可控制的极限达到
\(F=0\)，或者是否存在强制下降序列逼近退化边界的全局障碍。正曲率
\(v''>0\)、真实平端、简单 \(A\) 根以及完整单侧 primitive 在这个主问题中
继续保留。R479 的多个 cap 共同系数条件也继续适用；这里的局部下降
没有把逐点 partial 改成跨 cap 的正权平均。

## 独立窄核范围

文献代理只纸核了 (19) 的最高系数 \((-3/80)\cdot5\cdot16=-3\)，以及
当 \(P_7\) 有有限阶端零时 (17)—(18) 的相对阶数。五条原线性行的定义、
\(P_7\not\equiv0\)、有限紧支满秩和本稿的适用域由作者在上述各节给出；
该窄核不冒作全稿或全局零可达的独立审查。
