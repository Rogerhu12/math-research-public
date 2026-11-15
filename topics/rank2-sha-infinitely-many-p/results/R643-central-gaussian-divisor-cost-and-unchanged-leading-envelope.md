# R643 — 原中央行的 Gaussian 正成本仅占次主量

日期：2026-11-15。**状态：已证明。**

R639 支付了原完整中央解的整个形式群内盘，但没有改变原全格的
每一个混合来源行。本篇精确计算：在 R583 的原 Gaussian 正包络中，
仅保留满足原中央条件 \(s=(p+1)/6\mid k\) 的那些素位，
总量只有 \(O(k(1+\log\log(k+3))^2)=o(k\log k)\)。
任意固定有限个仿射余类条件也有同一结论。

所以只从既有正包络中删去这些稀疏中央行，并不改变其
\(3k\log k\) 的主系数。本篇不限制更强的实际负估值收益，
也不称原真实 jet 范数达到这个包络。

## 1. 同一个原全格正包络

保持 R583 的原九坐标单项式格、真正饱和前缀及实际 \(w^k\) 行。
其 Gaussian 正成本为
\[
\mathcal G(k)=
\sum_{\substack{p>71\\p\equiv5\ (6)\\p\notin\mathcal S}}
g_p(k)\log p,\qquad
g_p(k)=\left\lfloor\frac{6kp}{p^2-1}\right\rfloor,\qquad k\ge1.
\tag{1}
\]
固定坏集 \(\mathcal S\) 与 R583 相同。
该同篇的实际全素数估计是
\[
\mathcal G(k)=3k\log k+O(k).
\tag{2}
\]
共振吸收后的其余全素数误差为 \(O(k+D)\)；
本篇不重复改变或删除它们。

令 \(s_p=(p+1)/6\)。
对原固定 Euler germ，\(\Pi_0\) 在 \(w\) 级数上准确保留
\(s_p\mid k\) 的行；其它行投影为零。
定义这个正包络的中央子和
\[
\mathcal G_{\rm cent}(k)=
\sum_{\substack{p>71,\ p\equiv5(6),\ p\notin\mathcal S\\s_p\mid k}}
g_p(k)\log p.
\tag{3}
\]
这是一个明确的正数列，不是对 \(j_m\) 或实际 jet 赋值的猜测。

更一般，固定有限个整数仿射式
\[
L_\nu(k)=a_\nu k+b_\nu,\qquad a_\nu\ne0,\quad 1\le\nu\le M,
\tag{4}
\]
其系数及数量均不随 \(p,D,k\) 改变。
记 \(\mathcal G_{\mathcal L}(k)\) 为 (1) 中满足至少一个
\(s_p\mid L_\nu(k)\) 的子和；重复出现的素数只计一次。
该定义包括任何固定有限组行平移。

**定理。**
\[
\boxed{
\mathcal G_{\mathcal L}(k)
=O_{\mathcal L}\!\left(k(1+\log\log(k+3))^2\right)
=o_{\mathcal L}(k\log k).
}
\tag{5}
\]
(3) 是其中 \(L_1(k)=k\) 的特例。

## 2. 一个完整的加权约数估计

对正整数 \(n\)，置
\[
A(n)=\sum_{d\mid n}\frac{\log(6d)}d.
\]
我们先证明
\[
\boxed{A(n)\le C(1+\log\log(n+3))^2.}
\tag{6}
\]

记 \(\sigma_{-1}(n)=\sum_{d\mid n}d^{-1}\)。
对约数的 Euler 乘积逐因子微分，或者直接对各素数指数分组，得
\[
\sum_{d\mid n}\frac{\log d}{d}
=\sigma_{-1}(n)
 \sum_{q^a\parallel n}\log q\,
 \frac{\sum_{e=0}^a e q^{-e}}{\sum_{e=0}^a q^{-e}}.
\]
有限截断几何分布的加权均值不超过无限均值，故
\[
\frac{\sum_{e=0}^a e q^{-e}}{\sum_{e=0}^a q^{-e}}
\le\frac1{q-1}.
\]
于是
\[
A(n)\le \sigma_{-1}(n)
\left(\log6+\sum_{q\mid n}\frac{\log q}{q-1}\right).
\tag{7}
\]

下面把 (7) 的两个因子各估成 \(O(1+\log\log(n+3))\)，
并写出所需的全部范围。
可先吸收有限小 \(n\)，再取 \(y=\log n\ge3\)。
Chebyshev 界 \(\vartheta(t)=\sum_{q\le t}\log q=O(t)\)
由中央二项式给 \(\vartheta(2t)-\vartheta(t)=O(t)\)，再作二进分段得到。
分部求和因此给
\[
\sum_{q\le y}\frac{\log q}{q-1}=O(\log y).
\tag{8}
\]
而 \(q>y\) 的整除素数满足
\[
\sum_{\substack{q\mid n\\q>y}}\frac{\log q}{q-1}
\le\frac2y\sum_{q\mid n}\log q\le2.
\tag{9}
\]
所以 (7) 的括号为 \(O(\log y)\)。

