# 实际 Cartan 的阶三 Möbius 协变与完整卷积包的准确边界

日期：2026-11-12；课题：Serre uniformity；临时研究笔记，未登记新的 R 结果。

本笔记继续已保存的 `cartan-mobius-cyclic-module-resume2`。它给出一个在实际小惯性分支中确实成立的、更专门的阶三协变，并检验能否与全部纯 Gauss／二维卷积恒等式合用，排除三色 Fourier 共同零点。结论是：**这组加强后的恒等式仍不足够。** 下面的精确反模型不是真实 Cartan 特征，也不是实际 exceptional 素数反例；它明确违反了一个尚未使用的 Cartan 乘法关系。

全部证明为下述有限域计算及代数推导；没有把未发表的无 exceptional 猜想作为输入。

## 1. 实际小惯性分支中的阶三关系

设素数 $p>3$ 满足
$$p\equiv2\pmod3,\qquad v_3(p^2-1)=1.$$
后一个条件正是现有实际小惯性分支所使用的条件，即 $p\equiv2,5\pmod9$。令
$$F=\mathbb F_{p^2}=\mathbb F_p(\tau),\qquad\tau^2=-3,$$
并令 $\chi:F^\times\to\mu_3$ 为非平凡三次角色。因为 $3\nmid p-1$，它在 $\mathbb F_p^\times$ 上平凡；又因 $\tau^2\in\mathbb F_p^\times$，有 $\chi(\tau)=1$。

定义项目直线上的实际颜色函数
$$f(b)=\chi(1+b\tau)\quad(b\in\mathbb F_p),\qquad f(\infty)=1.$$
置 $\zeta=\chi(1+\tau)$。元素 $(1+\tau)/2$ 在 $F^\times$ 中有阶六，而 $v_3(p^2-1)=1$，故 $\zeta$ 是本原三次单位根。

下列三个置换均作用于整个 $\mathbb P^1(\mathbb F_p)$：
$$T(b)=\frac{b+1}{1-3b},\qquad W(b)=-\frac1{3b},\qquad R(b)=-b.$$
按通常规则处理极点及无穷远点。它们满足
$$T^3=W^2=R^2=1,\quad TW=WT,\quad RTR=T^{-1},\quad RWR=W,$$
且 $\langle T,W\rangle$ 是阶六的 Cartan 子群。实际颜色满足
$$\boxed{f(Tb)=\zeta f(b),\quad f(Wb)=f(b),\quad f(Rb)=f(b)^{-1}.}\tag{1.1}$$

第一式来自
$$1+T(b)\tau=\frac{(1+b\tau)(1+\tau)}{1-3b}.$$
分母在基域，角色值为一。极点 $b=1/3$ 给 $f(1/3)=\zeta^{-1}$；在 $b=\infty$，有 $T\infty=-1/3$ 和 $f(-1/3)=\zeta$，故没有漏掉项目端点。其余两式分别由 $\chi(\tau)=1$、以及
$$(1+b\tau)(1-b\tau)=1+3b^2\in\mathbb F_p^\times$$
得出。

$T$ 没有有理不动点，因为不动点需要 $3b^2=-1$，而 $-3$ 在 $\mathbb F_p$ 中非平方。因此每个 $T$ 轨道有三个元素，且三种颜色恰各出现一次。记 $m=(p+1)/3$，则项目直线上各色恰有 $m$ 点；有限直线上三色大小为 $m-1,m,m$，因为 $\infty$ 的颜色为一。

这确实比只要求三色平衡、$W$ 不变及 $R$ 取逆更强。另一方面，(1.1) 只使用了阶六 Cartan 子群，不是整个阶 $p+1$ Cartan。

## 2. 这些条件自动给出全部二维纯 Gauss 与卷积恒等式

本节不要求 $f$ 是实际角色。只假设
$$f:\mathbb P^1(\mathbb F_p)\to\mu_3$$
满足 (1.1) 和 $f(\infty)=1$。把它齐次延拓到 $F$：
$$\Phi(0)=0,\qquad \Phi(a+b\tau)=f(b/a)\ (a\ne0),\qquad\Phi(b\tau)=f(\infty)\ (b\ne0).$$
则 $\Phi$ 在每条非零 $\mathbb F_p$ 射线上常值。令 $\Phi^{-1}(0)=0$，在非零处取倒数。由于 $T$ 三循环，所有项目方向的值之和为零。

在任意含本原 $p$ 次和三次单位根、且 $3p$ 可逆的域 $k$ 中，选非平凡加性角色 $\psi:\mathbb F_p\to k^\times$，定义
$$\mathcal Fh(u)=\sum_{v\in F}h(v)\psi(\operatorname{Tr}_{F/\mathbb F_p}(uv)).$$
对 $u\ne0$，线性形式 $v\mapsto\operatorname{Tr}(uv)$ 的核是项目方向 $\tau/u$。对这条射线，非零标量和为 $p-1$；对其余每条射线，该和为 $-1$。所以
$$\mathcal F\Phi(u)=p\Phi(\tau/u).$$
若 $u$ 的方向是 $b$，$\tau/u$ 的方向是 $1/(3b)=RW(b)$。由 (1.1)，$\Phi(\tau/u)=\Phi(u)^{-1}$。原点处双方都为零。因此
$$\boxed{\mathcal F\Phi=p\Phi^{-1},\qquad \mathcal F\Phi^{-1}=p\Phi.}\tag{2.1}$$

