# R681 — 原完整规范的首挠点代数值与全部共振余数的有限返回

日期：2026-11-15。**状态：已证明。**

本篇将 R676 的原 CM 分子用于 R639 的同一个完整整规范 T_g。
在每个原非零 p 挠点，T_g 的值满足一个明确的代数幂方程；
原 u 参数中截至 p+1 次的有限 jet 唯一选定正确根。
所以这里没有把一个未支付收敛的 sigma 指数在边界上直接求值。

同一公式还给这些点上全部正阶 jet 的代数性。
结合 R663 的实际 LT 坐标，原所有 Q^ell 共振余数都能由有限代数数据
及 Hermite 插值准确恢复。R663 余数中的无限高尾因此完整计入，
不是用一个有限截断替代原余数。

本篇尚未证明这些实际余数非零或由原 j=0 被迫为零；
它把这一剩余条件变成可精确指定的有限代数关系。

## 1. 同一个原对象及实际挠点

保持
\[
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad e=p-1,\quad b=17,
\]
以及原
\[
u=x^{-1/2},\quad t=bu^6,\quad z=uH(t),\quad
\Theta=x\sigma^2,\quad \mathscr L(t)=\log\Theta(t).
\]
固定 \(\overline{\mathbf Q}\hookrightarrow\mathbf C_p\)。
所有以下代数值均使用这同一嵌入和原形式群参数。

R676 的实际全局 CM 整数和分子为
\[
\alpha=\omega(p+\omega),\qquad
\nu=p^2-p+1,\qquad
\Theta(f_\alpha(t))=B_\alpha(t)\Theta(t)^\nu,
\tag{1}
\]
其中 \(B_\alpha\in1+t\mathcal O[t]\) 是原 monic numerator 的反转，
系数在 \(\mathbf Q(\omega)\)，且 \(f_\alpha\in\mathbf Q(\omega)(t)\)。
这里不将它们换成模 p 模型。

R639 的完整原规范是
\[
h=\sigma/z,\quad F=\log h,\quad
F_{\rm c}(z^d)=\frac1d\sum_{\zeta^d=1}F(\zeta z),
\]
\[
P_\zeta(u)=\frac{h(\zeta z(u))}{h(z(u))}
\in1+u^2\mathcal O[[u]],\qquad
\boxed{T_g(u)=\left(\prod_{\zeta^d=1}P_\zeta(u)\right)^{1/d}.}
\tag{2}
\]
常数一的根沿原整级数取；\(T_g^{\pm1}\in1+u^2\mathcal O[[u]]\)，
且 \(E_{\rm c}=hT_g\)。所有原高阶中央项均在 (2) 中。

取原 \(T\in E[p]\setminus0\)，记 \(u_T=u(T)\)、\(t_T=bu_T^6\)。
R663 给
\[
v_p(u_T)=1/(q-1).
\tag{3}
\]
对 \(\zeta\in\mu_d\)，令 \(T_\zeta=[\zeta]_E T\)，
\(u_\zeta=u(T_\zeta)\)、\(t_\zeta=bu_\zeta^6\)。

这里的 \([\zeta]_E\) 是原完整局部 CM 作用，不被声称为全局椭圆同态。
但在 E[p] 上，选任意 \(a_\zeta\in\mathbf Z[\omega]\)
使 \(a_\zeta\equiv\zeta\pmod{p\mathcal O}\)，就准确有
\[
\boxed{T_\zeta=[a_\zeta]T.}
\tag{4}
\]
因为二者之差被 p 整除，确实杀掉 T。
所以所有 \(T_\zeta,u_\zeta,t_\zeta,\zeta\) 都是代数数。
u 的平方根选原形式参数的分支，不随点任意改号。

## 2. 原整比值的边界 log 身份