为自含地支付另一个因子，令 \(\delta=1/\log y\)。
由 \(1-q^{-\delta}\le\delta\log q\) 及 (8)，
\[
\log\frac{\prod_{q\le y}(1-q^{-1})^{-1}}
               {\prod_{q\le y}(1-q^{-1-\delta})^{-1}}
\le
\delta\sum_{q\le y}\frac{\log q}{q-1}=O(1).
\]
又
\[
\prod_{q\le y}(1-q^{-1-\delta})^{-1}
\le\zeta(1+\delta)\le1+\delta^{-1}=1+\log y.
\]
故
\[
\prod_{q\le y}(1-q^{-1})^{-1}=O(\log y).
\tag{10}
\]
大素数部分则有
\[
\log\prod_{\substack{q\mid n\\q>y}}(1-q^{-1})^{-1}
\le2\sum_{\substack{q\mid n\\q>y}}\frac1q
\le\frac2{y\log y}\sum_{q\mid n}\log q
\le\frac2{\log y}.
\tag{11}
\]
合并 (10)–(11)，
\(\sigma_{-1}(n)\le\prod_{q\mid n}(1-q^{-1})^{-1}=O(\log y)\)。
代入 (7)，即得 (6)。
该证明不借对 \(n\) 的平均估计，适用于每一个实际行指标。

## 3. 原素位子和化为同一行指标的约数和

若 \(g_p(k)>0\)，则 \(p^2-1\le6kp\)，所以 \(p\le6k\)。
因此 (1) 的所有和实际上有限，没有隐藏的无限小素位尾。

写 \(p=6d-1\)，则对 \(d\ge1\)
\[
g_p(k)\log p
\le \frac{6kp}{p^2-1}\log p
\le C k\,\frac{\log(6d)}d.
\tag{12}
\]
先取单个非零整数 \(n=L_\nu(k)\)。
相应的中央条件只是 \(d\mid |n|\)；
放宽素数条件和固定坏集只会增加这个正和。
所以由 (6)、(12)
\[
\sum_{\substack{p\ {\rm in}\ (1)\\s_p\mid n}}
g_p(k)\log p
\le Ck\sum_{d\mid |n|}\frac{\log(6d)}d
\le Ck(1+\log\log(|n|+3))^2.
\tag{13}
\]
对固定仿射式且充分大的 \(k\)，
\(|L_\nu(k)|\) 与 \(k\) 只差固定的常数倍，
因此 (13) 为定理 (5) 所写的量。

每个 \(L_\nu\) 最多有一个整数零点。
若在某个正整数 \(k\) 处为零，相应的素位条件确实全部成立，
但这样的 \(k\) 只有固定有限多个；
(1) 在这些实际行上的有限值可吸收入依赖 \(\mathcal L\) 的常数。
其余有限小 \(k\) 同样处理。
最后对固定有限个 \(\nu\) 求和，允许上界重复计数，即得 (5)。

证明没有将 \(p=6d-1\) 的素数性当作额外独立随机条件；
仅用真实的整除条件已经足够。

## 4. 删除这些正成本后，主系数仍为三

将 (2)、(5) 合并：
\[
\boxed{
\mathcal G(k)-\mathcal G_{\mathcal L}(k)
=3k\log k+
O_{\mathcal L}\!\left(k(1+\log\log(k+3))^2\right).
}
\tag{14}
\]
因此若一个步骤只把 (4) 所列中央行的既有 Gaussian 正成本
从 \(g_p(k)\log p\) 改为零，剩余正包络的 \(k\log k\) 主系数仍为三。
这在每一个真实 \(k\) 上成立，不需假定饱和跳跃 \(k\) 接近 \(D^9\)。

R639 的完整规范连接确实给同一个原中央条件的更大解析盘。
对一个固定原 germ，\(\Pi_0\) 仍准确只观察
\[
k\equiv0\pmod{s_p}.
\]
有限个固定单项式平移只会改为 (4) 中有限个固定余类。
所以仅把这些行从 R583 的正包络中删除，
没有支付原九格全饱和预算中 \(b_I<7/3\) 的严格门。

这里须区分三个不同量：

- (14) 是原已知正包络的准确子和计算；
- 原真实 \(\log\|\varphi_D^k\|_p\) 可远小于该上界；
- 若新算术关系给出更强负估值、整个来源的饱和传播或
  随 \(D\) 增长但已付成本的一族新余类，必须按其真实量词另算。

本篇没有证明这些更强输入不存在，
也没有把它们的可能收益限制为 (12)。
特别 (5) 的“固定有限”不能被改为任意 \(D\) 个行条件而仍保同一个常数。

## 5. 当前全格接口

原九格继续具有 R579 的普通
\(3k\log D+O(k+D)\)，
R583 的惰性
\(3k\log k+O(k+D)\)，
以及原复侧
\(-3k\log k+3k\log D+O(k+D)\)。
九个实际坐标与真实饱和旗标不变，严格充分门仍为
\(a_I+9b_I<21\)。

R639 的真实整体规范、R641 的准确边界、
R642 的旧第三精度整运输，可以用于寻找更强的原来源关系；
(14) 明确了只处理固定几条中央行的那一步尚未贡献主系数下降。
下一项需要的仍是同一原多项式来源、全部次数帽和完整前缀上的
算术传播，或者直接证明指定中央非零。

## 依赖

- [R583](R583-nine-coordinate-inert-resonance-absorption-and-sharp-envelope.md)：
  原全格包络 (1)–(2)、共振分母吸收及全部真实 \(D/k\) 量词。
- [R579](R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md)、
  [R581](R581-nine-coordinate-truncated-denominators-and-forced-large-inert-jets.md)：
  同格普通成本、完整饱和累计与真正全层 cutoff 接口。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)、
  [R641](R641-complete-central-remainders-exact-boundary-and-full-linear-span.md)、
  [R642](R642-complete-central-remainder-and-original-third-precision-unit.md)：
  完整中央规范及其已付解析、来源和旧目标范围。

加权约数估计已在 §2 全参数证明。本篇不增加素数扫描，
不以包络计算替代原固定曲线的无穷素数结论。