同时，$\Phi^3=1-\delta_0$。令星号表示 $F$ 的加法卷积。Fourier 变换将卷积化为逐点乘法，且 $p$ 可逆，故
$$\boxed{
\Phi*\Phi=p\Phi^{-1},\qquad
\Phi^{-1}*\Phi^{-1}=p\Phi,\qquad
\Phi*\Phi^{-1}=p^2\delta_0-1.
}\tag{2.2}$$
例如在 $1\in F$ 处，第一式给出完整 Jacobi 和
$$\sum_{v\in F}\Phi(v)\Phi(1-v)=p.$$
这些结论全部由 (1.1) 导出。因而不能用它们反过来宣称 $\Phi$ 已是乘法角色。

## 3. 一个同时保留阶三协变的严格共同零反模型

取
$$p=263,\qquad\ell=1579=6p+1,\qquad\xi=64\in\mathbb F_{1579}^\times.$$
二者均为素数，$\xi$ 的阶为 $263$。并且
$$v_3(p^2-1)=1,\quad\ell\equiv1\pmod p,\quad\ell\nmid3p(p^2-1),\quad\ell\equiv1\pmod3.$$
所以它保留实际 Tate 素数所要求的 $\ell\equiv\pm1\pmod p$ 以及所有有限群阶的可逆性，甚至满足商域为 $\mathbb Q(\sqrt{-3})$ 时两个 Frobenius 符号必须相同的附加条件。令 $\zeta$ 为 $\mathbb F_{1579}$ 中任意一个本原三次单位根。

标准库脚本 `verify_mobius_cubic_countermodel.py` 如下构造函数 $\widetilde f$。

1. 从实际 $\chi(1+b\tau)$ 开始。实际 $\chi(1+\tau)$ 在 $\mathbb F_{263^2}$ 中为 $131+131\tau$，用它统一标记三颜色。
2. 将 $\mathbb P^1(\mathbb F_{263})$ 分成 $\langle T,W\rangle$ 的 $44$ 个六元轨道。
3. 反射 $R$ 固定其中两个轨道，其余轨道配成 $21$ 对。在每一对上，分别将颜色加上 $a$ 和 $-a\pmod3$；自配对轨道不改色。这样准确保留 (1.1)、$f(0)=f(\infty)=1$、反射取逆和三色大小。
4. 在 $21$ 个三值变量中用精确有限环加法求一个共同零解。脚本按确定的字典序分成 $10+11$ 个变量计算；计算环 $\mathbb F_\ell[z]/(z^2+z+1)$ 是两个 $\mathbb F_\ell$ 的直积，零二元坐标准确表示对两个三次单位根的共同零。这只是给出一个可复验的反模型，不是经验搜索实际 exceptional 素数。

完整三个颜色集合保存于 `cartan_order_three_countermodel.json`，有限直线上的大小分别为 $87,88,88$。直接整数模运算给
$$\boxed{\sum_{\widetilde f(b)=\zeta^j}\xi^b=0\quad\text{in }\mathbb F_{1579},\qquad j=0,1,2.}\tag{3.1}$$
于是两条三色 Fourier 和也同时为零。由于 $\ell\equiv1\pmod3$ 且 $\xi\in\mathbb F_\ell$，所有单位根及两条和都被 $\ell$ 次 Frobenius 固定；计算没有使用一个与实际剩余域不相容的独立形式变量。

上述 $\widetilde f$ 严格满足整个 (1.1)，所以其齐次延拓还满足 (2.1)–(2.2) 的全部恒等式。可复验文件的输出同时记录真正的 Cartan 颜色在同一 $\xi$ 处的三组和为
$$1003,\quad382,\quad194\pmod{1579};$$
它们并未共同消失。

### 3.1 明确指出它缺少哪条实际乘法关系

实际完整 Cartan 要求对每个 $t\in\mathbb F_p$ 都有
$$g_t(b)=\frac{b+t}{1-3tb},\qquad f(g_t b)=f(t)f(b).\tag{3.2}$$
反模型在 $t=b=2$ 时失败：
$$g_2(2)=167\pmod{263},$$
而三个颜色指数分别是
$$\operatorname{col}(2)=1,\quad\operatorname{col}(2)=1,\quad\operatorname{col}(167)=0.$$
式 (3.2) 应要求最后的指数为 $2$，却是 $0$。因此这绝不是实际 Cartan 特征，也不能据此声称 $1579$ 是本课题的 exceptional 素数。

## 4. 对下一步的准确含义

已经严格验证的加强包包括：实际小惯性的 $3$ 进量词、真正阶三 Möbius 轮换、反演不变、反射取逆、三色大小、$\Phi^3$、完整二维 Gauss 变换、全部二元加法卷积／Jacobi 恒等式，以及 Tate 型的剩余域 Frobenius。这些条件的合取仍不能推出一维受限 Fourier 和没有共同零。

下一步必须真正使用 (3.2) 中阶六子群以外的乘法作用，不能只继续组合 (1.1)、(2.1)、(2.2)。先前 cyclic-module 笔记的精确剩余缺口依然是：若 $M$ 是两个实际颜色特征的所有加法平移之张成空间，证明其在 $W$ 下不变（等价于所需非零投影），或者给出一个与该不变性独立的整系数 Bezout 恒等式。

本笔记不把这个等价改写当作已经解决，不登记 R122，也不扩展为实际 exceptional 素数计算表。它只阻止重复走一条已经有严格反模型的加强路线。

复验：

```sh
python topics/serre-uniformity/notes/verify_mobius_cubic_countermodel.py
```

输出可与 `topics/serre-uniformity/notes/cartan_order_three_countermodel.json` 逐字节对照；程序同时验证全部项目端点、所有 $T,W,R$ 关系、三色大小、三组共同零，以及 (3.2) 的明确失败点。
