# R171. 真实 theta 图的非线性传播与全源共同次数块

日期：2026-11-12。**状态：已证明第一完整带及全部源的准确公式；
未证明全深度的严格惰性预算。**

令 $a=\vartheta^4$、$b=\sigma^4=sa$、
$t(s)=\log a=W(s)/17$。用真正逆参数写 $a=f(b)$。
源 $a^jb^i$、$i+j\le D$ 与标准 $(a-1),b$ 源整等距。

## 1. 原全部列的一个共同公式

若 $n=k-i>0$、$d=i+j$，则
$$
 [b^k]b^if(b)^j=
 \begin{cases}
 \displaystyle\frac j{d-k}[s^{k-i}]e^{(d-k)t},&d\ne k,\\[4pt]
 \displaystyle j[s^j]t,&d=k.
 \end{cases}
 \tag{1}
$$
固定总次数 $d$ 的全部列使用同一指数 $d-k$。
$n=0$ 时值为一，$n<0$ 或 $j=0,n>0$ 时值为零。

## 2. 下一 Gaussian 共振之前的实际传播

设 $p=4r-1\ge7$，$\tau_p=p[s^r]t\bmod p$。
R160 给 $\tau_p\ne0$ 且 $v_p(t_m)\ge-1$ 对所有 $m<p^2$ 成立。
对全部 $j\ge0$、$n<pr$ 有
$$
                v_p([b^n]f^j)\ge-\lfloor n/r\rfloor.
 \tag{2}
$$
因此同一原整源及其真实饱和前缀满足
$\log\|\varphi_D^k\|_p\le\lfloor k/r\rfloor\log p$，$k<pr$。

每个整带起点还有准确式
$$
 \boxed{\quad
 p^h[b^{hr}]f^j\equiv
       \frac{j(j-hr)^{h-1}}{h!}\tau_p^h\pmod p,
             \qquad1\le h<p.
 \quad}\tag{3}
$$
$h=1$ 的零次幂按一处理。因而对 $j=1$，除了 $h=4$，
这些系数的赋值均准确为 $-h$；$h=4$ 的下界改为 $-1$。
特别 $p^2[b^{2r}]f\equiv\tau_p^2/4\ne0$。

所以首个坏项的线性剪切并未自动移除其后的非线性分母。
反之，一个指定坐标的这些非零系数也不能作为饱和前缀的
范数下界。原两条中央零性读取的是 R169 的更低 amplitude，
没有改变这里始终非零的 $\tau_p$。

## 3. 全带及原混合源的共同主行

令 $k=hr+e$、$1\le h<p$、$0\le e<r$。真正周期满足
$p\log a\equiv\tau_p s^r\mathcal L(s)\pmod{p,s^{2r}}$。
对任一齐次源 $H(a,b)=a^dR(b/a)$，准确有
$$
 p^h[b^k]H(f(b),b)\equiv
 \frac{\tau_p^h(d-k)^{h-1}}{h!}
 [s^e]a^{d-k}\mathcal L^h(dR-sR')\pmod p.
 \tag{4}
$$
$d-k\equiv0$ 及 $d=k$ 都包含在内，$h=1$ 的零次幂仍按一处理。
原列 $A_2^jV^c$ 对应 $d=17j$、$R=P^jV^c$，所以 $j+c>e$
的列在此最高分母层自动消失。这保留了同一实际全源，不把
支撑限制升级为尚未证明的饱和范数改善。

完整证明及有限校准见
[首共振传播与共同块](../notes/2026-11-12-theta-graph-nonlinear-propagation-and-common-blocks.md)。
[准确脚本](../scripts/check-theta-graph-first-propagation.py) 使用真实逆级数，
核对 $p=7,11$ 的全 $n<pr$、全 $hr+e$ 带及
$j=0,1,2,3,5,17,34$；它不承担一般证明。
