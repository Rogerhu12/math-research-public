# R919 — 原中间坐标的多项式环余式构造与完整认证不变性

日期：2026-11-16。**状态：下列精确除法、有限候选构造和原完整认证的充分性已证明；新生产路径尚无实际成功回执。原 RR、端点与 shadow 的未闭要求全部保持。**

本篇接 R910。原 universal 计算仅需要一个线性中间关系，
而 Sage 10.6 的完整子结式接口还继续计算常数项 resultant；
其实现的普通除法也可能把系数送入分式域。
这里逐系数执行可复乘核验的整除，并在中间次数一处停止。
不预报性能，也不凭候选式的形式删除原两条完整关系检查。

## 1. 原对象与已亲读的接口

固定 $\ell=29$ 或 $41$，
$$
C=\mathbf F_\ell[x,v],\quad R=C[Z],\qquad
f=\Phi_{17}(x,Z),\quad g=\Phi_{17}(Z,v).
\tag{1}
$$
这里 $\Phi_{17}$ 仍为原 level3 Hauptmodul 的同一291项整数关系；
不是经典 $j$ 的另一个多项式。两式对 $Z$ 首一、次数18。

Sage 10.6 的原源码为
[src/sage/rings/polynomial/polynomial_element.pyx](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_element.pyx)，
blob 1cb68e8ee359b6eed86f97f9b15240768079a54a。
其 subresultants 函数使用伪余式与 Lazard 的次数降落归一化，
并在中间次数为零时返回全部列表。
本篇只改变实际构造器的环运算与停止位置；当前 R910 运行的
未完成阶段仍须等真实日志，不能据源码猜测该运行究竟停在哪一行。

## 2. 逐系数精确除法及有限构造

对 $A,B\in C[Z]$、$d=\deg A\ge e=\deg B$，
伪除法给
$$
\operatorname{lc}(B)^{d-e+1}A=QB+R_0,\qquad
\deg R_0<e.
\tag{2}
$$
这个身份只用 $C$ 内的加乘。实现同时保实际 Q、$R_0$，
并以(2)全式复乘核验。

若某一步规定将 $R_0=\sum c_jZ^j$ 除以非零 $a\in C$，
本篇不用通常分式除法。对每个系数作 $C$ 中的商余，
要求
$$
c_j=a q_j,\qquad \operatorname{rem}(c_j,a)=0;
\tag{3}
$$
然后返回 $\sum q_jZ^j$，再检查乘 a 恰回整个 $R_0$。
若任一整除失败，该路径失败；不能取有理近似，
也不能将非零余数删掉。接受(3)后所有系数仍在同一个 C 中。

具体初始值为
$$
A=g,\qquad B=\operatorname{prem}(f,-g),\qquad s=1.
$$
若 $B\ne0$，令 $d=\deg A,\ e=\deg B,\ \delta=d-e>0$。
取
$$
C_B=
\begin{cases}
B,&\delta=1,\\
\operatorname{ExactQuotient}
  \bigl(\operatorname{lc}(B)^{\delta-1}B,s^{\delta-1}\bigr),
  &\delta>1,
\end{cases}
\tag{4}
$$
其中 ExactQuotient 就是(3)。
若 $e=1$，保留 $C_B=a(x,v)Z+b(x,v)$ 并停止；
若 $e=0$ 或链提前为零，则不产生 U 证书。
其余情况继续
$$
B_{\rm next}=
\operatorname{ExactQuotient}
\bigl(\operatorname{prem}(A,-B),s^\delta\operatorname{lc}(A)\bigr),
\quad
A_{\rm next}=C_B,\quad s_{\rm next}=\operatorname{lc}(C_B).
\tag{5}
$$
每次接受的非零 $B_{\rm next}$ 次数严格小于 e。
所以非零循环至多18次；没有精度或高度猜测。
本篇不需要计算次数零的 resultant，也不调用 C 的分式域。
每个实际整除和次数变化都在公开日志的证书中记录。

(4)–(5)在分式域上是通常非零余式链的标量归一化；
精确商核验保证本实现没有改变实际多项式。
但在代入原循环曲线后，某些中途标量可能为零。
因此不能仅从这个分式域链，未经下面的检查便断言候选根属于原曲线。
这也是本篇始终保留完整末端认证的原因。

## 3. 原函数域中的唯一接受规则

若线性式的两个系数有共同 $(x-v)^r$ 因子，逐次精确除去，
并复乘核对。原 $T\ne V$ 保这个取消在原函数域中合法。
其它中途标量均不被默认为原曲线上的单位。