令 \(u_\zeta(u)=u([\zeta]_EP(u))\) 为原整形式作用。
它与 [-1] 交换，故是奇级数，且线性项为 ζ。因此
\[
R_\zeta(u):=\frac{u_\zeta(u)}{\zeta u}\in1+u^2\mathcal O[[u]].
\tag{5}
\]
在原正式级数中，由 (2) 直接得到
\[
\boxed{
2\log P_\zeta(u)
=\mathscr L(bu_\zeta(u)^6)-\mathscr L(bu^6)
 +2\log R_\zeta(u).
}
\tag{6}
\]
这等价于把 \(\sigma(\zeta z)/(\zeta\sigma(z))\) 的完整 u 尺度保留。
没有分别取在边界为零的 H 的 log。

R676 已证明 \(\mathscr L\) 在整个 \(|t|<1\) 解析。
(2)、(5) 的 log 也在开 u 单位盘解析，原 CM 作用保持该盘。
所以 (6) 从正式身份延到整个开盘，尤其可在 (3) 评价。

(1) 的原同态在 E[p] 上为 \([\omega^2]\)，故其六次参数固定每个 \(t_\zeta\)。
R676 的准确式为
\[
\boxed{
\mathscr L(t_\zeta)
=-\frac{\log B_\alpha(t_\zeta)}{\nu-1},\qquad
\nu-1=p(p-1).
}
\tag{7}
\]
这里只对实际代数单位取 p 进 log，不指数化 \(\mathscr L\)。

将 (7) 代 (6)，定义明确代数数
\[
\boxed{
A_{\zeta,T}
=\frac{B_\alpha(t_T)}{B_\alpha(t_\zeta)}
 \left(\frac{u_\zeta}{\zeta u_T}\right)^{2(\nu-1)}.
}
\tag{8}
\]
所有分母非零，且 \(A_{\zeta,T}\) 是 1 邻域的单位。
准确有
\[
\boxed{
2(\nu-1)\log P_\zeta(u_T)=\log A_{\zeta,T}.
}
\tag{9}
\]
不能从 (9) 直接删掉可能的 p 幂单位根。下一节完整支付这一点。

## 3. 显式幂方程，不遗漏单位根

由 (3)、(5) 和 \(B_\alpha\in1+t\mathcal O[t]\)，
\[
v_p(P_\zeta(u_T)-1)\ge\frac2{q-1},\qquad
v_p(A_{\zeta,T}-1)\ge\frac2{q-1}.
\tag{10}
\]
若 \(v_p(a-1)\ge2/(q-1)\)，二项式逐项给
\[
v_p(a^p-1)\ge
\min\left(1+\frac2{q-1},\frac{2p}{q-1}\right)
=\frac{2p}{q-1}>\frac1{p-1}.
\tag{11}
\]
在 \(v_p(a-1)>1/(p-1)\) 的盘，log 与通常收敛 exp 互逆。
这是阶乘估值 \(v_p(n!)\le n/(p-1)\) 及正式逆身份的直接结果；
故 log 在这个盘单射。

将 (9) 乘 p，再用 (10)–(11)，两边所对应的单位均在该单射盘。
因此得到真正的代数身份
\[
\boxed{
P_\zeta(u_T)^{\,2p(\nu-1)}=A_{\zeta,T}^{\,p}.
}
\tag{12}
\]
这里额外的 p 正是支付 log 核，未用任意的根选择冒原比值。

置
\[
\boxed{
A_T=\prod_{\zeta^d=1}A_{\zeta,T}
=\frac{B_\alpha(t_T)^d}{\prod_{\zeta^d=1}B_\alpha(t_\zeta)}
 \left(\prod_{\zeta^d=1}\frac{u_\zeta}{\zeta u_T}\right)^{2(\nu-1)}.
}
\tag{13}
\]
由原完整 (2)，
\[
\boxed{
T_g(u_T)^{M_p}=A_T^p,\qquad
M_p=2dp(\nu-1)=2(p+1)p^2(p-1).
}
\tag{14}
\]

