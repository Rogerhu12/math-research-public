# R441 — 原第六矩条件中央行与每个同深域的精确非零

日期：2026-11-14。**状态：已证明。** 使用原已允许的完整第二输出
测试 $X^6$，可以证明同深域的中央非零，无需猜测
$S/\sigma$ 的某条无限 Taylor 余类非零，也无需随 $p$ 增长
norm-three 展开长度。

在 R437 的确定原分解
$\mathcal K(y,v)=\sigma(y-v)\mathcal L^{\mathrm{phys}}(y,v)$ 中，
残余两个输出都在 $p^n$、独立 sigma 输入为单位的真实域，对每个
正偶整数 $n$，其第一 principal 中央乘 $X^6$ 的积分赋值恰为
$5n$。它来自明确单位首项，全部高尾严格更高。

进一步用 R439 的完整同深比较，R432 的平衡 $\Sigma$ 表示可固定
$m=0$：原 $\mathcal R$ 两输出、三个 sigma 输入及唯一 Theta
的两个原 sigma 输入全部同深，指定 sigma 为单位。
对每个正四倍深度 $n$，这个同一固定隐藏域的第六矩中央赋值恰为
$7n$。完整 $X^6$ 中央行与原 $J'_S(0)$ 之间也是单位倍关系。
本篇保完整补域，不把原完整中央零分配给这些真实子域。
主目标尚未完成。

## 1. 同一原来源与固定普通 ray

保持 R431、R437、R439 的同一固定普通 ray、原周期 $\Omega$、
$b=17$、$p>19$，以及
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=\bar\pi_0^{-1}=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\quad v_p(\kappa)=1,\quad d=p-1.
\tag{1}
$$
原小核始终为
$$
\mathcal K(y,v)=-\frac23\{S(y)G_{18}(v)-C_{34}(y)F_{18}(v)\},
\qquad S=G_{16}F_{18},\quad C_{34}=G_{16}G_{18}.
\tag{2}
$$
原 $(W,Q_*)$ 坐标是
$$
W=Y+X,\qquad Q_*=9Y-17X.
$$
R437 已整有界地支付
$$
\mathcal K(w+9q,w-17q)=\sigma(26q)\mathcal L(w,q).
\tag{3}
$$
令残余来源的物理输出为
$$
Z=(17W+Q^\circ)/26,\qquad H=(9W-Q^\circ)/26,
$$
其测度记为 $\nu_{\mathcal L}^{\mathrm{phys}}$。
这里 $H$ 只是残余第二坐标，不是旧二挠来源的名称。
生成函数准确是
$$
\boxed{\mathcal L^{\mathrm{phys}}(y,v)
=\frac{\mathcal K(y,v)}{\sigma(y-v)}
=G_{16}(y)\sigma(y+v)\mathcal R(y,v).}
\tag{4}
$$
这保 R437 的显式原整卷积，不是一个仅形式存在的商。

若 $c$ 取独立原 sigma 测度，则完整原联合为
$$
\boxed{\nu_{\mathcal K}
=(Y=c+Z,\ X=-c+H)_*
                  (\nu_{\mathcal L}^{\mathrm{phys}}\otimes\nu_\sigma(c)).}
\tag{5}
$$
没有把 R430 的分离张量域与 (5) 的输入域相认。

## 2. 完整 X6 行与原算术中央的单位等价

R430 对任意连续完整第二输出测试已经给
$$
\int_{Y\in\mathbf Z_p^\times}
 d\log_p\langle Y\rangle h(X)\,d\nu_{\mathcal K}
