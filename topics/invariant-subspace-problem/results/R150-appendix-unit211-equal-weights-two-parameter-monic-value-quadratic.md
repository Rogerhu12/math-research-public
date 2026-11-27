# R150：等权原图的两参数首一值二次式与完整首项单位来源

**已证明。** 原一般 LS 等权图在已闭的 y=1、y=1/2 和原权一次式首项零分支之外，可用两个参数及同一个首一二次值变量描述两条剩余均值条件。二次首项的非零有完整原理想单位身份，未丢任何首项零纤维。其余 N/P、原值矩和物理非零条件仍须继续；一般等权图和普通 Hilbert ISP 均未完成。

会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）；AI-assisted GPT-6 Astra Pro。

## 1. 全部逆从已经关闭的原分支而来

沿用[准确原均值图和首项排除](R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md)及[半均值排除](R150-appendix-unit211-equal-weights-half-singleton-mean-exclusion.md)。仍写
$$
m=b+c=u,\quad d=1-Q,\quad v=2y-1,\quad
x=m+(y-1)z.
$$
原 EBo 给
$$
t=2(1-z)+[2(z-d)y-Q]/m.
$$
原 E1−mEBe 给
$$
(m-1)A_m+z(dv^2-1)=0,\qquad A_m=(d+z^2)v-2z.
$$
已经完整支付 v、z、v−1、A_m、dv²−1 非零，连同原 m、m−1、Q、d、P02 非零。

取新参数
$$
\kappa=dv^2,\qquad \omega=zv,\qquad
A=\kappa+\omega^2-2\omega.
\tag{1}
$$
它们不是原 singleton U 值 k 或原 w_U=lambda−1−T；源码中短名 k、w 分别表示本稿 kappa、omega。准确原恢复为
$$
d=\kappa/v^2,\quad Q=1-\kappa/v^2,\quad
z=\omega/v,\quad y=(v+1)/2,
$$
$$
m=\frac{(\omega-1)(\omega-\kappa)}{A},\qquad
m-1=\frac{\omega(1-\kappa)}A.
\tag{2}
$$
这里 A=vA_m 已付非零；(2) 直接来自原均值差，没有追加任意权关系。

原条件继续保证
$$
v\omega\kappa(\omega-1)(\omega-\kappa)(\kappa-1)A
(v-1)(v^2-\kappa)\ne0.
\tag{3}
$$
P02 的剩余因子也保留：
$$
[(2m-1)v^2-3\kappa]\ne0.
\tag{4}
$$
不能由 v−1 非零进一步删掉 v+1=0。

## 2. 两条原均值的同一个二次返回

将 (2) 和前述原 x,t,f 返回完整 Gram。实际有
$$
\mathcal E:=A^2v^2E_1=A^2v^2(mE_{Be})
=\alpha(\kappa,\omega)v^2+\beta(\kappa,\omega).
\tag{5}
$$
附源从原均值逐项重建两边；不是只证明它们在某个抽象共根处相等。原 EBo 和 E0 已由准确图恢复恒为零。

定义
$$
R=\kappa^2+(\omega-1)^2\kappa-\omega^2,
$$
$$
B=\omega^4-2\omega^3+4\omega^2-2\omega+1,\qquad
C=\omega^2(\omega^2+1),
$$
$$
L=\kappa B-C,\qquad
q_*=\kappa^2+(\omega^2-5\omega)\kappa+3\omega^3+4\omega.
$$
(5) 的两个实际系数准确为
$$
2\alpha=(\omega-1)AR,\qquad
2\beta=q_*R-4\omega L.
\tag{6}
$$
展开后的 (5) 在 (kappa,omega,v) 中有26项，次数(4,5,2)，只有 v 的0、2次项。两个原均值返回是同一多项式。

## 3. 首项零分支的完整原单位恒等式

本节不给 B 或 L 预加非零假设。令
$$
J_*=\kappa B+C+(\omega-1)^2B,\qquad
U=\omega^4(\omega-1)^4.
$$
直接多项式展开给
$$
B^2R+U=LJ_*.
\tag{7}
$$
一种短推导是先用
$$
B=(\omega^2+1)(\omega-1)^2+2\omega^2
$$
算出
$$
C^2+(\omega-1)^2CB-\omega^2B^2=-U,
$$
再把左边与 B²R 相减。没有除 B。

由 (6)—(7)，并用 (5) 中 beta=Ecal−alpha v²，得到完整原身份
$$
\boxed{
\left[q_*J_*-4\omega B^2+
 J_*(\omega-1)Av^2\right]R
-2J_*\mathcal E
=4\omega^5(\omega-1)^4.
}
\tag{8}
$$
附源实际计算了 (7)、(8) 的每个乘积及和，全部逐项相等。右端由 (3) 已是单位。因此 R 在两原 mean 商中的逆具有准确原来源；特别任何原点都不可能使 R=0。

这比只在一般 R 非零图上继续消元更强：整个 R 零支已在同一个原理想中用单位组合排除，首项没有被先行删除。由 (6) 和 (3)，alpha 也成为已付单位。

## 4. 同一个首一值二次式及真正剩余条件

因此原两条剩余均值恰由
$$
v^2=-\beta/\alpha
\tag{9}
$$
表示，原恢复式 (1)—(2) 仍双向，且全部 (3)—(4) 和原 LS/值矩条件保留。因为 v≠0，beta 在原点上也非零。

若后续把原 N_H、N_S、P_S 用 (9) 返回，只能在同一个 v 上取余；每个余式可以一次，但不能让不同方程各选二次式的一条不同根。v−1 非零已经支付，而 v+1=0 仍可能，需要原返回后单独处理。P02、原 D_val、相同 f 和两 singleton 复嵌入亦不能丢弃。

本条还实际重建了原 N1 在新图中的必要多项式：仅剥已付 v² 后，其次数为(5,6,6)、62项；这是后继同 v 取余的原输入，不是本条新增的排空结论。

## 5. 实际执行源和准确范围

- [2026-11-27-unit211-equal-weight-three-parameter-original-chart-8542.js](../notes/2026-11-27-unit211-equal-weight-three-parameter-original-chart-8542.js)，SHA-256：183a3e4fd4f65d1a9e550fae35b606fb5b24384c7be495fa522e551e24aef9f3。
- [2026-11-27-unit211-equal-weight-monic-value-original-unit-8542.js](../notes/2026-11-27-unit211-equal-weight-monic-value-original-unit-8542.js)，SHA-256：338c51aee6eb49c64905b833f6a141e4ec06f2ba3856748b01513083c0dd0ee6。

第一份是新参数图的实际函数体，输入为已提交 regular-original-chart 的原返回对象。完整原 E1/mEBe/N1 重建及仅剥已付因子的检查实际0.110秒。第二份以第一份的 E1 返回行为唯一输入，准确构造 alpha、beta、(6)—(8)，实际0.005秒。二者均在纯 V8 BigInt 有理算术中正常完成，不读取外部数据；OS退出码和RSS没有由执行接口暴露。

[小执行回执](../notes/2026-11-27-unit211-equal-weight-monic-value-execution-8542.json)记录实际函数体 SHA、规范输出 SHA、原乘回与有限作用域；可重算的长系数数组不入库。没有等待额外整体复跑作为数学登记门槛。

下一数学输入是同一个 (9) 上的完整原 N/P 一次余式、所有新首项零面及原值矩返回，不是重做已经关闭的旧大门。