然后使用 R910 的同一个原 eta48 域、同一个 $T,V=T/t^{12}$，
以原分母清除和原定义方程约化计算候选
$$
U_{\rm cand}=-b(T,V)/a(T,V).
\tag{6}
$$
实际 $a(T,V)\ne0$ 是接受门；若为零则无证书。
之后必须精确检查
$$
\boxed{
\Phi_{17}(T,U_{\rm cand})=0,\qquad
\Phi_{17}(U_{\rm cand},V)=0
}
\tag{7}
$$
以及原完整非回退、绝对 Tate 支与两个 Atkin 符号。
(7)在原函数域中检查全式，不能替换成某个有限 q 前缀。

**命题。** 只要上述全部原门通过，(6)就是 R882 的同一原 U。

证明：R882 已将当前不可约原分支识别为同一 cyclic $17^2$
结构。它的唯一17阶子群给唯一中间 quotient；原 level3
结构沿这条 quotient 运输。因此在该函数域的泛点，
两条(7)和原绝对支只可能给该 U。
精确整函数域恒等式在泛点成立即为全局有理函数恒等式。
本篇没有换 T、V 或循环支，也没有把逐点选择的另一根拼接为函数。
故接受的 U 恰是原 U。证毕。

这个命题不依赖于(4)中每一个标量的特殊化是否可逆：
它们只用于提出(6)，完整(7)独立认证最终对象。
若候选失败，既不证明原 U 不存在，也不删除原 RR 条件。

## 4. 当前生产路径完整保留的下游门

新的 producer
scripts/produce-r919-original-shadow-rr-tate19-fraction-free.py
与 helper scripts/original_rr_fraction_free_algebra.py
只替换 R910 的 universal 中间关系构造。
原可分特化、q4500/ξ170有界模型恢复、两Atkin、
全部九个商 cusp/36个原 cusp、$D_0,A_u,A_v$、
四个 $27+27+33+33$ RR 块、原 $a_t^m$ 返回和205项全秩均保留。

请求参数仍为 --prime 29 --model tate19 --rr-powers 1 --q-precision 205，
使用原 pinned Sage10.6 容器且仅在本公开仓库 Actions 执行。
这份新路径不取消旧 R910，也不将 R917 的全局 q 格冒作函数域坐标。
尚无本路径的原 U 或完整 RR PASS。

所有可重算系数留在实际运行内，仓库只保源、请求、run与哈希。
依据为原 R882/R910 完整分支及认证证明、上述已亲读的固定 Sage 源码，
以及本篇(2)–(7)的直接代数验证。

## 5. 实际启动回执

[run43922594376](https://github.com/Rogerhu12/math-research-public/actions/runs/43922594376)、
job133493496664，source 45b7e91f3d7dfdcf667999634dd23e669d71acf5，
已进入原数学步骤。该记录只确认真实执行；尚无本路径的
U 恢复、正规化、四块 RR 或完整205行成功回执。
旧 R910 run43913500850仍运行，不能根据未返回的日志替它定位新卡点。


## 6. 同一认证门的几何优先执行次序

scripts/produce-r919-original-shadow-rr-tate19-geometry-first.py
只调整上面的依赖次序。原完整 Tate 方程给同一 $D=k(s)[L]$，
而原 eta48 域、$t,T,V$、两 Atkin 在这两个生成元上的作用、
$u=t-t^{-1}$、$v=T/t^6-729t^6/T$ 和 $a_t$
均已由同一方程得到。这些构造都不使用 U。

原正规化、全部九 cusp、$D_0,A_u,A_v$、branch 及四个 RR 块
仅以 $(D,s,L)$ 为输入；返回同一 eta48 域及原 Tate jets
仅用上述 $u,v,a_t$。因此可以先执行并逐项认证这些几何步骤，
再执行(6)–(7)和 U 的两个原 Atkin 检查。
这是原函数调用的依赖重排，没有删去或放宽任何接受门。

新的执行路径在全部四块/完整205行之后才调用同一个
recover_original_middle；随后仍精确要求
$W(U)=W_3(U)=729/U$，然后才返回含 U 的完整原 context 和末端 result。
若 U 未完成或任一检查失败，该运行不会返回完整前端成功。
先出现的 RR 阶段日志只证明它实际通过的几何步骤，
不能将运行中间状态冒作完整 shadow 输入。

此重排使旧运行尚未完成 U 时，可以独立推进不依赖 U 的
真实正规化与四块 RR 门。它不预报这些步骤的速度或成功，
也不以 R917 的抽象全局基替换这里的函数域基。
所有原参数、固定容器、可分检查、完整 cusp/Atkin/绝对支及输出规则保持。