**定理 1。** 原完整 \(T_g(u_T)\) 及所有 \(P_\zeta(u_T)\)
均为代数数。式 (12)、(14) 是其明确有限幂方程；
系数只涉及原 CM numerator 和原 p 挠坐标及单位根。

并不声称这些值落在未扩张的全局 p 除点域，
也不声称任何候选代数根都等于原值。

## 4. 一个有限原 jet 唯一确定正确分支

令
\[
\tau_d(U)=\sum_{n=0}^{d}[U^n]T_g(U)\,U^n.
\tag{15}
\]
这些有限系数是原正式 \(T_g=\exp(F_{\rm c}-F)\) 与原 z(u)
的系数组合，均为代数数；事实上在本原 b 模型中为有理数。
R639 的完整整性保证它们在当前 p 处整。

因为 (2) 的所有余系数整，(3) 给
\[
\boxed{
v_p\bigl(T_g(u_T)-\tau_d(u_T)\bigr)
\ge\frac{d+1}{q-1}>\frac1{p-1}.
}
\tag{16}
\]
\(M_p\) 的 p 部分准确为 p²。
两个不同的 (14) 根之比属于 \(\mu_{M_p}\)。
其中非平凡单位根与 1 的距离，最大可能估值为 \(1/(p-1)\)：
prime-to-p 非平凡根给估值零，p 或 p² 阶根分别给
\(1/(p-1)\)、\(1/(p(p-1))\)。

所以：

**定理 2。** (14) 在以下条件下有且只有一个根：
\[
\boxed{
v_p\bigl(X-\tau_d(u_T)\bigr)>1/(p-1).
}
\tag{17}
\]
它准确为原 \(T_g(u_T)\)。

存在性由 (16) 给出；唯一性由不同根的距离界给出。
这是用原截至 p+1 次的有限数据选择原分支。
它完整处理 p 幂单位根，不要求读一个无限尾或猜测 complex 分支。

若需从原 F 明确生成 (15)，只需使用
\(F_{\rm c}(z^d)=F_s z^d+O(z^{2d})\)，再作原 u/z 的有限组合。
必须先作完整差及指数，不能分别删掉其中可能有 p 分母的项。

## 5. 同一原 log 来源的全部正阶边界 jet

本节证明得到的并非只有零阶值。

原 \(f_\alpha\) 是 t 的有理函数，且在每个 \(t_T\) 正规。
因为 \([\alpha]T=[\omega^2]T\)，原不变微分给
\[
u_\alpha(u_T)=\omega^2u_T,\qquad
u_\alpha'(u_T)=\alpha\,C(t_T)/C(t_T)=\alpha.
\]
因此
\[
\boxed{
f_\alpha'(t_T)=\omega\alpha
=\gamma:=1+p\omega^2.
}
\tag{18}
\]
这里不能把边界的导数误写成原点导数 \(\alpha^6\)。

对每个正整数 k，
\[
\boxed{
\nu-\gamma^k
=p\epsilon_{k,p},\qquad
\epsilon_{k,p}\equiv-1-k\omega^2\pmod p
\in\mathcal O^\times.
}
\tag{19}
\]
同 R676 的惰性论证，\(\omega^2\notin\mathbf F_p\) 支付所有 k，
包括 k 被 p 整除的情形。

将原完整
\[
\mathscr L(f_\alpha(t))-\nu\mathscr L(t)=\log B_\alpha(t)
\tag{20}
\]
在 \(t_T\) 求 k 阶导数。
Faà di Bruno 式的最高项是 \(\gamma^k\mathscr L^{(k)}(t_T)\)，
其余项只涉及 \(1\le j<k\) 的导数；
不会涉及 \(\mathscr L(t_T)\) 本身。
故 (19) 给一个没有零分母的三角递推。
右边 log 的正阶导数是 \(B_\alpha\) 及其导数的有理式，均为代数数。

