# R150：一般等权孤立均值 y=0 整支的原有理数返回

日期：2026-11-27（Asia/Taipei）；Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明：** 原一般 LS 的 $b=c$ 图上，整个 $y=0$ 分支没有物理解。没有附加 $Q=1-u$、$\Delta=0$ 或 W=0 条件；不声称一般等权或普通 ISP 已完成。

## 1. 与已付原图的准确联系

沿用[等权首一二次图](R150-appendix-unit211-equal-weights-two-parameter-monic-value-quadratic.md)与[三原 N/P 多项式](R150-appendix-unit211-equal-weights-same-value-linear-remainders-and-six-projections.md)。
$y=0$ 即 $v=2y-1=-1$，故
$$
\kappa=1-Q,\quad \omega=-z,\quad
A=\kappa+\omega^2-2\omega,\quad
m=\frac{(\omega-1)(\omega-\kappa)}{A}.
$$
所有原点仍有
$$
\kappa\omega(\omega-1)(\omega-\kappa)(\kappa-1)A\ne0.
\tag{1.1}
$$
这来自原物理单位和此前完整的 $y=1$、$A_m=0$、$v=0$ 排除，没有预先把本页目标 $v+1$ 当成单位。

记原三元多项式为 $\mathcal F_N,\mathcal F_S,\mathcal F_P$。本页直接代入 $v=-1$，保留其全部系数；不将不同原方程分别放到不同的值根上。

## 2. 原均值成为首一四次式

两原均值的共同返回为 $E=\alpha v^2+\beta$，因此本支取
$$
G=2(\alpha+\beta).
$$
直接原返回给
$$
\begin{aligned}
G={}&\kappa^4+(2\omega^2-6\omega)\kappa^3\\
&+(\omega^4-2\omega^3+4\omega^2+4\omega-1)\kappa^2\\
&+(-4\omega^4+4\omega^3-6\omega^2+2\omega)\kappa
+3\omega^4-2\omega^3.
\end{aligned}
\tag{2.1}
$$
它在 $\mathbf Q[\omega][\kappa]$ 中首一，故对全部 $\omega$ 都可作四次余式，不丢首项零纤维。

对三条原 $\mathcal F_i|_{v=-1}$ 完整除以 G。剥除下列已付因子后，将余式记为 $N,S,P$：
$$
\begin{aligned}
\mathcal F_N|_{v=-1}&=q_N G+2(\kappa-1)N,\\
\mathcal F_S|_{v=-1}&=q_S G+2(\omega-1)^2(\kappa-1)S,\\
\mathcal F_P|_{v=-1}&=q_P G+2(\omega-1)^3(\kappa-1)P.
\end{aligned}
\tag{2.2}
$$
三式的完整商与余式均由原多项式除法逐项乘回。它们关于 $\kappa$ 的次数全为 2，关于 $\omega$ 的次数分别为 6、14、16，项数为 15、39、45。

具体第一式有 $q_N=-3\kappa+4\omega^2-15\omega+4$，且
$$
\begin{aligned}
N={}&(-2\omega^4+23\omega^3-41\omega^2+18\omega-2)\kappa^2\\
&+(-2\omega^6+13\omega^5-33\omega^4+53\omega^3-27\omega^2+4\omega)\kappa\\
&+6\omega^6-27\omega^5+21\omega^4-4\omega^3.
\end{aligned}
$$
$S,P$ 的完整定义就是 (2.2) 的原首一除法与所列规范，不依赖大缓存或数值插值。

## 3. 三个完整六阶结式

计算原固定次数 $4,2$ 的完整 6×6 Sylvester 行列式
$$
R_N=\operatorname{Res}_\kappa(G,N),\quad
R_S=\operatorname{Res}_\kappa(G,S),\quad
R_P=\operatorname{Res}_\kappa(G,P).
$$
实现使用 $\mathbf Q[\omega]$ 上的 Bareiss 消去，每次整除都实际乘回。原解必使三个行列式为零；并未倒置 N/S/P 的二次首项。

完整特征零次数为 26、55、62。仅剥除 (1.1) 的 $\omega,\omega-1$ 后得到首一多项式 $r_{12},s_{34},p_{38}$：
$$
R_N=256\omega^8(\omega-1)^6r_{12},\quad
R_S=-384\omega^{13}(\omega-1)^8s_{34},
$$
$$
R_P=-384\omega^{15}(\omega-1)^9p_{38}.
\tag{3.1}
$$
全部因子整除均乘回，没有用模因子重建猜测实际重数。作为原完整覆盖的明确小核对，
$$
\begin{aligned}
r_{12}={}&\omega^{12}-\frac{15}4\omega^{11}
+\frac{17}8\omega^{10}+\frac{449}8\omega^9
-\frac{2261}{16}\omega^8-\frac{629}2\omega^7
+\frac{1669}4\omega^6\\
&+\frac{557}4\omega^5-\frac{3091}8\omega^4
+\frac{857}4\omega^3-\frac{435}8\omega^2
+\frac{53}8\omega-\frac5{16}.
\end{aligned}
$$

## 4. 完整 QQ Bézout 给矛盾

实际在 $\mathbf Q[\omega]$ 中对 $r_{12},s_{34}$ 计算完整扩展 Euclid，得到次数 33、11 的 $a,b$，并逐项乘回
$$
a(\omega)r_{12}(\omega)+b(\omega)s_{34}(\omega)=1.
\tag{4.1}
$$
加入第三个原结式仍得同一个常数 1，第三乘子为零。这里记录的是整个有理多项式身份，不只是 gcd 次数或软件的成功标记。

任一原点由 (3.1) 和已付 $\omega(\omega-1)\ne0$ 必满足 $r_{12}=s_{34}=0$，与 (4.1) 矛盾。所以整个 $v=-1$ 分支排除。事实上本页无需使用原 $D_{\rm val}$ 的饱和，较少的原必要方程已经给出矛盾。

结合此前 $v=1$ 分支，后续等权图可使用
$$
v^2-1\ne0,\qquad \alpha+\beta=-\alpha(v^2-1)\ne0.
$$
这项新的纯参数单位只在本页完整排除后支付。

## 5. 源与实际执行

三段自含精确算术函数体位于 notes：

- 2026-11-27-unit211-equal-weight-vminusone-original-fiber-8542.js；
- 2026-11-27-unit211-equal-weight-vminusone-original-resultants-8542.js；
- 2026-11-27-unit211-equal-weight-vminusone-original-Bezout-8542.js。

第一段接受已提交三参数原行输出，第二段接受第一段输出，第三段接受第二段输出；以 new Function(source)(input,...) 调用。原输入的全部依赖见前两份正式正文，不读取 scratch 缓存。小执行 JSON 保存精确源哈希及规范输出哈希；可重算的大系数与 Bézout 缓存不入库。

实际 V8 时间分别为 0.095、0.191、27.241 秒，全部正常返回；没有 OS 子进程退出码或 RSS，回执如实为空。一般等权的新 QQ 任务 run 45940118594 是另一个尚在运行的输入，本页不依赖其结论，也不把它提前记成功。其余一般图和完整算子桥继续。