=-\frac23J'_S(0)\int h\,d\nu_{G_{18}}.
\tag{6}
$$
对 $h(X)=X^6$，右侧常数可以完整付清。
由原
$$
x=z^{-2}-\frac b7z^4+O(z^{10}),\quad
\sigma=z+\frac b{210}z^7+O(z^{13}),
$$
及
$$
G_{18}=\sigma^{18}(x^9-30bx^6-144b^2x^3-32b^3)
$$
准确得到
$$
G_{18}(z)=1+\left(-\frac97-30+\frac3{35}\right)b z^6+O(z^{12})
=1-\frac{156b}{5}z^6+O(z^{12}).
$$
因此
$$
\boxed{\mu_6(G_{18})=-22464b\Omega^6
=-2^6\,3^3\,13\,b\,\Omega^6.}
\tag{7}
$$
当前 $p>19$、$b=17$，所以这是单位。完整原第六矩中央行是
$$
\boxed{\mathcal C_{\mathrm{full}}
:=\int_{Y\ {\rm unit}}d\log_p\langle Y\rangle X^6\,d\nu_{\mathcal K}
=14976b\Omega^6 J'_S(0),}
\tag{8}
$$
其中 $14976=2^7\,3^2\,13$，比例仍为单位。
所以这一测试保原第一中央的零与非零；没有另换一个不受原条件
控制的 tame 行或辅助中央。

## 3. 真正的残余同深域及准确返回

R439 已支付 $\mathcal L$ 的实际两态第二核：
第一轴标量是 $-\lambda$，第二轴为 $\eta_p\lambda$ 乘固定交换，
$\eta_p^2=1$，交换平方固定原 $\mathcal L$。
所以对每个正偶整数 $n$，完整联合恰有
$$
\boxed{
\nu_{\mathcal L}|_{\{W\in p^n,\ Q^\circ\in p^n\}}
=\lambda^{2n}[\kappa^n,\kappa^n]_*\nu_{\mathcal L}.}
\tag{9}
$$
偶次使全部 $\eta_p$ 与交换相位消去。
该结论保完整第二输出，不假定 $\mathcal L$ 的单次第二核已是
某个固定标量。

坐标行列式为 $-26$，是当前素数处的单位；
因此 (9) 的实际域恰等于 $Z,H\in p^n$，
均匀缩放也与坐标变换交换。
在 (5) 的确定输入空间中定义
$$
\boxed{\mathscr D_n=\{Z,H\in p^n,\ c\in\mathbf Z_p^\times\}.}
\tag{10}
$$
该域上原 $Y,X$ 都为单位，原 $W=Z+H$ 在 $p^n$，
而 $Q_*=Q^\circ+26c$ 为单位。
记真正的原第六矩中央子域为
$$
\mathcal C_n=
d\int_{\mathscr D_n}\log_p\langle c+Z\rangle
                               (-c+H)^6\,
                 d\nu_{\mathcal L}^{\mathrm{phys}}d\nu_\sigma(c).
\tag{11}
$$
令
$$
\boxed{
\mathcal A(T)=d\int_{c\ {\rm unit}}\int
 \log_p\langle c+TZ\rangle(-c+TH)^6\,
              d\nu_{\mathcal L}^{\mathrm{phys}}(Z,H)d\nu_\sigma(c).}
\tag{12}
$$
在 $T\in p\mathcal O$ 上完整收敛，后面也给全部系数估计。
(9) 直接给
$$
\boxed{\mathcal C_n=\lambda^{2n}\mathcal A(\kappa^n)
\qquad(n\ge2\text{ 为偶数}).}
\tag{13}
$$
这是原域 (10) 的全函数返回，没有用同边际替换隐藏输入。

## 4. 残余完整首五阶与 log 常数项的准确消失

由 (4) 的 $G_{16}(0)=0$，有全函数身份
$$
\boxed{\mathcal L^{\mathrm{phys}}(0,v)=0.}
\tag{14}
$$
因此整个 $H$ 推前为零，特别所有 $\int H^j\,d\nu_{\mathcal L}^{\mathrm{phys}}$
都为零。它在 (12) 中精确杀掉 $\log_p\langle c\rangle$
乘多项式 $(-c+TH)^6$ 的全部项，不只杀掉一个质量。

R424 的实际首项
$G_{16}(y)=y^2+\cdots$、$F_{18}(y)=y^4+\cdots$、
$G_{18}(y)=1+\cdots$，以及原 $\sigma(y-v)=(y-v)+\cdots$，
给完整首个齐次部分
$$
\boxed{
\mathcal L^{\mathrm{phys}}(y,v)
=-\frac23(y^5+y^4v+y^3v^2+y^2v^3)
       +\text{总次数至少 }11\text{ 的项}.}
\tag{15}
$$
也可直接由 (4) 的
$\mathcal R(y,v)=-2(y^2+v^2)/3+\cdots$ 得到。
其共同 $\mu_6$ 权为五，所以之后只出现总次数
$5,11,17,\ldots$；没有总次数六至十的项。

记
$$
M_{a,j}=\int Z^aH^j\,d\nu_{\mathcal L}^{\mathrm{phys}}.
$$
它们全为整数环中的有界矩，(15) 给
$$
\boxed{M_{a,j}=-\frac23a!j!\Omega^5
 \quad\text{当 }(a,j)=(5,0),(4,1),(3,2),(2,3),}
\tag{16}
$$
而总次数五的另外两个矩为零。
总次数小于五的全部矩同样为零。

## 5. 第五次系数是对全部原素数的明确单位

展开真正单位输出的完整 log：
$$
\log_p\langle c+TZ\rangle
=\log_p\langle c\rangle+
 \sum_{a\ge1}\frac{(-1)^{a-1}}a T^aZ^ac^{-a}.
$$
第一个常数项已由 (14) 消失。
另有
$$
(-c+TH)^6
=\sum_{j=0}^6\binom6j(-1)^{6-j}c^{6-j}T^jH^j.
$$
在 $T^5$ 中，$a+j=5$。
两个符号的乘积为
$(-1)^{a-1+6-j}=(-1)^{10-2j}=+1$。
由 (16)，只有 $j=0,1,2,3$ 留下，全部真实系数为
$$
\boxed{\begin{aligned}
[T^5]\mathcal A
&=-\frac{2d}{3}\Omega^5
 \left(24+36+60+120\right)
 \int_{c\ {\rm unit}}c\,d\nu_\sigma(c)\\
&=-160d\Omega^5 I_1^\times(\sigma).
\end{aligned}}
\tag{17}
$$
四个数是
$\binom6j(4-j)!j!$，包括了 log 与第六次测试的全部碰撞。
$\log\langle c\rangle$ 对应的 $H^5$ 矩已精确为零，不能额外添加。

原 sigma 的同一完整 core 给
$$
I_1^\times(\sigma)
=(1-\lambda_\sigma\kappa)\Omega.
$$
因此
$$
\boxed{
a_5:=[T^5]\mathcal A
=-160d(1-\lambda_\sigma\kappa)\Omega^6
\in\mathcal O^\times.}
\tag{18}
$$
这里 $160=2^5\cdot5$、$d=p-1$，而
$\lambda_\sigma\kappa\in p\mathcal O$。
这只用原已付一次单位矩；没有任何固定负矩非零假设。

## 6. 所有高尾严格更高，所以每个同深都非零

对总次数 $k$，log 与第六次测试的每一项分母只可能是
$a=k-j$，$0\le j\le6$、$a\ge1$。
所有残余矩与单位 $c$ 的正、负矩均整，故
$$
v_p([T^k]\mathcal A)\ge
-\max_{\substack{0\le j\le6\\k-j\ge1}}v_p(k-j)
\ge-\lfloor\log_p k\rfloor.
\tag{19}
$$
这个下界保证 (12) 在 $p\mathcal O$ 上一致收敛，允许逐项积分。
(14)、(15) 还给
$$
\mathcal A(T)=a_5T^5+
                 \sum_{\ell\ge1}a_{5+6\ell}T^{5+6\ell}.
\tag{20}
$$

对于 $k\ge6$、$p>19$，
$$
\lfloor\log_p k\rfloor\le\frac{k-1}{p-1}<k-5.
$$
所以对每个整数 $n\ge1$，所有 $k>5$ 的项都满足
$$
kn-\lfloor\log_p k\rfloor\ge5n+1.
\tag{21}
$$
这甚至不需要先删除 (20) 中不存在的次数六至十。
(18)、(19)、(21) 因而给
$$
\boxed{\kappa^{-5n}\mathcal A(\kappa^n)
\equiv-160d(1-\lambda_\sigma\kappa)\Omega^6\pmod p,}
\qquad
\boxed{v_p(\mathcal A(\kappa^n))=5n.}
\tag{22}
$$
合并原域返回 (13)，得到：

**定理。** 在同一个原普通 ray 上，对每个正偶整数 $n$，
$$
\boxed{
v_p(\mathcal C_n)=5n,\qquad
\lambda^{-2n}\kappa^{-5n}\mathcal C_n
\equiv-160d(1-\lambda_\sigma\kappa)\Omega^6\pmod p.}
\tag{23}
$$
所以每一个这样的真实同深域都严格非零，而不只是存在某个深度。

这些域在固定输入表示中嵌套。
若 $n,n+2$ 为正偶数，则
$\mathscr D_{n+2}\subset\mathscr D_n$，
实际环域 $\mathscr D_n\setminus\mathscr D_{n+2}$ 的相同第六矩中央为
$\mathcal C_n-\mathcal C_{n+2}$，赋值仍准确是 $5n$。

## 7. 固定 m=0 的原 Sigma 隐藏同深域也每次非零

R437、R439 保同一原平衡表示的全部权，已证明对
$n\in4\mathbf Z_{\ge1}$、$M=2m+1$，
$$
\boxed{\ell_{m;n,n}
=\lambda^{(3+2M)n}\kappa^{2Mn}\,
 \nu_{\mathcal L}|_{\{W,Q^\circ\in p^n\}}.}
\tag{24}
$$
这是完整输出测度等式，不是两个底层事件相等。
它可以与同一个独立 $\nu_\sigma^\times(c)$ 张量，
并对原 $Y,X$ 作任意相同完整测试。

因此在 R432 的原 $\Sigma\mathcal R$ 表示中，保
$\mathcal R$ 两输出均在 $p^n$，三个 sigma 输入 $a,b,e$ 均在
$p^n$，全部 $2M$ 个 Theta 原 sigma 输入均在 $p^n$，
并保指定 $c$ 为单位。
其真正第六矩中央 $\mathcal C_{m,n}^{\mathrm{hid}}$ 满足
$$
\boxed{
\mathcal C_{m,n}^{\mathrm{hid}}
=\lambda^{(3+2M)n}\kappa^{2Mn}\mathcal C_n,\qquad
v_p(\mathcal C_{m,n}^{\mathrm{hid}})
=(2M+5)n=(4m+7)n.}
\tag{25}
$$
这对每个固定 $m\ge0$ 和每个正四倍深度 $n$ 都成立。

特别无需选随 $p$ 变化的 $m$，直接取 $m=0$：
$$
G_{16}(y)=\frac14\sigma(2y)^2\Theta(2y),\qquad M=1.
$$
其唯一 Theta 仍是两个原 sigma 带完整二次权的表示。
对同一个固定输入分解，
$$
\boxed{
\mathcal C_{0,n}^{\mathrm{hid}}
=\lambda^{5n}\kappa^{2n}\mathcal C_n,\qquad
v_p(\mathcal C_{0,n}^{\mathrm{hid}})=7n
\quad(n\in4\mathbf Z_{\ge1}).}
\tag{26}
$$
原输出仍在 $Y/X$ 双单位、$W$ 深度至少 $n$、差输出为单位的管内。
R432 的保输出 Hadamard 几何因 $q=2$ 继续准确成立；
那些变换后的 $X_B,Y_C$ 和全部补支仍须共同保留。

R439(37) 还完整给出这条隐藏事件在残余双输出深域内部的补集。
记 $a_{m,n}=\lambda^{(3+2M)n}\kappa^{2Mn}$，在相同的独立
$c$ 单位测试后，该补集的第六矩中央准确是
$$
\boxed{(1-a_{m,n})\mathcal C_n,\qquad
v_p((1-a_{m,n})\mathcal C_n)=5n.}
\tag{26a}
$$
因为 $v_p(a_{m,n})=2Mn>0$，该补集比例为单位。
所以已知隐藏同深块与它在输出深域内的补块分别有
$(2M+5)n$、$5n$ 的准确赋值；后者不能删去。

## 8. 与原中央失败之间保留什么补域

在确定输入表示 (5) 中，$\mathscr D_n$ 是
$\{Y\text{单位}\}$ 的真子域。
令 $\mathcal C_n^{\mathrm{comp}}$ 是其完整补域中同一个
$d\log_p\langle Y\rangle X^6$ 的积分。
由 (8)、(11)，准确有
$$
\boxed{14976b\Omega^6J'_S(0)
=\mathcal C_n+\mathcal C_n^{\mathrm{comp}}.}
\tag{27}
$$
若原中央失败，则补域必须恰为 $-\mathcal C_n$，赋值同为 $5n$。
本篇并未令补域为零；也没有从已知非零子域推出整个左侧非零。
原固定曲线和无穷素数目标仍需排除这份真实抵消。

同样，(25)、(26) 的隐藏事件比完整输出深域细。
只能通过 (24) 的完整推前式比较其积分，不能把原条件中央
对任意 $X$ 测试扩成对任意 sigma、Theta、$\mathcal R$ 隐藏条件的测试。

### 8.1 Q 方向整单位转置必须同时改变两个物理输出

R437 的有限差分原函数满足
$$
\nu_{\mathcal P}=\nu_{\mathcal L}*_Q\nu_{U_{26}},\qquad
U_{26}(0)=1,
$$
其整逆记为 $\iota_U$。本篇证明直接在 $\mathcal L$ 与原 sigma 的
表示 (5) 中进行，没有把这个纯 $Q$ 卷积当成纯 $X$ 操作。

若要把 (11) 写到 $\mathcal P$ 上，定义完整测试
$$
F_n(W,Q)=
\mathbf1_{\{W,Q\in p^n\}}\,
d\int_{c\ {\rm unit}}
 \log_p\left\langle c+\frac{17W+Q}{26}\right\rangle
 \left(-c+\frac{9W-Q}{26}\right)^6d\nu_\sigma(c).
$$
在指示域外取零。原返回准确是
$$
\boxed{
\mathcal C_n
=\int\!\!\int F_n(W,Q+t)\,d\iota_U(t)\,d\nu_{\mathcal P}(W,Q).}
\tag{28}
$$
它同时改变残余第二深度条件为 $Q+t\in p^n$，
把原 $Y$ 移为 $Y+t/26$，把 $X^6$ 改为 $(X-t/26)^6$。
不能省掉任一项或只给第六次测试套一个转置。

完整原第六矩行在 R437 的物理原函数上也仍是
$$
\Omega\int\{\ell(Y+1)(X-1)^6-\ell(Y)X^6\}\,d\mu_{\mathcal P}
=14976b\Omega^6J'_S(0),
$$
其中 $\ell(Y)=\mathbf1_{Y\ {\rm unit}}d\log_p\langle Y\rangle$。
它保两个不同单位边界；不能单独赋两项或 (28) 的子域以零。

## 依赖与新增结论

- [R430：原小核及对任意完整第二输出测试的中央返回](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R437：原 sigma 伴随分离、实际残余来源及有限差分转置](R437-original-sigma-companion-cancellation-and-degree52-primitive.md)。
- [R439：残余真实两态 core 与完整同深比较](R439-original-residual-companion-two-state-core-and-exact-depth-comparison.md)。
- [R432：原平衡 Sigma 隐藏域、Hadamard 三管及其真实补域](R432-original-balanced-two-depth-source-and-three-actual-hadamard-tubes.md)。

本篇支付了完整第六矩中央与原算术中央的单位等价，以及每个偶深
残余域、每个四倍深固定隐藏域的精确非零及赋值。
主要剩余问题已具体化为同一个原测试中的 (27) 及其隐藏输入版本
的补域控制，没有留下负矩单位或移动展开长度的假设。

