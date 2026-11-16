# R910 — 原 RR 的可分特化证书与唯一中间坐标的线性子结式恢复

日期：2026-11-16。**状态：以下替代证书的正确性和同原对象返回已证明；公开任务尚未取得新 RR PASS。运行快慢不作预报，主目标仍未完成。**

原 306 与 eta48 任务的完整结束日志见 [实际停止点](../notes/2026-11-16-original-rr-stopped-before-normalization.md)。前者停在 $\mathbf F_{29}(T)$ 上的次数 306 可分性 gcd，后者停在 eta48 函数域上的中间 $U$ gcd。这里只替换这些精确代数操作；不减少 R882 的全空间、端点、尖点或实际返回门。

本次实际请求针对 R882(C,E) 的 genus19 四块前端。完整原次数 24 方程仍由 $q^{4500}$、170 项局部迹和全局分子 153/分母 8 的界恢复；随后返回同一个 eta48 次数 48 函数域。

## 1. 保持次数的一个特化即认证原可分性

设 $k$ 为有限域、$K=k(t)$，$P(X)\in K[X]$ 次数为 $d$，$P'(X)$ 次数为 $e\ge0$。取有限扩张 $k'/k$ 及 $\tau\in k'$，要求：

1. $P$ 的每个系数在 $t=\tau$ 正则；
2. 特化后的 $P_\tau$ 与 $P_\tau'$ 仍分别为次数 $d,e$；
3. $\gcd(P_\tau,P_\tau')=1$。

则
$$
\boxed{\gcd(P,P')=1\quad\text{于 }K[X].}
\tag{1}
$$

**证明。** 令 $A=k[t,1/D]$，其中 $D$ 是所有系数分母之积；$\tau$ 满足 $D(\tau)\ne0$。相同次数的 Sylvester 矩阵在 $A$ 上定义，矩阵取行列式与 $t\mapsto\tau$ 相容。第三项给
$$
\operatorname{Res}_X(P,P')(\tau)
=\operatorname{Res}_X(P_\tau,P_\tau')\ne0.
$$
因此原 resultant 在 $K$ 中非零，等价于 (1)。所有分母和两个次数都已保留，不是把单点值当泛型证明。证毕。

实现依次在扩张次数 1、2、3 内尝试至多 256 个确定点，逐个检查三项。只要取得一个证书即可停止。若有界搜索未找到，则报未取得证书，不称多项式不可分；也不声称这个特化证明不可约性。原模型的几何不可约性和函数域识别仍来自 R882。

实际用于 genus19 方程、Fricke 次数 24 方程及原 eta48 次数 48 方程。原系数、次数和模型均不变。有限域特化只认证原 resultant 非零，后面的运算仍在原 $k(t)$ 和原函数域进行。

## 2. 原两条关系的线性子结式

保持原 $T_3=(\eta/\eta_3)^{12}$ 和整数 $\Phi_{17}$，设
$$
A=k[x,v],\qquad
f(Z)=\Phi_{17}(x,Z),\qquad
g(Z)=\Phi_{17}(Z,v).
\tag{2}
$$
二者在 $Z$ 中都是首一次数 18。对 (2) 在多项式系数环上求子结式序列，取实际非零的线性项
$$
S(x,Z,v)=a(x,v)Z+b(x,v).
\tag{3}
$$
这里不先进入原次数 48 扩张后逐次求逆。算法是否在时限内完成由实际执行决定。

子结式的行列式定义给
$$
S\in (f,g)\subset A[Z].
\tag{4}
$$
具体地，子结式矩阵最后一列由若干 $Z^i f$、$Z^j g$ 组成，沿该列展开即得到 (4)。这也说明任意系数特化与该多项式恒等式相容，不依赖除法步骤中的特殊首项仍非零。

实现可先准确除去 (3) 的公共对角幂 $(x-v)^r$。每次都检查多项式商余数为零，并最后检查
$$
S=(x-v)^r S_{\rm red}.
\tag{5}
$$
不假定 $r$ 的值，不除未认证的其它因子。

## 3. 同一原域内的存在、唯一性和分支

令 $B$ 是 R882 已识别的原 eta48 函数域，保原坐标 $T,V$。将 (5) 在 $(x,v)=(T,V)$ 特化；必须准确检查 $T\ne V$。故 $(T-V)^r$ 是域中的单位，特化后的 $S_{\rm red}$ 仍属于两条原关系生成的理想。

设实际线性首系数非零，即
$$
S_{\rm red}(T,Z,V)=a_B Z+b_B,\qquad a_B\ne0.
\tag{6}
$$
则任何两条原关系的公共根都只能是
$$
\boxed{U=-b_B/a_B.}
\tag{7}
$$
实现还在完整原函数域中逐字检查
$$
\Phi_{17}(T,U)=0,\qquad
\Phi_{17}(U,V)=0,\qquad U\ne T,V.
\tag{8}
$$
因此 (7) 确实存在且唯一，不是用近似展开猜一个根。

**同原对象的识别。** 原循环 $17^2$ 同源核有唯一阶 17 子群，所以原 $T,V$ 的两步循环链具有原中间坐标。式 (4)–(8) 说明恢复的正是它。原 $T,V$ 已由 R882 完整 Tate/全局系数界固定，故没有改选另一根、另一尖点或相邻但不同的 Hecke 对应。后续继续检查原两 Atkin 对合及全部绝对符号，包括
$$
W(U)=729/U,\qquad W_3(U)=729/U.
$$
不以已证 $F$ 映射或某个形式局部支代替这些条件。

若没有线性子结式、首系数特化为零、完整 (8) 失败，程序立即停止且不输出 RR PASS。这些失败不否定原映射或原 RR 空间的存在。

## 4. 保原 eta 坐标的整分母求值

在当前原模型有 $V=T/t^{12}$。对任意 $P(x,v)=\sum c_{ij}x^iv^j$，令 $d_v=\deg_vP$，则
$$
\widetilde P(X)=
\sum c_{ij}t^{12(d_v-j)}X^{i+j}
\in k[t][X],
\qquad
P(T,V)=t^{-12d_v}\widetilde P(T).
\tag{9}
$$
所有指数非负。将 $\widetilde P$ 对同一个原首一定义多项式取余后，仍代表同一域元素。

分别对 (6) 的多项式首项和常数项应用 (9)，记结果为
$\widetilde a,\widetilde b$、对应右次数为 $d_a,d_b$。则
$$
\boxed{
U=-\frac{\widetilde b(T)}{\widetilde a(T)}
t^{12(d_a-d_b)}.
}
\tag{10}
$$
实现准确检查 $\widetilde a(T)\ne0$。这是一次原函数域求逆；前面的多项式运算及基域有理函数运算仍是精确运算，不声称整个算法没有其它除法。

(9)–(10) 只是原坐标的代数重排。没有改 eta 单位、没有丢可能出现的负幂，也没有把原 degree48 坐标换成 quotient 上的自由根。

## 5. 完整 RR 认证保持

新 producer 保持原 genus19 方程的全部输入与唯一性证明，也保持：

- 真有限和无限极大整环、全部 9 个 quotient 尖点及 36 个原尖点的返回；
- $A_u,A_v$、分支除子、$D_0$，以及所有极点与负 floor；
- $m=1$ 的四块维数 $27+27+33+33=120$；
- 两 Atkin 的绝对号、完整函数域嵌入和 $a_t=-T/(24t\,dT/dt)$；
- 用 $a_t^m$ 返回原 $D_S$、全部 205 项 Tate 行和完整 Sturm 秩；
- 原 $T,U,V$ 的上下文，供后续同一消费者使用。

只有这些原完整门全部通过才输出原 RR 结果。线性子结式成功或一个可分特化成功均不是 RR PASS。两个原特征零映射仍按各自证书；R909 已付 $F$，$P$ 和完整 shadow 尚未由本篇支付。

因为通用子结式序列会包含零次子结式，本篇将记录 high_degree_resultant_computed 为真；不继续沿用旧直接 Tate producer 的“没有计算高次 resultant”标记。没有因式分解循环次数 306 方程来选新支。

## 6. 实现、参数、来源与执行范围

- helper：[original_rr_subresultant_algebra.py](../scripts/original_rr_subresultant_algebra.py)；
- producer：[produce-r910-original-shadow-rr-tate19-subresultant.py](../scripts/produce-r910-original-shadow-rr-tate19-subresultant.py)；
- request：[original-shadow-rr-r910-request.json](../ci/original-shadow-rr-r910-request.json)；
- workflow：.github/workflows/rank2-sha-original-shadow-rr-r910.yml；
- 参数：prime29、原 tate19、rr-powers1、q-precision205；
- 固定镜像：sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。

Sage Development Team，SageMath 10.6，src/sage/rings/polynomial/multi_polynomial.pyx，blob 792161352b0c2c40323cddde1b186bda431122fc，subresultants 方法；已按有限行读取源代码。它将指定变量转成一元多项式并返回同环的非零子结式，不依赖默认变量。参见 [固定版本源代码](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/multi_polynomial.pyx)及[官方一元子结式接口](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_element.html#sage.rings.polynomial.polynomial_element.Polynomial.subresultants)。本篇所用正确性已由上面恒等式和完整原残差给出，接口说明不代替实际通过记录。

所有数学执行仅在本公开仓库 Actions；具名容器退出时强制清理，最长 21000 秒后终止容器，不保存可重算输出、系数或 Release。最终仅登记实际 run/job/source、脚本依赖和结果 SHA-256。本文发布时尚无新执行结果；完成算法证明后立即请求执行，继续其它原未闭门。


## 7. 首次实际执行与确定的接口修复

首 run43912835484/job133459031944/source d622da0c720cef993a131ad47fc3214e08f771bc 于 16:57:02 UTC 失败。原整数 Phi17 已完整生成，hash 与旧两任务一致。实际异常为 RecursionError: maximum recursion depth exceeded during compilation，35.526014552 秒，最后记录 max_rss_kib=1055724。

完整调用栈落在 Sage 10.6 multi_polynomial.pyx 的子结式返回转换：它对一元子结式列表逐项调用原多元环构造器，后者经通用转换进入大表达式编译。没有线性子结式结果哈希，也没有 RR PASS。此失败与代数条件不成立不同。

修复直接建立 $k[x,v][Z]$ 的 19 个系数向量，对一元多项式调用同一 subresultants 算法；仅取线性项的两个 $k[x,v]$ 系数，按各自系数字典求值和记录哈希。对角幂的两个精确商余数与重乘身份均保留。这样避开整条大列表回转多元环的表达式编译；数学输入、子结式、(5)–(10) 及所有后续门不变。修复推送后重新请求原完整执行，不将首 run 记为算法或 RR 证书完成。