例如
\[
\boxed{
\mathscr L'(t_T)
=-\frac{(B_\alpha'/B_\alpha)(t_T)}{p(p+\omega)}.
}
\tag{21}
\]
由归纳：

**定理 3。** 对每个 \(k\ge1\)，
\(\mathscr L^{(k)}(t_T)\) 都是由 (18)–(20) 有限计算出的代数数。

零阶仍是 (7) 的代数数 log，本文没有将它混称为代数数。

## 6. 完整 T_g 和所有 CM 运输的正阶 jet

原 \([\zeta]\) 的全部有限 jet 在 \(u_T\) 也为代数。
虽然 \([\zeta]\) 不必是全局同态，它满足原微分身份
\[
\boxed{
u_\zeta'(u)=\zeta\,\frac{C(bu^6)}{C(bu_\zeta(u)^6)}.
}
\tag{22}
\]
右边是指定分支的代数函数，在这些点没有零分母。
初值 \(u_\zeta(u_T)=u_\zeta\) 已由 (4) 为代数，
故反复微分 (22) 给全部有限 jet 的代数性。

对 (6) 求正阶导数，使用定理3和 (22)，得
\[
(\log P_\zeta)^{(k)}(u_T)\in\overline{\mathbf Q},
\qquad k\ge1.
\]
再对 (2) 作 log 微分，得到
\[
(\log T_g)^{(k)}(u_T)\in\overline{\mathbf Q},\qquad k\ge1.
\tag{23}
\]
配合已确定的非零代数初值 (14)、(17)，Bell 多项式给
\[
\boxed{
T_g^{(k)}(u_T),\quad P_\zeta^{(k)}(u_T)
\in\overline{\mathbf Q}\qquad(k\ge0).
}
\tag{24}
\]
每个指定阶数都只需有限次上述代数运算。
这里保同一个原完整 T_g，而非挑一个满足低阶同余的单位。

## 7. 原 LT 坐标在全部首挠点的有限代数 jet

沿用 R663 的唯一整坐标
\[
v=h_{\rm LT}(u),\qquad
h_{\rm LT}([-p]_E(u))=-p\,h_{\rm LT}(u)+h_{\rm LT}(u)^q.
\tag{25}
\]
记右边多项式为 \(g_{\rm LT}(v)=-pv+v^q\)。
在非零 p 挠点，
\[
\boxed{v_T^{q-1}=p,\qquad v_T/u_T\in1+\mathfrak m.}
\tag{26}
\]
根的 prime-to-p 单位比彼此有单位距离，所以 (26) 唯一指定这个代数 \(v_T\)。

原 \([-p]\) 在 u 中是一个指定分支的代数函数 f，
而 \(h_{\rm LT}\) 在零点的每个固定系数由 R663 的递推有限给出，
均为代数数。
对 (25) 在 \(u_T\) 求导，f(u_T)=0，且
\[
g_{\rm LT}'(v_T)=p(q-1)\ne0.
\]
所以逐阶链式法则把
\(h_{\rm LT}^{(k)}(u_T)\) 表成较低阶和原点有限系数的代数式。
特别
\[
\boxed{h_{\rm LT}'(u_T)=-C(t_T)/(q-1)\ne0.}
\tag{27}
\]
故原逆 \(u(v)\) 在这些点的全部 有限 jet 也为代数。
再令 \(W=v^d\)，其导数 \(dv/dW=(d v^{d-1})^{-1}\) 非零，
所有 W 换参的有限 jet 同样准确代数。

这里只在这些已存在的非零点作局部换参；
没有假设 z 在首边界可逆。

## 8. R663 全部原共振余数的有限代数返回

对原 \(m=34,72\)，保
\[
A_m=\sigma^m\phi_m(x,y),\qquad
F_m(u)=T_g(u)^{-m}\phi_m(x(u),y(u)).
\]
原完整范数一投影仍是
\[
\Phi_m(u(v))
=\frac1d\sum_{\zeta^d=1}\zeta^mF_m(u(\zeta v))
=v^{d-m}\mathcal B_m(W),\qquad W=v^d .
\tag{28}
\]
没有删除任何原多项式项、CM 支或 T_g 高尾。

在每个首挠点，(4)、(24)、(27) 及原 \(\phi_m\) 的代数性给
(28) 全部有限阶 jet。
所以对 \(Q(W)=W^e-p\) 的每个根 ξ，
\[
\boxed{
\mathcal B_m^{(j)}(\xi)\in\overline{\mathbf Q}
\quad\text{对全部 }j\ge0.
}
\tag{29}
\]
其值可用 (28) 和前述有限代数递推准确计算。
\(e=p-1\) 个 ξ 分别对应原全部 \(\mu_d\) 轨道，没有只取一个代表族。

对任意正整数 ell，原 Q^ell 余数具有唯一形式
\[
R_{m,\ell}(W)
=\sum_{i=0}^{e-1}\sum_{j=0}^{\ell-1}
 \mathfrak r_{m,i,j}\,W^iQ(W)^j,\qquad \deg R_{m,\ell}<e\ell .
\tag{30}
\]
它由全部 ξ 上的条件
\[
R_{m,\ell}^{(j)}(\xi)=\mathcal B_m^{(j)}(\xi),
\qquad0\le j<\ell
\tag{31}
\]
唯一决定，因为 Q 的根互异，Hermite 矩阵可逆。
(29)–(31) 因此给所有系数的代数性和有限恢复。

R663 已付这些系数恰为原完整无限尾
\[
\boxed{
\mathfrak r_{m,i,j}
=\sum_{k\ge j}\binom{k}{j}p^{k-j}b_{m,i+ek},
\qquad \mathcal B_m(W)=\sum b_{m,n}W^n .
}
\tag{32}
\]
(31) 和 (32) 是同一余数的两种准确表示。
没有以截断 (32) 冒其原值。

**定理 4。** 对固定 p、m 及 ell，原全部
\(\mathfrak r_{m,i,j}\) 为带指定 p 进嵌入的代数数，
由原 p 挠点、原 CM numerator、原截至 d 次规范 jet，
以及有限阶代数微分/Hermite 插值准确确定。
因此
\[
Q^\ell\mid\mathcal B_m
\iff R_{m,\ell}=0
\tag{33}
\]
成为一个完整的有限代数零判定，不需要猜测无限高尾是否相消。

## 9. 原中央接口仍缺哪一步

R663 的同一个 Y 闭盘充要条件仍是 Q|B_m；
R660 的原 X 下降仍要求更高 \(Q^{d-m}\) 及原 j=0。
本篇没有将 (33) 认作中央零，也没有证明其恒成立或恒不成立。

新得到的是：原完整规范在首挠点的精确值、正确根的有限选择、
全部边界 jet，以及全部共振余数的有限代数呈示。
其中 p、T_g、CM 投影和分子仍依 p，
不能据“代数”二字把它们添加到固定全局来源格而免除成本。

下一步须利用这些**实际选定**代数关系，
控制原两条余数系统或把原 j=0 接到它们；
任意更换幂方程的根、删除 (17) 的分支条件或仅检查首个模 p 系数都不够。
固定曲线无穷不同 p 的完整初级有限主目标仍未完成。

## 依赖

- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：
  同一个完整 P_ζ、T_g、范数一投影和整单位性。
- [R676](R676-original-unit-cm-numerator-and-three-digit-lift.md)：
  原 CM numerator、开单位盘 log 身份及首挠点代数数 log。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原严格 LT 坐标、全部轨道、完整 Q^ell 余数及同解闭边界。
- [R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)：
  原 X 下降的更强必要条件。

本篇为原同态、解析 log 的单射盘和有限代数插值的完整证明；
不调用新预印本，不新增素数扫描或未执行的数值证书。
