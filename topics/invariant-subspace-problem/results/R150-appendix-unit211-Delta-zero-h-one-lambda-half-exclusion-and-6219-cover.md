# R150：Delta=0、h=1 的整个 lambda=1/2 分支排除及 6219 基点覆盖

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 原范围与结论

在[原 Delta=0、h=1 首一 ell 三次图](R150-appendix-unit211-Delta-zero-h-one-monic-cubic-original-unit-and-degree-49-curve.md)中，整个 lambda=1/2 分支不存在原点。证明是下面的原权恒等式，并只使用此前已付的原 T0=0 和等权排除。没有以另一个 Phi=0 图的结论代替本图。

结合[原消元式完整 QQ 分解](R150-appendix-unit211-Delta-zero-h-one-exact-factorization-and-6229-point-cover.md)，当前有序 h=1 图的不同 (lambda,rho) 基点界因此从 6229 收为 **6219**。原 ell 三次、原自由变量 t 与完整八条原行继续保留。

## 2. lambda=1/2 时的精确原数据

沿用原 p=1+rho、q=1-rho、Q=pq。原 rho,p,q,b,c 都非零。lambda=1/2 时，原矩给

$$A_2=\tfrac12,\quad B_3=-\tfrac12,\quad
\xi=-1,\quad c=\tfrac12,\quad b=\ell-\tfrac12,$$

$$S=1,\qquad \zeta=-\frac p{2\rho},\qquad
v_1=\frac1{2\rho},\qquad u=p\ell-\rho.$$

原权式为

$$T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q=T_0+2\ell Q,$$

$$\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),$$

$$N_F=(3-4\lambda)Q+S(2uQv_1+\zeta J),\quad
\Delta=\Phi N_F-S\zeta P_f.$$

直接代入且使用 u-pell=-rho，得到

$$\begin{aligned}
N_F
&=Q+\frac{2uQ-pJ}{2\rho}\\
&=Q+\frac{2(u-p\ell)Q-pT_0}{2\rho}
=-\frac{pT_0}{2\rho}=\zeta T_0. \tag{2.1}
\end{aligned}$$

又因 u-1=p(ell-1) 及 2-q=p，

$$\begin{aligned}
\Phi-(J-Q)
&=4(u-1)+2Q(1-\ell)\\
&=(4p-2Q)(\ell-1)
=2p^2(\ell-1). \tag{2.2}
\end{aligned}$$

所以完整原身份为

$$\boxed{\ \Delta
=-\frac{p^3}{\rho}\,(\ell-1)T_0.\ } \tag{2.3}$$

没有在推导中除以 Pf、Phi、Delta 或任何新的参数多项式。

## 3. 所有原零因子的返回

由于 p,rho 为原单位，Delta=0 迫使 ell=1 或 T0=0。

- ell=1 时 b=c=1/2，落入已刊[整个等权原排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)。
- T0=0 时使用已刊[一般 T0 原排除](R150-appendix-unit211-general-T0-zero-complete-original-exclusion.md)。

这里核清第二项的实际适用域：T0 覆盖的前两步用了物理 D 为单位。在当前 h=1 碰撞图，原矩精确给

$$D=\ell A_2-T^2=bA_2,\qquad T=A_2^2/B_3,$$

而 bA2 非零，所以该已付排除确实适用于本稿。**没有把这种 D 单位外推到 h=k 非 1 的碰撞图；后者 D=0，仍独立保留全部尚未返回的权面。**

两分支均矛盾，完成整个 lambda=1/2 纤维排除。B/C 原标签交换给对应有序 k=1 图的同一结论。

## 4. 原必要覆盖删去该整纤维

已实际付出的完整 QQ 因式身份为

$$G_{389}=a_0(2\lambda-1)^2J_{387},\qquad a_0\in\mathbb Q^\times,$$

其中 J387 的双次数为 (306,81)，而另一条原必要曲线 F49 的双次数为 (39,10)。前次实际因式运行已核 gcd(F49,J387)=1。

本稿支付 2lambda-1 在当前原图非零，所以每个剩余原点满足

$$F_{49}(\lambda,\rho)=J_{387}(\lambda,\rho)=0.$$

固定 rho 次数 10、81 的 Sylvester 非零行列式 R 有

$$\deg_\lambda R\le81\cdot39+10\cdot306=6219.$$

任一 lambda 纤维的 r 个不同 rho 根给固定 Sylvester 的 r 个独立幂向量核列，所以该行列式在此处的消失重数至少 r。互素排除共同垂直整线，故求和得到至多 6219 个不同基点。这个证明保留原首项为零的所有有限纤维，未展开大的 QQ 结式。

每个基点的原 ell 至多三个，因此不同 (lambda,rho,ell) 投影点至多 18657 个。原自由 t 未因此被消去；完整原解集未被宣称有限或排空。

本稿的新增证明为 (2.1)–(2.3) 及已付原零因子的完整返回；无需再执行旧曲线分解或完整 Gram 门。一般 h=k、其它 Delta 面、R150 与 ordinary ISP 继续开放。
